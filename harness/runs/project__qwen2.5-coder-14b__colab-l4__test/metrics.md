# project with qwen2.5-coder:14b on colab-l4, test slice (first 10 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 15 | 11 | 4 | 161 | 0.733 | 0.064 | 0.118 | 0.078 |
| eTour_en | 10 | 61 | 30 | 17 | 13 | 44 | 0.567 | 0.279 | 0.374 | 0.310 |
| iTrust | 10 | 21 | 26 | 3 | 23 | 18 | 0.115 | 0.143 | 0.128 | 0.136 |
| Avg. |  |  |  |  |  |  | 0.472 | 0.162 | 0.206 | 0.175 |
| w. Avg. |  |  |  |  |  |  | 0.642 | 0.122 | 0.180 | 0.139 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 30 | 25 | 5 | 147 | 0.833 | 0.145 | 0.248 | 0.174 |
| eTour_en | 10 | 61 | 62 | 40 | 22 | 21 | 0.645 | 0.656 | 0.650 | 0.654 |
| iTrust | 10 | 21 | 34 | 4 | 30 | 17 | 0.118 | 0.190 | 0.145 | 0.169 |
| Avg. |  |  |  |  |  |  | 0.532 | 0.331 | 0.348 | 0.332 |
| w. Avg. |  |  |  |  |  |  | 0.729 | 0.272 | 0.336 | 0.289 |

- Pairs: 600; answers from {'ollama': 0, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 491; cut at 4096 answer tokens: 0
- Per call: median 3.8 s (IQR 3.0-5.5 s, n = 600)
- Per requirement: median 85.8 s (IQR 75.4-100.6 s, n = 30)
