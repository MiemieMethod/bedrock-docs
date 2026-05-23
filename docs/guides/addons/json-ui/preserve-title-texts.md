# 通过Title保留并更新HUD文本<!-- md:flag vanilla -->

本技巧用于“只在Title包含特定标记时更新界面文本”。适合做低频状态推送，避免每条标题都触发UI刷新。

## 思路

1. 读取`#hud_title_text_string`。
2. 仅在文本含指定标记时把值保存到临时属性。
3. 显示层再读取该临时属性并移除标记字符。

## 示例

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
          "bindings": [
            { "binding_name": "#hud_title_text_string" },
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

## 说明

- `visibility_changed`可用于在可见状态切换时“锁存”文本。
- 该方案同样适用于副标题、动作栏或其他可绑定文本源。
- 字符串匹配对大小写和拼写敏感，建议统一约定标记格式。
