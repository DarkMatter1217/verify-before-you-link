# definition with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 321 | 161 | 160 | 343 | 0.502 | 0.319 | 0.390 | 0.344 |
| eTour_en | 30 | 156 | 284 | 89 | 195 | 67 | 0.313 | 0.571 | 0.405 | 0.490 |
| iTrust | 30 | 58 | 183 | 21 | 162 | 37 | 0.115 | 0.362 | 0.174 | 0.253 |
| Avg. |  |  |  |  |  |  | 0.310 | 0.417 | 0.323 | 0.363 |
| w. Avg. |  |  |  |  |  |  | 0.429 | 0.377 | 0.376 | 0.369 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 321 | 161 | 160 | 343 | 0.502 | 0.319 | 0.390 | 0.344 |
| eTour_en | 30 | 156 | 284 | 89 | 195 | 67 | 0.313 | 0.571 | 0.405 | 0.490 |
| iTrust | 30 | 58 | 183 | 21 | 162 | 37 | 0.115 | 0.362 | 0.174 | 0.253 |
| Avg. |  |  |  |  |  |  | 0.310 | 0.417 | 0.323 | 0.363 |
| w. Avg. |  |  |  |  |  |  | 0.429 | 0.377 | 0.376 | 0.369 |

- Pairs: 1800; answers from {'ollama': 0, 'harness-cache': 1800, 'lissa-rq1': 0}
- Without a <trace> tag: 90; cut at 4096 answer tokens: 16
- Per call: median 4.6 s (IQR 3.4-5.9 s, n = 1800)
- Per requirement: median 100.6 s (IQR 90.1-119.2 s, n = 90)
