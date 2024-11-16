---
title: 最佳实践
category: 通用
nav_order: 2
tags:
    - 指南
mentions:
    - LukasPAH
    - SmokeyStack
    - TheItsNameless
    - ThomasOrs
description: 处理JSON UI的最佳方法。
---

:::tip 信息
本文内容假设你对JSON-UI系统有一定了解。如果你是JSON-UI的新手，请通过阅读[JSON-UI简介](../json-ui/json-ui-intro.md)和[JSON-UI文档](../json-ui/json-ui-documentation.md)来熟悉它。
:::

## 最大化兼容性并最小化UI出错的可能性

JSON-UI与所有其他附加包系统不同，因为**JSON-UI没有版本控制**。你对UI所做的任何更改可能会在Mojang更新和修复JSON-UI系统时出错。幸运的是，你可以采取几种方法来防止在Mojang更改原版UI时你的UI出错。

### 仅修改必要部分
最有效的最小化UI出错风险的方法是仅进行你需要的更改。例如，如果你只想禁用经验值栏阴影，你可能会认为应该将其添加到你的附加包中的`hud_screen.json`文件。

```json
{
    "progress_text_label": {
        "type": "label",
        "shadow": false,
        "text": "#level_number",
        "color": "$experience_text_color",
        "anchor_from": "top_middle",
        "anchor_to": "bottom_middle",
        "bindings": [
            {
                "binding_name": "#level_number",
                "binding_type": "global"
            },
            {
                "binding_name": "#level_number_visible",
                "binding_type": "global",
                "binding_name_override": "#visible"
            }
        ]
    }
}
```

这在技术上是正确的，但容易出错，原因有几个：如果Mojang更改了绑定名称怎么办？如果他们更改了锚点怎么办？如果Mojang为元素添加了偏移怎么办？你所做的更改是与原版UI战略性地合并的，因此包含额外的细节是多余的，可能导致你的自定义UI出错。这可以简单地通过仅在元素中包含`shadow`属性来避免：

```json
{
    "progress_text_label": {
        "shadow": false
    }
}
```

这不仅在未来更不容易出错，而且看起来也更简洁，显著减少了文件大小。

通过仅修改必要的部分，你减少了UI中潜在的故障点数量，这大大有助于防止随着原版UI的更新而出错你的自定义UI。最后一点，**如果你在附加包中包含了原版UI文件的所有内容以及你的更改，你就错误地使用了JSON-UI**。

### 利用修改策略
使用[维基文档中记录的修改策略](../json-ui/json-ui-intro.md#modifications)是另一个减少在Mojang更新UI时出错机会的好方法。例如，许多附加包制作者在HUD中添加元素以显示与游戏玩法相关的信息。一个常用的策略是将自定义UI (`custom_ui@namespace.custom_ui`) 合并到`hud_screen.json`的根面板中。

```json
{
    "root_panel": {
        "type": "panel",
        "$xp_control_offset|default": [ 0, -13 ],
        "variables": [
            {
                "requires": "$education_edition",
                "$left_helpers": "hud.left_helpers_edu"
            },
            {
                "requires": "(not $education_edition)",
                "$left_helpers": "hud.left_helpers"
            }
        ],
        "controls": [
            {
                "custom_ui@namespace.custom_ui": {} // <--- 人们倾向于在这里添加自定义UI！
            },
            { "left_helpers@$left_helpers": {} },
            { "right_helpers@hud.right_helpers": {} },
            { "emote_helpers@hud.emote_helpers": {} },
            { "centered_gui_elements@centered_gui_elements": {} },
            { "centered_gui_elements_at_bottom_middle@centered_gui_elements_at_bottom_middle": {} }
            ... // 剩余的控件在这里继续。
        ]
    }
}
```

通过将你的自定义控件直接与原版根面板合并，你大大增加了UI在未来出错的几率。例如，如果Mojang将来更改根面板中的控件名称，你的UI可能会引用不存在或已大幅更改的UI元素，这*可能*会导致错误和/或崩溃。

为避免这种情况，请利用[修改策略](../json-ui/json-ui-intro.md#modifications)。

```json
{
    "root_panel": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": [
                    {
                        "custom_ui@namespace.custom_ui": {}
                    }
                ]
            }
        ]
    }
}
```

使用修改数组的修改策略是与原版UI战略性地合并，并且不会改变根面板中的兄弟控件。这样提高了与其他资源包的兼容性，并减少了你的UI出错的机会。

### 避免修改嵌套树中的控件
另一个常见的故障点是修改深度嵌套的控件。以下是一个具有嵌套控件的UI元素示例。

```json
{
    "label": {
        "type": "label",
        "text": "hello world",
        "color": [1, 1, 1]
    },

    "bg_image": {
        "type": "image",
        "texture": "textures/ui/Black",
        "alpha": 0.7
    },

    "panel_with_label_and_bg": {
        "type": "panel",
        "size": ["100%c", "100%c"],
        "controls": [
            {
                "bg_image@bg_image": {
                    "size": ["100%c + 2px", "100%c + 2px"],
                    "controls": [
                        {
                            "label@label": {
                                "layer": 5
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

为了最佳修改此UI，你应尽可能避免嵌套树。例如，如果你想将标签颜色修改为灰色而不是白色，并将背景图像设为透明，请在元素定义中修改颜色和不透明度，而不是在树中修改（记住只修改必要的内容！）：

```json
{
    "label": {
        "color": [0.5, 0.5, 0.5]
    },

    "bg_image": {
        "alpha": 0
    }
}
```

然而，有时无法避免修改树。在这种情况下，你应使用以下语法定位嵌套树中特定的控件。例如，要修改背景图像大小和标签层级，请使用以下语法。

```json
{
    "panel_with_label_and_bg/bg_image": {
        "size": ["100%c", "100%c"]
    },

    "panel_with_label_and_bg/bg_image/label": {
        "layer": -5
    }
}
```

`/`将定位到指定元素的子控件。请注意，如果指定的目标子控件名称不存在，将导致资源包错误。你的UI将正常运行，但由于此原因，最好尽量避免定位嵌套树中的控件。

### 利用单一入口点
为了向特定屏幕添加自定义UI，UI需要在某个点与原版UI合并。这称为入口点，最佳实践是在单一入口点将你的自定义UI与原版UI合并，以减少UI出错的可能性。以下是在`hud_screen.json`中使用两个入口点的示例：

```json
{
    "root_panel": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": [
                    {
                        "custom_ui_control_1@namespace_1.custom_ui_control_1": {}
                    }
                ]
            }
        ]
    },

    "hud_content": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": [
                    {
                        "custom_ui_control_2@namespace_2.custom_ui_control_2": {}
                    }
                ]
            }
        ]
    }
}
```

我们可以将入口点数量减少到一个，并将`custom_ui_control_1`和`custom_ui_control_2`整合到`hud_content`或`root_panel`控件中，如下所示：

```json
{
    "root_panel": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": [
                    {
                        "custom_ui_control_1@namespace_1.custom_ui_control_1": {}
                    },
                    {
                        "custom_ui_control_2@namespace_1.custom_ui_control_2": {}
                    }
                ]
            }
        ]
    }
}
```
使用单一入口点减少了UI出错的可能性，因为如果Mojang更新了`hud_content`控件名称，某些自定义UI可能会出错。使用单一入口点还使你的UI更易于调试，因为你只需处理一个入口点。

### 避免在原版命名空间中工作
如果你修改大量UI或添加大量自定义UI，应尽量避免在原版命名空间文件中工作。你可以通过在[UI定义文件](../json-ui/json-ui-intro.md#ui-defs)中添加具有唯一[命名空间](../json-ui/json-ui-intro.md#namespaces)的自定义UI文件来实现。记住，当你需要将UI合并到入口点时，可以使用`element@namespace.element`语法引用其他命名空间中的元素。通过在自定义命名空间中添加自定义UI，你减少了与原版控件名称冲突的可能性，这可能会引发问题。此外，像大多数其他附加包系统一样，命名空间可以支持前缀，例如`wiki:namespace`，可以引用为`element@wiki:namespace.element`。前缀还可以帮助避免与原版命名空间的冲突。

## 最大化性能

在FPS方面，JSON-UI是第二耗费性能的附加包子系统，仅次于实体。你是否曾经想过为什么打开背包会将你的FPS减半？简短的回答是JSON-UI极其未优化，导致FPS降低。添加大量自定义UI可能会带来**显著的开销**，导致持续的游戏内帧率下降、屏幕加载时间变长以及整体糟糕的用户体验。

### 最小化UI中的运算符数量

[运算符](../json-ui/json-ui-intro.md#using-operators)用于UI中评估条件、执行数学运算和修改字符串。这些运算符对于[条件渲染](../json-ui/json-ui-intro.md#conditional-rendering)等技术有用，但使用这些会**增加大量开销**。例如，如果你有一个变量`"$var": "(2 * (-1 * $number))"`，将其简化为`"$var": "(-2 * $number)"`性能更高。最好尽可能简化表达式，删除不需要的表达式，以尽可能加快评估速度。

### 最小化UI中的绑定数量
类似于运算符，使用许多[绑定](../json-ui/json-ui-intro.md#bindings)**也会增加显著的开销**。设置界面打开时间过长的部分原因是所有切换和选项都链接到特定的绑定，数量众多。删除不影响功能的绑定，或简化绑定，是提高性能的另一个极佳方法。

### 避免添加不必要的控件
也许提高JSON-UI性能的最佳方法是删除未使用或不必要的控件。在此示例中，子控件`panel`是不需要的，因为它是一个空面板。

```json
{
    "element": {
        "type": "image",
        "texture": "textures/ui/Black",
        "controls": [
            {
                "panel": {
                    "type": "panel"
                }
            },
            {
                "label": {
                    "type": "label",
                    "text": "hello world"
                }
            }
        ]
    }
}
```

要解决此问题，你可以将其从UI树中删除，或在`panel`控件中添加`"ignored": true`。使用`"ignored": true`与删除它相同。控件及所有子控件将不会在UI中被评估，导致与其根本不存在时相同的性能效果。**使用**`"visible": false`**不会产生相同的效果，控件仍会被评估。**

```json
{
    "element": {
        "type": "image",
        "texture": "textures/ui/Black",
        "controls": [
            {
                "label": {
                    "type": "label",
                    "text": "hello world"
                }
            }
        ]
    }
}
```
```json
{
    "element": {
        "type": "image",
        "texture": "textures/ui/Black",
        "controls": [
            {
                "panel": {
                    "type": "panel",
                    "ignored": true
                }
            },
            {
                "label": {
                    "type": "label",
                    "text": "hello world"
                }
            }
        ]
    }
}
```

有时，你可以简化并将多个控件合并为一个单一元素。例如，如果你想基于`#hud_title_text_string`是否为特定数字1-5来渲染特定的图像，你可能认为应该添加5个单独的控件来分别评估：

```json
{
    "image_template": {
        "type": "image",
        "texture": "$texture",
        "bindings": [
            {
                "binding_name": "#hud_title_text_string"
            },
            {
                "binding_type": "view",
                "source_property_name": "(#hud_title_text_string = $binding_text)",
                "target_property_name": "#visible"
            }
        ]
    },

    "image_1@image_template": {
        "$texture": "textures/ui/example_1",
        "$binding_text": "1"
    },

    "image_2@image_template": {
        "$texture": "textures/ui/example_2",
        "$binding_text": "2"
    },

    "image_3@image_template": {
        "$texture": "textures/ui/example_3",
        "$binding_text": "3"
    },

    "image_4@image_template": {
        "$texture": "textures/ui/example_4",
        "$binding_text": "4"
    },

    "image_5@image_template": {
        "$texture": "textures/ui/example_5",
        "$binding_text": "5"
    }
}
```
采取更有思想的方法，这可以大幅简化为一个控件，整体上减少运算符、绑定和控件的数量。

```json
{
    "image": {
        "type": "image",
        "texture": "#texture",
        "bindings": [
            {
                "binding_name": "#hud_title_text_string"
            },
            {
                "binding_type": "view",
                "source_property_name": "(((#hud_title_text_string * 1) > 0) and ((#hud_title_text_string * 1) < 6))",
                "target_property_name": "#visible"
            },
            {
                "binding_type": "view",
                "source_property_name": "('textures/ui/example_' + #hud_title_text_string)",
                "target_property_name": "#texture"
            }
        ]
    }
}
```

总的来说，为了提高UI的性能，了解你具体想要做什么，并尽可能按照这些通用指南进行调整是很重要的。保留单个控件未优化可能不会产生明显的差异。然而，当你开始保留许多未优化的控件时，性能可能会在已经未优化的UI系统上进一步下降。