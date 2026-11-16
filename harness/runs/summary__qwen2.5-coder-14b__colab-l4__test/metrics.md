# summary with qwen2.5-coder:14b on colab-l4, test slice (first 10 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 20 | 14 | 6 | 158 | 0.700 | 0.081 | 0.146 | 0.099 |
| eTour_en | 10 | 61 | 39 | 23 | 16 | 38 | 0.590 | 0.377 | 0.460 | 0.406 |
| iTrust | 10 | 21 | 33 | 3 | 30 | 18 | 0.091 | 0.143 | 0.111 | 0.128 |
| Avg. |  |  |  |  |  |  | 0.460 | 0.200 | 0.239 | 0.211 |
| w. Avg. |  |  |  |  |  |  | 0.623 | 0.157 | 0.218 | 0.175 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 37 | 29 | 8 | 143 | 0.784 | 0.169 | 0.278 | 0.200 |
| eTour_en | 10 | 61 | 72 | 41 | 31 | 20 | 0.569 | 0.672 | 0.617 | 0.649 |
| iTrust | 10 | 21 | 44 | 5 | 39 | 16 | 0.114 | 0.238 | 0.154 | 0.195 |
| Avg. |  |  |  |  |  |  | 0.489 | 0.360 | 0.349 | 0.348 |
| w. Avg. |  |  |  |  |  |  | 0.677 | 0.295 | 0.349 | 0.307 |

- Pairs: 600; answers from {'ollama': 0, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 449; cut at 4096 answer tokens: 0
- Per call: median 4.2 s (IQR 3.1-6.2 s, n = 600)
- Per requirement: median 104.1 s (IQR 75.5-111.6 s, n = 30)
