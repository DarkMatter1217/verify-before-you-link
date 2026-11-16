# examples with qwen2.5-coder:14b on colab-l4, test slice (first 10 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 25 | 22 | 3 | 150 | 0.880 | 0.128 | 0.223 | 0.154 |
| eTour_en | 10 | 61 | 38 | 26 | 12 | 35 | 0.684 | 0.426 | 0.525 | 0.461 |
| iTrust | 10 | 21 | 31 | 5 | 26 | 16 | 0.161 | 0.238 | 0.192 | 0.217 |
| Avg. |  |  |  |  |  |  | 0.575 | 0.264 | 0.314 | 0.278 |
| w. Avg. |  |  |  |  |  |  | 0.774 | 0.209 | 0.293 | 0.233 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 10 | 172 | 25 | 22 | 3 | 150 | 0.880 | 0.128 | 0.223 | 0.154 |
| eTour_en | 10 | 61 | 38 | 26 | 12 | 35 | 0.684 | 0.426 | 0.525 | 0.461 |
| iTrust | 10 | 21 | 31 | 5 | 26 | 16 | 0.161 | 0.238 | 0.192 | 0.217 |
| Avg. |  |  |  |  |  |  | 0.575 | 0.264 | 0.314 | 0.278 |
| w. Avg. |  |  |  |  |  |  | 0.774 | 0.209 | 0.293 | 0.233 |

- Pairs: 600; answers from {'ollama': 0, 'harness-cache': 600, 'lissa-rq1': 0}
- Without a <trace> tag: 275; cut at 4096 answer tokens: 0
- Per call: median 4.7 s (IQR 3.6-6.5 s, n = 600)
- Per requirement: median 100.2 s (IQR 88.5-118.5 s, n = 30)
