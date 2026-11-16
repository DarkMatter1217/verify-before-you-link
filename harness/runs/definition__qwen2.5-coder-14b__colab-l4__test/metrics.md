# definition with qwen2.5-coder:14b on colab-l4, test slice (first 10 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 15 | 12 | 3 | 160 | 0.800 | 0.070 | 0.128 | 0.085 |
| eTour_en | 10 | 61 | 21 | 12 | 9 | 49 | 0.571 | 0.197 | 0.293 | 0.226 |
| iTrust | 10 | 21 | 11 | 2 | 9 | 19 | 0.182 | 0.095 | 0.125 | 0.105 |
| Avg. |  |  |  |  |  |  | 0.518 | 0.121 | 0.182 | 0.139 |
| w. Avg. |  |  |  |  |  |  | 0.694 | 0.102 | 0.168 | 0.121 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 23 | 20 | 3 | 152 | 0.870 | 0.116 | 0.205 | 0.141 |
| eTour_en | 10 | 61 | 43 | 29 | 14 | 32 | 0.674 | 0.475 | 0.558 | 0.505 |
| iTrust | 10 | 21 | 18 | 4 | 14 | 17 | 0.222 | 0.190 | 0.205 | 0.196 |
| Avg. |  |  |  |  |  |  | 0.589 | 0.261 | 0.323 | 0.281 |
| w. Avg. |  |  |  |  |  |  | 0.769 | 0.209 | 0.290 | 0.233 |

- Pairs: 600; answers from {'ollama': 0, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 474; cut at 4096 answer tokens: 0
- Per call: median 4.2 s (IQR 3.4-5.5 s, n = 600)
- Per requirement: median 96.3 s (IQR 77.7-105.8 s, n = 30)
