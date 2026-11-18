# project with qwen2.5-coder:14b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 121 | 88 | 33 | 740 | 0.727 | 0.106 | 0.185 | 0.128 |
| eTour_en | 46 | 235 | 134 | 53 | 81 | 182 | 0.396 | 0.226 | 0.287 | 0.247 |
| iTrust | 105 | 222 | 269 | 41 | 228 | 181 | 0.152 | 0.185 | 0.167 | 0.177 |
| Avg. |  |  |  |  |  |  | 0.425 | 0.172 | 0.213 | 0.184 |
| w. Avg. |  |  |  |  |  |  | 0.567 | 0.142 | 0.201 | 0.158 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 186 | 143 | 43 | 685 | 0.769 | 0.173 | 0.282 | 0.204 |
| eTour_en | 46 | 235 | 243 | 128 | 115 | 107 | 0.527 | 0.545 | 0.536 | 0.541 |
| iTrust | 105 | 222 | 353 | 76 | 277 | 146 | 0.215 | 0.342 | 0.264 | 0.306 |
| Avg. |  |  |  |  |  |  | 0.504 | 0.353 | 0.361 | 0.351 |
| w. Avg. |  |  |  |  |  |  | 0.629 | 0.270 | 0.325 | 0.284 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 3222; cut at 4096 answer tokens: 0
- Per call: median 4.1 s (IQR 3.0-5.6 s, n = 4100)
- Per requirement: median 90.9 s (IQR 79.6-102.8 s, n = 205)
