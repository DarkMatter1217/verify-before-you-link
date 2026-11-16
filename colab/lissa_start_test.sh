#!/bin/bash
# Starts Ollama and the autosave loop when they are not running, runs the test pipeline in its own session
# (so a cell interrupt cannot kill it), and follows the pipeline's progress lines until it ends.
cd /content/LiSSA-Replication-Package
LOG=harness/runs/pipeline-test.log
if ! curl -s -m 3 http://127.0.0.1:11434/api/version > /dev/null; then
  OLLAMA_HOST=127.0.0.1:11434 OLLAMA_NUM_PARALLEL=1 OLLAMA_CONTEXT_LENGTH=16384 \
    setsid nohup ollama serve >> /content/ollama.log 2>&1 < /dev/null &
  sleep 8
fi
echo "ollama $(curl -s -m 5 http://127.0.0.1:11434/api/version)"
if ! pgrep -f "sleep 120; bash /content/sync.sh" > /dev/null; then
  setsid nohup bash -c "i=0; while true; do sleep 120; bash /content/sync.sh save >> /content/sync.log 2>&1; i=\$((i+1)); [ \$((i % 30)) -eq 0 ] && bash /content/sync.sh snapshot >> /content/sync.log 2>&1; done" \
    > /dev/null 2>&1 < /dev/null &
  echo "autosave loop started"
else
  echo "autosave loop already running"
fi
if ! pgrep -f "bash /content/drive/MyDrive/lissa_pipeline_test.sh" > /dev/null; then
  setsid nohup bash /content/drive/MyDrive/lissa_pipeline_test.sh > /dev/null 2>&1 < /dev/null &
  echo "test pipeline started"
else
  echo "test pipeline already running"
fi
sleep 5
PID=$(pgrep -of "bash /content/drive/MyDrive/lissa_pipeline_test.sh")
[ -n "$PID" ] || { tail -n 20 $LOG; exit 1; }
tail -n 3 --pid=$PID -f $LOG | grep --line-buffered -E "^===|Error|Traceback|Interrupted|TEST|\| Avg\.|significant|Comparison"
echo "test pipeline process ended"; tail -n 5 $LOG
