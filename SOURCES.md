# 来源、署名与引用边界

整理作者：酒鬼成员

## 黑莓官方PDF

- 标题：BlackBerry 10 UI Guidelines。
- 出版方：BlackBerry。
- 出版日期：2015-03-23；共156页。
- 官方链接：[查看或下载PDF](https://developer.blackberry.com/devzone/files/design/bb10/UI_Guidelines_BlackBerry_10.pdf)。
- 用于本规范核对的文件名：`UI_Guidelines_BlackBerry_10.pdf`。
- SHA-256：`1992691e60573f037fa366880c64094448f668f774fefde4eb7ca8714d0b2364`。

页码从1开始，指PDF物理页。原文文字、图中标注、截图形态与整理者推导使用不同证据等级；没有标注的尺寸不能仅因截图可测量就声称是官方规范值。主规范以10.3的视觉演进为主要基线，同时注明早期截图与标题栏变体。

原文件及图像通过上述官方地址获取，不随本仓库分发。`tokens.visual-profile.json` 中的提取图分辨率与校验码仅用于记录原先的量测依据，不能当成官方PDF本身的哈希或独立图片下载地址。需要复核时打开对应PDF页。

## 第三方参考仓库

- 仓库：[mybabysexy/BB10-UI-Kit](https://github.com/mybabysexy/BB10-UI-Kit)。
- 核对提交：[`cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b`](https://github.com/mybabysexy/BB10-UI-Kit/tree/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b)。
- 重点：[设计说明](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/DESIGN.md)、组件结构、颜色、尺寸、字体映射、键盘/焦点与本地化处理。
- 上游许可：[CC BY-NC 4.0许可文件](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/LICENSE)。

参考仓库是实现参考，不能取代官方PDF。其颜色、尺寸与时长在 `tokens.kit-reference.json` 中保留为K级未批准候选；差异见 [对照说明](KIT_COMPARISON.md)。本仓库没有复制该组件库源码，没有构建或设备兼容性测试结论。

## 本仓库的整理工作

酒鬼成员负责中文结构化整理、规则编号、组件与状态说明、过渡契约、来源区分、配置模板、项目接入和验收方法。源PDF、黑莓名称/商标、字体和第三方仓库内容仍归各自权利人。

引用本仓库时建议保留：仓库链接、采用的提交号或版本、整理作者、主来源及第三方出处。字体与资产的发布授权不能由引用设计规范自动获得；直接复用第三方代码时应分别遵循其许可。

本仓库暂未指定统一开源许可证。以链接和规则编号作为设计参考，与复制、改编或再分发仓库文字和脚本是不同的使用方式；需要后者时请向整理作者确认授权。公开可读和上游许可不代表本仓库所有内容具有同一许可。

## 推荐引用格式

```text
酒鬼成员：《BlackBerry 10设计语言》，版本1.2.0。
https://github.com/boySang/BlackBerry-10-Design-Language
主来源：BlackBerry 10 UI Guidelines，2015-03-23。
实现参考：mybabysexy/BB10-UI-Kit，固定提交cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b。
```

## 图标来源

历史Action包的原始下载地址、2013存档、ZIP/XLS校验和，以及两个官方GitHub样例库的完整提交见[图标来源与许可](icons/README.md)和[机器索引](icons/catalog.json)。索引保留原文件名和实际像素，不改色或描摹原图。该历史包是特定年份的资源，不是所有10.3系统图标的许可全集。

历史ZIP/XLS没有附独立再分发授权记录；bbUI.js还含第三方素材许可段落。仓库的官方发布方、图形原创者、源码许可和资产许可须分别记录。6个Cascades样例按随库原Apache-2.0许可复用；其余原图仅索引。联系表工具不改变上游许可条件。
