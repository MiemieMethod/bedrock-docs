---
title: textures_list.json
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - AFoxyToast
    - TheItsNameless
description: textures_list 文件是 Minecraft 用于缓存每个纹理的方式，以便比逐个查找纹理文件夹中的每个图像更快地检索它。
---

## 概述

`textures_list` 文件是 Minecraft 用于 *缓存* 每个纹理的方式，以便比逐个查找纹理文件夹中的每个图像更快地检索它。这在你拥有大量纹理时尤其重要，因为 Minecraft 可能会出现混淆，导致纹理互换，甚至根本无法加载它们。如果文件中未列出纹理，Minecraft 通常会抛出内容日志 _警告_。如果你的纹理数量较少，可以忽略此警告，但建议你还是将纹理列出。

## 文件中可以使用哪些纹理？

任何纹理！任何纹理都可以并且 _应该_ 在 textures_list.json 文件中使用，以确保最佳实践和性能。

## 文件结构

结构很简单。文件本身位于 `RP/textures` 中，名为 `textures_list.json`。该文件包含你想要在文件中列出的每个纹理的文件路径：

```json title="RP/textures/textures_list.json"
[
	"textures/blocks/foo",
	"textures/blocks/bar",

	"textures/items/foo",
	"textures/items/bar",

	"textures/models/foo",
	"textures/models/bar",

	"textures/entity/foo",
	"textures/entity/bar"
]
```

## 自动化

如果你有很多纹理，手动列出所有纹理路径显然会很繁琐。在这种情况下，你可以开始使用 [Regolith](https://bedrock-oss.github.io/regolith/) 及其出色的过滤器。