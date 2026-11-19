# baseline with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 80 | 174 | 1131 | 63 | 1068 | 111 | 0.056 | 0.362 | 0.097 | 0.172 |
| Avg. |  |  |  |  |  |  | 0.204 | 0.465 | 0.260 | 0.335 |
| w. Avg. |  |  |  |  |  |  | 0.289 | 0.449 | 0.331 | 0.378 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 80 | 174 | 1131 | 63 | 1068 | 111 | 0.056 | 0.362 | 0.097 | 0.172 |
| Avg. |  |  |  |  |  |  | 0.204 | 0.465 | 0.260 | 0.335 |
| w. Avg. |  |  |  |  |  |  | 0.289 | 0.449 | 0.331 | 0.378 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 549; cut at 4096 answer tokens: 41
- Per call: median 4.6 s (IQR 3.6-5.7 s, n = 3600)
- Per requirement: median 100.1 s (IQR 89.2-118.6 s, n = 180)
