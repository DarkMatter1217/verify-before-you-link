# examples with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 20 | 8 | 12 | 208 | 0.400 | 0.037 | 0.068 | 0.045 |
| eTour_en | 12 | 73 | 30 | 14 | 16 | 59 | 0.467 | 0.192 | 0.272 | 0.217 |
| iTrust | 26 | 64 | 43 | 7 | 36 | 57 | 0.163 | 0.109 | 0.131 | 0.117 |
| Avg. |  |  |  |  |  |  | 0.343 | 0.113 | 0.157 | 0.127 |
| w. Avg. |  |  |  |  |  |  | 0.371 | 0.082 | 0.121 | 0.094 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 20 | 8 | 12 | 208 | 0.400 | 0.037 | 0.068 | 0.045 |
| eTour_en | 12 | 73 | 30 | 14 | 16 | 59 | 0.467 | 0.192 | 0.272 | 0.217 |
| iTrust | 26 | 64 | 43 | 7 | 36 | 57 | 0.163 | 0.109 | 0.131 | 0.117 |
| Avg. |  |  |  |  |  |  | 0.343 | 0.113 | 0.157 | 0.127 |
| w. Avg. |  |  |  |  |  |  | 0.371 | 0.082 | 0.121 | 0.094 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 1; cut at 4096 answer tokens: 1
- Per call: median 5.0 s (IQR 4.3-6.3 s, n = 1020)
- Per requirement: median 107.7 s (IQR 100.6-116.5 s, n = 51)
