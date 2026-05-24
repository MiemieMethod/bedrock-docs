# 维度定义

本页列出国际版行为包`dimensions/`目录中维度定义文件的可确认字段。内容来源于Microsoft Learn的DimensionReference自动导出资料。

/// warning | 适用范围与资料状态
本页仅记录国际版维度定义，不适用于中国版`netease_dimension`目录与模组SDK接口。自动导出存在根对象命名不一致问题，使用时应结合目标版本实测。
///

## 根对象

维度文件包含`format_version`和一个维度定义对象。自动导出资料同时出现了两种根对象形态。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 维度文件格式版本。自动导出资料建议使用`1.20.0`及以上。 |
| `minecraft:dimension` | 对象 | 未设置 | 自动导出中的一种维度定义根对象。 |
| `minecraft:dimension_type` | 对象 | 未设置 | 自动导出中的另一种维度定义根对象。 |

## 维度定义对象

`minecraft:dimension`与`minecraft:dimension_type`都记录为相同结构，均包含`description`和`components`。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 维度描述信息。 |
| `components` | 对象 | 未设置 | 维度组件集合。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 维度赋命名空间标识符，使用`namespace:name`格式。 |

### `components`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `minecraft:dimension_bounds` | 对象 | `{"max":0,"min":0}` | 维度垂直边界设置。 |
| `minecraft:generation` | 对象 | 未设置 | 维度生成器设置。 |

#### `minecraft:dimension_bounds`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数 | 未设置 | 维度最小Y边界。 |
| `max` | 整数 | 未设置 | 维度最大Y边界。 |

#### `minecraft:generation`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `generator_type` | 字符串 | 未设置 | 生成器类型。缺少官方完整可用取值列表。 |

## 自动导出命名差异

自动导出资料还出现了`minecraft:dimensiondocument`和`minecraft:dimension_document`词条。两者都描述“维度定义文档”概念，不代表可直接写入JSON文件的稳定根字段名。维护时应优先按目标版本可加载的根对象形态实测。