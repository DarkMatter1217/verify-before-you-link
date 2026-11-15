# baseline with qwen2.5-coder:14b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 36 | 23 | 13 | 193 | 0.639 | 0.106 | 0.183 | 0.128 |
| eTour_en | 12 | 73 | 44 | 24 | 20 | 49 | 0.545 | 0.329 | 0.410 | 0.357 |
| iTrust | 26 | 64 | 79 | 8 | 71 | 56 | 0.101 | 0.125 | 0.112 | 0.119 |
| Avg. |  |  |  |  |  |  | 0.429 | 0.187 | 0.235 | 0.201 |
| w. Avg. |  |  |  |  |  |  | 0.522 | 0.156 | 0.217 | 0.174 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 54 | 34 | 20 | 182 | 0.630 | 0.157 | 0.252 | 0.185 |
| eTour_en | 12 | 73 | 72 | 42 | 30 | 31 | 0.583 | 0.575 | 0.579 | 0.577 |
| iTrust | 26 | 64 | 93 | 14 | 79 | 50 | 0.151 | 0.219 | 0.178 | 0.201 |
| Avg. |  |  |  |  |  |  | 0.455 | 0.317 | 0.337 | 0.321 |
| w. Avg. |  |  |  |  |  |  | 0.533 | 0.255 | 0.306 | 0.269 |

- Pairs: 1020; answers from {'ollama': 0, 'harness-cache': 0, 'lissa-rq1': 1020}
- Without a <trace> tag: 685; cut at 4096 answer tokens: 0
- Per call: not enough timed calls
- Per requirement: not enough timed calls
