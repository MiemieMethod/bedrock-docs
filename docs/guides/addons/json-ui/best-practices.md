# JSON UI最佳实践<!-- md:flag vanilla -->

本页汇总JSON UI改造中的高频经验，目标是两件事：减少版本更新后的界面崩溃，以及降低界面运行开销。

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

大量静态重复控件可合并为模板+变量或集合驱动控件。对完全不用的控件，优先考虑`"ignored": true`。

## 维护建议

1. 每次升级目标版本后，先检查`hud_screen.json`和常改界面。
2. 先用内容日志定位报错，再做结构修复。
3. 保留“最小可回滚”改动，避免一次性重写大量控件树。
