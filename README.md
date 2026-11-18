# Verify Before You Link: Local LLMs for Requirements Traceability

Course project for CSI5187 (Applications of NLP and ML in Software Engineering), University of Ottawa, Fall 2026.
**Team:** Prabhjot Singh and Rahul.

Trace links tell which code implements which requirement. They support change impact analysis, maintenance and certification, but developers rarely keep them up to date by hand.
LiSSA (Fuchß et al., ICSE 2025) recovers them automatically: it retrieves the 20 code files most similar to a requirement and asks GPT-4o whether each one is linked. This project:

- **RQ1:** runs LiSSA unchanged with free, self-hosted open models (Qwen2.5-Coder-14B, Llama-3.1-8B) on a laptop and compares them with GPT-4o;
- **RQ2:** tests which added information in the prompt helps (a trace-link definition, a code summary, a project description, labelled examples);
- **RQ3:** keeps a link only if the model's justification, split into small claims, is confirmed by the code itself;
- **RQ4:** analyses the remaining errors and the runtime per requirement on a laptop.

## Start here

| Read | For |
|---|---|
| [`proposal/`](proposal/) | The submitted proposal (Word and PDF) |
| [`project-flow/`](project-flow/README.md) | Current state, next steps, and how each step is done |
| [`reports/progress-report.md`](reports/progress-report.md) | Progress report with the results so far |
| [`reports/proposal-compliance.md`](reports/proposal-compliance.md) | How the setup still matches the proposal, with reasons |
| [`reports/code-changes.md`](reports/code-changes.md) | Every change to LiSSA's code, and why |
| [`reports/test-timeline.md`](reports/test-timeline.md) | The test-slice run stage by stage, with the results at each stage |
| [`reports/rq1-laptop-vs-colab.md`](reports/rq1-laptop-vs-colab.md) | How the two RQ1 runs (laptop and Colab) compare |
| [`results/`](results/README.md) | Where every result is, with the main numbers |

## Repository layout

| Path | Contents |
|---|---|
| `LiSSA-RATLR-V2/lissa/` | LiSSA's code, the SMOS, eTour and iTrust data, and LiSSA's own GPT-4o results, from the official replication package. Only two Java files changed (see `reports/code-changes.md`). |
| `LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/` | **RQ1, main result:** the run on Rahul's laptop (MacBook Pro, M5 Pro, 24 GB), with its logs, Ollama logs and the time per requirement (`timing.md`) |
| `LiSSA-RATLR-V2/lissa/cache-local-r2c-laptop/` | The laptop run's saved model answers and embeddings |
| `LiSSA-RATLR-V2/lissa/results-local/rq1/` | RQ1, second run, on a Colab L4 GPU. RQ2 and RQ3 use this run's candidate pairs |
| `LiSSA-RATLR-V2/lissa/cache-local-r2c/` | The Colab run's saved model answers and embeddings |
| `run_rq1_benchmark.py` | Runs RQ1 and writes `rq1-report.md` |
| `harness/` | Our Python code for RQ2, RQ3 and the analysis, with its inputs (`data/`, `prompts/`), runs (`runs/`) and saved answers (`cache/`) |
| `colab/` | The Colab notebooks and scripts that ran RQ1–RQ3 |
| `Evaluation-Req2Code.xlsx` | LiSSA's published numbers, read only (the RQ1 report compares against them) |

Only deliverables are kept here. Left out: LiSSA V1, the architecture-documentation datasets and results, the Dronology projects (their code is not redistributed, and the proposal excludes them), the Docker files, the paper preprint, LiSSA's statistics scripts, earlier laptop runners and working notes, and temporary files from the runs.

## Running it

**Requirements:** Java 21, Maven, Ollama with `qwen2.5-coder:14b`, `llama3.1:8b` and `bge-m3` (we used 0.40.14 on the laptop and 0.40.2 on Colab), and Python 3 with `pip install -r harness/requirements.txt`.
Start Ollama with `OLLAMA_CONTEXT_LENGTH=16384`.

```bash
# Build LiSSA
cd LiSSA-RATLR-V2/lissa && mvn -q package -DskipTests && cd ../..

# RQ1 (one seed); run the same command again to continue after a stop. Writes to results-local/rq1/
python3 run_rq1_benchmark.py --seeds 1

# RQ1: compare the laptop and Colab runs; time per requirement on the laptop (RQ4)
python3 reports/compare_rq1_runs.py --out reports/rq1-laptop-vs-colab.md
python3 reports/rq1_laptop_timing.py --out LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/timing.md

# RQ2 and RQ3 (see harness/README.md)
python3 harness/selftest.py
python3 harness/run.py --variant baseline --model qwen2.5-coder:14b --slice dev
python3 harness/verify.py --run harness/runs/<run folder> --parser strict
python3 harness/analyze.py --parser strict table harness/runs/<run folder>
```

[`colab/README.md`](colab/README.md) describes exactly how the reported runs were made on Colab.
All model answers are saved, so every table can be recomputed without calling a model again.

## Credits

- LiSSA and its replication package: D. Fuchß, T. Hey, J. Keim, H. Liu, N. Ewald, T. Thirolf, A. Koziolek, ICSE 2025, [doi:10.5281/zenodo.14714706](https://doi.org/10.5281/zenodo.14714706). MIT licence: [`LiSSA-RATLR-V2/LICENSE-replication-package.md`](LiSSA-RATLR-V2/LICENSE-replication-package.md).
- Datasets: the CoEST traceability datasets (SMOS, eTour, iTrust), as distributed with LiSSA's package.
