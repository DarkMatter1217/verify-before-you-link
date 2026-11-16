# Test-slice timeline

A dated record of the test-slice run: what happened at each stage, the results so far and what they suggest.
Each stage is committed, so the commit history shows how the results developed.
The tables come from `reports/test_progress.py`.

- **Scoring:** strict parsing (LiSSA's rule). Choices frozen in [`harness/FROZEN.md`](../harness/FROZEN.md).
- **Partial results:** results are reported for the requirements scored so far. GPT-4o is always shown on exactly the same requirements, so partial comparisons are fair. Partial numbers are noisy; only the final, whole-slice results with the Wilcoxon tests count.

---

## 2026-11-16 14:45 UTC — Test run started (session 1)

- **Setup:** a new Colab L4 session. The setup checks passed: Drive mounted, NVIDIA L4, the harness hashes matched, Ollama 0.40.2, and everything was restored from the end of the dev pass.
- **Plan:** per model, requirements in 11 chunks (the first 10, 20, …, 110 per project). In each chunk, every prompt runs, then the baseline and the frozen best prompt are verified.
- **Size:** about 95–100 GPU hours, about 5 sessions.

## 2026-11-16 18:47–18:56 UTC — Stop and fix

- **What happened:** the run stopped at the end of chunk 1, in the verification step. When given a limit, `run.py` names its folder `…__test-first10`, and the test script looked for the name without the suffix.
- **Fix:** `run.py` is now called with `--run-id`, so every chunk writes to the same folder. This changes no prompt, setting or result. New script hash: `49258919b74f`.
- **Restart:** in the same session. All 3,000 chunk-1 answers were reused from the save, with no new model calls.

## 2026-11-16 19:39 UTC — Chunk 1 done (Qwen, first 30 test requirements)

| Prompt | Requirements | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, τ 0.2 | GPT-4o, same requirements |
|---|---|---|---|---|---|---|
| baseline | 30 | 0.247 | 0.461 / 0.212 | 0.230 / 0.415 / 0.097 | 0.217 (P 0.502, R 0.175) | 0.350–0.355 |
| definition | 30 | 0.182 | 0.518 / 0.121 | 0.128 / 0.293 / 0.125 | | 0.350–0.355 |
| summary | 30 | 0.239 | 0.460 / 0.200 | 0.146 / 0.460 / 0.111 | | 0.350–0.355 |
| project | 30 | 0.206 | 0.472 / 0.162 | 0.118 / 0.374 / 0.128 | | 0.350–0.355 |
| **examples (frozen best)** | 30 | **0.314** | 0.575 / 0.264 | 0.223 / 0.525 / 0.192 | 0.295 (P 0.637, R 0.221) | 0.350–0.355 |

**Inferences so far**
- **The dev picture holds on unseen requirements:** `examples` is again Qwen's best prompt (+0.067 over the baseline). Definition and project description hurt again.
- **Verification again lowers F1:** precision rises (examples 0.575 → 0.637), but recall falls more.
- **Gap to GPT-4o:** about 0.04 on these 30 requirements, smaller than on dev (0.07). Qwen is close on eTour (0.525 vs 0.54–0.56).

## 2026-11-16 20:55 UTC — Chunk 2 running (Qwen, up to 20 requirements per project)

- **Progress:** the baseline finished chunk 2; the other prompts and verification are running.
- **Baseline over 60 requirements:** F1 0.260 (GPT-4o on the same 60: 0.375–0.382).
- **Compute:** 1 session, about 1,272 units left.
- **Monitoring changed at Prabhjot's request:** instead of checks every 50 minutes, a restart check runs when each Colab session ends, and a health check one hour after each new session starts. Each stage is added here and committed.
