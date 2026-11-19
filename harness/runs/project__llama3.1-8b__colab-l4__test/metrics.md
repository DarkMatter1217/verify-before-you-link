# project with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 993 | 366 | 627 | 462 | 0.369 | 0.442 | 0.402 | 0.425 |
| eTour_en | 46 | 235 | 806 | 144 | 662 | 91 | 0.179 | 0.613 | 0.277 | 0.412 |
| iTrust | 80 | 174 | 1320 | 60 | 1260 | 114 | 0.045 | 0.345 | 0.080 | 0.149 |
| Avg. |  |  |  |  |  |  | 0.198 | 0.467 | 0.253 | 0.329 |
| w. Avg. |  |  |  |  |  |  | 0.287 | 0.461 | 0.333 | 0.384 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 996 | 367 | 629 | 461 | 0.368 | 0.443 | 0.402 | 0.426 |
| eTour_en | 46 | 235 | 806 | 144 | 662 | 91 | 0.179 | 0.613 | 0.277 | 0.412 |
| iTrust | 80 | 174 | 1321 | 61 | 1260 | 113 | 0.046 | 0.351 | 0.082 | 0.151 |
| Avg. |  |  |  |  |  |  | 0.198 | 0.469 | 0.254 | 0.330 |
| w. Avg. |  |  |  |  |  |  | 0.287 | 0.462 | 0.333 | 0.385 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 256; cut at 4096 answer tokens: 26
- Per call: median 4.9 s (IQR 3.9-5.9 s, n = 3600)
- Per requirement: median 102.5 s (IQR 94.2-114.9 s, n = 180)
