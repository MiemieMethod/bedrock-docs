# 矿石战利品表

这一页展示如何创建一个只有正确工具才能掉落物品的矿石方块，并在成功开采时奖励经验球。

## 战利品表

使用 `match_tool` 条件限制掉落：

```json title="BP/loot_tables/blocks/silver_ore.json"
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
                    "name": "wiki:raw_silver"
                }
            ]
        }
    ]
}
```

只有使用铁镐及以上品质的镐才会掉落 `wiki:raw_silver`；用其他工具或徒手破坏则什么都不掉。

### 附魔过滤

如果要针对特定附魔（如时运）添加额外掉落，需要为每个附魔等级单独添加一个池：

```json title="pools > conditions（节选）"
"conditions": [
    {
        "condition": "match_tool",
        "minecraft:match_tool_filter_all": ["minecraft:is_pickaxe"],
        "minecraft:match_tool_filter_any": ["minecraft:iron_tier", "minecraft:diamond_tier", "minecraft:netherite_tier"],
        "enchantments": [
            {
                "fortune": { "level": 1 }
            }
        ]
    }
]
```

/// note
附魔检测目前只能正确识别第1和第2附魔等级，请分别为每个等级创建独立的池。
///

## 经验球脚本

通过自定义组件在 `onPlayerBreak` 时生成经验球：

```js title="BP/scripts/silver_ore.js"
import { system, EquipmentSlot } from "@minecraft/server";

const OreExpComponent = {
    onPlayerBreak({ block, dimension, player }, { params }) {
        const equip = player?.getComponent("minecraft:equippable");
        if (!equip) return;
        const item = equip.getEquipment(EquipmentSlot.Mainhand);
        if (!item?.hasTag("minecraft:is_pickaxe")) return;
        if (!item.hasTag("minecraft:iron_tier") &&
            !item.hasTag("minecraft:diamond_tier") &&
            !item.hasTag("minecraft:netherite_tier")) return;
        // 丝绸之触不给经验
        if (item.getComponent("minecraft:enchantable")?.getEnchantment("silk_touch")) return;

        const count = params.min + Math.floor(Math.random() * (params.max - params.min + 1));
        for (let i = 0; i < count; i++) {
            dimension.spawnEntity("minecraft:xp_orb", block.location);
        }
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:ore_exp", OreExpComponent);
});
```

## 方块定义

把战利品表和自定义组件挂到方块上：

```json title="BP/blocks/silver_ore.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:silver_ore",
            "menu_category": {
                "category": "nature",
                "group": "minecraft:itemGroup.name.ore"
            }
        },
        "components": {
            "minecraft:destructible_by_mining": { "seconds_to_destroy": 3.0 },
            "minecraft:loot": "loot_tables/blocks/silver_ore.json",
            "minecraft:material_instances": {
                "*": { "texture": "wiki:silver_ore" }
            },
            "wiki:ore_exp": { "min": 1, "max": 5 }
        }
    }
}
```

别忘了在 `terrain_texture.json` 中注册纹理短名 `wiki:silver_ore`。