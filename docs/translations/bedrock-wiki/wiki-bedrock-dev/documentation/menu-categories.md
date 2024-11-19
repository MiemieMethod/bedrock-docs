---
title: 菜单类别
mentions:
    - Warhead51707
    - yanasakana
    - SirLich
    - SmokeyStack
    - MedicalJewel105
    - Chikorita-Lover
    - MiemieMethod
    - retr0cube
    - TheItsNameless
    - QuazChick
description: 菜单类别决定了物品和方块在创造模式物品栏和配方书中的显示位置。
---

菜单类别决定了物品和方块在创造模式物品栏和配方书中的显示位置。

-   可以定义一个 `category` 来将物品放置在某个标签下（例如建筑）。点击 [这里](#list-of-categories) 查看有效类别的列表。

-   `group` 指定了物品放置到哪个可扩展组中。如果使用自定义值，则不会创建新的可扩展组，但具有相同组的物品将会在创造模式物品栏中相邻放置。点击 [这里](#list-of-groups) 查看可扩展组的列表。

-   还可以将 `is_hidden_in_commands` 设置为 true，以从命令中移除此方块/物品，例如 `/give` 和 `/setblock`。

如果省略 `menu_category`，该物品将只能通过命令访问，并且不会出现在创造模式物品栏或配方书中。

**注意：** 自定义生成蛋的菜单类别无法修改。你必须创建一个带有 `minecraft:entity_placer` 组件的自定义物品。

```json title=""
"menu_category": {
    "category": "construction", // 物品放置的标签
    "group": "itemGroup.name.door", // 可选 - 物品放置的组
    "is_hidden_in_commands": false // 可选 - 默认值为 false（物品可在命令中使用）
}
```

/// danger | 隐藏物品在命令中无法访问 ([MCPE-177866](https://bugs.mojang.com/browse/MCPE-177866))
目前，在自定义物品（非方块）中将类别设置为 "none" 会阻止该物品在命令中使用，覆盖 "is_hidden_in_commands" 选项。此问题不影响方块。
///

## 方块示例

```json title="BP/blocks/balsa_wood.json"
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:balsa_wood",
            "menu_category": {
                "category": "nature",
                "group": "itemGroup.name.wood" // 放置到可扩展组中
            }
        }
    }
}
```

## 物品示例

```json title="BP/items/dagger.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:dagger",
            "menu_category": {
                "category": "equipment",
                "is_hidden_in_commands": true // 物品无法在命令中使用
            }
        }
    }
}
```

## 类别列表

_用于 `menu_category` 参数中的 `category`。_

| 类别         | 描述                                                  |
| ------------ | ----------------------------------------------------- |
| construction | 添加到“建筑”标签中。                                |
| equipment    | 添加到“装备”标签中。                                |
| items        | 添加到“物品”标签中。                                |
| nature       | 添加到“自然”标签中。                                |
| none         | 不添加到任何标签，仅可通过命令访问。                |

## 组列表

_用于 `menu_category` 参数中的 `group`。_

<!-- page_dumper_start -->

| 创造模式类别：                |
| ----------------------------- |
| itemGroup.name.anvil          |
| itemGroup.name.arrow          |
| itemGroup.name.axe            |
| itemGroup.name.banner         |
| itemGroup.name.banner_pattern |
| itemGroup.name.bed            |
| itemGroup.name.boat           |
| itemGroup.name.boots          |
| itemGroup.name.buttons        |
| itemGroup.name.candles        |
| itemGroup.name.chalkboard     |
| itemGroup.name.chest          |
| itemGroup.name.chestboat      |
| itemGroup.name.chestplate     |
| itemGroup.name.compounds      |
| itemGroup.name.concrete       |
| itemGroup.name.concretePowder |
| itemGroup.name.cookedFood     |
| itemGroup.name.copper         |
| itemGroup.name.coral          |
| itemGroup.name.coral_decorations |
| itemGroup.name.crop           |
| itemGroup.name.door           |
| itemGroup.name.dye            |
| itemGroup.name.enchantedBook  |
| itemGroup.name.fence          |
| itemGroup.name.fenceGate      |
| itemGroup.name.firework       |
| itemGroup.name.fireworkStars  |
| itemGroup.name.flower         |
| itemGroup.name.glass          |
| itemGroup.name.glassPane      |
| itemGroup.name.glazedTerracotta |
| itemGroup.name.goatHorn       |
| itemGroup.name.grass          |
| itemGroup.name.hanging_sign   |
| itemGroup.name.helmet         |
| itemGroup.name.hoe            |
| itemGroup.name.horseArmor     |
| itemGroup.name.leaves         |
| itemGroup.name.leggings       |
| itemGroup.name.lingeringPotion |
| itemGroup.name.log            |
| itemGroup.name.minecart       |
| itemGroup.name.miscFood       |
| itemGroup.name.mobEgg         |
| itemGroup.name.monsterStoneEgg |
| itemGroup.name.mushroom       |
| itemGroup.name.netherWartBlock |
| itemGroup.name.ore            |
| itemGroup.name.permission      |
| itemGroup.name.pickaxe        |
| itemGroup.name.planks         |
| itemGroup.name.potion         |
| itemGroup.name.potterySherds  |
| itemGroup.name.pressurePlate  |
| itemGroup.name.products       |
| itemGroup.name.rail           |
| itemGroup.name.rawFood        |
| itemGroup.name.record         |
| itemGroup.name.sandstone      |
| itemGroup.name.sapling        |
| itemGroup.name.sculk          |
| itemGroup.name.seed           |
| itemGroup.name.shovel         |
| itemGroup.name.shulkerBox     |
| itemGroup.name.sign           |
| itemGroup.name.skull          |
| itemGroup.name.slab           |
| itemGroup.name.smithing_templates |
| itemGroup.name.splashPotion   |
| itemGroup.name.stainedClay    |
| itemGroup.name.stairs         |
| itemGroup.name.stone          |
| itemGroup.name.stoneBrick     |
| itemGroup.name.sword          |
| itemGroup.name.trapdoor       |
| itemGroup.name.walls          |
| itemGroup.name.wood           |
| itemGroup.name.wool           |
| itemGroup.name.woolCarpet     |

_最后更新于 1.21.0_

<!-- page_dumper_end -->