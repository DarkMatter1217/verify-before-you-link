# project with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 381 | 151 | 230 | 193 | 0.396 | 0.439 | 0.417 | 0.430 |
| eTour_en | 20 | 101 | 357 | 71 | 286 | 30 | 0.199 | 0.703 | 0.310 | 0.466 |
| iTrust | 20 | 42 | 315 | 18 | 297 | 24 | 0.057 | 0.429 | 0.101 | 0.186 |
| Avg. |  |  |  |  |  |  | 0.217 | 0.523 | 0.276 | 0.361 |
| w. Avg. |  |  |  |  |  |  | 0.326 | 0.493 | 0.367 | 0.416 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 381 | 151 | 230 | 193 | 0.396 | 0.439 | 0.417 | 0.430 |
| eTour_en | 20 | 101 | 357 | 71 | 286 | 30 | 0.199 | 0.703 | 0.310 | 0.466 |
| iTrust | 20 | 42 | 316 | 19 | 297 | 23 | 0.060 | 0.452 | 0.106 | 0.196 |
| Avg. |  |  |  |  |  |  | 0.218 | 0.531 | 0.278 | 0.364 |
| w. Avg. |  |  |  |  |  |  | 0.326 | 0.495 | 0.368 | 0.417 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 73; cut at 4096 answer tokens: 10
- Per call: median 4.9 s (IQR 3.9-5.9 s, n = 1200)
- Per requirement: median 105.4 s (IQR 93.9-114.2 s, n = 60)
