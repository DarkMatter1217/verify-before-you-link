# baseline with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 234 | 85 | 149 | 131 | 0.363 | 0.394 | 0.378 | 0.387 |
| eTour_en | 12 | 73 | 195 | 51 | 144 | 22 | 0.262 | 0.699 | 0.381 | 0.524 |
| iTrust | 26 | 64 | 363 | 18 | 345 | 46 | 0.050 | 0.281 | 0.084 | 0.145 |
| Avg. |  |  |  |  |  |  | 0.225 | 0.458 | 0.281 | 0.352 |
| w. Avg. |  |  |  |  |  |  | 0.285 | 0.436 | 0.325 | 0.371 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 234 | 85 | 149 | 131 | 0.363 | 0.394 | 0.378 | 0.387 |
| eTour_en | 12 | 73 | 195 | 51 | 144 | 22 | 0.262 | 0.699 | 0.381 | 0.524 |
| iTrust | 26 | 64 | 363 | 18 | 345 | 46 | 0.050 | 0.281 | 0.084 | 0.145 |
| Avg. |  |  |  |  |  |  | 0.225 | 0.458 | 0.281 | 0.352 |
| w. Avg. |  |  |  |  |  |  | 0.285 | 0.436 | 0.325 | 0.371 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 154; cut at 4096 answer tokens: 8
- Per call: median 4.5 s (IQR 3.6-5.6 s, n = 1020)
- Per requirement: median 98.5 s (IQR 86.9-109.8 s, n = 51)
