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

## 2026-11-17 15:03 UTC — Session 2 started (resumed after the 24-hour limit)

- **Session 1** ran from 14:35 UTC on Nov 16 and ended at 14:33 UTC on Nov 17, at Colab's 24-hour limit, in Qwen chunk 6.
- **Saved by then:** the last Drive save was at 14:32 UTC. Nothing finished was lost; the pipeline skips the finished chunks and re-asks at most a minute of calls.
- **Delay:** the browser connection to Colab dropped and had to be restored first, so the restart came about 30 minutes after the session ended.
- **Session 2 (15:03 UTC):** L4 runtime, Drive mounted, harness hashes matched, Ollama 0.40.2, everything restored from Drive, test script hashes `49258919b74f` and `9e393ad004b2`. Exactly 1 active session at about 1.94 units per hour; 1,237.9 units left.
- **Progress:** Qwen chunks 1–5 are done (146 requirements). In chunk 6, the baseline and `definition` have reached 160 requirements.

**qwen2.5-coder-14b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 160 | 0.241 | 0.398 / 0.210 | 0.212 / 0.384 / 0.126 | 0.212 (P 0.475, R 0.165; 146 requirements) | 0.344–0.349 |
| definition | 160 | 0.191 | 0.499 / 0.131 | 0.137 / 0.264 / 0.173 |  | 0.344–0.349 |
| summary | 146 | 0.216 | 0.360 / 0.187 | 0.185 / 0.330 / 0.133 |  | 0.347–0.351 |
| project | 146 | 0.213 | 0.419 / 0.172 | 0.193 / 0.287 / 0.159 |  | 0.347–0.351 |
| examples (frozen best) | 146 | 0.305 | 0.548 / 0.259 | 0.204 / 0.495 / 0.217 | 0.264 (P 0.611, R 0.197; 146 requirements) | 0.347–0.351 |

**Inferences so far**
- **The ranking of the prompts has stayed the same at every stage:** `examples` is clearly best (+0.06 over the baseline on the same 146 requirements). Definition, project description and code summary all score below the baseline.
- **The gap to GPT-4o has settled at about 0.04–0.05 F1.** It was 0.04 after chunk 1, 0.015 after chunk 2 and 0.035 after chunk 3; it narrows on iTrust and widens on SMOS.
- **Verification keeps lowering F1** (examples 0.305 → 0.264): precision rises (0.548 → 0.611), but recall drops more. RQ3's negative result from dev holds.
- These are partial results over about 70–78% of the test requirements; the final numbers and the Wilcoxon tests come once all 205 are scored.

## 2026-11-17 16:06 UTC — Session 2 running normally

- **Health check one hour into session 2:** exactly 1 active session at about 1.94 units per hour; 1,235.8 units left. Drive saved at 16:03 UTC. No new error since the restart (the only Traceback in the log is the folder-name issue fixed on Nov 16).
- **After the restart:** chunk 6 finished at 15:57 UTC, including verification of the baseline's 548 and `examples`' 432 accepted links. All prompts have now scored 160 requirements.
- **Now:** Qwen chunk 7 (iTrust only, up to 70 per project), the baseline at 3,276 of 3,400 pairs.

**qwen2.5-coder-14b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 160 | 0.241 | 0.398 / 0.210 | 0.212 / 0.384 / 0.126 | 0.207 (P 0.477, R 0.160; 160 requirements) | 0.344–0.349 |
| definition | 160 | 0.191 | 0.499 / 0.131 | 0.137 / 0.264 / 0.173 |  | 0.344–0.349 |
| summary | 160 | 0.212 | 0.360 / 0.182 | 0.178 / 0.330 / 0.129 |  | 0.344–0.349 |
| project | 160 | 0.208 | 0.420 / 0.167 | 0.185 / 0.287 / 0.152 |  | 0.344–0.349 |
| examples (frozen best) | 160 | 0.310 | 0.558 / 0.263 | 0.201 / 0.495 / 0.234 | 0.261 (P 0.612, R 0.195; 160 requirements) | 0.344–0.349 |

**Inferences so far**
- **Every prompt has now scored the same 160 requirements** (all of SMOS and eTour, 60 of iTrust's 105), so the comparison between prompts is like for like.
- **`examples` holds its lead:** 0.310 vs the baseline's 0.241 (+0.07). Every other kind of added information stays below the baseline.
- **The gap to GPT-4o is about 0.035–0.04** (0.310 vs 0.344–0.349). It comes mostly from SMOS (0.20 vs about 0.29). On iTrust, the remaining requirements will decide it.
- **Verification lowers F1 for both prompts** (examples 0.310 → 0.261, baseline 0.241 → 0.207) while raising precision. RQ3's negative result keeps holding.
