---
title: 文本与本地化
mentions:
  - ThijsHankelMC
  - SirLich
  - aexer0e
  - MedicalJewel105
  - Luthorius
  - Fabrimat
  - TheDoctor15
  - Hatchibombotar
  - ChibiMango
  - SmokeyStack
  - Sprunkles
description: Minecraft是一款在全球范围内拥有完全本地化文本的游戏。
---

Minecraft是一款在全球范围内拥有完全本地化文本的游戏。为了实现这一点，Minecraft采用了一种系统，其中内部**翻译键**根据每种语言分配值。Minecraft会为自定义实体、物品和区块生成翻译键，而我们需要在资源包中为它们分配本地化名称。

## 语言文件

### 文件位置

语言文件通常放在资源包的“texts”文件夹中，文件扩展名为`.lang`。这些文件可以放在行为包中，但它所能更改的唯一可翻译文本是包清单的名称和描述。

<FolderView :paths="[
  'RP/texts/en_US.lang',
  'RP/texts/languages.json',
  'RP/manifest.json'
]"
></FolderView>

目前，Minecraft支持29种语言，具体描述见[§ 原版语言](../concepts/text-and-translations.md#vanilla-languages)。

### 格式

语言文件的格式相当简单。翻译以键值对的形式提供，用等号（`=`）分隔，键为翻译键，值为字符串。值中不能包含换行符。

```toml
wiki.example_translation.line_1=第一行！
wiki.example_translation.line_2=第一行之后的一些信息。
```

可以使用两个井号（`##`）添加注释，既可以作为行注释，也可以作为行内注释。所有在井号之后的文本都是注释，直到下一行。

:::warning
行内注释的尾随空格不会被修剪。如果想缩进注释，请使用Tab字符。
:::

```toml
## 翻译者注：我觉得把这个放在这里会很有趣。
item.flint_and_steel.name=火石与史蒂夫	##[sic]
```

翻译可以包含文本的替代项。替代项可以是有序的（`%1`、`%2`等）或无序的（`%s`）。原版翻译的值由游戏填充，而玩家可以通过使用原始JSON文本格式的命令手动设置替代项的值，例如使用[`/tellraw`](../concepts/rawtext.md)。

```toml
commands.op.success=已提升权限：%s
immersive_reader.book_page_header=第%1页，共%2页
```

### 用法

本地化几乎可以在任何可以使用文本的地方进行，包括（但不限于）：

-   包名称和描述
-   实体、物品或区块名称
-   书中的页面
-   标牌上的行
-   `/tellraw`和`/titleraw`命令
-   对话中的文本

然而，有些文本是无法翻译的，例如在铁砧中重命名的物品。

## 本地化

:::tip
为每种主要语言创建语言文件的副本是一种良好的实践。例如，为了支持完整的英语，应该分别创建`en_US.lang`和`en_GB.lang`文件，以覆盖美国和英国的英语。
:::

在编辑语言文件时，还必须在`texts`文件夹中添加一个`languages.json`文件，包含一个数组，列出你计划更改的每种语言。这让Minecraft知道应该为这些语言应用本地化。

<CodeHeader>RP/texts/languages.json</CodeHeader>

```json
[
  "en_US",
  "en_GB",
  "fr_FR"
]
```

### 自定义语言

通过全局资源包，可以通过`languages.json`和`language_names.json`文件引入自定义语言。一旦包被全局应用，语言可以在游戏设置的“语言”选项卡中更改。

在以下示例中，假设我们有两个功能齐全的语言文件，一个名为`xx_XX.lang`，另一个名为`yy_YY.lang`。

<CodeHeader>RP/texts/languages.json</CodeHeader>

```json
[
  "xx_XX",
  "yy_YY"
]
```

`language_names.json`也是一个数组，但这次用于定义显示的语言名称。

<CodeHeader>RP/texts/language_names.json</CodeHeader>

```json
[
  [ "xx_XX", "新语言（自定义语言#1）" ],
  [ "yy_YY", "维基语（自定义语言#2）" ]
]
```

:::warning
使用自定义语言时，请确保在禁用存储该语言的资源包之前，先卸下该语言，否则Minecraft将崩溃。
:::

### 工具
如果微软正在本地化你的.lang文件，则必须遵循特定的技术要求。

- 确保注释前是&lt;tab&gt;#（**而不是**空格）。
- 确保换行符为Windows风格（CR+LF），而不是Unix风格。
- 不能包含重复的键。
- 字符串必须添加注释以便于翻译。

你可以使用免费的基于浏览器的[LangUtil工具](https://langutil.bedrockexplorer.com)来帮助处理这些问题。

### 原版语言

以下是Minecraft默认支持的29种语言的表格。

| 文件ID | 语言                  | 国家            |
|--------|-----------------------|------------------|
| id_ID  | 印尼语                | 印尼              |
| da_DK  | 丹麦语                | 丹麦              |
| de_DE  | 德语                  | 德国              |
| en_GB  | 英语                  | 英国              |
| en_US  | 英语                  | 北美              |
| es_ES  | 西班牙语              | 西班牙            |
| es_MX  | 墨西哥西班牙语       | 墨西哥            |
| fr_CA  | 加拿大法语            | 加拿大            |
| fr_FR  | 法语                  | 法国              |
| it_IT  | 意大利语              | 意大利            |
| hu_HU  | 匈牙利语              | 匈牙利            |
| nl_NL  | 荷兰语                | 荷兰              |
| nb_NO  | 博克马尔语            | 挪威              |
| pl_PL  | 波兰语                | 波兰              |
| pt_BR  | 巴西葡萄牙语         | 巴西              |
| pt_PT  | 葡萄牙语              | 葡萄牙            |
| sk_SK  | 斯洛伐克语            | 斯洛伐克          |
| fi_FI  | 芬兰语                | 芬兰              |
| sv_SE  | 瑞典语                | 瑞典              |
| tr_TR  | 土耳其语              | 土耳其            |
| cs_CZ  | 捷克语                | 捷克共和国        |
| el_GR  | 希腊语                | 希腊              |
| bg_BG  | 保加利亚语            | 保加利亚          |
| ru_RU  | 俄语                  | 俄罗斯            |
| uk_UA  | 乌克兰语              | 乌克兰            |
| ja_JP  | 日语                  | 日本              |
| zh_CN  | 中文（简体）          | 中国              |
| zh_TW  | 中文（繁体）          | 台湾              |
| ko_KR  | 韩语                  | 韩国              |