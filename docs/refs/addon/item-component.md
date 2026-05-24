# 物品组件

**物品组件（Item Component）**是行为包物品定义中位于`minecraft:item.components`对象内的键值项，用于声明物品的堆叠、耐久、使用、放置、食物、弹射物、穿戴、存储和界面表现等行为。组件键通常使用`minecraft:`命名空间，组件值可以是布尔值、数值、字符串、对象或数组，具体形态由组件本身决定。

本页列出官方物品组件参考中适合自定义物品使用的组件、主要字段、依赖关系和已弃用项。物品定义的根结构见[物品定义](item.md)。

## `description`

`description`不是`components`内的组件，但它与组件共同构成`minecraft:item`对象。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 物品的赋命名空间标识符。自定义物品不得使用`minecraft`命名空间；除非确实是在覆盖原版物品。 |
| `menu_category` | 对象 | 未设置 | 控制创造模式物品栏分类、物品组和命令可见性。 |

### `menu_category`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `category` | 字符串 | `items` | 创造模式分类。官方资料列出`construction`、`nature`、`equipment`、`items`和`none`。 |
| `group` | 字符串 | 未设置 | 创造模式物品组，例如`itemGroup.name.sword`、`itemGroup.name.pickaxe`或`itemGroup.name.miscFood`。组名长度最多256个字符。 |
| `is_hidden_in_commands` | 布尔值 | 未设置 | 是否在命令中隐藏该物品；未设置时命令默认可以使用该物品。 |

## 组件一览

| 组件 | 值形态 | 用途 | 主要字段与限制 |
| --- | --- | --- | --- |
| `minecraft:allow_off_hand` | 布尔值或对象 | 控制物品是否可放入副手槽位。 | 对象形态使用`value`布尔值。 |
| `minecraft:block_placer` | 对象 | 使物品使用时放置方块。 | 基础放置功能由`block`指定被放置方块，并可用`use_on`限制可使用方块；`aligned_placement`控制长按交互时是否对齐放置。Microsoft Learn说明，`replace_block_item`等默认方块物品联动能力在`1.21.40`及“Upcoming Creator Features”下可用；为真时该物品会注册为目标方块的默认物品，且物品标识符必须与方块标识符匹配。 |
| `minecraft:bundle_interaction` | 对象 | 启用收纳袋式交互方案和提示。 | <!-- md:flag experimental -->要求`format_version`不低于`1.21.40`；需要同时定义`minecraft:storage_item`；`num_viewable_slots`为可见槽位数，范围为1到64，默认值为12。 |
| `minecraft:can_destroy_in_creative` | 布尔值或对象 | 控制创造模式玩家是否能用该物品破坏方块。 | 对象形态使用`value`布尔值。 |
| `minecraft:compostable` | 对象 | 使物品可用于堆肥桶。 | 要求`format_version`不低于`1.21.60`；`composting_chance`为产生一层堆肥的概率。 |
| `minecraft:cooldown` | 对象 | 为物品动作添加冷却。 | `category`用于把多个物品归入同一冷却组；`duration`为冷却秒数；`type`为触发冷却的动作类型，默认值为`use`。 |
| `minecraft:damage` | 整数或对象 | 增加物品攻击造成的额外伤害。 | 对象形态使用`value`整数。该值会加到基础徒手伤害之上。 |
| `minecraft:damage_absorption` | 对象 | 使穿戴中的物品吸收本应作用于穿戴者的伤害。 | 物品需要装备在盔甲槽位，并需要`minecraft:durability`；`absorbable_causes`列出可吸收的伤害原因。 |
| `minecraft:digger` | 对象 | 将物品配置为工具，使其更快破坏指定方块。 | `destroy_speeds`列出方块匹配项和开采速度；`use_efficiency`为真时效率魔咒会提高开采速度。 |
| `minecraft:display_name` | 对象 | 设置物品显示名。 | `value`可写直接文本，也可写本地化键。 |
| `minecraft:durability` | 对象 | 设置物品耐久，并允许在铁砧、砂轮或工作台中合并。 | `max_durability`为最大耐久；`damage_chance`为损耗耐久的概率范围，默认最小值与最大值均为100。 |
| `minecraft:durability_sensor` | 对象 | 在物品受到耐久损耗并达到阈值时发出效果。 | 需要`minecraft:durability`；`durability_thresholds`至少包含1项；当多个阈值同时满足时，只考虑受损后耐久值最低的阈值；`sound_event`可设置阈值达成音效。 |
| `minecraft:dyeable` | 对象 | 使物品可像皮革盔甲一样在合成网格中染色。 | 要求`format_version`不低于`1.21.30`；`default_color`为未染色时颜色，可写字符串或RGB数组。 |
| `minecraft:enchantable` | 对象 | 定义物品可应用的魔咒槽位和附魔值。 | `slot`可使用`none`、`all`、`sword`、`bow`、`spear`、`crossbow`、`axe`、`pickaxe`、`shovel`、`hoe`、`shears`、`shield`、`fishing_rod`、`elytra`、`armor_head`、`armor_torso`、`armor_legs`、`armor_feet`等槽位；`value`为魔咒值，最小为0。 |
| `minecraft:entity_placer` | 对象 | 使物品可在世界中放置实体。 | `entity`指定被放置实体；`use_on`限制玩家使用时可放置的方块；`dispense_on`限制发射器可放置的方块。`use_on`和`dispense_on`可以使用字符串或方块描述符对象。 |
| `minecraft:fire_resistant` | 布尔值或对象 | 控制掉落物是否免疫火和熔岩燃烧。 | 对象形态使用`value`布尔值，默认值为`true`。 |
| `minecraft:food` | 对象 | 使物品可被玩家食用。 | 需要配合`minecraft:use_modifiers`才能正常工作；`nutrition`增加饥饿值；`saturation_modifier`参与饱和度计算；`can_always_eat`允许满饥饿时食用；`using_converts_to`设置食用后转换为的物品；`remove_effects`已弃用且在较新版本中不再工作。 |
| `minecraft:fuel` | 数值或对象 | 使物品可作为熔炉燃料。 | 对象形态使用`duration`，单位为秒，值必须不小于0.05。 |
| `minecraft:glint` | 布尔值或对象 | 控制物品是否显示附魔光效。 | 对象形态使用`value`布尔值。 |
| `minecraft:hand_equipped` | 布尔值或对象 | 控制物品在玩家手中是否按工具方式渲染。 | 对象形态使用`value`布尔值。官方还存在拼写错误的`minecraft:hand_equippped`页面，其语义与本组件相同，不应作为新组件名使用。 |
| `minecraft:hover_text_color` | 字符串或对象 | 设置鼠标悬停时物品名的颜色。 | 对象形态使用`value`字符串。 |
| `minecraft:icon` | 字符串或对象 | 设置物品在界面等位置使用的图标。 | 字符串形态直接写纹理键；对象形态优先使用`textures.default`等映射。旧字段`texture`仍可见于示例，但官方已标注为已弃用。`minecraft:block_placer`也可用目标方块渲染图标。 |
| `minecraft:interact_button` | 布尔值或字符串 | 控制触摸控制中的交互按钮是否显示及其文本。 | 值为`true`时显示默认“使用物品”文本；字符串值可指定按钮文本。 |
| `minecraft:kinetic_weapon` | 对象 | 使物品在使用期间沿使用者视线方向造成动能伤害和相关效果。 | `delay`为开始生效前的刻数；`reach`和`creative_reach`为命中距离范围；`hitbox_margin`为射线检测容差；`damage_multiplier`和`damage_modifier`参与伤害计算；`damage_conditions`、`knockback_conditions`和`dismount_conditions`分别控制伤害、击退和卸下骑手的条件。 |
| `minecraft:liquid_clipped` | 布尔值或对象 | 控制物品使用时是否与液体方块交互。 | 对象形态使用`value`布尔值。若要允许方块放置在液体上，应同时关注方块的放置过滤相关组件。 |
| `minecraft:max_stack_size` | 整数或对象 | 设置物品最大堆叠数量。 | 对象形态使用`value`整数，默认值为64。若可穿戴物品选择非手部槽位，最大堆叠通常会变为1。 |
| `minecraft:piercing_weapon` | 对象 | 使物品沿使用者视线方向对直线上的实体造成伤害。 | 该攻击动作优先于破坏方块，因此带有此组件的物品不能破坏方块；`reach`和`creative_reach`控制距离范围；`hitbox_margin`控制检测容差。 |
| `minecraft:projectile` | 对象 | 将物品定义为可被发射器射出或可作为弹药生成实体的弹射物。 | `projectile_entity`指定被发射的实体；`minimum_critical_power`控制暴击所需蓄力。与`minecraft:throwable`配合时，决定投掷后生成的实体。 |
| `minecraft:rarity` | 字符串或对象 | 设置基础稀有度，并影响悬停名称颜色。 | 要求`format_version`不低于`1.21.30`；可选值为`common`、`uncommon`、`rare`和`epic`。附魔会自动提高显示稀有度：普通或罕见物品提高为稀有，稀有物品提高为史诗。 |
| `minecraft:record` | 对象 | 使物品可作为唱片播放音乐。 | `sound_event`为播放的声音事件；`duration`为秒数；`comparator_signal`为唱片机比较器输出强度，范围通常为1到13。 |
| `minecraft:repairable` | 对象 | 定义可用于修复该物品的物品及恢复耐久。 | `repair_items`为修复项列表；每项包含可用物品列表和可选的`repair_amount`。 |
| `minecraft:seed` | 对象 | 使物品可作为种子种植并放置作物方块。 | 要求`format_version`不低于`1.10.0`；`crop_result`为种植后放置的方块；`plant_at`为可种植或可附着的方块。`plant_at_any_solid_surface`和`plant_at_face`已弃用。 |
| `minecraft:shooter` | 对象 | 使物品像弓或弩一样发射弹射物。 | 需要`minecraft:use_modifiers`；弹药物品需要`minecraft:projectile`；`ammunition`列出可用弹药；`charge_on_draw`控制是否拉动即蓄力；`max_draw_duration`和`scale_power_by_draw_duration`控制蓄力时长与发射力度。 |
| `minecraft:should_despawn` | 布尔值或对象 | 控制物品实体是否会自然消失。 | 对象形态使用`value`布尔值。 |
| `minecraft:stacked_by_data` | 布尔值或对象 | 控制附加值不同的同类物品是否可堆叠，也影响世界中的物品实体是否可合并。 | 对象形态使用`value`布尔值。 |
| `minecraft:storage_item` | 对象 | 使物品保存与其关联的动态容器数据。 | <!-- md:flag experimental -->要求`format_version`不低于`1.21.40`；若要与存储容器交互，需要`minecraft:bundle_interaction`；`allow_nested_storage_items`控制是否允许嵌套存储物品；`allowed_items`和`banned_items`限制可存入物品；`max_slots`最大为64。 |
| `minecraft:storage_weight_limit` | 对象 | 设置存储物品可容纳的最大重量。 | `max_weight_limit`默认值为64，最大值为64。 |
| `minecraft:storage_weight_modifier` | 对象 | 设置该物品放入其他存储物品时占用的重量。 | `weight_in_storage_item`默认值为4；值为0表示该物品在存储物品中不占重量。 |
| `minecraft:swing_duration` | 数值或对象 | 设置开采或攻击时挥动动画的持续时间。 | 对象形态使用`value`秒数；只影响视觉表现，不改变攻击频率或其他玩法机制。 |
| `minecraft:swing_sounds` | 对象 | 覆盖使用者挥动时发出的声音。 | `attack_hit`、`attack_miss`和`attack_critical_hit`分别设置命中、未命中和暴击命中声音事件。 |
| `minecraft:tags` | 对象 | 为物品附加标签。 | `tags`为字符串数组。自定义标签应使用自己的命名空间；只有原版标签可使用`minecraft:`命名空间。 |
| `minecraft:throwable` | 对象 | 使物品可像雪球或末影珍珠一样被玩家投掷。 | 常与`minecraft:projectile`配合；`do_swing_animation`控制投掷时是否挥手；`min_draw_duration`、`max_draw_duration`、`scale_power_by_draw_duration`、`launch_power_scale`和`max_launch_power`控制蓄力与发射力度。 |
| `minecraft:use_animation` | 字符串或对象 | 指定玩家使用物品时播放的动画。 | 对象形态使用`value`字符串，例如食物常用`eat`。 |
| `minecraft:use_modifiers` | 对象 | 设置物品使用时长、移动速度和开始使用行为。 | `use_duration`为使用时长秒数；`movement_modifier`为使用中移动速度倍率，必须不大于1；`emit_vibrations`控制开始或停止使用时是否发出振动；`start_sound`为开始使用声音；`start_using`可为`if_first`或`always`。 |
| `minecraft:wearable` | 对象 | 使物品可被玩家穿戴到装备槽位。 | `slot`指定槽位；`protection`为保护值；`hides_player_location`控制是否在定位器地图和定位器栏中隐藏玩家位置；`dispensable`控制是否可由发射器装备。 |

## 方块描述符

`minecraft:block_placer`、`minecraft:entity_placer`以及部分子结构使用方块描述符限制“可使用于”或“可发射于”的方块。方块描述符可以写为简单字符串，也可以写为对象。

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `name` | 字符串 | 方块标识符。 |
| `states` | 对象、字符串、整数或布尔值 | 方块状态条件。 |
| `tags` | 字符串 | 方块标签条件。 |

## 阈值与条件子结构

| 子结构 | 所属组件 | 字段 | 描述 |
| --- | --- | --- | --- |
| 耐久阈值 | `minecraft:durability_sensor.durability_thresholds` | `durability`、`particle_type`、`sound_event` | 当受损后耐久小于或等于`durability`时发出粒子和声音。官方参考列出了粒子类型与声音事件的大型枚举。 |
| 动能效果条件 | `minecraft:kinetic_weapon` | `min_speed`、`min_relative_speed`、`max_duration` | 控制动能武器的伤害、击退或卸下骑手效果何时生效。速度按使用者视线方向投影计算；`max_duration`为`delay`结束后仍允许生效的刻数，`-1`表示不限制。 |

## 已弃用或不宜使用的项

| 项 | 官方状态 | 说明 |
| --- | --- | --- |
| `minecraft:chargeable` | 已弃用 | 旧式“使用完成时触发事件”组件，已不再用于最新版Minecraft。 |
| `minecraft:custom_components` | 已弃用 | 旧式脚本自定义组件声明项，已不再用于最新版Minecraft。 |
| `minecraft:render_offsets` | 已弃用 | 旧式手持渲染偏移组件，已不再用于最新版Minecraft。 |
| `minecraft:use_duration` | 已弃用 | 旧式使用时长组件；新内容应使用`minecraft:use_modifiers.use_duration`。 |
| `minecraft:weapon` | 已弃用 | 原版武器会自动拥有该旧组件；自定义武器应使用`minecraft:damage`、`minecraft:cooldown`和`minecraft:durability`等组件组合。 |
| `minecraft:hand_equippped` | 拼写异常 | 官方资料存在三重`p`拼写页面，但标准组件名为`minecraft:hand_equipped`。 |
| `minecraft:item`、`minecraft:item_v1_21_90`、`minecraft:item_v1_26_0` | 根定义页 | 这些页面描述物品定义根对象和组件集合，不是可放入`components`中的普通组件。 |

## 使用建议

- 一个物品同时拥有多种使用行为时，应优先避免互相竞争的组件组合。尤其是放置方块、放置实体、食用、投掷、射击和穿戴等行为可能争用同一次使用输入。
- 新物品应优先使用`minecraft:use_modifiers`描述使用时长；不应继续使用已弃用的`minecraft:use_duration`组件。
- 实验性存储类组件需要满足版本、纹理和组件依赖。收纳袋式物品通常至少同时需要`minecraft:storage_item`、`minecraft:bundle_interaction`和对应资源包图标纹理。
- 当组件字段接受方块、物品、实体、声音或粒子标识符时，应使用与当前包内容和目标游戏版本一致的标识符；不存在的标识符通常会导致内容日志报错或运行时无效。