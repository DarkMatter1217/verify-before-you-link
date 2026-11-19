# definition+summary with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 468 | 233 | 235 | 595 | 0.498 | 0.281 | 0.360 | 0.308 |
| eTour_en | 46 | 235 | 356 | 117 | 239 | 118 | 0.329 | 0.498 | 0.396 | 0.451 |
| iTrust | 80 | 174 | 472 | 55 | 417 | 119 | 0.117 | 0.316 | 0.170 | 0.235 |
| Avg. |  |  |  |  |  |  | 0.314 | 0.365 | 0.309 | 0.332 |
| w. Avg. |  |  |  |  |  |  | 0.412 | 0.327 | 0.340 | 0.325 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 468 | 233 | 235 | 595 | 0.498 | 0.281 | 0.360 | 0.308 |
| eTour_en | 46 | 235 | 356 | 117 | 239 | 118 | 0.329 | 0.498 | 0.396 | 0.451 |
| iTrust | 80 | 174 | 472 | 55 | 417 | 119 | 0.117 | 0.316 | 0.170 | 0.235 |
| Avg. |  |  |  |  |  |  | 0.314 | 0.365 | 0.309 | 0.332 |
| w. Avg. |  |  |  |  |  |  | 0.412 | 0.327 | 0.340 | 0.325 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 262; cut at 4096 answer tokens: 24
- Per call: median 5.0 s (IQR 3.8-6.4 s, n = 3600)
- Per requirement: median 109.6 s (IQR 97.4-122.7 s, n = 180)
