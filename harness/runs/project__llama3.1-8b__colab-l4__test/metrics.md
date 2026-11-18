# project with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 561 | 218 | 343 | 286 | 0.389 | 0.433 | 0.409 | 0.423 |
| eTour_en | 30 | 156 | 518 | 101 | 417 | 55 | 0.195 | 0.647 | 0.300 | 0.442 |
| iTrust | 30 | 58 | 491 | 19 | 472 | 39 | 0.039 | 0.328 | 0.069 | 0.131 |
| Avg. |  |  |  |  |  |  | 0.207 | 0.469 | 0.259 | 0.332 |
| w. Avg. |  |  |  |  |  |  | 0.318 | 0.471 | 0.358 | 0.404 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 561 | 218 | 343 | 286 | 0.389 | 0.433 | 0.409 | 0.423 |
| eTour_en | 30 | 156 | 518 | 101 | 417 | 55 | 0.195 | 0.647 | 0.300 | 0.442 |
| iTrust | 30 | 58 | 492 | 20 | 472 | 38 | 0.041 | 0.345 | 0.073 | 0.138 |
| Avg. |  |  |  |  |  |  | 0.208 | 0.475 | 0.261 | 0.334 |
| w. Avg. |  |  |  |  |  |  | 0.318 | 0.472 | 0.358 | 0.404 |

- Pairs: 1800; answers from {'ollama': 580, 'harness-cache': 1220, 'lissa-rq1': 0}
- Without a <trace> tag: 117; cut at 4096 answer tokens: 13
- Per call: median 5.0 s (IQR 3.9-6.0 s, n = 1800)
- Per requirement: median 104.7 s (IQR 93.1-116.4 s, n = 90)
