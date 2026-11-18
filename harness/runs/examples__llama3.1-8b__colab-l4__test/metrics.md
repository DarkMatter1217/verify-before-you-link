# examples with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 83 | 47 | 36 | 457 | 0.566 | 0.093 | 0.160 | 0.112 |
| eTour_en | 30 | 156 | 56 | 29 | 27 | 127 | 0.518 | 0.186 | 0.274 | 0.213 |
| iTrust | 30 | 58 | 71 | 5 | 66 | 53 | 0.070 | 0.086 | 0.078 | 0.083 |
| Avg. |  |  |  |  |  |  | 0.385 | 0.122 | 0.170 | 0.136 |
| w. Avg. |  |  |  |  |  |  | 0.516 | 0.113 | 0.178 | 0.132 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 83 | 47 | 36 | 457 | 0.566 | 0.093 | 0.160 | 0.112 |
| eTour_en | 30 | 156 | 56 | 29 | 27 | 127 | 0.518 | 0.186 | 0.274 | 0.213 |
| iTrust | 30 | 58 | 71 | 5 | 66 | 53 | 0.070 | 0.086 | 0.078 | 0.083 |
| Avg. |  |  |  |  |  |  | 0.385 | 0.122 | 0.170 | 0.136 |
| w. Avg. |  |  |  |  |  |  | 0.516 | 0.113 | 0.178 | 0.132 |

- Pairs: 1800; answers from {'ollama': 580, 'harness-cache': 1220, 'lissa-rq1': 0}
- Without a <trace> tag: 0; cut at 4096 answer tokens: 0
- Per call: median 5.1 s (IQR 4.4-6.2 s, n = 1800)
- Per requirement: median 108.4 s (IQR 101.8-116.5 s, n = 90)
