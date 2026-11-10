# -*- coding: utf-8 -*-
"""
生成"婚礼纪速发物料包"：
1) 照片上传包：把已压缩的 WebP 栈照转成 JPG（婚礼纪 App 上传兼容 JPEG 最好）
2) 二维码：自建 H5 完整版链接，供桌卡/喜糖盒印制
3) 文案与操作指引文件在 materials 目录单独写入
"""
import os
from PIL import Image

ROOT = r"D:\python_file\project_AI\marria_card"
IMG_SRC = os.path.join(ROOT, "assets", "img")
DST = os.path.join(ROOT, "materials", "婚礼纪物料", "照片上传包")
QR_PATH = os.path.join(ROOT, "materials", "婚礼纪物料", "二维码-完整版H5.png")
H5_URL = "https://gossiperg.github.io/wedding-invitation-2026/"

def convert_all() -> list:
    os.makedirs(DST, exist_ok=True)
    made = []
    for name in sorted(os.listdir(IMG_SRC)):
        if not name.endswith(".webp") or "_full" in name:
            continue
        im = Image.open(os.path.join(IMG_SRC, name)).convert("RGB")
        out = os.path.join(DST, name.replace(".webp", ".jpg"))
        im.save(out, "JPEG", quality=85, optimize=True)
        made.append((name.replace(".webp", ".jpg"), os.path.getsize(out) / 1e3))
    return made

def make_qr() -> None:
    import qrcode
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=14, border=2)
    qr.add_data(H5_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#8c2f24", back_color="#f7f2ea").convert("RGB")
    os.makedirs(os.path.dirname(QR_PATH), exist_ok=True)
    img.save(QR_PATH)

def main() -> None:
    rows = convert_all()
    print("== 照片上传包 ==")
    for name, kb in rows:
        print(f"{name}: {kb:.0f}KB")
    make_qr()
    print(f"== 二维码 ==\n{QR_PATH}\n指向: {H5_URL}")

if __name__ == "__main__":
    main()
