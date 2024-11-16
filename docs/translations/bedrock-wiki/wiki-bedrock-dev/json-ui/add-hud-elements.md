---
title: 添加HUD元素
category: 教程
tags:
    - 初学者
mentions:
    - shanewolf38
    - SmokeyStack
description: 在本教程中，你将学习如何向HUD屏幕添加元素。
---

在本教程中，你将学习如何向HUD屏幕添加元素。

## 概述

HUD屏幕是游戏中大部分时间显示的界面，展示了玩家的关键信息。你可能会想在这个屏幕上添加许多元素，例如在完成某些事件后弹出的文本、显示玩家能量的耐力条、显示玩家速度的速度计等等！

要将你创建的元素添加到HUD屏幕上，你需要使用`modification`参数将新的`control`（元素）添加到`root_panel`。根面板是一种面板类型元素，几乎包含了所有显示在HUD上的元素。

## 单个元素

以下代码创建了一个图像元素，在屏幕顶部显示一个黑色方块，创建了一个标签元素，在屏幕右上角显示文本“hud text”，并对`root_panel`进行修改，将图像和标签元素添加到HUD屏幕。

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>

```json
"hud_square": {
	"type": "image",
	"texture": "textures/ui/Black",   // 原版纹理
	"anchor_from": "top_middle",
	"anchor_to": "top_middle",
	"size": [ 64, 64 ],
	"offset": [ 0, 4 ]
},

"hud_text": {
	"type": "label",
	"text": "hud text",
	"anchor_from": "top_right",
	"anchor_to": "top_right",
	"offset": [ -4, 4 ]
},

"root_panel": {
	"modifications": [
		{
			"array_name": "controls",
			"operation": "insert_front",
			"value": [
				{ "hud_square@hud.hud_square": {} },
				{ "hud_text@hud.hud_text": {} }
			]
		}
	]
},
```

所有添加到HUD屏幕的元素都在根面板`modifications`的`value`部分列出。添加元素时指定的命名空间（例如`@hud.hud_square`）可以更改，如果添加的元素存在于另一个命名空间中。例如，如果`hud_square`元素是在`scoreboard`命名空间下的scoreboards.json UI页面中创建的，你在将元素添加到根面板时应使用`@scoreboard.hud_square`。

## 组合元素

出于组织目的，通常不建议将多个元素单独添加到根面板。以下代码将之前定义的`hud_square`和`hud_text`元素（未显示）包装在一个名为`hud_elements_panel`的面板元素中，然后将该元素添加到HUD屏幕的根面板中。效果与单个元素代码相同。

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>
```json
"hud_elements_panel": {
	"type": "panel",
	"controls": [
		{ "hud_square@hud_square": {} },
		{ "hud_text@hud_text": {} }
	]
},

"root_panel": {
	"modifications": [
		{
			"array_name": "controls",
			"operation": "insert_front",
			"value": [
				{ "hud_elements_panel@hud.hud_elements_panel": {} }
			]
		}
	]
},
```

`hud_elements_panel`没有直接定义其大小参数，因此它将继承其父元素（`root_panel`）的大小。这使得子元素的锚定、百分比大小等能够相对于HUD屏幕正常工作。