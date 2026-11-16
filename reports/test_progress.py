#!/usr/bin/env python3
"""Prints the test-slice results so far as a Markdown table, for the timeline in reports/test-timeline.md.

For every test run folder that exists, it shows how many requirements have been scored, the average precision,
recall and F1 (LiSSA's strict answer rule), F1 per project, the same after verification at the frozen tau 0.2,
and GPT-4o's average F1 on exactly the same requirements (LiSSA's three seeds), so partial results are compared
fairly while the run is still going.

    python3 reports/test_progress.py [--runs PATH/TO/harness/runs]
"""

import argparse
import csv
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "harness"))
import evaluate  # noqa: E402
import lissa_compat as lc  # noqa: E402

MODELS = ("qwen2.5-coder-14b", "llama3.1-8b")
CONFIGS = ("baseline", "definition", "summary", "project", "examples", "definition+summary")
BEST = {"qwen2.5-coder-14b": "examples", "llama3.1-8b": "definition+summary"}
TAU = "0.2"
GPT4O = REPO / "LiSSA-RATLR-V2" / "lissa" / "results-r2c"
SEEDS = ("133742243", "35418170", "83939039")


def average(rows):
    return next(row for row in rows if row["project"] == "Avg.")


def per_project(rows):
    return {row["project"]: row["f1"] for row in rows if row["project"] in lc.PROJECTS}


def judged(run):
    """The requirements a run has scored so far, per project."""
    found = {}
    with open(run / "decisions.csv", newline="") as file:
        for row in csv.DictReader(file):
            found.setdefault(row["project"], set()).add(lc.link_id(row["requirement"]))
    return {"projects": {p: {"judged": sorted(reqs)} for p, reqs in found.items()}}


def gpt4o_range(split):
    scores = []
    for seed in SEEDS:
        links = {}
        for project in split["projects"]:
            path = next(GPT4O.glob(f"traceLinks-{project}_{seed}_artifact_artifact_reasoning_gpt_gpt-4o-2024-05-13.json_*.csv"))
            links[project] = lc.read_trace_links(path)
        scores.append(average(evaluate.evaluate(links, "judged", split)["projects"])["f1"])
    return min(scores), max(scores)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runs", type=pathlib.Path, default=REPO / "harness" / "runs")
    args = parser.parse_args()
    for model in MODELS:
        lines = []
        for config in CONFIGS:
            run = args.runs / f"{config}__{model}__colab-l4__test"
            if not (run / "metrics.json").exists():
                continue
            metrics = json.loads((run / "metrics.json").read_text())["strict"]["projects"]
            avg, f1 = average(metrics), per_project(metrics)
            count = sum(row["requirements"] for row in metrics if row["project"] in lc.PROJECTS)
            low, high = gpt4o_range(judged(run))
            verified = run / "verify-strict" / "metrics.json"
            after = ""
            if verified.exists():
                rows = json.loads(verified.read_text())[TAU]["projects"]
                v = average(rows)
                checked = sum(row["requirements"] for row in rows if row["project"] in lc.PROJECTS)
                after = f"{v['f1']:.3f} (P {v['p']:.3f}, R {v['r']:.3f}; {checked} requirements)"
            mark = " (frozen best)" if config == BEST[model] else ""
            lines.append(f"| {config}{mark} | {count} | {avg['f1']:.3f} | {avg['p']:.3f} / {avg['r']:.3f} | "
                         f"{f1.get('SMOS', 0):.3f} / {f1.get('eTour_en', 0):.3f} / {f1.get('iTrust', 0):.3f} | "
                         f"{after} | {low:.3f}–{high:.3f} |")
        if lines:
            print(f"\n**{model}** (test slice, strict parsing)\n")
            print("| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | "
                  f"With verification, tau {TAU} | GPT-4o on the same requirements |")
            print("|---|---|---|---|---|---|---|")
            print("\n".join(lines))


if __name__ == "__main__":
    main()
