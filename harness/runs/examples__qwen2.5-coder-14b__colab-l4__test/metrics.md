# examples with qwen2.5-coder:14b on colab-l4, test slice (first 50 per project)

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 110 | 88 | 22 | 664 | 0.800 | 0.117 | 0.204 | 0.141 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 50 | 106 | 152 | 28 | 124 | 78 | 0.184 | 0.264 | 0.217 | 0.243 |
| Avg. |  |  |  |  |  |  | 0.548 | 0.259 | 0.305 | 0.271 |
| w. Avg. |  |  |  |  |  |  | 0.710 | 0.191 | 0.268 | 0.213 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 50 | 752 | 110 | 88 | 22 | 664 | 0.800 | 0.117 | 0.204 | 0.141 |
| eTour_en | 46 | 235 | 141 | 93 | 48 | 142 | 0.660 | 0.396 | 0.495 | 0.430 |
| iTrust | 50 | 106 | 152 | 28 | 124 | 78 | 0.184 | 0.264 | 0.217 | 0.243 |
| Avg. |  |  |  |  |  |  | 0.548 | 0.259 | 0.305 | 0.271 |
| w. Avg. |  |  |  |  |  |  | 0.710 | 0.191 | 0.268 | 0.213 |

- Pairs: 2920; answers from {'ollama': 500, 'harness-cache': 2420, 'lissa-rq1': 0}
- Without a <trace> tag: 1391; cut at 4096 answer tokens: 0
- Per call: median 4.7 s (IQR 3.6-6.5 s, n = 2920)
- Per requirement: median 102.1 s (IQR 91.1-119.0 s, n = 146)
