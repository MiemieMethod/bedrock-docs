# 阴影风格设置<!-- md:flag vanilla -->

本页列出国际版延迟渲染/Vibrant Visuals资源包中`minecraft:shadow_settings`文件结构。资料来源为Microsoft Learn在Deferred Rendering目录下的`minecraft:shadowstylizationconfig_shadowstylizationconfigsettings`页面。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 文件使用的格式版本。 |
| `minecraft:shadow_settings` | 对象 | 未设置 | 阴影风格设置对象。 |

## `minecraft:shadow_settings`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `shadow_style` | 字符串 | 未设置 | 阴影风格枚举值。 |
| `texel_size` | 整数 | 未设置 | 阴影纹素尺寸，取值范围为`1`到`1024`。 |

## 相关参考

- [光照设置](lighting-settings.md)
- [点光设置](point-light-settings.md)