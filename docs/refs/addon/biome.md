# 生物群系定义

本页列出行为包`biomes/`目录中生物群系定义文件的主要字段。生物群系定义文件的根对象包含`format_version`和`minecraft:biome`。`minecraft:biome`用于声明生物群系的标识信息和服务端生成组件。

/// warning | 适用范围
本页记录的是行为包中的服务端生物群系定义。资源包中的客户端生物群系文件负责天空颜色、水色、迷雾和环境声音等客户端表现，不使用本页所列的根对象结构。
///

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 生物群系定义文件使用的格式版本。 |
| `minecraft:biome` | 对象 | 未设置 | 单个生物群系定义。 |

## `minecraft:biome`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 生物群系的非组件设置。 |
| `components` | 对象 | 未设置 | 生物群系使用的组件集合。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 生物群系的赋命名空间标识符，可被`/locate biome`等功能引用。标识符应仅使用小写字符，且必须匹配`^[a-z0-9._%+-]+:[a-z0-9._%+-]+$`。 |

## `components`

| 组件 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `minecraft:climate` | 对象 | 未设置 | 定义温度、降水量和积雪等气候属性。未设置时使用默认值。 |
| `minecraft:creature_spawn_probability` | 对象 | 未设置 | 定义区块生成时生物在该生物群系中生成的概率。 |
| `minecraft:humidity` | 对象 | 未设置 | 强制该生物群系始终潮湿或始终不潮湿，并影响火焰蔓延概率和速度。 |
| `minecraft:map_tints` | 对象 | 未设置 | 定义地图上草和树叶的染色色调。 |
| `minecraft:mountain_parameters` | 对象 | 未设置 | 定义主世界山地地形生成使用的噪声参数。 |
| `minecraft:multinoise_generation_rules` | 对象 | 未设置 | 定义旧版下界多噪声生成规则。 |
| `minecraft:overworld_generation_rules` | 对象 | 未设置 | 定义旧版主世界生成规则。 |
| `minecraft:overworld_height` | 对象 | 未设置 | 定义主世界高度噪声参数。 |
| `minecraft:partially_frozen` | 对象 | 未设置 | 影响冻结生物群系的局部温度，使一部分区域不冻结。 |
| `minecraft:replace_biomes` | 对象 | 未设置 | 定义用当前生物群系替换一个或多个原版生物群系的规则。 |
| `minecraft:subsurface_builder` | 对象 | 未设置 | 指定应用于常规地形表面下方生物群系的地表构建器。 |
| `minecraft:surface_builder` | 对象 | 未设置 | 定义地形生成使用的地表材料。 |
| `minecraft:surface_material_adjustments` | 对象 | 未设置 | 按噪声函数对生成材料进行细节调整。 |
| `minecraft:tags` | 对象 | 未设置 | 为生物群系附加字符串标签。 |
| `minecraft:village_type` | 对象 | 未设置 | 定义村庄类型。 |

### `minecraft:climate`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `temperature` | 数值 | 未设置 | 温度。影响雪和冰的放置、海绵干燥、天空颜色等视觉或行为表现。 |
| `downfall` | 数值 | 未设置 | 降水对颜色和方块变化的影响程度。设为`0`会阻止该生物群系下雨。 |
| `snow_accumulation` | 数值数组 | 未设置 | 最小和最大积雪层数范围。数组必须恰有2个元素，每增加`0.125`表示增加一层雪。 |

### `minecraft:creature_spawn_probability`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `probability` | 数值 | 未设置 | 区块生成时生物生成的概率，取值范围为`0.0`到`0.75`。 |

### `minecraft:humidity`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `is_humid` | 布尔值 | 未设置 | 是否强制该生物群系按潮湿环境处理。 |

### `minecraft:map_tints`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `foliage` | 字符串或数值数组 | 未设置 | 地图上树叶使用的染色色调。 |
| `grass` | 对象 | 未设置 | 地图上草的染色色调，可使用自定义色调或基于噪声的色调。 |

`foliage`和固定色调形式的`grass.tint`可写为字符串，也可写为数值数组。`grass.type`用于选择地图草色计算方式，可为`noise`或`tint`；`noise`表示使用基于噪声的草色色调，`tint`表示使用`grass.tint`指定的固定色调。

### `minecraft:mountain_parameters`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `east_slopes` | 布尔值 | 未设置 | 是否启用东向坡面。 |
| `north_slopes` | 布尔值 | 未设置 | 是否启用北向坡面。 |
| `south_slopes` | 布尔值 | 未设置 | 是否启用南向坡面。 |
| `west_slopes` | 布尔值 | 未设置 | 是否启用西向坡面。 |
| `material` | 字符串或方块说明对象 | 未设置 | 陡峭坡面使用的方块。 |
| `steep_material_adjustment` | 对象 | 未设置 | 陡峭坡面的材料调整。 |
| `top_slide` | 对象 | 未设置 | 世界顶部密度渐变控制。 |

方块说明对象通常包含`name`和`states`。`states`是以方块状态名为键的集合，值可为布尔值、整数或字符串。

`steep_material_adjustment`可再次指定`east_slopes`、`north_slopes`、`south_slopes`、`west_slopes`和`material`，用于定义特定朝向陡坡的表面材料。`top_slide.enabled`为`false`时禁用顶部滑动，为`true`时会将其他顶部滑动参数纳入计算。

### 旧版生成规则组件

/// note | 旧版组件
官方参考说明，`minecraft:multinoise_generation_rules`是洞穴与山崖更新前的组件，且不用于自定义生物群系。`minecraft:overworld_generation_rules`同样是洞穴与山崖更新前的组件，且不用于自定义生物群系。`minecraft:overworld_height`也是洞穴与山崖更新前的组件；它不会改变主世界高度，目前仅影响地图物品渲染。
///

#### `minecraft:multinoise_generation_rules`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `target_altitude` | 数值 | 未设置 | 相对于其他生物群系的目标海拔。 |
| `target_humidity` | 数值 | 未设置 | 相对于其他生物群系的目标湿度。 |
| `target_temperature` | 数值 | 未设置 | 相对于其他生物群系的目标温度。 |
| `target_weirdness` | 数值 | 未设置 | 相对于其他生物群系的目标怪异度。 |
| `weight` | 数值 | 未设置 | 相对于其他生物群系的生成权重。 |

#### `minecraft:overworld_generation_rules`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `generate_for_climates` | 字符串或数组 | 未设置 | 控制该生物群系可出现的主世界气候类别。条目由气候名和权重组成。 |
| `hills_transformation` | 字符串或数组 | 未设置 | 转换为丘陵生物群系时使用的目标生物群系。 |
| `mutate_transformation` | 字符串或数组 | 未设置 | 转换为变种生物群系时使用的目标生物群系。 |
| `river_transformation` | 字符串或数组 | 未设置 | 转换为河流生物群系时使用的目标生物群系。 |
| `shore_transformation` | 字符串或数组 | 未设置 | 邻近海洋生物群系时转换为的目标生物群系。 |

`generate_for_climates`、`hills_transformation`等字段使用的气候类别包括`medium`、`warm`、`lukewarm`、`cold`和`frozen`。

#### `minecraft:overworld_height`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `noise_params` | 数值数组 | 未设置 | 高度噪声参数。第1个值为深度，越负越偏向水下，越正越偏向高处；第2个值为缩放。数组必须恰有2个元素。 |
| `noise_type` | 字符串 | 未设置 | 使用内置预设而非手动`noise_params`。 |

`noise_type`可为`beach`、`deep_ocean`、`default`、`default_mutated`、`extreme`、`highlands`、`less_extreme`、`lowlands`、`mountains`、`mushroom`、`ocean`、`river`、`stone_beach`、`swamp`或`taiga`。

### `minecraft:replace_biomes`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `replacements` | 对象数组 | 未设置 | 生物群系替换配置列表。 |

`replacements`中的每个对象具有下列字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `amount` | 数值 | 未设置 | 尝试替换的噪声阈值，作用类似百分比。取值范围为`(0.0,1.0]`。 |
| `dimension` | 字符串 | 未设置 | 替换发生的维度，可为`minecraft:overworld`或`minecraft:nether`。 |
| `noise_frequency_scale` | 数值 | 未设置 | 替换尝试的频率缩放，取值范围为`(0.0,100.0]`。较低值通常形成更大、更少的连续区域；较高值通常形成更小、更多的连续区域。 |
| `targets` | 对象数组 | 未设置 | 要被当前生物群系替换的生物群系。目标生物群系名不应包含命名空间，且数组至少包含1项。 |

/// warning | 替换顺序
官方参考说明，向`replacements`列表前部追溯添加新替换项会导致世界生成改变。新增替换项应追加到列表末尾。
///

### `minecraft:surface_builder`与`minecraft:subsurface_builder`

`minecraft:surface_builder`控制地形生成使用的地表材料。`minecraft:subsurface_builder`具有相近结构，但用于常规地形表面下方的生物群系。官方参考指出，既有地表构建器类型尚未完全适配地下高度范围，因此在`minecraft:subsurface_builder`中使用它们可能产生意外结果。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `builder` | 对象 | 未设置 | 地表构建器设置。 |

`builder.type`可为`minecraft:overworld`、`minecraft:frozen_ocean`、`minecraft:mesa`、`minecraft:swamp`、`minecraft:capped`、`minecraft:the_end`或`minecraft:noise_gradient`。其中，`minecraft:overworld`、`minecraft:frozen_ocean`、`minecraft:mesa`和`minecraft:swamp`常见字段如下：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `foundation_material` | 字符串或方块说明对象 | 未设置 | 生物群系深层地下使用的方块。 |
| `mid_material` | 字符串或方块说明对象 | 未设置 | 生物群系表面下方层使用的方块。 |
| `top_material` | 字符串或方块说明对象 | 未设置 | 生物群系表面使用的方块。 |
| `sea_floor_material` | 字符串或方块说明对象 | 未设置 | 水体底部使用的方块。 |
| `sea_material` | 字符串或方块说明对象 | 未设置 | 水体使用的方块。 |
| `sea_floor_depth` | 整数 | 未设置 | 水平面下方水底应出现的深度，最大为`127`。 |

`minecraft:frozen_ocean`类型与常规主世界地表构建器相近，但会额外生成冰山。`minecraft:mesa`类型额外支持`bryce_pillars`、`clay_material`、`hard_clay_material`和`has_forest`。`minecraft:swamp`类型额外支持`max_puddle_depth_below_sea_level`，用于控制水平面下方可替换为水坑的查找深度，最大为`127`。

`minecraft:capped`类型用于在上方或下方存在非固体方块的方块上生成表面，可使用`beach_material`、`ceiling_materials`、`floor_materials`、`foundation_material`和`sea_material`。`ceiling_materials`和`floor_materials`至少包含1项。`minecraft:the_end`类型表示使用末地维度特征地形生成，仅需指定`type`。

`minecraft:noise_gradient`类型根据噪声分布连续放置方块带，其处理流程已考虑地下高度范围。该类型支持下列字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `noise_block_specifiers` | 对象数组 | 未设置 | 将噪声范围或阈值映射到方块的说明项，至少包含1项。噪声范围在`[-1,1]`区间内有效，端点可以重叠。 |
| `noise_descriptor` | 对象 | 未设置 | 地表构建器使用的噪声说明。 |
| `non_replaceable_blocks` | 字符串或方块说明对象 | 未设置 | 不允许被此地表构建器替换的方块列表。未设置或为空时，可以替换任意非空气方块。 |

`noise_block_specifiers`中的每个对象可包含`block`、`noise`、`range`和`threshold`。`block`是噪声采样满足条件时放置的方块；`noise`是与该说明项关联的噪声字符串标识符，必须匹配非空白字符串；`range`由`min`和`max`组成，默认均为`0`；`threshold`是采样噪声值的最低阈值，默认值为`0`。

`noise_descriptor`可包含`name`、`first_octave`和`amplitudes`。`name`仅用于初始化噪声，不影响生成值的定性特征；`first_octave`控制生成噪声的一般频率特征，较低值会产生较低频率内容；`amplitudes`控制前若干个八度的衰减，数组至少包含1项，至多包含100项。

### `minecraft:partially_frozen`

该组件影响冻结生物群系中的局部温度，使一部分区域不冻结，例如形成斑驳冰面或斑驳积雪。官方参考未列出额外字段。

### `minecraft:surface_material_adjustments`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `adjustments` | 对象数组 | 未设置 | 与某列噪声值匹配时应用的材料调整。多个匹配项按列表顺序应用。 |

`adjustments`中的每个对象具有下列字段：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `height_range` | 数值数组、布尔值或字符串 | 未设置 | 调整适用的高度噪声范围。数组形式必须恰有2个元素。 |
| `noise_range` | 数值数组 | 未设置 | 调整适用的噪声值范围。数组必须恰有2个元素。 |
| `noise_frequency_scale` | 数值 | 未设置 | 访问材料调整噪声值时乘到位置上的缩放。 |
| `materials` | 对象 | 未设置 | 调整生效时使用的方块材料。 |

`materials`可包含`foundation_material`、`mid_material`、`sea_floor_material`、`sea_material`和`top_material`。这些字段均可使用字符串或方块说明对象。

### `minecraft:tags`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `tags` | 字符串数组 | 未设置 | 供实体生成等其他系统使用的生物群系标签。 |

大多数标签由JSON设置引用。部分标签的意义直接实现在游戏代码中：

| 标签 | 描述 |
| --- | --- |
| `birch` | 该生物群系使用野花，且与其他花类生物群系标签互斥；若同时具有`hills`标签则无效。 |
| `cold` | 村民穿着寒冷天气服装。 |
| `deep` | 洞穴与山崖更新前，用于阻止海洋拥有岛屿或相连河流，并降低该生物群系生成丘陵的概率。 |
| `desert` | 允许半埋藏的废弃传送门生成；玩家附近的沙子方块会播放环境音效。 |
| `extreme_hills` | 废弃传送门可以生成在比通常更高的位置；同时具有`forest`或`forest_generation`标签的生物群系使用普通主世界花，而非森林花。 |
| `flower_forest` | 该生物群系使用森林花，且与其他花类生物群系标签互斥。 |
| `forest` | 该生物群系使用森林花，且与其他花类生物群系标签互斥；若同时具有`taiga`或`extreme_hills`标签则无效。 |
| `forest_generation` | 等同于`forest`。 |
| `frozen` | 村民穿着寒冷天气服装；若同时具有`ocean`标签，则阻止该生物群系包含岩浆泉。 |
| `ice` | 废弃传送门附近的岩浆总是替换为下界岩，且下界岩不能被岩浆块替换。 |
| `ice_plains` | 若同时具有`mutated`标签，则阻止该生物群系包含岩浆泉。 |
| `jungle` | 废弃传送门会非常多苔。 |
| `hills` | 同时具有`meadow`或`birch`标签的生物群系使用普通主世界花，而非野花。 |
| `meadow` | 该生物群系使用野花，且与其他花类生物群系标签互斥；若同时具有`hills`标签则无效。 |
| `mesa` | 玩家附近的沙子方块会播放环境音效。 |
| `mountain` | 废弃传送门可以生成在比通常更高的位置。 |
| `mutated` | 洞穴与山崖更新前，用于阻止切换到指定的`mutate_transformation`，因为该生物群系已视为变种；若同时具有`ice_plains`标签，则阻止该生物群系包含岩浆泉。 |
| `no_legacy_worldgen` | 阻止生物群系使用旧版世界生成行为，除非该生物群系正被放置在主世界中。 |
| `ocean` | 若同时具有`frozen`标签，则阻止该生物群系包含岩浆泉；允许废弃传送门在水下生成；洞穴与山崖更新前，用于决定是否在生物群系边缘放置海岸线和河流，并在不存在`deep`标签时将生物群系标识为浅海以放置岛屿。 |
| `pale_garden` | 该生物群系使用闭眼花簇，且与其他花类生物群系标签互斥。 |
| `plains` | 该生物群系使用平原花，且与其他花类生物群系标签互斥。 |
| `rare` | 洞穴与山崖更新前，用于将该生物群系标记为特殊生物群系。海洋不能是特殊生物群系。 |
| `swamp` | 允许废弃传送门在水下生成；该生物群系使用沼泽花，且与其他花类生物群系标签互斥。 |
| `taiga` | 同时具有`forest`或`forest_generation`标签的生物群系使用普通主世界花，而非森林花。 |

### `minecraft:village_type`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 村庄类型，可为`default`、`desert`、`ice`、`savanna`或`taiga`。 |

## 示例

```json title="BP/biomes/example_biome.json"
{
  "format_version": "1.21.110",
  "minecraft:biome": {
    "description": {
      "identifier": "demo:white_sand_beach"
    },
    "components": {
      "minecraft:climate": {
        "downfall": 0.4,
        "snow_accumulation": [0.0, 0.125],
        "temperature": 0.8
      },
      "minecraft:surface_builder": {
        "builder": {
          "type": "minecraft:overworld",
          "sea_floor_depth": 7,
          "sea_floor_material": "minecraft:gravel",
          "foundation_material": "minecraft:stone",
          "mid_material": "demo:white_sand",
          "top_material": "demo:white_sand",
          "sea_material": "minecraft:water"
        }
      },
      "minecraft:tags": {
        "tags": ["beach", "monster", "overworld", "warm"]
      }
    }
  }
}
```
