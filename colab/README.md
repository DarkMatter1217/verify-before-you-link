# Colab notebooks and scripts

RQ1–RQ3 run on Google Colab with an **NVIDIA L4** GPU, one session at a time. Everything is saved to Google Drive (`MyDrive/lissa-colab/`) every 2 minutes, with an hourly snapshot (`MyDrive/lissa-colab-snapshots/`, the last 6 kept).

| File | What it is |
|---|---|
| `rq1_colab_L4.ipynb` | RQ1: LiSSA unchanged with both models. Ran 14 Nov 20:30 – 15 Nov 13:32 UTC. Includes its output. |
| `rq2_rq3_colab_L4.ipynb` | RQ2/RQ3 on the dev slice. Cells 1–4 set up the session; the last cells start pipeline v2. |
| `lissa_pipeline2.sh` | Pipeline v2: both dev passes. For each model, a fresh baseline and the four variants, then the round-2 combination, the repeatability check, and claim verification. Finished steps are skipped. |
| `lissa_rq23v2.py` | Helpers for the pipeline: choose the round-2 combination, find the best single variant, the repeatability checks, the dev summary. |
| `lissa_start2.sh` | Starts Ollama and the autosave if needed, starts the pipeline as its own background process, and shows its progress. |
| `lissa_pipeline_test.sh` | The test slice, run once with the choices in `harness/FROZEN.md`: per model, requirements in chunks (the first 10, 20, …, 110 per project), every configuration per chunk, verification of the baseline and the best prompt, then the Wilcoxon comparisons. Log: `harness/runs/pipeline-test.log`. |
| `lissa_start_test.sh` | Like `lissa_start2.sh`, for the test pipeline. Run it with `!bash /content/drive/MyDrive/lissa_start_test.sh` after setup cells 1–4. |

The three scripts are byte-for-byte the versions that ran (SHA-256 prefixes `06929e34ad74`, `a5980eaa19f1`, `d52c55258d51`). On Colab they live in `MyDrive/`.

## What the setup cells do

1. **Cell 1:** connects Google Drive; stops if the GPU is not an L4, so every run uses the same GPU type.
2. **Cell 2:** installs Java 21, Maven and Ollama 0.40.2, and adds a two-line stand-in for macOS's `java_home` tool, which the RQ1 runner uses to find Java 21.
   - The code comes from the `rq2-rq3-harness` branch of the team repository (commit `ce58f68`). It is the same code as in this repository, apart from the plain-English comments added later (see [`reports/code-changes.md`](../reports/code-changes.md), section 5).
   - In the RQ2/RQ3 notebook, this cell also writes the three harness files changed on 15 Nov (see [`reports/code-changes.md`](../reports/code-changes.md), section 4) and prints their hashes.
3. **Cell 3:** writes `sync.sh` (save to Drive, restore from Drive, snapshot) and restores the latest saved state.
4. **Cell 4:** starts Ollama with a 16,384-token context and one request at a time, plus the 2-minute autosave.

## History of the RQ2/RQ3 notebook

- **Pipeline v1** (the long `%%bash` cell) ran from 15 Nov 14:24 UTC. It used RQ1's saved answers as the baseline.
- After a repeat check showed small differences between sessions, it was stopped at 14:39 UTC. **Do not run that cell again.**
- **Pipeline v2** (`lissa_start2.sh`) started at 14:42 UTC in the same session, with a fresh baseline. RQ1's answers for the baseline are kept as `harness/runs/rq1cache-baseline__…__dev-rq1` for comparison.

## Resuming after a lost session

1. Open `rq2_rq3_colab_L4.ipynb`. Check that Runtime > Change runtime type shows **L4**, then Connect.
2. Run cells 1 to 4 in order. Cell 1 must print `NVIDIA L4`, cell 3 `restored from Drive`, cell 4 `{"version":"0.40.2"}`.
3. Run the hash-check cell (`!sha256sum …`) and compare with the hashes above.
4. Run `!bash /content/drive/MyDrive/lissa_start2.sh`.
5. Check Runtime > Manage sessions: exactly one session, at about 1.94 compute units per hour.

**Never** use "Run all", and never click Connect while a run is alive: it can start a second, separately billed GPU.

## When finished

Save (`!bash /content/sync.sh save && bash /content/sync.sh snapshot`), then Runtime > Disconnect and delete runtime, so compute units stop being used.
