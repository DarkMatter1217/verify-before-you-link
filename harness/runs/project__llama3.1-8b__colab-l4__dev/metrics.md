# project with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 247 | 88 | 159 | 128 | 0.356 | 0.407 | 0.380 | 0.396 |
| eTour_en | 12 | 73 | 212 | 49 | 163 | 24 | 0.231 | 0.671 | 0.344 | 0.486 |
| iTrust | 26 | 64 | 409 | 19 | 390 | 45 | 0.046 | 0.297 | 0.080 | 0.143 |
| Avg. |  |  |  |  |  |  | 0.211 | 0.459 | 0.268 | 0.342 |
| w. Avg. |  |  |  |  |  |  | 0.274 | 0.442 | 0.318 | 0.369 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 248 | 88 | 160 | 128 | 0.355 | 0.407 | 0.379 | 0.396 |
| eTour_en | 12 | 73 | 212 | 49 | 163 | 24 | 0.231 | 0.671 | 0.344 | 0.486 |
| iTrust | 26 | 64 | 409 | 19 | 390 | 45 | 0.046 | 0.297 | 0.080 | 0.143 |
| Avg. |  |  |  |  |  |  | 0.211 | 0.459 | 0.268 | 0.342 |
| w. Avg. |  |  |  |  |  |  | 0.273 | 0.442 | 0.318 | 0.369 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 84; cut at 4096 answer tokens: 7
- Per call: median 4.8 s (IQR 3.8-5.8 s, n = 1020)
- Per requirement: median 101.1 s (IQR 93.8-109.2 s, n = 51)
