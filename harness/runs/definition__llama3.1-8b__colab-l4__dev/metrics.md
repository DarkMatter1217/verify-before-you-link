# definition with llama3.1:8b on colab-l4, dev slice

## Strict parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 122 | 55 | 67 | 161 | 0.451 | 0.255 | 0.325 | 0.279 |
| eTour_en | 12 | 73 | 126 | 45 | 81 | 28 | 0.357 | 0.616 | 0.452 | 0.538 |
| iTrust | 26 | 64 | 139 | 16 | 123 | 48 | 0.115 | 0.250 | 0.158 | 0.203 |
| Avg. |  |  |  |  |  |  | 0.308 | 0.374 | 0.312 | 0.340 |
| w. Avg. |  |  |  |  |  |  | 0.371 | 0.329 | 0.321 | 0.319 |

## Tolerant parsing

| Project | Reqs | Gold | Pred. | TP | FP | FN | P | R | F1 | F2 |
|---|---|---|---|---|---|---|---|---|---|---|
| SMOS | 13 | 216 | 122 | 55 | 67 | 161 | 0.451 | 0.255 | 0.325 | 0.279 |
| eTour_en | 12 | 73 | 126 | 45 | 81 | 28 | 0.357 | 0.616 | 0.452 | 0.538 |
| iTrust | 26 | 64 | 139 | 16 | 123 | 48 | 0.115 | 0.250 | 0.158 | 0.203 |
| Avg. |  |  |  |  |  |  | 0.308 | 0.374 | 0.312 | 0.340 |
| w. Avg. |  |  |  |  |  |  | 0.371 | 0.329 | 0.321 | 0.319 |

- Pairs: 1020; answers from {'ollama': 1020, 'harness-cache': 0, 'lissa-rq1': 0}
- Without a <trace> tag: 61; cut at 4096 answer tokens: 5
- Per call: median 4.5 s (IQR 3.4-5.9 s, n = 1020)
- Per requirement: median 97.4 s (IQR 83.7-111.7 s, n = 51)
