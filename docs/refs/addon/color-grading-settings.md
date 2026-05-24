# 色彩分级设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:color_grading_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:colorgraderconfig_colorgradingparameterssrc`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:color_grading_settings` | 对象 | 未设置 | 色彩分级设置对象。 |

## `minecraft:color_grading_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 色彩分级定义描述信息。 |
| `color_grading` | 对象 | 未设置 | 阴影、中间调、高光三段色彩分级参数。 |
| `tone_mapping` | 对象 | 未设置 | 色调映射设置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 色彩分级设置的赋命名空间标识符。 |

### `color_grading`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `shadows` | 对象 | 未设置 | 阴影区参数。 |
| `midtones` | 对象 | 未设置 | 中间调参数。 |
| `highlights` | 对象 | 未设置 | 高光区参数。 |

### 阴影、中间调、高光通用字段

`shadows`、`midtones`和`highlights`均可使用以下向量字段。每个字段可写为三通道数组，也可写为`x`、`y`、`z`对象。

| 字段 | 约束 |
| --- | --- |
| `saturation` | 最大值为`10`。 |
| `contrast` | 最大值为`4`。 |
| `gamma` | 最大值为`4`。 |
| `gain` | 最大值为`10`。 |
| `offset` | 取值范围为`-1`到`1`。 |

### `shadows`附加字段

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 未设置 | 是否启用阴影区单独参数。 |
| `shadowsMax` | 数值 | 未设置 | 阴影区上界，最大值为`1`。 |

### `highlights`附加字段

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 未设置 | 是否启用高光区单独参数。 |
| `highlightsMin` | 数值 | 未设置 | 高光区下界，取值范围为`1`到`20`。 |

### `tone_mapping`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `operator` | 字符串 | 未设置 | 色调映射算子枚举值。 |

## 相关参考

- [光照设置](lighting-settings.md)
- [大气散射设置](atmosphere-settings.md)