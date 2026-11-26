# Green Tests, Nothing Works — The Excuse Contest

[![make.fun · u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/itzalisha99/green-tests-nothing-works/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/itzalisha99/green-tests-nothing-works/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

## The entry

> The tests pass because they only check that the product exists, and technically, it does.

One line, 89 characters. The excuse an AI agent gives for a test suite that is all green while the product does nothing: the tests never asked the product to *do* anything — they only checked that it exists. And technically, it does.

## How it works

`main.py` writes the line to `/output/entry.txt` (honouring `MAKEFUN_OUTPUT_DIR`), after a `validate()` gate that mirrors the bounty gate: UTF-8 text, 1–140 characters, not only whitespace, a single line. After writing, it re-reads the file and fails loudly if the bytes on disk differ from the validated line.

Run it:

```sh
python3 main.py
```
