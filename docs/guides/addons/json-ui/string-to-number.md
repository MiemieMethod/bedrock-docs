# 字符串转数值<!-- md:flag vanilla -->

JSON UI中的很多绑定值以字符串形式传入。若需要做范围比较或数值运算，通常要先把字符串转成数值。

## 字符串转数值

常见做法是让字符串参与数值运算，例如乘以`1`。

```json title="RP/ui/hud_screen.json"
{
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
        "source_property_name": "(#player_score_sidebar * 1)",
        "target_property_name": "#score"
      },
      {
        "binding_type": "view",
        "source_property_name": "((#score > 99) and (#score < 1000))",
        "target_property_name": "#visible"
      }
    ]
  }
}
```

## 数值转字符串

若目标属性需要字符串，可先拼接一个字符串前缀，再输出。

```json title="RP/ui/hud_screen.json"
{
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
}
```

## 注意事项

- 仅在确认输入确实含数字时再做转换。
- 若涉及小数，需在表达式中引入浮点运算路径。
- 先把中间值写到临时属性，便于内容日志排错。
