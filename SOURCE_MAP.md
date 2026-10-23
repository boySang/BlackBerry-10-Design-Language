# 来源覆盖索引

整理作者：酒鬼成员
主来源为 [原 PDF](https://developer.blackberry.com/devzone/files/design/bb10/UI_Guidelines_BlackBerry_10.pdf)。物理页码从 1 开始，正文印刷页码与物理页相同。规则编号对应 DESIGN_LANGUAGE.md；分段为连续覆盖索引，部分原章节在页中开始或跨页延续。

| PDF 页 | 原章节或页内主题 | 规范入口 |
| --- | --- | --- |
| 1-2 | 封面与出版信息 | BASE-01 |
| 3-4 | 目录 | SOURCE_MAP |
| 5-8 | 10.3视觉更新 | BASE-01 EXP-07 VIS-01 |
| 9-18 | 关键原则 | EXP-01 EXP-02 EXP-03 EXP-04 EXP-05 EXP-06 |
| 19-20 | 测量设计单位 | GEO-01 GEO-02 |
| 21-22 | 线框原型技巧、工具与导航引言 | PROCESS-01 |
| 23-27 | 应用结构 | NAV-01 NAV-02 NAV-03 NAV-04 NAV-05 NAV-06 |
| 28-30 | 屏幕视图 | PAGE-01 |
| 31-36 | 屏幕结构 | PAGE-02 PAGE-03 PAGE-04 PAGE-05 PAGE-06 PAGE-07 |
| 37-48 | 不同屏幕尺寸 | ADAPT-01 ADAPT-02 |
| 49-50 | 竖屏与横屏方向 | ADAPT-03 |
| 51-56 | 手势 | INPUT-01 INPUT-04 TASK-13 |
| 57-58 | 键盘 | INPUT-02 INPUT-03 |
| 59-61 | 触控板、Classic导航键与通知引言 | INPUT-05 NOTIFY-01 |
| 62-67 | 通知与调用框架引言 | NOTIFY-01 NOTIFY-02 |
| 68 | 分享与调用框架 | NOTIFY-02 |
| 69-72 | 跨应用任务界面Card | TASK-05 |
| 73 | 语言与文案 | COPY-01 TASK-12 |
| 74-76 | 可访问性 | ACCESS-01 TYPE-03 STATE-01 |
| 77-81 | 菜单 | TASK-01 TASK-02 TASK-03 |
| 82-83 | 表单与应用菜单续章 | TASK-03 TASK-06 TASK-07 TASK-08 |
| 84-85 | 临时任务页Sheet | TASK-04 |
| 86-88 | 对话框与轻提示 | COMP-12 COMP-13 |
| 89-90 | 设置 | TASK-09 |
| 91-93 | 进度与活动指示 | COMP-11 STATE-01 |
| 94-95 | 保存 | TASK-10 |
| 96-98 | 删除与错误预防引言 | TASK-11 TASK-12 |
| 99-102 | 避免和处理错误 | TASK-08 TASK-12 |
| 103-109 | 组件 | COMP-01 COMP-02 COMP-03 COMP-04 COMP-05 COMP-06 COMP-07 COMP-08 COMP-09 COMP-10 COMP-11 |
| 110 | 触控热区 | GEO-02 |
| 111-113 | 高亮反馈 | MOTION-03 MOTION-04 |
| 114 | 空状态 | STATE-01 |
| 115-116 | 色彩 | COLOR-01 COLOR-02 |
| 117-119 | 应用图标 | ASSET-01 |
| 120-123 | 活动框架Active Frames | ASSET-02 |
| 124 | 启动页与活动框架续章 | ASSET-02 ASSET-03 |
| 125-128 | 提示音设计与应用内图标引言 | SOUND-01 ICON-01 |
| 129-146 | 应用内图标 | ICON-01 ICON-02 ICON-03 ICON-04 ICON-05 |
| 147 | 动画与过渡 | MOTION-01 |
| 148-149 | OLED显示设计与排版引言 | ADAPT-04 TYPE-01 |
| 150 | 字体与排版 | TYPE-01 TYPE-02 |
| 151-152 | 文字颜色与视觉资产尺寸表 | COLOR-01 ASSET-01 ASSET-02 ICON-02 |
| 153-156 | 原文法律声明 | SOURCES |

## 证据核对范围

已提取并通读 156 页可提取文本；已渲染全书并检查 13 张总览联系表；另对颜色、字体、资产尺寸、手势与关键组件图示进行较高分辨率核对。图片中的 p.116 色板、p.119 图标色板、p.150 字号表和 p.151 文字色已转录入 JSON。总览用于发现结构和图示，不代表其中每一行小字都能在缩略图上读清。

未自动从示意图中测量未标尺寸，也未把 OCR 推测当原始参数。PDF 文本提取对旋转文字有不完整警告，因此字体、颜色和关键图表使用实际页面图核对。原文歧义保留在 GAPS.md。

BB10 UI Kit 阅读范围为固定提交的 README、DESIGN、LICENSE、三个 token 文件、Theme、Scaffold、Tabs、ActionBar、Dialog 与 Icons；另检查完整文件树。此为源代码与文档对照，没有构建、运行其测试或实机验证。

机器可读覆盖表见 [source-map.json](source-map.json)。本地验证脚本检查 1-156 页连续、无遗漏或重叠，并检查参数页码范围。
