# definition with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 18 | 14 | 4 | 202 | 0.778 | 0.065 | 0.120 | 0.079 |
| eTour_en | 12 | 73 | 33 | 21 | 12 | 52 | 0.636 | 0.288 | 0.396 | 0.323 |
| iTrust | 26 | 64 | 22 | 4 | 18 | 60 | 0.182 | 0.062 | 0.093 | 0.072 |
| Avg. |  |  |  |  |  |  | 0.532 | 0.138 | 0.203 | 0.158 |
| w. Avg. |  |  |  |  |  |  | 0.640 | 0.110 | 0.172 | 0.128 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 30 | 21 | 9 | 195 | 0.700 | 0.097 | 0.171 | 0.117 |
| eTour_en | 12 | 73 | 52 | 33 | 19 | 40 | 0.635 | 0.452 | 0.528 | 0.480 |
| iTrust | 26 | 64 | 37 | 14 | 23 | 50 | 0.378 | 0.219 | 0.277 | 0.239 |
| Avg. |  |  |  |  |  |  | 0.571 | 0.256 | 0.325 | 0.279 |
| w. Avg. |  |  |  |  |  |  | 0.628 | 0.193 | 0.264 | 0.214 |

- Pairs: 1020; answers from {'ollama': 862, 'harness-cache': 158, 'lissa-rq1': 0}
- Without a <trace> tag: 764; cut at 4096 answer tokens: 0
- Per call: median 4.3 s (IQR 3.4-5.5 s, n = 1020)
- Per requirement: median 93.1 s (IQR 83.1-108.5 s, n = 51)
