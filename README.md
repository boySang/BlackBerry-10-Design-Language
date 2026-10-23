# BlackBerry 10 设计语言

**整理作者：酒鬼成员 · 规范版本：1.1.2 · 中文整理版**

把黑莓的体验原则转成可以在真实项目里使用的设计约束：内容优先、底部高频操作、连续的页面层级、可取消的手势，以及统一的组件和状态。适用于原生 BB10 项目，也可作为 Android、网页及其他平台的适配参考。

本仓库以 **BlackBerry 10.3 的视觉演进**为主要基线，保留历史变体及其适用边界。它是一套规范与参数资料，不是已经实现的界面组件库，也不代表黑莓官方发布。

## 先看什么

| 文件 | 用途 |
| --- | --- |
| [设计语言正文](DESIGN_LANGUAGE.md) | 体验原则、信息结构、导航、视觉、交互、状态、设备与资产，共87条规则 |
| [关键控件标准](COMPONENT_STANDARDS.md) | 底栏、主圆、两端按钮、顶部取消/保存、下拉选择及其完整状态 |
| [动画与过渡](MOTION.md) | 进入、退出、取消、同步位移、手势跟随与焦点恢复 |
| [项目接入指南](ADOPTION.md) | 设计师、开发者及其他AI的阅读顺序、配置填写、参数落地、完整提示词与验收步骤 |
| [设计信息缺口](GAPS.md) | 原文没有给出的参数、历史资料歧义及标定方法 |
| [设计验收清单](ACCEPTANCE.md) | 页面、输入、状态、字体、热区和动画的验收要求 |
| [来源与署名](SOURCES.md) | 黑莓官方PDF、参考仓库、固定提交、出处与权利边界 |
| [章节索引](SOURCE_MAP.md) / [原图页码索引](VISUAL_REFERENCE.md) | 回到官方PDF检查完整上下文 |
| [与参考实现的对照](KIT_COMPARISON.md) | 第三方实现可借鉴的部分及与PDF的差异 |
| [核对记录](VERIFICATION.md) / [更新记录](CHANGELOG.md) | 当前版本的核对范围与变化 |

## 立即用于其他项目

1. 在项目入口记录本仓库链接及固定提交号；需要存放文件副本时，先确认 [文件复用的授权边界](SOURCES.md)，再放到 `docs/design/blackberry-10/`。
2. 阅读正文、关键控件和动画标准；参照 [配置模板](PROJECT_PROFILE.template.json) 建立项目自己的 `PROJECT_PROFILE.json`，填写平台、屏幕、单位映射、字体和标题栏变体。
3. 将规范入口写进项目文档或 `AGENTS.md`，按验收清单交付真实截图与可操作结果。

可直接交给其他AI或协作者：

```text
本项目参考 https://github.com/boySang/BlackBerry-10-Design-Language 的设计语言1.1.2，
固定本次采用的完整提交号；如已有授权保存的本地副本，读取 docs/design/blackberry-10/。
先读 README.md、DESIGN_LANGUAGE.md、COMPONENT_STANDARDS.md、MOTION.md、GAPS.md，
以及本项目的 PROJECT_PROFILE.json。
以黑莓官方PDF为主来源，第三方UI Kit只作实现参考；保留证据等级和项目适配记录。
统一实现主题、尺寸、字体、组件、状态和过渡；不要只换颜色与图标。
不把源设备px、du、Android dp/sp和网页CSS px直接等同。
按 ACCEPTANCE.md 验证，缺失参数和偏离项写入 DESIGN_EXCEPTIONS.md。
```

更完整的目录、配置字段说明、参数换算示例和可复制AI指令见 [项目接入指南](ADOPTION.md)。只提供仓库名称不会自动应用规范，需确保协作者实际读取这些文件及当前项目配置。

## 参数怎样使用

| 文件 | 内容 | 采用方式 |
| --- | --- | --- |
| [tokens.source.json](tokens.source.json) | 125项PDF来源参数，保留单位、页码与证据类别 | 按目标设备与平台转换，不直接当通用CSS/dp/sp |
| [tokens.visual-profile.json](tokens.visual-profile.json) | 10项原图归一化量测，以及明确分离的复刻配置 | 原图比例和项目皮肤分别处理，不伪称官方硬数值 |
| [tokens.kit-reference.json](tokens.kit-reference.json) | 71项第三方候选参数 | 全部为未批准候选，不覆盖PDF |
| [PROJECT_PROFILE.template.json](PROJECT_PROFILE.template.json) | 平台与字体配置、28项待标定参数 | 复制到项目填写，未知值保留 `null` |

JSON键名、单位和枚举保留技术标识，方便代码读取；说明文字使用中文。本格式为自描述参考格式，没有宣称可直接导入某种设计工具。

标题栏必须显式选型：默认复刻配置使用 **framed有框按钮**，小圆角随画布缩放；追求10.3新版原生形态时选 **lightweight-10.3轻量文字式**。二者来源和完整状态见关键控件标准，不能混为同一套样式。

## 参考来源

- **主来源：** [BlackBerry 10 UI Guidelines，黑莓官方PDF](https://developer.blackberry.com/devzone/files/design/bb10/UI_Guidelines_BlackBerry_10.pdf)。出版日期2015-03-23，共156页。仓库所有页码指PDF物理页。
- **补充参考：** [mybabysexy/BB10-UI-Kit](https://github.com/mybabysexy/BB10-UI-Kit)，核对固定提交 [`cbed5b7`](https://github.com/mybabysexy/BB10-UI-Kit/tree/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b)。
- **当前仓库：** [boySang/BlackBerry-10-Design-Language](https://github.com/boySang/BlackBerry-10-Design-Language)。

PDF与第三方仓库不一致时，以PDF为准；项目明确选择的复刻变体与跨平台适配须单独记录，不能反称为官方要求。证据分为原文要求E、原文建议R、原图示例V、数学推导D、项目约定P与第三方参考K。

## 轻量分发与校验

本仓库**不提交原PDF、整页截图、提取图片、字体、压缩包或演示应用**，通过官方链接、页码、来源哈希和参数保持可追溯。PDF链接可带 `#page=31` 等页码锚点；不支持该锚点的阅读器请手动跳页。

使用Python 3运行：

```sh
python3 tools/validate.py
```

检查JSON、规则入口、156页覆盖、引用、归一化比例和仓库体积。若已从官方链接另行下载原PDF，还可额外核对文件哈希：

```sh
python3 tools/validate.py --pdf /path/to/UI_Guidelines_BlackBerry_10.pdf
```

脚本不会自动下载文件，也不能替代项目界面、设备或逐帧动画的验收。第三方字体、商标、图像与代码仍保留各自权利，详见来源说明。
