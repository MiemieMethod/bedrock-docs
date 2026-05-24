# 基于工具的破坏

基岩版的自定义方块默认可以用任何工具（或徒手）在同等速度内破坏。这一页介绍如何让方块只能用特定品质的工具高效破坏，以及如何在战利品表中限制掉落物。

## 破坏时间

`minecraft:destructible_by_mining` 组件中的 `seconds_to_destroy` 是方块的**硬度值**——注意名称有些误导：实际破坏时间是硬度值的1.5倍（使用合适工具时可能更快）。

```json title="BP/blocks/my_ore.json > components"
"minecraft:destructible_by_mining": {
    "seconds_to_destroy": 3.0
}
```

上面的配置意味着徒手破坏时约需4.5秒。如果想模拟铁矿石（硬度3）的手感，设置为 `3.0` 即可。

## 基于工具标签的掉落物控制

战利品表的 `match_tool` 条件可以检查玩家使用的工具，实现只有特定工具才能掉落物品的效果：

```json title="BP/loot_tables/blocks/my_ore.json"
{
    "pools": [
        {
            "rolls": 1,
            "conditions": [
                {
                    "condition": "match_tool",
                    "minecraft:match_tool_filter_all": [
                        "minecraft:is_tool",
                        "minecraft:is_pickaxe"
                    ],
                    "minecraft:match_tool_filter_any": [
                        "minecraft:iron_tier",
                        "minecraft:diamond_tier",
                        "minecraft:netherite_tier"
                    ],
                    "count": 1
                }
            ],
            "entries": [
                {
                    "type": "item",
                    "name": "wiki:my_ore_drop"
                }
            ]
        }
    ]
}
```

在方块JSON中引用战利品表：

```json title="BP/blocks/my_ore.json > components"
"minecraft:loot": "loot_tables/blocks/my_ore.json"
```

/// warning | 非玩家破坏
`match_tool` 只检查工具，对爆炸、命令等非玩家破坏方式无效——这些情况下战利品表依然会执行，如果没有满足条件的池，什么都不掉落。
///

## 工具品质标签

| 标签 | 工具品质 |
|------|---------|
| `minecraft:is_pickaxe` | 任意镐 |
| `minecraft:is_axe` | 任意斧 |
| `minecraft:is_shovel` | 任意铲 |
| `minecraft:is_hoe` | 任意锄 |
| `minecraft:is_sword` | 任意剑 |
| `minecraft:wood_tier` | 木质工具 |
| `minecraft:stone_tier` | 石质工具 |
| `minecraft:iron_tier` | 铁质工具 |
| `minecraft:gold_tier` | 金质工具 |
| `minecraft:diamond_tier` | 钻石工具 |
| `minecraft:netherite_tier` | 下界合金工具 |

## 用于方块的可摧毁标签

方块可以通过添加方块标签来让特定工具获得挖掘加速，从而使该工具对方块特别有效。以下6个标签对应6种破坏方式：

| 标签 | 合适工具 |
|------|---------|
| `minecraft:is_pickaxe_item_tier_1` ～ `minecraft:is_pickaxe_item_tier_4` | 对应品质的镐 |
| `minecraft:is_axe_item_tier_1` ～ `minecraft:is_axe_item_tier_4` | 对应品质的斧 |
| `minecraft:is_shovel_item_tier_1` ～ `minecraft:is_shovel_item_tier_4` | 对应品质的铲 |

品质层级：1=木/金，2=石，3=铁，4=钻石/下界合金。

```json title="BP/blocks/my_ore.json > components"
"tag:minecraft:is_pickaxe_item_tier_3": {}
```

这让铁镐及以上品质的镐对该方块更有效（不用合适工具时，破坏速度会乘以约0.3倍的惩罚系数）。

## 奖励经验值

如果希望方块破坏时掉落经验球（类似原版矿石），可以用脚本API在 `onPlayerBreak` 事件中生成经验实体：

```js title="BP/scripts/my_ore.js"
import { system, EquipmentSlot } from "@minecraft/server";

const OreExpComponent = {
    onPlayerBreak({ block, dimension, player }, { params }) {
        const equip = player?.getComponent("minecraft:equippable");
        if (!equip) return;
        const item = equip.getEquipment(EquipmentSlot.Mainhand);
        if (!item?.hasTag("minecraft:is_pickaxe")) return;
        // 不掉落丝绸之触时才给经验
        const enchantable = item.getComponent("minecraft:enchantable");
        if (enchantable?.getEnchantment("silk_touch")) return;
        const amount = params.min + Math.floor(Math.random() * (params.max - params.min + 1));
        for (let i = 0; i < amount; i++) {
            dimension.spawnEntity("minecraft:xp_orb", block.location);
        }
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:ore_exp", OreExpComponent);
});
```

方块JSON中：

```json title="components"
"wiki:ore_exp": { "min": 1, "max": 5 }
```