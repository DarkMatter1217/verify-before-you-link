# definition+summary with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 468 | 233 | 235 | 595 | 0.498 | 0.281 | 0.360 | 0.308 |
| eTour_en | 46 | 235 | 356 | 117 | 239 | 118 | 0.329 | 0.498 | 0.396 | 0.451 |
| iTrust | 105 | 222 | 616 | 75 | 541 | 147 | 0.122 | 0.338 | 0.179 | 0.249 |
| Avg. |  |  |  |  |  |  | 0.316 | 0.372 | 0.312 | 0.336 |
| w. Avg. |  |  |  |  |  |  | 0.402 | 0.331 | 0.335 | 0.324 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 468 | 233 | 235 | 595 | 0.498 | 0.281 | 0.360 | 0.308 |
| eTour_en | 46 | 235 | 356 | 117 | 239 | 118 | 0.329 | 0.498 | 0.396 | 0.451 |
| iTrust | 105 | 222 | 616 | 75 | 541 | 147 | 0.122 | 0.338 | 0.179 | 0.249 |
| Avg. |  |  |  |  |  |  | 0.316 | 0.372 | 0.312 | 0.336 |
| w. Avg. |  |  |  |  |  |  | 0.402 | 0.331 | 0.335 | 0.324 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 295; cut at 4096 answer tokens: 28
- Per call: median 4.9 s (IQR 3.8-6.4 s, n = 4100)
- Per requirement: median 107.5 s (IQR 94.5-121.4 s, n = 205)
