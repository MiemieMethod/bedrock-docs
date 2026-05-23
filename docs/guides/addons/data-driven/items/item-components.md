# 物品组件概览

物品组件（item component）是控制物品行为与外观的基本单元，写在`minecraft:item`的`components`对象中。本页对所有可用组件按功能分类进行介绍，并给出典型用法示例。

## 外观与展示

### `minecraft:icon`

指定物品在UI中显示的图标，引用`item_texture.json`中的短名。

```json
"minecraft:icon": "wiki:custom_item"
```

也可以使用对象格式，支持染色后图标（`dyed`）、盔甲纹饰图标叠层（`icon_trim`）和束包界面图标（`bundle_open_back`/`bundle_open_front`）：

```json
"minecraft:icon": {
    "textures": {
        "default": "wiki:custom_item",
        "dyed": "wiki:custom_item_dyed"
    }
}
```

### `minecraft:display_name`

覆盖物品的显示名称本地化键：

```json
"minecraft:display_name": {
    "value": "item.wiki:custom_item"
}
```

若值不存在对应翻译条目，则直接显示原始字符串。

### `minecraft:hover_text_color`

更改物品名称文字的颜色（详见[基岩版格式代码](https://zh.minecraft.wiki/w/格式代码)）：

```json
"minecraft:hover_text_color": "minecoin_gold"
```

/// note | 优先级
`hover_text_color`会覆盖`rarity`组件的颜色设置。
///

### `minecraft:rarity`

通过稀有度改变物品名称颜色。可用值：`"common"`（白）、`"uncommon"`（黄）、`"rare"`（青）、`"epic"`（紫）。附魔时稀有度会自动升一级（`rare`→`epic`）：

```json
"minecraft:rarity": "rare"
```

### `minecraft:glint`

控制物品是否显示附魔光效，即使未附魔也可强制开启：

```json
"minecraft:glint": true
```

### `minecraft:hand_equipped`

决定物品在第三人称时是否以工具形式渲染（平放 vs. 竖立）：

```json
"minecraft:hand_equipped": true
```

### `minecraft:use_animation`

使用充能物品（如食物）时播放的动画。可用值：`"eat"`、`"drink"`、`"bow"`、`"brush"`、`"spear"`、`"spyglass"`等：

```json
"minecraft:use_animation": "eat"
```

## 堆叠与存储

### `minecraft:max_stack_size`

最大堆叠数量（1–64）：

```json
"minecraft:max_stack_size": 16
```

### `minecraft:stacked_by_data`

同类型但附加值不同的物品是否分开堆叠：

```json
"minecraft:stacked_by_data": true
```

### `minecraft:should_despawn`

物品实体是否会随时间消失：

```json
"minecraft:should_despawn": false
```

### `minecraft:storage_item`

让物品充当容器，可存放其他物品（类似束包），需配合`minecraft:bundle_interaction`使用：

```json
"minecraft:storage_item": {
    "max_slots": 64,
    "allow_nested_storage_items": true,
    "banned_items": ["minecraft:shulker_box"]
}
```

## 战斗与工具

### `minecraft:damage`

攻击时额外造成的伤害值（0–32767），在物品提示中显示为"+X 攻击伤害"：

```json
"minecraft:damage": 10
```

### `minecraft:digger`

控制物品挖掘特定方块的速度：

```json
"minecraft:digger": {
    "use_efficiency": true,
    "destroy_speeds": [
        {
            "block": {
                "tags": "q.any_tag('minecraft:is_pickaxe_item_destructible')"
            },
            "speed": 6
        }
    ]
}
```

### `minecraft:enchantable`

允许物品在附魔台、铁砧等处被附魔，`slot`决定可用魔咒类型，`value`影响附魔质量：

```json
"minecraft:enchantable": {
    "slot": "sword",
    "value": 10
}
```

可用槽位包括`"sword"`、`"axe"`、`"pickaxe"`、`"shovel"`、`"hoe"`、`"bow"`、`"crossbow"`、`"armor_head"`、`"armor_torso"`、`"armor_legs"`、`"armor_feet"`、`"elytra"`、`"shield"`等。

### `minecraft:durability`

赋予物品耐久值，物品被使用后耐久降低，归零后物品损坏：

```json
"minecraft:durability": {
    "max_durability": 250
}
```

### `minecraft:repairable`

定义可修复该物品的材料与修复量：

```json
"minecraft:repairable": {
    "repair_items": [
        {
            "items": ["minecraft:diamond"],
            "repair_amount": "context.other->q.remaining_durability + 0.05 * context.other->q.max_durability"
        }
    ]
}
```

### `minecraft:durability_sensor`

当耐久值降至阈值时触发粒子或音效：

```json
"minecraft:durability_sensor": {
    "durability_thresholds": [
        {
            "durability": 5,
            "sound_event": "raid.horn"
        }
    ]
}
```

### `minecraft:damage_absorption`

装备在盔甲槽时吸收特定来源的伤害（需配合`minecraft:wearable`和`minecraft:durability`）：

```json
"minecraft:damage_absorption": {
    "absorbable_causes": ["all"]
}
```

### `minecraft:kinetic_weapon`

玩家移动时对周围实体造成动能伤害（类似密度9原版长矛）：

```json
"minecraft:kinetic_weapon": {
    "delay": 15,
    "reach": { "min": 2.0, "max": 4.5 },
    "damage_multiplier": 0.7,
    "damage_conditions": {
        "max_duration": 300,
        "min_relative_speed": 4.6
    }
}
```

### `minecraft:piercing_weapon`

攻击时对直线上所有实体造成伤害：

```json
"minecraft:piercing_weapon": {
    "reach": { "min": 0.0, "max": 3.0 }
}
```

### `minecraft:swing_duration`

玩家挥手/挖掘动画的基础时长（秒）：

```json
"minecraft:swing_duration": { "value": 0.5 }
```

### `minecraft:swing_sounds`

攻击时播放的音效，区分命中（`attack_hit`）、暴击（`attack_critical_hit`）和落空（`attack_miss`）：

```json
"minecraft:swing_sounds": {
    "attack_hit": "item.wooden_spear.attack_hit",
    "attack_miss": "item.wooden_spear.attack_miss"
}
```

## 可穿戴

### `minecraft:wearable`

允许物品被穿戴在指定槽位上：

```json
"minecraft:wearable": {
    "protection": 4,
    "slot": "slot.armor.head"
}
```

可用槽位：`"slot.weapon.offhand"`、`"slot.armor.head"`、`"slot.armor.chest"`、`"slot.armor.legs"`、`"slot.armor.feet"`。

### `minecraft:dyeable`

允许物品在锅炉中被染色，染色后显示`dyed`图标纹理：

```json
"minecraft:dyeable": {
    "default_color": "#a06540"
}
```

## 食物与消耗

### `minecraft:food`

允许物品被食用，恢复饥饿值与饱和度。需配合`minecraft:use_modifiers`（必须指定`use_duration`）：

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": 0.6,
    "can_always_eat": false
}
```

### `minecraft:use_modifiers`

控制可充能物品的使用行为（食物、弓、弩等）：

```json
"minecraft:use_modifiers": {
    "use_duration": 1.6,
    "movement_modifier": 0.35
}
```

### `minecraft:fuel`

允许物品作为熔炉燃料，`duration`为燃烧秒数：

```json
"minecraft:fuel": {
    "duration": 8.5
}
```

### `minecraft:compostable`

允许物品放入堆肥桶，`composting_chance`为增加堆肥层数的概率（0–100）：

```json
"minecraft:compostable": {
    "composting_chance": 50
}
```

## 弹射与投掷

### `minecraft:projectile`

关联一个弹射物实体，配合`minecraft:throwable`或`minecraft:shooter`使用：

```json
"minecraft:projectile": {
    "projectile_entity": "minecraft:arrow",
    "minimum_critical_power": 1.25
}
```

### `minecraft:throwable`

允许物品被抛出（类似雪球、鸡蛋）：

```json
"minecraft:throwable": {
    "do_swing_animation": true,
    "max_launch_power": 1.0
}
```

### `minecraft:shooter`

允许物品发射弹药（类似弓、弩）：

```json
"minecraft:shooter": {
    "ammunition": [
        {
            "item": "minecraft:arrow",
            "search_inventory": true,
            "use_in_creative": true,
            "use_offhand": true
        }
    ],
    "scale_power_by_draw_duration": true
}
```

## 交互与放置

### `minecraft:block_placer`

允许物品放置方块：

```json
"minecraft:block_placer": {
    "block": "wiki:custom_block"
}
```

### `minecraft:entity_placer`

允许物品放置实体（类似刷怪蛋）：

```json
"minecraft:entity_placer": {
    "entity": "minecraft:spider",
    "use_on": ["minecraft:dirt"]
}
```

### `minecraft:interact_button`

在触屏控件中显示交互按钮。值为`true`时显示通用"使用物品"文字，值为字符串时显示对应本地化键：

```json
"minecraft:interact_button": "action.interact.wiki:launch"
```

### `minecraft:liquid_clipped`

物品在对准液体时能否与液体内部的方块交互（类似钓鱼竿）：

```json
"minecraft:liquid_clipped": true
```

## 特殊功能

### `minecraft:record`

允许物品插入唱片机播放音乐：

```json
"minecraft:record": {
    "comparator_signal": 8,
    "duration": 120,
    "sound_event": "record.chirp"
}
```

### `minecraft:cooldown`

物品使用后进入冷却状态，`category`相同的物品共享冷却：

```json
"minecraft:cooldown": {
    "category": "wiki:my_cooldown",
    "duration": 1.0,
    "type": "use"
}
```

### `minecraft:allow_off_hand`

允许物品装备在副手槽：

```json
"minecraft:allow_off_hand": true
```

### `minecraft:can_destroy_in_creative`

创造模式下持有物品能否破坏方块（默认为`true`）：

```json
"minecraft:can_destroy_in_creative": false
```

### `minecraft:fire_resistant`

物品实体落在岩浆/火焰中是否不被销毁：

```json
"minecraft:fire_resistant": { "value": true }
```

### `minecraft:bundle_interaction`

启用束包式工具提示与交互功能（需配合`minecraft:storage_item`）：

```json
"minecraft:bundle_interaction": {
    "num_viewable_slots": 12
}
```

### `minecraft:tags`

为物品添加标签，用于过滤器、配方、Molang查询等。详见[物品标签](item-tags.md)：

```json
"minecraft:tags": {
    "tags": ["wiki:my_tag", "minecraft:is_food"]
}
```

---

关于如何在脚本中监听物品事件（如使用、攻击、消耗），请继续阅读[物品事件](item-events.md)。