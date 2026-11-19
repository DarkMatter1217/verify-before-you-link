# examples with llama3.1:8b on colab-l4, test slice (first 80 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 131 | 68 | 63 | 760 | 0.519 | 0.082 | 0.142 | 0.099 |
| eTour_en | 46 | 235 | 90 | 39 | 51 | 196 | 0.433 | 0.166 | 0.240 | 0.189 |
| iTrust | 80 | 174 | 154 | 12 | 142 | 162 | 0.078 | 0.069 | 0.073 | 0.071 |
| Avg. |  |  |  |  |  |  | 0.343 | 0.106 | 0.152 | 0.120 |
| w. Avg. |  |  |  |  |  |  | 0.441 | 0.096 | 0.151 | 0.112 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 131 | 68 | 63 | 760 | 0.519 | 0.082 | 0.142 | 0.099 |
| eTour_en | 46 | 235 | 90 | 39 | 51 | 196 | 0.433 | 0.166 | 0.240 | 0.189 |
| iTrust | 80 | 174 | 154 | 12 | 142 | 162 | 0.078 | 0.069 | 0.073 | 0.071 |
| Avg. |  |  |  |  |  |  | 0.343 | 0.106 | 0.152 | 0.120 |
| w. Avg. |  |  |  |  |  |  | 0.441 | 0.096 | 0.151 | 0.112 |

- Pairs: 3600; answers from {'ollama': 0, 'harness-cache': 3600, 'lissa-rq1': 0}
- Without a <trace> tag: 0; cut at 4096 answer tokens: 0
- Per call: median 5.1 s (IQR 4.4-6.3 s, n = 3600)
- Per requirement: median 108.9 s (IQR 100.6-116.5 s, n = 180)
