# 世界设置架构参考

本文档汇总ManifestReference中的世界设置结构。世界设置项通过清单的`settings`字段声明。

## 设置结构一览

| 结构 | 说明 | 详情页 |
|------|------|--------|
| `minecraft:togglesetting` | 布尔切换项。 | [切换设置](world-setting-toggle.md) |
| `minecraft:slidersetting` | 数值滑块项。 | [滑块设置](world-setting-slider.md) |
| `minecraft:dropdownsetting` | 下拉菜单项。 | [下拉菜单设置](world-setting-dropdown.md) |
| `minecraft:labelsetting` | 只读标签项。 | [标签设置](world-setting-label.md) |
| `minecraft:dropdownoption` | 下拉选项子结构。 | [下拉菜单选项](world-setting-dropdown-option.md) |

## 类型取值集合

ManifestReference在设置结构中统一给出`type`可选值：

| 值 |
|----|
| `dropdown` |
| `label` |
| `slider` |
| `toggle` |

## 相关页面

- [清单文件架构](manifest-schema.md)