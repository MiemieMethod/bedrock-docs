# JSON UI最佳实践<!-- md:flag vanilla -->

本页汇总JSON UI改造中的高频经验，目标是两件事：减少版本更新后的界面崩溃，以及降低界面运行开销。实际排错时，先看内容日志，再看控件树。

## 兼容性优先

### 只改必要字段

若仅需改一个属性，只覆写该属性，不复制整份原版文件。复制整份文件会放大后续版本冲突面。

```json title="RP/ui/hud_screen.json"
{
  "progress_text_label": {
    "shadow": false
  }
}
```

### 优先使用`modifications`

向数组追加控件、绑定或按钮映射时，优先使用`modifications`，而不是重写整个数组。

```json title="RP/ui/hud_screen.json"
{
  "root_panel": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_front",
        "value": [
          { "custom_panel@my_ui.custom_panel": {} }
        ]
      }
    ]
  }
}
```

### 使用单一入口点

向某个屏幕添加自定义界面时，需要在原版界面中选一处作为"合并入口"。优先将所有自定义控件集中到同一个入口，而不是分散挂载在多个原版控件上。入口越少，受原版更新影响的风险点越少，也更容易排错。

```json title="RP/ui/hud_screen.json"
{
  "root_panel": {
    "modifications": [
      {
        "array_name": "controls",
        "operation": "insert_front",
        "value": [
          { "custom_ui_control_1@namespace_1.custom_ui_control_1": {} },
          { "custom_ui_control_2@namespace_1.custom_ui_control_2": {} }
        ]
      }
    ]
  }
}
```

### 避免在原版命名空间中工作

若需要添加大量自定义控件，应将它们放入具有独立命名空间的新文件，通过`_ui_defs.json`注册，再在入口处以`元素名@命名空间.元素名`形式引用。这样可以避免与原版控件名冲突，也便于迁移和拆分。命名空间支持前缀，例如`wiki:namespace`，可进一步降低冲突概率。

### 避免深层硬覆写

深层控件结构更易受原版改动影响。若必须改深层字段，优先使用路径覆写和最小改动：

```json
{
  "panel_with_label/bg_image": {
    "size": ["100%c", "100%c"]
  }
}
```

### 使用自定义命名空间

不要把自定义控件直接放进原版命名空间。统一使用项目命名空间可显著减少命名冲突。

## 性能优化

### 减少无效表达式

表达式越复杂，评估成本越高。可合并的运算尽量合并，重复表达式尽量提取为变量或复用绑定。

### 精简绑定

每条绑定都带来评估成本。应定期清理未使用绑定，避免多个绑定重复计算同一值。

### 减少控件数量

大量静态重复控件可合并为模板+变量或集合驱动控件。对完全不用的控件，优先考虑`"ignored": true`而非`"visible": false`；前者会使控件及其所有子控件被完全跳过求值，后者仍会继续评估控件树。

利用变量与绑定可以大幅减少重复控件的数量。以下示例将5个分别控制可见性的图片控件合并为1个：

/// tab | 未优化
```json
{
  "image_template": {
    "type": "image",
    "texture": "$texture",
    "bindings": [
      { "binding_name": "#hud_title_text_string" },
      {
        "binding_type": "view",
        "source_property_name": "(#hud_title_text_string = $binding_text)",
        "target_property_name": "#visible"
      }
    ]
  },
  "image_1@image_template": { "$texture": "textures/wiki/ui/example_1", "$binding_text": "1" },
  "image_2@image_template": { "$texture": "textures/wiki/ui/example_2", "$binding_text": "2" },
  "image_3@image_template": { "$texture": "textures/wiki/ui/example_3", "$binding_text": "3" },
  "image_4@image_template": { "$texture": "textures/wiki/ui/example_4", "$binding_text": "4" },
  "image_5@image_template": { "$texture": "textures/wiki/ui/example_5", "$binding_text": "5" }
}
```
///

/// tab | 优化后
```json
{
  "image": {
    "type": "image",
    "texture": "#texture",
    "bindings": [
      { "binding_name": "#hud_title_text_string" },
      {
        "binding_type": "view",
        "source_property_name": "(((#hud_title_text_string * 1) > 0) and ((#hud_title_text_string * 1) < 6))",
        "target_property_name": "#visible"
      },
      {
        "binding_type": "view",
        "source_property_name": "('textures/wiki/ui/example_' + #hud_title_text_string)",
        "target_property_name": "#texture"
      }
    ]
  }
}
```
///

## 维护建议

1. 每次升级目标版本后，先检查`hud_screen.json`和常改界面。
2. 先用内容日志定位报错，再做结构修复。
3. 保留“最小可回滚”改动，避免一次性重写大量控件树。