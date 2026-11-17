# definition with qwen2.5-coder:14b on colab-l4, test slice (first 60 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 79 | 62 | 17 | 766 | 0.785 | 0.075 | 0.137 | 0.091 |
| eTour_en | 46 | 235 | 91 | 43 | 48 | 192 | 0.473 | 0.183 | 0.264 | 0.209 |
| iTrust | 60 | 125 | 71 | 17 | 54 | 108 | 0.239 | 0.136 | 0.173 | 0.149 |
| Avg. |  |  |  |  |  |  | 0.499 | 0.131 | 0.191 | 0.150 |
| w. Avg. |  |  |  |  |  |  | 0.666 | 0.103 | 0.166 | 0.121 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 112 | 92 | 20 | 736 | 0.821 | 0.111 | 0.196 | 0.134 |
| eTour_en | 46 | 235 | 157 | 93 | 64 | 142 | 0.592 | 0.396 | 0.474 | 0.424 |
| iTrust | 60 | 125 | 98 | 33 | 65 | 92 | 0.337 | 0.264 | 0.296 | 0.276 |
| Avg. |  |  |  |  |  |  | 0.584 | 0.257 | 0.322 | 0.278 |
| w. Avg. |  |  |  |  |  |  | 0.725 | 0.184 | 0.261 | 0.207 |

- Pairs: 3200; answers from {'ollama': 0, 'harness-cache': 3200, 'lissa-rq1': 0}
- Without a <trace> tag: 2430; cut at 4096 answer tokens: 0
- Per call: median 4.4 s (IQR 3.4-5.7 s, n = 3200)
- Per requirement: median 95.7 s (IQR 83.4-108.7 s, n = 160)
