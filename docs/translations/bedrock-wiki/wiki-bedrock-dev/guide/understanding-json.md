---
title: 理解JSON
category: 额外
description: JSON的初步了解
nav_order: 1
prefix: 'a. '
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - Dreamedc2015
    - sermah
    - cda94581
---

::: tip
这是一个附录页面。您可以从[这里](../guide/index.md)开始阅读指南。
:::

JSON是一种简单的文本文件格式，既易于人类理解，也易于计算机处理。基岩版使用.json文件作为附加包的“语言”，因此您需要扎实地理解如何读取和编写JSON！如果您之前从未听说过JSON，建议您阅读[本教程](https://www.digitalocean.com/community/tutorials/an-introduction-to-json)。它将教您编写有效JSON文件所需的所有知识。

## 有效的JSON

编写JSON时需要记住的重要一点是，它必须是_完全无错误的_，否则将无法正常工作。即使是一个错误的字符或一个多余的逗号也会导致整个文件失败。因此，编写有效的JSON至关重要。

我们可以使用一个名为[json lint](https://jsonlint.com/)的在线工具来检查我们的JSON是否有效。只需将您的代码粘贴到网站中，然后按`Validate JSON`。您将收到一个响应，指示您的代码是否正确，以及任何错误的位置和类型。

## 数据结构

在JSON中，数据可以以多种格式编写。每种格式专门用于表示特定类型的数据。以下是我们可用的结构：

| 名称   | 示例      | 说明                                  |
|--------|-----------|---------------------------------------|
| 字符串 | "hello!"  | 单词或字符。需要使用引号。           |
| 整数   | 15        | 一个数字。不需要引号。                |
| 浮点数 | 1.2       | 一个小数。不需要引号。                |
| 布尔值 | true      | 只能是true或false。不需要引号。       |

现在，以.json格式表示：

```json
{
  "my_string": "hello!",
  "my_int": 15,
  "my_float": 1.2,
  "my_bool": true
}
```

除了这些简单的结构外，我们还有两种特殊结构。特殊结构用于*嵌套*其他数据。

### 数组

数组用两个方括号`[]`表示。它们代表一个_列表_。我们可以在列表中放入_其他数据结构_。列表中的每个_元素_应以逗号分隔。

一些示例：

| 结构           | 注释                                   |
|----------------|----------------------------------------|
| [1, 2, 3]      | 一个整数列表。                         |
| ["Red", "blue"]| 一个字符串列表。注意引号！            |

现在，以.json格式表示：

```json
{
   "my_ints": [1, 2, 3],
   "my_strings": ["Red", "blue"]
}
```

### 对象

对象用两个大括号`{}`表示。对象是一种特殊的语法，包含_命名_的数据结构。名称称为`key`，结构称为`value`。本页之前的示例是一个包含其他数据类型示例的*字典*。

这种键值语法的格式如下：`"<key>": <任何结构>`。注意键周围的引号和冒号。

下面是一个对象的示例，包含几个_键值对_。

<CodeHeader></CodeHeader>

```json
{
	"a_list_of_integers": [1, 2, 3],
	"is_json_cool": true
}
```

我们需要用逗号分隔每个键值对。

我们将对象的键值对称为其_子项_或称为_在_对象内。

## JSON结构

在Minecraft中，JSON文件总是以一个_对象_开始，您可以记住这是两个大括号`{}`。我们在这个对象_内部_编写代码，以键值对的形式表示。

以下是一个用于Minecraft附加包的简单json文件示例：

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.12.0",
	"animations": {
		"animation.car.wheel_spin": {
			"loop": true,
			"animation_length": 1.0,
			"bones": {
				"front_wheels": {
					"rotation": ["q.modified_distance_moved * -30", 0, 0]
				},
				"back_wheels": {
					"rotation": ["q.modified_distance_moved * -30", 0, 0]
				}
			}
		}
	}
}
```

仔细查看格式。您会发现整个结构是由我们已经学习过的数据结构构建的。如果您想练习您的JSON技能，请尝试回答以下问题：

-   顶层对象中有多少个键？您能命名它们吗？
-   `format_version`的值是什么？
-   `"loop"`键中存储的数据类型是什么？（字符串、布尔值等）

## 故障排除示例

以下是一些示例，帮助您理解在Discord或在线上可能收到的反馈。我们在谈论JSON错误时往往使用技术术语，因此希望本节能帮助您熟悉这些术语：

---

您写道：`"format_version": 1.12`

他们说："_format_version的值类型错误。它应该是一个字符串。_"

请记住，`type`指的是结构之一：`String`、`Int`、`Float`、`Array`或`Object`。如果我们检查代码，会发现我们将`format_version`设置为`Float`，而不是`String`。我们可以通过在`"1.12"`周围添加引号来解决此问题。

---

您写道：`[1 2 5 6]`

他们说："_您的数组缺少逗号。_"

请记住，数组元素需要用逗号分隔。您的数组应该是这样的：`[1, 2, 5, 6]`

---

他们说：_"您不小心将格式版本放在了描述内部。它应该放在顶层外部。_"

这意味着`"format_version"`的键值对作为描述的_子项_。您应该将键值对从描述对象中复制/粘贴出来，并放置在顶层。