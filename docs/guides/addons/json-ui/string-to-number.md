# 字符串转数值<!-- md:flag vanilla -->

JSON UI中的很多绑定值以字符串形式传入。若需要做范围比较或数值运算，通常要先把字符串转成数值。

## 字符串转数值

常见做法是让字符串参与数值运算，例如乘以`1`。这样可以把侧栏分数、标题文本中的数字片段或其他字符串数值转回可比较的数值。

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
- 若需要浮点数而非整数，不能直接在表达式中写浮点字面量（如`1.0`），需通过变量或绑定引入浮点值。例如：

```json
{
  "binding_type": "view",
  "source_property_name": "($float_one * #player_score_sidebar)",
  "target_property_name": "#score_float"
}
```

其中`$float_one`应在控件上定义为`"$float_one": 1.0`，这样运算结果才会是浮点数。

- 先把中间值写到临时属性，便于内容日志排错。