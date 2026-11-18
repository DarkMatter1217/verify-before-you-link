# examples with qwen2.5-coder:14b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 117 | 95 | 22 | 733 | 0.812 | 0.115 | 0.201 | 0.139 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 105 | 222 | 294 | 70 | 224 | 152 | 0.238 | 0.315 | 0.271 | 0.296 |
| Avg. |  |  |  |  |  |  | 0.570 | 0.275 | 0.322 | 0.288 |
| w. Avg. |  |  |  |  |  |  | 0.685 | 0.201 | 0.267 | 0.219 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 117 | 95 | 22 | 733 | 0.812 | 0.115 | 0.201 | 0.139 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 105 | 222 | 295 | 71 | 224 | 151 | 0.241 | 0.320 | 0.275 | 0.300 |
| Avg. |  |  |  |  |  |  | 0.571 | 0.277 | 0.323 | 0.290 |
| w. Avg. |  |  |  |  |  |  | 0.685 | 0.202 | 0.267 | 0.220 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 1869; cut at 4096 answer tokens: 0
- Per call: median 4.8 s (IQR 3.6-6.7 s, n = 4100)
- Per requirement: median 102.8 s (IQR 92.7-121.8 s, n = 205)
