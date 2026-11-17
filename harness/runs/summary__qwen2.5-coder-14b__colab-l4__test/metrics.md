# summary with qwen2.5-coder:14b on colab-l4, test slice (first 60 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 149 | 87 | 62 | 741 | 0.584 | 0.105 | 0.178 | 0.126 |
| eTour_en | 46 | 235 | 177 | 68 | 109 | 167 | 0.384 | 0.289 | 0.330 | 0.304 |
| iTrust | 60 | 125 | 169 | 19 | 150 | 106 | 0.112 | 0.152 | 0.129 | 0.142 |
| Avg. |  |  |  |  |  |  | 0.360 | 0.182 | 0.212 | 0.191 |
| w. Avg. |  |  |  |  |  |  | 0.495 | 0.146 | 0.203 | 0.163 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 250 | 165 | 85 | 663 | 0.660 | 0.199 | 0.306 | 0.232 |
| eTour_en | 46 | 235 | 277 | 129 | 148 | 106 | 0.466 | 0.549 | 0.504 | 0.530 |
| iTrust | 60 | 125 | 230 | 39 | 191 | 86 | 0.170 | 0.312 | 0.220 | 0.267 |
| Avg. |  |  |  |  |  |  | 0.432 | 0.353 | 0.343 | 0.343 |
| w. Avg. |  |  |  |  |  |  | 0.570 | 0.280 | 0.336 | 0.294 |

- Pairs: 3200; answers from {'ollama': 36, 'harness-cache': 3164, 'lissa-rq1': 0}
- Without a <trace> tag: 2430; cut at 4096 answer tokens: 0
- Per call: median 4.3 s (IQR 3.1-6.1 s, n = 3200)
- Per requirement: median 100.5 s (IQR 85.7-110.3 s, n = 160)
