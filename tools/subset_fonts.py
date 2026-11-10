# -*- coding: utf-8 -*-
"""
从 index.html 提取实际使用的字符集，并用 fonttools 子集化思源宋体：
  noto400.woff2 (全量 1.4MB) -> assets/fonts/noto-400.woff2 (~20KB)
  noto600.woff2 (全量 1.5MB) -> assets/fonts/noto-600.woff2 (~20KB)
"""
import html
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "index.html")
CHARS = os.path.join(ROOT, "tools", "used_chars.txt")
SRC_DIR = os.path.join(ROOT, "tools")
DST_DIR = os.path.join(ROOT, "assets", "fonts")

def build_charset() -> int:
    src = open(HTML, encoding="utf-8").read()
    text = re.sub(r"<script[\s\S]*?</script>", "", re.sub(r"<style[\s\S]*?</style>", "", src))
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    charset = set(text)
    charset |= set(
        "0123456789 "
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        "·—…“”！？：；、（）(),.:;!?【】《》囍♡❤"
    )
    data = "".join(sorted(charset))
    with open(CHARS, "w", encoding="utf-8") as f:
        f.write(data)
    return len(charset)

def main() -> None:
    n = build_charset()
    print(f"页面字符集: {n} 个字符")
    os.makedirs(DST_DIR, exist_ok=True)
    from fontTools import subset

    for weight in (400, 600):
        src = os.path.join(SRC_DIR, f"noto{weight}.woff2")
        dst = os.path.join(DST_DIR, f"noto-{weight}.woff2")
        opt = subset.Options()
        opt.flavor = "woff2"
        opt.layout_features = ["*"]
        opt.hinting = True
        opt.desubroutinize = True
        fnt = subset.load_font(src, opt)
        subsetter = subset.Subsetter(opt)
        subsetter.populate(text=open(CHARS, encoding="utf-8").read())
        subsetter.subset(fnt)
        subset.save_font(fnt, dst, opt)
        kb = os.path.getsize(dst) / 1e3
        print(f"noto-{weight}.woff2: {kb:.0f}KB")

if __name__ == "__main__":
    main()
