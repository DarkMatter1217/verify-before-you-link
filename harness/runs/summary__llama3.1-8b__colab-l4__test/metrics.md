# summary with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 761 | 291 | 470 | 537 | 0.382 | 0.351 | 0.366 | 0.357 |
| eTour_en | 46 | 235 | 644 | 133 | 511 | 102 | 0.207 | 0.566 | 0.303 | 0.420 |
| iTrust | 105 | 222 | 1265 | 76 | 1189 | 146 | 0.060 | 0.342 | 0.102 | 0.176 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.420 | 0.257 | 0.318 |
| w. Avg. |  |  |  |  |  |  | 0.295 | 0.389 | 0.309 | 0.337 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 761 | 291 | 470 | 537 | 0.382 | 0.351 | 0.366 | 0.357 |
| eTour_en | 46 | 235 | 644 | 133 | 511 | 102 | 0.207 | 0.566 | 0.303 | 0.420 |
| iTrust | 105 | 222 | 1265 | 76 | 1189 | 146 | 0.060 | 0.342 | 0.102 | 0.176 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.420 | 0.257 | 0.318 |
| w. Avg. |  |  |  |  |  |  | 0.295 | 0.389 | 0.309 | 0.337 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 1037; cut at 4096 answer tokens: 33
- Per call: median 5.5 s (IQR 4.4-6.9 s, n = 4100)
- Per requirement: median 119.8 s (IQR 103.3-133.6 s, n = 205)
