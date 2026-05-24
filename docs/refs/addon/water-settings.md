# 水体设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:water_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:waterconfig_waterconfigsettingsv1`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:water_settings` | 对象 | 未设置 | 水体设置对象。 |

## `minecraft:water_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 水体定义描述信息。 |
| `caustics` | 对象 | 未设置 | 焦散设置。 |
| `particle_concentrations` | 对象 | 未设置 | 水体粒子浓度设置。 |
| `waves` | 对象 | 未设置 | 水波设置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 水体设置的赋命名空间标识符。 |

### `caustics`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 未设置 | 是否启用焦散。 |
| `frame_length` | 数值 | 未设置 | 焦散帧时长，取值范围为`0.009999999776482582`到`5`。 |
| `power` | 整数 | 未设置 | 焦散强度，取值范围为`1`到`6`。 |
| `scale` | 数值 | 未设置 | 焦散缩放，取值范围为`0.10000000149011612`到`5`。 |
| `texture` | 字符串 | 未设置 | 焦散纹理标识。 |

### `particle_concentrations`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `cdom` | 数值 | 未设置 | 有色可溶性有机物浓度，最大值为`15`。 |
| `chlorophyll` | 数值 | 未设置 | 叶绿素浓度，最大值为`10`。 |
| `suspended_sediment` | 数值 | 未设置 | 悬浮沉积物浓度，最大值为`300`。 |

### `waves`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled` | 布尔值 | 未设置 | 是否启用水波。 |
| `depth` | 数值 | 未设置 | 波深，最大值为`3`。 |
| `direction_increment` | 数值 | 未设置 | 波向增量，最大值为`360`。 |
| `frequency` | 数值 | 未设置 | 波频率，取值范围为`0.009999999776482582`到`3`。 |
| `frequency_scaling` | 数值 | 未设置 | 波频率缩放，最大值为`2`。 |
| `mix` | 数值 | 未设置 | 波混合系数，最大值为`1`。 |
| `octaves` | 整数 | 未设置 | 波叠加层数，取值范围为`1`到`30`。 |
| `pull` | 数值 | 未设置 | 波拉伸系数，取值范围为`-1`到`1`。 |
| `sampleWidth` | 数值 | 未设置 | 采样宽度，取值范围为`0.009999999776482582`到`1`。 |
| `shape` | 数值 | 未设置 | 波形参数，取值范围为`1`到`10`。 |
| `speed` | 数值 | 未设置 | 波速度，取值范围为`0.009999999776482582`到`10`。 |
| `speed_scaling` | 数值 | 未设置 | 波速度缩放，最大值为`2`。 |

## 相关参考

- [大气散射设置](atmosphere-settings.md)
- [光照设置](lighting-settings.md)