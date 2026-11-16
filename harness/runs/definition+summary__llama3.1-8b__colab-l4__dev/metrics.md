# definition+summary with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 94 | 46 | 48 | 170 | 0.489 | 0.213 | 0.297 | 0.240 |
| eTour_en | 12 | 73 | 99 | 39 | 60 | 34 | 0.394 | 0.534 | 0.453 | 0.499 |
| iTrust | 26 | 64 | 127 | 19 | 108 | 45 | 0.150 | 0.297 | 0.199 | 0.248 |
| Avg. |  |  |  |  |  |  | 0.344 | 0.348 | 0.316 | 0.329 |
| w. Avg. |  |  |  |  |  |  | 0.408 | 0.295 | 0.311 | 0.295 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 94 | 46 | 48 | 170 | 0.489 | 0.213 | 0.297 | 0.240 |
| eTour_en | 12 | 73 | 99 | 39 | 60 | 34 | 0.394 | 0.534 | 0.453 | 0.499 |
| iTrust | 26 | 64 | 127 | 19 | 108 | 45 | 0.150 | 0.297 | 0.199 | 0.248 |
| Avg. |  |  |  |  |  |  | 0.344 | 0.348 | 0.316 | 0.329 |
| w. Avg. |  |  |  |  |  |  | 0.408 | 0.295 | 0.311 | 0.295 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 76; cut at 4096 answer tokens: 7
- Per call: median 4.9 s (IQR 3.8-6.3 s, n = 1020)
- Per requirement: median 107.9 s (IQR 97.2-120.9 s, n = 51)
