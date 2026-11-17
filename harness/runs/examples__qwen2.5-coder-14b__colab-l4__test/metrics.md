# examples with qwen2.5-coder:14b on colab-l4, test slice (first 60 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 117 | 95 | 22 | 733 | 0.812 | 0.115 | 0.201 | 0.139 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 60 | 125 | 174 | 35 | 139 | 90 | 0.201 | 0.280 | 0.234 | 0.260 |
| Avg. |  |  |  |  |  |  | 0.558 | 0.263 | 0.310 | 0.276 |
| w. Avg. |  |  |  |  |  |  | 0.718 | 0.188 | 0.263 | 0.209 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 54 | 828 | 117 | 95 | 22 | 733 | 0.812 | 0.115 | 0.201 | 0.139 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 60 | 125 | 174 | 35 | 139 | 90 | 0.201 | 0.280 | 0.234 | 0.260 |
| Avg. |  |  |  |  |  |  | 0.558 | 0.263 | 0.310 | 0.276 |
| w. Avg. |  |  |  |  |  |  | 0.718 | 0.188 | 0.263 | 0.209 |

- Pairs: 3200; answers from {'ollama': 260, 'harness-cache': 2940, 'lissa-rq1': 0}
- Without a <trace> tag: 1555; cut at 4096 answer tokens: 0
- Per call: median 4.7 s (IQR 3.6-6.5 s, n = 3200)
- Per requirement: median 102.3 s (IQR 90.4-119.1 s, n = 160)
