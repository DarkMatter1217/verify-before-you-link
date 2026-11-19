# examples with llama3.1:8b on colab-l4, test slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 131 | 68 | 63 | 760 | 0.519 | 0.082 | 0.142 | 0.099 |
| eTour_en | 46 | 235 | 90 | 39 | 51 | 196 | 0.433 | 0.166 | 0.240 | 0.189 |
| iTrust | 105 | 222 | 210 | 20 | 190 | 202 | 0.095 | 0.090 | 0.093 | 0.091 |
| Avg. |  |  |  |  |  |  | 0.349 | 0.113 | 0.158 | 0.126 |
| w. Avg. |  |  |  |  |  |  | 0.430 | 0.099 | 0.151 | 0.114 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 131 | 68 | 63 | 760 | 0.519 | 0.082 | 0.142 | 0.099 |
| eTour_en | 46 | 235 | 90 | 39 | 51 | 196 | 0.433 | 0.166 | 0.240 | 0.189 |
| iTrust | 105 | 222 | 210 | 20 | 190 | 202 | 0.095 | 0.090 | 0.093 | 0.091 |
| Avg. |  |  |  |  |  |  | 0.349 | 0.113 | 0.158 | 0.126 |
| w. Avg. |  |  |  |  |  |  | 0.430 | 0.099 | 0.151 | 0.114 |

- Pairs: 4100; answers from {'ollama': 0, 'harness-cache': 4100, 'lissa-rq1': 0}
- Without a <trace> tag: 1; cut at 4096 answer tokens: 1
- Per call: median 5.1 s (IQR 4.4-6.3 s, n = 4100)
- Per requirement: median 109.0 s (IQR 100.5-116.8 s, n = 205)
