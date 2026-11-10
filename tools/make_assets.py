# -*- coding: utf-8 -*-
"""
从原始婚纱照目录中挑选照片并压缩为 H5 请求帖所需尺寸。
封面图 1080 宽，相册图 900 宽；输出 WebP（微信浏览器兼容）。
"""
import os
from PIL import Image

SRC = r"H:\huangym_disk\老三照片\极速下载好的文件\敏\小敏 完\黄少娴-放大摆台"
DST = r"D:\python_file\project_AI\marria_card\assets\img"

# 文件名 -> 输出名（cover 为封面, 序号决定相册顺序）
PLAN = {
    "IMG_7819.jpg": "cover_001.webp",   # 我们结婚啦卷轴 —— 封面
    "IMG_7925.jpg": "gal_01.webp",      # 秀禾服红金
    "IMG_7390.jpg": "gal_02.webp",      # 海边笑容
    "IMG_7694.jpg": "gal_03.webp",      # 金色浪漫
    "IMG_7666.jpg": "gal_04.webp",      # 光影对望
    "IMG_7792.jpg": "gal_05.webp",      # 红黑灯笼互动
    "IMG_7810.jpg": "gal_06.webp",      # 喜字灯笼
    "IMG_7574.jpg": "gal_07.webp",      # 绿植拱门
    "IMG_7515.jpg": "gal_08.webp",      # 草坪大裙摆（横幅）
}

MAX_COVER_W = 1080
MAX_GAL_W = 900
QUALITY = 80

def convert(src_path: str, dst_path: str, max_w: int) -> None:
    im = Image.open(src_path)
    im = im.convert("RGB")
    if im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(dst_path, "WEBP", quality=QUALITY, method=6)

def main() -> None:
    os.makedirs(DST, exist_ok=True)
    total_in = total_out = 0
    for src_name, dst_name in PLAN.items():
        src_path = os.path.join(SRC, src_name)
        dst_path = os.path.join(DST, dst_name)
        before = os.path.getsize(src_path) / 1e6
        convert(src_path, dst_path, MAX_COVER_W if "cover" in dst_name else MAX_GAL_W)
        after = os.path.getsize(dst_path) / 1e6
        total_in += before
        total_out += after
        print(f"{src_name} -> {dst_name}: {before:.1f}MB -> {after * 1000:.0f}KB")
    print(f"----\n合计: {total_in:.0f}MB -> {total_out:.1f}MB")

if __name__ == "__main__":
    main()
