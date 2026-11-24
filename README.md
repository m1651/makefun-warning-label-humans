# Warning Label for Humans: One Line, Big Laugh

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/m1651/makefun-warning-label-humans/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/m1651/makefun-warning-label-humans/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

An entry for the make.fun bounty
[Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85):
write the funniest single-line safety warning label that should come
printed on every human being, in 160 characters or fewer.

## The label

> WARNING: This human skipped the instructions, voided the warranty, and is now confidently in charge of everything.

## How it works

`main.py` is a small Python 3.13 program using only the standard library.
It writes the label above, as a single line, to `entry.txt` inside the
output directory given by the `MAKEFUN_OUTPUT_DIR` environment variable
(defaulting to `/output`). The label is a fixed string baked into the
program, so every run produces byte-identical output with no network
access and no randomness.

## Why this line

The joke is built the way a real warning label is built: a flat,
official-sounding `WARNING:` prefix, a list of defects, and then the
punchline lands in the last few words. Skipping instructions and voiding
warranties are things everyone recognises in themselves and in other
people, and the turn — that this same person is now confidently in
charge of everything — is the part that stings because it is true.
One idea, one read, no filler.

## Running it

```sh
python3 main.py
```

With a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/warninglabel-out1 python3 main.py
```

## Verification

The program was run twice into two different output directories and the
two `entry.txt` files were compared byte-for-byte with `cmp`; they were
identical. The label is 114 characters long, inside the 1–160 character
gate, and contains no trailing newline.

## License

MIT — see [LICENSE](LICENSE).
