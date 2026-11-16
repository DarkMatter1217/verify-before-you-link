# summary with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 188 | 75 | 113 | 141 | 0.399 | 0.347 | 0.371 | 0.356 |
| eTour_en | 12 | 73 | 180 | 48 | 132 | 25 | 0.267 | 0.658 | 0.379 | 0.508 |
| iTrust | 26 | 64 | 296 | 19 | 277 | 45 | 0.064 | 0.297 | 0.106 | 0.172 |
| Avg. |  |  |  |  |  |  | 0.243 | 0.434 | 0.285 | 0.346 |
| w. Avg. |  |  |  |  |  |  | 0.311 | 0.402 | 0.325 | 0.354 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 188 | 75 | 113 | 141 | 0.399 | 0.347 | 0.371 | 0.356 |
| eTour_en | 12 | 73 | 180 | 48 | 132 | 25 | 0.267 | 0.658 | 0.379 | 0.508 |
| iTrust | 26 | 64 | 296 | 19 | 277 | 45 | 0.064 | 0.297 | 0.106 | 0.172 |
| Avg. |  |  |  |  |  |  | 0.243 | 0.434 | 0.285 | 0.346 |
| w. Avg. |  |  |  |  |  |  | 0.311 | 0.402 | 0.325 | 0.354 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 243; cut at 4096 answer tokens: 8
- Per call: median 5.6 s (IQR 4.4-7.0 s, n = 1020)
- Per requirement: median 121.2 s (IQR 109.2-132.2 s, n = 51)
