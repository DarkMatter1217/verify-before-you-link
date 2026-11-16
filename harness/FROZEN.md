# Frozen choices for the test slice

Written and approved on 16 November 2026, after the dev passes finished (11:26 UTC) and **before any test-slice call**.
Nothing below may change once the test runs start.

## Choices (made on the dev slice by rules fixed before any result was seen)

| Choice | Rule | Result |
|---|---|---|
| Best prompt, Qwen2.5-Coder-14B | Highest dev average F1 (strict) among the baseline, the four variants and the round-2 combination | `examples` (0.308; definition+examples 0.307) |
| Best prompt, Llama-3.1-8B | Same | `definition+summary` (0.316) |
| τ for verification | Highest average F1 of the baseline's dev verification, from {0.2, 0.4, 0.6, 0.8, 1.0}; ties go to the smaller τ | 0.2 |
| Answer parsing | LiSSA's rule (strict) for all results; tolerant only in RQ4 | strict |
| Verification details | "Unclear" is not support; a link without claims has share 0 | as stated |
| Wilcoxon tests | Two-sided, α = 0.05, Holm over the comparisons of one model; requirements without gold links left out | as stated |

## What runs on the test slice (205 requirements: SMOS 54, eTour 46, iTrust 105)

Per model, as the proposal says: the baseline, each of the four variants, the best prompt, and verification of the baseline and of the best prompt (the 2×2).

| Model | Classification runs | Verification runs (τ = 0.2 reported) |
|---|---|---|
| Qwen2.5-Coder-14B | baseline, definition, summary, project, examples | baseline, examples |
| Llama-3.1-8B | baseline, definition, summary, project, examples, definition+summary | baseline, definition+summary |

The round-2 combination of Qwen (definition+examples) is not run on test, because it is not Qwen's best prompt.

## Settings and files (the same as on dev)

| Item | Value |
|---|---|
| Ollama | 0.40.2, one request at a time, context 16,384, answers capped at 4,096 tokens |
| Decoding | temperature 0, seed 133742243 |
| Qwen digest | `9ec8897f747e246e970bc5cfdda85d22f1123dc2e3d34978a010a75968716849` |
| Llama digest | `46e0c10c039e019119339687c3c1757cc81b9da49709a3b3924863ba87ca666e` |
| GPU | NVIDIA L4 (Google Colab), answers saved under `colab-l4` |
| `data/split.json` | `f62dd9ab7d3c63a8f53994eb3da1bfeb600152b06156a2be2e51e20d05505e33` |
| `data/candidates-rq1.json` | `7cde755d62b57db7a2f2bdae62ad88992f233b845495107e69cda9ee8b6a6b14` |

SHA-256 prefixes of the prompt files: `definition.txt` feeac325a38475d0, `project-SMOS.txt` a3e7140aef47aa99, `project-eTour_en.txt` 5cfd4874c62937e2, `project-iTrust.txt` cfed41a06991d6a6, `examples-SMOS.txt` 56b637814b50d714, `examples-eTour_en.txt` 9227d00d8a011cb2, `examples-iTrust.txt` 8db381c32db87ff4, `claims.txt` 908d580239517476, `check.txt` 1b494b20cfa7e01c.

Harness code as it ran on Colab (from each run's `run.json`): `lissa_compat.py` 1d6613ff894c8cbe, `llm.py` 6b80cc95092d87e5, `variants.py` 69580753ceddd246, `run.py` d73e34880c32e187, `javaparse.py` a1fb3fb159a60689.

## Reference: GPT-4o chain-of-thought on the same test slice (LiSSA's own links)

| Seed | SMOS | eTour | iTrust | Average F1 |
|---|---|---|---|---|
| 133742243 | 0.294 | 0.485 | 0.277 | 0.352 |
| 35418170 | 0.292 | 0.487 | 0.282 | 0.354 |
| 83939039 | 0.286 | 0.490 | 0.282 | 0.353 |

## How the test slice is run

`colab/lissa_pipeline_test.sh`: per model, the requirements are processed in chunks (the first 10, 20, …, 110 per project), so all configurations of a requirement are answered close together. Every answer is saved, finished chunks are skipped after a session restart, and a final pass scores the whole slice.
