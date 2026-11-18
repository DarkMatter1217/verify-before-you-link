# Code changes

This file lists every change we made to LiSSA's code, why, and what we added around it.
LiSSA's method (prompts, retrieval, link decisions, metrics) is unchanged.

Original code: the official LiSSA replication package, commit `a8e652f`
([GitHub](https://github.com/ardoco/ReplicationPackage-ICSE25_LiSSA-Toward-Generic-Traceability-Link-Recovery-through-RAG),
[Zenodo](https://doi.org/10.5281/zenodo.14714706)).

## 1. Changes to LiSSA's own code: two Java files

The full line-by-line difference is saved by each RQ1 run, in
[`LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/lissa-vs-upstream.diff`](../LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/lissa-vs-upstream.diff) (laptop, the main run)
and [`LiSSA-RATLR-V2/lissa/results-local/rq1/lissa-vs-upstream.diff`](../LiSSA-RATLR-V2/lissa/results-local/rq1/lissa-vs-upstream.diff) (Colab).
Both contain the same changed lines. Nothing else in LiSSA's Java code differs from the original.

### 1.1 `ChatLanguageModelProvider.java` (16 lines added, 3 changed)

Path: `LiSSA-RATLR-V2/lissa/src/main/java/edu/kit/kastel/sdq/lissa/ratlr/classifier/`

| What | Value | Why |
|---|---|---|
| Context size sent to Ollama (`num_ctx`) | 16,384 tokens | Without it, Ollama uses its own small default (often 4,096 tokens) and **silently cuts** longer prompts. The longest prompt in our data is about 10,200 tokens. GPT-4o, used in the original runs, had no such limit at this size. |
| Maximum answer length (`num_predict`) | 4,096 tokens | The answer limit of the GPT-4o version that produced the original results. Without a limit, a local model caught repeating itself never stops. |

Both values can be changed in a configuration file; the defaults above were used in every run.
Temperature 0 and LiSSA's seed were already set by the original code and are unchanged.

### 1.2 `OllamaEmbeddingCreator.java` (104 lines added, 8 removed)

Path: `LiSSA-RATLR-V2/lissa/src/main/java/edu/kit/kastel/sdq/lissa/ratlr/embeddingcreator/`

- **Problem:** the original code asks Ollama for embeddings through an old endpoint (`/api/embeddings`, through the LangChain4j library version LiSSA uses). That endpoint **fails with an error (HTTP 500) on long code files**, so retrieval could not run on our data.
- **Fix:** a small replacement class calls Ollama's current endpoint (`/api/embed`) instead. Long inputs are cut at 8,192 tokens, the input limit of bge-m3. LiSSA's original OpenAI path also cuts long inputs to the embedding model's limit, so both paths now behave the same way.
- **What stays the same:** the vectors are still saved in LiSSA's cache and used by LiSSA's unchanged retrieval (cosine similarity, top 20).

This is why the change is larger than a few lines: it replaces one library call with a direct request. Its effect on the method is only that long files are embedded at all.

## 2. Files we added (not changes to LiSSA)

| File or folder | What it does |
|---|---|
| `run_rq1_benchmark.py` | Runs RQ1: LiSSA unchanged with Ollama, every configuration, then builds `rq1-report.md` with the published GPT-4o, GPT-4o-mini, VSM, LSI and FTLR numbers next to ours. Resumes after a stop. |
| `reports/compare_rq1_runs.py` | Compares the laptop and Colab RQ1 runs: shared candidate pairs, same decisions, link overlap, F1. Writes `reports/rq1-laptop-vs-colab.md`. |
| `reports/rq1_laptop_timing.py` | RQ4: time per question and per requirement of the laptop RQ1 run, from LiSSA's time-stamped logs. Writes `rq1-laptop/timing.md`. |
| `LiSSA-RATLR-V2/lissa/local/` | Helpers for the runner: model settings (`models.conf`), a check that each model loads fully on the GPU before a run (`preflight.py`), configuration generation and result summaries. |
| `LiSSA-RATLR-V2/lissa/env-template-ollama` | Tells LiSSA where Ollama runs. |
| `harness/` | Our Python code for RQ2 (prompt variants), RQ3 (claim verification) and the analysis (Wilcoxon, Holm). It copies LiSSA's prompt, retrieval candidates, answer parsing and metrics exactly. `harness/selftest.py` and `harness/check_rq1.py` prove this against LiSSA's own files. |
| `colab/` | The two Colab notebooks and three scripts that ran RQ1–RQ3. See [`colab/README.md`](../colab/README.md). |

## 3. Running on Google Colab: no code changes

Colab needed only setup steps in the notebook, no change to any code:

1. Install Java 21, Maven and Ollama 0.40.2, the same version in every Colab notebook. Rahul's laptop used Ollama 0.40.14 for the main RQ1 run. The hardware and the version differ together between the two RQ1 runs; [`rq1-laptop-vs-colab.md`](rq1-laptop-vs-colab.md) measures how much the results differ.
2. The RQ1 runner finds Java 21 with a macOS tool (`/usr/libexec/java_home`). On Colab, the notebook creates a two-line stand-in that returns the Java 21 folder.
3. Start Ollama with `OLLAMA_CONTEXT_LENGTH=16384` (same context as above) and `OLLAMA_NUM_PARALLEL=1` (one request at a time, as on a laptop).
4. Pass `--device colab-l4` to the harness, so answers from the Colab GPU are saved separately from answers produced on a laptop and are never mixed in one run.

## 4. Changes to our own harness while running (15 Nov 2026)

| File | Change | Effect on results |
|---|---|---|
| `harness/evaluate.py` | Bug fix: the link-weighted average also tried to include the plain-average row and stopped with an error. Both averages are now computed from the project rows only. | None on numbers; the average could not be computed before. |
| `harness/variants.py` | Added the round-2 prompts that combine several kinds of information. | None on the single variants: their prompts are unchanged, character for character (`selftest.py` checks this). |
| `harness/prepare_prompts.py` | The length check covers the single variants; the combination is checked when it is chosen. | None. |

These three files ran on Colab with SHA-256 prefixes `d2a54b44634c`, `0037b645a15c` and `69580753cedd`.

## 5. Plain-English comments (15 Nov 2026)

After the runs, the comments and docstrings in `harness/*.py` and `run_rq1_benchmark.py` were rewritten in plain English.
**The code itself did not change.** We checked this by comparing the parsed code of every file before and after, with docstrings removed.
Because comments are part of a file's bytes, the file hashes stored in each run's `run.json` belong to the earlier wording.
The Colab scripts in `colab/` are byte-for-byte the versions that ran.
