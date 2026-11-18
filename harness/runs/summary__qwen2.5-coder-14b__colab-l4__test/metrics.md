# summary with qwen2.5-coder:14b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 149 | 87 | 62 | 741 | 0.584 | 0.105 | 0.178 | 0.126 |
| eTour_en | 46 | 235 | 177 | 68 | 109 | 167 | 0.384 | 0.289 | 0.330 | 0.304 |
| iTrust | 105 | 222 | 321 | 41 | 280 | 181 | 0.128 | 0.185 | 0.151 | 0.170 |
| Avg. |  |  |  |  |  |  | 0.365 | 0.193 | 0.220 | 0.200 |
| w. Avg. |  |  |  |  |  |  | 0.469 | 0.153 | 0.201 | 0.166 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 250 | 165 | 85 | 663 | 0.660 | 0.199 | 0.306 | 0.232 |
| eTour_en | 46 | 235 | 277 | 129 | 148 | 106 | 0.466 | 0.549 | 0.504 | 0.530 |
| iTrust | 105 | 222 | 427 | 78 | 349 | 144 | 0.183 | 0.351 | 0.240 | 0.297 |
| Avg. |  |  |  |  |  |  | 0.436 | 0.367 | 0.350 | 0.353 |
| w. Avg. |  |  |  |  |  |  | 0.542 | 0.289 | 0.331 | 0.297 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 3099; cut at 4096 answer tokens: 0
- Per call: median 4.4 s (IQR 3.1-6.1 s, n = 4100)
- Per requirement: median 99.5 s (IQR 85.8-110.8 s, n = 205)
