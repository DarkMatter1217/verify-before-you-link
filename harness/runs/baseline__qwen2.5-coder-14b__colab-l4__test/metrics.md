# baseline with qwen2.5-coder:14b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 163 | 105 | 58 | 723 | 0.644 | 0.127 | 0.212 | 0.151 |
| eTour_en | 46 | 235 | 176 | 79 | 97 | 156 | 0.449 | 0.336 | 0.384 | 0.354 |
| iTrust | 105 | 222 | 381 | 45 | 336 | 177 | 0.118 | 0.203 | 0.149 | 0.177 |
| Avg. |  |  |  |  |  |  | 0.404 | 0.222 | 0.249 | 0.227 |
| w. Avg. |  |  |  |  |  |  | 0.518 | 0.178 | 0.233 | 0.193 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 239 | 164 | 75 | 664 | 0.686 | 0.198 | 0.307 | 0.231 |
| eTour_en | 46 | 235 | 243 | 124 | 119 | 111 | 0.510 | 0.528 | 0.519 | 0.524 |
| iTrust | 105 | 222 | 433 | 73 | 360 | 149 | 0.169 | 0.329 | 0.223 | 0.276 |
| Avg. |  |  |  |  |  |  | 0.455 | 0.352 | 0.350 | 0.344 |
| w. Avg. |  |  |  |  |  |  | 0.565 | 0.281 | 0.331 | 0.292 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 2684; cut at 4096 answer tokens: 0
- Per call: median 4.1 s (IQR 3.0-5.7 s, n = 4100)
- Per requirement: median 92.5 s (IQR 82.0-103.0 s, n = 205)
