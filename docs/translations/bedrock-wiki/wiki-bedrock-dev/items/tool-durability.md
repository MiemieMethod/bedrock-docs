---
title: 工具耐久度
category: 教程
tags:
    - 实验性
    - 中级
    - 脚本
mentions:
    - MedicalJewel105
    - TheDoctor15
    - napstaa967
description: 为自定义工具添加类似原版的耐久度。
hidden: true
---

## 介绍

1.21.10+ 版本的物品具有与 1.10 和 1.16 版本不同的耐久度机制。现在你需要定义物品何时会受到耐久度损坏，以及执行此操作的事件。本页面将讨论以下内容：

- 耐久度组件
- 更新耐久度的事件
- 造成伤害的实体
- 破坏方块
- `repair_amount` 值
- `on_tool_used` 事件

### 组件

<CodeHeader>BP/items/my_item.json#components</CodeHeader>

```json
"minecraft:durability": {
    "max_durability": 200
}
```

`minecraft:durability` 将为你的物品设置最大耐久度。

## 事件

### 物品事件

<CodeHeader>BP/items/my_item.json#events</CodeHeader>

```json
"durability_update": {
    "damage": {
        "type": "none",
        "amount": 1,
        "target": "self"
    }
}
```

当调用此事件时，物品（`self` 目标）将受到耐久度损坏。看起来很简单，不是吗？

### 脚本事件

对于脚本方法，我们将使用一个函数来损坏我们的物品。

此函数支持物品的无破坏性。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
function damage_item(item) {
    // 获取耐久度
    const durabilityComponent = item.getComponent("durability");
    var unbreaking = 0;
    // 获取无破坏等级
    if (item.hasComponent("enchantments")) {
        unbreaking = item.getComponent("enchantments").enchantments.getEnchantment("unbreaking");
        if (!unbreaking) {
            unbreaking = 0;
        } else {
            unbreaking = unbreaking.level;
        }
    }
    // 应用伤害
    if (durabilityComponent.damage == durabilityComponent.maxDurability) {
        return;
    }
    durabilityComponent.damage += Number(
        Math.round(Math.random() * 100) <= durabilityComponent.getDamageChance(unbreaking)
    );
    return item;
}
```

## 造成伤害的实体

### 使用脚本

:::warning 实验性脚本

此脚本使用 `@minecraft/server 1.9.0-beta`，在下一个Minecraft更新中将会更改。
:::

对于格式版本 1.20.40 及之后，`on_hurt_entity` 不再有效。

这提供了一种通过脚本损坏武器的方法。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
// 将你的物品ID添加到此数组中
const my_items = ["wiki:silver_dagger"];

world.afterEvents.entityHurt.subscribe((event) => {
    // 如果没有源实体，则跳过
    if (!event.damageSource.damagingEntity) return;

    // 获取装备的武器
    const equipment = event.damageSource.damagingEntity.getComponent("minecraft:equippable");
    if (!equipment) return;
    const weapon = equipment.getEquipment(EquipmentSlot.Mainhand);

    // 如果没有武器，则跳过
    if (!weapon) return;

    // 如果物品不在我们的物品ID中，则跳过
    if (!my_items.includes(weapon.typeId)) return;
    let newItem = damage_item(weapon);
    equipment.setEquipment(EquipmentSlot.Mainhand, newItem);
    if (!newItem) {
        if (event.damageSource.damagingEntity instanceof Player) {
            event.damageSource.damagingEntity.playSound("random.break");
        }
    }
});
```

### on_hurt_entity

:::warning

`on_hurt_entity` 在格式版本 1.20.40 中被移除。
:::

`on_hurt_entity` 可以在 "minecraft:weapon" 组件中定义。它告诉游戏当玩家使用此物品伤害实体时应该发生什么事件。

<CodeHeader>BP/items/my_item.json#components</CodeHeader>

```json
"minecraft:weapon": {
    "on_hurt_entity": {
        "event": "durability_update"
    }
}
```

## 破坏方块

### 使用脚本

:::warning 实验性脚本

此脚本使用 `@minecraft/server 1.9.0-beta`，在下一个Minecraft更新中将会更改。
:::

对于格式版本 1.20.20 及之后，`on_dig` 不再有效。

这提供了一种通过脚本损坏挖掘工具的方法。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
// 将你的物品ID添加到此数组中
const my_items = ["wiki:obsidian_pickaxe"];

world.afterEvents.playerBreakBlock.subscribe((event) => {
    // 如果没有物品，则跳过
    if (!event.itemStackAfterBreak) return;
    // 如果物品不在我们的物品ID中，则跳过
    if (!my_items.includes(event.itemStackAfterBreak.typeId)) return;

    // 如果玩家处于创造模式，则跳过
    if (
        world
            .getPlayers({
                gameMode: GameMode.creative,
            })
            .includes(event.player)
    )
        return;
    const newItem = damage_item(event.itemStackAfterBreak);
    event.player.getComponent("minecraft:equippable").setEquipment(EquipmentSlot.Mainhand, newItem);
    if (!newItem) {
        event.player.playSound("random.break");
    }
});
```

### on_dig

:::warning

`on_dig` 在格式版本 1.20.20 中被移除。
:::

`on_dig` 可以在 "minecraft:digger" 组件中定义。它告诉游戏当玩家使用此物品挖掘方块时应该发生什么事件。

<CodeHeader>BP/items/my_item.json#components</CodeHeader>

```json
"minecraft:digger": {
    "use_efficiency": true,
    "destroy_speeds": [
        {
            "block": {
                "tags": "q.any_tag('wood')"
            },
            "speed": 8,
            "on_dig": {
                // 定义当挖掘带有木材标签的方块时应该发生的事件。
                "event": "durability_update"
            }
        }
    ],
    "on_dig": {
        // 定义当任何方块被破坏时应该发生的事件。
        "event": "durability_update"
    }
}
```

## repair_amount

`repair_amount` 可以在 "minecraft:repairable" 组件中定义。它告诉游戏修理时物品的耐久度应该恢复多少。

<CodeHeader>BP/items/my_item.json#components</CodeHeader>

```json
"minecraft:repairable": {
    "repair_items": [
        {
            "repair_amount": "context.other->q.remaining_durability + 0.05 * context.other->q.max_durability",
            "items": [
                "bs:silver",
                "bs:silver_axe"
            ]
        }
    ]
}
```

公式解释：

`"context.other->q.remaining_durability + 0.05 * context.other->q.max_durability"`

最终耐久度将是第一把斧头的耐久度 + 第二把斧头的耐久度 + 第二把斧头最大耐久度的 5%。

## on_tool_used

（这可能现在无法使用）  
`on_tool_used` 是一个特殊事件，可以通过标签调用。  
标签类似于实体的运行时标识符。  
已知标签：

| 标签                  | 效果          | 如何调用                                          |
| --------------------- | ------------- | ------------------------------------------------ |
| minecraft:is_axe     | 剥去树皮      | 通过与斧头交互的方块进行交互                    |
| minecraft:is_hoe      | 制作农田      | 通过与锄头交互的方块进行交互                    |
| minecraft:is_pickaxe  | 未知         | 未知                                            |
| minecraft:is_sword    | 未知         | 未知                                            |

你可以通过以下方式应用这些标签：

<CodeHeader>BP/items/my_item.json#components</CodeHeader>

```json
"tag:minecraft:is_axe": {}
```