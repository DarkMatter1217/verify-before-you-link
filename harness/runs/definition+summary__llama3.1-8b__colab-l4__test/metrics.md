# definition+summary with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 181 | 97 | 84 | 247 | 0.536 | 0.282 | 0.370 | 0.311 |
| eTour_en | 20 | 101 | 160 | 54 | 106 | 47 | 0.338 | 0.535 | 0.414 | 0.479 |
| iTrust | 20 | 42 | 134 | 19 | 115 | 23 | 0.142 | 0.452 | 0.216 | 0.315 |
| Avg. |  |  |  |  |  |  | 0.338 | 0.423 | 0.333 | 0.368 |
| w. Avg. |  |  |  |  |  |  | 0.461 | 0.349 | 0.365 | 0.346 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 181 | 97 | 84 | 247 | 0.536 | 0.282 | 0.370 | 0.311 |
| eTour_en | 20 | 101 | 160 | 54 | 106 | 47 | 0.338 | 0.535 | 0.414 | 0.479 |
| iTrust | 20 | 42 | 134 | 19 | 115 | 23 | 0.142 | 0.452 | 0.216 | 0.315 |
| Avg. |  |  |  |  |  |  | 0.338 | 0.423 | 0.333 | 0.368 |
| w. Avg. |  |  |  |  |  |  | 0.461 | 0.349 | 0.365 | 0.346 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 88; cut at 4096 answer tokens: 9
- Per call: median 5.1 s (IQR 3.8-6.6 s, n = 1200)
- Per requirement: median 109.9 s (IQR 98.6-123.3 s, n = 60)
