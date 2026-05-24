# 按钮与开关<!-- md:flag vanilla -->

本页介绍如何在JSON UI中创建自定义按钮（`button`）和开关（`toggle`），以及如何利用它们控制界面元素的行为。

/// warning | 适用范围
本页内容基于国际版JSON UI。中国版模组SDK提供专有界面接口，无需以此方式创建按钮与开关。
///

## 使用原版模板

JSON UI的原版资源包提供了若干现成的按钮与开关模板，分别存放于`ui/ui_template_buttons.json`与`ui/ui_template_toggles.json`中，可直接通过继承语法（`元素名@命名空间.基控件名`）复用，无需从头构建控件树。

### 创建开关

引用`common_toggles.light_text_toggle`，即可快速创建带文字的开关控件。

```json title="RP/ui/your_file.json"
{
  "our_toggle@common_toggles.light_text_toggle": {
    "size": [64, 32],
    "$button_text": "Click me!",
    "$toggle_name": "wiki_toggle",
    "$toggle_view_binding_name": "wiki_toggle_state"
  }
}
```

- `$button_text`：开关上显示的文字。
- `$toggle_name`：开关的唯一标识名称，必填；仅在使用硬编码开关名时才真正生效。
- `$toggle_view_binding_name`：为该开关的状态指定一个控件名，其他控件可通过`source_control_name`读取该状态。

将上述控件加入某个屏幕的`root_panel`即可测试。

### 利用开关控制可见性

通过`view`类型绑定，可将开关状态（`#toggle_state`，布尔值）映射到另一控件的`#visible`属性，实现条件渲染。

```json title="RP/ui/your_file.json"
{
  "our_toggle@common_toggles.light_text_toggle": {
    "size": [64, 32],
    "$button_text": "Click me!",
    "$toggle_name": "wiki_toggle",
    "$toggle_view_binding_name": "wiki_toggle_state"
  },
  "our_image": {
    "type": "image",
    "texture": "textures/items/apple",
    "size": [16, 16],
    "offset": [0, 20],
    "bindings": [
      {
        "binding_type": "view",
        "source_control_name": "wiki_toggle_state",
        "source_property_name": "#toggle_state",
        "target_property_name": "#visible"
      }
    ]
  }
}
```

- `source_control_name`填写`$toggle_view_binding_name`中指定的控件名。
- `source_property_name`填写`#toggle_state`，它返回开关当前状态（选中为`1`/`true`，未选中为`0`/`false`）。

### 创建按钮

引用`common_buttons.light_text_button`，即可创建文字按钮。`$pressed_button_name`是必填字段，填入触发的全局按钮名或硬编码按钮名。

```json title="RP/ui/your_file.json"
{
  "our_button@common_buttons.light_text_button": {
    "size": [64, 32],
    "$button_text": "Click me!",
    "$pressed_button_name": "button.menu_exit"
  }
}
```

点击该按钮将触发`button.menu_exit`，效果等同于退出当前屏幕。

/// note | 按钮功能局限
按钮的实际功能主要依赖硬编码实现，只能触发已有的全局按钮ID或特定屏幕的专属动作。相比开关，按钮自身不保存状态，也不能直接通过纯资源包向游戏逻辑传递自定义数据。
///

## 进阶用法

### 带悬停文字的按钮

使用`common_buttons.light_content_button`可以创建内容按钮，其子控件区域由`$button_content`变量引用。在内容面板中放置`common.hover_text`控件，即可实现鼠标悬停时显示提示文字。

```json title="RP/ui/your_file.json"
{
  "our_button@common_buttons.light_content_button": {
    "size": [18, 18],
    "$button_content": "namespace.our_button_content_panel",
    "$pressed_button_name": "button.menu_exit"
  },
  "our_button_content_panel": {
    "type": "panel",
    "controls": [
      {
        "our_image": {
          "type": "image",
          "texture": "textures/items/apple",
          "size": [16, 16]
        }
      },
      {
        "our_hover_text@common.hover_text": {
          "ignored": "$default_state",
          "property_bag": {
            "#hover_text": "悬停提示文字"
          }
        }
      }
    ]
  }
}
```

`"ignored": "$default_state"`确保提示文字仅在按钮被悬停时出现，默认状态下隐藏。悬停文字不支持本地化键，若需要多语言提示，需自行构建自定义悬停文字控件。

### 点击按钮播放动画

将按钮的`$pressed_button_name`值用作动画元素的`play_event`属性，即可在点击按钮时触发对应的UI动画。

```json title="RP/ui/your_file.json"
{
  "example_animation": {
    "anim_type": "offset",
    "easing": "linear",
    "duration": 2,
    "from": [0, 0],
    "to": [-50, 0],
    "play_event": "button.example_button_id"
  },
  "example_button@common_buttons.light_text_button": {
    "$pressed_button_name": "button.example_button_id",
    "$button_text": "播放动画",
    "size": [80, 20]
  },
  "example_label": {
    "type": "label",
    "text": "示例文字",
    "anims": ["@namespace.example_animation"],
    "anchor_from": "top_right",
    "anchor_to": "top_right"
  }
}
```

动画定义中的`play_event`与按钮的`$pressed_button_name`保持一致，即可在点击时触发该动画。

## 相关参考

- [JSON UI](../../../docs/general/json-ui.md)
- [JSON UI文件参考](../../../refs/addon/json-ui.md)