# 客户端生物群系定义

本页列出资源包客户端生物群系文件的主要字段。客户端生物群系文件用于定义生物群系的天空、水体、迷雾、环境声音和音乐等客户端表现，不参与服务端世界生成与生物生成逻辑。

/// warning | 适用范围
本页记录的是资源包中的客户端生物群系定义。行为包中的服务端生物群系定义请见[生物群系定义](biome.md)。
///

## 文件位置与兼容性

- 当前推荐将客户端生物群系按文件拆分，放在资源包`biomes/`目录中。
- `biomes_client.json`仍可被自定义内容加载，可用于兼容既有内容。
- 自基础游戏版本`1.21.40`起，原版内置资源包不再依赖`biomes_client.json`承载原版生物群系客户端数据。

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 客户端生物群系文件使用的格式版本。 |
| `minecraft:client_biome` | 对象 | 未设置 | 单个客户端生物群系定义。 |

## `minecraft:client_biome`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 客户端生物群系的非组件设置。 |
| `components` | 对象 | 未设置 | 客户端生物群系使用的组件集合。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 客户端生物群系的赋命名空间标识符。应与游戏或行为包中已存在的生物群系同名，可被`/locate biome`等功能引用。值必须匹配`^[a-z0-9._%+-]+:[a-z0-9._%+-]+$`。 |

### `components`

| 组件 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `minecraft:ambient_sounds` | 对象 | 未设置 | 定义环境声音。 |
| `minecraft:biome_music` | 对象 | 未设置 | 定义生物群系音乐与音量系数。 |
| `minecraft:fog_appearance` | 对象 | 未设置 | 定义使用的迷雾标识符。 |
| `minecraft:foliage_appearance` | 对象 | 未设置 | 定义树叶渲染颜色或色图。 |
| `minecraft:grass_appearance` | 对象 | 未设置 | 定义草渲染颜色或色图。 |
| `minecraft:sky_color` | 对象 | 未设置 | 定义天空颜色。 |
| `minecraft:water_appearance` | 对象 | 未设置 | 定义水面颜色与透明度。 |
| `minecraft:dry_foliage_color` | 对象 | 未设置 | 定义干枯树叶颜色。 |
| `minecraft:precipitation` | 对象 | 未设置 | 定义灰烬、孢子等降水粒子的视觉密度。 |
| `minecraft:atmosphere_identifier` | 对象 | 未设置 | 定义鲜艳视觉大气散射配置标识符。 |
| `minecraft:color_grading_identifier` | 对象 | 未设置 | 定义鲜艳视觉色彩分级配置标识符。 |
| `minecraft:lighting_identifier` | 对象 | 未设置 | 定义鲜艳视觉光照配置标识符。 |
| `minecraft:water_identifier` | 对象 | 未设置 | 定义鲜艳视觉水体配置标识符。 |
| `minecraft:cubemap_identifier` | 对象 | 未设置 | 定义鲜艳视觉天空盒配置标识符。 |

### `minecraft:ambient_sounds`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `addition` | 对象 | 未设置 | 偶发播放的命名声音。 |
| `loop` | 对象 | 未设置 | 玩家位于该生物群系时循环播放的命名声音。 |
| `mood` | 对象 | 未设置 | 低亮度空气方块附近低频播放的命名声音；未设置时使用`ambient.cave`。 |

`addition`对象可包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `asset` | 字符串 | 未设置 | 要播放的声音资源名。 |
| `chance` | 数值 | 未设置 | 每次检测间隔触发播放的概率，范围为`0.0`到`1.0`。 |

/// note | 字段完备性说明
Microsoft Learn该目录未单独给出`loop`和`mood`的子字段表。本页仅记录该目录明确给出的字段与行为说明。
///

### `minecraft:biome_music`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `music_definition` | 对象 | 未设置 | 进入该生物群系后使用的音乐定义。缺失或找不到时按维度默认音乐处理；空字符串表示不播放音乐。 |
| `volume_multiplier` | 数值 | 未设置 | 进入该生物群系后渐变应用的音乐音量乘数，范围为`0`到`1`。 |

### `minecraft:fog_appearance`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `fog_identifier` | 对象 | 未设置 | 迷雾定义标识符。引用目标见[迷雾定义](fog-settings.md)。 |

### `minecraft:foliage_appearance`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 对象 | 未设置 | 树叶颜色。可写为RGB颜色，也可写为树叶色图对象。 |

树叶色图对象可包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color_map` | 字符串 | 未设置 | 树叶色图名称。 |

`color_map`可用值：

| 值 | 描述 |
| --- | --- |
| `birch` | 白桦树叶色图。 |
| `dry_foliage` | 干枯树叶色图。 |
| `evergreen` | 常绿树叶色图。 |
| `foliage` | 通用树叶色图。 |
| `mangrove_swamp_foliage` | 红树林沼泽树叶色图。 |
| `swamp_foliage` | 沼泽树叶色图。 |

### `minecraft:grass_appearance`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 对象 | 未设置 | 草颜色。可写为RGB颜色，也可写为草色图对象。 |

草色图对象可包含以下字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color_map` | 字符串 | 未设置 | 草色图名称。 |

`color_map`可用值：

| 值 | 描述 |
| --- | --- |
| `grass` | 通用草色图。 |
| `swamp_grass` | 沼泽草色图。 |

### `minecraft:sky_color`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `sky_color` | 字符串或数值数组 | 未设置 | 天空RGB颜色。 |

### `minecraft:water_appearance`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `surface_color` | 字符串或数值数组 | 未设置 | 水面RGB颜色。 |
| `surface_opacity` | 数值 | 未设置 | 水面不透明度，范围为`0`到`1`。 |

`surface_color`和`surface_opacity`至少应设置其一。

### `minecraft:dry_foliage_color`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color` | 字符串或数值数组 | 未设置 | 干枯树叶RGB颜色。 |

### `minecraft:precipitation`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `ash` | 数值 | 未设置 | 灰烬降水视觉密度。 |
| `blue_spores` | 数值 | 未设置 | 蓝色孢子降水视觉密度。 |
| `red_spores` | 数值 | 未设置 | 红色孢子降水视觉密度。 |
| `white_ash` | 数值 | 未设置 | 白色灰烬降水视觉密度。 |

同一生物群系最多设置一种降水类型。

### `minecraft:atmosphere_identifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `atmosphere_identifier` | 对象 | 未设置 | 大气散射配置标识符。引用目标应存在于`atmospherics/`目录并符合对应架构。相关字段见[大气散射设置](atmosphere-settings.md)。 |

### `minecraft:color_grading_identifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `color_grading_identifier` | 对象 | 未设置 | 色彩分级配置标识符。引用目标应存在于`color_grading/`目录并符合对应架构。相关字段见[色彩分级设置](color-grading-settings.md)。 |

### `minecraft:lighting_identifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `lighting_identifier` | 对象 | 未设置 | 光照配置标识符。引用目标应存在于`lighting/`目录并符合对应架构。相关字段见[光照设置](lighting-settings.md)。 |

### `minecraft:water_identifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `water_identifier` | 对象 | 未设置 | 水体配置标识符。引用目标应存在于`water/`目录并符合对应架构。相关字段见[水体设置](water-settings.md)。 |

### `minecraft:cubemap_identifier`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `cubemap_identifier` | 对象 | 未设置 | 天空盒配置标识符。引用目标应存在于`cubemaps/`目录并符合对应架构。 |

## 示例

```json title="RP/biomes/demo_the_end.json"
{
  "format_version": "1.21.40",
  "minecraft:client_biome": {
    "description": {
      "identifier": "minecraft:the_end"
    },
    "components": {
      "minecraft:sky_color": {
        "sky_color": "#000000"
      },
      "minecraft:fog_appearance": {
        "fog_identifier": "minecraft:fog_the_end"
      },
      "minecraft:water_appearance": {
        "surface_color": "#62529e"
      }
    }
  }
}
```