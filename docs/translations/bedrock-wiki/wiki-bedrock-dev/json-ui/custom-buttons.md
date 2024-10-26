---
title: 添加自定义按钮
category: 教程
tags:
  - 初学者
mentions:
  - TheoristMC
description: 在本教程中，您将学习开关/按钮的工作原理、如何添加它们以及它们之间的区别。
---

在本教程中，您将学习开关/按钮的工作原理、如何添加它们以及它们之间的区别。

## 概述

“如何制作/放置按钮”是关于JSON-UI时常被问到的问题之一。今天，您将学习它们是如何工作的以及如何创建它们。

目前有两种类型的按钮：开关和按钮（尽管开关有所不同，但其功能类似）。

## 开关

以下代码将创建一个从原版文件(`ui/ui_template_toggles.json`)引用的开关。点击开关后，它将显示我们创建的`toggled_image`。

<CodeHeader>RP/ui/your_file.json</CodeHeader>

```json
"custom_toggle@common_toggles.light_text_toggle": {
  "$toggle_name": "our_toggle",
  "$button_text": "模板开关",
  "size": [90, 15],
  "$toggle_view_binding_name": "view_toggle"
},

"toggled_image": {
  "type": "image",
  "texture": "textures/items/apple",
  "size": [32, 32],
  
  "bindings": [
    {
      "binding_type": "view",
      "source_control_name": "view_toggle",
      "source_property_name": "#toggle_state",
      "target_property_name": "#visible"
    }
  ]
}
```

-   `$toggle_name`是我们开关的名称（可以选择性使用）
-   `$toggle_view_binding_name`是我们开关的主要关键部分，因为它是切换我们元素的部分。
-   在`source_control_name`中，我们通过`$toggle_view_binding_name`获取开关的状态。
-   在`source_property_name`中，我们获取来自开关的`#toggle_state`绑定。（注意：它返回布尔值）

如果我们希望图像在关闭而不是打开时显示呢？

我们只需将`source_property_name`的表达式更改为`(not #toggle_state)`。

## 按钮

以下代码创建一个从原版文件(`ui/ui_template_buttons`)引用的按钮。

按钮具有硬编码的按钮ID，这意味着我们只能使用原版ID，而不能使用自定义ID。唯一的例外是如果按钮用作动画播放器。

<CodeHeader>RP/ui/your_file.json</CodeHeader>

```json
"custom_button@common_buttons.light_text_button": {
  "$pressed_button_name": "button.menu_exit",
  "$button_text": "退出游戏",
  "size": [90, 15]
}
```

-   `$pressed_button_name`是我们的主要关键部分。如您所见，我使用了一个硬编码的按钮ID，它会弹出提示以退出游戏。

## 按钮与开关

在选择按钮和开关时，请考虑您想要执行的操作。按钮适合于离散操作，如“退出游戏”，而开关则用于切换状态，如打开/关闭设置。选择按钮用于单一操作，选择开关用于状态更改。