# definition+summary with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 262 | 147 | 115 | 357 | 0.561 | 0.292 | 0.384 | 0.323 |
| eTour_en | 30 | 156 | 227 | 80 | 147 | 76 | 0.352 | 0.513 | 0.418 | 0.470 |
| iTrust | 30 | 58 | 194 | 20 | 174 | 38 | 0.103 | 0.345 | 0.159 | 0.235 |
| Avg. |  |  |  |  |  |  | 0.339 | 0.383 | 0.320 | 0.342 |
| w. Avg. |  |  |  |  |  |  | 0.479 | 0.344 | 0.373 | 0.348 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 262 | 147 | 115 | 357 | 0.561 | 0.292 | 0.384 | 0.323 |
| eTour_en | 30 | 156 | 227 | 80 | 147 | 76 | 0.352 | 0.513 | 0.418 | 0.470 |
| iTrust | 30 | 58 | 194 | 20 | 174 | 38 | 0.103 | 0.345 | 0.159 | 0.235 |
| Avg. |  |  |  |  |  |  | 0.339 | 0.383 | 0.320 | 0.342 |
| w. Avg. |  |  |  |  |  |  | 0.479 | 0.344 | 0.373 | 0.348 |

- Pairs: 1800; answers from {'ollama': 580, 'harness-cache': 1220, 'lissa-rq1': 0}
- Without a <trace> tag: 131; cut at 4096 answer tokens: 12
- Per call: median 5.1 s (IQR 3.8-6.6 s, n = 1800)
- Per requirement: median 112.1 s (IQR 98.2-124.2 s, n = 90)
