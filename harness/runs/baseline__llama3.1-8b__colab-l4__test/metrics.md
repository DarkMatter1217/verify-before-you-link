# baseline with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 353 | 144 | 209 | 200 | 0.408 | 0.419 | 0.413 | 0.416 |
| eTour_en | 20 | 101 | 327 | 71 | 256 | 30 | 0.217 | 0.703 | 0.332 | 0.486 |
| iTrust | 20 | 42 | 281 | 20 | 261 | 22 | 0.071 | 0.476 | 0.124 | 0.223 |
| Avg. |  |  |  |  |  |  | 0.232 | 0.533 | 0.290 | 0.375 |
| w. Avg. |  |  |  |  |  |  | 0.339 | 0.483 | 0.371 | 0.414 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 353 | 144 | 209 | 200 | 0.408 | 0.419 | 0.413 | 0.416 |
| eTour_en | 20 | 101 | 327 | 71 | 256 | 30 | 0.217 | 0.703 | 0.332 | 0.486 |
| iTrust | 20 | 42 | 281 | 20 | 261 | 22 | 0.071 | 0.476 | 0.124 | 0.223 |
| Avg. |  |  |  |  |  |  | 0.232 | 0.533 | 0.290 | 0.375 |
| w. Avg. |  |  |  |  |  |  | 0.339 | 0.483 | 0.371 | 0.414 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 176; cut at 4096 answer tokens: 16
- Per call: median 4.5 s (IQR 3.5-5.7 s, n = 1200)
- Per requirement: median 100.5 s (IQR 89.8-151.6 s, n = 60)
