# 在世界中生成物品

本篇介绍在基岩版中让物品以掉落物形式出现在世界中的若干方法。

## 方法一：`/loot`命令

`/loot`命令可以从战利品表中生成物品。这是最简洁的方式，适合在函数或命令方块中使用：

```mcfunction
# 在指定坐标生成战利品表中的物品
/loot spawn 100 64 100 loot "loot_tables/custom/my_loot"
```

将战利品表JSON文件放在`BP/loot_tables/custom/my_loot.json`。

## 方法二：实体死亡掉落

在实体行为文件中添加`minecraft:loot`组件，实体死亡时自动从战利品表中掉落物品：

```json title="实体 components"
"minecraft:loot": {
    "table": "loot_tables/custom/my_entity_loot.json"
}
```

这是最标准的掉落物实现方式，适用于怪物、动物等实体的掉落设计。

## 方法三：虚假实体触发死亡

若不希望修改现有实体，可以生成一个立即死亡的虚假实体，利用它的死亡掉落来"生成"物品：

### 虚假实体行为文件

```json title="BP/entities/item_dropper.json"
{
    "format_version": "1.21.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:item_dropper",
            "is_spawnable": false,
            "is_summonable": true,
            "is_experimental": false
        },
        "components": {
            "minecraft:loot": {
                "table": "loot_tables/custom/my_items.json"
            },
            "minecraft:health": {
                "value": 1,
                "max": 1
            },
            "minecraft:instant_despawn": {}
        }
    }
}
```

`minecraft:instant_despawn`让实体在下一刻消失（同时触发死亡掉落）。通过命令召唤此实体即可在指定位置"放置"物品：

```mcfunction
/summon wiki:item_dropper 100 64 100
```

## 方法四：`behavior.drop_item_for`

通过给实体添加`minecraft:behavior.drop_item_for` AI意向，可以让实体主动将物品丢向玩家：

```json title="实体 components"
"minecraft:behavior.drop_item_for": {
    "priority": 2,
    "seconds_before_pickup": 0,
    "goal_radius": 4.0,
    "loot_table": "loot_tables/custom/my_items.json",
    "drop_item_chance": 1.0,
    "offering_distance": 5.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "value": "player"
            }
        }
    ]
}
```

此意向会让实体在玩家附近时从战利品表中丢出物品。

## 方法五：结构文件

将物品掉落物（实体`item`）作为结构的一部分保存下来，通过`/structure load`或结构地物（structure feature）在指定位置加载，从而"放置"物品：

1. 在创意模式中将物品扔在地上，用`/structure save`覆盖该范围进行保存。
2. 保存的结构文件存放于`BP/structures/`。
3. 在需要生成物品的地方使用`/structure load my_structure ~ ~ ~`加载。

此方法适合需要精确摆放多个物品的场景，但较为繁琐。

## 战利品表示例

以上方法（除`/loot spawn`之外）都引用了战利品表文件，以下是一个简单示例：

```json title="BP/loot_tables/custom/my_items.json"
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "wiki:my_item",
                    "weight": 1
                }
            ]
        }
    ]
}
```