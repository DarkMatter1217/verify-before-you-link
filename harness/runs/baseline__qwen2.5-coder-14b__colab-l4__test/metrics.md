# baseline with qwen2.5-coder:14b on colab-l4, test slice (first 60 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 163 | 105 | 58 | 723 | 0.644 | 0.127 | 0.212 | 0.151 |
| eTour_en | 46 | 235 | 176 | 79 | 97 | 156 | 0.449 | 0.336 | 0.384 | 0.354 |
| iTrust | 60 | 125 | 209 | 21 | 188 | 104 | 0.100 | 0.168 | 0.126 | 0.148 |
| Avg. |  |  |  |  |  |  | 0.398 | 0.210 | 0.241 | 0.218 |
| w. Avg. |  |  |  |  |  |  | 0.548 | 0.173 | 0.237 | 0.191 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 239 | 164 | 75 | 664 | 0.686 | 0.198 | 0.307 | 0.231 |
| eTour_en | 46 | 235 | 243 | 124 | 119 | 111 | 0.510 | 0.528 | 0.519 | 0.524 |
| iTrust | 60 | 125 | 239 | 36 | 203 | 89 | 0.151 | 0.288 | 0.198 | 0.244 |
| Avg. |  |  |  |  |  |  | 0.449 | 0.338 | 0.341 | 0.333 |
| w. Avg. |  |  |  |  |  |  | 0.595 | 0.273 | 0.338 | 0.290 |

- Pairs: 3200; answers from {'ollama': 0, 'harness-cache': 3200, 'lissa-rq1': 0}
- Without a <trace> tag: 2178; cut at 4096 answer tokens: 0
- Per call: median 4.1 s (IQR 3.0-5.7 s, n = 3200)
- Per requirement: median 92.4 s (IQR 81.9-103.0 s, n = 160)
