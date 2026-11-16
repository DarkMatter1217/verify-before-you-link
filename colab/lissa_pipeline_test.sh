#!/bin/bash
# RQ2/RQ3 on the test slice, run once with the choices in harness/FROZEN.md.
# Per model, requirements are processed in chunks (the first 10, 20, ... per project), so every configuration of a
# requirement is answered close together. All answers are saved; finished chunks are skipped after a restart.
set -eo pipefail
cd /content/LiSSA-Replication-Package
mkdir -p harness/runs/.markers
exec > >(tee -a harness/runs/pipeline-test.log) 2>&1
D=colab-l4
TAU=0.2
MODELS="qwen2.5-coder:14b llama3.1:8b"
LIMITS="10 20 30 40 50 60 70 80 90 100 110"
say() { echo "=== $(date -u +%FT%TZ) $*"; }
done_() { [ -f harness/runs/.markers/$1 ]; }
mark() { touch harness/runs/.markers/$1; }
run_dir() { echo "harness/runs/$1__$2__${D}__test"; }
best_of() { case "$1" in qwen2.5-coder:14b) echo examples ;; llama3.1:8b) echo definition+summary ;; esac; }

say "TEST PIPELINE: frozen choices (qwen: examples, llama: definition+summary, tau $TAU, strict parsing)"
for m in $MODELS; do
  for i in 1 2 3 4 5; do ollama pull $m > /dev/null 2>&1 && break; say "pull $m failed, retry $i"; sleep 30; done
done

for M in $MODELS; do
  T=${M/:/-}
  B=$(best_of $M)
  CONFIGS="baseline definition summary project examples"
  case " $CONFIGS " in *" $B "*) ;; *) CONFIGS="$CONFIGS $B" ;; esac
  for N in $LIMITS; do
    done_ test-$T-L$N && continue
    say "TEST $M: chunk up to $N requirements per project"
    for v in $CONFIGS; do
      python3 harness/run.py --variant $v --model $M --slice test --limit $N --device $D
    done
    for v in baseline $B; do
      python3 harness/verify.py --run "$(run_dir $v $T)" --parser strict --device $D
    done
    bash /content/sync.sh save
    mark test-$T-L$N
  done
  if ! done_ test-$T-full; then
    say "TEST $M: whole slice (answers already saved; scoring)"
    for v in $CONFIGS; do
      python3 harness/run.py --variant $v --model $M --slice test --device $D
    done
    for v in baseline $B; do
      python3 harness/verify.py --run "$(run_dir $v $T)" --parser strict --device $D
    done
    bash /content/sync.sh save
    mark test-$T-full
  fi
  if ! done_ test-$T-stats; then
    say "TEST $M: comparisons with the baseline (Wilcoxon, Holm)"
    OTHERS=""
    for v in $CONFIGS; do [ "$v" = baseline ] || OTHERS="$OTHERS $(run_dir $v $T)"; done
    python3 harness/analyze.py --parser strict test "$(run_dir baseline $T)" $OTHERS \
      "$(run_dir baseline $T)@tau=$TAU" "$(run_dir $B $T)@tau=$TAU" --json harness/runs/test-comparisons-$T.json
    bash /content/sync.sh save
    mark test-$T-stats
  fi
  say "TEST $M DONE"
done

say "GPT-4o CoT on the test slice (reference)"
python3 - <<'PY'
import pathlib, sys
sys.path.insert(0, "harness")
import evaluate
R = pathlib.Path("LiSSA-RATLR-V2/lissa/results-r2c")
links = {p: {tuple(l.split(",")) for l in next(R.glob(f"traceLinks-{p}_133742243_artifact_artifact_reasoning_gpt_gpt-4o-2024-05-13.json_*.csv")).read_text().splitlines() if l}
         for p in ("SMOS", "eTour_en", "iTrust")}
print(evaluate.table(evaluate.evaluate(links, "test")))
PY
mark test-done
bash /content/sync.sh save
bash /content/sync.sh snapshot
say "TEST DONE"
