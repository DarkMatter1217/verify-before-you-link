# definition+examples with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 25 | 16 | 9 | 200 | 0.640 | 0.074 | 0.133 | 0.090 |
| eTour_en | 12 | 73 | 45 | 29 | 16 | 44 | 0.644 | 0.397 | 0.492 | 0.430 |
| iTrust | 26 | 64 | 30 | 14 | 16 | 50 | 0.467 | 0.219 | 0.298 | 0.245 |
| Avg. |  |  |  |  |  |  | 0.584 | 0.230 | 0.307 | 0.255 |
| w. Avg. |  |  |  |  |  |  | 0.609 | 0.167 | 0.237 | 0.188 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 25 | 16 | 9 | 200 | 0.640 | 0.074 | 0.133 | 0.090 |
| eTour_en | 12 | 73 | 45 | 29 | 16 | 44 | 0.644 | 0.397 | 0.492 | 0.430 |
| iTrust | 26 | 64 | 30 | 14 | 16 | 50 | 0.467 | 0.219 | 0.298 | 0.245 |
| Avg. |  |  |  |  |  |  | 0.584 | 0.230 | 0.307 | 0.255 |
| w. Avg. |  |  |  |  |  |  | 0.609 | 0.167 | 0.237 | 0.188 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 441; cut at 4096 answer tokens: 0
- Per call: median 4.7 s (IQR 3.6-6.3 s, n = 1020)
- Per requirement: median 102.5 s (IQR 87.9-121.8 s, n = 51)
