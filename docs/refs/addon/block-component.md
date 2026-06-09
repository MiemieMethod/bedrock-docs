# 方块组件

本页列出行为包方块定义中`minecraft:block.components`对象可用的主要方块组件、值形态、关键字段、版本或实验性要求，以及官方列为内部或已弃用的项。方块定义的根结构见[方块定义](block.md)。

## 组件一览

| 组件 | 值形态 | 默认值 | 用途与主要字段 |
| --- | --- | --- | --- |
| `minecraft:block_light_absorption` | 数值 | 未设置 | 旧组件，仅用于`format_version`低于`1.19.40`的内容。表示光穿过方块时被削减的等级，范围为`0`到`15`；新内容应使用`minecraft:light_dampening`。 |
| `minecraft:block_light_emission` | 数值 | 未设置 | 旧组件，仅用于`format_version`低于`1.19.40`的内容。表示方块发光等级，范围为`0`到`15`；新内容应使用`minecraft:light_emission`。 |
| `minecraft:chest_obstruction` | 对象 | 未设置 | 控制箱子开启时如何判断该方块阻挡箱盖。`obstruction_rule`为字符串，默认值为`shape`。在`1.26.20`之前的格式版本中需要“Upcoming Creator Features”。 |
| `minecraft:collision_box` | 布尔值或对象 | 完整碰撞箱 | 定义实体碰撞箱。`true`使用默认完整方块，`false`禁用实体碰撞；对象形态使用`origin`和`size`，两者相加必须落在`[-8,0,-8]`到`[8,24,8]`范围内。 |
| `minecraft:connection_rule` | 对象 | 未设置 | 定义栅栏、墙、铁栏杆、玻璃板等是否可连接到该方块。`accepts_connections_from`默认值为`all`；`enabled_directions`默认启用`north`、`south`、`east`和`west`。在`1.26.0`之前的格式版本中需要“Upcoming Creator Features”。 |
| `minecraft:crafting_table` | 对象 | 未设置 | 使方块打开自定义合成台界面。仅支持有序配方和无序配方。`crafting_tags`最多`64`个标签，每个标签最多`64`个字符；`table_name`为界面标题的本地化键。 |
| `minecraft:destroy_time` | 数值 | 未设置 | 旧组件，仅用于`format_version`低于`1.19.40`的内容。表示基础工具破坏耗时；新内容应使用`minecraft:destructible_by_mining`。 |
| `minecraft:destructible_by_explosion` | 布尔值或对象 | 默认爆炸抗性 | 控制爆炸能否破坏方块。`true`使用默认爆炸抗性，`false`表示不可被爆炸破坏；对象形态使用`explosion_resistance`设置爆炸抗性，默认值为`0`。 |
| `minecraft:destructible_by_mining` | 布尔值或对象 | 默认破坏耗时 | 控制开采破坏耗时。`true`使用默认耗时，`false`表示不可开采破坏；对象形态使用`seconds_to_destroy`和`item_specific_speeds`。`item_specific_speeds`项包含`item`匹配项和`destroy_speed`。 |
| `minecraft:destruction_particles` | 对象 | 未设置 | 设置方块被破坏时产生的粒子<!-- md:flag experimental -->。`particle_count`默认`100`且最大`255`；`texture`指定粒子纹理；`tint_method`可为`none`、`default_foliage`、`birch_foliage`、`evergreen_foliage`、`dry_foliage`、`grass`或`water`。 |
| `minecraft:display_name` | 字符串 | 方块名 | 设置物品栏和快捷栏悬停时显示的文本。字符串可为本地化键；无法解析为本地化键时会直接显示原始字符串。 |
| `minecraft:embedded_visual` | 对象 | 未设置 | 设置方块嵌入另一个方块内部时使用的几何体和材质实例，例如花盆中的花。字段为`geometry`和`material_instances`，形态对应同名组件。 |
| `minecraft:entity_fall_on` | 对象 | `1`格 | 设置实体至少下落多少格后触发脚本自定义组件事件`onEntityFallOn`。字段`minimum_fall_distance`为十进制数。 |
| `minecraft:explosion_resistance` | 数值 | 未设置 | 旧组件，仅用于`format_version`低于`1.19.40`的内容。新内容应使用`minecraft:destructible_by_explosion`。 |
| `minecraft:flammable` | 布尔值或对象 | 不自然引燃 | 控制方块自然引燃和燃毁概率。`true`使用木板式默认值，`false`或省略时不会因邻近火焰自然着火，但仍可被直接点燃；对象形态使用`catch_chance_modifier`和`destroy_chance_modifier`，默认值分别为`5`和`20`。 |
| `minecraft:flower_pottable` | 空对象 | 未设置 | 表示该方块可被放入花盆。 |
| `minecraft:friction` | 数值 | `0.4` | 设置实体在方块上移动时的摩擦力，范围为`0.0`到`0.9`。值越大越不易滑动；冰的参考值为`0.02`。 |
| `minecraft:geometry` | 字符串或对象 | 未设置 | 指定方块渲染几何体。可使用资源包中的几何体标识符，也可使用`minecraft:geometry.full_block`或`minecraft:geometry.cross`。对象形态可设置`identifier`、`bone_visibility`、`culling`、`culling_layer`、`culling_shape`和`uv_lock`。 |
| `minecraft:instrument_sound` | 对象 | `up`为`note.harp`，`down`为`note.none` | 设置音符盒位于方块上方或下方时使用的乐器音色<!-- md:flag experimental -->。字段`up`和`down`至少设置其一；可用`note.none`表示无声音。 |
| `minecraft:item_visual` | 对象 | 未设置 | 设置该方块作为物品显示时使用的几何体和材质实例<!-- md:flag experimental -->。字段`geometry`和`material_instances`均为必填，并映射到同名方块组件的结构。 |
| `minecraft:light_dampening` | 数值 | 未设置 | 设置光穿过方块时被削减的等级，范围为`0`到`15`。`0`近似完全透明，`15`近似完全不透光；树叶参考值为`1`，水参考值为`2`。 |
| `minecraft:light_emission` | 数值 | 未设置 | 设置方块发光等级，范围为`0`到`15`。火把参考值为`14`，荧石参考值为`15`，红石火把参考值为`7`，灵魂火把参考值为`10`。怪物不能在亮度等级不低于`8`的方块上生成。 |
| `minecraft:liquid_detection` | 对象或对象数组 | 未设置 | 定义方块检测液体时的行为。每种液体类型只能使用一条规则；后续重复规则会被忽略。关键字段包括`liquid_type`、`can_contain_liquid`、`on_liquid_touches`、`stops_liquid_flowing_from_direction`和`use_liquid_clipping`。目前官方资料仅列出`water`液体类型。 |
| `minecraft:loot` | 字符串 | 掉落自身 | 指定方块被破坏时使用的战利品表路径。路径相对于行为包根目录，例如`loot_tables/blocks/example.json`，字符串最长`256`个字符。 |
| `minecraft:map_color` | 字符串、数组或对象 | 不显示在地图上 | 设置方块在地图上渲染的颜色。颜色可写为`#RRGGBB`字符串，也可写为`[R,G,B]`数组；对象形态还可设置`tint_method`。 |
| `minecraft:material_instances` | 对象或字符串 | 未设置 | 将几何体中的面名或材质实例名映射到实际材质实例。面键包括`*`、`up`、`down`、`north`、`south`、`east`和`west`。材质实例可设置`texture`、`render_method`、`ambient_occlusion`、`face_dimming`、`isotropic`和`tint_method`。`isotropic`要求`format_version`不低于`1.21.80`。 |
| `minecraft:movable` | 对象 | 未设置 | 控制方块被活塞等方块推动时的移动行为<!-- md:flag experimental -->。`movement_type`为必填字段，默认语义为`push_pull`；`sticky`控制推动时如何处理相邻方块，默认值为`none`。在`1.21.100`之前的格式版本中需要“Upcoming Creator Features”。 |
| `minecraft:placement_filter` | 对象 | 未设置 | 设置方块可以放置和保持存在的条件。`conditions`最多`64`项；每项可设置`allowed_faces`和`block_filter`。`allowed_faces`可用`up`、`down`、`north`、`south`、`east`、`west`、`side`和`all`，最多`6`个面。`block_filter`项可使用`name`、`states`和`tags`。 |
| `minecraft:precipitation_interactions` | 对象 | 未设置 | 设置方块与雨雪的交互<!-- md:flag experimental -->。`precipitation_behavior`为行为字符串。Microsoft Learn当前列出的值包括`obrain`、`obstruct_rain_accumulate_snow`和`none`；实际可用值应以目标版本内容日志校验为准。在`1.21.120`之前的格式版本中需要“Upcoming Creator Features”。 |
| `minecraft:random_offset` | 对象 | 未设置 | 根据方块位置和指定范围随机偏移方块渲染位置、轮廓和碰撞。`x`、`y`、`z`分别包含`range`和`steps`；`range`包含`min`和`max`。 |
| `minecraft:redstone_conductivity` | 对象 | 使用默认红石属性 | 设置基础红石导电属性，要求`format_version`不低于`1.21.30`。`allows_wire_to_step_down`默认`true`；`redstone_conductor`默认`false`。 |
| `minecraft:redstone_consumer` | 对象 | 未设置 | 表示方块可消耗并可能传播红石信号。该组件不可用于方块置换。`min_power`设置最小输入信号强度，默认`0`；`propagates_power`控制是否让信号穿过该方块，默认`false`。 |
| `minecraft:redstone_producer` | 对象 | 未设置 | 表示方块产生红石信号。`power`为`0`到`15`；`connected_faces`指定参与电路连接的面；`strongly_powered_face`指定被强充能的面；`transform_relative`为真时会随`minecraft:transformation`旋转相关面。 |
| `minecraft:replaceable` | 空对象 | 未设置 | 表示其他方块可放置到同一位置并替换该方块<!-- md:flag experimental -->。在`1.21.60`之前的格式版本中需要“Upcoming Creator Features”。 |
| `minecraft:selection_box` | 布尔值或对象 | 完整选取箱 | 定义玩家准星选中方块时显示的选取箱。`true`使用完整方块，`false`使方块不可被准星选中；对象形态使用`origin`和`size`，两者相加必须落在`[-8,0,-8]`到`[8,16,8]`范围内。 |
| `minecraft:support` | 对象 | 单位立方体支撑 | 定义方块的支撑形状。`shape`为必填字段，目前官方列出`fence`和`stair`。自定义楼梯支撑通常还需要通过方块特质启用`minecraft:vertical_half`和`minecraft:cardinal_direction`或`minecraft:facing_direction`。 |
| `tag:<标签名>` | 空对象 | 未设置 | 为方块添加标签。创作者可以创建自己的标签，但只有原版方块标签可使用`minecraft:`命名空间。原版标签表见[原版方块标签](../tables/blocks/vanilla_tags.md)。 |
| `minecraft:tick` | 对象 | 未设置 | 使方块按随机选取的固定间隔触发脚本自定义组件`onTick`事件。`interval_range`为刻数范围，默认`[0,0]`；`looping`默认`true`。监听`onTick`的自定义组件若添加到没有该组件的方块上，会产生内容错误。 |
| `minecraft:transformation` | 对象 | 未设置 | 设置方块相对世界位置中心的平移、旋转和缩放。字段包括`translation`、`rotation`、`scale`、`rotation_pivot`和`scale_pivot`；`rotation`使用`90`度增量。 |

## 材质实例渲染方法

| 值 | 用途 |
| --- | --- |
| `opaque` | 普通不透明纹理，不允许透明或半透明。 |
| `double_sided` | 禁用背面剔除。 |
| `blend` | 用于染色玻璃等半透明纹理。 |
| `alpha_test` | 仅允许完全不透明或完全透明，并禁用背面剔除。 |
| `alpha_test_single_sided` | 仅允许完全不透明或完全透明，并启用背面剔除。 |
| `blend_to_opaque` | 近处按`blend`渲染，远处转为不透明。 |
| `alpha_test_to_opaque` | 近处按`alpha_test`渲染，远处转为不透明。 |
| `alpha_test_single_sided_to_opaque` | 近处按`alpha_test_single_sided`渲染，远处转为不透明。 |

## 内部或已弃用项

Microsoft Learn将下列项列为内部或已弃用项，说明其不适合作为自定义内容中的普通方块组件使用，或应改用较新的组件与脚本自定义组件机制。

| 项 | 状态 | 说明 |
| --- | --- | --- |
| `bone_visibility` | 内部/子结构 | 将几何体骨骼名映射到布尔值，控制指定骨骼是否可见。新内容通常在`minecraft:geometry.bone_visibility`中使用。 |
| `breathability` | 内部/已弃用 | 定义方块按`solid`还是`air`处理呼吸性；省略时默认按`solid`。 |
| `minecraft:custom_components` | 已弃用或旧式 | 旧式脚本自定义组件绑定列表。应以当前脚本API和官方自定义组件注册方式为准。 |
| `minecraft:queued_ticking` | 已弃用或旧式 | 旧式定时触发事件组件。新内容应优先使用`minecraft:tick`和脚本自定义组件事件。 |
| `minecraft:random_ticking` | 已弃用或旧式 | 旧式随机刻触发事件组件，受`randomTickSpeed`游戏规则影响。 |
| `minecraft:unit_cube` | 内部 | 指定使用单位立方体进行细分渲染。 |