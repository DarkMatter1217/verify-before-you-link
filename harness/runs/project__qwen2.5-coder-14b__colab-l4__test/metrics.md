# project with qwen2.5-coder:14b on colab-l4, test slice (first 50 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 117 | 84 | 33 | 668 | 0.718 | 0.112 | 0.193 | 0.134 |
| eTour_en | 46 | 235 | 134 | 53 | 81 | 182 | 0.396 | 0.226 | 0.287 | 0.247 |
| iTrust | 50 | 106 | 133 | 19 | 114 | 87 | 0.143 | 0.179 | 0.159 | 0.171 |
| Avg. |  |  |  |  |  |  | 0.419 | 0.172 | 0.213 | 0.184 |
| w. Avg. |  |  |  |  |  |  | 0.593 | 0.143 | 0.210 | 0.162 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 177 | 134 | 43 | 618 | 0.757 | 0.178 | 0.288 | 0.210 |
| eTour_en | 46 | 235 | 243 | 128 | 115 | 107 | 0.527 | 0.545 | 0.536 | 0.541 |
| iTrust | 50 | 106 | 175 | 32 | 143 | 74 | 0.183 | 0.302 | 0.228 | 0.267 |
| Avg. |  |  |  |  |  |  | 0.489 | 0.342 | 0.351 | 0.339 |
| w. Avg. |  |  |  |  |  |  | 0.652 | 0.269 | 0.336 | 0.287 |

- Pairs: 2920; answers from {'ollama': 500, 'harness-cache': 2420, 'lissa-rq1': 0}
- Without a <trace> tag: 2316; cut at 4096 answer tokens: 0
- Per call: median 4.1 s (IQR 3.1-5.6 s, n = 2920)
- Per requirement: median 90.5 s (IQR 81.4-102.8 s, n = 146)
