---
标题: 区块格式历史
描述: 每个 Minecraft 版本中数据驱动区块格式的所有更改列表。
分类: 文档
大纲深度: 2
提及:
    - QuazChick
---

## 1.21.50

### 组件

<Label color="green">版本化</Label>

-   更新了 `minecraft:destructible_by_mining`
    -   从实验性功能中发布了 `item_specific_speeds` 参数

## 1.21.40

### 组件

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:redstone_conductivity`

## 1.21.30

### 组件

<Tag name="experimental" />
<Label color="blue">即将推出的创作者功能</Label>

-   更新了 `minecraft:destructible_by_mining`
    -   添加了 `item_specific_speeds`，用于确定数组中每个 `item` 描述符的 `destroy_speed`。
-   添加了 `minecraft:redstone_conductivity`
    -   包含 `redstone_conductor`，用于确定此区块是否导红石。
    -   包含 `allows_wire_to_step_down`，用于确定红石线是否可以沿此区块的侧面向下传输。

## 1.21.10

### 组件

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:custom_components`
-   从实验性功能中发布了 `minecraft:entity_fall_on`
-   从实验性功能中发布了 `minecraft:tick`

## 1.20.80

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   移除了 `events`

### 组件

<Tag name="experimental" />
<Label color="yellow">测试版 API</Label>

-   添加了 `minecraft:custom_components`
    -   列出了应该应用于此区块的所有自定义组件。
-   添加了 `minecraft:entity_fall_on`
    -   包含 `min_fall_distance`，用于确定实体必须坠落的最小距离以触发实体坠落事件。
-   将 `minecraft:queued_ticking` 重命名为 `minecraft:tick`
    -   移除了 `on_tick` 参数

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   移除了 `minecraft:on_fall_on` 触发器
-   移除了 `minecraft:on_interact` 触发器
-   移除了 `minecraft:on_placed` 触发器
-   移除了 `minecraft:on_player_destroyed` 触发器
-   移除了 `minecraft:on_player_placing` 触发器
-   移除了 `minecraft:on_step_off` 触发器
-   移除了 `minecraft:on_step_on` 触发器
-   移除了 `minecraft:random_ticking` 触发器

### 事件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   移除了 `add_mob_effect` 响应
-   移除了 `damage` 响应
-   移除了 `decrement_stack` 响应
-   移除了 `die` 响应
-   移除了 `play_effect` 响应
-   移除了 `play_sound` 响应
-   移除了 `remove_mob_effect` 响应
-   移除了 `run_command` 响应
-   移除了 `set_block` 响应
-   移除了 `set_block_at_pos` 响应
-   移除了 `set_block_state` 响应
-   移除了 `spawn_loot` 响应
-   移除了 `swing` 响应
-   移除了 `teleport` 响应
-   移除了 `transform` 响应
-   移除了 `trigger` 响应

## 1.20.60

### 组件

-   更新了 `minecraft:geometry`
    -   添加了 `culling` 参数，用于确定应用于此区块模型的剔除规则。

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   移除了 `minecraft:unit_cube`

## 1.20.20

### 描述

-   从实验性功能中发布了 `traits`

#### Traits

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:placement_direction`
-   从实验性功能中发布了 `minecraft:placement_position`

## 1.20.10

### 描述

-   将 `properties` 重命名为 `states`

### 组件

-   更新了 `minecraft:geometry`
    -   为 `bone_visibility` 条目添加了 Molang 排列条件支持。

### 事件

<Tag name="experimental" />
<Label color="blue">即将推出的创作者功能</Label>

-   将 `set_block_property` 响应重命名为 `set_block_state`

## 1.20.0

### 描述

<Tag name="experimental" />
<Label color="blue">即将推出的创作者功能</Label>

-   添加了 `traits`
    -   区块 traits 是创作者添加原版状态和值设置器到数据驱动区块的快捷方式。

#### Traits

-   添加了 `minecraft:placement_direction`
    -   可以启用 `minecraft:cardinal_direction` 和 `minecraft:facing_direction` 状态。
-   添加了 `minecraft:placement_position`
    -   可以启用 `minecraft:block_face` 和 `minecraft:vertical_half` 状态。

## 1.19.80

### 组件

<Label color="green">版本化</Label>

-   添加了 `minecraft:transformation`
    -   包含 `rotation`、`scale` 和 `translation`，用于确定区块模型和碰撞的变换。
-   更新了 `minecraft:geometry`
    -   添加了 `bone_visibility` 参数，用于根据布尔值确定骨骼的立方体是否可见。

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   移除了 `minecraft:part_visibility`

## 1.19.70

### 描述

-   从实验性功能中发布了 `properties`

### 排列

-   从实验性功能中发布
-   如果 `condition` 参数不是有效的 Molang 排列条件，区块将无法加载。

## 1.19.60

### 组件

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:display_name`
-   从实验性功能中发布了 `minecraft:placement_filter`
-   从实验性功能中发布了 `minecraft:selection_box`

## 1.19.50

### 组件

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:crafting_table`
-   从实验性功能中发布了 `minecraft:collision_box`

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   移除了 `minecraft:breathability`

## 1.19.40

### 描述

-   更新了 `menu_category`
    -   添加了 `is_hidden_in_commands` 参数，用于确定在使用命令时区块是否被视为无效。

### 组件

<Label color="green">版本化</Label>

-   从实验性功能中发布了 `minecraft:geometry`
-   从实验性功能中发布了 `minecraft:material_instances`
-   移除了 `minecraft:breathability`
-   将 `minecraft:block_light_filter` 重命名为 `minecraft:light_dampening`

## 1.19.30

### 描述

-   添加了 `menu_category`
    -   包含 `category`，用于确定区块放置在哪个标签页中。
    -   包含 `group`，用于确定区块与哪些其他项目分组。

### 组件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   移除了 `minecraft:creative_category`
-   更新了 `minecraft:display_name`
    -   不再在给定的显示名称前添加 `tile.`，也不再在后面添加 `.name`。

## 1.19.20

### 组件

<Label color="green">版本化</Label>

-   将 `minecraft:block_light_emission` 重命名为 `minecraft:light_emission`
    -   现在以整数光级（0-15）而非小数（0.0-1.0）确定发光量。
-   用 `minecraft:destructible_by_mining` 替换了 `minecraft:destroy_time`
    -   设置为 `false` 可防止通过挖掘破坏区块。
    -   设置为 `true` 允许立即通过挖掘破坏区块。
    -   设置为对象则允许确定 `seconds_to_destroy`。
-   用 `minecraft:destructible_by_explosion` 替换了 `minecraft:explosion_resistance`
    -   设置为 `false` 可防止通过爆炸破坏区块。
    -   设置为 `true` 则允许通过爆炸轻松破坏区块。
    -   设置为对象则允许确定 `explosion_resistance`。
-   `minecraft:friction` 的值现在代表运动阻力而非运动。

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   移除了 `minecraft:unwalkable`
-   将 `minecraft:aim_collision` 重命名为 `minecraft:selection_box`

## 1.19.10

### 组件

<Label color="green">版本化</Label>

-   将 `minecraft:block_light_filter` 重命名为 `minecraft:light_dampening`
-   更新了 `minecraft:flammable`
    -   现在可以设置为布尔值，`false` 表示区块不可燃，`true` 使用默认的可燃值。
    -   将 `flame_odds` 参数重命名为 `catch_chance_modifier`
    -   将 `burn_odds` 参数重命名为 `destroy_chance_modifier`

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   将 `minecraft:block_collision` 重命名为 `minecraft:collision_box`
-   更新了 `minecraft:crafting_table`
    -   将 `custom_description` 参数重命名为 `table_name`
    -   移除了 `grid_size` 参数
-   将 `minecraft:ticking` 重命名为 `minecraft:queued_ticking`
    -   将 `range` 参数替换为 `interval_range`，现在以刻（ticks）而非秒来衡量。

<Tag name="experimental" />
<Label color="blue">即将推出的创作者功能</Label>

-   更新了 `minecraft:part_visibility`
    -   将 `rules` 参数重命名为 `conditions`

## 1.18.30

### 组件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   移除了 `minecraft:breakonpush`
-   移除了 `minecraft:immovable`
-   移除了 `minecraft:onlypistonpush`
-   移除了 `minecraft:preventsjumping`

## 1.18.10

### 组件

<Label color="green">版本化</Label>

-   将 `minecraft:block_light_absorption` 重命名为 `minecraft:block_light_filter`

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   将 `minecraft:entity_collision` 重命名为 `minecraft:block_collision`
-   将 `minecraft:pick_collision` 重命名为 `minecraft:aim_collision`

## 1.18.0

### 组件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   添加了 `minecraft:crafting_table`
    -   包含 `crafting_tags`，用于确定支持哪些标签的配方。
    -   包含 `custom_description`，将在 UI 中显示而非 "Crafting Table"。
    -   包含 `grid_size`，用于确定配方网格的横向和纵向槽位数量。唯一支持的值为 `3`。

## 1.17.30

### 组件

<Tag name="experimental" />
<Label color="blue">即将推出的创作者功能</Label>

-   添加了 `minecraft:part_visibility`
    -   根据 Molang 排列条件确定模型中骨骼的直接子级是否可见。

## 1.17.20

### 组件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   添加了 `minecraft:creative_category`
    -   确定此区块在创意菜单中的显示位置。

## 1.16.210

### 事件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>

-   更新了 `decrement_stack` 响应
    -   添加了 `ignore_game_mode` 参数，用于确定玩家处于创造模式时是否会减少堆叠。

## 1.16.100

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   添加了 `events`

### 描述

-   移除了 `is_experimental`
-   移除了 `register_to_creative_menu`

### 组件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   添加了 `minecraft:breakonpush`
    -   确定此区块在活塞尝试推动时是否会破坏。
-   添加了 `minecraft:breathability`
    -   确定区块是导致窒息（`solid`）还是可呼吸的（`air`）。
-   添加了 `minecraft:display_name`
    -   确定此区块的本地化 ID，将以 `tile.<id>.name` 格式使用。
-   添加了 `minecraft:entity_collision`
    -   确定此区块的实体碰撞盒。
    -   可以设置为 `false` 以完全移除碰撞。
    -   包含 `origin`，用于确定盒子的起始位置。
    -   包含 `size`，用于确定从 `origin` 开始的盒子尺寸。
-   添加了 `minecraft:geometry`
    -   定义此区块应使用的模型的几何标识符。
-   添加了 `minecraft:immovable`
    -   确定此区块是否可被活塞移动。
-   添加了 `minecraft:material_instances`
    -   包含与 `minecraft:geometry` 或 `minecraft:unit_cube` 组件一起使用的渲染配置。
-   添加了 `minecraft:on_fall_on` 触发器
-   添加了 `minecraft:on_interact` 触发器
-   添加了 `minecraft:on_placed` 触发器
-   添加了 `minecraft:on_player_destroyed` 触发器
-   添加了 `minecraft:on_player_placing` 触发器
-   添加了 `minecraft:on_step_off` 触发器
-   添加了 `minecraft:on_step_on` 触发器
-   添加了 `minecraft:onlypistonpush`
    -   确定此区块是否只能被活塞推动，而不能被粘性活塞拉动。
-   添加了 `minecraft:pick_collision`
    -   确定玩家选择此区块的边界。
    -   可以设置为 `false` 以完全移除碰撞。
    -   包含 `origin`，用于确定盒子的起始位置。
    -   包含 `size`，用于确定从 `origin` 开始的盒子尺寸。
-   添加了 `minecraft:placement_filter`
    -   确定玩家可以放置区块且不会弹出的地方。
    -   包含至少一个必须匹配的 `conditions`。
    -   每个条件可能包含 `allowed_faces` 和/或 `block_filter`。
-   添加了 `minecraft:preventsjumping`
    -   确定实体在此区块上时是否具有有限的跳跃能力。
-   添加了 `minecraft:random_ticking` 触发器
-   添加了 `minecraft:rotation`
    -   以轴对齐角度旋转此区块的碰撞盒和模型。
-   添加了 `minecraft:ticking`
    -   确定此区块将以多长时间间隔刻（tick）更新一次，并保存待处理的刻数据。
    -   包含 `looping`，用于确定是否无限期地继续刻动。
    -   包含 `range`，用于确定间隔的随机延迟。
    -   包含 `on_tick`，可在此区块刻动时触发事件。
-   添加了 `minecraft:unit_cube`
    -   使此区块显示为全尺寸单位区块。
-   添加了 `minecraft:unwalkable`
    -   确定实体是否应避免在此区块上行走。

### 事件

<Tag name="experimental" />
<Label color="red">节日创作者功能</Label>
<Label color="green">版本化</Label>

-   添加了 `add_mob_effect` 响应
-   添加了 `damage` 响应
-   添加了 `decrement_stack` 响应
-   添加了 `die` 响应
-   添加了 `play_effect` 响应
-   添加了 `play_sound` 响应
-   添加了 `remove_mob_effect` 响应
-   添加了 `run_command` 响应
-   添加了 `set_block` 响应
-   添加了 `set_block_at_pos` 响应
-   添加了 `set_block_property` 响应
-   添加了 `spawn_loot` 响应
-   添加了 `swing` 响应
-   添加了 `teleport` 响应
-   添加了 `transform` 响应
-   添加了 `trigger` 响应

## 1.10.0

### 描述

-   添加了 `identifier`
    -   定义区块的标识符。命名空间不能为 `minecraft`。
-   添加了 `is_experimental`
    -   仅在世界设置中启用 "使用实验性游戏玩法" 切换时注册区块。
-   添加了 `register_to_creative_menu`
    -   使区块出现在创意菜单的 `Construction` 分类中。
    -   目前无法将自定义区块添加到配方书中。

### 组件

-   添加了 `minecraft:block_light_absorption`
    -   确定通过区块时将吸收多少光（以 0-15 的整数光级）。
-   添加了 `minecraft:block_light_emission`
    -   确定此区块发出的光量（以 0.0-1.0 的小数表示）。
-   添加了 `minecraft:destroy_time`
    -   确定在生存或冒险模式下挖掘此区块所需的时间。
-   添加了 `minecraft:explosion_resistance`
    -   确定此区块对爆炸的抵抗力。
-   添加了 `minecraft:flammable`
    -   包含 `burn_odds`，用于确定此区块在着火时被销毁的可能性。
    -   包含 `flame_odds`，用于确定此区块在附近有火时着火的可能性。
-   添加了 `minecraft:friction`
    -   确定实体在此区块上的移动速度。
    -   注意，这不是阻力的衡量标准，与现代格式不同。
-   添加了 `minecraft:loot`
    -   确定此区块被销毁时掉落的战利品表的路径。
    -   如果使用的工具具有 `丝触` 附魔，则此组件将被忽略。
-   添加了 `minecraft:map_color`
    -   确定此区块在地图上的显示颜色。