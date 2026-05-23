# 大气散射设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:atmosphere_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:atmosphericscattering_atmosphericscatteringconfigsettings`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:atmosphere_settings` | 对象 | 未设置 | 大气散射设置对象。 |

## `minecraft:atmosphere_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 大气散射定义描述信息。 |
| `horizon_blend_stops` | 对象 | 未设置 | 地平线混合区间参数。 |
| `moon_mie_strength` | 数值或关键帧对象 | 未设置 | 月光米氏散射强度，单值模式最大为`20`。 |
| `rayleigh_strength` | 数值或关键帧对象 | 未设置 | 瑞利散射强度，单值模式最大为`11`。 |
| `sky_horizon_color` | 字符串、关键帧字符串对象或对象集 | 未设置 | 天空地平线颜色。 |
| `sky_zenith_color` | 字符串、关键帧字符串对象或对象集 | 未设置 | 天空天顶颜色。 |
| `sun_glare_shape` | 数值或关键帧对象 | 未设置 | 太阳眩光形状参数，单值模式最大为`50`。 |
| `sun_mie_strength` | 数值或关键帧对象 | 未设置 | 太阳米氏散射强度，单值模式最大为`60`。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 大气散射设置的赋命名空间标识符。 |

### `horizon_blend_stops`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 数值或关键帧对象 | 未设置 | 地平线混合最小位置，单值模式最大为`1`。 |
| `start` | 数值或关键帧对象 | 未设置 | 地平线混合起始位置，单值模式最大为`1`。 |
| `max` | 数值或关键帧对象 | 未设置 | 地平线混合最大位置，单值模式最大为`1`。 |
| `mie_start` | 数值或关键帧对象 | 未设置 | 米氏散射起始位置，单值模式最大为`1.2000000476837158`。 |

## 相关参考

- [光照设置](lighting-settings.md)
- [色彩分级设置](color-grading-settings.md)
- [水体设置](water-settings.md)
