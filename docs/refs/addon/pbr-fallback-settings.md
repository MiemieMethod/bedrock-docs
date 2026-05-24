# PBR回退设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:pbr_fallback_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:pbrfallbackconfig_pbrfallbackconfigsettings`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:pbr_fallback_settings` | 对象 | 未设置 | PBR回退设置对象。 |

## `minecraft:pbr_fallback_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `actors` | 对象 | 未设置 | 活动对象类别回退参数。 |
| `blocks` | 对象 | 未设置 | 方块类别回退参数。 |
| `items` | 对象 | 未设置 | 物品类别回退参数。 |
| `particles` | 对象 | 未设置 | 粒子类别回退参数。 |

`actors`、`blocks`、`items`和`particles`使用相同结构。

### 类别回退参数

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `global_metalness_emissive_roughness` | 字符串或数组 | 未设置 | MER统一值。 |
| `global_metalness_emissive_roughness_subsurface` | 字符串或数组 | 未设置 | MERS统一值。 |

## 通道约定

- `global_metalness_emissive_roughness`对应红色通道金属度、绿色通道自发光、蓝色通道粗糙度。
- `global_metalness_emissive_roughness_subsurface`在前三个通道基础上，额外使用Alpha通道表示次表面散射。

## 相关参考

- [纹理集](texture-set.md)
- [光照设置](lighting-settings.md)