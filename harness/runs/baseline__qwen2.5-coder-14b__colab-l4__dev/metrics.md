# baseline with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 29 | 20 | 9 | 196 | 0.690 | 0.093 | 0.163 | 0.112 |
| eTour_en | 12 | 73 | 40 | 22 | 18 | 51 | 0.550 | 0.301 | 0.389 | 0.331 |
| iTrust | 26 | 64 | 78 | 5 | 73 | 59 | 0.064 | 0.078 | 0.070 | 0.075 |
| Avg. |  |  |  |  |  |  | 0.435 | 0.157 | 0.208 | 0.173 |
| w. Avg. |  |  |  |  |  |  | 0.547 | 0.133 | 0.193 | 0.151 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 52 | 32 | 20 | 184 | 0.615 | 0.148 | 0.239 | 0.175 |
| eTour_en | 12 | 73 | 69 | 41 | 28 | 32 | 0.594 | 0.562 | 0.577 | 0.568 |
| iTrust | 26 | 64 | 93 | 14 | 79 | 50 | 0.151 | 0.219 | 0.178 | 0.201 |
| Avg. |  |  |  |  |  |  | 0.453 | 0.310 | 0.332 | 0.314 |
| w. Avg. |  |  |  |  |  |  | 0.527 | 0.246 | 0.298 | 0.261 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 718; cut at 4096 answer tokens: 0
- Per call: median 4.0 s (IQR 3.0-5.6 s, n = 1020)
- Per requirement: median 92.0 s (IQR 76.9-105.4 s, n = 51)
