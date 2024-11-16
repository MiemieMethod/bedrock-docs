---
title: Vanilla 使用生成规则
category: 文档
mentions:
    - MedicalJewel105
description: 自动生成的 vanilla 使用的生成规则组件列表。
---

此页面是使用 [Wiki内容生成器](https://github.com/Bedrock-OSS/bedrock-wiki-content-generator) 创建的。如果有问题，请在 [Bedrock OSS](https://discord.gg/XjV87YN) Discord 服务器联系我们。
请注意，为了保持页面加载速度，每个组件最多只显示8个示例。命名空间 `minecraft` 也已移除。如果你想查看完整页面，可以点击[这里](../entities/vusr-full.md)。*最后更新于1.21.0*

## biome_filter

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "value": "savanna"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "all_of": [
        {
            "test": "has_biome_tag",
            "value": "mesa"
        },
        {
            "test": "has_biome_tag",
            "operator": "not",
            "value": "plateau"
        }
    ]
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "all_of": [
        {
            "test": "has_biome_tag",
            "value": "mesa"
        },
        {
            "test": "has_biome_tag",
            "value": "plateau"
        }
    ]
}
```

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "lush_caves"
}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

bee

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": [
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "sunflower_plains"
    },
    {
        "test": "has_biome_tag",
        "operator": "==",
        "value": "flower_forest"
    }
]
```

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "any_of": [
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "swamp"
        },
        {
            "test": "has_biome_tag",
            "operator": "==",
            "value": "mangrove_swamp"
        }
    ]
}
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

</Spoiler>

## brightness_filter

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 4,
    "adjust_for_weather": true
}
```

bee

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

cow

<CodeHeader></CodeHeader>

```json
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

</Spoiler>

## delay_filter

<Spoiler title="显示">

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_easy",
    "spawn_chance": 20
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_normal",
    "spawn_chance": 20
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_hard",
    "spawn_chance": 20
}
```

</Spoiler>

## density_limit

<Spoiler title="显示">

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "underground": 5
}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

cod

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 20
}
```

creeper

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

dolphin

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5,
    "underground": 0
}
```

drowned

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 5
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 2
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:density_limit": {
    "surface": 2
}
```

</Spoiler>

## difficulty_filter

<Spoiler title="显示">

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

creeper

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

drowned

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

enderman

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

</Spoiler>

## disallow_spawns_in_bubble

<Spoiler title="显示">

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:disallow_spawns_in_bubble": {}
```

</Spoiler>

## distance_filter

<Spoiler title="显示">

cod

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

pufferfish

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

salmon

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

tropicalfish

<CodeHeader></CodeHeader>

```json
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

</Spoiler>

## height_filter

<Spoiler title="显示">

bat

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": -63,
    "max": 63
}
```

cod

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

dolphin

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

glow_squid

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": -64,
    "max": 30
}
```

pufferfish

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

salmon

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

stray

<CodeHeader></CodeHeader>

```json
"minecraft:height_filter": {
    "min": 60,
    "max": 66
}
```

</Spoiler>

## herd

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 3
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 4,
    "max_size": 6,
    "event": "minecraft:entity_born",
    "event_skip_count": 2
}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 2
}
```

bee

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 1,
    "max_size": 1
}
```

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:herd": {
    "min_size": 2,
    "max_size": 4
}
```

</Spoiler>

## mob_event_filter

<Spoiler title="显示">

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

</Spoiler>

## permute_type

<Spoiler title="显示">

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

zombie

<CodeHeader></CodeHeader>

```json
"minecraft:permute_type": [
    {
        "weight": 95
    },
    {
        "weight": 5,
        "entity_type": "minecraft:zombie_villager_v2"
    }
]
```

</Spoiler>

## player_in_village_filter

<Spoiler title="显示">

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

</Spoiler>

## spawn_event

<Spoiler title="显示">

stray

<CodeHeader></CodeHeader>

```json
"minecraft:spawn_event": {
    "event": "change_to_skeleton"
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawn_event": {
    "event": "change_to_skeleton"
}
```

</Spoiler>

## spawns_lava

<Spoiler title="显示">

strider

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_lava": {}
```

</Spoiler>

## spawns_on_block_filter

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": [
    {
        "name": "minecraft:grass_block"
    },
    {
        "name": "minecraft:sand",
        "states": {
            "sand_type": "red"
        }
    },
    {
        "name": "minecraft:dirt",
        "states": {
            "dirt_type": "coarse"
        }
    },
    {
        "name": "minecraft:brown_terracotta"
    },
    {
        "name": "minecraft:hardened_clay"
    },
    {
        "name": "minecraft:orange_terracotta"
    },
    {
        "name": "minecraft:light_gray_terracotta"
    },
    {
        "name": "minecraft:red_terracotta"
    },
    {
        "name": "minecraft:white_terracotta"
    },
    {
        "name": "minecraft:yellow_terracotta"
    }
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": [
    {
        "name": "minecraft:grass_block"
    },
    {
        "name": "minecraft:sand",
        "states": {
            "sand_type": "red"
        }
    },
    {
        "name": "minecraft:dirt",
        "states": {
            "dirt_type": "coarse"
        }
    },
    {
        "name": "minecraft:brown_terracotta"
    },
    {
        "name": "minecraft:hardened_clay"
    },
    {
        "name": "minecraft:orange_terracotta"
    },
    {
        "name": "minecraft:light_gray_terracotta"
    },
    {
        "name": "minecraft:red_terracotta"
    },
    {
        "name": "minecraft:white_terracotta"
    },
    {
        "name": "minecraft:yellow_terracotta"
    }
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": [
    {
        "name": "minecraft:grass_block"
    },
    {
        "name": "minecraft:sand",
        "states": {
            "sand_type": "red"
        }
    },
    {
        "name": "minecraft:dirt",
        "states": {
            "dirt_type": "coarse"
        }
    },
    {
        "name": "minecraft:brown_terracotta"
    },
    {
        "name": "minecraft:hardened_clay"
    },
    {
        "name": "minecraft:orange_terracotta"
    },
    {
        "name": "minecraft:light_gray_terracotta"
    },
    {
        "name": "minecraft:red_terracotta"
    },
    {
        "name": "minecraft:white_terracotta"
    },
    {
        "name": "minecraft:yellow_terracotta"
    }
]
```

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:clay"
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

cow

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

donkey

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

</Spoiler>

## spawns_on_block_prevented_filter

<Spoiler title="显示">

hoglin

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

magma_cube

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

piglin

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

skeleton

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

zombie_pigman

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

</Spoiler>

## spawns_on_surface

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

bee

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

cod

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

cow

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_on_surface": {}
```

</Spoiler>

## spawns_underground

<Spoiler title="显示">

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

creeper

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

enderman

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

ghast

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

glow_squid

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underground": {}
```

</Spoiler>

## spawns_underwater

<Spoiler title="显示">

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

cod

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

dolphin

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

drowned

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

glow_squid

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

guardian

<CodeHeader></CodeHeader>

```json
"minecraft:spawns_underwater": {}
```

</Spoiler>

## weight

<Spoiler title="显示">

armadillo

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 6,
    "rarity": 3
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 6,
    "rarity": 2
}
```

axolotl

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

bat

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

bee

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

bogged

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 40
}
```

chicken

<CodeHeader></CodeHeader>

```json
"minecraft:weight": {
    "default": 10
}
```

</Spoiler>

## world_age_filter

<Spoiler title="显示">

pillager_patrol

<CodeHeader></CodeHeader>

```json
"minecraft:world_age_filter": {
    "min": 6000
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:world_age_filter": {
    "min": 6000
}
```

<CodeHeader></CodeHeader>

```json
"minecraft:world_age_filter": {
    "min": 6000
}
```

</Spoiler>