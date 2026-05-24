# 地物定义

本页列出行为包`features/`目录中地物定义文件的主要结构和常用地物类型。地物定义用于描述一个可被世界生成系统放置的内容单元；地物规则、其他地物或部分原版世界生成流程可以引用该定义。

## 文件位置与命名

地物定义文件位于行为包的`features/`目录。官方资料要求每个文件只包含一个地物定义，且文件名必须与地物标识符中冒号后的名称一致。例如，`features/my_tree_feature.json`可以声明`my_pack:my_tree_feature`或`my_tree_feature`，但不应声明其他名称。

同一地物标识符被多个行为包定义时，包栈中位置较高的定义会覆盖较低的定义。使用地物系统不要求配套资源包；但当结构地物引用的结构包含自定义方块或自定义物品时，应同时提供对应资源包并建立依赖。官方入门资料建议行为包的`min_engine_version`至少为`1.20.20`。

## 根对象

地物文件的根对象通常由`format_version`和一个具体的`minecraft:*_feature`对象构成。该对象的名称决定地物类型。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 字符串 | 未设置 | 地物定义文件的格式版本。官方地物文档要求使用`1.13.0`或更高版本；部分现代字段要求更高版本。 |
| `minecraft:*_feature` | 对象 | 未设置 | 具体地物类型对象，例如`minecraft:ore_feature`、`minecraft:scatter_feature`或`minecraft:tree_feature`。 |

各具体地物类型对象都包含`description`对象。`description.identifier`为该地物的赋命名空间标识符，官方参考要求冒号后的名称与文件名一致。

## 地物类型

| 类型 | 用途 | 主要字段与限制 |
| --- | --- | --- |
| `minecraft:aggregate_feature` | 在同一输入位置放置一组地物，放置顺序不保证。 | `features`列出被放置的地物；至少一个地物成功时成功，全部失败时失败。 |
| `minecraft:cave_carver_feature` | 在当前区块及周围8向径向范围内雕刻洞穴。 | `height_limit`、`skip_carve_chance`、`width_modifier`、`fill_with`、`y_scale`、`horizontal_radius_multiplier`、`vertical_radius_multiplier`和`floor_level`控制雕刻；官方参考要求放置于`pregeneration_pass`。 |
| `minecraft:fossil_feature` | 生成由骨块和矿石类方块组成的化石结构。 | `ore_block`指定矿石方块；`max_empty_corners`限制包围盒角落为空气或流体的数量。 |
| `minecraft:geode_feature` | 生成晶洞状岩石结构。 | `filler`、各层方块、分布点、半径、裂口和潜在放置物相关字段共同控制结构；至少放置一个方块时成功。 |
| `minecraft:growing_plant_feature` | 放置从地面或天花板生长的柱状植物。 | `growth_direction`使用`UP`或`DOWN`；`height_distribution`、`body_blocks`、`head_blocks`和`allow_water`控制高度、主体、尖端与含水放置。 |
| `minecraft:height_difference_filter_feature` | 按周围高度差过滤地物放置。 | `search_radius`和上下方向的最小、最大高度差字段控制过滤条件。官方参考未给出示例。 |
| `minecraft:multiface_feature` | 在地面、墙面或天花板上放置多面向方块；名称虽指多面向方块，但官方说明允许任意方块。 | `places_block`、`search_range`、`can_place_on_floor`、`can_place_on_ceiling`、`can_place_on_wall`和`can_place_on`控制放置。 |
| `minecraft:nether_cave_carver_feature` | 在下界中雕刻洞穴。 | 字段与普通洞穴雕刻地物相近；官方参考要求放置于`pregeneration_pass`。 |
| `minecraft:ore_feature` | 放置模拟矿脉的一组方块；名称虽指矿石，但官方说明允许任意方块。 | `count`为放置方块数；`replace_rules`以`places_block`和`may_replace`定义替换规则。 |
| `minecraft:partially_exposed_blob_feature` | 生成大部分嵌入表面、允许单侧暴露的团块。 | `places_block`、`placement_radius_around_floor`、`placement_probability_per_valid_position`和`exposed_face`控制团块。 |
| `minecraft:scatter_feature` | 在区块中散植另一个地物。 | `places_feature`指定被散植地物；`distribution`自`format_version`为`1.21.20`起整合`iterations`、`x`、`y`、`z`和`scatter_chance`，旧格式将这些字段直接置于根级。 |
| `minecraft:sculk_patch_feature` | 生成幽匿块簇和表面蔓延结构。 | 官方参考明确标注该类型为原版内部用途，不支持自定义内容使用。 |
| `minecraft:search_feature` | 在轴对齐搜索体积内查找可放置位置并放置地物。 | `places_feature`、`search_volume`、`search_axis`和`required_successes`控制搜索范围、方向和所需成功次数。 |
| `minecraft:sequence_feature` | 按数据中出现的顺序依次放置一组地物。 | `features`列出地物序列；前一地物的输出位置作为后一地物的输入位置；任一地物失败时后续地物被跳过。 |
| `minecraft:single_block_feature` | 放置单个方块或按权重从多个方块中选择一个方块。 | 官方参考注明现代字段结构要求`format_version`不低于`1.21.40`；`places_block`、`may_attach_to`、`may_not_attach_to`、`may_replace`、`randomize_rotation`和放置规则检查字段共同控制放置。 |
| `minecraft:snap_to_surface_feature` | 将被放置地物的Y坐标吸附到地面、天花板或随机水平表面。 | `feature_to_snap`、`vertical_search_range`、`surface`、`allowed_surface_blocks`、`allow_air_placement`、`allow_underwater_placement`和`embed_in_surface`控制吸附行为。 |
| `minecraft:structure_template_feature` | 在世界中放置行为包`structures/`目录中的`.mcstructure`结构。 | `structure_name`指定结构；`adjustment_radius`、`facing_direction`、`ground_level`、`rotate_around_center`和`constraints`控制调整、朝向和放置约束。 |
| `minecraft:surface_relative_threshold_feature` | 在估算地表以下达到指定距离时放置地物。 | `feature_to_place`和`minimum_distance_below_surface`控制放置；官方参考说明该类型仅适用于使用1.18或更高世界生成的主世界生成器。 |
| `minecraft:tree_feature` | 生成由树干、树冠、根系和附属装饰组成的树。 | `base_block`、`may_grow_on`、`may_grow_through`、`may_replace`以及各类树干、树冠、根系对象共同描述树形。 |
| `minecraft:underwater_cave_carver_feature` | 在海平面以下雕刻水下洞穴。 | 字段与洞穴雕刻地物相近，额外可使用`replace_air_with`替换雕刻产生的空气；官方参考要求放置于`pregeneration_pass`。 |
| `minecraft:vegetation_patch_feature` | 在指定表面附近生成植被斑块。 | `ground_block`、`vegetation_feature`、`replaceable_blocks`、`surface`、`depth`、`vertical_range`、`horizontal_radius`、`vegetation_chance`和`waterlogged`控制斑块形态。 |
| `minecraft:weighted_random_feature` | 按权重从多个地物中选择并放置一个。 | `features`为由地物标识符和权重组成的列表。 |

## 内部或已弃用地物

Microsoft Learn将下列地物类型标记为原版内部用途或已弃用类型。这些类型不应作为自定义内容中的普通地物类型使用。

| 类型 | 官方说明概要 |
| --- | --- |
| `minecraft:beards_and_shavers` | 为结构生成“胡须”式填充或剃除空间，以便结构与地形衔接。 |
| `minecraft:conditional_list` | 按顺序检查条件，并放置第一个满足条件的地物。 |
| `minecraft:rect_layout` | 在矩形网格中排列地物。 |
| `minecraft:scan_surface` | 扫描地表位置后放置地物。 |
| `minecraft:sculk_patch_feature` | 生成幽匿块簇及其蔓延结构。 |

## 地物规则关联

地物定义本身只描述可放置内容。地物若要参与常规世界生成，通常还需要通过[地物规则](feature-rule.md)挂接到至少一个生物群系。世界生成时，生物群系按区块尝试执行附加到自身的地物规则；规则中的`conditions`决定生物群系过滤和放置阶段，`distribution`决定地物的初始散植。

## 散植参数

`minecraft:scatter_feature`和地物规则的`distribution`使用相同的散植参数概念。`iterations`控制尝试放置次数；`scatter_chance`在每次散植前检查一次，检查失败时不会执行任何迭代；`x`、`y`和`z`是相对输入位置的偏移，可以是固定值、随机分布对象或求值为数字的Molang表达式；`coordinate_eval_order`控制坐标求值顺序。

/// note | 版本差异
`minecraft:scatter_feature`在`1.21.20`及更高格式中使用`distribution`字段集中保存散植参数。较早格式将`iterations`、`x`、`y`、`z`和`scatter_chance`直接写在`minecraft:scatter_feature`对象内。
///

## 结构地物约束

`minecraft:structure_template_feature`的`constraints`可限制结构与环境的关系。

| 字段 | 描述 |
| --- | --- |
| `block_intersection` | 限制结构只能与允许的方块相交；`only_check_intersection_for_motion_blocking_blocks`为真时仅检查结构内阻碍运动的方块。 |
| `grounded` | 要求结构的地面层接触地面。 |
| `leveled` | 要求结构地面层位于相对平坦的地形上；`max_steepness`限制结构四边采样点与放置点之间的最大高度差。 |
| `unburied` | 要求结构上方具有空气。 |