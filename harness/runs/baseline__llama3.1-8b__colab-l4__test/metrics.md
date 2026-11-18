# baseline with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 529 | 206 | 323 | 298 | 0.389 | 0.409 | 0.399 | 0.405 |
| eTour_en | 30 | 156 | 480 | 100 | 380 | 56 | 0.208 | 0.641 | 0.314 | 0.453 |
| iTrust | 30 | 58 | 438 | 22 | 416 | 36 | 0.050 | 0.379 | 0.089 | 0.164 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.476 | 0.267 | 0.341 |
| w. Avg. |  |  |  |  |  |  | 0.323 | 0.457 | 0.355 | 0.396 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 529 | 206 | 323 | 298 | 0.389 | 0.409 | 0.399 | 0.405 |
| eTour_en | 30 | 156 | 480 | 100 | 380 | 56 | 0.208 | 0.641 | 0.314 | 0.453 |
| iTrust | 30 | 58 | 438 | 22 | 416 | 36 | 0.050 | 0.379 | 0.089 | 0.164 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.476 | 0.267 | 0.341 |
| w. Avg. |  |  |  |  |  |  | 0.323 | 0.457 | 0.355 | 0.396 |

- Pairs: 1800; answers from {'ollama': 0, 'harness-cache': 1800, 'lissa-rq1': 0}
- Without a <trace> tag: 251; cut at 4096 answer tokens: 21
- Per call: median 4.6 s (IQR 3.6-5.7 s, n = 1800)
- Per requirement: median 101.8 s (IQR 89.6-126.6 s, n = 90)
