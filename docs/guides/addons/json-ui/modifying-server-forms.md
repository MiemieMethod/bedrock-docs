# 修改服务器表单<!-- md:flag vanilla -->

本页介绍如何使用JSON UI的`factory`机制为`server_form.json`中的动作表单（Action Form）和模态表单（Modal Form）添加自定义界面，同时保持与原版表单的兼容性。

/// warning | 适用范围
本页内容基于国际版JSON UI。中国版模组SDK提供了专有的服务器表单接口。
///

## 原理概述

`server_form.json`使用一种叫做**工厂（Factory）**的机制来生成表单界面：当服务端向客户端发送特定类型的表单数据时，名为`server_form_factory`的工厂会根据数据类型，将对应的`control_ids`中的控件渲染到屏幕上。其中：

- `long_form`对应动作表单
- `custom_form`对应模态表单

通过向`main_screen_content`的`controls`数组插入一个新的工厂面板，并在`control_ids`中引用自定义控件，就可以在不破坏原版表单的前提下叠加自定义界面。

## 修改动作表单

### 第一步：插入自定义工厂

向`main_screen_content`的`controls`数组末尾插入一个新的工厂面板，引用自定义的`long_form`控件。注意：工厂面板的名称不能与原版的`server_form_factory`相同。

```json title="RP/ui/server_form.json"
{
  "main_screen_content": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_back",
        "value": [
          {
            "wiki_server_form_factory": {
              "type": "panel",
              "factory": {
                "name": "server_form_factory",
                "control_ids": {
                  "long_form": "@server_form.our_long_form_panel"
                }
              }
            }
          }
        ]
      }
    ]
  }
}
```

建议只插入一个工厂，将所有自定义表单逻辑集中到`our_long_form_panel`中统一管理，以减少维护成本。

### 第二步：定义自定义表单面板

通过`#title_text`绑定获取表单标题，再利用绑定表达式判断标题是否包含特定前缀，从而控制各自定义表单内容的显隐。

```json title="RP/ui/server_form.json"
{
  "our_long_form_panel": {
    "type": "panel",
    "bindings": [
      {
        "binding_name": "#title_text"
      }
    ],
    "controls": [
      {
        "our_custom_made_long_form": {
          "type": "image",
          "texture": "textures/items/apple",
          "size": [32, 32],
          "$title_needs_to_contain": "wiki_form:",
          "bindings": [
            {
              "binding_type": "view",
              "source_control_name": "our_long_form_panel",
              "source_property_name": "(not ((#title_text - $title_needs_to_contain) = #title_text))",
              "target_property_name": "#visible"
            }
          ]
        }
      }
    ]
  }
}
```

在`source_property_name`中，表达式`((#title_text - $title_needs_to_contain) = #title_text)`的含义是：从`#title_text`中减去前缀字符串后，若结果与原始文本相同，说明原始文本中不含该前缀。取反后，"当标题含前缀时显示"的逻辑即可成立。

### 第三步：避免与原版表单重叠

如果此时测试，会发现自定义内容与原版表单同时显示。需要向原版的`long_form`控件添加额外绑定，使其在自定义表单显示时隐藏自身。

```json title="RP/ui/server_form.json"
{
  "long_form": {
    "modifications": [
      {
        "array_name": "bindings",
        "operation": "insert_back",
        "value": [
          {
            "binding_name": "#title_text"
          },
          {
            "binding_type": "view",
            "source_property_name": "((#title_text - 'wiki_form:') = #title_text)",
            "target_property_name": "#visible"
          }
        ]
      }
    ]
  }
}
```

表达式`((#title_text - 'wiki_form:') = #title_text)`在标题不含`wiki_form:`前缀时为`true`，即原版表单只在标题不带自定义前缀时可见。

/// tip | 支持多个自定义前缀
可以串联多个减法判断，例如：
```json
"source_property_name": "((#title_text - 'form_1' - 'form_2' - 'form_3') = #title_text)"
```
这样三种前缀都会触发隐藏原版表单。
///

## 修改模态表单

模态表单（在`server_form.json`内部称为`custom_form`）的修改方式与动作表单相同，只需额外在`control_ids`中添加`custom_form`映射，并同样对原版的`custom_form`控件添加隐藏绑定。

### 插入工厂

```json title="RP/ui/server_form.json"
{
  "main_screen_content": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_back",
        "value": [
          {
            "wiki_server_form_factory": {
              "type": "panel",
              "factory": {
                "name": "server_form_factory",
                "control_ids": {
                  "long_form": "@server_form.our_long_form_panel",
                  "custom_form": "@server_form.our_custom_form_panel"
                }
              }
            }
          }
        ]
      }
    ]
  }
}
```

### 定义模态表单面板

```json title="RP/ui/server_form.json"
{
  "our_custom_form_panel": {
    "type": "panel",
    "bindings": [
      {
        "binding_name": "#title_text"
      }
    ],
    "controls": [
      {
        "our_custom_made_custom_form": {
          "type": "image",
          "texture": "textures/items/apple",
          "size": [32, 32],
          "$title_needs_to_contain": "wiki_form:",
          "bindings": [
            {
              "binding_type": "view",
              "source_control_name": "our_custom_form_panel",
              "source_property_name": "(not ((#title_text - $title_needs_to_contain) = #title_text))",
              "target_property_name": "#visible"
            }
          ]
        }
      }
    ]
  }
}
```

### 隐藏原版模态表单

```json title="RP/ui/server_form.json"
{
  "custom_form": {
    "modifications": [
      {
        "array_name": "bindings",
        "operation": "insert_back",
        "value": [
          {
            "binding_name": "#title_text"
          },
          {
            "binding_type": "view",
            "source_property_name": "((#title_text - 'wiki_form:') = #title_text)",
            "target_property_name": "#visible"
          }
        ]
      }
    ]
  }
}
```

## 注意事项

- 工厂面板名称不能与`server_form_factory`相同，且同级工厂面板名称也不能互相重复。
- 建议每种表单类型只插入一个工厂，将所有自定义表单逻辑集中在一个主面板中。
- 标题前缀约定建议在项目内统一规范，避免不同包之间的命名冲突。
- 上述示例以图片展示效果为例，实际使用时可将`our_custom_made_long_form`替换为任意自定义控件面板。

## 相关参考

- [JSON UI](../../../docs/general/json-ui.md)
- [JSON UI文件参考](../../../refs/addon/json-ui.md)
- [向HUD添加元素](add-hud-elements.md)