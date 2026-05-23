# 光照设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:lighting_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:lightinggroup_lightingimpl_1_21_70`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:lighting_settings` | 对象 | 未设置 | 光照设置对象。 |

## `minecraft:lighting_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 光照定义描述信息。 |
| `ambient` | 对象 | 未设置 | 环境光设置。 |
| `directional_lights` | 对象 | 未设置 | 定向光设置，包含太阳和月亮。 |
| `emissive` | 对象 | 未设置 | 自发光去饱和设置。 |
| `sky` | 对象 | 未设置 | 天空强度设置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 光照设置的赋命名空间标识符。 |

### `ambient`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 字符串或数组 | 未设置 | 环境光颜色。 |
| `illuminance` | 数值 | 未设置 | 环境光照度，最大值为`5`。 |

### `directional_lights`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `sun` | 对象 | 未设置 | 太阳光设置。结构与`moon`相同。 |
| `moon` | 对象 | 未设置 | 月光设置。 |
| `orbital_offset_degrees` | 数值或关键帧对象 | 未设置 | 太阳月亮轨道偏移角度，单值模式最大为`359.989990234375`。 |

### `sun`与`moon`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 字符串、关键帧字符串对象或对象集 | 未设置 | 定向光颜色。 |
| `illuminance` | 数值或关键帧对象 | 未设置 | 定向光照度，单值模式最大为`110000`。 |

### `emissive`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `desaturation` | 数值 | 未设置 | 自发光去饱和强度，最大值为`1`。 |

### `sky`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `intensity` | 数值 | 未设置 | 天空光强度，取值范围为`0.1`到`1`。 |

## 相关参考

- [纹理集](texture-set.md)
- [PBR回退设置](pbr-fallback-settings.md)
- [大气散射设置](atmosphere-settings.md)
