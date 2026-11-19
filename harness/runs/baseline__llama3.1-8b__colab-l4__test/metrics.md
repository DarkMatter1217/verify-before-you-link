# baseline with llama3.1:8b on colab-l4, test slice (first 90 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 90 | 191 | 1249 | 72 | 1177 | 119 | 0.058 | 0.377 | 0.100 | 0.179 |
| Avg. |  |  |  |  |  |  | 0.205 | 0.470 | 0.261 | 0.338 |
| w. Avg. |  |  |  |  |  |  | 0.286 | 0.450 | 0.328 | 0.377 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 951 | 348 | 603 | 480 | 0.366 | 0.420 | 0.391 | 0.408 |
| eTour_en | 46 | 235 | 751 | 144 | 607 | 91 | 0.192 | 0.613 | 0.292 | 0.426 |
| iTrust | 90 | 191 | 1249 | 72 | 1177 | 119 | 0.058 | 0.377 | 0.100 | 0.179 |
| Avg. |  |  |  |  |  |  | 0.205 | 0.470 | 0.261 | 0.338 |
| w. Avg. |  |  |  |  |  |  | 0.286 | 0.450 | 0.328 | 0.377 |

- Pairs: 3800; answers from {'ollama': 200, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 609; cut at 4096 answer tokens: 43
- Per call: median 4.5 s (IQR 3.5-5.7 s, n = 3800)
- Per requirement: median 99.6 s (IQR 87.8-118.5 s, n = 190)
