# 通过Title保留并更新HUD文本<!-- md:flag vanilla -->

本页介绍如何构建一个可复用的UI组件，使其"监听"标题文本，只在标题包含特定标记时更新界面显示内容。这种方式适合通过`/title`命令向界面推送低频状态数据，避免每条标题都触发界面重算。

## 设计思路

组件由两部分构成：

1. 可见的`label`（`preserved_title_display`）：负责显示文字。
2. 隐藏的子`panel`（`data_control`）：负责检测标记、保存文本，是整个组件的逻辑核心。

关键技术点：使用`property_bag`在`data_control`中创建一个**局部变量**`#preserved_text`。由于它不是全局变量，每个组件实例都拥有独立的`#preserved_text`，互不干扰，从而实现真正的模块化复用。

## 实现代码

```json title="RP/ui/hud_screen.json"
{
  "preserved_title_display": {
    "$update_string": "update",
    "type": "label",
    "text": "#text",
    "controls": [
      {
        "data_control": {
          "type": "panel",
          "size": [0, 0],
          "property_bag": {
            "#preserved_text": ""
          },
          "bindings": [
            {
              "binding_name": "#hud_title_text_string"
            },
            {
              "binding_name": "#hud_title_text_string",
              "binding_name_override": "#preserved_text",
              "binding_condition": "visibility_changed"
            },
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
        "source_control_name": "data_control",
        "source_property_name": "(#preserved_text - $update_string)",
        "target_property_name": "#text"
      }
    ]
  }
}
```

## 原理说明

### `data_control`的逻辑

`data_control`是一个尺寸为`[0, 0]`的不可见面板，负责检测标记并保存文本：

1. **`property_bag`**：在面板上创建并初始化局部变量`#preserved_text`为空字符串。因为是局部变量，每个`preserved_title_display`实例都有自己独立的`#preserved_text`，不同实例之间完全隔离。

2. **`visibility_changed`绑定**：当`data_control`的可见状态切换时，此绑定立即将当前的`#hud_title_text_string`复制到`#preserved_text`中，完成"锁存"操作。

3. **可见性条件**：第三条绑定决定`data_control`何时"闪烁"（在单帧内变为可见），触发上述锁存操作。两个条件同时满足时才会触发：
   - `not (#hud_title_text_string = #preserved_text)`：新到的标题与已保存的不同（防止同一标题重复触发）。
   - `not ((#hud_title_text_string - $update_string) = #hud_title_text_string)`：新标题中包含更新标记`$update_string`。

当含标记的新标题到来时，面板变为可见、`visibility_changed`触发锁存、可见性条件立即变为`false`——面板在单帧内完成一次"闪烁"，后续标题不再触发，除非又有新的含标记标题到来。

### `preserved_title_display`标签的绑定

外层标签从子控件`data_control`读取数据：

- `source_control_name: "data_control"`：指向子控件。
- `source_property_name: "(#preserved_text - $update_string)"`：取出保存的文本，并去除标记字符串，得到干净的显示内容。

## 使用方法

1. 将`$update_string`设置为自己约定的标记前缀（默认为`"update"`）。
2. 通过`/title @s title update:你的内容`命令推送数据；标记与内容的格式由`$update_string`决定。
3. 同一屏幕中可以多次使用该组件，每个实例互不干扰。
4. 本组件同样适用于副标题（`#hud_subtitle_text_string`）或其他可绑定文本源，只需替换`binding_name`中的绑定名即可。

/// note | 关于字符串匹配
字符串匹配对大小写和拼写敏感，建议在项目内统一约定标记格式，例如`"wiki:"`作为前缀，避免与其他资源包冲突。
///