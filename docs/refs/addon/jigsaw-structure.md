# 拼图结构

本页列出国际版行为包拼图结构相关JSON结构，覆盖`minecraft:jigsaw_structure`和`minecraft:jigsaw_structure_metadata`两类根对象。内容来源于Microsoft Learn的JigsawReference自动导出资料。

/// warning | 资料状态
JigsawReference为自动导出内容，部分子结构页面存在字段命名和类型不一致。以下表格优先采用主结构页面可互相印证的字段，并在差异处标注。
///

## 文件位置与作用

- 拼图结构定义通常放置于行为包`worldgen/jigsaw_structures/`目录。
- 拼图结构用于描述结构生成入口、递归深度、高度与地形适配策略。
- 拼图结构本身不直接存放方块数据，被引用的结构模板仍来自`structures/`目录中的`.mcstructure`文件。

## `minecraft:jigsaw_structure`根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 拼图结构定义格式版本。 |
| `minecraft:jigsaw` | 对象 | 未设置 | 拼图结构定义主体。 |

## `minecraft:jigsaw`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 结构标识信息。 |
| `biome_filters` | 对象数组 | 未设置 | 生物群系过滤器数组，用于限制可生成生物群系。 |
| `heightmap_projection` | 字符串 | 未设置 | 表面投影高度图类型。 |
| `max_depth` | 整数 | `7` | 拼图递归连接最大深度。 |
| `max_distance_from_center` | 对象 | 未设置 | 相对结构中心的最大生成距离。 |
| `start_height` | 对象 | 未设置 | 起始高度提供器配置。 |
| `start_pool` | 字符串 | 未设置 | 起始模板池标识符。 |
| `step` | 字符串 | 未设置 | 世界生成阶段。 |
| `terrain_adaptation` | 字符串 | 未设置 | 结构与地形适配策略。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 拼图结构赋命名空间标识符。 |

### `heightmap_projection`

`heightmap_projection`支持下列值：

- `world_surface`
- `world_surface_wg`
- `ocean_floor`
- `ocean_floor_wg`
- `motion_blocking`
- `motion_blocking_no_leaves`

### `max_distance_from_center`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `horizontal` | 整数 | `80` | 水平方向最大距离（方块）。 |
| `vertical` | 整数 | `80` | 垂直方向最大距离（方块）。 |

### `start_height`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `type` | 字符串 | 未设置 | 高度提供器类型。 |
| `value` | 对象 | 未设置 | 对应高度提供器的值对象。 |

`start_height.type`支持下列值：

- `constant`
- `uniform`
- `biased_to_bottom`
- `very_biased_to_bottom`
- `trapezoid`
- `weighted_list`

`start_height.value`可使用下列键：

| 键 | 类型 | 描述 |
| --- | --- | --- |
| `above_bottom` | 整数 | 距世界底部的偏移量。 |
| `absolute` | 整数 | 绝对Y坐标。 |
| `below_top` | 整数 | 距世界顶部的偏移量。 |

### `step`

`step`支持下列值：

- `raw_generation`
- `lakes`
- `local_modifications`
- `underground_structures`
- `surface_structures`
- `strongholds`
- `underground_ores`
- `underground_decoration`
- `fluid_springs`
- `vegetal_decoration`
- `top_layer_modification`

### `terrain_adaptation`

`terrain_adaptation`支持下列值：

- `none`
- `beard_thin`
- `beard_box`
- `bury`
- `encapsulate`

## `minecraft:jigsaw_structure_metadata`根对象

自动导出资料同时包含拼图结构元数据根对象与元数据注册表结构，适用于描述已生成结构的元数据映射。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 元数据文件格式版本。 |
| `minecraft:jigsaw_structure_metadata` | 对象 | 未设置 | 拼图结构元数据注册表。 |

### 元数据注册表对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `metadata` | 对象 | 未设置 | 结构位置到拼图元数据的映射表。 |

### 拼图方块元数据项

自动导出资料定义了拼图方块元数据项结构，字段如下：

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `block` | 字符串 | 未设置 | 生成前拼图方块序列化标识符。 |
| `final_block` | 字符串 | 未设置 | 生成后替换该起始拼图方块的序列化标识符。 |
| `joint_type` | 字符串 | 未设置 | 与目标拼图方块连接时使用的关节类型。 |
| `name` | 字符串 | 未设置 | 可被其他拼图方块`target`字段引用的名称。 |
| `placement_priority` | 整数 | 未设置 | 目标方块放置优先级。 |
| `pool` | 字符串 | 未设置 | 可选结构模板所在模板池标识符。 |
| `pos` | 对象 | 未设置 | 拼图方块位置对象。 |
| `selection_priority` | 整数 | 未设置 | 目标方块选择优先级。 |
| `target` | 字符串 | 未设置 | 在生成结构中要连接的目标拼图名称。 |
