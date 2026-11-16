# project with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 23 | 16 | 7 | 200 | 0.696 | 0.074 | 0.134 | 0.090 |
| eTour_en | 12 | 73 | 32 | 15 | 17 | 58 | 0.469 | 0.205 | 0.286 | 0.231 |
| iTrust | 26 | 64 | 57 | 3 | 54 | 61 | 0.053 | 0.047 | 0.050 | 0.048 |
| Avg. |  |  |  |  |  |  | 0.406 | 0.109 | 0.156 | 0.123 |
| w. Avg. |  |  |  |  |  |  | 0.532 | 0.096 | 0.150 | 0.112 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 41 | 26 | 15 | 190 | 0.634 | 0.120 | 0.202 | 0.144 |
| eTour_en | 12 | 73 | 75 | 44 | 31 | 29 | 0.587 | 0.603 | 0.595 | 0.599 |
| iTrust | 26 | 64 | 78 | 14 | 64 | 50 | 0.179 | 0.219 | 0.197 | 0.210 |
| Avg. |  |  |  |  |  |  | 0.467 | 0.314 | 0.331 | 0.318 |
| w. Avg. |  |  |  |  |  |  | 0.542 | 0.238 | 0.283 | 0.250 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 808; cut at 4096 answer tokens: 0
- Per call: median 4.1 s (IQR 3.0-5.6 s, n = 1020)
- Per requirement: median 91.2 s (IQR 74.6-106.7 s, n = 51)
