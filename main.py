"""make.fun entry: write the committed front page to the output directory.

entry.png is drawn by build.py; this program only copies its bytes, so every run
writes the same file.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
