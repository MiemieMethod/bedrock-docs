---
title: 生成规则
category: 一般
mentions:
    - SirLich
    - solvedDev
    - MedicalJewel105
    - aexer0e
    - Ciosciaa
    - FrankyRay
    - Luthorius
    - TheItsNameless
    - SmokeyStack
description: 生成规则定义了实体如何在世界中生成。
---

生成规则定义了实体如何在世界中生成。当你希望自定义实体像原版实体一样自然生成时，应使用生成规则。不同的组件允许你定义实体生成的时间、地点和方式。

一般来说，你可以以与原版实体非常相似的方式生成自定义实体。例如，可以像牛一样成群生成，像原版僵尸一样仅在夜间生成，或像鱼一样仅在水下生成。

## 示例生成规则

以下是一个生成规则示例，并对各字段进行解释。

```json title="BP/spawn_rules/zombie.json"
{
	"format_version": "1.8.0",
	"minecraft:spawn_rules": {
		"description": {
			"identifier": "minecraft:zombie",
			"population_control": "monster"
		},
		"conditions": [
			{
				"minecraft:spawns_on_surface": {},
				"minecraft:spawns_underground": {},
				"minecraft:brightness_filter": {
					"min": 0,
					"max": 7,
					"adjust_for_weather": true
				},
				"minecraft:difficulty_filter": {
					"min": "easy",
					"max": "hard"
				},
				"minecraft:weight": {
					"default": 100
				},
				"minecraft:herd": {
					"min_size": 2,
					"max_size": 4
				},
				"minecraft:permute_type": [
					{
						"weight": 95
					},
					{
						"weight": 5,
						"entity_type": "minecraft:zombie_villager"
					}
				],
				"minecraft:biome_filter": {
					"test": "has_biome_tag",
					"operator": "==",
					"value": "monster"
				}
			}
		]
	}
}
```

-   "`description`">"`identifier`": 要生成的实体
-   "`population_control`": 控制生成和消失数量。可以设置为 "`animal`"、"`underwater_animal`"、"`monster`" 和 "`ambient`"。
-   "`conditions`" 是一系列必须满足的条件，以使生成尝试成功。
-   "`minecraft:spawns_on_surface`"、"`minecraft:spawns_underground`" 和 "`minecraft:spawns_underwater`" 控制实体生成的地点限制。
-   "`minecraft:brightness_filter`" 可以设置为 0 到 15，控制实体可以在什么光照等级下生成。"`adjust_for_weather`" 定义在雨天或雷暴天气时光照等级是否会降低。
-   "`minecraft:difficulty_filter`" 设置启用该实体生成的难度等级范围。
-   "`minecraft:herd`" 设置一起生成的实体数量，适用于同一生成规则。
-   "`minecraft:permute_type`" 通过 "`weight`" 和 "`entity_type`" 设置生成的实体变异为不同实体的几率。
-   "`minecraft:biome_filter`" 测试特定的生物群落标签。请查阅文档中的过滤器语法和生物群落标签列表，或在原版示例包中搜索示例。

## 所有已知组件

以下是所有已知组件的列表。我们将随着对它们使用方式的更好理解而添加文档。

```
minecraft:weight
minecraft:density_limit
minecraft:spawns_on_block_filter
minecraft:spawns_on_block_prevented_filter
minecraft:spawns_above_block_filter
minecraft:herd
minecraft:permute_type
minecraft:brightness_filter
minecraft:height_filter
minecraft:spawns_on_surface
minecraft:spawns_underground
minecraft:spawns_underwater
minecraft:disallow_spawns_in_bubble
minecraft:spawns_lava
minecraft:biome_filter
minecraft:difficulty_filter
minecraft:distance_filter
minecraft:is_experimental
minecraft:world_age_filter
minecraft:delay_filter
minecraft:mob_event_filter
minecraft:is_persistent
minecraft:player_in_village_filter
```

## 文档

### minecraft:herd

```json title=""
"minecraft:herd": {
          "min_size": 1,
          "max_size": 2,
          "event":"minecraft:entity_born",
          "event_skip_count": 1
        },
```

-   "`minecraft:herd`" 也可以这样使用，使第二个生成的实体在此场景中通过 "`minecraft:entity_born`" 事件生成（作为幼体）。可以在任何事件中使用。
    `"event_skip_count": 2`，例如，意味着前两个实体不会通过此事件生成，但所有后续实体将会生成。

### minecraft:spawns_above_block_filter

```json title=""
        "minecraft:spawns_above_block_filter": {
          "blocks": "minecraft:stone",
          "distance": 10
        }
```

-   "`minecraft:spawns_above_block_filter`" 将在设定的垂直距离内检测方块，如果条件满足，实体将成功生成。

### minecraft:spawns_on_block_prevented_filter

```json title=""
        "minecraft:spawns_on_block_prevented_filter": [
          "minecraft:nether_wart_block",
          "minecraft:shroomlight"
        ]
```

-   最后，"`minecraft:spawns_on_block_prevented_filter`" 是上述的相反。这是一个方块标识符数组，实体将永远不会在这些方块上生成。