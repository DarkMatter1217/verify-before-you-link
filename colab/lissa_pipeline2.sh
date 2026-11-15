#!/bin/bash
# RQ2/RQ3 dev passes, v2: fresh same-session baselines; all classification first, verification last.
set -eo pipefail
cd /content/LiSSA-Replication-Package
mkdir -p harness/runs/.markers
exec > >(tee -a harness/runs/pipeline-dev.log) 2>&1
D=colab-l4
H=/content/drive/MyDrive
MODELS="qwen2.5-coder:14b llama3.1:8b"
say() { echo "=== $(date -u +%FT%TZ) $*"; }
done_() { [ -f harness/runs/.markers/$1 ]; }
mark() { touch harness/runs/.markers/$1; }
best() { python3 harness/analyze.py --parser strict variant harness/runs/*__$1__${D}__dev | tee /dev/stderr | sed -n 's/^Highest average F1 (strict parsing): //p'; }
verify_once() { [ -f harness/runs/$1/verify-strict/metrics.json ] || { say "RQ3 dev verify $1"; python3 harness/verify.py --run harness/runs/$1 --parser strict --device $D; }; }

say "PIPELINE v2: fresh same-session baselines; classification for both models first, verification last"
for m in $MODELS; do
  for i in 1 2 3 4 5; do ollama pull $m > /dev/null 2>&1 && break; say "pull $m failed, retry $i"; sleep 30; done
done

if ! done_ v2-keep-rq1-baselines; then
  for T in qwen2.5-coder-14b llama3.1-8b; do
    if [ -d harness/runs/baseline__${T}__${D}__dev ]; then
      rm -rf harness/runs/rq1cache-baseline__${T}__${D}__dev-rq1
      mv harness/runs/baseline__${T}__${D}__dev harness/runs/rq1cache-baseline__${T}__${D}__dev-rq1
      say "kept RQ1's cached baseline for $T as rq1cache-baseline__${T}__${D}__dev-rq1"
    fi
  done
  mark v2-keep-rq1-baselines
fi

for M in $MODELS; do
  T=${M/:/-}
  if ! done_ v2-cls1-$T; then
    say "RQ2 dev $M baseline (fresh, this session)"
    python3 harness/run.py --variant baseline --model $M --slice dev --device $D
    for v in definition summary project examples; do
      say "RQ2 dev $M $v"
      python3 harness/run.py --variant $v --model $M --slice dev --device $D
    done
    bash /content/sync.sh save
    mark v2-cls1-$T
  fi
done
say "PASS 1 CLASSIFICATION DONE"

for M in $MODELS; do
  T=${M/:/-}
  if ! done_ v2-cls2-$T; then
    CHOICE=$(python3 $H/lissa_rq23v2.py choose $T $D | tail -1)
    echo "$CHOICE"
    COMBO=$(echo "$CHOICE" | python3 -c 'import json,sys; print(json.load(sys.stdin)["combination"])')
    if [ -n "$COMBO" ]; then
      say "RQ2 dev round 2 $M $COMBO"
      python3 harness/run.py --variant $COMBO --model $M --slice dev --device $D
      bash /content/sync.sh save
    fi
    mark v2-cls2-$T
  fi
done
say "PASS 2 CLASSIFICATION DONE"

if ! done_ v2-noise; then
  for T in qwen2.5-coder-14b llama3.1-8b; do python3 $H/lissa_rq23v2.py noise $T $D 50; done
  python3 $H/lissa_rq23v2.py rq1noise $D
  mark v2-noise
fi

for M in $MODELS; do
  T=${M/:/-}
  if ! done_ v2-ver-$T; then
    B1=$(python3 $H/lissa_rq23v2.py best1 $T $D)
    B2=$(best $T)
    verify_once baseline__${T}__${D}__dev
    verify_once $B1
    verify_once $B2
    python3 harness/analyze.py --parser strict tau harness/runs/baseline__${T}__${D}__dev
    bash /content/sync.sh save
    mark v2-ver-$T
  fi
done
say "ROUND 1 DEV DONE"

say "SUMMARY after round 2, dev slice"
python3 $H/lissa_rq23v2.py summary $D
python3 $H/lissa_rq23v2.py rq1noise $D
say "GPT-4o CoT on the dev slice (target)"
python3 - <<'PY'
import pathlib, sys
sys.path.insert(0, "harness")
import evaluate
R = pathlib.Path("LiSSA-RATLR-V2/lissa/results-r2c")
links = {p: {tuple(l.split(",")) for l in next(R.glob(f"traceLinks-{p}_133742243_artifact_artifact_reasoning_gpt_gpt-4o-2024-05-13.json_*.csv")).read_text().splitlines() if l}
         for p in ("SMOS", "eTour_en", "iTrust")}
print(evaluate.table(evaluate.evaluate(links, "dev")))
PY
mark dev2
bash /content/sync.sh save
bash /content/sync.sh snapshot
say "ROUND 2 DEV DONE"
