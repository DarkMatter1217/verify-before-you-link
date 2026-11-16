# examples with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 26 | 15 | 11 | 201 | 0.577 | 0.069 | 0.124 | 0.084 |
| eTour_en | 12 | 73 | 50 | 34 | 16 | 39 | 0.680 | 0.466 | 0.553 | 0.497 |
| iTrust | 26 | 64 | 58 | 15 | 43 | 49 | 0.259 | 0.234 | 0.246 | 0.239 |
| Avg. |  |  |  |  |  |  | 0.505 | 0.257 | 0.308 | 0.273 |
| w. Avg. |  |  |  |  |  |  | 0.541 | 0.181 | 0.235 | 0.198 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 26 | 15 | 11 | 201 | 0.577 | 0.069 | 0.124 | 0.084 |
| eTour_en | 12 | 73 | 50 | 34 | 16 | 39 | 0.680 | 0.466 | 0.553 | 0.497 |
| iTrust | 26 | 64 | 58 | 15 | 43 | 49 | 0.259 | 0.234 | 0.246 | 0.239 |
| Avg. |  |  |  |  |  |  | 0.505 | 0.257 | 0.308 | 0.273 |
| w. Avg. |  |  |  |  |  |  | 0.541 | 0.181 | 0.235 | 0.198 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 486; cut at 4096 answer tokens: 0
- Per call: median 4.7 s (IQR 3.5-6.7 s, n = 1020)
- Per requirement: median 106.5 s (IQR 88.3-120.8 s, n = 51)
