# examples with llama3.1:8b on colab-l4, test slice (first 20 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 60 | 30 | 30 | 314 | 0.500 | 0.087 | 0.149 | 0.104 |
| eTour_en | 20 | 101 | 37 | 20 | 17 | 81 | 0.541 | 0.198 | 0.290 | 0.227 |
| iTrust | 20 | 42 | 45 | 4 | 41 | 38 | 0.089 | 0.095 | 0.092 | 0.094 |
| Avg. |  |  |  |  |  |  | 0.376 | 0.127 | 0.177 | 0.142 |
| w. Avg. |  |  |  |  |  |  | 0.473 | 0.111 | 0.173 | 0.129 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 20 | 344 | 60 | 30 | 30 | 314 | 0.500 | 0.087 | 0.149 | 0.104 |
| eTour_en | 20 | 101 | 37 | 20 | 17 | 81 | 0.541 | 0.198 | 0.290 | 0.227 |
| iTrust | 20 | 42 | 45 | 4 | 41 | 38 | 0.089 | 0.095 | 0.092 | 0.094 |
| Avg. |  |  |  |  |  |  | 0.376 | 0.127 | 0.177 | 0.142 |
| w. Avg. |  |  |  |  |  |  | 0.473 | 0.111 | 0.173 | 0.129 |

- Pairs: 1200; answers from {'ollama': 600, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 0; cut at 4096 answer tokens: 0
- Per call: median 5.0 s (IQR 4.4-6.2 s, n = 1200)
- Per requirement: median 107.0 s (IQR 99.1-114.8 s, n = 60)
