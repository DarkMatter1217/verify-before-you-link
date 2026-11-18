# definition with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 204 | 105 | 99 | 239 | 0.515 | 0.305 | 0.383 | 0.332 |
| eTour_en | 20 | 101 | 202 | 62 | 140 | 39 | 0.307 | 0.614 | 0.409 | 0.512 |
| iTrust | 20 | 42 | 112 | 19 | 93 | 23 | 0.170 | 0.452 | 0.247 | 0.339 |
| Avg. |  |  |  |  |  |  | 0.330 | 0.457 | 0.346 | 0.394 |
| w. Avg. |  |  |  |  |  |  | 0.442 | 0.382 | 0.377 | 0.370 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 204 | 105 | 99 | 239 | 0.515 | 0.305 | 0.383 | 0.332 |
| eTour_en | 20 | 101 | 202 | 62 | 140 | 39 | 0.307 | 0.614 | 0.409 | 0.512 |
| iTrust | 20 | 42 | 112 | 19 | 93 | 23 | 0.170 | 0.452 | 0.247 | 0.339 |
| Avg. |  |  |  |  |  |  | 0.330 | 0.457 | 0.346 | 0.394 |
| w. Avg. |  |  |  |  |  |  | 0.442 | 0.382 | 0.377 | 0.370 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 70; cut at 4096 answer tokens: 11
- Per call: median 4.5 s (IQR 3.4-5.9 s, n = 1200)
- Per requirement: median 100.4 s (IQR 89.6-115.3 s, n = 60)
