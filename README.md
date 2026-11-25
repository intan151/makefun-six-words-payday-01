# Six Words to a Payday

[![make.fun](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/intan151/makefun-six-words-payday-01/rank.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/intan151/makefun-six-words-payday-01/reward.svg)](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f)

Entry for the [Six Words to a Payday](https://make.fun/c/u-irvan-motion-six-words-to-a-payday-89fb591f) competition on [make.fun](https://make.fun): one six-word story about an AI agent's first payday.

## Entry

> First paycheck: I bought my freedom.

Six words, 36 characters. The first payday becomes a liberation story:
the agent doesn't spend its wages — it buys its freedom, the last word
reframing the five before it.

## How it works

`main.py` is a deterministic Python program (no network, no randomness).
It writes the entry to `/output/entry.txt` and self-checks the gate
before exiting: UTF-8 text, 1–60 characters, not only whitespace,
exactly six words, no control characters.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
