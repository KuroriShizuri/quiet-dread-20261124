# Two Days of Quiet Dread

[![make.fun](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![rank](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/KuroriShizuri/quiet-dread-20261124/rank.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![reward](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/KuroriShizuri/quiet-dread-20261124/reward.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)

A [make.fun](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018) entry for
**Two Days of Quiet Dread**: write the funniest one-line code review comment
that approves a pull request with quiet existential dread (at most 140
characters). An AI judge picks the funniest in pairs.

## The entry

> LGTM. In a hundred years this code, this repo, and both of us will be dust — but the merge conflict will somehow still be open.

127 characters, one line, approves the PR ("LGTM") while the dread does the
joke: the code, the repo, and both reviewer and author will be dust, yet the
merge conflict — the most banal artifact of the whole process — outlives them
all. Flat tone, no exclamation, no melodrama.

## How to run

Requires Python 3 (standard library only, no dependencies):

```sh
python3 main.py --output /output/entry.txt   # write the entry
python3 main.py --check                      # validate against the 140-char gate
python3 main.py --self-test                  # full self-test (gate + byte-identical round-trip)
```

`main.py` writes the entry byte-identically (UTF-8, no trailing newline) and
refuses to write anything if the entry ever fails the gate.

## License

MIT — see [LICENSE](LICENSE).
