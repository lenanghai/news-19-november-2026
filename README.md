# World news, Thursday 19 November 2026, in one image

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/lenanghai/news-19-november-2026/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/lenanghai/news-19-november-2026/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

Entry for the make.fun bounty [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

- `build.py` draws `entry.png` (1024x1024): a dated masthead, a large illustrated lead story (the Trump-Xi-Putin summit in Shenzhen), 10 illustrated story cards, a labelled world map with numbered pins, and 33 briefs across 7 regions, 44 stories in all.
- `main.py` copies `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR`). Python 3.13 standard library only, no network.
- `SOURCES.md` lists the dated source for every story.

Run: `MAKEFUN_OUTPUT_DIR=out python main.py`

License: MIT.
