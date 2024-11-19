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

```json title=""
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "value": "savanna"
}
```

```json title=""
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

```json title=""
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

```json title=""
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "lush_caves"
}
```

bat

```json title=""
"minecraft:biome_filter": {
    "test": "has_biome_tag",
    "operator": "==",
    "value": "animal"
}
```

bee

```json title=""
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

```json title=""
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

```json title=""
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

```json title=""
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json title=""
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

```json title=""
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

bat

```json title=""
"minecraft:brightness_filter": {
    "min": 0,
    "max": 4,
    "adjust_for_weather": true
}
```

bee

```json title=""
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

bogged

```json title=""
"minecraft:brightness_filter": {
    "min": 0,
    "max": 7,
    "adjust_for_weather": true
}
```

chicken

```json title=""
"minecraft:brightness_filter": {
    "min": 7,
    "max": 15,
    "adjust_for_weather": false
}
```

cow

```json title=""
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

```json title=""
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_easy",
    "spawn_chance": 20
}
```

```json title=""
"minecraft:delay_filter": {
    "min": 600,
    "max": 660,
    "identifier": "minecraft:pillager_patrol_normal",
    "spawn_chance": 20
}
```

```json title=""
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

```json title=""
"minecraft:density_limit": {
    "underground": 5
}
```

bat

```json title=""
"minecraft:density_limit": {
    "surface": 5
}
```

cod

```json title=""
"minecraft:density_limit": {
    "surface": 20
}
```

creeper

```json title=""
"minecraft:density_limit": {
    "surface": 5
}
```

dolphin

```json title=""
"minecraft:density_limit": {
    "surface": 5,
    "underground": 0
}
```

drowned

```json title=""
"minecraft:density_limit": {
    "surface": 5
}
```

```json title=""
"minecraft:density_limit": {
    "surface": 2
}
```

```json title=""
"minecraft:density_limit": {
    "surface": 2
}
```

</Spoiler>

## difficulty_filter

<Spoiler title="显示">

bogged

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

creeper

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

drowned

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

enderman

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

```json title=""
"minecraft:difficulty_filter": {
    "min": "easy",
    "max": "hard"
}
```

</Spoiler>

## disallow_spawns_in_bubble

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:disallow_spawns_in_bubble": {}
```

</Spoiler>

## distance_filter

<Spoiler title="显示">

cod

```json title=""
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

pillager_patrol

```json title=""
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

```json title=""
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

```json title=""
"minecraft:distance_filter": {
    "min": 24,
    "max": 48
}
```

pufferfish

```json title=""
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

salmon

```json title=""
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

```json title=""
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

tropicalfish

```json title=""
"minecraft:distance_filter": {
    "min": 12,
    "max": 32
}
```

</Spoiler>

## height_filter

<Spoiler title="显示">

bat

```json title=""
"minecraft:height_filter": {
    "min": -63,
    "max": 63
}
```

cod

```json title=""
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

dolphin

```json title=""
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

glow_squid

```json title=""
"minecraft:height_filter": {
    "min": -64,
    "max": 30
}
```

pufferfish

```json title=""
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

salmon

```json title=""
"minecraft:height_filter": {
    "min": 0,
    "max": 64
}
```

```json title=""
"minecraft:height_filter": {
    "min": 50,
    "max": 64
}
```

stray

```json title=""
"minecraft:height_filter": {
    "min": 60,
    "max": 66
}
```

</Spoiler>

## herd

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:herd": {
    "min_size": 2,
    "max_size": 3
}
```

```json title=""
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

```json title=""
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

axolotl

```json title=""
"minecraft:herd": {
    "min_size": 4,
    "max_size": 6,
    "event": "minecraft:entity_born",
    "event_skip_count": 2
}
```

bat

```json title=""
"minecraft:herd": {
    "min_size": 2,
    "max_size": 2
}
```

bee

```json title=""
"minecraft:herd": {
    "min_size": 1,
    "max_size": 1
}
```

bogged

```json title=""
"minecraft:herd": {
    "min_size": 1,
    "max_size": 2
}
```

chicken

```json title=""
"minecraft:herd": {
    "min_size": 2,
    "max_size": 4
}
```

</Spoiler>

## mob_event_filter

<Spoiler title="显示">

pillager_patrol

```json title=""
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

```json title=""
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

```json title=""
"minecraft:mob_event_filter": {
    "event": "minecraft:pillager_patrols_event"
}
```

</Spoiler>

## permute_type

<Spoiler title="显示">

pillager_patrol

```json title=""
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

```json title=""
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

```json title=""
"minecraft:permute_type": [
    {
        "weight": 100,
        "entity_type": "minecraft:pillager<minecraft:spawn_as_patrol_follower>"
    }
]
```

zombie

```json title=""
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

```json title=""
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

```json title=""
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

```json title=""
"minecraft:player_in_village_filter": {
    "distance": 48,
    "village_border_tolerance": 32
}
```

</Spoiler>

## spawn_event

<Spoiler title="显示">

stray

```json title=""
"minecraft:spawn_event": {
    "event": "change_to_skeleton"
}
```

```json title=""
"minecraft:spawn_event": {
    "event": "change_to_skeleton"
}
```

</Spoiler>

## spawns_lava

<Spoiler title="显示">

strider

```json title=""
"minecraft:spawns_lava": {}
```

</Spoiler>

## spawns_on_block_filter

<Spoiler title="显示">

armadillo

```json title=""
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

```json title=""
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

```json title=""
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

```json title=""
"minecraft:spawns_on_block_filter": "minecraft:clay"
```

chicken

```json title=""
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

cow

```json title=""
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

donkey

```json title=""
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

```json title=""
"minecraft:spawns_on_block_filter": "minecraft:grass"
```

</Spoiler>

## spawns_on_block_prevented_filter

<Spoiler title="显示">

hoglin

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

magma_cube

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

piglin

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

skeleton

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

zombie_pigman

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

```json title=""
"minecraft:spawns_on_block_prevented_filter": [
    "minecraft:nether_wart_block",
    "minecraft:shroomlight"
]
```

</Spoiler>

## spawns_on_surface

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:spawns_on_surface": {}
```

```json title=""
"minecraft:spawns_on_surface": {}
```

```json title=""
"minecraft:spawns_on_surface": {}
```

bee

```json title=""
"minecraft:spawns_on_surface": {}
```

bogged

```json title=""
"minecraft:spawns_on_surface": {}
```

chicken

```json title=""
"minecraft:spawns_on_surface": {}
```

cod

```json title=""
"minecraft:spawns_on_surface": {}
```

cow

```json title=""
"minecraft:spawns_on_surface": {}
```

</Spoiler>

## spawns_underground

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:spawns_underground": {}
```

bat

```json title=""
"minecraft:spawns_underground": {}
```

creeper

```json title=""
"minecraft:spawns_underground": {}
```

enderman

```json title=""
"minecraft:spawns_underground": {}
```

```json title=""
"minecraft:spawns_underground": {}
```

```json title=""
"minecraft:spawns_underground": {}
```

ghast

```json title=""
"minecraft:spawns_underground": {}
```

glow_squid

```json title=""
"minecraft:spawns_underground": {}
```

</Spoiler>

## spawns_underwater

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:spawns_underwater": {}
```

cod

```json title=""
"minecraft:spawns_underwater": {}
```

dolphin

```json title=""
"minecraft:spawns_underwater": {}
```

drowned

```json title=""
"minecraft:spawns_underwater": {}
```

```json title=""
"minecraft:spawns_underwater": {}
```

```json title=""
"minecraft:spawns_underwater": {}
```

glow_squid

```json title=""
"minecraft:spawns_underwater": {}
```

guardian

```json title=""
"minecraft:spawns_underwater": {}
```

</Spoiler>

## weight

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:weight": {
    "default": 10
}
```

```json title=""
"minecraft:weight": {
    "default": 6,
    "rarity": 3
}
```

```json title=""
"minecraft:weight": {
    "default": 6,
    "rarity": 2
}
```

axolotl

```json title=""
"minecraft:weight": {
    "default": 10
}
```

bat

```json title=""
"minecraft:weight": {
    "default": 10
}
```

bee

```json title=""
"minecraft:weight": {
    "default": 10
}
```

bogged

```json title=""
"minecraft:weight": {
    "default": 40
}
```

chicken

```json title=""
"minecraft:weight": {
    "default": 10
}
```

</Spoiler>

## world_age_filter

<Spoiler title="显示">

pillager_patrol

```json title=""
"minecraft:world_age_filter": {
    "min": 6000
}
```

```json title=""
"minecraft:world_age_filter": {
    "min": 6000
}
```

```json title=""
"minecraft:world_age_filter": {
    "min": 6000
}
```

</Spoiler>