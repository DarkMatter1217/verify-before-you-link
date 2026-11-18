#!/usr/bin/env python3
"""RQ4: how long LiSSA's own prompts take on Rahul's laptop (MacBook Pro, M5 Pro, 24 GB).

LiSSA writes one log line, with a time stamp, each time it asks the model about a requirement and a code file:
    2026-11-12 19:30:22:003 -0500 [pool-1-thread-1] INFO ReasoningClassifier - Classifying: UC1.txt and X.java
LiSSA asks one question at a time, so a question took from its own line until the next line of the same run.

Left out, as the proposal says (warm-up and saved answers):
- the first question after each start or restart, because it includes loading the model;
- the last question before a stop, because its end is unknown;
- questions that took longer than LiSSA's 15-minute time limit (the laptop was asleep or paused).
Saved answers are never logged by LiSSA, so they are left out by themselves.

A requirement's time is the sum of its questions, counted only when none of its questions was left out.

    python3 reports/rq1_laptop_timing.py [--run LiSSA-RATLR-V2/lissa/results-local/rq1-laptop] [--out FILE]
"""

import argparse
import datetime
import pathlib
import re
import statistics

LINE = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d):(\d{3}) [+-]\d{4} \[[^\]]+\] INFO (\S+) - (.*)$")
QUESTION = re.compile(r"Classifying: (\S+) and (\S+)$")
TIME_LIMIT = 15 * 60
PROMPTS = {"reasoning": "chain-of-thought", "simple": "KISS"}


def read_log(path):
    """List of (time in seconds, message) for every time-stamped line."""
    lines = []
    for text in path.read_text(errors="replace").splitlines():
        match = LINE.match(text)
        if match:
            stamp = datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S").timestamp()
            lines.append((stamp + int(match.group(2)) / 1000, match.group(4)))
    return lines


def question_times(lines):
    """(requirement, seconds or None) for each question; None means left out."""
    result = []
    first_since_start = True
    for i, (start, message) in enumerate(lines):
        if message.startswith(("Found ", "Invoking")):
            first_since_start = True
        question = QUESTION.search(message)
        if not question:
            continue
        following = lines[i + 1] if i + 1 < len(lines) else None
        stopped = following is None or following[1].startswith(("Found ", "Invoking"))
        seconds = None if stopped else following[0] - start
        if first_since_start or seconds is None or seconds > TIME_LIMIT:
            seconds = None
        first_since_start = False
        result.append((question.group(1), seconds))
    return result


def median_iqr(values):
    if len(values) < 2:
        return "—"
    q1, q2, q3 = statistics.quantiles(values, n=4)
    return f"{q2:.1f} s ({q1:.1f}–{q3:.1f} s)"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run", default="LiSSA-RATLR-V2/lissa/results-local/rq1-laptop")
    parser.add_argument("--out", help="also write the tables to this Markdown file")
    args = parser.parse_args()

    rows = []
    for log in sorted(pathlib.Path(args.run, "logs").glob("*_ollama_*.log")):
        match = re.match(r"(SMOS|eTour_en|iTrust)_.*artifact_(reasoning|simple)_ollama_(.+)_bge-m3\.log$", log.name)
        project, prompt, model = match.groups()
        times = question_times(read_log(log))
        per_requirement = {}
        for requirement, seconds in times:
            per_requirement.setdefault(requirement, []).append(seconds)
        rows.append({"model": model, "prompt": PROMPTS[prompt], "project": project,
                     "asked": len(times), "calls": [s for _, s in times if s is not None],
                     "requirements": [sum(v) for v in per_requirement.values() if None not in v]})

    out = ["# RQ1 on the laptop: time per question and per requirement", "",
           f"Source: LiSSA's logs in `{args.run}/logs/` (MacBook Pro, Apple M5 Pro, 24 GB; Ollama 0.40.14).",
           "Median with the interquartile range in brackets. Left out: the first question after each start "
           "(model loading), the last question before a stop, and questions over LiSSA's 15-minute limit.", ""]
    out += ["## By configuration (all three projects)", "",
            "| Model | Prompt | Questions timed | Per question | Requirements timed | Per requirement |",
            "|---|---|---|---|---|---|"]
    for model in sorted({r["model"] for r in rows}):
        for prompt in ("KISS", "chain-of-thought"):
            group = [r for r in rows if r["model"] == model and r["prompt"] == prompt]
            calls = [c for r in group for c in r["calls"]]
            reqs = [c for r in group for c in r["requirements"]]
            asked = sum(r["asked"] for r in group)
            out.append(f"| {model} | {prompt} | {len(calls):,} of {asked:,} | {median_iqr(calls)} | "
                       f"{len(reqs)} | {median_iqr(reqs)} |")
    out += ["", "## By project", "",
            "| Model | Prompt | Project | Questions timed | Per question | Requirements timed | Per requirement |",
            "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: (r["model"], r["prompt"], r["project"])):
        out.append(f"| {r['model']} | {r['prompt']} | {r['project']} | {len(r['calls']):,} of {r['asked']:,} | "
                   f"{median_iqr(r['calls'])} | {len(r['requirements'])} | {median_iqr(r['requirements'])} |")
    text = "\n".join(out) + "\n"
    print(text)
    if args.out:
        pathlib.Path(args.out).write_text(text)


if __name__ == "__main__":
    main()
