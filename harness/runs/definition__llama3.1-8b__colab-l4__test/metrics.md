# definition with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 80 | 174 | 483 | 58 | 425 | 116 | 0.120 | 0.333 | 0.177 | 0.246 |
| Avg. |  |  |  |  |  |  | 0.290 | 0.398 | 0.310 | 0.349 |
| w. Avg. |  |  |  |  |  |  | 0.382 | 0.363 | 0.349 | 0.350 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 569 | 264 | 305 | 564 | 0.464 | 0.319 | 0.378 | 0.340 |
| eTour_en | 46 | 235 | 442 | 127 | 315 | 108 | 0.287 | 0.540 | 0.375 | 0.459 |
| iTrust | 80 | 174 | 483 | 58 | 425 | 116 | 0.120 | 0.333 | 0.177 | 0.246 |
| Avg. |  |  |  |  |  |  | 0.290 | 0.398 | 0.310 | 0.349 |
| w. Avg. |  |  |  |  |  |  | 0.382 | 0.363 | 0.349 | 0.350 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 172; cut at 4096 answer tokens: 28
- Per call: median 4.5 s (IQR 3.4-5.9 s, n = 3600)
- Per requirement: median 98.1 s (IQR 86.6-114.7 s, n = 180)
