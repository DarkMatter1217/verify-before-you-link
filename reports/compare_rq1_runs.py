#!/usr/bin/env python3
"""Compares the two RQ1 runs: Rahul's laptop (the main result) and the Colab GPU (the second run).

For each configuration and project it reports:
- the code files retrieved for the requirements (the candidate pairs) that both runs share;
- how many yes/no decisions are the same, over the candidate pairs both runs share;
- the overlap of the accepted links (Jaccard: shared links / links in either run);
- the average F1 over the three projects, on all requirements and on the test slice of RQ2/RQ3.

    python3 reports/compare_rq1_runs.py [--out reports/rq1-laptop-vs-colab.md]
"""

import argparse
import glob
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "harness"))
import evaluate  # noqa: E402
import lissa_compat as lc  # noqa: E402

RUNS = {"laptop": ROOT / "LiSSA-RATLR-V2/lissa/results-local/rq1-laptop",
        "Colab": ROOT / "LiSSA-RATLR-V2/lissa/results-local/rq1"}
PROJECTS = ["SMOS", "eTour_en", "iTrust"]
CONFIGS = [("qwen2.5-coder-14b", "simple", "KISS"), ("qwen2.5-coder-14b", "reasoning", "chain-of-thought"),
           ("llama3.1-8b", "simple", "KISS"), ("llama3.1-8b", "reasoning", "chain-of-thought")]


def links(run, project, kind):
    """Accepted links of one run; kind is 'no_llm' (retrieval only: every candidate pair) or e.g. 'reasoning_ollama_x'."""
    files = [f for f in glob.glob(str(RUNS[run] / f"traceLinks-{project}_*artifact_{kind}_bge-m3.json_*.csv"))]
    if len(files) != 1:
        raise SystemExit(f"Expected one traceLinks file for {run} {project} {kind}, found {len(files)}")
    return lc.read_trace_links(files[0])


def average_f1(predicted, slice_name):
    rows = evaluate.evaluate(predicted, slice_name)["projects"]
    return next(row["f1"] for row in rows if row["project"] == "Avg.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", help="also write the tables to this Markdown file")
    args = parser.parse_args()

    candidates = {run: {p: links(run, p, "no_llm") for p in PROJECTS} for run in RUNS}
    out = ["# RQ1: laptop run vs Colab run", "",
           "- **Laptop (main result):** MacBook Pro, Apple M5 Pro, 24 GB; Ollama 0.40.14; finished 17 Nov 2026.",
           "- **Colab (second run):** NVIDIA L4; Ollama 0.40.2; finished 15 Nov 2026. RQ2/RQ3 use this run's "
           "candidate pairs (`harness/data/candidates-rq1.json`).",
           "- Same models (same digests, Q4_K_M), same LiSSA code and settings (temperature 0, seed 133742243, "
           "context 16,384 tokens, answers up to 4,096 tokens). The hardware and the Ollama version differ together, "
           "so their effects cannot be separated.", "",
           "## Retrieval: candidate pairs (bge-m3, top 20)", "",
           "| Project | Pairs per run | Shared | Shared share |", "|---|---|---|---|"]
    for p in PROJECTS:
        a, b = candidates["laptop"][p], candidates["Colab"][p]
        out.append(f"| {p} | {len(a):,} | {len(a & b):,} | {len(a & b) / len(a):.1%} |")

    out += ["", "## Decisions and links", "",
            "Same decisions: yes/no answers that agree, over the candidate pairs both runs share. "
            "Link overlap: links accepted by both runs / links accepted by either (Jaccard). "
            "For comparison, GPT-4o's own runs with three seeds overlap 0.79–0.88.", "",
            "| Model | Prompt | Project | Links laptop / Colab | Same decisions | Link overlap |",
            "|---|---|---|---|---|---|"]
    f1_rows = []
    for model, prompt, label in CONFIGS:
        kind = f"{prompt}_ollama_{model}"
        found = {run: {p: links(run, p, kind) for p in PROJECTS} for run in RUNS}
        for p in PROJECTS:
            a, b = found["laptop"][p], found["Colab"][p]
            shared = candidates["laptop"][p] & candidates["Colab"][p]
            differ = len((a ^ b) & shared)
            out.append(f"| {model} | {label} | {p} | {len(a):,} / {len(b):,} | {1 - differ / len(shared):.1%} | "
                       f"{len(a & b) / len(a | b):.3f} |")
        f1_rows.append((model, label, *(average_f1(found[run], s) for s in ("all", "test") for run in RUNS)))

    out += ["", "## Average F1 over the three projects (LiSSA's strict rule)", "",
            "| Model | Prompt | All requirements: laptop | Colab | Test slice: laptop | Colab |",
            "|---|---|---|---|---|---|"]
    for model, label, all_laptop, all_colab, test_laptop, test_colab in f1_rows:
        out.append(f"| {model} | {label} | {all_laptop:.3f} | {all_colab:.3f} | {test_laptop:.3f} | {test_colab:.3f} |")
    out += ["", "The test slice has 205 of the 256 requirements (see `harness/data/split.json`). The RQ2/RQ3 baseline is "
            "LiSSA's chain-of-thought prompt asked again by our harness on Colab; on the test slice it scores 0.249 with "
            "Qwen (`harness/runs/baseline__qwen2.5-coder-14b__colab-l4__test`)."]
    text = "\n".join(out) + "\n"
    print(text)
    if args.out:
        pathlib.Path(args.out).write_text(text)


if __name__ == "__main__":
    main()
