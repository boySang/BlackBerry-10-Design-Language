# BB10 UI Kit 与 PDF 的对照

整理作者：酒鬼成员
核对仓库：[mybabysexy/BB10-UI-Kit](https://github.com/mybabysexy/BB10-UI-Kit/tree/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b)；固定提交 `cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b`，核对日期 2026-10-23。

它是受 BB10 启发的 Android Jetpack Compose 组件库。它提供有用的实现结构，但不是 PDF 的官方可执行版本。以下判断以读取到的代码为准；仓库自己的说明与实现不完全一致时，不据说明推断真实行为。

## 主要差异与裁决

| 项目 | 仓库实际代码或明确文档约定 | PDF 依据 | 本设计语言的处理 |
| --- | --- | --- | --- |
| 标题栏 | `Bb10Scaffold` 必需 title 且始终构造标题栏；DESIGN 要求每页 header | p.33 按内容是否能说明上下文决定，列出不用标题栏的情况 | 不采用强制每页标题栏；需要无标题栏和沉浸页能力 |
| 全局 Tab | `Scaffold(tabs=...)` 替换顶部标题；`Bb10TabBar` 在 header 下方 | p.23 全局 Tab 在底部操作栏，仅一级；p.34 分段控件是同内容过滤 | 全局 Tab 回到底部；顶部控件只能按 segmented 的职责重新审视 |
| Tab 与分段混称 | 顶部 local/global 都以 Tab strip 表达 | p.23、34 明确不同层次和职责 | 用语义决定布局，不能只因库名叫 Tab 就视为官方导航 |
| 明亮背景 | `background=#F8F8F8` | p.116 背景色样为 `#FFFFFF` | 严格基线取 PDF；其他 surface/field 值另列项目参数 |
| 文字色 | 暗主文 `#FFFFFF`、次文 `#A6A6A6`；亮主文 `#262626`、次文 `#6E6E6E` | p.116、151 为 `#F0F0F0/#969696` 与 `#323232/#646464`，还有三级色 | 采用 PDF 文字色；不把库颜色写入源 token |
| 默认主色 | Blue `#0092CC` | p.116 Sky Blue 同值 | 可直接参考这一主色值 |
| 其他品牌色 | Teal、Green、Orange、Red、Purple 为自定近似色 | p.116 有另一组明确 primary/base 色样 | 库的六主题色是扩展候选，不是官方全色板 |
| 渐变 | 默认蓝部件 `#0080B2→#008FC9`；selection `#087098→#065F81` | p.142-143 明确的数值是图标渐变，selected 为 `#3CBCE7→#01A8DF` | 两者作用域不同；不能拿库部件渐变冒充 PDF 图标值，也不能把 PDF 图标值刷给所有部件 |
| 字体 | `FontFamily.Default`，没有 Slate Pro 选项 | p.149 首选 Slate Pro | 系统字体可作项目适配，须声明；不能声称已还原原字体 |
| 字号与行高 | title 18sp、body 15sp 等；行高字号 ×1.3 | p.150 为源字号表，未给上述角色对应和统一行高 | 这些仅是 Android 候选参数，不直接取代 PDF 表 |
| 尺度系统 | Regular/Compact 用 dp；近方屏差值 ≤40dp 选 Compact | p.19-20 du/bucket；p.48 要对方屏优化，未指定这套阈值 | 复用分档机制思路，数值作为项目配置；不能宣称 1du=1dp |
| 触控目标 | `minTouchTarget=48dp`，control 通过 touchHeight 扩大 | p.110 同时写 101px、7.2mm，需按 ppi | 保留视觉尺寸与热区分离的方法；真实密度和物理目标另校验 |
| 图标 | 24 网格、约 1.8 线宽，代码绘制的线框风格 | p.130-144 有 du 画布、焦点区、轮廓/细节、视觉重量和微渐变要求 | 代码绘制可参考；24/1.8 不作为 PDF 参数，形态仍需核对 |
| 操作栏数量 | `maxVisibleActions=5`；splitActions 在无溢出时可显示 5 个业务动作 | p.32 尽量不超过 3 个动作；p.23 最多 4 个 Tab 是另一规则 | 限制业务动作数量，不用库默认容量驱动信息架构 |
| 主动作 | 一个居中圆形主动作、底部动作与返回位置接近 PDF | p.31-32 标志性动作需按高频与上下文使用 | 可借鉴组成；不能每页无条件提供主圆按钮 |
| 全局应用菜单 | DESIGN 将 Settings 等也列入右侧菜单；未提供与 PDF 同等的顶部应用菜单模式 | p.81-82 顶部下滑、内容向下推、最多 5 项、帮助左/设置右 | Android 可有可达性适配入口，但角色仍分开；严格目标需补顶部模式 |
| 默认确认焦点 | Dialog 非 focusContent 时将焦点设到 confirm | p.106 破坏动作不能作为默认按钮 | 用于 Delete 等操作前必须改造默认焦点，不能直接套通用默认 |
| Dialog 几何 | 宽 85%、最大 420dp，未见半屏高度约束 | p.86 建议低于半屏，复杂任务用 Sheet/Card | 这些宽度是库参数；小方屏、大字体和键盘时需额外验收 |
| 透明度 | DESIGN 通用禁用写 0.4，文本字段段落又写 50% | p.142-143 图标禁用 50%，其余无统一值 | 不从库内部不一致推断统一官方值；具体控件分别核验 |
| 动画 | 文档给 120-240ms 等不同时间、不同焦点恢复策略 | p.147 给原则，未给时长 | 可作原型候选，不能称官方时序 |
| 显示缩放 | 必须提供 0.85/1/1.25/1.5/2 五档，整体修改 Density，保留系统 fontScale | p.75 尊重用户字号，没有要求每个 App 必须自建五档显示缩放 | 保留用户可访问性目标；是否整体缩放由目标平台决定 |
| 补充控件 | Stepper、密码显隐、字符计数、只读等 | PDF 未给这些控件完整规范 | 可设计为扩展，单独标记，并遵循已有语言 |

## 可以借鉴的工程做法

将颜色、尺寸、字体、图标和组件分层；统一触摸与 D-pad 的可点击入口；编辑状态下隔离快捷键；弹层将焦点留在自身并在关闭后恢复；给仅图标按钮、状态和标题添加辅助技术语义；用资源文件本地化。这些方法有助于实现 `INPUT-03/05`、`STATE-01` 和无障碍原则。

但“代码里有某个机制”不代表在本项目上已经验证通过。这里没有运行该库测试、编译 Catalog 或安装到设备。README 所列测试属于仓库声明，不能移作本参考包的通过证据。

## 原型候选值

在 [tokens.kit-reference.json](tokens.kit-reference.json) 中保留了源代码的颜色、字号、间距和栏高等候选，全部带 K 级标记。它们与 `tokens.source.json` 分开，项目选择采用后再记入自己的批准配置。不能用库的 40dp 按钮高、48dp 热区或 18sp 标题来填补“官方参数”。

仓库 DESIGN 开头声称不使用渐变，但同一文档后续颜色章节以及 `Bb10Colors.kt` 实际定义了渐变。对这种情况，本对照按实际 token 判断，不能只读原则段就断言当前实现没有渐变。

## 引用代码与资产的边界

仓库 [LICENSE](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/LICENSE) 标注 **CC BY-NC 4.0**；README 要求署名并注明修改，且不允许商业使用。若以后要将代码集成进商业 App，应先解决其适用许可。本仓库仅整理参考与差异，没有分发该库源码或将其引入依赖。

其 README 明确不包含 BlackBerry 标志、官方图标和 Slate Pro 字体。采用这个库不会自动补齐字体或官方资产缺口。

## 固定来源入口

- [README](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/README.md)：组件清单、用法、限制和许可声明。
- [DESIGN](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/DESIGN.md)：仓库自身的设计约定，K 级。
- [Colors](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/tokens/Bb10Colors.kt)、[Dimens](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/tokens/Bb10Dimens.kt)、[Typography](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/tokens/Bb10Typography.kt)：真实参数。
- [Scaffold](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/components/Scaffold.kt)、[Tabs](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/components/Tabs.kt)、[ActionBar](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/components/ActionBar.kt)：结构与动作容量。
- [Theme](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/theme/Bb10Theme.kt)、[Dialog](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/components/Dialog.kt)、[Icons](https://github.com/mybabysexy/BB10-UI-Kit/blob/cbed5b73f3e5bc1aef10500034e4a2b9f191cd7b/bb10-kotlin-ui-kit/src/main/kotlin/duc1607/bb10/designsystem/icons/Bb10Icons.kt)：缩放、对话框焦点和图标画法。
