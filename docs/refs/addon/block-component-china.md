# 方块组件（中国版）<!-- md:flag china -->

本页列出中国版行为包方块定义中`minecraft:block.components`对象可用的中国版专有方块组件，组件键使用`netease:`命名空间。这些组件由网易维护，仅在中国版中生效；国际版客户端将忽略或对这些组件发出警告。方块定义的根结构见[方块定义](block.md)，国际版方块组件见[方块组件](block-component.md)。

所有中国版专有方块组件均不需要开启任何实验性玩法。

## 组件一览

| 组件 | 值形态 | 默认值 | 用途与主要字段 |
| --- | --- | --- | --- |
| `netease:aabb` | 对象 | 未设置 | 自定义碰撞箱与射线检测箱。`collision`定义与实体碰撞的碰撞箱；`clip`定义准星选中和弹射物碰撞的射线检测箱。每个字段均可为包含`min`和`max`坐标三元数组的单一对象，或支持Molang条件的对象数组（每项含`enable`表达式、`min`和`max`，`enable`目前仅支持`query.is_connect`查询）。坐标范围：`min`各分量不小于`-1`，`max`各分量不大于`2`；有碰撞箱时`clip`范围应不超过`collision`范围，否则弹射物命中时可能出现异常。将`collision`每项均设为`0`可实现无碰撞方块。 |
| `netease:block_chest` | 对象 | 未设置 | 赋予方块完整的箱子界面与存储功能，使用该组件会自动创建方块实体。会覆盖`base_block`及其相关组件；不可与`netease:face_directional`共用；使用脚本API创建时须先将目标位置置为空气，再延迟调用创建。`chest_capacity`（必填，1~8行）控制容量，设置`can_pair`为`true`时容量自动限制为最大4行；`can_pair`（默认`false`）控制是否可与相邻同类方块组合为大箱子；`is_shulker_box`（默认`false`）控制是否为潜影盒模式（破坏时不掉落物品，不可与相邻箱子组合）；`mute`（默认`false`）控制是否关闭箱子开关音效；`can_be_blocked`（默认`false`）控制上方有阻挡方块时是否可打开箱子。 |
| `netease:block_entity` | 对象 | 未设置 | 赋予方块自定义方块实体。`tick`（默认`false`）为`true`时，方块每秒向服务端脚本发送20次`ServerBlockEntityTickEvent`事件；`client_tick`（默认`false`）为`true`时，方块每秒向客户端脚本发送20次`ModBlockEntityTickClientEvent`事件；`movable`（默认`true`）控制方块是否可被粘性活塞拉回。 |
| `netease:block_properties` | 对象 | 未设置 | 配置方块的特殊物理属性，多项可叠加使用。`properties`为字符串枚举数组：`piston_block_grabber`（被活塞推动时连带推动相邻方块）、`slime`（作为移动方块时修改对实体的力计算，用于模拟黏液块效果）、`breaks_when_fallen_on_by_heavy`（重力方块结束下落于该方块位置时此方块被破坏并产生掉落物；若碰撞箱边长因`netease:aabb`等缩小至约0.4以下则可能不会触发）。 |
| `netease:block_random_offset` | 对象 | 未设置 | 使方块视觉位置按方块坐标产生随机XZ偏移，实现类似原版花朵的随机摆动效果。`x_scope`与`z_scope`各为两元素浮点数数组，取值范围`0.0`~`1.0`，两值相同时为固定偏移。使用该组件后材质自动切换为透明，不可与`netease:render_layer`的`opaque`值共用；建议优先配合模型方块使用，普通贴图方块在相邻不透明方块时可能出现面裁剪渲染异常。 |
| `netease:connection` | 对象 | 未设置 | 定义方块与其他方块的连接关系，用于实现类似栅栏自动连接的逻辑。`blocks`为方块标识符数组，列出与该方块具有连接关系的方块。连接属性为单向：方块A连接方块B，但B不一定连接A。可配合`netease:aabb`数组形态，通过`query.is_connect(n)`（`n`为面索引：0=下、1=上、2=北、3=南、4=西、5=东）Molang查询获取连接状态，进而动态切换碰撞箱形态。 |
| `netease:custom_tips` | 对象 | 未设置 | 为该方块作为物品时添加自定义描述信息。`value`为描述字符串，支持格式化代码（如`§8`）。与自定义物品的`netease:customtips`作用相同。 |
| `netease:face_directional` | 对象 | 未设置 | 启用方块多面向放置功能，放置时自动依据玩家朝向旋转方块。`type`枚举：`direction`（四面向，仅水平四个方向）、`facing_direction`（六面向，含上方和下方）。不可与`netease:block_chest`共用。 |
| `netease:fire_resistant` | 对象 | 未设置 | 控制方块破坏后的掉落物是否免疫火焰和熔岩，效果与下界合金一致。`value`为布尔值；为`true`时掉落物不会被烧毁，掉入熔岩时会弹出。 |
| `netease:fuel` | 对象 | 未设置 | 允许该方块作为物品放入熔炉中充当燃料。`duration`为燃烧时长（秒，浮点数）；省略或设为`0`时无燃烧效果。 |
| `netease:listen_block_remove` | 对象 | 未设置 | 控制方块被移除时是否向服务端脚本发送`BlockRemoveServerEvent`事件。`value`为布尔值，默认`false`。 |
| `netease:may_place_on` | 对象 | 未设置 | 限制该方块只能放置和存在于特定方块上方。`block`为方块标识符数组，匹配这些方块的所有方块状态；`block_state`为方块状态描述符对象数组，仅匹配特定状态（多个独立状态组合需枚举所有排列组合）；可放置集合取两者并集。`spawn_resources`（默认`true`）控制下方方块变化导致该方块被破坏时是否产生掉落物。 |
| `netease:neighborchanged_sendto_script` | 对象 | 未设置 | 控制方块周围有方块发生变化时是否向服务端脚本发送`BlockNeighborChangedServerEvent`事件。`value`为布尔值，默认`false`。 |
| `netease:no_crop_face_block` | 空对象 | 未设置 | 使方块与相邻方块接触时不裁剪相邻面，实现类似原版树叶相邻不裁面的渲染效果。需配合`netease:render_layer`使用：`optionalAlpha`可实现原版叶子效果，`alpha`则超过一定距离后方块不再渲染。为避免相邻面变黑，通常还需将`minecraft:block_light_absorption`设为`0`。 |
| `netease:on_after_fall_on` | 空对象 | 未设置 | 启用方块接收"实体下落结束于该方块"事件的能力，主要用于力的计算逻辑。在实体完成下落后向服务端脚本发送相关事件。 |
| `netease:on_before_fall_on` | 空对象 | 未设置 | 启用方块接收"实体刚落至该方块"事件的能力，主要用于自定义下落伤害计算逻辑。在实体首次落地时向服务端脚本发送相关事件。 |
| `netease:on_entity_inside` | 空对象 | 未设置 | 启用方块在实体坐标所在位置存在该方块时持续触发事件的能力（依据方块格坐标判断是否"在方块内"，与方块碰撞箱大小无关）。持续向服务端脚本发送相关事件。 |
| `netease:on_stand_on` | 对象 | 未设置 | 启用方块接收"实体站在方块上"事件的能力。`send_python_event`为布尔值，控制是否向Python脚本发送事件。 |
| `netease:on_step_off` | 空对象 | 未设置 | 启用方块接收"实体刚离开该实心方块顶面"事件的能力。在实体离开时向服务端脚本发送相关事件。 |
| `netease:on_step_on` | 空对象 | 未设置 | 启用方块接收"实体刚移动至该实心方块顶面"事件的能力。在实体踏上时向服务端脚本发送相关事件。 |
| `netease:pathable` | 对象 | `true` | 控制游戏AI寻路时对该方块的处理方式。`value`为布尔值：`true`时AI将该方块视为空气，寻路路径可经过方块内部；`false`时视为障碍物，AI可在其上方行走但不可穿过。 |
| `netease:random_tick` | 对象 | 未设置 | 控制方块是否响应随机刻，以及随机刻时是否通知脚本。`enable`（默认`false`）控制是否启用随机刻；`tick_to_script`（默认`false`）为`true`时在随机刻触发时向服务端脚本发送`BlockRandomTickServerEvent`事件。 |
| `netease:redstone` | 对象 | 未设置 | 配置方块为自定义红石源或红石机械元件。`type`枚举：`producer`（红石源，主动产生红石信号）或`consumer`（红石机械元件，接收红石信号并可传播）。`strength`为初始信号强度整数（0~15，默认`15`）。 |
| `netease:redstone_property` | 对象 | 未设置 | 控制方块与活塞的特殊交互方式。`value`目前仅支持`break_on_push`：设置后方块被活塞推动时会被破坏并产生掉落物，而非被活塞移动推走。未设置该组件时方块被活塞正常推动。 |
| `netease:render_layer` | 对象 | `opaque` | 设置方块渲染所使用的材质类型。`value`枚举：`opaque`（不透明，对应`terrain_opaque`材质，默认值）、`alpha`（全透明，对应`terrain_alpha`材质，用于异形方块，超过一定距离将不渲染；与不透明方块相邻时可能出现闪烁，可配合`netease:no_crop_face_block`缓解）、`blend`（半透明，对应`terrain_blend`材质，用于彩色玻璃等半透明效果）、`optionalAlpha`（局部透明，与`alpha`不同之处在于不因距离而停止渲染，可配合`netease:no_crop_face_block`实现原版叶子效果）。 |
| `netease:solid` | 对象 | `true` | 控制方块是否被视为实心方块，影响实体在方块内时是否受到窒息伤害。`value`为布尔值：`true`（默认）时实体在方块内受到窒息伤害；`false`时不受窒息伤害。注意：使用该组件后方块不会投射阴影。 |
| `netease:tier` | 对象 | 未设置 | 设置方块的工具品质要求，控制特定工具的开采速度加成与掉落物条件。`digger`（必填）指定适用工具类型：`shovel`（铲）、`pickaxe`（镐）、`hatchet`（斧）。`destroy_special`（默认`false`）为`true`时，仅使用`digger`指定工具开采才产生掉落物。`level`（默认`0`）仅在`destroy_special`为`true`时生效，设定产生掉落物所需的最低工具品质等级（`0`=木制/金制/徒手，`1`=石制，`2`=铁制，`3`=钻石）。 |
