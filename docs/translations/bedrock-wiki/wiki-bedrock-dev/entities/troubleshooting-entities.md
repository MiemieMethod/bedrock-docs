---
title: 实体故障排除
category: 一般
nav_order: 3
tags:
    - 帮助
mentions:
    - SirLich
    - BlueFrog130
    - SmokeyStack
    - MedicalJewel105
    - aexer0e
    - ChibiMango
    - RonarsCorruption
description: 实体故障排除指南。
---

:::tip
本页面包含关于_实体_的故障排除信息。在继续之前，请阅读我们的[全局故障排除](../guide/troubleshooting.md)文档。
:::

:::warning
请务必检查内容日志！
:::

## 0.0.0 - 你搞错了

接受某些地方出了问题的事实。_没有人_在_任何_层面上能够免于这些错误，所以不要感到冒犯，想“我当然会这样做！”然后跳过某个步骤！

<Button link="#_1-0-0-两个包都激活了吗">继续</Button>

## 1.0.0 - 两个包都激活了吗？

确保资源包和行为包在世界中都是激活状态（避免意外出现此问题的一个好方法是将每个包设置为另一个包的依赖项，在两个包的manifest.json文件中，这样添加或删除一个包时会自动添加/删除另一个包）。

<Button link="#_2-0-0-确定问题是在RP还是BP">继续</Button>

## 2.0.0 - 确定问题是在RP还是BP

你遇到的问题可以通过实体的生成蛋在创意库存中的外观来显著缩小范围。即使你不希望实体有生成蛋，也请暂时进行以下更改，直到找到问题：

### 在RP中

确保.entity文件具有自定义的spawn_egg对象，如下所示：

<CodeHeader></CodeHeader>

```json
"spawn_egg":{
    "base_color": "#FF0000",
    "overlay_color": "#FFFF00"
}
```

你选择的颜色需要是除了“#000000”以外的其他颜色。

### 在BP中

确保`is_spawnable`和`is_summonable`设置为true，并且`is_experimental`在描述对象中设置为false：

<CodeHeader></CodeHeader>

```json
"description":{
    "identifier": "wiki:example_entity",
    "is_spawnable": true,
    "is_summonable": true,
    "is_experimental": false
}
```

### 结果

我根本看不到生成蛋：<Button link="#_3-1-0-bp">去</Button>

我看到了我的实体的生成蛋，但它只是黑色的，并且在我生成或召唤时实体并没有出现：<Button link="#step-3-2-0-rp-entity">去</Button>

我看到了我的实体的生成蛋，并且它具有我选择的颜色，但实体在我生成或召唤时仍然没有出现：<Button link="#step-3-3-0-rp-resources-still-writing-because-this-is-going-to-be-extensive">去</Button>

## 3.0.0 - 定位具体问题

## 3.1.0 - BP

_你在创意库存中看不到你的实体的生成蛋，即使在行为文件中确保“is_spawnable”设置为true。_

这意味着游戏根本没有检测到实体的行为文件。一些常见原因包括：

-   行为文件中的语法错误
-   文件夹命名错误

### 3.1.1 - 语法错误

.json文件中的单个语法错误会导致整个文件失效并被忽略。要检查你的文件是否没有语法错误，请访问[Json Lint](https://jsonlint.com/)，将行为文件的内容粘贴到大框中，然后点击“验证JSON”。
（注意：虽然该网站会将//注释标记为错误，但Minecraft确实允许.json文件包含它们）

### 3.1.2 - 文件夹命名错误

确保包含行为文件的文件夹命名为“entities”，而不是“entity”。在行为包中，文件夹通常命名为“entities”，而在资源包中，它们通常命名为“entity”。我知道，这并不愉快。

## 第3.2.0步 - RP .entity

_你在创意库存中看到了你的实体的生成蛋，但它是黑色的（可能有一个奇怪的名字，比如“item.spawn_egg.entity.wiki:your_mob.name”），并且在你生成/召唤时没有任何东西出现。_

这意味着你有一个有效的行为文件，但由于某种原因，游戏没有将其连接到资源包中的相应.entity文件。一些常见原因包括：

-   .entity文件中的语法错误
-   实体的标识符不匹配
-   .entity文件指向的一个或多个资源无效
-   检查你的RP文件夹是否为“entity”，而你的BP文件夹是否为“entities”

### 第3.2.1步 - 语法错误

.json文件中的单个语法错误会导致整个文件失效并被忽略。要检查你的文件是否没有语法错误，请访问[Json Lint](https://jsonlint.com/)，将行为文件的内容粘贴到大框中，然后点击“验证JSON”。
（注意：虽然该网站会将//注释标记为错误，但Minecraft确实允许.json文件包含它们）

### 第3.2.2步 - 标识符不匹配

行为文件中的“identifier”必须与.entity文件中的完全相同，包括命名空间（冒号前的部分，如`minecraft`在`minecraft:bat`中），并且除非是默认生物，否则都不应使用`minecraft`作为命名空间。

你的标识符也不应包含任何空格或特殊字符（冒号与ID之间的冒号除外），而且由于罕见的边缘案例错误原因，你应避免命名空间或ID以除小写字母以外的任何内容开头。以数字或大写字母开头_不应该_再是一个问题，但在游戏的早期版本中并非总是如此，因此过去曾偶尔出现过以数字或大写字母开头会产生意外效果的错误。因此，如果可能的话，最好避免这种情况。

### 第3.2.3步 - 无效资源

.entity文件中的实体ID与行为文件中使用的ID不匹配。

## 第3.3.0步 - RP资源：（进行中）

_你在创意库存中看到了你的实体的生成蛋，并且它确实具有你在.entity文件的“spawn_egg”对象中指定的正确颜色，但在你生成/召唤时没有任何东西出现，或者只是一个阴影。_

这意味着你有一个有效的`.behavior`和`.entity`文件，但在`.entity`文件中指向的某个内容要么是损坏的文件，要么是指向另一个有效文件但导致损坏文件的文件。

首先：

-   看不见，没有阴影 -> 坏RP引用：<Button link="#_3-3-1-invisible-no-shadow">去</Button>
-   看不见，阴影存在 -> 几何问题：<Button link="#_3-3-2-invisible-shadow-exists">去</Button>
-   可见，奇怪的纹理 -> 纹理问题：<Button link="#_3-3-3-visible-weird-texture">去</Button>
-   可见，奇怪的可见性问题 -> 材质问题：<Button link="#_3-3-4-visible-weird-visibility-stuff">去</Button>

### 3.3.1 - 看不见，没有阴影

这可能是由于...。首先确保你的实体在它的位置上（例如，它没有瞬间消失）。

### 3.3.2 - 看不见，阴影存在

这种情况可能是由于几何体错误或材质错误（如果使用半透明即发光纹理）。

1. 确保几何体名称没有拼写错误，几何体文件有效且几何体偏移量正确。
2. 确保你使用的是正确的材质。例如，一些材质仅支持发光纹理。
3. 检查你的渲染控制器。问题可能出在这里。

### 3.3.3 - 可见，奇怪的纹理

### 3.3.4 - 可见，奇怪的可见性问题