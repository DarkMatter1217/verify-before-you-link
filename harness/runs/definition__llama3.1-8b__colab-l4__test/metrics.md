# definition with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 105 | 222 | 644 | 80 | 564 | 142 | 0.124 | 0.360 | 0.185 | 0.261 |
| Avg. |  |  |  |  |  |  | 0.292 | 0.407 | 0.313 | 0.354 |
| w. Avg. |  |  |  |  |  |  | 0.373 | 0.367 | 0.344 | 0.348 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 105 | 222 | 644 | 80 | 564 | 142 | 0.124 | 0.360 | 0.185 | 0.261 |
| Avg. |  |  |  |  |  |  | 0.292 | 0.407 | 0.313 | 0.354 |
| w. Avg. |  |  |  |  |  |  | 0.373 | 0.367 | 0.344 | 0.348 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 198; cut at 4096 answer tokens: 33
- Per call: median 4.4 s (IQR 3.3-5.8 s, n = 4100)
- Per requirement: median 95.9 s (IQR 84.7-113.2 s, n = 205)
