# summary with llama3.1:8b on colab-l4, test slice (first 30 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 417 | 169 | 248 | 335 | 0.405 | 0.335 | 0.367 | 0.347 |
| eTour_en | 30 | 156 | 418 | 93 | 325 | 63 | 0.222 | 0.596 | 0.324 | 0.446 |
| iTrust | 30 | 58 | 363 | 22 | 341 | 36 | 0.061 | 0.379 | 0.105 | 0.185 |
| Avg. |  |  |  |  |  |  | 0.229 | 0.437 | 0.265 | 0.326 |
| w. Avg. |  |  |  |  |  |  | 0.338 | 0.396 | 0.336 | 0.356 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 30 | 504 | 417 | 169 | 248 | 335 | 0.405 | 0.335 | 0.367 | 0.347 |
| eTour_en | 30 | 156 | 418 | 93 | 325 | 63 | 0.222 | 0.596 | 0.324 | 0.446 |
| iTrust | 30 | 58 | 363 | 22 | 341 | 36 | 0.061 | 0.379 | 0.105 | 0.185 |
| Avg. |  |  |  |  |  |  | 0.229 | 0.437 | 0.265 | 0.326 |
| w. Avg. |  |  |  |  |  |  | 0.338 | 0.396 | 0.336 | 0.356 |

- Pairs: 1800; answers from {'ollama': 426, 'harness-cache': 1374, 'lissa-rq1': 0}
- Without a <trace> tag: 429; cut at 4096 answer tokens: 16
- Per call: median 5.6 s (IQR 4.5-7.0 s, n = 1800)
- Per requirement: median 120.2 s (IQR 109.6-133.7 s, n = 90)
