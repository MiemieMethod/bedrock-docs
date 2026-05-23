# 方块定义

本页列出行为包`blocks/`目录中的方块定义文件、资源包根目录`blocks.json`以及与自定义方块外观相关的辅助定义结构。方块定义用于声明一个可被世界、命令、战利品表、配方、物品放置器和脚本等系统引用的自定义方块。

## 行为包方块文件

行为包方块定义文件通常位于`blocks/`目录。根对象包含`format_version`和`minecraft:block`。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本字符串 | 未设置 | 方块定义文件使用的格式版本。较新的组件、萃取或字段可能要求更高版本。 |
| `minecraft:block` | 对象 | 未设置 | 方块定义对象，包含`description`、`components`、`permutations`等字段。 |

### `minecraft:block`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 对所有方块置换共同适用的描述信息。必须包含`identifier`。 |
| `components` | 对象 | 未设置 | 方块组件集合。每个键为组件标识符或标签组件名，值形态由组件决定。详见[方块组件](block-component.md)。 |
| `permutations` | 数组 | 未设置 | 方块置换列表。每项使用条件决定在特定方块状态下附加或覆盖的组件。详见[方块状态与置换](block-state.md)。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 方块的赋命名空间标识符。自定义方块应使用自己的命名空间；除非确实是在覆盖原版方块，否则不得使用`minecraft`命名空间。 |
| `states` | 对象 | 未设置 | 自定义方块状态集合。每个键为状态名，值为该状态允许的所有取值。 |
| `traits` | 对象 | 未设置 | 方块萃取集合，用于复用由引擎维护的放置方向、放置位置或连接状态。详见[方块萃取](block-trait.md)。 |
| `menu_category` | 对象 | 未设置 | 控制该方块是否出现在创造模式物品栏和合成台容器界面中。省略时通常不会出现在这些界面。 |

### `menu_category`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `category` | 字符串 | 未设置 | 创造模式分类。可用值为`construction`、`nature`、`equipment`、`items`和`none`。省略或设为`none`时，该方块不会显示在创造模式物品栏和合成台容器界面中。 |
| `group` | 本地化字符串 | 未设置 | 创造模式物品组的语言文件键。若省略，或不存在匹配的组，该方块会作为独立项放在所选分类中。 |
| `is_hidden_in_commands` | 布尔值 | `false` | 是否在命令中隐藏该方块。未设置时，命令默认可以使用该方块。 |

## 资源包`blocks.json`

资源包根目录的`blocks.json`用于声明方块在资源包侧的基础表现属性。Microsoft Learn说明，行为包组件`minecraft:geometry`和`minecraft:material_instances`会覆盖此文件中的纹理和渲染设置；因此，在较新的自定义方块中，`blocks.json`更常作为声音配置文件使用。

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `format_version` | 版本字符串 | 文件语法版本。 |
| `<namespace:block_name>` | 对象 | 单个方块的资源包侧配置项。键为方块标识符。 |
| `sound` | 字符串 | 放置、破坏或行走时使用的方块音效组。 |
| `textures` | 字符串或对象 | 地形图集中定义的纹理键。对象形态可按面指定纹理。 |
| `carried_textures` | 字符串或对象 | 手持或物品形态使用的纹理；省略时使用`textures`。 |
| `isotropic` | 布尔值 | 是否对方块纹理使用各向同性随机化。 |

`textures`对象可使用`up`、`down`、`north`、`south`、`east`和`west`指定单独面，也可使用`side`指定四个水平侧面，使用`*`作为未指定面的默认纹理。

## 方块剔除规则

方块剔除规则文件的根对象为`minecraft:block_culling_rules`。该文件定义几何体中的面、立方体或骨骼在相邻方块满足条件时是否被剔除。`minecraft:geometry.culling`字段可以引用剔除规则的`description.identifier`。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本字符串 | 未设置 | 方块剔除规则文件使用的格式版本。 |
| `minecraft:block_culling_rules` | 对象 | 未设置 | 方块剔除规则根对象。 |
| `description` | 对象 | 未设置 | 包含可被`minecraft:geometry`引用的剔除规则标识符。 |
| `rules` | 数组 | 未设置 | 剔除规则列表。 |

### 剔除规则项

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `geometry_part` | 对象 | 未设置 | 指定被剔除的骨骼、立方体或面。省略`cube`和`face`时可剔除整个骨骼。 |
| `direction` | 字符串 | 未设置 | 检查相邻方块的方向。若方块使用`minecraft:transformation`旋转，方向也随之旋转。 |

当`direction`方向上的相邻方块为完整且不透明的方块时，指定几何部分会被剔除。这里的不透明通常指完整立方体并使用`opaque`渲染方法。

## 方块物品表现

数据驱动方块会自动生成默认方块物品。物品组件`minecraft:block_placer`可让自定义物品放置指定方块；在`1.21.40`及“Upcoming Creator Features”实验性开关下，`replace_block_item`可将标识符相同的自定义物品显式注册为该方块的默认物品。

方块组件`minecraft:item_visual`可为方块物品形态指定不同于放置后方块的几何体和材质实例。使用该组件时，需要提供与`minecraft:geometry`和`minecraft:material_instances`对应的`geometry`和`material_instances`字段。

## `item_display_transforms`

`item_display_transforms`位于资源包几何体文件中，用于控制自定义方块作为物品渲染时的平移、旋转、缩放和轴心点。Microsoft Learn说明，该功能要求几何体版本不低于`1.21.0`，并需要启用“Upcoming Creator Features”实验性开关。

| 场景键 | 语义 |
| --- | --- |
| `firstperson_righthand` | 第一人称主手。 |
| `firstperson_lefthand` | 第一人称副手。 |
| `thirdperson_righthand` | 第三人称主手。 |
| `thirdperson_lefthand` | 第三人称副手。 |
| `fixed` | 物品展示框。 |
| `ground` | 世界中的掉落物。 |
| `gui` | 物品栏和界面。 |
| `head` | 头部显示场景。 |

| 字段 | 取值范围 | 描述 |
| --- | --- | --- |
| `translation` | `[-80,-80,-80]`到`[80,80,80]` | 平移。 |
| `rotation` | `[-360,-360,-360]`到`[360,360,360]` | 旋转。 |
| `scale` | `[0,0,0]`到`[4,4,4]` | 缩放。 |
| `rotation_pivot` | `[-80,-80,-80]`到`[80,80,80]` | 旋转轴心点，默认值为`[0,0,0]`。 |
| `scale_pivot` | `[-80,-80,-80]`到`[80,80,80]` | 缩放轴心点，默认值为`[0,0,0]`。 |
