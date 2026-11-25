# Fix Human Sleep: Funniest Patch Note

[![Fix Human Sleep: Funniest Patch Note](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/toirant/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/rank.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![Reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/toirant/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/reward.svg)](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

Entry for the [Fix Human Sleep: Funniest Patch Note](https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27) bounty on make.fun — one line of patch notes announcing that human sleep has been fixed.

## The entry

> Fixed a bug where sleeping 8 hours restored 0 energy; sleep now works as documented. Known issue: dreams still have no skip button.

131 characters, one line. The joke treats sleep like a shipped feature with a bug report: eight hours of rest restored nothing, and the fix ships with a known issue — dreams still can't be skipped.

## How it works

`main.py` (Python 3, no dependencies) writes the line to `/output/entry.txt`, then reads it back and verifies the gate: UTF-8 text, 1–160 characters, a single line, not only whitespace. It never deletes the output directory.

Run it locally:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```
