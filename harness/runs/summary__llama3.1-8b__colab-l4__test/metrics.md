# summary with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 761 | 291 | 470 | 537 | 0.382 | 0.351 | 0.366 | 0.357 |
| eTour_en | 46 | 235 | 644 | 133 | 511 | 102 | 0.207 | 0.566 | 0.303 | 0.420 |
| iTrust | 80 | 174 | 961 | 56 | 905 | 118 | 0.058 | 0.322 | 0.099 | 0.169 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.413 | 0.256 | 0.315 |
| w. Avg. |  |  |  |  |  |  | 0.303 | 0.388 | 0.317 | 0.343 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 761 | 291 | 470 | 537 | 0.382 | 0.351 | 0.366 | 0.357 |
| eTour_en | 46 | 235 | 644 | 133 | 511 | 102 | 0.207 | 0.566 | 0.303 | 0.420 |
| iTrust | 80 | 174 | 961 | 56 | 905 | 118 | 0.058 | 0.322 | 0.099 | 0.169 |
| Avg. |  |  |  |  |  |  | 0.216 | 0.413 | 0.256 | 0.315 |
| w. Avg. |  |  |  |  |  |  | 0.303 | 0.388 | 0.317 | 0.343 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 887; cut at 4096 answer tokens: 26
- Per call: median 5.6 s (IQR 4.5-7.0 s, n = 3600)
- Per requirement: median 120.6 s (IQR 108.1-133.6 s, n = 180)
