# definition with llama3.1:8b on colab-l4, test slice (first 90 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 90 | 191 | 524 | 68 | 456 | 123 | 0.130 | 0.356 | 0.190 | 0.264 |
| Avg. |  |  |  |  |  |  | 0.294 | 0.405 | 0.314 | 0.355 |
| w. Avg. |  |  |  |  |  |  | 0.380 | 0.366 | 0.349 | 0.351 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 90 | 191 | 524 | 68 | 456 | 123 | 0.130 | 0.356 | 0.190 | 0.264 |
| Avg. |  |  |  |  |  |  | 0.294 | 0.405 | 0.314 | 0.355 |
| w. Avg. |  |  |  |  |  |  | 0.380 | 0.366 | 0.349 | 0.351 |

- Pairs: 3800; answers from {'ollama': 200, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 187; cut at 4096 answer tokens: 31
- Per call: median 4.5 s (IQR 3.4-5.8 s, n = 3800)
- Per requirement: median 97.7 s (IQR 86.1-114.8 s, n = 190)
