# summary with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 32 | 20 | 12 | 196 | 0.625 | 0.093 | 0.161 | 0.112 |
| eTour_en | 12 | 73 | 39 | 13 | 26 | 60 | 0.333 | 0.178 | 0.232 | 0.196 |
| iTrust | 26 | 64 | 65 | 7 | 58 | 57 | 0.108 | 0.109 | 0.109 | 0.109 |
| Avg. |  |  |  |  |  |  | 0.355 | 0.127 | 0.167 | 0.139 |
| w. Avg. |  |  |  |  |  |  | 0.471 | 0.113 | 0.166 | 0.129 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 53 | 33 | 20 | 183 | 0.623 | 0.153 | 0.245 | 0.180 |
| eTour_en | 12 | 73 | 81 | 41 | 40 | 32 | 0.506 | 0.562 | 0.532 | 0.550 |
| iTrust | 26 | 64 | 93 | 15 | 78 | 49 | 0.161 | 0.234 | 0.191 | 0.215 |
| Avg. |  |  |  |  |  |  | 0.430 | 0.316 | 0.323 | 0.315 |
| w. Avg. |  |  |  |  |  |  | 0.515 | 0.252 | 0.295 | 0.263 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 794; cut at 4096 answer tokens: 1
- Per call: median 4.2 s (IQR 3.1-5.9 s, n = 1020)
- Per requirement: median 93.7 s (IQR 81.3-113.4 s, n = 51)
