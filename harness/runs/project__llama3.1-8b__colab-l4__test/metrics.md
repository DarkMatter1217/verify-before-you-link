# project with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 993 | 366 | 627 | 462 | 0.369 | 0.442 | 0.402 | 0.425 |
| eTour_en | 46 | 235 | 806 | 144 | 662 | 91 | 0.179 | 0.613 | 0.277 | 0.412 |
| iTrust | 105 | 222 | 1716 | 82 | 1634 | 140 | 0.048 | 0.369 | 0.085 | 0.157 |
| Avg. |  |  |  |  |  |  | 0.198 | 0.475 | 0.254 | 0.332 |
| w. Avg. |  |  |  |  |  |  | 0.278 | 0.461 | 0.324 | 0.377 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 996 | 367 | 629 | 461 | 0.368 | 0.443 | 0.402 | 0.426 |
| eTour_en | 46 | 235 | 806 | 144 | 662 | 91 | 0.179 | 0.613 | 0.277 | 0.412 |
| iTrust | 105 | 222 | 1717 | 83 | 1634 | 139 | 0.048 | 0.374 | 0.086 | 0.159 |
| Avg. |  |  |  |  |  |  | 0.198 | 0.477 | 0.255 | 0.333 |
| w. Avg. |  |  |  |  |  |  | 0.278 | 0.462 | 0.325 | 0.377 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 316; cut at 4096 answer tokens: 29
- Per call: median 4.8 s (IQR 3.9-5.9 s, n = 4100)
- Per requirement: median 101.7 s (IQR 93.1-113.0 s, n = 205)
