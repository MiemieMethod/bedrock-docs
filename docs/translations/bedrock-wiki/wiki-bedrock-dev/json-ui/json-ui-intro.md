---
title: JSON UI入门
category: General
nav_order: 1
tags:
    - guide
mentions:
    - sermah
    - KalmeMarq
    - SirLich
    - solvedDev
    - Joelant05
    - GTB3NW
    - stirante
    - MedicalJewel105
    - r4isen1920
    - shanewolf38
    - LeGend077
    - mark-wiemer
    - TheItsNameless
    -
    - QuazChick
description: JSON UI介绍。
---

## 介绍

:::warning
JSON UI 正在被 [Ore UI](https://github.com/Mojang/ore-ui) 取代。请注意，任何使用 JSON UI 的附加包将在未来几年内失效。
:::

:::tip
本页概述了包含 JSON UI 基础知识的信息。有关更详细的文档，请查看 [JSON UI 文档](/json-ui/json-ui-documentation) 页面。
:::

游戏的用户界面是数据驱动的，可以被修改。它允许我们修改某些用户界面如何渲染以及在某种程度上如何行为。要开始，所有原版 UI 文件存储在 `RP/ui/...` 文件夹中。

JSON UI 可能包含以下文件：

### 系统文件

这些是 JSON UI 中使用的内置文件：

-   `_global_variables.json` - 用于标示后续使用的默认变量
-   `_ui_defs.json` - 用于引用 UI 中使用的文件

### 屏幕

这些文件包含用于渲染屏幕的元素：

-   `hud_screen.json` - 显示主游戏屏幕，其中渲染了游戏内功能如快捷栏
-   `inventory_screen.json` - 显示玩家的物品栏屏幕
-   等等。

### 模板

这些文件存储 JSON UI 元素供其他命名空间（如屏幕）使用：

-   `ui_common.json` - 包含诸如按钮等元素，这些元素在大多数其他命名空间中被引用，例如设置屏幕的按钮
-   `ui_template_*.json` - 包含整齐组织的元素，供其他命名空间使用

## UI 定义

`_ui_defs.json` 文件在一个数组中引用所有 JSON UI 文件。

你可以创建新文件，例如我们将添加 `RP/ui/button.json` 和 `RP/my_ui/main_menu.json`。在文件中，我们会这样列出它们：

<CodeHeader>RP/ui/_ui_defs.json</CodeHeader>

```json
{
    "ui_defs": ["ui/button.json", "my_ui/main_menu.json"]
}
```

-   确保追加你所引用的 UI 的完整文件路径 - 包括文件扩展名（例如 `*.json`），从资源包根文件夹开始！
-   只引用你在包中添加的新 UI 文件。你无需引用原版文件或其他第三方 JSON UI 文件，因为它会自动与其他包合并。
-   你可以使用 `RP/ui/...` 文件夹外的自定义文件路径，或引用 `RP/ui/...` 文件夹内子文件夹中的文件。
-   你可以追加除 `*.json` 之外的自定义文件扩展名 - 只要文件内容有效并用 JSON 编写。

## 全局变量

我们可以在 `_global_variables.json` 文件中这样标示一个变量 `"$info_text_color"` 及其值 `[0.8, 0.8, 0.8]`：

<CodeHeader>RP/ui/_global_variables.json</CodeHeader>

```json
{
    "$info_text_color": [0.8, 0.8, 0.8]
}
```

不同 JSON UI 文件中的其他元素可以引用这个变量以便后续使用：

<CodeHeader>vanilla/my_ui/file1.json</CodeHeader>

```json
{
  "some_info": {
    ...
    "text": "Hey",
    "color": "$info_text_color"
  }
}
```

<CodeHeader>vanilla/my_ui/file2.json</CodeHeader>

```json
{
  "info": {
    ...
    "text": "Information",
    "color": "$info_text_color"
  }
}
```

-   你可以在 `_global_variables.json` 文件中添加更多变量及其值，使用逗号分隔。
-   存储在此文件中的变量是常量且**单向的**。因此，你不能修改一个命名空间中的默认变量以供其他命名空间使用。

## 命名空间

命名空间是 UI 文件的标识符。它们用于在所有其他文件中访问某些文件中的元素。在添加新命名空间时，必须具有唯一的名称。

例如，我们在命名空间 `one` 中有一个元素 `foobar`：

<CodeHeader>vanilla/ui/file_a.json</CodeHeader>

```json
{
  "namespace": "one",

  "foobar": {...}
}
```

然后我们可以在不同的命名空间 `two` 中引用相同的元素：

<CodeHeader>vanilla/ui/file_b.json</CodeHeader>

```json
{
  "namespace": "two",

  "fizzbuzz@one.foobar": {...}
}
```

在引用不同命名空间的元素时，必须使用以下格式：

```json
"[element_name]@[namespace_reference].[element_name_reference]"
```

## 屏幕

屏幕文件包含在适当情况下调用的用户界面，例如用于渲染玩家物品栏屏幕的 `inventory_screen.json` 文件。这些文件包含游戏直接访问数据的根元素。

屏幕是特殊的，因为它只能访问数据，而其他屏幕可能无法访问。

## 元素

JSON UI 元素是 JSON UI 中数据的基本形式。每个命名空间的元素必须具有唯一名称，以避免与相同名称但功能可能不同的其他元素冲突。

这里元素 `type` 是 `label`，所以调用时会渲染 `Hello World` 的文本：

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
    "test_element": {
        "type": "label",
        "text": "Hello World"
    }
}
```

### 类型

以下是一些元素类型，它们是 `type` 属性的可能值：

-   `label` - 用于创建文本对象
-   `image` - 用于从提供的文件路径渲染图像
-   `button` - 用于创建交互式和可点击的元素
-   `panel` - 一个空容器，你可以在其中存储所有其他可能重叠的元素
-   `stack_panel` - 一个空容器，你可以在其中按堆叠存储所有其他不重叠的元素
-   `grid` - 使用另一个元素作为模板，然后在多行多列中重复渲染它
-   `factory` - 基于另一个元素渲染一个元素，能够调用硬编码值和变量
-   `custom` - 与另一个属性 `renderer` 配对，渲染硬编码的 JSON UI 元素
-   `screen` - 游戏直接调用的元素，通常是根面板元素

## 动画

当在 `type` 属性的位置使用 `anim_type` 属性时，你可以创建动画以动画化其他元素。

动画元素可以在其他非动画元素类型（如 `label` 和 `panel`）中被引用。

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
  "namespace": "example_nm",

  "anim_size": {
    "anim_type": "size",
    "easing": "linear",
    "from": [ "100%", 27 ],
    "to": [ "100% + 3px", 30 ],
    "duration": 1.25
  },

  "anim_alpha": {
    "anim_type": "alpha",
    "easing": "linear",
    "from": 1,
    "to": 0.5,
    "duration": 2
  },

  "test_animated_element": {
    ...
    "anims": [
      "@example_nm.anim_size",
      "@example_nm.anim_alpha"
    ]
  }
}
```

### 类型

以下是元素类型列表，它们是 `anim_type` 属性的可能值：

-   `alpha` - 接受浮点值，动画化元素的透明度
-   `offset` - 接受一个数组，动画化元素相对于其锚点的位置
-   `size` - 接受一个数组，动画化大小（宽度，高度）
-   `flip_book` - 接受整数值，动画化翻书纹理或逐帧图像
-   `uv` - 接受一个数组，根据 UV 纹理动画化图像
-   `color` - 接受从 0.0 到 1.0 的浮点 RGB 值，动画化元素的颜色
-   `wait` - 接受数字值，用于等待/停留
-   `aseprite_flip_book` - 类似于 `flip_book` 动画，使用精灵表。更多信息 [这里](/json-ui/aseprite-animations)
-   `clip`

## 使用运算符

你可以在 JSON UI 中使用运算符，以及 `$变量` 和 `#绑定` 到常见属性如 `size` 和 `offset`。以下是你可以使用的属性列表：

| 运算符名称          | 运算符 | 示例                                                                      |
| ------------------- | ------ | ------------------------------------------------------------------------- |
| 加法                | +      | `"100% + 420px"` `($text + ' my')` `($index + 2)` `('#' + $bdg_nm + '_name')` |
| 减法                | -      | `"100% - 69px"` `($text - ' my')` `($index - 13)`                             |
| 乘法                | *      | `($var * 9)` `(#value * 5)`                                                   |
| 除法                | /      | `($var / 12)` `(#value / 2)`                                                  |
| 等于                | =      | `($var = 12)` `($var = 'this_text')` `(#name = 'Wither')`                     |
| 大于                | >      | `(#value > 13)`                                                               |
| 小于                | <      | `($var < 4)`                                                                  |
| 大于或等于          | > 或 = | `(#value > 2 or #value = 2)`                                                  |
| 小于或等于          | < 或 = | `(#value < 2 or #value = 2)`                                                  |
| 逻辑与              | and    | `($is_school and $is_open)`                                                   |
| 逻辑或              | or     | `($is_cool or $is_awesome)`                                                   |
| 逻辑非              | not    | `(not #name)` `(not (#name = 'text'))` `(not $name)`                          |

## 变量

变量不仅限于 `_global_variables.json` 文件。相反，它可以在其他命名空间中直接使用和标示，以便将数据从一个元素传递到另一个元素。

### 定义变量

在每个字符串前面添加符号 `$` 以标示其为变量。变量可以存储整数、浮点数、布尔值、字符串和数组。

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
  "test_element": {
    ...
    // 定义变量
    "$array_variable": [ 10, 10 ],
    "$string_variable": "foobar",
    "$float_variable": 1.0,
    "$string_variable2": "my_button.template_button",

    // 使用变量
    "size": "$array_variable",
    "text": "$string_variable",
    "alpha": "$float_variable",

    // 你也可以使用变量引用另一个元素作为子元素
    "controls": [
      { "foobar@$string_variable2": {} }
    ]
  }
}
```

### 派生变量

你也可以从另一个元素派生变量，如下所示：

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
  "foobar": {
    ...
    "$cool_variable": 1,
    "$rad_variable": false
  },

  // 元素 "fizzbuzz" 扩展 "foobar"
  // 并将 `$cool_variable` 的值替换为 2
  // 而 `$rad_variable` 保持不变。
  "fizzbuzz@foobar": {
    "$cool_variable": 2
  }
}
```

对派生元素的任何属性在更改时将被完全覆盖。

## 绑定

绑定用于将硬编码值绑定到元素并用于处理元素。以下是一个使用硬编码文本的标签示例：

`text` 属性的值是 `#hardtext`。通过使用 `bindings`，我可以获取硬编码变量 `#hardtext` 的值，因此 `text` 属性可以使用它。
这里它直接将 `#hardtext` 的值赋给 `text` 属性。

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
    "label": {
        "type": "label",
        "text": "#hardtext",
        "bindings": [
            {
                "binding_name": "#hardtext"
            }
        ]
    }
}
```

或者，有时看起来如下所示：

<CodeHeader>vanilla/ui/example_file.json</CodeHeader>

```json
{
    "label": {
        "type": "label",
        "text": "#text",
        "bindings": [
            {
                "binding_name": "#hardtext",
                "binding_name_override": "#text"
            }
        ]
    }
}
```

在这种情况下，`#hardtext` 的值被赋给 `#text` 绑定属性名称，然后被赋给 `text` 属性。

这种情况在 `visible` 和 `enabled` 属性中经常发生。以下是两者的示例：

<CodeHeader></CodeHeader>

```json
{
    "send_button": {
        "bindings": [
            {
                "binding_name": "#using_touch",
                "binding_name_override": "#visible"
            }
        ]
    },

    "play_button": {
        "bindings": [
            {
                "binding_name": "#play_button_enabled",
                "binding_name_override": "#enabled"
            }
        ]
    }
}
```

在这种情况下，`#using_touch` 和 `#play_button_enabled` 存储布尔值。如果你在触摸设备上游玩，`#using_touch` 将为 `true`，否则为 `false`。`#play_button_enabled` 用于 `Add External Server` 屏幕。因此，在这种情况下，如果所有文本字段（`server name`、`server ip` 和 `server_port`）中都有文本，它将为 `true`。

所以 `#using_touch` 的值将覆盖 `#visible` 绑定属性的值，在这种情况下，这也是一个属性（`#visible` 用于 `property_bag`，这将与将 `visible` 设置为某个值相同）。
`#play_button_enabled` 将覆盖 `#enabled` 绑定属性的值，然后将其值设置为 `enabled` 属性。

假设你想在选择/勾选特定切换时显示一个带有内容的面板。你需要不同类型的绑定结构。
我们必须告诉源元素值将来自何处，告诉我们想要从源元素中获取哪个属性的值，以及我们想要覆盖其值的哪个属性。

<CodeHeader></CodeHeader>

```json
{
  "panel": {
    ...
    "bindings": [
      {
        "binding_type": "view",
        "source_control_name": "my_toggle", // 源元素的名称
        "source_property_name": "#toggle_state", // 我们需要这个属性值，告诉切换处于哪种状态
        "target_property_name": "#visible" // 覆盖的目标属性名称
      }
    ]
  },

  "my_toggle": {
    ...
  }
}
```

当切换被选中时，`#toggle_state` 将被检查（`1` 或 `true`），并将覆盖元素的 `visible` 属性值为 `true`。当你取消选中时，它将被取消选中（`0` 或 `false`），并再次覆盖 `visible` 值。

## 条件渲染

在使用标准属性使内容在屏幕上可见时，操控 Bedrock 当前的 UI 系统是有挑战的。然而，变量和绑定在 JSON UI 中是卓越的，因为它们包含直接来自 Bedrock 引擎的数据。使用一些巧妙的 UI 技术，可以完全控制 UI 控件渲染的条件。这些方法分为两类：使用变量的条件渲染和使用绑定的条件渲染。

### 使用变量的条件渲染

变量可用于有条件地渲染 UI 控件。回想一下，UI 变量是前面有 `$` 的属性。在 `hud_screen.json` 中携带引擎数据的一个变量示例是 `$actionbar_text`。查看 `hud_actionbar_text`，我们可以看到 `$actionbar_text` 用于显示动作栏文本。

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
...
  "hud_actionbar_text": {
    "type": "image",
    "size": [ "100%c + 12px", "100%c + 5px" ],
    "offset": [ 0, "50%-68px" ],
    "texture": "textures/ui/hud_tip_text_background",
    "alpha": "@hud.anim_actionbar_text_background_alpha_out",
    "controls": [
      {
        "actionbar_message": {
          "type": "label",
          "anchor_from": "center",
          "anchor_to": "center",
          "color": "$tool_tip_text",
          "layer": 1,
          "text": "$actionbar_text",
          "localize": false,
          "alpha": "@hud.anim_actionbar_text_alpha_out"
        }
      }
    ]
  }
...
}
```

在使用携带 Bedrock 引擎数据的变量时，`visible` 属性用于有条件地渲染 UI 控件。考虑以下示例。创建了 `$actionbar_text` 变量的副本，以允许我们修改和对其进行比较（无法直接对硬编码变量执行此操作）。副本变量 `$atext` 然后用于添加的 `visible` 属性，其含义是“如果动作栏文本不等于 `hello world`，则使文本标签可见”。

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
...
  "hud_actionbar_text": {
    "type": "image",
    "size": ["100%c + 12px", "100%c + 5px"],
    "offset": [0, "50%-68px"],
    "texture": "textures/ui/hud_tip_text_background",
    "alpha": "@hud.anim_actionbar_text_background_alpha_out",
    "controls": [
      {
        "actionbar_message": {
          "type": "label",
          "anchor_from": "center",
          "anchor_to": "center",
          "color": "$tool_tip_text",
          "layer": 1,
          "text": "$actionbar_text",
          "localize": false,
          "alpha": "@hud.anim_actionbar_text_alpha_out",
          // 如果动作栏文本等于 "hello world"，则忽略文本标签
          "$atext": "$actionbar_text",
          "visible": "(not ($atext = 'hello world'))"
        }
      }
    ]
  }
...
}
```

将上述 JSON 修改为资源包中使用的不显眼 UI 文件应与此相同：

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
    "hud_actionbar_text/actionbar_message": {
        "$atext": "$actionbar_text",
        "visible": "(not ($atext = 'hello world'))"
    }
}
```

当你启用资源包并登录到世界时，尝试执行 `/title @s actionbar hello world`。你应该注意到没有消息出现！运行任何其他动作栏标题将显示其他消息。如果你希望动作栏文本及其背景消失，还可以移除代码中的 `/actionbar_message`。背景包含在 `hud_actionbar_text` 中，使其不可见也会使其子元素（`actionbar_message`）不可见。

以下是使用变量的条件渲染的一个更复杂示例。在这种情况下，必须使用动作栏工厂。工厂是元素生成器，有些具有特定名称，如 `hud_actionbar_text_factory`，它们具有硬编码的属性。每当运行动作栏命令时，此工厂会生成/重置其 `control_id` 内的元素，并传递一些有用的变量，如 `$actionbar_text`、`$tool_tip_text` 等，这些数据只能通过工厂访问。

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
    "black_conditional_image": {
        "type": "image",
        "texture": "textures/ui/Black",
        "size": [16, 16],
        "layer": 10,
        "$atext": "$actionbar_text",
        "visible": "($atext = 'hello world')"
    },

    "black_conditional_image_factory": {
        "type": "panel",
        "factory": {
            "name": "hud_actionbar_text_factory",
            "control_ids": {
                "hud_actionbar_text": "black_conditional_image@hud.black_conditional_image"
            }
        }
    },

    "root_panel": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": {
                    "black_conditional_image_factory@hud.black_conditional_image_factory": {}
                }
            }
        ]
    }
}
```

上述示例在动作栏文本字符串等于 `hello world` 时在 HUD 屏幕上显示一个 16x16 的黑色方块。你还可以为你的图像应用动画，使其更加动态。使用变量的条件渲染不限于图像和标签。你可以在使用变量的条件渲染中使用任何对象类型。可以想象，将 UI 代码与动作栏文本配对允许对 JSON UI 进行高度操作（至少在 `hud_screen.json` 中）。`visible` 属性支持 UI 运算符，因此你有更多的控制。任何携带 Bedrock 引擎数据的变量所在的位置都允许使用变量进行条件渲染。

### 使用绑定的条件渲染

继上述使用动作栏的示例，你可能会逻辑上推断标题也使用变量。但事实并非如此。标题使用绑定来处理其数据，如下所示。

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
...
  "hud_title_text": {
    "type": "stack_panel",
    "orientation": "vertical",
    "offset": [ 0, -19 ],
    "layer": 1,
    "alpha": "@hud.anim_title_text_alpha_in",
    "propagate_alpha": true,
    "controls": [
      {
        "title_frame": {
          "type": "panel",
          "size": [ "100%", "100%cm" ],
          "controls": [
            {
              "title_background": {
                "type": "image",
                "size": [ "100%sm + 30px", "100%sm + 6px" ],
                "texture": "textures/ui/hud_tip_text_background",
                "alpha": "@hud.anim_title_background_alpha_in"
              }
            },
            {
              "title": {
                "type": "label",
                "anchor_from": "top_middle",
                "anchor_to": "top_middle",
                "color": "$title_command_text_color",
                "text": "#text",
                "layer": 1,
                "localize": false,
                "font_size": "extra_large",
                "variables": [
                  {
                    "requires": "(not $title_shadow)",
                    "$show_shadow": false
                  },
                  {
                    "requires": "$title_shadow",
                    "$show_shadow": true
                  }
                ],
                "shadow": "$show_shadow",
                "text_alignment": "center",
                "offset": [ 0, 6 ],
                "bindings": [
                  {
                    "binding_name": "#hud_title_text_string",
                    "binding_name_override": "#text",
                    "binding_type": "global"
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
...
}
```

你需要向文本添加另一个绑定对象以控制其可见性。回想一下，`#visible` 包含通过绑定直接控制的可见性。以下示例不会渲染标题字符串 `hello world`，但会渲染所有其他字符串。尝试在游戏中输入 `/title @s title hello world` 以查看效果。

<CodeHeader>vanilla/ui/hud_screen.json</CodeHeader>

```json
{
...
  "hud_title_text": {
    "type": "stack_panel",
    "orientation": "vertical",
    "offset": [ 0, -19 ],
    "layer": 1,
    "alpha": "@hud.anim_title_text_alpha_in",
    "propagate_alpha": true,
    "controls": [
      {
        "title_frame": {
          "type": "panel",
          "size": [ "100%", "100%cm" ],
          "controls": [
            {
              "title_background": {
                "type": "image",
                "size": [ "100%sm + 30px", "100%sm + 6px" ],
                "texture": "textures/ui/hud_tip_text_background",
                "alpha": "@hud.anim_title_background_alpha_in"
              }
            },
            {
              "title": {
                "type": "label",
                "anchor_from": "top_middle",
                "anchor_to": "top_middle",
                "color": "$title_command_text_color",
                "text": "#text",
                "layer": 1,
                "localize": false,
                "font_size": "extra_large",
                "variables": [
                  {
                    "requires": "(not $title_shadow)",
                    "$show_shadow": false
                  },
                  {
                    "requires": "$title_shadow",
                    "$show_shadow": true
                  }
                ],
                "shadow": "$show_shadow",
                "text_alignment": "center",
                "offset": [ 0, 6 ],
                "bindings": [
                  {
                    "binding_name": "#hud_title_text_string",
                    "binding_name_override": "#text",
                    "binding_type": "global"
                  },
                  {
                    "binding_type": "view", // 使其成为观察绑定
                    "source_property_name": "(not (#text = 'hello world'))", // 检测标题文本字符串是否不等于 "hello world"
                    "target_property_name": "#visible" // 根据 "source_property_name" 的真或假覆盖 #visible 属性
                  }
                ]
              }
            }
          ]
        }
      }
    ]
  }
...
}
```

将上述 JSON 修改为资源包中使用的不显眼 UI 文件应与此相同：

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>

```json
{
    "hud_title_text/title_frame/title": {
        "modifications": [
            {
                "array_name": "bindings",
                "operation": "insert_back",
                "value": {
                    "binding_type": "view",
                    "source_property_name": "(not (#text = 'hello world'))",
                    "target_property_name": "#visible"
                }
            }
        ]
    }
}
```

与之前一样，以下是使用绑定的条件渲染的一个更复杂示例。在这种情况下，只有当标题文本字符串等于 `hello world` 时，16x16 的黑色图像才会渲染。虽然在这种情况下你不需要使用标题工厂，但如果你打算使用 UI 动画，应该使用它。

<CodeHeader>RP/ui/hud_screen.json</CodeHeader>

```json
{
    "black_conditional_image": {
        "type": "image",
        "texture": "textures/ui/Black",
        "size": [16, 16],
        "layer": 10,
        "bindings": [
            {
                "binding_name": "#hud_title_text_string"
            },
            {
                "binding_type": "view",
                "source_property_name": "(#hud_title_text_string = 'hello world')",
                "target_property_name": "#visible"
            }
        ]
    },

    "black_conditional_image_factory": {
        "type": "panel",
        "factory": {
            "name": "hud_title_text_factory",
            "control_ids": {
                "hud_title_text": "black_conditional_image@hud.black_conditional_image"
            }
        }
    },

    "root_panel": {
        "modifications": [
            {
                "array_name": "controls",
                "operation": "insert_front",
                "value": {
                    "black_conditional_image_factory@hud.black_conditional_image_factory": {}
                }
            }
        ]
    }
}
```

## 字符串格式化

你可以通过使用 `%.#s` 格式获取字符串的特定部分，其中 `#` 是一个数字，通过将其乘以字符串。例如：

```json
{
    "label_element": {
        "type": "label",
        "text": "#text",
        "layer": 2,
        "bindings": [
            {
                "binding_type": "global",
                "binding_name": "#hud_title_text_string"
            },
            {
                "binding_type": "view",
                "source_property_name": "('%.3s' * #hud_title_text_string)",
                "target_property_name": "#text"
            }
        ]
    }
}
```

在上述示例中，我们获取了标题文本的前 3 个字符。所以如果标题文本是 `abcdefghi`，标签中将只有 `abc`。另一个示例是我们有一个变量：`"$var": "abcdefghijklmn"`，
`'%.5s' * $var` 将返回 `abcde`。
`$var - ('%.7s' * $var)` 将返回 `hijklm`。

记住，这种格式的使用是有限的。

## 按钮映射

`button_mappings` 允许你修改在输入某个控制时按下的按钮。此控制可以来自键盘和鼠标、触摸或控制器。

以下是带有 `button_mappings` 属性的按钮元素示例：

```json
{
    "sample_button@common.button": {
        "$pressed_button_name": "button_id",
        "button_mappings": [
            {
                "to_button_id": "$pressed_button_name",
                "mapping_type": "pressed"
            },
            {
                "from_button_id": "button.menu_ok",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "focused"
            },
            {
                "from_button_id": "button.menu_select",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "pressed"
            },
            {
                "from_button_id": "button.menu_up",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "global"
            }
        ]
    }
}
```

### 映射类型

定义指定按钮映射的范围：

-   `focused` - 意味着当按钮首先被悬停时
-   `pressed` - 意味着当按钮被点击或按下时
-   `global` - 意味着当按钮存在并在屏幕上被调用时

只要 `from_button_id` 使用其适当的 `mapping_type` 输入，它将满足条件并触发 `to_button_id` 属性：

```json
{
    "sample_button@common.button": {
        "$pressed_button_name": "button_id",
        "button_mappings": [
            // 仅在你首先将鼠标悬停在按钮上时触发此按钮
            {
                "from_button_id": "button.menu_ok",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "focused"
            },
            // 当按钮被点击或按下时触发此按钮
            {
                "from_button_id": "button.menu_select",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "pressed"
            },
            // 当 `button.menu_up` 键从任何地方被按下时触发此按钮
            {
                "from_button_id": "button.menu_up",
                "to_button_id": "$pressed_button_name",
                "mapping_type": "global"
            }
        ]
    }
}
```

### 常用按钮 ID

以下是你可以在 `from_button_id` 属性中使用的常用按钮 ID 列表。

**对于鼠标和键盘：**
| 按钮 ID                     | 描述              |
|-----------------------------|-------------------|
| `button.menu_select`        | 鼠标左键点击       |
| `button.menu_secondary_select` | 鼠标右键点击       |
| `button.menu_ok`            | ENTER键           |
| `button.menu_exit`          | ESC键             |
| `button.menu_cancel`        | ESC键             |
| `button.menu_up`            | 上箭头键          |
| `button.menu_down`          | 下箭头键          |
| `button.menu_left`          | 左箭头键          |
| `button.menu_right`         | 右箭头键          |
| `button.menu_autocomplete`  | TAB键             |

**对于控制器：**
| 按钮 ID                     | 描述              |
|-----------------------------|-------------------|
| `button.controller_select`  | X/A 按钮          |
| `button.menu_secondary_select` | Y 按钮             |
| `button.menu_exit`          | B 按钮             |
| `button.menu_cancel`        | B 按钮             |
| `button.menu_up`            | 上 DPAD 键         |
| `button.menu_down`          | 下 DPAD 键         |
| `button.menu_left`          | 左 DPAD 键         |
| `button.menu_right`         | 右 DPAD 键         |

在创建 UI 时，支持不同平台上具有不同控制方法的各种控制是良好实践。

## 修改

要以非侵入性的方式修改 JSON UI，你可以使用 `modifications` 属性来修改其他包（通常是原版 JSON UI 文件）中先前存在的 JSON UI 元素。这样做可以确保仅修改必要的部分，除非另有意图，以提高与修改 JSON UI 的其他包的兼容性。

| 修改类型         | 描述                                     |
|------------------|------------------------------------------|
| `insert_back`    | **插入**到数组末尾                       |
| `insert_front`   | **插入**到数组开头                       |
| `insert_after`   | **插入**到数组中目标之后                 |
| `insert_before`  | **插入**到数组中目标之前                 |
| `move_back`      | **移动**目标到数组末尾                   |
| `move_front`     | **移动**目标到数组开头                   |
| `move_after`     | **移动**目标到第二个目标之后             |
| `move_before`    | **移动**目标到第二个目标之前             |
| `swap`           | **交换**第一个目标与第二个目标的位置     |
| `replace`        | **替换**第一个目标为第二个目标            |
| `remove`         | **移除**目标                             |

### 示例

#### 前/后

修改列表顶部（开始）或底部（结束）的锚定。

从列表顶部前缀新 `foo` 控件：

```json
{
    "array_name": "controls",
    "operation": "insert_front",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将新 `foo` 控件追加到列表底部：

```json
{
    "array_name": "controls",
    "operation": "insert_back",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将现有 `foo` 控件移动到列表顶部：

```json
{
    "array_name": "controls",
    "operation": "move_front",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将现有 `foo` 控件移动到列表底部：

```json
{
    "array_name": "controls",
    "operation": "move_back",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将现有 `#example_binding_2` 绑定移动到列表顶部：

```json
{
    "array_name": "bindings",
    "operation": "move_front",
    "where": {
        "binding_name": "#example_binding_2"
    }
}
```

将现有 `#example_binding_2` 绑定移动到列表底部：

```json
{
    "array_name": "bindings",
    "operation": "move_back",
    "where": {
        "binding_name": "#example_binding_1"
    }
}
```

#### 后/前

修改列表中现有控件或绑定的下方（后）或上方（前）的锚定。

在列表中 `second_target` 控件下方添加新 `foo` 控件：

```json
{
    "control_name": "second_target",
    "operation": "insert_after",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

在列表中 `second_target` 控件上方添加新 `foo` 控件：

```json
{
    "control_name": "second_target",
    "operation": "insert_before",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

在列表中 `#example_binding_2` 绑定下方添加新 `#my_binding_1` 绑定：

```json
{
    "array_name": "bindings",
    "operation": "insert_after",
    "where": {
        "binding_name": "#example_binding_2"
    },
    "value": [
        {
            "binding_name": "#my_binding_1"
        }
    ]
}
```

在列表中 `#example_binding_2` 绑定上方添加新 `#my_binding_1` 绑定：

```json
{
    "array_name": "bindings",
    "operation": "insert_before",
    "where": {
        "binding_name": "#example_binding_2"
    },
    "value": [
        {
            "binding_name": "#my_binding_1"
        }
    ]
}
```

将现有 `foo` 控件移动到列表中 `second_target` 控件下方：

```json
{
    "control_name": "second_target",
    "operation": "move_after",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将现有 `foo` 控件移动到列表中 `second_target` 控件上方：

```json
{
    "control_name": "second_target",
    "operation": "move_before",
    "value": [
        {
            "foo@example.bar": {}
        }
    ]
}
```

将现有 `#example_binding_1` 绑定移动到列表中 `#example_binding_2` 绑定下方：

```json
{
    "array_name": "bindings",
    "operation": "move_after",
    "where": {
        "binding_name": "#example_binding_2"
    },
    "target": {
        "binding_name": "#example_binding_1"
    }
}
```

将现有 `#example_binding_1` 绑定移动到列表中 `#example_binding_2` 绑定上方：

```json
{
    "array_name": "bindings",
    "operation": "move_before",
    "where": {
        "binding_name": "#example_binding_1"
    },
    "target": {
        "binding_name": "#example_binding_2"
    }
}
```

#### 交换/替换/移除

修改至少一个现有控件或绑定的锚定：

交换现有 `#example_binding_1` 和 `#example_binding_2` 绑定的位置：

```json
{
    "array_name": "bindings",
    "operation": "swap",
    "where": {
        "binding_name": "#example_binding_1"
    },
    "target": {
        "binding_name": "#example_binding_2"
    }
}
```

将现有 `#example_binding_1` 绑定替换为新的 `#replacement_binding` 绑定：

```json
{
    "array_name": "bindings",
    "operation": "replace",
    "where": {
        "binding_name": "#example_binding_1"
    },
    "value": {
        "binding_name": "#replacement_binding"
    }
}
```

移除现有 `#example_binding_1` 绑定：

```json
{
    "array_name": "bindings",
    "operation": "remove",
    "where": {
        "binding_name": "#example_binding_1"
    }
}
```