# RQ1 on the laptop: time per question and per requirement

Source: LiSSA's logs in `LiSSA-RATLR-V2/lissa/results-local/rq1-laptop/logs/` (MacBook Pro, Apple M5 Pro, 24 GB; Ollama 0.40.14).
Median with the interquartile range in brackets. Left out: the first question after each start (model loading), the last question before a stop, and questions over LiSSA's 15-minute limit.

## By configuration (all three projects)

| Model | Prompt | Questions timed | Per question | Requirements timed | Per requirement |
|---|---|---|---|---|---|
| llama3.1-8b | KISS | 5,034 of 5,043 | 0.8 s (0.5–1.3 s) | 246 | 25.4 s (20.0–31.8 s) |
| llama3.1-8b | chain-of-thought | 5,029 of 5,048 | 4.6 s (3.4–6.0 s) | 242 | 103.1 s (92.6–120.8 s) |
| qwen2.5-coder-14b | KISS | 5,036 of 5,041 | 1.8 s (1.0–2.9 s) | 248 | 51.5 s (41.0–63.3 s) |
| qwen2.5-coder-14b | chain-of-thought | 5,030 of 5,047 | 4.7 s (3.5–6.8 s) | 242 | 113.9 s (99.1–130.6 s) |

## By project

| Model | Prompt | Project | Questions timed | Per question | Requirements timed | Per requirement |
|---|---|---|---|---|---|---|
| llama3.1-8b | KISS | SMOS | 1,337 of 1,342 | 0.9 s (0.7–1.1 s) | 64 | 25.0 s (20.1–32.3 s) |
| llama3.1-8b | KISS | eTour_en | 1,159 of 1,160 | 0.8 s (0.5–2.2 s) | 57 | 34.2 s (26.1–39.7 s) |
| llama3.1-8b | KISS | iTrust | 2,538 of 2,541 | 0.6 s (0.4–1.3 s) | 125 | 22.6 s (17.5–28.9 s) |
| llama3.1-8b | chain-of-thought | SMOS | 1,338 of 1,341 | 5.0 s (4.0–6.3 s) | 65 | 110.5 s (100.3–120.8 s) |
| llama3.1-8b | chain-of-thought | eTour_en | 1,158 of 1,161 | 4.5 s (3.4–6.4 s) | 56 | 107.0 s (96.1–125.2 s) |
| llama3.1-8b | chain-of-thought | iTrust | 2,533 of 2,546 | 4.3 s (3.0–5.7 s) | 121 | 98.1 s (85.7–123.8 s) |
| qwen2.5-coder-14b | KISS | SMOS | 1,339 of 1,340 | 1.8 s (1.4–2.3 s) | 66 | 51.0 s (38.9–58.6 s) |
| qwen2.5-coder-14b | KISS | eTour_en | 1,158 of 1,161 | 1.8 s (1.0–4.1 s) | 56 | 67.6 s (52.1–79.6 s) |
| qwen2.5-coder-14b | KISS | iTrust | 2,539 of 2,540 | 1.6 s (0.9–3.0 s) | 126 | 46.2 s (37.8–58.8 s) |
| qwen2.5-coder-14b | chain-of-thought | SMOS | 1,339 of 1,340 | 4.1 s (3.4–5.5 s) | 66 | 105.5 s (88.5–114.9 s) |
| qwen2.5-coder-14b | chain-of-thought | eTour_en | 1,156 of 1,163 | 5.6 s (3.9–7.9 s) | 54 | 130.8 s (117.5–149.4 s) |
| qwen2.5-coder-14b | chain-of-thought | iTrust | 2,535 of 2,544 | 4.9 s (3.5–6.9 s) | 122 | 111.2 s (95.6–129.7 s) |
