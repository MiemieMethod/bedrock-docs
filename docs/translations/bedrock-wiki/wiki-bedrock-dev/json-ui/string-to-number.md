---
title: 字符串转数字
category: 教程
tags:
    - 中级
mentions:
    - shanewolf38
    - SmokeyStack
    - ThomasOrs
description: 在本教程中，你将学习如何将数字字符串转换为数字，以及将数字转换为文本字符串。
---

在本教程中，你将学习如何将数字字符串转换为数字，以及将数字转换为文本字符串。

## 概述

在许多情况下，文本字符串会通过标题、动作栏、记分板或其他来源传递到用户界面。当我们希望根据传入的字符串动态更改元素时，能够进行数字比较是非常有帮助的。然而，像“34”或“89”这样的数字字符串通常会被视为文本，无法与数字进行比较，只能与其他字符串比较。在这种情况下，我们需要将该字符串转换为数字。

要将字符串转换为数字，我们将利用乘法。将任何数字字符串乘以一个数字，或从包含数字的字符串中去除文本，将使游戏将该值视为数字而不是字符串。

## 字符串转数字

以下代码创建了一个标签元素，当添加到根面板时，如果记分板侧边栏中的最高值在100到999之间，则显示该值。

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>

```json
"string_to_number": {
    "type": "label",
    "text": "#player_score_sidebar",
    "bindings": [
        {
            "binding_name": "#player_score_sidebar",
            "binding_type": "collection",
            "binding_collection_name": "scoreboard_scores"
        },
        {
            "binding_type": "view",
            "source_property_name": "(#player_score_sidebar * 1)",   // 将分数从字符串转换为数字
            "target_property_name": "#score"
        },
        {
            "binding_type": "view",
            "source_property_name": "((#score > 99) and (#score < 1000))",   // 在100到999之间可见
            "target_property_name": "#visible"
        }
    ]
}
```

第一个绑定读取记分板侧边栏中的最高值（绑定被硬编码为字符串），第二个绑定通过将其乘以1将该分数转换为数字（也可以从中减去任何文本字符串），第三个绑定使元素仅在分数大于99且小于1000时可见。

**注意：** 如果你希望数字以浮点数而不是整数形式读取，请将一个使用浮点数的变量或绑定传入方程中，例如除以1.0（必须通过变量或绑定进行--直接放置浮点数无效）。这对于`#clip-ratio`绑定特别有用。

## 数字转字符串

以下代码创建了一个标签元素，当添加到根面板时，显示格式为“strength: #”的标题中传入的数字#。

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>

```json
"number_to_string": {
	"type": "label",
	"text": "#text",
	"bindings": [
		{
			"binding_type": "global",
			"binding_name": "#hud_title_text_string"
		},
		{
			"binding_type": "view",
			"source_property_name": "('§z' + (#hud_title_text_string - 'strength: '))",
			"target_property_name": "#text"
		}
	]
}
```

在使用标题、副标题等传入文本与数字组合的情况下，此方法将允许你仅显示数字。在去除多余文本以将字符串简化为数字后，在数字前添加文本以将值转换为字符串（`text`参数无法读取具有数值的绑定）。在这种情况下，减法周围的括号并不是必需的，但存在是为了表明它转换了数字，而不仅仅是将其保持为字符串。添加的文本`§z`是一个不存在的Minecraft格式代码，因此它不会在数字的显示中注册，也不会影响标签的颜色参数。如果数字周围存在无法全部减去的可见文本，一个好的方法是将元素包装在一个面板中，并设置`"clips_children": true`和适当的大小。