# definition+summary with llama3.1:8b on colab-l4, test slice (first 10 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 89 | 44 | 45 | 128 | 0.494 | 0.256 | 0.337 | 0.283 |
| eTour_en | 10 | 61 | 90 | 34 | 56 | 27 | 0.378 | 0.557 | 0.450 | 0.509 |
| iTrust | 10 | 21 | 76 | 4 | 72 | 17 | 0.053 | 0.190 | 0.082 | 0.125 |
| Avg. |  |  |  |  |  |  | 0.308 | 0.335 | 0.290 | 0.306 |
| w. Avg. |  |  |  |  |  |  | 0.430 | 0.323 | 0.343 | 0.324 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 89 | 44 | 45 | 128 | 0.494 | 0.256 | 0.337 | 0.283 |
| eTour_en | 10 | 61 | 90 | 34 | 56 | 27 | 0.378 | 0.557 | 0.450 | 0.509 |
| iTrust | 10 | 21 | 76 | 4 | 72 | 17 | 0.053 | 0.190 | 0.082 | 0.125 |
| Avg. |  |  |  |  |  |  | 0.308 | 0.335 | 0.290 | 0.306 |
| w. Avg. |  |  |  |  |  |  | 0.430 | 0.323 | 0.343 | 0.324 |

- Pairs: 600; answers from {'ollama': 600, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 48; cut at 4096 answer tokens: 4
- Per call: median 5.1 s (IQR 3.9-6.7 s, n = 600)
- Per requirement: median 113.1 s (IQR 100.1-119.2 s, n = 30)
