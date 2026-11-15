"""Round 2 choice and the dev summary for the RQ2/RQ3 pipeline on Colab.

    python3 /content/rq23.py choose MODEL_TAG DEVICE   -> JSON line with the round 2 combination
    python3 /content/rq23.py summary DEVICE             -> dev results per model, with GPT-4o's dev F1 as the target
    python3 rq23.py best1 MODEL_TAG DEVICE              -> the best single-information run of pass 1 (strict dev F1)
    python3 rq23.py noise MODEL_TAG DEVICE N            -> re-asks N baseline pairs of this session: within-session noise
    python3 rq23.py rq1noise DEVICE                     -> RQ1's cached baseline vs this session's baseline: across sessions
"""
import csv
import glob
import json
import pathlib
import sys

sys.path.insert(0, "harness")
import analyze  # noqa: E402
import evaluate  # noqa: E402
import lissa_compat as lc  # noqa: E402
import variants  # noqa: E402
import verify  # noqa: E402

GPT4O_DEV = 0.385
MODELS = ("qwen2.5-coder-14b", "llama3.1-8b")


def runs(tag, device):
    return sorted(glob.glob(f"harness/runs/*__{tag}__{device}__dev"))


def name_of(run):
    return pathlib.Path(run).name.split("__")[0]


def avg_f1(run, parser):
    _, links, split = analyze.load(run, parser)
    return analyze.average_f1(evaluate.evaluate(links, "judged", split))


def choose(tag, device):
    scores = {name_of(r): avg_f1(r, "strict") for r in runs(tag, device) if name_of(r) in variants.BASE_VARIANTS}
    singles = sorted((n for n in scores if n != "baseline"), key=lambda n: -scores[n])
    helpful = [n for n in singles if scores[n] > scores["baseline"]]
    parts = helpful if len(helpful) >= 2 else singles[:2]
    candidates = json.loads(pathlib.Path("harness/data/candidates-rq1.json").read_text())
    texts = {p: (lc.load_artifacts(lc.DATASETS / p / "UC"), lc.load_artifacts(lc.DATASETS / p / "CC")) for p in lc.PROJECTS}
    limit = lc.NUM_CTX - 1024

    def tokens(chosen):
        variant, longest = variants.combined(set(chosen)), 0
        for p in lc.PROJECTS:
            requirements, code = texts[p]
            for req, ranked in candidates["projects"][p].items():
                for target, _ in ranked:
                    system, user = variant(variants.Pair(p, req, target, requirements[req], code[target]))
                    longest = max(longest, len(system) + len(user))
        return longest / 4.0

    while len(parts) >= 2 and tokens(parts) > limit:
        parts = parts[:-1]
    combination = "+".join(p for p in variants.PARTS if p in parts) if len(parts) >= 2 else ""
    print(json.dumps({"model": tag, "dev_f1": scores, "helpful": helpful, "combination": combination}))


def best1(tag, device):
    scores = {r: avg_f1(r, "strict") for r in runs(tag, device) if name_of(r) in variants.BASE_VARIANTS}
    print(pathlib.Path(max(scores, key=scores.get)).name)


def noise(tag, device, n):
    import random
    import llm
    model = {"qwen2.5-coder-14b": "qwen2.5-coder:14b", "llama3.1-8b": "llama3.1:8b"}[tag]
    path = lc.HARNESS / "cache" / f"{tag}__{device}.jsonl"
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    records = [r for r in records if r.get("kind", "classify") == "classify" and r.get("variant") == "baseline"]
    sample = random.Random(f"noise-{tag}").sample(records, min(int(n), len(records)))
    texts, same = {}, {"text": 0, "strict": 0, "tolerant": 0}
    for r in sample:
        if r["project"] not in texts:
            texts[r["project"]] = (lc.load_artifacts(lc.DATASETS / r["project"] / "UC"),
                                   lc.load_artifacts(lc.DATASETS / r["project"] / "CC"))
        requirements, code = texts[r["project"]]
        system, user = variants.baseline(variants.Pair(r["project"], r["requirement"], r["code"],
                                                       requirements[r["requirement"]], code[r["code"]]))
        assert llm.call_key(system, user) == r["key"], "rebuilt prompt does not match the cached one"
        answer = llm.ask("http://127.0.0.1:11434", model, system, user)["answer"]
        same["text"] += answer == r["answer"]
        same["strict"] += lc.is_related_cot(answer) == lc.is_related_cot(r["answer"])
        same["tolerant"] += lc.is_related_tolerant(answer) == lc.is_related_tolerant(r["answer"])
    print(f"NOISE within this session, {tag}: re-asked {len(sample)} baseline pairs: identical text {same['text']}, "
          f"same strict decision {same['strict']}, same tolerant decision {same['tolerant']}")


def rq1noise(device):
    for tag in MODELS:
        old = pathlib.Path(f"harness/runs/rq1cache-baseline__{tag}__{device}__dev-rq1")
        new = pathlib.Path(f"harness/runs/baseline__{tag}__{device}__dev")
        if not (old / "decisions.csv").exists() or not (new / "decisions.csv").exists():
            print(f"NOISE across sessions, {tag}: not available (no RQ1-cache baseline kept for this model)")
            continue
        def rows(run):
            with open(run / "decisions.csv", newline="") as file:
                return {(r["project"], r["requirement"], r["code"]): r for r in csv.DictReader(file)}
        a, b = rows(old), rows(new)
        keys = a.keys() & b.keys()
        s = sum(a[k]["related_strict"] == b[k]["related_strict"] for k in keys)
        t = sum(a[k]["related_tolerant"] == b[k]["related_tolerant"] for k in keys)
        print(f"NOISE across sessions, {tag}: {len(keys)} dev pairs; same strict decision {s} ({s / len(keys):.1%}), "
              f"same tolerant decision {t} ({t / len(keys):.1%}); dev average F1 (strict) RQ1 cache "
              f"{avg_f1(str(old), 'strict'):.3f} vs this session {avg_f1(str(new), 'strict'):.3f}")


def verified(run, parser="strict"):
    out = pathlib.Path(run) / f"verify-{parser}"
    if not (out / "links.jsonl").exists():
        return None
    records = [json.loads(line) for line in (out / "links.jsonl").read_text().splitlines() if line]
    with open(pathlib.Path(run) / "decisions.csv", newline="") as file:
        rows = list(csv.DictReader(file))
    return rows, records


def by_tau(rows, records, supported, parser="strict"):
    rescored = []
    for record in records:
        n = sum(claim["verdict"] in supported for claim in record["claims"])
        rescored.append({**record, "share": n / len(record["claims"]) if record["claims"] else 0.0})
    return {tau: analyze.average_f1(result) for tau, result in verify.metrics_by_tau(rows, rescored, parser).items()}


def summary(device):
    for tag in MODELS:
        print(f"\n## {tag}: dev average F1, strict | tolerant parsing")
        best = ("", -1.0)
        for run in runs(tag, device):
            strict, tolerant = avg_f1(run, "strict"), avg_f1(run, "tolerant")
            print(f"  {name_of(run):40} {strict:.3f} | {tolerant:.3f}")
            best = max(best, (f"{name_of(run)} (no verification)", strict), key=lambda x: x[1])
            v = verified(run)
            if v:
                for label, supported in (("unclear = not supported", {"supported"}),
                                         ("unclear = supported (sensitivity)", {"supported", "unclear"})):
                    f1 = by_tau(*v, supported)
                    print(f"     verified, {label}: " + "  ".join(f"tau {t}: {x:.3f}" for t, x in f1.items()))
                    if supported == {"supported"}:
                        for tau, x in f1.items():
                            if tau != "none":
                                best = max(best, (f"{name_of(run)} + verification, tau {tau}", x), key=lambda y: y[1])
        verdict = "BEATS GPT-4o" if best[1] > GPT4O_DEV else "below GPT-4o"
        print(f"  BEST on dev: {best[0]} = {best[1]:.3f} vs GPT-4o {GPT4O_DEV:.3f} -> {verdict}")


if __name__ == "__main__":
    {"choose": lambda: choose(sys.argv[2], sys.argv[3]), "summary": lambda: summary(sys.argv[2]),
     "best1": lambda: best1(sys.argv[2], sys.argv[3]), "noise": lambda: noise(sys.argv[2], sys.argv[3], sys.argv[4]),
     "rq1noise": lambda: rq1noise(sys.argv[2])}[sys.argv[1]]()
