# 图标来源、原图与许可

整理作者：酒鬼成员 · 目录版本：2026-10-24

本目录含155个去重源文件的资料：121个历史Action条目、6个Cascades样例和28个bbUI样例。**只随库分发6个Cascades原PNG**；其余149条提供来源与元数据。仓库样例与历史官方包分别记录，第三方Subway不并入官方目录。分类与完整语义见[INDEX.md](INDEX.md)，机器字段见[catalog.json](catalog.json)，选型标准见[ICON_LIBRARY.md](../ICON_LIBRARY.md)。

## 历史Action包

- 原始文件名：`Action_Icons_BlackBerry_10.zip`。
- 原下载地址保留在JSON中，属于BlackBerry历史下载域名，不承诺当前可用。
- [2013-11-22历史存档](https://web.archive.org/web/20131122015712id_/http://downloads-us.blackberry.com/upr/developers/downloads/Action_Icons_BlackBerry_10.zip)，时间戳`20131122015712`。
- ZIP：273604 bytes；SHA-256 `63363885c2ede7b3ef6ce77dd21c817978c206add2fe40896863d51d89a8b7f0`；122个成员（121 PNG与Action_Icons.xls）。
- 原XLS的大小与SHA-256见[catalog.json](catalog.json)的`sources.official_action_pack_2013.xls`。本库中文语义为121行描述摘要；不再分发XLS中的嵌入图像。

包内没有附独立LICENSE、NOTICE或明确再分发授权记录。因此仅登记来源、分类、语义、尺寸和哈希；ZIP、XLS、121枚PNG及含它们的完整联系图不上传本仓库。存档可取得、来源为官方不等于MIT或其他再分发许可。完整性指这一个2013包，不表示全部10.3系统图标。

## Cascades样例原图：Apache-2.0

固定仓库：[blackberry/Cascades-Samples](https://github.com/blackberry/Cascades-Samples/tree/2429ddebecd56d92b018be98ab66eb7178f05b7c)，完整提交`2429ddebecd56d92b018be98ab66eb7178f05b7c`。

| 样例 | 随库原文件 | 原许可 |
| --- | --- | --- |
| appshot | `assets/images/ic_done.png`及8ppd/12ppd同名变体，共3枚 | [上游LICENSE](https://github.com/blackberry/Cascades-Samples/blob/2429ddebecd56d92b018be98ab66eb7178f05b7c/appshot/LICENSE) · [随库原件](licenses/cascades-samples/appshot/LICENSE) |
| datamanagerusage | `assets/images/ic_add.png`、`ic_edit.png`、`ic_delete.png`，共3枚 | [上游LICENSE](https://github.com/blackberry/Cascades-Samples/blob/2429ddebecd56d92b018be98ab66eb7178f05b7c/datamanagerusage/LICENSE) · [随库原件](licenses/cascades-samples/datamanagerusage/LICENSE) |

6个PNG位于`assets/cascades_samples/`下，保留原仓库目录及文件名；原字节、像素、颜色、透明度均未修改。索引`assetPath`相对于本icons目录，`gitBlob`与SHA-256用于核对；两份原LICENSE按上游字节分别保留，未合并或改写。固定提交的这两个样例目录未见独立NOTICE。

这些文件随各自Apache-2.0样例项目发布。分发时保留原许可与适用的归属/版权说明，修改时记录修改；许可不授予BlackBerry商标权，也不代表黑莓为使用本库的产品背书。来源归属是BlackBerry GitHub样例仓库，不把这些自定义样例图形称为系统Action标准。appshot三个`ic_done`是相机图，不是勾选。

一手来源链补充：[datamanagerusage样例初始提交](https://github.com/blackberry/Cascades-Samples/commit/8a2d6ee2b3760f0e05f123751e33f18b29c21b6c)、[将图形改为自定义图标的提交](https://github.com/blackberry/Cascades-Samples/commit/98ac006c07abf5b8b4a8ad0a4f66cd79813fc70d)、[appshot样例初始提交](https://github.com/blackberry/Cascades-Samples/commit/0d32927fa4fd2fa0861f1223a91faa1cb92ecf8b)。这些补充链接不替代实际采用的固定提交。

## bbUI样例：代码与图片来源分开

固定仓库：[blackberry/bbUI.js](https://github.com/blackberry/bbUI.js/tree/5da817014b2773f48b825ac7f32f9df944a0f1fd)，完整提交`5da817014b2773f48b825ac7f32f9df944a0f1fd`。

- `samples/bb10/www/images/icons/icon1.png`至`icon25.png`，25个130×130图形：上游[README Authors](https://github.com/blackberry/bbUI.js/blob/5da817014b2773f48b825ac7f32f9df944a0f1fd/README.md#authors)明确将Plastique Icons归于Scott Lewis / Iconify.it，并列为CC BY-SA 3.0。根[LICENSE](https://github.com/blackberry/bbUI.js/blob/5da817014b2773f48b825ac7f32f9df944a0f1fd/LICENSE)中Plastique前置说明同样写BY-SA 3.0，但后附BY 3.0正文，存在上游文档内部差异。本次保留来源与哈希，不捆绑原图、不把它们统称Apache或BlackBerry原创。
- `samples/bb10/www/images/menu_icons/icon1.png`至`icon3.png`，3个65×65图形：仓库有Apache-2.0项目许可与贡献记录，但二进制没有逐文件版权声明，本次未独立确认素材原创归属链，继续仅索引。不能说“没有任何仓库许可”，也不以发布者身份代替逐资产来源核对。

这些编号图没有可靠官方系统动作名，本目录保留“用途待核”。图片归属、源码许可和官方仓库发布方是三项不同信息；不要将它们合并成“官方免费图标”。

## 未并入的第三方资料

[mariuszostrowski/subway](https://github.com/mariuszostrowski/subway/tree/98cc590b68185db5746604cdb23831bb313f0c0f)是第三方图标套系，固定提交`98cc590b68185db5746604cdb23831bb313f0c0f`。移交的326条包括306个不同内容及20个重复副本；仅保留排除数量和来源，不复制到官方目录。该库自己的许可、作者署名和产品使用决定由采用它的项目单独处理。

## 联系表与校验

[contact-sheet.html](contact-sheet.html)为不联网联系表，自带6枚有许可原图及155条资料；其余图像需在本机选择已经取得的PNG目录。页面不上传本机文件，不用外链图片自动补齐。打印得到的联系表如包含仅作本机参考的原图，也不因此取得公开分发许可。

在仓库根目录运行`python3 tools/validate_icons.py`检查目录和6枚随库原图；本机完整资源核验、私人图表生成与参数见[图标使用标准](../ICON_LIBRARY.md)。原图校验通过不代表某个App的热区、语义、适配或许可流程已经完成。
