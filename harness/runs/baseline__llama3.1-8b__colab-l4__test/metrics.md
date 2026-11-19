# baseline with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 105 | 222 | 1460 | 82 | 1378 | 140 | 0.056 | 0.369 | 0.098 | 0.175 |
| Avg. |  |  |  |  |  |  | 0.205 | 0.467 | 0.260 | 0.336 |
| w. Avg. |  |  |  |  |  |  | 0.281 | 0.447 | 0.322 | 0.371 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 105 | 222 | 1460 | 82 | 1378 | 140 | 0.056 | 0.369 | 0.098 | 0.175 |
| Avg. |  |  |  |  |  |  | 0.205 | 0.467 | 0.260 | 0.336 |
| w. Avg. |  |  |  |  |  |  | 0.281 | 0.447 | 0.322 | 0.371 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 682; cut at 4096 answer tokens: 47
- Per call: median 4.5 s (IQR 3.5-5.7 s, n = 4100)
- Per requirement: median 99.1 s (IQR 86.8-118.5 s, n = 205)
