---
title: 物品组件
description: 物品组件用于改变你的物品在世界中的外观和功能。
category: 综合
nav_order: 2
mentions:
    - SmokeyStack
    - QuazChick
---

/// tip | FORMAT & MIN ENGINE VERSION `1.21.40`
使用最新的格式版本创建自定义物品可以访问新的功能和改进。维基旨在分享关于自定义物品的最新信息，目前目标格式版本为 `1.21.40`。
///

## 应用组件

物品组件用于改变你的物品在世界中的外观和功能。它们被应用在 `minecraft:item` 的 `components` 子项中。

```json title="BP/items/custom_item.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:icon": {
                "textures": {
                    "default": "custom_item"
                }
            }
        }
    }
}
```

## 组件列表

### 允许副手

确定物品是否可以放置在物品栏的副手槽中。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:allow_off_hand": {
    "value": true
}
```

### 方块放置器

方块放置器物品组件。具有此组件的物品在使用时会放置方块。在格式版本 1.20.10 中从实验中发布。

在生存模式中使用时，物品将被消耗。

类型：对象

- `block`: 字符串/对象
    - 定义将被放置的方块。
- `use_on`: 数组
    - 包含此物品可用于的方块描述符的方块列表。如果留空，则允许所有方块。有关使用行为的更多信息，请参见 自定义物品使用优先级。
    - 这也适用于创造模式。

```json title="minecraft:item > components"
"minecraft:block_placer": {
    "block": "wiki:custom_block",
    "use_on": [
        "minecraft:dirt",
        "wiki:custom_dirt"
    ]
}
```

### 包裹交互

启用物品上的包裹界面和功能。
物品必须具有 `minecraft:storage_item` 组件才能使此组件生效。

_在格式版本 1.21.40 及更高版本中，`Bundles` 从实验中发布。_

类型：对象

- `num_viewable_slots`: 整数（1-64）
    - 定义从包裹顶部可访问的物品堆叠的最大数量。
    - 槽位按行从工具提示的底部从右到左填充访问。

```json title="minecraft:item > components"
"minecraft:bundle_interaction": {
    "num_viewable_slots": 12
}
```

### 创造模式中可破坏

确定物品在挥动时是否会在创造模式中破坏方块。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:can_destroy_in_creative": {
    "value": true
}
```

### 冷却

组件的冷却时间。使用后，所有在指定“冷却类别”中的物品将在组件中定义的确定时间内不可用。在格式版本 1.20.10 中从实验中发布。

需要 `minecraft:use_modifiers`。

类型：对象

- `category`: 字符串
    - 此物品的冷却类型。
- `duration`: 浮点数
    - 具有匹配类别的物品在再次可用之前将花费冷却时间（以秒为单位）。
    - 如果此值为负数，则物品不可用。

```json title="minecraft:item > components"
"minecraft:cooldown": {
    "category": "attack",
    "duration": 0.2
}
```

### 自定义组件

自定义组件是一种将 JSON 中块和物品的配置直接且有针对性地连接到脚本功能的新方法。这一新概念允许脚本功能在块和物品之间的可组合性和可重用性，同时确保脚本仅为特定的块和物品运行。

在 `1.21.10.23` 中添加。需要 `format_version: "1.21.10"` 或更高版本。

类型：数组

```json title="minecraft:item > components"
"minecraft:custom_component": [
    "wiki:custom_component"
]
```

### 伤害

确定物品在攻击时造成的额外伤害量。请注意，此值必须为正数。

根据文档，实体将实际受到 `value + 1` 的伤害，因为手/物品有默认的 1 点伤害。
伤害值为 `value % 256`。
使用有符号的 16 位整数。2 的补码创建负范围。
`[32768-65536]` - 被视为负数。物品的值将为 `(-32768-0)`。因此，负范围为 `[256*(256x+128) - 256*(256(x+1)))`，其中 `x` 是任意数。

https://bugs.mojang.com/browse/MCPE-180073

类型：整数

```json title="minecraft:item > components"
"minecraft:damage": {
    "value": 10
}
```

### 伤害吸收

使物品能够吸收原本会对其佩戴者造成的伤害。为此，物品需要具有耐久度组件并装备在护甲槽中。

类型：对象

- `absorbable_causes`: 数组
    - 可以被物品吸收的伤害原因列表（例如 `entity_attack` 和 `magma`）。

```json title="minecraft:item > components"
"minecraft:damage_absorption": {
	"absorbable_causes": ["all"]
}
```

### 掘掘者

确定物品挖掘特定方块的速度。

类型：对象

- `destroy_speeds`: 对象
    - 要挖掘的方块列表，以及相应的挖掘速度。
    - `block`: 字符串/对象
        - 物品将摧毁的方块。
            - `tags`: 字符串
                - Molang 查询
    - `speed`: 整数
        - 方块被摧毁的速度。
        - 可以为负值。如果为负，物品将无法摧毁该方块。
- `use_efficiency`: 布尔值
    - 确定如果物品应用了 `效率` 附魔，物品是否应该受到影响。
    - 似乎不起作用。

```json title="minecraft:item > components"
"minecraft:digger": {
	"use_efficiency": true,
	"destroy_speeds": [
		{
			"block": {
				"tags": "q.any_tag('stone', 'metal')" // 注意并非所有方块都有标签；可能需要列出许多方块
			},
			"speed": 6
		}
	]
}
```

### 显示名称

定义当显示物品名称时显示的文本，例如悬停文本。在格式版本 1.20.0 中从实验中发布。

不支持换行转义字符

类型：字符串

#### 示例

```json title="minecraft:item > components"
"minecraft:display_name": {
    "value": "secret_weapon"
}
```

#### 使用本地化键的示例

```json title="minecraft:item > components"
"minecraft:display_name": {
    "value": "item.snowball.name"
}
```

### 耐久度

确定物品在破损前可以承受多少伤害，并允许物品在合成中被合并。在格式版本 1.20.0 中从实验中发布。

耐久度在挖掘方块时不会隐式地损坏自身。必须通过 ScriptAPI 处理。然而，在对致命生物造成伤害时会隐式地损坏自身。
每次对生物造成伤害时，耐久度减少 2。这与武器的原版属性不匹配，但与工具的原版属性相匹配。

当与 `minecraft:wearable` 一起使用时，用物品击打生物不会减少耐久度 2。相反，当装备并被实体击中时，耐久度会隐式减少 1。这与原版属性相匹配。

https://bugs.mojang.com/browse/MCPE-180112

类型：对象

- `damage_chance`: 对象
    - 伤害几率是此物品失去耐久度的百分比几率。默认值设置为 100。定义为具有最小和最大值的 int 范围。
    - `min`: 整数
        - 耐久度受损的最低几率。范围：[0, 100]。
    - `max`: 整数
        - 耐久度受损的最高几率。范围：[0, 100]。
- `max_durability`: 整数
    - 最大耐久度是此物品在破碎前可以承受的伤害量。这是一个必填参数，最小值为 0。
    - 使用有符号的 16 位整数。2 的补码创建负范围。`[32768-65536]` - 被视为负数。物品的值将为 `(-32768-0)`。因此，负范围为 `[256*(256x+128) - 256*(256(x+1)))`，其中 `x` 是任意数。
    - https://bugs.mojang.com/browse/MCPE-180112

#### 伤害几率

用于计算耐久度击破几率。

- 无耐久度击破 - 无论范围如何，100% 的时间
- 耐久度击破 I - 范围的 50%
- 耐久度击破 II - 范围的 33%
- 耐久度击破 III - 范围的 25%

最大值不能大于最小值

```json title="minecraft:item > components"
"minecraft:durability": {
    "damage_chance": {
        "min": 0,
        "max": 100
    },
    "max_durability": 100
}
```

### 耐久度传感器

在物品受到伤害时使其发出效果。

类型：对象

- `durability_thresholds`: 数组
    - 项目定义了耐久度阈值以及每个阈值达到时发出的效果。
    - 当多个阈值被满足时，仅考虑应用伤害后耐久度最低的阈值。

#### 耐久度阈值

类型：对象

- `durability`: 整数
    - 当物品耐久度值小于或等于此值时，将发出效果。
- `particle_type`: 字符串
    - 达到阈值时发出的粒子效果。
- `sound_event`: 字符串
    - 达到阈值时发出的声音效果。

```json title="minecraft:item > components"
"minecraft:durability_sensor": {
    "durability_thresholds": [
        {
            "durability": 100,
            "particle_type": "minecraft:explosion_manual",
            "sound_event": "blast"
        },
        {
            "durability": 5,
            "sound_event": "raid.horn"
        }
    ]
}
```

### 可染色

允许物品通过水槽中的水进行染色。染色后，物品将显示 `minecraft:icon` 组件中定义的 `dyed` 纹理，而不是 `default`。

类型：对象

- `default_color`: 字符串
    - 可选的默认颜色，在玩家尚未染色物品之前使用。

```json title="minecraft:item > components"
"minecraft:dyeable": {
	"default_color": "#ffffff"
}
```

### 可附魔

确定哪些附魔可以应用于物品。并非所有附魔都会对所有物品组件产生影响。

https://bugs.mojang.com/browse/MCPE-180331

类型：对象

- `slot`: 字符串
    - 可以应用哪些附魔（例如，使用 `bow` 将允许此物品像弓一样被附魔）。
    - 必填字段。
- `value`: 整数
    - 附魔的值（最小为 0）。
    - 必填字段
    - 值为 `value % 256`

#### 槽位

- armor_feet
- armor_torso
- armor_head
- armor_legs
- axe
- bow
- cosmetic_head
- crossbow
- elytra
- fishing_rod
- flintsteel
- hoe
- pickaxe
- shears
- shield
- shovel
- sword
- all

#### 可附魔值

确定物品的附魔性，影响潜在附魔的质量和数量。较高的值增加获得更强大附魔的机会。下表详细说明了不同材料的附魔性分数，展示了它们获得附魔的能力。

| 材料       | 护甲附魔性 | 剑/工具附魔性 |
| ---------- | ---------- | ------------- |
| 木材       | 不适用     | 15            |
| 皮革       | 15         | 不适用        |
| 石头       | 不适用     | 5             |
| 链甲       | 12         | 不适用        |
| 铁         | 9          | 14            |
| 黄金       | 25         | 22            |
| 钻石       | 10         | 10            |
| 海龟       | 9          | 不适用        |
| 下界合金   | 15         | 15            |
| 其他       | 1          | 1             |

有关附魔性及其对游戏影响的深入探讨，请参阅 [非官方Minecraft维基的附魔机制](https://minecraft.wiki/w/Enchanting_mechanics#Enchantability)。

```json title="minecraft:item > components"
"minecraft:enchantable": {
    "slot": "sword",
    "value": 10
}
```

### 实体放置器

允许物品将指定的实体放置到世界中。在格式版本 1.20.0 中从实验中发布。

类型：对象

- `dispense_on`: 数组
    - 物品可以被分配器放出的方块描述符的方块列表。如果留空，则允许所有方块。
    - 分配器的口必须指向空气方块或此数组中定义的方块。如果是空气方块，游戏将检查其下方的方块是否匹配此数组中定义的方块。
- `entity`: 字符串
    - 要放置在世界中的实体。
- `use_on`: 数组
    - 物品可以用于的方块描述符的方块列表。如果留空，则允许所有方块。有关使用行为的更多信息，请参见 自定义物品使用优先级。

```json title="minecraft:item > components"
    "minecraft:entity_placer": {
        "entity": "minecraft:spider",
        "dispense_on": [
            "minecraft:dirt"
        ],
        "use_on": [
            "minecraft:dirt"
        ]
    }
```

### 食物

当物品具有食物组件时，玩家可以食用它。必须拥有 `minecraft:use_modifiers` 组件才能正常运行。

在第三人称视角下，会隐式播放吃的动画。第一人称视角需要 `minecraft:use_animation`。

类型：对象

- `can_always_eat`: 布尔值
    - 如果为 `true`，即使不饿也可以一直食用此物品。
- `nutrition`: 整数
    - 使用此物品时添加到角色营养值的数值。
    - 可以为负值。
    - 最大值为 32 位整数限制。
- `saturation_modifier`: 浮点数
    - 饱和度修正用于以下公式：(nutrition * saturation_modifier * 2) 应用于饱和度增益。
    - 值必须大于 0。
- `using_converts_to`: 字符串
    - 使用时，转换为此字段中指定的物品。

```json title="minecraft:item > components"
"minecraft:food": {
    "can_always_eat": false,
    "nutrition": 3,
    "saturation_modifier": 0.6,
    "using_converts_to": "bowl"
}
```

### 燃料

允许物品作为熔炉中的燃料来“烹饪”其他物品。在格式版本 1.20.0 中从实验中发布。

最大值为 `107374180`，包括在内。这个数字的原因是当转换为刻时，它达到了 32 位整数限制。

类型：对象

- `duration`: 浮点数
    - 此燃料烹饪物品的持续时间（以秒为单位）。最小值：0.05。

```json title="minecraft:item > components"
"minecraft:fuel": {
    "duration": 3.0
}
```

### 闪光

确定物品是否具有附魔闪光渲染效果。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:glint": {
    "value": false
}
```

### 手持装备

确定物品在手中时是否像工具一样渲染。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:hand_equipped": {
    "value": true
}
```

### 悬停文本颜色

确定悬停物品时物品名称的颜色。

有效颜色可以在这里找到：https://minecraft.wiki/w/Formatting_codes#Color_codes

类型：字符串

```json title="minecraft:item > components"
"minecraft:hover_text_color": "minecoin_gold"
```

### 图标

确定用于在UI和其他地方代表物品的图标。在格式版本 1.20.10 中从实验中发布。

类型：对象

- `textures`: 对象
    - 此映射包含可用于物品图标的不同纹理。`default` 将包含实际的图标纹理。此处还可以指定护甲饰边纹理和调色板。图标纹理是与纹理文件关联的 `resource_pack/textures/item_texture.json -> texture_data` 对象中的键。
        - `default`: 字符串
            - 物品的实际图标
        - `dyed`: 字符串
            - 物品在水槽中染色后使用的图标。
            - 仅在物品具有 `minecraft:dyeable` 组件时才可显示。
        - `icon_trim`: 字符串
            - 物品有饰边时的图标覆盖。
            - `icon_trim` 隐式回退到 `minecraft:wearable` 组件中的槽位类型。目前，仅当短名称与物品标识符匹配时，图标才会覆盖。尚不清楚这是一个错误还是功能。

```json title="minecraft:item > components"
"minecraft:icon":{
    "textures": {
        "default": "custom_item"
    }
}
```

### 交互按钮

此组件是布尔值或字符串，决定是否在触控控制中显示交互按钮以及按钮上显示的文本。当设置为 `true` 时，将使用默认的“使用物品”文本。

类型：布尔值/字符串

```json title="minecraft:item > components"
"minecraft:interact_button": "Use This Custom Item"
```

```json title="minecraft:item > components"
"minecraft:interact_button": {
    "value": true
}
```

### 液体剪切

确定物品在使用时是否与液体方块互动。

当与液体互动时，轮廓选择不能高亮显示液体下方的任何方块。互动发生在液体方块内部，而不是在其侧面。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:liquid_clipped": {
    "value": true
}
```

### 最大堆叠数量

确定可以堆叠在一起的物品数量。

类型：整数

```json title="minecraft:item > components"
"minecraft:max_stack_size": {
    "value": 64
}
```

### 投射物

投射物物品组件。投射物物品会射出，如箭矢。在格式版本 1.20.10 中从实验中发布。

类型：对象

- `minimum_critical_power`: 浮点数
    - 定义投射物需要充能的时间以进行致命一击。
- `projectile_entity`: 字符串
    - 作为投射物发射的实体。如果未指定命名空间，则假定为 `minecraft`。

```json title="minecraft:item > components"
"minecraft:projectile": {
    "minimum_critical_power": 1.25,
    "projectile_entity": "arrow"
}
```

### 稀有度

通过更改其名称文本的颜色来表示物品的获取难度。
如果同时应用了 `minecraft:hover_text_color`，此组件将被覆盖且无效。

物品的稀有度值将在被附魔时升级为 `rare`，如果其基础稀有度已经是 `rare`，则升级为 `epic`。
具有 `epic` 稀有度的物品在被附魔时保持不变。

类型：字符串

- `common` 结果为白色名称。
- `uncommon` 结果为黄色名称。
- `rare` 结果为青色名称。
- `epic` 结果为浅紫色名称。

```json title="minecraft:item > components"
"minecraft:rarity": "rare"
```

### 唱片

唱片物品组件允许物品在唱片机中使用时播放声音。

类型：对象

- `comparator_signal`: 整数
    - 比较器块使用的信号强度
    - 虽然此值可以是任何数字（甚至是负数！），但比较器信号仍然锁定在 [0, 15] 之间。
- `duration`: 浮点数
    - 声音事件的持续时间（以秒为单位）。
- `sound_event`: 字符串
    - 声音事件类型
    - 如果声音类型是任何原版音乐唱片，物品将具有艺术家名称的描述文本。在唱片机中播放时，玩家屏幕上会出现一个动作栏，描述正在播放的唱片。
    - 无论使用何种声音类型，物品的文本颜色都将像原版音乐唱片一样变为青色。
    - 仅允许原版声音事件。

```json title="minecraft:item > components"
"minecraft:record": {
    "comparator_signal": 1,
    "duration": 5,
    "sound_event": "ambient.tame"
}
```

#### 声音事件

可用声音列表见 [此处](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/itemreference/examples/itemcomponents/minecraft_record?view=minecraft-bedrock-stable)。

### 可修复

可修复物品组件：确定哪些物品可用于修复定义的物品，以及指定物品将修复的耐久度量。在格式版本 1.20.10 中从实验中发布。

默认情况下，它可以通过自身修复。它将合并两个耐久度。

类型：对象

- `repair_items`: 数组
    - 修复物品条目列表。
        - `repair_amount`: 整数/字符串
            - 修复的耐久度量
            - 字符串类型可以使用 Molang。使用 `context.other` 获取铁砧的第二个槽位。
        - `items`: 数组
            - 用于修复物品的物品
            - 必填字段

```json title="minecraft:item > components"
"minecraft:repairable":{
    "repair_items": [
        {
            "items":[
                "minecraft:diamond"
            ],
            "repair_amount": 10
        }
    ]
}
```

```json title="minecraft:item > components"
"minecraft:repairable":{
    "repair_items": [
        {
            "items":[
                "minecraft:diamond"
            ],
            "repair_amount": "math.random(1,10)"
        }
    ]
}
```

```json title="minecraft:item > components"
"minecraft:repairable":{
    "repair_items": [
        {
            "items":[
                "minecraft:diamond"
            ],
            "repair_amount": "math.min(q.remaining_durability + c.other->q.remaining_durability + math.floor(q.max_durability /20), c.other->q.max_durability)" // 原版公式
        }
    ]
}
```

### 射手

射手物品组件。必须拥有 `minecraft:use_modifiers` 组件才能正常运行。在格式版本 1.20.10 中从实验中发布。

类型：对象

- `ammunition`: 数组
    - `item`: 字符串
        - 表示物品描述符标识符。物品必须具有 `minecraft:projectile` 组件。
    - `use_offhand`: 布尔值
        - 设置为 `true` 时，可以从副手使用弹药。
    - `search_inventory`: 布尔值
        - 确定是否可以搜索物品栏以使用弹药。在生存模式中必须为 `true`。在创造模式中，如果 `use_in_creative` 为 `false`，则必须为 `true`。在创造模式中不会消耗弹药。
    - `use_in_creative`: 布尔值
        - 确定是否可以在创造模式中使用弹药。
- `charge_on_draw`: 布尔值
    - 设置物品在拉出时是否充能
    - 物品的 `minecraft:use_modifiers` -> `use_duration` 必须 >= `max_draw_duration`。
- `max_draw_duration`: 浮点数
    - 确定在自动释放前武器可以拉动的时间长度
- `scale_power_by_draw_duration`: 布尔值
    - 设置为 `true` 时，武器拉动的时间越长，释放时的力量越大

#### 弹药

设置用作弹药的实体。使用物品的优先级如下：首先，检查副手槽是否有匹配的弹药。如果匹配，则查看该物品是否设置了 `use_offhand`。如果副手没有匹配的物品，则按数组顺序遍历，无论物品栏顺序如何。

```json title="minecraft:item > components"
"minecraft:shooter": {
    "ammunition": [
        {
            "item": "custom_projectile",
            "use_offhand": true,
            "search_inventory": true,
            "use_in_creative": true
        }
    ],
    "max_draw_duration": 1.0,
    "scale_power_by_draw_duration": true,
    "charge_on_draw": false
}
```

### 应该消失

确定物品是否应在世界中漂浮时最终消失。

类型：布尔值

```json title="minecraft:item > components"
"minecraft:should_despawn": {
    "value": true
}
```

### 按数据堆叠

确定具有不同辅助值的相同物品是否可以堆叠。此外，定义物品在世界中漂浮时，物品行为者是否可以合并。

```json title="minecraft:item > components"
"minecraft:stacked_by_data": {
    "value": true
}
```

### 存储物品

允许物品充当容器并存储其他物品。
物品必须具有最大堆叠数量为1，才能使此组件生效。

_在格式版本 1.21.40 及更高版本中，`Bundles` 从实验中发布。_

类型：对象

- `allow_nested_storage_items`: 布尔值
    - 确定是否可以将其他存储物品放入容器中。
- `allowed_items`: 数组
    - 定义仅允许在容器中的物品。
    - 如果为空，则允许容器中所有物品。
- `banned_items`: 数组
    - 定义不允许在容器中的物品。
- `max_slots`: 整数（1-64）
    - 定义容器中的槽位数量。
- `max_weight_limit`: 整数
    - 定义容器中所有物品的最大总重量。
        - 计算物品重量的方法是将64除以其最大堆叠数量。
        - 堆叠到64的物品每个重量1，堆叠到16的物品每个重量4，无法堆叠的物品每个重量64。
- `weight_in_storage_item`: 整数（0-64）
    - 定义物品在另一个存储物品内时增加的额外重量。
        - 值为0表示不允许此物品放入另一个存储物品中。

```json title="minecraft:item > components"
"minecraft:storage_item": {
    "max_slots": 64,
    "max_weight_limit": 64,
    "weight_in_storage_item": 4,
    "allow_nested_storage_items": true,
    "banned_items": [
        "minecraft:shulker_box",
        "minecraft:undyed_shulker_box"
    ]
}
```

### 标签

`tags` 组件确定附加到物品的标签。

类型：对象

- `tags`: 数组
    - 附加到物品的标签列表。

```json title="minecraft:item > components"
"minecraft:tags": {
    "tags": [
        "custom_tag"
    ]
}
```

### 可投掷

可投掷物品组件。可投掷物品，如雪球。在格式版本 1.20.10 中从实验中发布。物品必须具有 `minecraft:projectile` 组件。

类型：对象

- `do_swing_animation`: 布尔值
    - 物品被投掷时是否应使用挥动动画。
- `launch_power_scale`: 浮点数
    - 投掷力量增加的比例。
    - 可以为负值。负值将使投射物向相反方向发射。
- `max_draw_duration`: 浮点数
    - 拉动可投掷物品的最大持续时间。
    - 可以为负值。将立即投掷。
    - 如果最大值小于测试中的最小值，则无副作用。
- `max_launch_power`: 浮点数
    - 发射可投掷物品的最大力量。
    - 可以为负值。
- `min_draw_duration`: 浮点数
    - 拉动可投掷物品的最小持续时间。
    - 可以为负值。将立即投掷。
- `scale_power_by_draw_duration`: 布尔值
    - 投掷力量是否随充能持续时间增加而增加。当为 `true` 时，持有时间越长，释放时力量越大。

```json title="minecraft:item > components"
"minecraft:throwable": {
    "do_swing_animation": false,
    "launch_power_scale": 1.0,
    "max_draw_duration": 0.0,
    "max_launch_power": 1.0,
    "min_draw_duration": 0.0,
    "scale_power_by_draw_duration": false
}
```

### 使用动画

确定使用物品时播放哪个动画。

类型：字符串

```json title="minecraft:item > components"
"minecraft:use_animation": {
    "value": "eat"
}
```

#### 已知动画

- eat
- drink
- bow
- block
- camera
- crossbow
- none
- brush
- spear
- spyglass

### 使用修改器

修改使用效果，包括使用物品所需的时间以及与射手、可投掷或食物等组件结合使用时玩家的速度。

类型：对象

- `movement_modifier`: 浮点数
    - 使用物品时缩放玩家移动速度的修改值。
    - 范围：[0, 1]
- `use_duration`: 浮点数
    - 使用物品所需的时间（以秒为单位）。
    - 必填字段

```json title="minecraft:item > components"
"minecraft:use_modifiers": {
    "movement_modifier": 0.5,
    "use_duration": 1.0
}
```

### 可穿戴

确定物品可以佩戴的位置。如果选择任何非手部槽位，最大堆叠数量将设置为1。

类型：对象

- `protection`: 整数
- `slot`: 字符串

```json title="minecraft:item > components"
"minecraft:wearable": {
    "protection": 10,
    "slot": "slot.armor.chest"
}
```

#### 槽位

| 槽位名称             |
| -------------------- |
| slot.weapon.offhand   |
| slot.armor.head       |
| slot.armor.chest      |
| slot.armor.legs       |
| slot.armor.feet       |