# summary with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 287 | 114 | 173 | 230 | 0.397 | 0.331 | 0.361 | 0.343 |
| eTour_en | 20 | 101 | 290 | 63 | 227 | 38 | 0.217 | 0.624 | 0.322 | 0.454 |
| iTrust | 20 | 42 | 240 | 20 | 220 | 22 | 0.083 | 0.476 | 0.142 | 0.245 |
| Avg. |  |  |  |  |  |  | 0.233 | 0.477 | 0.275 | 0.347 |
| w. Avg. |  |  |  |  |  |  | 0.333 | 0.405 | 0.334 | 0.357 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 287 | 114 | 173 | 230 | 0.397 | 0.331 | 0.361 | 0.343 |
| eTour_en | 20 | 101 | 290 | 63 | 227 | 38 | 0.217 | 0.624 | 0.322 | 0.454 |
| iTrust | 20 | 42 | 240 | 20 | 220 | 22 | 0.083 | 0.476 | 0.142 | 0.245 |
| Avg. |  |  |  |  |  |  | 0.233 | 0.477 | 0.275 | 0.347 |
| w. Avg. |  |  |  |  |  |  | 0.333 | 0.405 | 0.334 | 0.357 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 273; cut at 4096 answer tokens: 13
- Per call: median 5.6 s (IQR 4.5-6.9 s, n = 1200)
- Per requirement: median 119.5 s (IQR 109.1-136.1 s, n = 60)
