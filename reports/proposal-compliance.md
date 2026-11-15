# How the project still matches the proposal

Status: 15 November 2026. Proposal: [`proposal/CSI5187_Proposal_Singh_Rahul.pdf`](../proposal/CSI5187_Proposal_Singh_Rahul.pdf).

**Short answer:** the research design is the one in the proposal: same RQs, data, models, prompts, slices, metrics and tests.
What changed is **where** the experiments run (a rented GPU instead of our laptops). The method did not change.
Each change below is stated, explained and backed by a measurement, and the final report will say the same.

## 1. Item by item

| The proposal says | What we do | Status |
|---|---|---|
| LiSSA's benchmark: SMOS, eTour, iTrust; 256 requirements, 442 code files, 1,638 gold links; top-20 retrieval, 5,120 candidate pairs | Same data, checked by the RQ1 runner (`rq1-report.md`, "Validity checks") | Matches |
| RQ1: LiSSA run unchanged with Ollama, bge-m3, Qwen2.5-Coder-14B and Llama-3.1-8B, 4-bit, temperature 0, no paid API | Same. Two technical fixes in LiSSA's connection to Ollama (see [`code-changes.md`](code-changes.md)) | Matches; the fixes are reported |
| RQ1 metrics: P, R, F1, F2 per project, average and link-weighted average; compared with GPT-4o, GPT-4o-mini, VSM, LSI, FTLR; retrieval-only recall@20 as the ceiling | All in `rq1-report.md` | Matches |
| Scoring "exactly as LiSSA does"; LiSSA run "unchanged" | Every reported result uses LiSSA's own answer rule (strict parsing): RQ1, the dev choices, the test comparisons, the Wilcoxon tests and the GPT-4o comparison | Matches |
| (not in the proposal) | Tolerant parsing, used only in RQ4 to measure how much the "missing answer tag" error costs | Inside RQ4's error analysis, see 2.5 |
| RQ2 adds one piece of information at a time to LiSSA's chain-of-thought prompt: definition, code summary from a Java parser, project description, cross-project examples | Four single variants, prompt texts frozen on 14 Nov 2026 before any run | Matches |
| (not in the proposal) | Round-2 prompt combining the information types that helped on dev, with the rule fixed before pass 1 | Extension, see 2.3 |
| RQ3: up to five atomic claims citing code identifiers; static identifier check; a factored check that sees only the cited code and not the requirement; keep a link if the supported share reaches τ | Implemented this way (`harness/verify.py`) | Matches |
| 20% development / 80% test split per project; variants and τ chosen on dev, then frozen | Split fixed with seed 5187 before any RQ2 result; only dev has been run | Matches |
| On test: each variant, verification and the 2×2 (baseline or best prompt, with or without verification) against the baseline; Wilcoxon signed-rank on per-requirement F1, two-sided, α = 0.05, Holm | Planned this way (`harness/analyze.py test`) | Matches; still to run |
| RQ4: up to 100 coded errors in three pools, Cohen's κ; runtime and tokens per requirement on a laptop, median and IQR | Errors from the RQ3 test outputs; tokens from the saved answers; runtime from laptop runs (see 2.1) | Matches if the laptop timing runs happen |
| Threats to validity following Runeson and Höst [9] | Running list kept; variability is measured (see 2.2) | On track |
| Experiments on "a 24 GB Apple M5 laptop" / "our two laptops" | RQ1–RQ3 on a Google Colab L4 GPU; RQ1 also running on Rahul's laptop; RQ4 timings on Rahul's laptop | Change of hardware, see 2.1 |
| Milestones: RQ1 by Nov 14, RQ2–RQ3 by Nov 28, analysis by Dec 5, report mid-December | RQ1 (Colab) finished Nov 15; RQ2–RQ3 dev in progress; test planned Nov 17–21 | One day late on RQ1; on track otherwise |

## 2. The changes, with reasons

### 2.1 Colab GPU instead of laptops

**Why.** A smoke test on Rahul's laptop estimated about 27 hours for one RQ1 run (20,480 model calls). RQ2 and RQ3 need roughly three times as many calls again (over 60,000 classification calls on dev and test, plus verification), which would not fit in the course timeline on two laptops (one of them fanless).

**Why the results still answer the RQs.**
- **Same software, same models.** Ollama 0.40.2, the same 4-bit model files (Qwen digest `9ec8897f747e`, Llama digest `46e0c10c039e`), temperature 0, LiSSA's seed, the same context size. Only the chip doing the arithmetic differs.
- **Hardware affects only small details, and we measured it.** In our smoke tests, two GPU types (T4 and L4) gave identical KISS and retrieval results, and chain-of-thought differed by about 1 link in 40.
- **The models are still self-hosted.** RQ1 is about open models that an organisation runs itself instead of sending code to a cloud model's API. On Colab we run our own Ollama: no model provider receives any prompt, and the model version cannot change under us. The benchmark code is open source, so using a rented machine raises no privacy issue.
- **The laptop question is answered on a laptop.** RQ4's runtime per requirement is measured on Rahul's 24 GB M5 Pro, not taken from Colab. Rahul's laptop RQ1 run gives the timings of LiSSA's own prompts; a small timing sample covers the RQ2/RQ3 configurations.

**No paid API was used.** Colab compute comes from a subscription we already had; the proposal's constraint was about paid LLM APIs.

### 2.2 Answers vary slightly between runs

Temperature 0 makes a model pick its most likely word each time, but GPU arithmetic is not bit-identical from one session to the next, so close calls can flip.

| Measurement | Result |
|---|---|
| Same 20 RQ1 questions asked again in a later Colab session | identical text 8 of 20, identical yes/no 17 of 20 |
| Qwen dev baseline, RQ1's answers vs. a fresh run (strict parsing) | average F1 0.235 vs. 0.208 |
| Same, tolerant parsing | 0.337 vs. 0.332 |
| GPT-4o in LiSSA's own package, three runs with different seeds | links overlap only 79–88% (Jaccard), but average F1 varies by less than 0.01 (dev 0.385–0.394) |

**Why this is acceptable, and how we handle it.**
- It is a known threat: Sallou et al. [3] list output variability as a reproducibility threat, and OpenAI states that GPT-4o is not guaranteed to be deterministic either. Our variability is of the same kind as GPT-4o's own.
- We follow Sallou et al.'s two guidelines. (1) **Measure it:** the re-asks and repeated runs above, plus a 50-pair check per model in the current session. (2) **Record what ran:** model digests, Ollama version, seed, settings, GPU type, and every prompt and answer with its time, all in this repository.
- **Design:** all RQ2 comparisons on dev run in one Colab session (a fresh baseline was run for this reason); verification is compared within the same run; the test runs are split by requirement so that all configurations of a requirement are answered in the same session.
- **Reading the results:** differences smaller than the measured run-to-run difference are not treated as effects. "On par with GPT-4o" is judged against GPT-4o's own spread.
- Strict parsing varies more than tolerant parsing (0.027 vs. 0.005 above), because whether Qwen writes the `<trace>` tag changes between runs. This is reported as a finding.

### 2.3 Round-2 combination prompt

The proposal says RQ2 adds one piece of information at a time, and RQ2 is answered exactly that way by the four single variants.
For the 2×2 design we need the "best prompt". We also try one combination of the information types that helped on dev,
chosen by a rule fixed **before** pass 1 was seen. It is one more candidate for "best prompt", chosen on dev like every other choice.
The report will describe it as an extension.

### 2.4 RQ1 run with one seed

LiSSA's significance runs used five seeds. At temperature 0, the seed made no difference in our smoke tests, so we ran one seed (`133742243`, LiSSA's first). The variation that does exist comes from the GPU session, which section 2.2 measures.

### 2.5 Answer parsing: strict for all results, tolerant only in RQ4

**What the proposal says.** RQ1 metrics are computed "exactly as LiSSA does", and LiSSA is run "unchanged". RQ2–RQ3 report precision, recall and F1 and test per-requirement F1. The proposal names no second parsing rule.

**What we do.**
- **Strict parsing** is LiSSA's own rule: a link only if the answer's `<trace>` tag says yes; an answer without the tag counts as "no". It is used for **every reported result**: RQ1, the dev choices (best prompt, τ), all test comparisons, the Wilcoxon tests and the comparison with GPT-4o.
- **Tolerant parsing** is our addition: if the tag is missing, a "yes" or "no" at the very start of the answer is taken as the answer. It is **not** used for any RQ1–RQ3 result. It appears only in RQ4.

**Why tolerant parsing belongs in RQ4.** RQ4 asks which error types remain. One of the most frequent is a format error: the model answers but leaves out the required tag. Qwen does this in 65% of its chain-of-thought answers in RQ1 and in 70–78% on the dev slice; Llama in about 19% in RQ1. Under the strict rule each of these answers becomes "no", even when the answer starts with "Yes". Scoring the same answers with the tolerant rule shows how much F1 this one error type costs, which is a measurement of an error type, not a new evaluation metric.

**Why it is not used elsewhere.**
- The published GPT-4o numbers use only the strict rule. Tolerant scores for our models would have no GPT-4o counterpart, so a comparison would mix two rules.
- The proposal fixes the scoring to LiSSA's. Choosing prompts or τ, or running the Wilcoxon tests, with a different rule would change the study.

**What it shows so far (dev slice, Qwen):** strict average F1 0.17–0.21, tolerant 0.32–0.33 for the baseline, `definition` and `summary`. The added information hardly changes Qwen's actual yes/no judgement, but it makes Qwen leave out the tag more often.

## 3. Wording for the final report

**Setup:**
> A smoke test showed that one full RQ1 run takes about 27 hours on our 24 GB laptop, which made all RQ1–RQ3 configurations infeasible within the course timeline. We therefore ran RQ1–RQ3 with the identical software stack (Ollama 0.40.2, the same 4-bit model files, temperature 0, fixed seed, 16K context) on a single NVIDIA L4 GPU. No paid LLM API was used, and no model provider received any prompt. RQ4 runtimes were measured on a 24 GB M5 Pro laptop.

**Threats to validity, output variability** (fill in the bracketed numbers when the runs finish):
> We decode greedily (temperature 0, fixed seed), yet outputs are not bit-identical across GPU sessions, a reproducibility threat noted by Sallou et al. [3]. Following their guidelines, we measured it: re-asked prompts gave identical decisions in [X]% of cases within a session and 85% across sessions, and two full runs of the baseline on the development slice differed by 0.027 in average F1. LiSSA's own three GPT-4o runs have link-set Jaccard indices of 0.79–0.88 but differ by at most 0.009 in average F1. We ran all compared configurations of a slice in one session where possible, release all prompts, answers, model and runtime versions, and do not interpret differences smaller than the measured run-to-run difference.

**One sentence of the proposal to word more precisely.** The proposal says local open models "support reproducible research [3]". Sallou et al. warn that closed models change without notice; they do not claim that open models solve reproducibility. Suggested wording:
> Closed models can change without notice, a reproducibility threat noted by Sallou et al. [3]; open weights can be pinned to an exact version.

## 4. What must still happen for this to hold

1. **RQ4 timing runs on Rahul's laptop**, so that "runtime on a laptop" is measured on a laptop.
2. **Freeze before test:** write down the chosen prompt per model and τ, with the date and file hashes, before any test-slice call.
3. **Run the test slice once**, with every variant, verification and the 2×2, and the Wilcoxon tests as planned.
4. **Teamwork as planned:** Rahul leads the evaluation scripts, statistics, laptop runs and the threats section; both code the RQ4 errors independently.
5. **Score every RQ1–RQ3 result with LiSSA's strict rule**; use tolerant scores only in the RQ4 error analysis.
6. **State all changes** in sections 2.1–2.5 in the report.
