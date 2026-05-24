# 向HUD添加元素<!-- md:flag vanilla -->

本页演示如何把自定义控件安全插入HUD，而不是直接覆盖整份`hud_screen.json`。

## 基本思路

HUD根容器通常是`root_panel`。向HUD新增元素时，推荐在`root_panel.modifications`里对`controls`数组做插入，而不是直接改写整份界面。

## 方式一：直接插入多个控件

```json title="RP/ui/hud_screen.json"
{
  "hud_square": {
    "type": "image",
    "texture": "textures/ui/Black",
    "anchor_from": "top_middle",
    "anchor_to": "top_middle",
    "size": [64, 64],
    "offset": [0, 4]
  },
  "hud_text": {
    "type": "label",
    "text": "HUD文本",
    "anchor_from": "top_right",
    "anchor_to": "top_right",
    "offset": [-4, 4]
  },
  "root_panel": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_front",
        "value": [
          { "hud_square@hud.hud_square": {} },
          { "hud_text@hud.hud_text": {} }
        ]
      }
    ]
  }
}
```

## 方式二：先组面板再插入

当元素较多时，建议先放进一个面板，再插入该面板，便于后续维护。

```json title="RP/ui/hud_screen.json"
{
  "hud_elements_panel": {
    "type": "panel",
    "controls": [
      { "hud_square@hud.hud_square": {} },
      { "hud_text@hud.hud_text": {} }
    ]
  },
  "root_panel": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_front",
        "value": [
          { "hud_elements_panel@hud.hud_elements_panel": {} }
        ]
      }
    ]
  }
}
```

## 注意事项

- 自定义控件建议统一使用项目命名空间。
- 插入顺序会影响渲染层级和输入命中。
- 若插入后无显示，优先检查`_ui_defs.json`是否已加载该文件。