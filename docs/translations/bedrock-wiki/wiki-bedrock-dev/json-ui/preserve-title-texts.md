---
title: 保持标题文本
category: 教程
tags:
    - 中级
mentions:
    - shanewolf38
    - SmokeyStack
description: 在本教程中，你将学习如何保持绑定数据，并根据包含特定字符串的标题更新元素。
---

在本教程中，你将学习如何保持绑定数据，并根据包含特定字符串的标题更新元素。

## 概述

标题是传递数据到用户界面系统的一种非常常见的方法。只有在传入包含特定字符串的标题时，更新这些数据的元素才会非常有用，而忽略所有不包含该字符串的标题。尽管本教程的名称中提到了标题，但此方法适用于通过绑定传入的任何数据（如副标题、玩家记分板名称等），而不仅限于标题。

为了保存特定字符串，使用`visibility_changed`绑定更新条件与`source_control_name`结合，仅在包含特定字符串时更新绑定，然后将该绑定传递给另一个元素。

## 标题命令

以下代码创建一个标签元素，当添加到根面板时，如果该标题包含字符串“update”，则在屏幕上显示该标题（“update”文本从显示的文本中移除）。在此之后传入的任何标题仅在包含字符串“update”时更新显示的文本。

```json title="RP/ui/hud_screen.json"
"preserved_title_display": {
	"$update_string": "update",   // 标题必须包含此字符串才能更新元素
	"type": "label",
	"text": "#text",
	"controls": [
		{
			"data_control": {
				"type": "panel",
				"size": [ 0, 0 ],
				"bindings": [
					{
						"binding_name": "#hud_title_text_string"      // 读取当前标题字符串
					},
					{
						"binding_name": "#hud_title_text_string",
						"binding_name_override": "#preserved_text",   // 当此元素的可见性变化时更新 #preserved_text
						"binding_condition": "visibility_changed"
					},
					// 当传入包含更新字符串的标题时，元素变为可见，然后立即变为不可见
					{
						"binding_type": "view",
						"source_property_name": "(not (#hud_title_text_string = #preserved_text) and not ((#hud_title_text_string - $update_string) = #hud_title_text_string))",
						"target_property_name": "#visible"
					}
				]
			}
		}
	],
	"bindings": [
		{
			"binding_type": "view",
			"source_control_name": "data_control",   						// 从 "data_control" 子元素读取绑定
			//"resolve_sibling_scope": true,		 						// 如果 "data_control" 是提取绑定的元素的兄弟元素，则需要此项
			"source_property_name": "(#preserved_text - $update_string)",   // 从要显示的文本中移除字符串更新文本
			"target_property_name": "#text"
		}
	]
},
```

变量`$update_string`定义了必须包含在标题命令中的特定字符串，以便该元素更新。子元素`data_control`用于在标题文本包含更新字符串时保持标题文本。这必须是传递保存文本的元素的子元素或兄弟元素，因为`data_control`元素的可见性必须变化以保存文本。元素中的第一个绑定将跟踪当前标题文本，第二个绑定将在元素的可见性变化时将当前标题文本保存到`#preserved_text`绑定中，第三个绑定将在传入包含更新字符串的标题时使元素可见，然后立即将其变为不可见。

`data_control`元素中的第三个绑定有两个主要部分，只有当两个部分都为真时，元素才会可见。
1. `not (#hud_title_text_string = #preserved_text)` - 当当前标题文本与保存的标题文本不匹配时为真
2. `not ((#hud_title_text_string - $update_string)` - 当当前标题文本包含更新字符串时为真

当传入的标题包含更新字符串且与当前保存的文本不同，两部分都为真，元素更新。然后，保存的文本被更新，第一部分立即变为假，使元素变为不可见。