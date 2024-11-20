---
title: 理解JSON
category: 额外
description: JSON的初步了解
---

# 理解JSON

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/guide/understanding-json.html](https://wiki.bedrock.dev/guide/understanding-json.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/understanding-json.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/understanding-json.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@a8f9908938d012a976ac9ee3b2b5b11095fd7570 -->
- 该页面的作者有：
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @solvedDev -->
    - <!-- md:samp @Joelant05 -->
    - <!-- md:samp @Dreamedc2015 -->
    - <!-- md:samp @sermah -->
    - <!-- md:samp @cda94581 -->
///

/// tip
这是一个附录页面。你可以从[这里](../guide/index.md)开始阅读指南。
///

JSON是一种简单的文本文件格式，既易于人类理解，也易于计算机处理。基岩版使用.json文件作为附加包的“语言”，因此你需要扎实地理解如何读取和编写JSON！如果你之前从未听说过JSON，建议你阅读[本教程](https://www.digitalocean.com/community/tutorials/an-introduction-to-json)。它将教你编写有效JSON文件所需的所有知识。

## 有效的JSON

编写JSON时需要记住的重要一点是，它必须是*完全无错误的*，否则将无法正常工作。即使是一个错误的字符或一个多余的逗号也会导致整个文件失败。因此，编写有效的JSON至关重要。

我们可以使用一个名为[json lint](https://jsonlint.com/)的在线工具来检查我们的JSON是否有效。只需将你的代码粘贴到网站中，然后按`Validate JSON`。你将收到一个响应，指示你的代码是否正确，以及任何错误的位置和类型。

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

数组用两个方括号`[]`表示。它们代表一个*列表*。我们可以在列表中放入*其他数据结构*。列表中的每个*元素*应以逗号分隔。

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

对象用两个大括号`{}`表示。对象是一种特殊的语法，包含*具名*的数据结构。名称称为`key`，结构称为`value`。本页之前的示例是一个包含其他数据类型示例的*字典*。

这种键值语法的格式如下：`"<key>": <任何结构>`。注意键周围的引号和冒号。

下面是一个对象的示例，包含几个*键值对*。

```json title=""
{
  "a_list_of_integers": [1, 2, 3],
  "is_json_cool": true
}
```

我们需要用逗号分隔每个键值对。

我们将对象的键值对称为其*子项*或称为在对象*内部*。

## JSON结构

在Minecraft中，JSON文件总是以一个*对象*开始，你可以记住这是两个大括号`{}`。我们在这个对象*内部*编写代码，以键值对的形式表示。

以下是一个用于Minecraft附加包的简单json文件示例：

```json title=""
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

仔细查看格式。你会发现整个结构是由我们已经学习过的数据结构构建的。如果你想练习你的JSON技能，请尝试回答以下问题：

-   顶层对象中有多少个键？你能命名它们吗？
-   `format_version`的值是什么？
-   `"loop"`键中存储的数据类型是什么？（字符串、布尔值等）

## 故障排除示例

以下是一些示例，帮助你理解在Discord或在线上可能收到的反馈。我们在谈论JSON错误时往往使用技术术语，因此希望本节能帮助你熟悉这些术语：

---

你写道：`"format_version": 1.12`

他们说：“*format_version的值写错类型了。它应该是一个字符串。*”

请记住，`类型`指的是结构之一：`字符串`、`整数`、`浮点数`、`数组`或`对象`。如果我们检查代码，会发现我们将`format_version`设置为了`浮点数`，而不是`字符串`。我们可以通过在`"1.12"`周围添加引号来解决此问题。

---

你写道：`[1 2 5 6]`

他们说：“*你的数组没写逗号。*”

请记住，数组元素需要用逗号分隔。你的数组应该是这样的：`[1, 2, 5, 6]`

---

他们说：“*你把格式版本错放到描述内部了。它应该外放在顶层。*”

这意味着`"format_version"`的键值对目前是描述的一个*子项*。你应该将键值对从描述对象中复制/粘贴出来，并放置在顶层。