# baseline with qwen2.5-coder:14b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 57 | 43 | 14 | 301 | 0.754 | 0.125 | 0.214 | 0.150 |
| eTour_en | 20 | 101 | 79 | 35 | 44 | 66 | 0.443 | 0.347 | 0.389 | 0.362 |
| iTrust | 20 | 42 | 82 | 11 | 71 | 31 | 0.134 | 0.262 | 0.177 | 0.220 |
| Avg. |  |  |  |  |  |  | 0.444 | 0.244 | 0.260 | 0.244 |
| w. Avg. |  |  |  |  |  |  | 0.636 | 0.183 | 0.247 | 0.200 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 90 | 68 | 22 | 276 | 0.756 | 0.198 | 0.313 | 0.232 |
| eTour_en | 20 | 101 | 117 | 61 | 56 | 40 | 0.521 | 0.604 | 0.560 | 0.585 |
| iTrust | 20 | 42 | 91 | 18 | 73 | 24 | 0.198 | 0.429 | 0.271 | 0.347 |
| Avg. |  |  |  |  |  |  | 0.492 | 0.410 | 0.381 | 0.388 |
| w. Avg. |  |  |  |  |  |  | 0.659 | 0.302 | 0.361 | 0.315 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 780; cut at 4096 answer tokens: 0
- Per call: median 4.0 s (IQR 3.0-5.7 s, n = 1200)
- Per requirement: median 91.3 s (IQR 79.0-107.2 s, n = 60)
