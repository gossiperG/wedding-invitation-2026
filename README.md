# 黄少娴 & 赵超杰 · 电子婚宴请柬

新中式风格单页 H5 电子请帖。纯静态，无任何构建依赖。

## 目录结构

```
marria_card/
├── index.html            # 全部页面（样式 + 文案 + 交互都在这一个文件里）
├── assets/
│   ├── img/              # 压缩后的 WebP 照片（cover_001 封面，gal_01~08 相册）
│   └── audio/bgm.mp3     # 背景音乐（卡农 D 大调，150 秒淡入淡出）
├── tools/make_assets.py  # 从原图目录重新生成压缩照片的脚本
└── README.md
```

## 本地预览

```
cd D:\python_file\project_AI\marria_card
python -m http.server 8710
# 浏览器打开 http://localhost:8710
```

URL 加 `?flat=1`（如 `http://localhost:8710/index.html?flat=1`）可关闭全部动效，
适合屏幕截图 / 低性能环境预览。

## 常见修改（都在 index.html 里，直接搜索改即可）

| 想改什么 | 去哪改 |
|---|---|
| 婚期/时间/地址文案 | HTML 内对应 section（搜 `2026.11.14` 或 `12:00`） |
| 时光轴故事文案 | `id="story"` 区块的 4 个 `<div class="node">`（当前是占位文案，请换成两人专属版本） |
| 换照片 | 替换 `assets/img/` 下同名文件，或改 HTML 里的 `src` |
| 换背景音乐 | 覆盖 `assets/audio/bgm.mp3`（建议 60~180 秒、64~96kbps） |
| 导航坐标 | `#nav` 里两个链接中的 `113.522482,22.275370`（GCJ-02 坐标） |

## 部署上线（微信可直接转发）

任选免费静态托管：

1. **Cloudflare Pages**（推荐）：拖上传 `marria_card` 文件夹，或关联 GitHub 仓库
2. **GitHub Pages**：仓库 Settings → Pages → 主分支根目录

拿到 `https://xxx` 链接后，在微信里"发送给朋友"即可。微信分享卡片默认取页面
`<title>` 和第一张图（封面月洞窗照片），如需精确控制可在页面 `<head>` 补充：
`og:title`、`og:description`、`og:image`。

## 版权说明

- 背景音乐：Kevin MacLeod《Canon in D Major》(incompetech.com)，CC BY 3.0。
  页面页脚已署名，请保留该署名。
- 照片版权归新人/摄影工作室所有，请确认工作室允许用于婚礼宣传。

## 尚待用户确认的内容

- [ ] 时光轴文案（初遇/相知/求婚/成礼）换成真实故事
- [ ] 是否补充婚宴当天其他时间节点（迎宾签到 / 仪式 / 敬酒）
- [ ] 是否需要 RSVP 回执表单
- [ ] 分发渠道确认后补充微信分享卡片信息
