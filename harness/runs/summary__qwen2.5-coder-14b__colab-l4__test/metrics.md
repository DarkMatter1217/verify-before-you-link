# summary with qwen2.5-coder:14b on colab-l4, test slice (first 50 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 143 | 83 | 60 | 669 | 0.580 | 0.110 | 0.185 | 0.132 |
| eTour_en | 46 | 235 | 177 | 68 | 109 | 167 | 0.384 | 0.289 | 0.330 | 0.304 |
| iTrust | 50 | 106 | 149 | 17 | 132 | 89 | 0.114 | 0.160 | 0.133 | 0.148 |
| Avg. |  |  |  |  |  |  | 0.360 | 0.187 | 0.216 | 0.195 |
| w. Avg. |  |  |  |  |  |  | 0.493 | 0.154 | 0.212 | 0.170 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 239 | 156 | 83 | 596 | 0.653 | 0.207 | 0.315 | 0.240 |
| eTour_en | 46 | 235 | 277 | 129 | 148 | 106 | 0.466 | 0.549 | 0.504 | 0.530 |
| iTrust | 50 | 106 | 198 | 31 | 167 | 75 | 0.157 | 0.292 | 0.204 | 0.249 |
| Avg. |  |  |  |  |  |  | 0.425 | 0.350 | 0.341 | 0.340 |
| w. Avg. |  |  |  |  |  |  | 0.564 | 0.289 | 0.345 | 0.303 |

- Pairs: 2920; answers from {'ollama': 500, 'harness-cache': 2420, 'lissa-rq1': 0}
- Without a <trace> tag: 2186; cut at 4096 answer tokens: 0
- Per call: median 4.3 s (IQR 3.1-6.1 s, n = 2920)
- Per requirement: median 100.9 s (IQR 86.5-110.5 s, n = 146)
