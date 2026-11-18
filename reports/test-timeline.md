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

## 2026-11-18 11:25 UTC — Qwen complete

- **Qwen finished at 22:50 UTC on Nov 17,** about 32 hours after the test started. The whole slice (205 requirements, 4,100 pairs per prompt) was scored from the saved answers, and the Wilcoxon tests ran. Llama started at once.
- **Session 2:** exactly 1 active session at about 1.94 units per hour; 1,198.6 units left. Drive saved at 11:14 UTC. No errors.
- **Qwen's speed on the L4:** median 4.1–4.8 s per call and 91–103 s per requirement (classification only).
- **Llama:** chunk 1 (30 requirements) finished at 05:47 UTC and took about 7 hours, against about 4.7 hours for Qwen, so Llama is about 1.5 times slower per requirement. Chunk 2 is on its sixth prompt. Llama should finish in the evening of Nov 19 (Eastern time), about 00:00 UTC on Nov 20.

**qwen2.5-coder-14b, final** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 205 | 0.249 | 0.404 / 0.222 | 0.212 / 0.384 / 0.149 | 0.220 (P 0.491, R 0.171) | 0.352–0.354 |
| definition | 205 | 0.199 | 0.510 / 0.137 | 0.137 / 0.264 / 0.196 |  | 0.352–0.354 |
| summary | 205 | 0.220 | 0.365 / 0.193 | 0.178 / 0.330 / 0.151 |  | 0.352–0.354 |
| project | 205 | 0.213 | 0.425 / 0.172 | 0.185 / 0.287 / 0.167 |  | 0.352–0.354 |
| examples (frozen best) | 205 | 0.322 | 0.570 / 0.275 | 0.201 / 0.495 / 0.271 | 0.279 (P 0.637, R 0.209) | 0.352–0.354 |

Verification at the other thresholds (average F1; verification only removes links, so it can only lower recall):

| tau | none | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
|---|---|---|---|---|---|---|
| baseline | 0.249 | 0.220 | 0.189 | 0.143 | 0.106 | 0.047 |
| examples | 0.322 | 0.279 | 0.241 | 0.209 | 0.146 | 0.070 |

**Comparisons with the baseline** (per-requirement F1, strict parsing; 183 requirements with gold links; two-sided Wilcoxon, Holm over the 6 comparisons; from `harness/runs/test-comparisons-qwen2.5-coder-14b.json`)

| Comparison | n | changed | mean ΔF1 | p | p (Holm) | r | significant |
|---|---|---|---|---|---|---|---|
| definition vs baseline | 183 | 124 | −0.041 | 0.0035 | 0.0159 | −0.30 | yes |
| summary vs baseline | 183 | 106 | −0.013 | 0.1793 | 0.3587 | −0.15 | no |
| project vs baseline | 183 | 104 | −0.021 | 0.0968 | 0.2905 | −0.19 | no |
| examples vs baseline | 183 | 120 | +0.073 | < 0.0001 | 0.0002 | +0.43 | yes |
| baseline + verification (tau 0.2) vs baseline | 183 | 92 | −0.027 | 0.0032 | 0.0159 | −0.35 | yes |
| examples + verification (tau 0.2) vs baseline | 183 | 129 | +0.032 | 0.2532 | 0.3587 | +0.12 | no |

**llama3.1-8b, so far** (partial; the numbers will change)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 60 | 0.290 | 0.232 / 0.533 | 0.413 / 0.332 / 0.124 | 0.245 (P 0.235, R 0.349; 30 requirements) | 0.375–0.382 |
| definition | 60 | 0.346 | 0.330 / 0.457 | 0.383 / 0.409 / 0.247 |  | 0.375–0.382 |
| summary | 60 | 0.275 | 0.233 / 0.477 | 0.361 / 0.322 / 0.142 |  | 0.375–0.382 |
| project | 60 | 0.276 | 0.217 / 0.523 | 0.417 / 0.310 / 0.101 |  | 0.375–0.382 |
| examples | 60 | 0.177 | 0.376 / 0.127 | 0.149 / 0.290 / 0.092 |  | 0.375–0.382 |
| definition+summary (frozen best) | 30 | 0.290 | 0.308 / 0.335 | 0.337 / 0.450 / 0.082 | 0.256 (P 0.326, R 0.281; 30 requirements) | 0.350–0.355 |

**Inferences for Qwen**
- **RQ2: only one kind of added information helps.** Labelled examples are the only enrichment that improves on LiSSA's prompt, significantly (average F1 0.249 → 0.322; +0.073 per requirement, Holm p 0.0002, r +0.43). They raise both precision (0.404 → 0.570) and recall (0.222 → 0.275). The trace-link definition makes the model more cautious and is significantly worse (−0.041). The code summary and project description make no significant difference. The choice made on dev held on unseen requirements.
- **RQ3: verification does not help.** It raises precision (baseline 0.404 → 0.491; examples 0.570 → 0.637), but recall falls more, so F1 drops. On the baseline the drop is significant (−0.027, Holm p 0.016). With examples, verification removes most of the gain: examples + verification is no longer significantly better than the baseline. Every higher threshold lowers F1 further.
- **For RQ4:** of the links verification removed at tau 0.2, 157 of 315 (baseline) and 87 of 225 (examples) had no claims at all. The verifier also flagged many claims for citing identifiers that the file does not declare (668 of 2,803 verdicts for the baseline). RQ4 should examine both.
- **Against GPT-4o:** Qwen's best prompt reaches 0.322 against 0.352–0.354, about 91% of GPT-4o. It is level on eTour (0.495 vs 0.49) and close on iTrust (0.271 vs 0.28); the whole gap is on SMOS (0.201 vs 0.29). The SMOS gap does not come from retrieval: on SMOS, bge-m3's recall ceiling (0.45) is higher than that of GPT-4o's embedding model (0.42; RQ1 report).
- **Llama (early):** `definition` leads after 60 requirements (0.346), while the frozen best, `definition+summary`, has 0.290 after 30. It is too early to read anything into this; the frozen choice stays.

## 2026-11-18 16:00 UTC — Session 3 started

- **Session 2** ended at Colab's 24-hour limit. Its last Drive save was at 14:41:51 UTC on Nov 18, and saves run every 2 minutes, so it ended at about 14:42 UTC. The 24 hours count from when the runtime starts, about 20 minutes before the pipeline starts (setup), as in session 1. It stopped in Llama chunk 3 (up to 30 requirements per project), during the `summary` prompt.
- **Saved by then:** everything up to 14:41 UTC. At most about 2 minutes of answers were lost; the pipeline asks those again.
- **Delay:** the restart check was timed from the pipeline start (15:03 UTC) instead of the runtime start, so setup began at 15:27 UTC and the pipeline restarted at 15:46 UTC, about an hour after the session ended. Session 3's runtime started at 15:27 UTC, so it should end at about 15:27 UTC on Nov 19; the next restart check is timed from that.
- **Session 3 (15:46 UTC):** L4 runtime, Drive mounted, harness hashes matched, Ollama 0.40.2, everything restored from Drive (last save 14:41:51 UTC), test script hashes `49258919b74f` and `9e393ad004b2`. Exactly 1 active session at about 1.94 units per hour; 1,191 units left.
- **Progress:** Qwen is complete (skipped). Llama chunks 1–2 are done (60 requirements, all six prompts). In chunk 3 (90 requirements), the baseline and `definition` are done, and `summary` resumed with 1,374 of its 1,800 pairs already answered; `project`, `examples`, `definition+summary` and the verification follow.
- **Expected finish:** Llama has about 31 hours of work left (one chunk of 30 requirements takes about 7 hours), and session 3 will need one more restart, so Llama should still finish in the evening of Nov 19 (Eastern time).


**qwen2.5-coder-14b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 205 | 0.249 | 0.404 / 0.222 | 0.212 / 0.384 / 0.149 | 0.220 (P 0.491, R 0.171; 205 requirements) | 0.352–0.354 |
| definition | 205 | 0.199 | 0.510 / 0.137 | 0.137 / 0.264 / 0.196 |  | 0.352–0.354 |
| summary | 205 | 0.220 | 0.365 / 0.193 | 0.178 / 0.330 / 0.151 |  | 0.352–0.354 |
| project | 205 | 0.213 | 0.425 / 0.172 | 0.185 / 0.287 / 0.167 |  | 0.352–0.354 |
| examples (frozen best) | 205 | 0.322 | 0.570 / 0.275 | 0.201 / 0.495 / 0.271 | 0.279 (P 0.637, R 0.209; 205 requirements) | 0.352–0.354 |

**llama3.1-8b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 90 | 0.267 | 0.216 / 0.476 | 0.399 / 0.314 / 0.089 | 0.265 (P 0.242, R 0.442; 60 requirements) | 0.366–0.369 |
| definition | 90 | 0.323 | 0.310 / 0.417 | 0.390 / 0.405 / 0.174 |  | 0.366–0.369 |
| summary | 60 | 0.275 | 0.233 / 0.477 | 0.361 / 0.322 / 0.142 |  | 0.375–0.382 |
| project | 60 | 0.276 | 0.217 / 0.523 | 0.417 / 0.310 / 0.101 |  | 0.375–0.382 |
| examples | 60 | 0.177 | 0.376 / 0.127 | 0.149 / 0.290 / 0.092 |  | 0.375–0.382 |
| definition+summary (frozen best) | 60 | 0.333 | 0.338 / 0.423 | 0.370 / 0.414 / 0.216 | 0.302 (P 0.363, R 0.355; 60 requirements) | 0.375–0.382 |

**Inferences so far (Llama, partial)**
- **Llama behaves very differently from Qwen.** With LiSSA's prompt it says "yes" much more often: precision 0.216 and recall 0.476, against Qwen's 0.404 and 0.222.
- **RQ2: the information that helps depends on the model.** The trace-link definition, which made Qwen significantly worse, helps Llama (0.323 vs the baseline's 0.267 on the same 90 requirements). Labelled examples, Qwen's best prompt, hurt Llama badly (0.177 on 60 requirements): recall collapses to 0.127.
- **The frozen best prompt, `definition+summary`, is ahead of the baseline** (0.333 vs 0.290 on the same 60 requirements), but `definition` alone scored slightly higher on those 60 (0.346). The frozen choice stays; the Wilcoxon tests on all 205 requirements will decide.
- **RQ3: verification lowers F1 for Llama too** (`definition+summary` 0.333 → 0.302, baseline 0.290 → 0.265 on 60 requirements), the same pattern as for Qwen and on dev.
- **Against GPT-4o:** Llama's frozen best reaches about 88% of GPT-4o on the same 60 requirements (0.333 vs 0.375–0.382), close to Qwen's final 91%.

## 2026-11-18 17:02 UTC — Session 3 running normally

- **Session 3:** exactly 1 active session at about 1.94 units per hour; 1,188.9 units left. Drive saved at 17:00 UTC. No errors.
- **Speed:** 656 Llama calls since the restart at 15:48 UTC, about 6.6 s per call on average (these requirements are from SMOS and eTour, where Llama's calls are slowest; on iTrust they average 5.4 s).
- **Chunk 3 (90 requirements):** `summary` is done; `project` is running; `examples`, `definition+summary` and the verification follow. Chunk 3 should end at about 20:30 UTC.
- **Expected finish:** about 13,800 calls remain after chunk 3. Llama should finish at about 22:30 UTC on Nov 19 (about 5:30 pm Eastern; likely 4–8 pm), including one more restart when session 3 reaches 24 hours at about 15:27 UTC on Nov 19.


**qwen2.5-coder-14b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 205 | 0.249 | 0.404 / 0.222 | 0.212 / 0.384 / 0.149 | 0.220 (P 0.491, R 0.171; 205 requirements) | 0.352–0.354 |
| definition | 205 | 0.199 | 0.510 / 0.137 | 0.137 / 0.264 / 0.196 |  | 0.352–0.354 |
| summary | 205 | 0.220 | 0.365 / 0.193 | 0.178 / 0.330 / 0.151 |  | 0.352–0.354 |
| project | 205 | 0.213 | 0.425 / 0.172 | 0.185 / 0.287 / 0.167 |  | 0.352–0.354 |
| examples (frozen best) | 205 | 0.322 | 0.570 / 0.275 | 0.201 / 0.495 / 0.271 | 0.279 (P 0.637, R 0.209; 205 requirements) | 0.352–0.354 |

**llama3.1-8b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 90 | 0.267 | 0.216 / 0.476 | 0.399 / 0.314 / 0.089 | 0.265 (P 0.242, R 0.442; 60 requirements) | 0.366–0.369 |
| definition | 90 | 0.323 | 0.310 / 0.417 | 0.390 / 0.405 / 0.174 |  | 0.366–0.369 |
| summary | 90 | 0.265 | 0.229 / 0.437 | 0.367 / 0.324 / 0.105 |  | 0.366–0.369 |
| project | 60 | 0.276 | 0.217 / 0.523 | 0.417 / 0.310 / 0.101 |  | 0.375–0.382 |
| examples | 60 | 0.177 | 0.376 / 0.127 | 0.149 / 0.290 / 0.092 |  | 0.375–0.382 |
| definition+summary (frozen best) | 60 | 0.333 | 0.338 / 0.423 | 0.370 / 0.414 / 0.216 | 0.302 (P 0.363, R 0.355; 60 requirements) | 0.375–0.382 |

**Inferences so far (Llama, partial)**
- **The code summary makes no difference for Llama either:** 0.265 against the baseline's 0.267 on the same 90 requirements, as for Qwen (no significant difference).
- **`definition` keeps its lead over the baseline on 90 requirements** (0.323 vs 0.267), mainly through higher precision (0.310 vs 0.216). For Qwen the same definition was significantly worse, so the effect of the added information depends on the model.
- No new results for `project`, `examples` and `definition+summary` yet; they reach 90 requirements later in chunk 3.

## 2026-11-18 20:20 UTC — Llama chunk 3 done (90 of 205 requirements)

- **Chunk 3 finished at 20:16 UTC**, about 15 minutes ahead of the estimate. All six prompts and the verification of the baseline and `definition+summary` now cover the same 90 requirements (30 per project).
- **Chunk 4 (up to 40 requirements per project) started at 20:16 UTC.** Drive saved at 20:17 UTC; no new errors in the log.
- **Expected finish unchanged:** about 13,800 calls remain. Llama should finish at about 22:30 UTC on Nov 19 (about 5:30 pm Eastern; likely 4–8 pm), including the restart when session 3 reaches 24 hours at about 15:27 UTC on Nov 19.


**qwen2.5-coder-14b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 205 | 0.249 | 0.404 / 0.222 | 0.212 / 0.384 / 0.149 | 0.220 (P 0.491, R 0.171; 205 requirements) | 0.352–0.354 |
| definition | 205 | 0.199 | 0.510 / 0.137 | 0.137 / 0.264 / 0.196 |  | 0.352–0.354 |
| summary | 205 | 0.220 | 0.365 / 0.193 | 0.178 / 0.330 / 0.151 |  | 0.352–0.354 |
| project | 205 | 0.213 | 0.425 / 0.172 | 0.185 / 0.287 / 0.167 |  | 0.352–0.354 |
| examples (frozen best) | 205 | 0.322 | 0.570 / 0.275 | 0.201 / 0.495 / 0.271 | 0.279 (P 0.637, R 0.209; 205 requirements) | 0.352–0.354 |

**llama3.1-8b** (test slice, strict parsing)

| Prompt | Requirements scored | Avg. F1 | P / R | F1 SMOS / eTour / iTrust | With verification, tau 0.2 | GPT-4o on the same requirements |
|---|---|---|---|---|---|---|
| baseline | 90 | 0.267 | 0.216 / 0.476 | 0.399 / 0.314 / 0.089 | 0.240 (P 0.220, R 0.388; 90 requirements) | 0.366–0.369 |
| definition | 90 | 0.323 | 0.310 / 0.417 | 0.390 / 0.405 / 0.174 |  | 0.366–0.369 |
| summary | 90 | 0.265 | 0.229 / 0.437 | 0.367 / 0.324 / 0.105 |  | 0.366–0.369 |
| project | 90 | 0.259 | 0.207 / 0.469 | 0.409 / 0.300 / 0.069 |  | 0.366–0.369 |
| examples | 90 | 0.170 | 0.385 / 0.122 | 0.160 / 0.274 / 0.078 |  | 0.366–0.369 |
| definition+summary (frozen best) | 90 | 0.320 | 0.339 / 0.383 | 0.384 / 0.418 / 0.159 | 0.284 (P 0.358, R 0.315; 90 requirements) | 0.366–0.369 |

**Inferences so far (Llama, 90 requirements, all prompts on the same requirements)**
- **RQ2: only the trace-link definition helps Llama.** `definition` 0.323 and `definition+summary` 0.320 against the baseline's 0.267. The summary (0.265) and the project description (0.259) make no difference. Labelled examples, Qwen's best prompt, hurt Llama (0.170): recall drops to 0.122.
- **Adding the code summary to the definition does not add anything** (0.320 vs 0.323). The frozen choice stays; the Wilcoxon tests on all 205 requirements will decide.
- **RQ3: verification lowers F1 for Llama as well** (`definition+summary` 0.320 → 0.284, baseline 0.267 → 0.240). It raises precision a little (0.339 → 0.358) but costs more recall (0.383 → 0.315), the same pattern as for Qwen and on dev.
- **Against GPT-4o:** Llama's frozen best reaches about 87% of GPT-4o on the same 90 requirements (0.320 vs 0.366–0.369).
