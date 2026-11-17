# project with qwen2.5-coder:14b on colab-l4, test slice (first 60 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 121 | 88 | 33 | 740 | 0.727 | 0.106 | 0.185 | 0.128 |
| eTour_en | 46 | 235 | 134 | 53 | 81 | 182 | 0.396 | 0.226 | 0.287 | 0.247 |
| iTrust | 60 | 125 | 152 | 21 | 131 | 104 | 0.138 | 0.168 | 0.152 | 0.161 |
| Avg. |  |  |  |  |  |  | 0.420 | 0.167 | 0.208 | 0.179 |
| w. Avg. |  |  |  |  |  |  | 0.600 | 0.136 | 0.202 | 0.155 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 186 | 143 | 43 | 685 | 0.769 | 0.173 | 0.282 | 0.204 |
| eTour_en | 46 | 235 | 243 | 128 | 115 | 107 | 0.527 | 0.545 | 0.536 | 0.541 |
| iTrust | 60 | 125 | 203 | 39 | 164 | 86 | 0.192 | 0.312 | 0.238 | 0.277 |
| Avg. |  |  |  |  |  |  | 0.496 | 0.343 | 0.352 | 0.341 |
| w. Avg. |  |  |  |  |  |  | 0.660 | 0.261 | 0.328 | 0.279 |

- Pairs: 3200; answers from {'ollama': 260, 'harness-cache': 2940, 'lissa-rq1': 0}
- Without a <trace> tag: 2553; cut at 4096 answer tokens: 0
- Per call: median 4.0 s (IQR 3.0-5.6 s, n = 3200)
- Per requirement: median 90.5 s (IQR 80.4-102.6 s, n = 160)
