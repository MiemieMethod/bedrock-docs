# 下拉菜单设置架构参考

本文档对应Microsoft Learn的`minecraft:dropdownsetting`结构。

## 字段

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `default` | *未设置* | 字符串 | 默认选项名。 |
| `name` | *未设置* | 字符串 | 设置标识符。 |
| `options` | *未设置* | [下拉菜单选项](#下拉菜单选项字段)项 | 选项集合。 |
| `text` | *未设置* | 字符串 | 显示文本。 |
| `type` | *未设置* | [类型可选值](#类型可选值) | 类型字段。 |

## 下拉菜单选项字段

`options`中的单项结构对应`minecraft:dropdownoption`：

| 字段 | 默认值 | 类型 | 说明 |
|------|--------|------|------|
| `name` | *未设置* | 字符串 | 选项标识符。 |
| `text` | *未设置* | 字符串 | 选项显示文本。 |

## 类型可选值

| 值 |
|----|
| `dropdown` |
| `label` |
| `slider` |
| `toggle` |

## 相关页面

- [下拉菜单选项](world-setting-dropdown-option.md)
- [世界设置](world-setting.md)
