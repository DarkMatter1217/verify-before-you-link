# definition with qwen2.5-coder:14b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 79 | 62 | 17 | 766 | 0.785 | 0.075 | 0.137 | 0.091 |
| eTour_en | 46 | 235 | 91 | 43 | 48 | 192 | 0.473 | 0.183 | 0.264 | 0.209 |
| iTrust | 105 | 222 | 125 | 34 | 91 | 188 | 0.272 | 0.153 | 0.196 | 0.168 |
| Avg. |  |  |  |  |  |  | 0.510 | 0.137 | 0.199 | 0.156 |
| w. Avg. |  |  |  |  |  |  | 0.639 | 0.108 | 0.170 | 0.126 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 112 | 92 | 20 | 736 | 0.821 | 0.111 | 0.196 | 0.134 |
| eTour_en | 46 | 235 | 157 | 93 | 64 | 142 | 0.592 | 0.396 | 0.474 | 0.424 |
| iTrust | 105 | 222 | 175 | 68 | 107 | 154 | 0.389 | 0.306 | 0.343 | 0.320 |
| Avg. |  |  |  |  |  |  | 0.601 | 0.271 | 0.338 | 0.293 |
| w. Avg. |  |  |  |  |  |  | 0.705 | 0.197 | 0.272 | 0.219 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 3086; cut at 4096 answer tokens: 0
- Per call: median 4.4 s (IQR 3.4-5.6 s, n = 4100)
- Per requirement: median 95.3 s (IQR 84.1-107.4 s, n = 205)
