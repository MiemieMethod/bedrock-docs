---
title: Vanilla Usage Components
category: Documentation
mentions:
    - MedicalJewel105
description: Automatically generated list of entity components used in vanilla.
---

此页面是使用 [Wiki内容生成器](https://github.com/Bedrock-OSS/bedrock-wiki-content-generator) 创建的。如果有问题，请在 [Bedrock OSS](https://discord.gg/XjV87YN) Discord 服务器联系我们。
请注意，为了保持页面加载速度，每个组件最多只显示8个示例，且每个实体最多只显示3个示例。命名空间 `minecraft` 也已移除。
如果你想查看完整页面，可以点击[这里](../entities/vusr-full.md)。*最后更新于1.21.0*

## addrider

<Spoiler title="显示">

cave_spider

```json title="#component_groups/minecraft:spider_jockey"
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```json title="#component_groups/minecraft:spider_stray_jockey"
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

```json title="#component_groups/minecraft:spider_wither_jockey"
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.wither"
}
```

ravager

```json title="#component_groups/minecraft:pillager_rider"
"minecraft:addrider": {
    "entity_type": "minecraft:pillager"
}
```

```json title="#component_groups/minecraft:pillager_rider_for_raid"
"minecraft:addrider": {
    "entity_type": "minecraft:pillager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

```json title="#component_groups/minecraft:evoker_rider_for_raid"
"minecraft:addrider": {
    "entity_type": "minecraft:evocation_illager",
    "spawn_event": "minecraft:spawn_for_raid"
}
```

spider

```json title="#component_groups/minecraft:spider_jockey"
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton"
}
```

```json title="#component_groups/minecraft:spider_stray_jockey"
"minecraft:addrider": {
    "entity_type": "minecraft:skeleton.stray"
}
```

</Spoiler>

## admire_item

<Spoiler title="显示">

piglin

```json title=""
"minecraft:admire_item": {
    "duration": 8,
    "cooldown_after_being_attacked": 20
}
```

</Spoiler>

## ageable

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:baby"
"minecraft:ageable": {
    "duration": 1200,
    "interact_filters": {
        "test": "enum_property",
        "domain": "minecraft:armadillo_state",
        "value": "unrolled"
    },
    "feed_items": "spider_eye",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

axolotl

```json title="#component_groups/axolotl_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "tropical_fish_bucket",
    "transform_to_item": "water_bucket:0",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

bee

```json title="#component_groups/bee_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "minecraft:poppy",
        "minecraft:blue_orchid",
        "minecraft:allium",
        "minecraft:azure_bluet",
        "minecraft:red_tulip",
        "minecraft:orange_tulip",
        "minecraft:white_tulip",
        "minecraft:pink_tulip",
        "minecraft:oxeye_daisy",
        "minecraft:cornflower",
        "minecraft:lily_of_the_valley",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sunflower",
        "minecraft:lilac",
        "minecraft:rose_bush",
        "minecraft:peony",
        "minecraft:flowering_azalea",
        "minecraft:azalea_leaves_flowered",
        "minecraft:mangrove_propagule",
        "minecraft:pitcher_plant",
        "minecraft:torchflower",
        "minecraft:cherry_leaves",
        "minecraft:pink_petals"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

camel

```json title="#component_groups/minecraft:camel_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "cactus",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

cat

```json title="#component_groups/minecraft:cat_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

chicken

```json title="#component_groups/minecraft:chicken_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds",
        "pitcher_pod",
        "torchflower_seeds"
    ],
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

cow

```json title="#component_groups/minecraft:cow_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": "wheat",
    "grow_up": {
        "event": "minecraft:ageable_grow_up",
        "target": "self"
    }
}
```

dolphin

```json title="#component_groups/dolphin_baby"
"minecraft:ageable": {
    "duration": 1200,
    "feed_items": [
        "fish",
        "salmon"
    ],
    "grow_up": {
        "event": "ageable_grow_up",
        "target": "self"
    }
}
```

</Spoiler>

## ambient_sound_interval

<Spoiler title="显示">

allay

```json title=""
"minecraft:ambient_sound_interval": {
    "value": 5.0,
    "range": 5.0,
    "event_name": "ambient",
    "event_names": [
        {
            "event_name": "ambient.tame",
            "condition": "query.is_using_item"
        },
        {
            "event_name": "ambient",
            "condition": "!query.is_using_item"
        }
    ]
}
```

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:ambient_sound_interval": {}
```

bee

```json title="#component_groups/look_for_food"
"minecraft:ambient_sound_interval": {
    "event_name": "ambient.pollinate",
    "range": 3.0,
    "value": 2.0
}
```

```json title="#component_groups/default_sound"
"minecraft:ambient_sound_interval": {
    "event_name": "ambient",
    "range": 0.0,
    "value": 0.0
}
```

evocation_illager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:ambient_sound_interval": {
    "value": 2.0,
    "range": 4.0,
    "event_name": "ambient.in.raid"
}
```

fox

```json title="#component_groups/minecraft:fox_ambient_normal"
"minecraft:ambient_sound_interval": {
    "event_name": "ambient"
}
```

```json title="#component_groups/minecraft:fox_ambient_sleep"
"minecraft:ambient_sound_interval": {
    "event_name": "sleep"
}
```

```json title="#component_groups/minecraft:fox_ambient_night"
"minecraft:ambient_sound_interval": {
    "event_name": "screech",
    "value": 80,
    "range": 160
}
```

</Spoiler>

## anger_level

<Spoiler title="显示">

warden

```json title=""
"minecraft:anger_level": {
    "max_anger": 150,
    "angry_threshold": 80,
    "remove_targets_below_angry_threshold": true,
    "angry_boost": 20,
    "anger_decrement_interval": 1.0,
    "default_annoyingness": 35,
    "default_projectile_annoyingness": 10,
    "on_increase_sounds": [
        {
            "sound": "listening_angry",
            "condition": "query.anger_level(this) >= 40"
        },
        {
            "sound": "listening",
            "condition": "query.anger_level(this) >= 0"
        }
    ],
    "nuisance_filter": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "other",
                "operator": "not",
                "value": "warden"
            },
            {
                "test": "is_family",
                "subject": "other",
                "operator": "not",
                "value": "inanimate"
            }
        ]
    }
}
```

</Spoiler>

## angry

<Spoiler title="显示">

bee

```json title="#component_groups/angry_bee"
"minecraft:angry": {
    "duration": 25,
    "broadcastAnger": true,
    "broadcastRange": 20,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "!=",
        "value": "pacified"
    },
    "calm_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

cave_spider

```json title="#component_groups/minecraft:spider_angry"
"minecraft:angry": {
    "duration": 10,
    "duration_delta": 3,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

dolphin

```json title="#component_groups/dolphin_angry"
"minecraft:angry": {
    "duration": 25,
    "broadcast_anger": true,
    "broadcast_range": 16,
    "calm_event": {
        "event": "on_calm",
        "target": "self"
    }
}
```

enderman

```json title="#component_groups/minecraft:enderman_angry"
"minecraft:angry": {
    "duration": 25,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

hoglin

```json title="#component_groups/angry_hoglin"
"minecraft:angry": {
    "duration": 10,
    "broadcast_anger": true,
    "broadcast_range": 16,
    "calm_event": {
        "event": "become_calm_event",
        "target": "self"
    },
    "angry_sound": "angry",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

llama

```json title="#component_groups/minecraft:llama_angry"
"minecraft:angry": {
    "duration": 4,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

```json title="#component_groups/minecraft:llama_angry_wolf"
"minecraft:angry": {
    "duration": -1,
    "broadcast_anger": false,
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

panda

```json title="#component_groups/minecraft:panda_angry"
"minecraft:angry": {
    "duration": 500,
    "broadcast_anger": true,
    "broadcast_range": 41,
    "broadcast_filters": {
        "test": "is_family",
        "operator": "==",
        "value": "panda_aggressive"
    },
    "calm_event": {
        "event": "minecraft:on_calm",
        "target": "self"
    }
}
```

</Spoiler>

## annotation.break_door

<Spoiler title="显示">

drowned

```json title="#component_groups/minecraft:can_break_doors"
"minecraft:annotation.break_door": {}
```

husk

```json title="#component_groups/minecraft:can_break_doors"
"minecraft:annotation.break_door": {}
```

vindicator

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:annotation.break_door": {
    "break_time": 30,
    "min_difficulty": "normal"
}
```

zombie

```json title="#component_groups/minecraft:can_break_doors"
"minecraft:annotation.break_door": {}
```

zombie_villager

```json title="#component_groups/can_break_doors"
"minecraft:annotation.break_door": {}
```

zombie_villager_v2

```json title="#component_groups/can_break_doors"
"minecraft:annotation.break_door": {}
```

</Spoiler>

## annotation.open_door

<Spoiler title="显示">

piglin

```json title=""
"minecraft:annotation.open_door": {}
```

piglin_brute

```json title=""
"minecraft:annotation.open_door": {}
```

villager

```json title=""
"minecraft:annotation.open_door": {}
```

villager_v2

```json title=""
"minecraft:annotation.open_door": {}
```

</Spoiler>

## area_attack

<Spoiler title="显示">

magma_cube

```json title="#component_groups/minecraft:slime_large"
"minecraft:area_attack": {
    "damage_range": 0.15,
    "damage_per_tick": 6,
    "damage_cooldown": 0.5,
    "cause": "entity_attack",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            }
        ]
    }
}
```

```json title="#component_groups/minecraft:slime_medium"
"minecraft:area_attack": {
    "damage_range": 0.15,
    "damage_per_tick": 4,
    "damage_cooldown": 0.5,
    "cause": "entity_attack",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            }
        ]
    }
}
```

```json title="#component_groups/minecraft:slime_small"
"minecraft:area_attack": {
    "damage_range": 0.15,
    "damage_per_tick": 3,
    "damage_cooldown": 0.5,
    "cause": "entity_attack",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            }
        ]
    }
}
```

pufferfish

```json title="#component_groups/minecraft:full_puff"
"minecraft:area_attack": {
    "damage_range": 0.2,
    "damage_per_tick": 2,
    "damage_cooldown": 0.5,
    "cause": "contact",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

slime

```json title="#component_groups/minecraft:slime_large"
"minecraft:area_attack": {
    "damage_range": 0.15,
    "damage_per_tick": 4,
    "damage_cooldown": 0.5,
    "cause": "entity_attack",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "snowgolem"
            }
        ]
    }
}
```

```json title="#component_groups/minecraft:slime_medium"
"minecraft:area_attack": {
    "damage_range": 0.15,
    "damage_per_tick": 2,
    "damage_cooldown": 0.5,
    "cause": "entity_attack",
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "snowgolem"
            }
        ]
    }
}
```

</Spoiler>

## attack

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:attack": {
    "damage": 2
}
```

bee

```json title="#component_groups/easy_attack"
"minecraft:attack": {
    "damage": 2
}
```

```json title="#component_groups/normal_attack"
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 10
}
```

```json title="#component_groups/hard_attack"
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 18
}
```

blaze

```json title="#component_groups/melee_mode"
"minecraft:attack": {
    "damage": 6
}
```

bogged

```json title="#component_groups/minecraft:melee_attack"
"minecraft:attack": {
    "damage": 3,
    "effect_name": "slowness",
    "effect_duration": 10
}
```

cave_spider

```json title="#component_groups/minecraft:spider_poison_easy"
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 0
}
```

```json title="#component_groups/minecraft:spider_poison_normal"
"minecraft:attack": {
    "damage": 2,
    "effect_name": "poison",
    "effect_duration": 7
}
```

</Spoiler>

## attack_cooldown

<Spoiler title="显示">

axolotl

```json title="#component_groups/attack_cooldown"
"minecraft:attack_cooldown": {
    "attack_cooldown_time": 120.0,
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

goat

```json title="#component_groups/attack_cooldown"
"minecraft:attack_cooldown": {
    "attack_cooldown_time": [
        30,
        40
    ],
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

hoglin

```json title="#component_groups/attack_cooldown"
"minecraft:attack_cooldown": {
    "attack_cooldown_time": [
        10.0,
        15.0
    ],
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

piglin

```json title="#component_groups/attack_cooldown"
"minecraft:attack_cooldown": {
    "attack_cooldown_time": [
        30.0,
        120.0
    ],
    "attack_cooldown_complete_event": {
        "event": "attack_cooldown_complete_event",
        "target": "self"
    }
}
```

</Spoiler>

## attack_damage

<Spoiler title="显示">

cat

```json title=""
"minecraft:attack_damage": {
    "value": 4
}
```

ocelot

```json title=""
"minecraft:attack_damage": {
    "value": 3
}
```

</Spoiler>

## balloonable

<Spoiler title="显示">

allay

```json title=""
"minecraft:balloonable": {
    "mass": 0.5
}
```

armadillo

```json title=""
"minecraft:balloonable": {}
```

bee

```json title=""
"minecraft:balloonable": {
    "mass": 0.5
}
```

boat

```json title=""
"minecraft:balloonable": {}
```

camel

```json title=""
"minecraft:balloonable": {}
```

cat

```json title=""
"minecraft:balloonable": {
    "mass": 0.6
}
```

chest_boat

```json title=""
"minecraft:balloonable": {}
```

chicken

```json title=""
"minecraft:balloonable": {
    "mass": 0.5
}
```

</Spoiler>

## barter

<Spoiler title="显示">

piglin

```json title="#component_groups/piglin_adult"
"minecraft:barter": {
    "barter_table": "loot_tables/entities/piglin_barter.json",
    "cooldown_after_being_attacked": 20
}
```

</Spoiler>

## behavior.admire_item

<Spoiler title="显示">

piglin

```json title=""
"minecraft:behavior.admire_item": {
    "priority": 2,
    "admire_item_sound": "admire",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "on_admire_item_start": {
        "event": "admire_item_started_event",
        "target": "self"
    },
    "on_admire_item_stop": {
        "event": "admire_item_stopped_event",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.avoid_block

<Spoiler title="显示">

hoglin

```json title=""
"minecraft:behavior.avoid_block": {
    "priority": 1,
    "tick_interval": 5,
    "search_range": 8,
    "search_height": 4,
    "walk_speed_modifier": 1,
    "sprint_speed_modifier": 1,
    "avoid_block_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "target_selection_method": "nearest",
    "target_blocks": [
        "minecraft:warped_fungus",
        "minecraft:portal",
        "minecraft:respawn_anchor"
    ],
    "on_escape": [
        {
            "event": "escaped_event",
            "target": "self"
        }
    ]
}
```

piglin

```json title=""
"minecraft:behavior.avoid_block": {
    "priority": 9,
    "tick_interval": 5,
    "search_range": 8,
    "search_height": 4,
    "sprint_speed_modifier": 1.1,
    "target_selection_method": "nearest",
    "target_blocks": [
        "minecraft:soul_fire",
        "minecraft:soul_lantern",
        "minecraft:soul_torch",
        "minecraft:item.soul_campfire"
    ],
    "avoid_block_sound": "retreat",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    }
}
```

</Spoiler>

## behavior.avoid_mob_type

<Spoiler title="显示">

bogged

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wolf"
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.2,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:behavior.avoid_mob_type": {
    "priority": 6,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10,
            "walk_speed_multiplier": 0.8,
            "sprint_speed_multiplier": 1.33
        }
    ]
}
```

cave_spider

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "armadillo"
                    },
                    {
                        "test": "enum_property",
                        "subject": "other",
                        "domain": "minecraft:armadillo_state",
                        "value": "unrolled"
                    }
                ]
            },
            "max_dist": 6,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

creeper

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 3,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "ocelot"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "cat"
                    }
                ]
            },
            "max_dist": 6,
            "sprint_speed_multiplier": 1.2
        }
    ]
}
```

dolphin

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian_elder"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "guardian"
                    }
                ]
            },
            "max_dist": 8,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.0
        }
    ],
    "probability_per_strength": 0.14
}
```

evocation_illager

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 8,
            "walk_speed_multiplier": 0.6,
            "sprint_speed_multiplier": 1.0
        }
    ]
}
```

cod

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "axolotl"
                    }
                ]
            },
            "max_dist": 6,
            "walk_speed_multiplier": 1.5,
            "sprint_speed_multiplier": 2.0
        }
    ]
}
```

fox

```json title=""
"minecraft:behavior.avoid_mob_type": {
    "priority": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "trusts",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            },
                            {
                                "test": "is_sneaking",
                                "subject": "other",
                                "operator": "!=",
                                "value": true
                            }
                        ]
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "polarbear"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "wolf"
                    }
                ]
            },
            "max_dist": 10,
            "walk_speed_multiplier": 1.0,
            "sprint_speed_multiplier": 1.5
        }
    ]
}
```

</Spoiler>

## behavior.barter

<Spoiler title="显示">

piglin

```json title=""
"minecraft:behavior.barter": {
    "priority": 3
}
```

</Spoiler>

## behavior.beg

<Spoiler title="显示">

wolf

```json title=""
"minecraft:behavior.beg": {
    "priority": 9,
    "look_distance": 8,
    "look_time": [
        2,
        4
    ],
    "items": [
        "bone",
        "porkchop",
        "cooked_porkchop",
        "chicken",
        "cooked_chicken",
        "beef",
        "cooked_beef",
        "rotten_flesh",
        "muttonraw",
        "muttoncooked",
        "rabbit",
        "cooked_rabbit"
    ]
}
```

</Spoiler>

## behavior.breed

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:adult_unrolled"
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

axolotl

```json title="#component_groups/axolotl_adult"
"minecraft:behavior.breed": {
    "priority": 1,
    "speed_multiplier": 1.0
}
```

bee

```json title="#component_groups/bee_adult"
"minecraft:behavior.breed": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:behavior.breed": {
    "priority": 2,
    "speed_multiplier": 1.0
}
```

cat

```json title="#component_groups/minecraft:cat_adult"
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

chicken

```json title="#component_groups/minecraft:chicken_adult"
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

cow

```json title=""
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

```json title="#component_groups/minecraft:cow_adult"
"minecraft:behavior.breed": {
    "priority": 3,
    "speed_multiplier": 1.0
}
```

</Spoiler>

## behavior.celebrate

<Spoiler title="显示">

evocation_illager

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

pillager

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

ravager

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

vindicator

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

witch

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate": {
    "priority": 5,
    "celebration_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "jump_interval": {
        "range_min": 1.0,
        "range_max": 3.5
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.celebrate_survive

<Spoiler title="显示">

villager

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate_survive": {
    "priority": 5,
    "fireworks_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

villager_v2

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.celebrate_survive": {
    "priority": 5,
    "fireworks_interval": {
        "range_min": 2.0,
        "range_max": 7.0
    },
    "duration": 30.0,
    "on_celebration_end_event": {
        "event": "minecraft:stop_celebrating",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.charge_attack

<Spoiler title="显示">

vex

```json title=""
"minecraft:behavior.charge_attack": {
    "priority": 4
}
```

</Spoiler>

## behavior.charge_held_item

<Spoiler title="显示">

piglin

```json title="#component_groups/ranged_unit"
"minecraft:behavior.charge_held_item": {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

pillager

```json title=""
"minecraft:behavior.charge_held_item": {
    "priority": 3,
    "items": [
        "minecraft:arrow"
    ]
}
```

</Spoiler>

## behavior.circle_around_anchor

<Spoiler title="显示">

phantom

```json title=""
"minecraft:behavior.circle_around_anchor": {
    "priority": 3,
    "radius_change": 1.0,
    "radius_adjustment_chance": 0.004,
    "height_adjustment_chance": 0.002857,
    "goal_radius": 1.0,
    "angle_change": 15.0,
    "radius_range": [
        5.0,
        15.0
    ],
    "height_offset_range": [
        -4.0,
        5.0
    ],
    "height_above_target_range": [
        20.0,
        40.0
    ]
}
```

</Spoiler>

## behavior.controlled_by_player

<Spoiler title="显示">

pig

```json title="#component_groups/minecraft:pig_saddled"
"minecraft:behavior.controlled_by_player": {
    "priority": 0
}
```

strider

```json title="#component_groups/minecraft:strider_saddled"
"minecraft:behavior.controlled_by_player": {
    "priority": 0,
    "mount_speed_multiplier": 1.45
}
```

</Spoiler>

## behavior.croak

<Spoiler title="显示">

frog

```json title=""
"minecraft:behavior.croak": {
    "priority": 9,
    "interval": [
        10,
        20
    ],
    "duration": 4.5,
    "filters": {
        "all_of": [
            {
                "test": "in_water",
                "value": false
            },
            {
                "test": "in_lava",
                "value": false
            }
        ]
    }
}
```

</Spoiler>

## behavior.defend_trusted_target

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:trusting_fox"
"minecraft:behavior.defend_trusted_target": {
    "priority": 0,
    "within_radius": 25,
    "must_see": false,
    "aggro_sound": "mad",
    "sound_chance": 0.05,
    "on_defend_start": {
        "event": "minecraft:fox_configure_defending",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.defend_village_target

<Spoiler title="显示">

iron_golem

```json title="#component_groups/minecraft:village_created"
"minecraft:behavior.defend_village_target": {
    "priority": 1,
    "must_reach": true,
    "attack_chance": 0.05,
    "entity_types": {
        "filters": {
            "any_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "mob"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "player"
                }
            ]
        }
    }
}
```

</Spoiler>

## behavior.delayed_attack

<Spoiler title="显示">

ravager

```json title="#component_groups/minecraft:hostile"
"minecraft:behavior.delayed_attack": {
    "priority": 4,
    "attack_once": false,
    "track_target": true,
    "require_complete_path": false,
    "random_stop_interval": 0,
    "reach_multiplier": 1.5,
    "speed_multiplier": 1.0,
    "attack_duration": 0.75,
    "hit_delay_pct": 0.5
}
```

</Spoiler>

## behavior.dig

<Spoiler title="显示">

warden

```json title=""
"minecraft:behavior.dig": {
    "priority": 1,
    "duration": 5.5,
    "idle_time": 60.0,
    "vibration_is_disturbance": true,
    "suspicion_is_disturbance": true,
    "digs_in_daylight": false,
    "on_start": {
        "event": "on_digging_event",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.dragonchargeplayer

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_flying"
"minecraft:behavior.dragonchargeplayer": {
    "priority": 1
}
```

</Spoiler>

## behavior.dragondeath

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_death"
"minecraft:behavior.dragondeath": {
    "priority": 0
}
```

</Spoiler>

## behavior.dragonflaming

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_sitting"
"minecraft:behavior.dragonflaming": {
    "priority": 1
}
```

</Spoiler>

## behavior.dragonholdingpattern

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_flying"
"minecraft:behavior.dragonholdingpattern": {
    "priority": 3
}
```

</Spoiler>

## behavior.dragonlanding

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_sitting"
"minecraft:behavior.dragonlanding": {
    "priority": 0
}
```

</Spoiler>

## behavior.dragonscanning

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_sitting"
"minecraft:behavior.dragonscanning": {
    "priority": 2
}
```

</Spoiler>

## behavior.dragonstrafeplayer

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_flying"
"minecraft:behavior.dragonstrafeplayer": {
    "priority": 2
}
```

</Spoiler>

## behavior.dragontakeoff

<Spoiler title="显示">

ender_dragon

```json title="#component_groups/dragon_flying"
"minecraft:behavior.dragontakeoff": {
    "priority": 0
}
```

</Spoiler>

## behavior.drink_milk

<Spoiler title="显示">

wandering_trader

```json title=""
"minecraft:behavior.drink_milk": {
    "priority": 5,
    "filters": {
        "all_of": [
            {
                "test": "is_daytime",
                "value": true
            },
            {
                "test": "is_visible",
                "subject": "self",
                "value": false
            },
            {
                "test": "is_avoiding_mobs",
                "subject": "self",
                "value": false
            }
        ]
    }
}
```

</Spoiler>

## behavior.drink_potion

<Spoiler title="显示">

wandering_trader

```json title=""
"minecraft:behavior.drink_potion": {
    "priority": 1,
    "speed_modifier": -0.2,
    "potions": [
        {
            "id": 7,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "hourly_clock_time",
                                "operator": ">=",
                                "value": 18000
                            },
                            {
                                "test": "hourly_clock_time",
                                "operator": "<",
                                "value": 12000
                            }
                        ]
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "all_of": [
                                    {
                                        "test": "has_component",
                                        "subject": "self",
                                        "value": "minecraft:angry"
                                    },
                                    {
                                        "test": "is_family",
                                        "subject": "target",
                                        "operator": "!=",
                                        "value": "player"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": 8,
            "chance": 1.0,
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 18000
                    },
                    {
                        "test": "is_visible",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_avoiding_mobs",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "test": "has_component",
                                "subject": "self",
                                "value": "minecraft:angry"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

witch

```json title=""
"minecraft:behavior.drink_potion": {
    "priority": 1,
    "speed_modifier": -0.25,
    "potions": [
        {
            "id": 19,
            "chance": 0.15,
            "filters": {
                "all_of": [
                    {
                        "test": "is_underwater",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "none_of": [
                            {
                                "test": "has_mob_effect",
                                "subject": "self",
                                "value": "water_breathing"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": 12,
            "chance": 0.15,
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "on_fire",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "test": "on_hot_block",
                                "subject": "self",
                                "value": true
                            },
                            {
                                "test": "taking_fire_damage",
                                "subject": "self",
                                "value": true
                            }
                        ]
                    },
                    {
                        "none_of": [
                            {
                                "test": "has_mob_effect",
                                "subject": "self",
                                "value": "fire_resistance"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "id": 21,
            "chance": 0.05,
            "filters": {
                "all_of": [
                    {
                        "test": "is_missing_health",
                        "subject": "self",
                        "value": true
                    }
                ]
            }
        },
        {
            "id": 14,
            "chance": 0.25,
            "filters": {
                "all_of": [
                    {
                        "test": "has_target",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "none_of": [
                            {
                                "test": "has_mob_effect",
                                "subject": "self",
                                "value": "speed"
                            }
                        ]
                    },
                    {
                        "test": "target_distance",
                        "subject": "self",
                        "value": 11.0,
                        "operator": ">="
                    }
                ]
            }
        }
    ]
}
```

</Spoiler>

## behavior.drop_item_for

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_gift_for_owner"
"minecraft:behavior.drop_item_for": {
    "priority": 1,
    "seconds_before_pickup": 0.0,
    "cooldown": 0.25,
    "drop_item_chance": 0.7,
    "offering_distance": 5.0,
    "minimum_teleport_distance": 2.0,
    "max_head_look_at_height": 10.0,
    "target_range": [
        5.0,
        5.0,
        5.0
    ],
    "teleport_offset": [
        0.0,
        1.0,
        0.0
    ],
    "time_of_day_range": [
        0.74999,
        0.8
    ],
    "speed_multiplier": 1.0,
    "search_range": 5,
    "search_height": 2,
    "search_count": 0,
    "goal_radius": 1.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 6
        }
    ],
    "loot_table": "loot_tables/entities/cat_gift.json",
    "on_drop_attempt": {
        "event": "minecraft:cat_gifted_owner",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.eat_block

<Spoiler title="显示">

sheep

```json title=""
"minecraft:behavior.eat_block": {
    "priority": 6,
    "success_chance": "query.is_baby ? 0.02 : 0.001",
    "time_until_eat": 1.8,
    "eat_and_replace_block_pairs": [
        {
            "eat_block": "grass",
            "replace_block": "dirt"
        },
        {
            "eat_block": "tallgrass",
            "replace_block": "air"
        }
    ],
    "on_eat": {
        "event": "minecraft:on_eat_block",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.eat_carried_item

<Spoiler title="显示">

fox

```json title=""
"minecraft:behavior.eat_carried_item": {
    "priority": 12,
    "delay_before_eating": 28
}
```

</Spoiler>

## behavior.eat_mob

<Spoiler title="显示">

frog

```json title=""
"minecraft:behavior.eat_mob": {
    "priority": 7,
    "run_speed": 2.0,
    "eat_animation_time": 0.3,
    "pull_in_force": 0.75,
    "reach_mob_distance": 1.75,
    "eat_mob_sound": "tongue",
    "loot_table": "loot_tables/entities/frog.json"
}
```

</Spoiler>

## behavior.emerge

<Spoiler title="显示">

warden

```json title="#component_groups/emerging"
"minecraft:behavior.emerge": {
    "duration": 7.0,
    "on_done": {
        "event": "minecraft:emerged",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.enderman_leave_block

<Spoiler title="显示">

enderman

```json title=""
"minecraft:behavior.enderman_leave_block": {
    "priority": 10
}
```

</Spoiler>

## behavior.enderman_take_block

<Spoiler title="显示">

enderman

```json title=""
"minecraft:behavior.enderman_take_block": {
    "priority": 11
}
```

</Spoiler>

## behavior.equip_item

<Spoiler title="显示">

bogged

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

drowned

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

evocation_illager

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

fox

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 2
}
```

husk

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 2
}
```

piglin

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 5
}
```

pillager

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

skeleton

```json title=""
"minecraft:behavior.equip_item": {
    "priority": 3
}
```

</Spoiler>

## behavior.explore_outskirts

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.explore_outskirts": {}
```

```json title="#component_groups/wander_schedule_villager"
"minecraft:behavior.explore_outskirts": {
    "priority": 9,
    "next_xz": 5,
    "next_y": 3,
    "min_wait_time": 3.0,
    "max_wait_time": 10.0,
    "max_travel_time": 60.0,
    "speed_multiplier": 0.6,
    "explore_dist": 6.0,
    "min_perimeter": 1.0,
    "min_dist_from_target": 2.5,
    "timer_ratio": 2.0,
    "dist_from_boundary": [
        5.0,
        0.0,
        5.0
    ]
}
```

</Spoiler>

## behavior.fertilize_farm_block

<Spoiler title="显示">

villager_v2

```json title="#component_groups/work_schedule_farmer"
"minecraft:behavior.fertilize_farm_block": {
    "priority": 8
}
```

</Spoiler>

## behavior.find_cover

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:fox_thunderstorm"
"minecraft:behavior.find_cover": {
    "priority": 0,
    "speed_multiplier": 1,
    "cooldown_time": 0.0
}
```

```json title="#component_groups/minecraft:fox_day"
"minecraft:behavior.find_cover": {
    "priority": 9,
    "speed_multiplier": 1,
    "cooldown_time": 5.0
}
```

</Spoiler>

## behavior.find_mount

<Spoiler title="显示">

husk

```json title="#component_groups/minecraft:zombie_husk_jockey"
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

parrot

```json title="#component_groups/minecraft:parrot_tame"
"minecraft:behavior.find_mount": {
    "priority": 3,
    "within_radius": 16,
    "avoid_water": true,
    "start_delay": 100,
    "target_needed": false,
    "mount_distance": 2.0
}
```

piglin

```json title="#component_groups/piglin_jockey"
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

zombie

```json title="#component_groups/minecraft:zombie_jockey"
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16,
    "start_delay": 15,
    "max_failed_attempts": 20
}
```

zombie_villager

```json title="#component_groups/jockey"
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

zombie_villager_v2

```json title="#component_groups/jockey"
"minecraft:behavior.find_mount": {
    "priority": 1,
    "within_radius": 16
}
```

</Spoiler>

## behavior.find_underwater_treasure

<Spoiler title="显示">

dolphin

```json title=""
"minecraft:behavior.find_underwater_treasure": {
    "priority": 2,
    "speed_multiplier": 2.0,
    "search_range": 30,
    "stop_distance": 50
}
```

</Spoiler>

## behavior.fire_at_target

<Spoiler title="显示">

breeze

```json title=""
"minecraft:behavior.fire_at_target": {
    "projectile_def": "minecraft:breeze_wind_charge_projectile",
    "priority": 3,
    "attack_range": [
        2,
        16
    ],
    "attack_cooldown": 0.5,
    "pre_shoot_delay": 0.75,
    "post_shoot_delay": 0.2,
    "ranged_fov": 90.0,
    "owner_anchor": 2,
    "owner_offset": [
        0.0,
        0.3,
        0.0
    ],
    "target_anchor": 0,
    "target_offset": [
        0.0,
        0.5,
        0.0
    ]
}
```

</Spoiler>

## behavior.flee_sun

<Spoiler title="显示">

bogged

```json title=""
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

drowned

```json title=""
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

skeleton

```json title=""
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

stray

```json title=""
"minecraft:behavior.flee_sun": {
    "priority": 2,
    "speed_multiplier": 1
}
```

zombie_villager

```json title="#component_groups/from_abandoned_village"
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

zombie_villager_v2

```json title="#component_groups/from_abandoned_village"
"minecraft:behavior.flee_sun": {
    "priority": 4,
    "speed_multiplier": 1
}
```

</Spoiler>

## behavior.float

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.float": {
    "priority": 7
}
```

armadillo

```json title=""
"minecraft:behavior.float": {
    "priority": 0
}
```

bat

```json title=""
"minecraft:behavior.float": {
    "priority": 0
}
```

bee

```json title=""
"minecraft:behavior.float": {
    "priority": 19
}
```

blaze

```json title=""
"minecraft:behavior.float": {
    "priority": 0
}
```

breeze

```json title=""
"minecraft:behavior.float": {
    "priority": 0
}
```

camel

```json title=""
"minecraft:behavior.float": {
    "priority": 0,
    "sink_with_passengers": true
}
```

cat

```json title=""
"minecraft:behavior.float": {
    "priority": 0
}
```

</Spoiler>

## behavior.float_wander

<Spoiler title="显示">

bat

```json title=""
"minecraft:behavior.float_wander": {
    "xz_dist": 10,
    "y_dist": 7,
    "y_offset": -2.0,
    "random_reselect": true,
    "float_duration": [
        0.1,
        0.35
    ]
}
```

ghast

```json title=""
"minecraft:behavior.float_wander": {
    "priority": 2,
    "must_reach": true
}
```

</Spoiler>

## behavior.follow_caravan

<Spoiler title="显示">

llama

```json title=""
"minecraft:behavior.follow_caravan": {
    "priority": 3,
    "speed_multiplier": 2.1,
    "entity_count": 10,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "llama"
        }
    }
}
```

trader_llama

```json title=""
"minecraft:behavior.follow_caravan": {
    "priority": 3,
    "speed_multiplier": 2.1,
    "entity_count": 10,
    "entity_types": {
        "filters": {
            "test": "is_family",
            "subject": "other",
            "value": "llama"
        }
    }
}
```

</Spoiler>

## behavior.follow_mob

<Spoiler title="显示">

parrot

```json title="#component_groups/minecraft:parrot_wild"
"minecraft:behavior.follow_mob": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "stop_distance": 3,
    "search_range": 20
}
```

</Spoiler>

## behavior.follow_owner

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.follow_owner": {
    "priority": 6,
    "speed_multiplier": 8,
    "start_distance": 16,
    "stop_distance": 4,
    "can_teleport": false,
    "ignore_vibration": false
}
```

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

ocelot

```json title="#component_groups/minecraft:ocelot_tame"
"minecraft:behavior.follow_owner": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

parrot

```json title="#component_groups/minecraft:parrot_tame"
"minecraft:behavior.follow_owner": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "start_distance": 5,
    "stop_distance": 1
}
```

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:behavior.follow_owner": {
    "priority": 6,
    "speed_multiplier": 1.0,
    "start_distance": 10,
    "stop_distance": 2
}
```

</Spoiler>

## behavior.follow_parent

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:baby_unrolled"
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.25
}
```

axolotl

```json title="#component_groups/axolotl_baby"
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

bee

```json title="#component_groups/bee_baby"
"minecraft:behavior.follow_parent": {
    "priority": 11,
    "speed_multiplier": 1.1
}
```

camel

```json title="#component_groups/minecraft:camel_baby"
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 2.5
}
```

chicken

```json title="#component_groups/minecraft:chicken_baby"
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

cow

```json title=""
"minecraft:behavior.follow_parent": {
    "priority": 5,
    "speed_multiplier": 1.1
}
```

```json title="#component_groups/minecraft:cow_baby"
"minecraft:behavior.follow_parent": {
    "priority": 6,
    "speed_multiplier": 1.1
}
```

dolphin

```json title="#component_groups/dolphin_baby"
"minecraft:behavior.follow_parent": {
    "priority": 4,
    "speed_multiplier": 1.1
}
```

</Spoiler>

## behavior.follow_target_captain

<Spoiler title="显示">

pillager

```json title="#component_groups/minecraft:patrol_follower"
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

vindicator

```json title="#component_groups/minecraft:patrol_follower"
"minecraft:behavior.follow_target_captain": {
    "priority": 5,
    "speed_multiplier": 0.8,
    "within_radius": 64,
    "follow_distance": 5
}
```

</Spoiler>

## behavior.go_and_give_items_to_noteblock

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.go_and_give_items_to_noteblock": {
    "priority": 3,
    "run_speed": 8,
    "throw_sound": "item_thrown",
    "on_item_throw": [
        {
            "event": "pickup_item_delay",
            "target": "self"
        }
    ]
}
```

</Spoiler>

## behavior.go_and_give_items_to_owner

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.go_and_give_items_to_owner": {
    "priority": 4,
    "run_speed": 8,
    "throw_sound": "item_thrown",
    "on_item_throw": [
        {
            "event": "pickup_item_delay",
            "target": "self"
        }
    ]
}
```

</Spoiler>

## behavior.go_home

<Spoiler title="显示">

bee

```json title="#component_groups/return_to_home"
"minecraft:behavior.go_home": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "interval": 1,
    "goal_radius": 1.2,
    "on_home": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:bee_nest"
                    },
                    {
                        "test": "is_block",
                        "subject": "block",
                        "operator": "!=",
                        "value": "minecraft:beehive"
                    }
                ]
            },
            "event": "find_hive_event",
            "target": "self"
        }
    ],
    "on_failed": [
        {
            "event": "find_hive_event",
            "target": "self"
        }
    ]
}
```

piglin_brute

```json title="#component_groups/go_back_to_spawn"
"minecraft:behavior.go_home": {
    "priority": 6,
    "interval": 200,
    "speed_multiplier": 0.6,
    "goal_radius": 4.0,
    "on_failed": [
        {
            "event": "go_back_to_spawn_failed",
            "target": "self"
        }
    ]
}
```

turtle

```json title="#component_groups/minecraft:pregnant"
"minecraft:behavior.go_home": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "interval": 700,
    "goal_radius": 4.0,
    "on_home": [
        {
            "event": "minecraft:go_lay_egg",
            "target": "self"
        }
    ]
}
```

</Spoiler>

## behavior.guardian_attack

<Spoiler title="显示">

elder_guardian

```json title=""
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

guardian

```json title=""
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

```json title="#component_groups/minecraft:guardian_aggressive"
"minecraft:behavior.guardian_attack": {
    "priority": 4
}
```

</Spoiler>

## behavior.harvest_farm_block

<Spoiler title="显示">

villager

```json title="#component_groups/behavior_peasant"
"minecraft:behavior.harvest_farm_block": {
    "priority": 9,
    "speed_multiplier": 0.5
}
```

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.harvest_farm_block": {}
```

```json title="#component_groups/work_schedule_farmer"
"minecraft:behavior.harvest_farm_block": {
    "priority": 7
}
```

</Spoiler>

## behavior.hide

<Spoiler title="显示">

villager_v2

```json title=""
"minecraft:behavior.hide": {
    "priority": 0,
    "speed_multiplier": 0.8,
    "poi_type": "bed",
    "duration": 30.0
}
```

</Spoiler>

## behavior.hold_ground

<Spoiler title="显示">

pillager

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:behavior.hold_ground": {
    "priority": 5,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:ranged_mode",
        "target": "self"
    }
}
```

```json title="#component_groups/minecraft:patrol_follower"
"minecraft:behavior.hold_ground": {
    "priority": 6,
    "min_radius": 10,
    "broadcast": true,
    "broadcast_range": 8,
    "within_radius_event": {
        "event": "minecraft:ranged_mode",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.hurt_by_target

<Spoiler title="显示">

bee

```json title="#component_groups/track_attacker"
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

blaze

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

bogged

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "operator": "!=",
                "value": "breeze"
            }
        }
    ]
}
```

breeze

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 4,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "skeleton"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "stray"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "zombie"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "husk"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "spider"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "cavespider"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "slime"
                    }
                ]
            }
        }
    ]
}
```

cave_spider

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 1,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "operator": "!=",
                "value": "breeze"
            }
        }
    ]
}
```

creeper

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 2
}
```

dolphin

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

drowned

```json title=""
"minecraft:behavior.hurt_by_target": {
    "priority": 1
}
```

</Spoiler>

## behavior.inspect_bookshelf

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.inspect_bookshelf": {}
```

```json title="#component_groups/work_schedule_librarian"
"minecraft:behavior.inspect_bookshelf": {
    "priority": 8,
    "speed_multiplier": 0.6,
    "search_range": 4,
    "search_height": 3,
    "goal_radius": 0.8,
    "search_count": 0
}
```

</Spoiler>

## behavior.investigate_suspicious_location

<Spoiler title="显示">

warden

```json title=""
"minecraft:behavior.investigate_suspicious_location": {
    "priority": 5,
    "speed_multiplier": 0.7
}
```

</Spoiler>

## behavior.jump_around_target

<Spoiler title="显示">

breeze

```json title=""
"minecraft:behavior.jump_around_target": {
    "priority": 5,
    "filters": {
        "all_of": [
            {
                "any_of": [
                    {
                        "test": "in_water",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "value": true
                    }
                ]
            },
            {
                "test": "is_riding",
                "value": false
            },
            {
                "test": "in_lava",
                "value": false
            }
        ]
    },
    "jump_cooldown_duration": 0.5,
    "jump_cooldown_when_hurt_duration": 0.1,
    "last_hurt_duration": 2.0,
    "prepare_jump_duration": 0.5,
    "max_jump_velocity": 1.4,
    "check_collision": false,
    "entity_bounding_box_scale": 0.7,
    "line_of_sight_obstruction_height_ignore": 4,
    "valid_distance_to_target": [
        4.0,
        20.0
    ],
    "landing_position_spread_degrees": 90,
    "landing_distance_from_target": [
        4.0,
        8.0
    ],
    "required_vertical_space": 4,
    "snap_to_surface_block_range": 10,
    "jump_angles": [
        40.0,
        55.0,
        60.0,
        75.0,
        80.0
    ]
}
```

</Spoiler>

## behavior.jump_to_block

<Spoiler title="显示">

frog

```json title=""
"minecraft:behavior.jump_to_block": {
    "priority": 10,
    "search_width": 8,
    "search_height": 4,
    "minimum_path_length": 2,
    "minimum_distance": 1,
    "scale_factor": 0.6,
    "max_velocity": 1,
    "cooldown_range": [
        5,
        7
    ],
    "preferred_blocks": [
        "minecraft:waterlily",
        "minecraft:big_dripleaf"
    ],
    "preferred_blocks_chance": 0.5,
    "forbidden_blocks": [
        "minecraft:water"
    ]
}
```

goat

```json title=""
"minecraft:behavior.jump_to_block": {
    "priority": 8,
    "search_width": 10,
    "search_height": 10,
    "minimum_path_length": 8,
    "minimum_distance": 1,
    "scale_factor": 0.6,
    "cooldown_range": [
        30,
        60
    ]
}
```

</Spoiler>

## behavior.knockback_roar

<Spoiler title="显示">

ravager

```json title="#component_groups/roaring"
"minecraft:behavior.knockback_roar": {
    "priority": 1,
    "duration": 1,
    "attack_time": 0.5,
    "knockback_damage": 6,
    "knockback_horizontal_strength": 3,
    "knockback_vertical_strength": 3,
    "knockback_range": 4,
    "knockback_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "ravager"
    },
    "damage_filters": {
        "test": "is_family",
        "subject": "other",
        "operator": "!=",
        "value": "illager"
    },
    "on_roar_end": {
        "event": "minecraft:end_roar"
    },
    "cooldown_time": 0.1
}
```

</Spoiler>

## behavior.lay_down

<Spoiler title="显示">

panda

```json title="#component_groups/minecraft:panda_lazy"
"minecraft:behavior.lay_down": {
    "priority": 5,
    "interval": 400,
    "random_stop_interval": 2000
}
```

</Spoiler>

## behavior.lay_egg

<Spoiler title="显示">

frog

```json title="#component_groups/pregnant"
"minecraft:behavior.lay_egg": {
    "priority": 2,
    "speed_multiplier": 1.0,
    "search_range": 10,
    "search_height": 3,
    "goal_radius": 1.7,
    "target_blocks": [
        "minecraft:water"
    ],
    "target_materials_above_block": [
        "Air"
    ],
    "allow_laying_from_below": true,
    "use_default_animation": false,
    "lay_seconds": 2,
    "egg_type": "minecraft:frog_spawn",
    "lay_egg_sound": "lay_spawn",
    "on_lay": {
        "event": "laid_egg",
        "target": "self"
    }
}
```

turtle

```json title="#component_groups/minecraft:wants_to_lay_egg"
"minecraft:behavior.lay_egg": {
    "priority": 1,
    "speed_multiplier": 1.0,
    "search_range": 16,
    "search_height": 4,
    "goal_radius": 1.5,
    "on_lay": {
        "event": "minecraft:laid_egg",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.leap_at_target

<Spoiler title="显示">

cat

```json title=""
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

cave_spider

```json title="#component_groups/minecraft:spider_hostile"
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

```json title="#component_groups/minecraft:spider_angry"
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

ocelot

```json title=""
"minecraft:behavior.leap_at_target": {
    "priority": 3,
    "target_dist": 0.3
}
```

spider

```json title="#component_groups/minecraft:spider_angry"
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4,
    "must_be_on_ground": false
}
```

wolf

```json title=""
"minecraft:behavior.leap_at_target": {
    "priority": 4,
    "yd": 0.4
}
```

</Spoiler>

## behavior.look_at_entity

<Spoiler title="显示">

evocation_illager

```json title=""
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8.0,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

ravager

```json title="#component_groups/minecraft:hostile"
"minecraft:behavior.look_at_entity": {
    "priority": 10,
    "look_distance": 8,
    "angle_of_view_horizontal": 45,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

vex

```json title=""
"minecraft:behavior.look_at_entity": {
    "priority": 9,
    "look_distance": 6.0,
    "probability": 0.02,
    "filters": {
        "test": "is_family",
        "subject": "other",
        "value": "mob"
    }
}
```

</Spoiler>

## behavior.look_at_player

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 8,
    "target_distance": 6.0,
    "probability": 0.02
}
```

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "target_distance": 6.0,
    "probability": 0.02,
    "min_look_time": 40,
    "max_look_time": 80
}
```

axolotl

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 10,
    "target_distance": 6.0,
    "probability": 0.02
}
```

bogged

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 8
}
```

breeze

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 16
}
```

camel

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "target_distance": 6.0,
    "probability": 0.02
}
```

cat

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 9
}
```

cave_spider

```json title=""
"minecraft:behavior.look_at_player": {
    "priority": 7,
    "look_distance": 6.0,
    "probability": 0.02
}
```

</Spoiler>

## behavior.look_at_target

<Spoiler title="显示">

wither

```json title=""
"minecraft:behavior.look_at_target": {
    "priority": 5
}
```

</Spoiler>

## behavior.look_at_trading_player

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.look_at_trading_player": {
    "priority": 2
}
```

villager_v2

```json title=""
"minecraft:behavior.look_at_trading_player": {
    "priority": 7
}
```

wandering_trader

```json title=""
"minecraft:behavior.look_at_trading_player": {
    "priority": 4
}
```

</Spoiler>

## behavior.make_love

<Spoiler title="显示">

villager

```json title="#component_groups/adult"
"minecraft:behavior.make_love": {
    "priority": 6
}
```

villager_v2

```json title="#component_groups/make_and_receive_love"
"minecraft:behavior.make_love": {
    "priority": 5
}
```

</Spoiler>

## behavior.melee_attack

<Spoiler title="显示">

creeper

```json title=""
"minecraft:behavior.melee_attack": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "track_target": false,
    "reach_multiplier": 0.0
}
```

</Spoiler>

## behavior.melee_box_attack

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.melee_box_attack": {
    "priority": 4,
    "on_kill": {
        "event": "killed_enemy_event",
        "target": "self"
    }
}
```

bee

```json title="#component_groups/angry_bee"
"minecraft:behavior.melee_box_attack": {
    "priority": 2,
    "attack_once": true,
    "speed_multiplier": 1.4,
    "on_attack": {
        "event": "countdown_to_perish_event",
        "target": "self"
    }
}
```

blaze

```json title="#component_groups/melee_mode"
"minecraft:behavior.melee_box_attack": {
    "priority": 3
}
```

bogged

```json title="#component_groups/minecraft:melee_attack"
"minecraft:behavior.melee_box_attack": {
    "priority": 4,
    "track_target": true,
    "speed_multiplier": 1.25
}
```

cave_spider

```json title="#component_groups/minecraft:spider_hostile"
"minecraft:behavior.melee_box_attack": {
    "priority": 3,
    "track_target": true,
    "random_stop_interval": 100
}
```

```json title="#component_groups/minecraft:spider_angry"
"minecraft:behavior.melee_box_attack": {
    "priority": 3,
    "track_target": true
}
```

dolphin

```json title="#component_groups/dolphin_adult"
"minecraft:behavior.melee_box_attack": {
    "priority": 2,
    "track_target": true
}
```

drowned

```json title="#component_groups/minecraft:melee_mode"
"minecraft:behavior.melee_box_attack": {
    "can_spread_on_fire": true,
    "priority": 3,
    "speed_multiplier": 1,
    "track_target": false,
    "require_complete_path": true
}
```

</Spoiler>

## behavior.mingle

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.mingle": {}
```

```json title="#component_groups/gather_schedule_villager"
"minecraft:behavior.mingle": {
    "priority": 7,
    "speed_multiplier": 0.5,
    "duration": 30,
    "cooldown_time": 10,
    "mingle_partner_type": "minecraft:villager_v2",
    "mingle_distance": 2.0
}
```

</Spoiler>

## behavior.mount_pathing

<Spoiler title="显示">

cat

```json title=""
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0,
    "track_target": true
}
```

cave_spider

```json title=""
"minecraft:behavior.mount_pathing": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

chicken

```json title=""
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

cow

```json title=""
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

donkey

```json title="#component_groups/minecraft:donkey_wild"
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

horse

```json title="#component_groups/minecraft:horse_wild"
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.5,
    "target_dist": 0.0,
    "track_target": true
}
```

husk

```json title="#component_groups/minecraft:zombie_husk_adult"
"minecraft:behavior.mount_pathing": {
    "priority": 2,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

llama

```json title=""
"minecraft:behavior.mount_pathing": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "target_dist": 0.0,
    "track_target": true
}
```

</Spoiler>

## behavior.move_away_from_target

<Spoiler title="显示">

breeze

```json title=""
"minecraft:behavior.move_away_from_target": {
    "priority": 2,
    "destination_position_range": [
        4.0,
        8.0
    ],
    "movement_speed": 1.2,
    "destination_pos_spread_degrees": 90,
    "filters": {
        "all_of": [
            {
                "test": "on_ground",
                "value": true
            },
            {
                "test": "target_distance",
                "subject": "self",
                "value": 4.0,
                "operator": "<="
            }
        ]
    }
}
```

</Spoiler>

## behavior.move_indoors

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.move_indoors": {
    "priority": 4,
    "speed_multiplier": 0.8
}
```

villager_v2

```json title=""
"minecraft:behavior.move_indoors": {
    "priority": 6,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

</Spoiler>

## behavior.move_outdoors

<Spoiler title="显示">

villager

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.move_outdoors": {
    "priority": 2,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

villager_v2

```json title="#component_groups/minecraft:celebrate"
"minecraft:behavior.move_outdoors": {
    "priority": 2,
    "speed_multiplier": 0.8,
    "timeout_cooldown": 8.0
}
```

</Spoiler>

## behavior.move_through_village

<Spoiler title="显示">

iron_golem

```json title=""
"minecraft:behavior.move_through_village": {
    "priority": 3,
    "speed_multiplier": 0.6,
    "only_at_night": true
}
```

</Spoiler>

## behavior.move_to_block

<Spoiler title="显示">

bee

```json title="#component_groups/look_for_food"
"minecraft:behavior.move_to_block": {
    "priority": 10,
    "tick_interval": 1,
    "start_chance": 0.5,
    "search_range": 6,
    "search_height": 4,
    "goal_radius": 1.0,
    "stay_duration": 20.0,
    "target_selection_method": "random",
    "target_offset": [
        0,
        0.25,
        0
    ],
    "target_block_filters": {
        "test": "is_waterlogged",
        "subject": "block",
        "operator": "==",
        "value": false
    },
    "target_blocks": [
        "minecraft:poppy",
        "minecraft:blue_orchid",
        "minecraft:allium",
        "minecraft:azure_bluet",
        "minecraft:red_tulip",
        "minecraft:orange_tulip",
        "minecraft:white_tulip",
        "minecraft:pink_tulip",
        "minecraft:oxeye_daisy",
        "minecraft:cornflower",
        "minecraft:lily_of_the_valley",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sunflower",
        "minecraft:lilac",
        "minecraft:rose_bush",
        "minecraft:peony",
        "minecraft:flowering_azalea",
        "minecraft:azalea_leaves_flowered",
        "minecraft:mangrove_propagule",
        "minecraft:pitcher_plant",
        "minecraft:torchflower",
        "minecraft:cherry_leaves",
        "minecraft:pink_petals"
    ],
    "on_stay_completed": [
        {
            "event": "collected_nectar",
            "target": "self"
        }
    ]
}
```

```json title="#component_groups/find_hive"
"minecraft:behavior.move_to_block": {
    "priority": 10,
    "search_range": 16,
    "search_height": 10,
    "tick_interval": 1,
    "goal_radius": 0.633,
    "target_blocks": [
        "bee_nest",
        "beehive"
    ],
    "on_reach": [
        {
            "event": "minecraft:bee_returned_to_hive",
            "target": "block"
        }
    ]
}
```

</Spoiler>

## behavior.move_to_land

<Spoiler title="显示">

frog

```json title=""
"minecraft:behavior.move_to_land": {
    "priority": 6,
    "search_range": 30,
    "search_height": 8,
    "search_count": 80,
    "goal_radius": 2
}
```

turtle

```json title="#component_groups/minecraft:adult"
"minecraft:behavior.move_to_land": {
    "priority": 6,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 0.5
}
```

</Spoiler>

## behavior.move_to_liquid

<Spoiler title="显示">

strider

```json title="#component_groups/minecraft:strider_pathing_behaviors"
"minecraft:behavior.move_to_liquid": {
    "priority": 7,
    "search_range": 16,
    "search_height": 10,
    "goal_radius": 0.9,
    "material_type": "Lava",
    "search_count": 30
}
```

</Spoiler>

## behavior.move_to_random_block

<Spoiler title="显示">

pillager

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:behavior.move_to_random_block": {
    "priority": 6,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

vindicator

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:behavior.move_to_random_block": {
    "priority": 5,
    "speed_multiplier": 0.55,
    "within_radius": 8,
    "block_distance": 512
}
```

</Spoiler>

## behavior.move_to_village

<Spoiler title="显示">

evocation_illager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:behavior.move_to_village": {
    "priority": 6,
    "speed_multiplier": 0.7
}
```

pillager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

ravager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:behavior.move_to_village": {
    "priority": 5,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

vindicator

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:behavior.move_to_village": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "goal_radius": 2.0
}
```

witch

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:behavior.move_to_village": {
    "priority": 3,
    "speed_multiplier": 1.2,
    "goal_radius": 2.0
}
```

</Spoiler>

## behavior.move_to_water

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.move_to_water": {
    "priority": 6,
    "search_range": 16,
    "search_height": 5,
    "search_count": 1,
    "goal_radius": 0.1
}
```

dolphin

```json title=""
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5
}
```

frog

```json title="#component_groups/pregnant"
"minecraft:behavior.move_to_water": {
    "priority": 3,
    "search_range": 20,
    "search_height": 5,
    "goal_radius": 1.5
}
```

turtle

```json title=""
"minecraft:behavior.move_to_water": {
    "priority": 4,
    "search_range": 16,
    "search_height": 5,
    "goal_radius": 1.5
}
```

```json title="#component_groups/minecraft:baby"
"minecraft:behavior.move_to_water": {
    "priority": 1,
    "search_range": 15,
    "search_height": 5,
    "goal_radius": 0.1
}
```

</Spoiler>

## behavior.move_towards_dwelling_restriction

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 7
}
```

iron_golem

```json title=""
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 4,
    "speed_multiplier": 1
}
```

villager_v2

```json title=""
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 11,
    "speed_multiplier": 0.6
}
```

</Spoiler>

## behavior.move_towards_home_restriction

<Spoiler title="显示">

bee

```json title=""
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 9
}
```

elder_guardian

```json title=""
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

guardian

```json title=""
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

wandering_trader

```json title=""
"minecraft:behavior.move_towards_home_restriction": {
    "priority": 6,
    "speed_multiplier": 0.6
}
```

</Spoiler>

## behavior.move_towards_target

<Spoiler title="显示">

iron_golem

```json title=""
"minecraft:behavior.move_towards_target": {
    "priority": 2,
    "speed_multiplier": 0.9,
    "within_radius": 32
}
```

</Spoiler>

## behavior.nap

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:fox_day"
"minecraft:behavior.nap": {
    "priority": 8,
    "cooldown_min": 2.0,
    "cooldown_max": 7.0,
    "mob_detect_dist": 12.0,
    "mob_detect_height": 6.0,
    "can_nap_filters": {
        "all_of": [
            {
                "test": "in_water",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            {
                "test": "on_ground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_underground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "weather_at_position",
                "subject": "self",
                "operator": "!=",
                "value": "thunderstorm"
            }
        ]
    },
    "wake_mob_exceptions": {
        "any_of": [
            {
                "test": "trusts",
                "subject": "other",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_family",
                "subject": "other",
                "operator": "==",
                "value": "fox"
            },
            {
                "test": "is_sneaking",
                "subject": "other",
                "operator": "==",
                "value": true
            }
        ]
    }
}
```

</Spoiler>

## behavior.nearest_attackable_target

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.nearest_attackable_target": {
    "priority": 3,
    "must_see": true,
    "reselect_targets": true,
    "within_radius": 20.0,
    "must_see_forget_duration": 17.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "in_water",
                        "subject": "other",
                        "value": true
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "operator": "!=",
                        "value": "minecraft:attack_cooldown"
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "squid"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "fish"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "tadpole"
                            }
                        ]
                    }
                ]
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "in_water",
                        "subject": "other",
                        "value": true
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "drowned"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "guardian"
                            },
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "guardian_elder"
                            }
                        ]
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

bee

```json title="#component_groups/take_nearest_target"
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 10
        }
    ]
}
```

blaze

```json title=""
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 48.0
        }
    ]
}
```

bogged

```json title=""
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "reselect_targets": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 16
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

breeze

```json title=""
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "within_radius": 24,
    "scan_interval": 10,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 24
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "irongolem"
            },
            "max_dist": 24
        }
    ],
    "must_see": true
}
```

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:behavior.nearest_attackable_target": {
    "priority": 1,
    "reselect_targets": true,
    "within_radius": 16.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 8
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 8
        }
    ]
}
```

cave_spider

```json title="#component_groups/minecraft:spider_hostile"
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "attack_interval": 5,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

```json title="#component_groups/minecraft:spider_angry"
"minecraft:behavior.nearest_attackable_target": {
    "priority": 2,
    "must_see": true,
    "attack_interval": 10,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "max_dist": 16
        }
    ]
}
```

</Spoiler>

## behavior.nearest_prioritized_attackable_target

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:fox_red"
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 0
        }
    ]
}
```

```json title="#component_groups/minecraft:fox_arctic"
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 6,
    "attack_interval": 2,
    "reselect_targets": true,
    "target_search_height": 5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "rabbit"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "chicken"
            },
            "max_dist": 12,
            "priority": 1
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "cod"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "salmon"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "tropicalfish"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "baby_turtle"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    }
                ]
            },
            "max_dist": 12,
            "priority": 1
        }
    ]
}
```

piglin_brute

```json title="#component_groups/alert_for_attack_targets"
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 3,
    "within_radius": 12.0,
    "persist_time": 2.0,
    "must_see": true,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 12,
            "priority": 0
        },
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "wither"
            },
            "max_dist": 12,
            "priority": 1
        }
    ]
}
```

witch

```json title=""
"minecraft:behavior.nearest_prioritized_attackable_target": {
    "priority": 2,
    "entity_types": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "snowgolem"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "irongolem"
                    }
                ]
            },
            "priority": 1,
            "max_dist": 10
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_raider",
                        "subject": "other",
                        "value": true
                    },
                    {
                        "test": "is_raider",
                        "subject": "self",
                        "value": true
                    },
                    {
                        "none_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "witch"
                            }
                        ]
                    }
                ]
            },
            "priority": 2,
            "cooldown": 10,
            "max_dist": 10
        }
    ],
    "must_reach": true
}
```

</Spoiler>

## behavior.ocelot_sit_on_block

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 7,
    "speed_multiplier": 1.0
}
```

ocelot

```json title="#component_groups/minecraft:ocelot_tame"
"minecraft:behavior.ocelot_sit_on_block": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

</Spoiler>

## behavior.ocelotattack

<Spoiler title="显示">

cat

```json title=""
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "cooldown_time": 1.0,
    "x_max_rotation": 30.0,
    "y_max_head_rotation": 30.0,
    "max_distance": 15.0,
    "max_sneak_range": 15.0,
    "max_sprint_range": 4.0,
    "reach_multiplier": 2.0,
    "sneak_speed_multiplier": 0.6,
    "sprint_speed_multiplier": 1.33,
    "walk_speed_multiplier": 0.8
}
```

ocelot

```json title=""
"minecraft:behavior.ocelotattack": {
    "priority": 4,
    "cooldown_time": 1.0,
    "x_max_rotation": 30.0,
    "y_max_head_rotation": 30.0,
    "max_distance": 15.0,
    "max_sneak_range": 15.0,
    "max_sprint_range": 4.0,
    "reach_multiplier": 2.0,
    "sneak_speed_multiplier": 0.6,
    "sprint_speed_multiplier": 1.33,
    "walk_speed_multiplier": 0.8
}
```

</Spoiler>

## behavior.offer_flower

<Spoiler title="显示">

iron_golem

```json title=""
"minecraft:behavior.offer_flower": {
    "priority": 5,
    "filters": {
        "all_of": [
            {
                "test": "is_daytime",
                "value": true
            }
        ]
    }
}
```

</Spoiler>

## behavior.open_door

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
}
```

</Spoiler>

## behavior.owner_hurt_by_target

<Spoiler title="显示">

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:behavior.owner_hurt_by_target": {
    "priority": 1
}
```

</Spoiler>

## behavior.owner_hurt_target

<Spoiler title="显示">

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:behavior.owner_hurt_target": {
    "priority": 2
}
```

</Spoiler>

## behavior.panic

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 2.0
}
```

armadillo

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "ignore_mob_damage": true,
    "speed_multiplier": 2.0
}
```

bee

```json title="#component_groups/escape_fire"
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "force": true
}
```

```json title="#component_groups/countdown_to_perish"
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25,
    "force": true
}
```

camel

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 4
}
```

cat

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

chicken

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.5
}
```

cow

```json title=""
"minecraft:behavior.panic": {
    "priority": 1,
    "speed_multiplier": 1.25
}
```

</Spoiler>

## behavior.pet_sleep_with_owner

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:behavior.pet_sleep_with_owner": {
    "priority": 2,
    "speed_multiplier": 1.2,
    "search_radius": 10,
    "search_height": 10,
    "goal_radius": 1.0
}
```

</Spoiler>

## behavior.pickup_items

<Spoiler title="显示">

allay

```json title="#component_groups/pickup_item"
"minecraft:behavior.pickup_items": {
    "priority": 2,
    "max_dist": 32,
    "search_height": 32,
    "goal_radius": 2.2,
    "speed_multiplier": 6,
    "pickup_based_on_chance": false,
    "can_pickup_any_item": false,
    "can_pickup_to_hand_or_equipment": false,
    "pickup_same_items_as_in_hand": true
}
```

bogged

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 5,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true
}
```

drowned

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true,
    "excluded_items": [
        "minecraft:glow_ink_sac"
    ]
}
```

evocation_illager

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 7,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0
}
```

fox

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 11,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 0.5
}
```

husk

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0,
    "pickup_based_on_chance": true,
    "can_pickup_any_item": true,
    "excluded_items": [
        "minecraft:glow_ink_sac"
    ]
}
```

piglin

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 6,
    "max_dist": 10,
    "goal_radius": 2,
    "speed_multiplier": 0.8,
    "pickup_based_on_chance": false,
    "can_pickup_any_item": false,
    "cooldown_after_being_attacked": 20.0
}
```

pillager

```json title=""
"minecraft:behavior.pickup_items": {
    "priority": 7,
    "max_dist": 3,
    "goal_radius": 2,
    "speed_multiplier": 1.0
}
```

</Spoiler>

## behavior.play

<Spoiler title="显示">

villager

```json title="#component_groups/baby"
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.32
}
```

villager_v2

```json title="#component_groups/play_schedule_villager"
"minecraft:behavior.play": {
    "priority": 8,
    "speed_multiplier": 0.6,
    "friend_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "villager"
                    },
                    {
                        "test": "is_baby",
                        "subject": "other",
                        "operator": "==",
                        "value": true
                    }
                ]
            }
        }
    ]
}
```

</Spoiler>

## behavior.play_dead

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.play_dead": {
    "priority": 0,
    "duration": 10,
    "force_below_health": 8,
    "random_start_chance": 0.33,
    "random_damage_range": [
        0,
        2
    ],
    "damage_sources": [
        "contact",
        "entity_attack",
        "entity_explosion",
        "magic",
        "projectile",
        "thorns",
        "wither"
    ],
    "apply_regeneration": true,
    "filters": {
        "test": "in_water",
        "operator": "==",
        "value": true
    }
}
```

</Spoiler>

## behavior.player_ride_tamed

<Spoiler title="显示">

camel

```json title="#component_groups/minecraft:camel_saddled"
"minecraft:behavior.player_ride_tamed": {}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:behavior.player_ride_tamed": {}
```

horse

```json title="#component_groups/minecraft:horse_saddled"
"minecraft:behavior.player_ride_tamed": {}
```

mule

```json title="#component_groups/minecraft:mule_saddled"
"minecraft:behavior.player_ride_tamed": {}
```

skeleton_horse

```json title=""
"minecraft:behavior.player_ride_tamed": {}
```

zombie_horse

```json title="#component_groups/minecraft:horse_adult"
"minecraft:behavior.player_ride_tamed": {}
```

</Spoiler>

## behavior.raid_garden

<Spoiler title="显示">

fox

```json title=""
"minecraft:behavior.raid_garden": {
    "priority": 12,
    "blocks": [
        "minecraft:sweet_berry_bush",
        "minecraft:cave_vines_head_with_berries",
        "minecraft:cave_vines_body_with_berries"
    ],
    "speed_multiplier": 1.2,
    "search_range": 12,
    "search_height": 2,
    "goal_radius": 0.8,
    "max_to_eat": 0,
    "initial_eat_delay": 2
}
```

rabbit

```json title=""
"minecraft:behavior.raid_garden": {
    "priority": 5,
    "blocks": [
        "minecraft:carrots"
    ],
    "search_range": 16,
    "goal_radius": 1.0,
    "speed_multiplier": 0.6
}
```

</Spoiler>

## behavior.ram_attack

<Spoiler title="显示">

goat

```json title="#component_groups/ram_default"
"minecraft:behavior.ram_attack": {
    "priority": 5,
    "run_speed": 0.7,
    "ram_speed": 1.8,
    "min_ram_distance": 4,
    "ram_distance": 7,
    "knockback_force": 2.5,
    "knockback_height": 0.04,
    "pre_ram_sound": "pre_ram",
    "ram_impact_sound": "ram_impact",
    "cooldown_range": [
        30,
        300
    ],
    "on_start": [
        {
            "event": "start_event",
            "target": "self"
        }
    ]
}
```

```json title="#component_groups/ram_screamer"
"minecraft:behavior.ram_attack": {
    "priority": 5,
    "run_speed": 0.7,
    "ram_speed": 1.8,
    "min_ram_distance": 4,
    "ram_distance": 7,
    "knockback_force": 2.5,
    "knockback_height": 0.04,
    "pre_ram_sound": "pre_ram.screamer",
    "ram_impact_sound": "ram_impact.screamer",
    "cooldown_range": [
        5,
        15
    ],
    "on_start": [
        {
            "event": "start_event",
            "target": "self"
        }
    ]
}
```

</Spoiler>

## behavior.random_breach

<Spoiler title="显示">

dolphin

```json title=""
"minecraft:behavior.random_breach": {
    "priority": 6,
    "interval": 50,
    "xz_dist": 6,
    "cooldown_time": 2.0
}
```

</Spoiler>

## behavior.random_fly

<Spoiler title="显示">

parrot

```json title="#component_groups/minecraft:parrot_wild"
"minecraft:behavior.random_fly": {
    "priority": 2,
    "xz_dist": 15,
    "y_dist": 1,
    "y_offset": 0,
    "speed_multiplier": 1.0,
    "can_land_on_trees": true,
    "avoid_damage_blocks": true
}
```

</Spoiler>

## behavior.random_hover

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.random_hover": {
    "priority": 9,
    "xz_dist": 8,
    "y_dist": 8,
    "y_offset": -1,
    "interval": 1,
    "hover_height": [
        1,
        4
    ]
}
```

bee

```json title=""
"minecraft:behavior.random_hover": {
    "priority": 12,
    "xz_dist": 8,
    "y_dist": 8,
    "y_offset": -1,
    "interval": 1,
    "hover_height": [
        1,
        4
    ]
}
```

</Spoiler>

## behavior.random_look_around

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

blaze

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 5
}
```

bogged

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

breeze

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

camel

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

cave_spider

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 7
}
```

chicken

```json title=""
"minecraft:behavior.random_look_around": {
    "priority": 8
}
```

</Spoiler>

## behavior.random_look_around_and_sit

<Spoiler title="显示">

camel

```json title=""
"minecraft:behavior.random_look_around_and_sit": {
    "priority": 4,
    "continue_if_leashed": true,
    "continue_sitting_on_reload": true,
    "min_look_count": 2,
    "max_look_count": 5,
    "min_look_time": 80,
    "max_look_time": 100,
    "min_angle_of_view_horizontal": -30,
    "max_angle_of_view_horizontal": 30,
    "random_look_around_cooldown": 5,
    "probability": 0.001
}
```

fox

```json title=""
"minecraft:behavior.random_look_around_and_sit": {
    "priority": 12,
    "min_look_count": 2,
    "max_look_count": 5,
    "min_look_time": 80,
    "max_look_time": 100,
    "probability": 0.001
}
```

</Spoiler>

## behavior.random_search_and_dig

<Spoiler title="显示">

sniffer

```json title="#component_groups/sniffer_search_and_dig"
"minecraft:behavior.random_search_and_dig": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "find_valid_position_retries": 5,
    "target_blocks": [
        "minecraft:dirt",
        "minecraft:grass",
        "minecraft:podzol",
        "minecraft:dirt_with_roots",
        "minecraft:moss_block",
        "minecraft:mud",
        "minecraft:muddy_mangrove_roots"
    ],
    "goal_radius": 2.0,
    "search_range_xz": 20.0,
    "search_range_y": 3,
    "cooldown_range": 0.0,
    "digging_duration_range": [
        8.0,
        10.0
    ],
    "item_table": "loot_tables/gameplay/entities/sniffer_seeds.json",
    "spawn_item_after_seconds": 6.0,
    "spawn_item_pos_offset": 2.25,
    "on_searching_start": {
        "event": "on_searching_start",
        "target": "self"
    },
    "on_fail_during_searching": {
        "event": "on_fail_during_searching",
        "target": "self"
    },
    "on_digging_start": {
        "event": "on_digging_start",
        "target": "self"
    },
    "on_item_found": {
        "event": "on_item_found",
        "target": "self"
    },
    "on_fail_during_digging": {
        "event": "on_fail_during_digging",
        "target": "self"
    },
    "on_success": {
        "event": "on_search_and_digging_success",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.random_sitting

<Spoiler title="显示">

panda

```json title=""
"minecraft:behavior.random_sitting": {
    "priority": 5,
    "start_chance": 0.01,
    "stop_chance": 0.3,
    "cooldown": 30,
    "min_sit_time": 10
}
```

```json title="#component_groups/minecraft:panda_lazy"
"minecraft:behavior.random_sitting": {
    "priority": 6,
    "start_chance": 0.02,
    "stop_chance": 0.2,
    "cooldown": 25,
    "min_sit_time": 15
}
```

</Spoiler>

## behavior.random_stroll

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

axolotl

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "interval": 100
}
```

blaze

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

bogged

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1
}
```

breeze

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 1.0
}
```

camel

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 2
}
```

cat

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 8,
    "speed_multiplier": 0.8
}
```

cave_spider

```json title=""
"minecraft:behavior.random_stroll": {
    "priority": 6,
    "speed_multiplier": 0.8
}
```

</Spoiler>

## behavior.random_swim

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 8,
    "interval": 0,
    "xz_dist": 30,
    "y_dist": 15
}
```

dolphin

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 5,
    "interval": 0,
    "xz_dist": 20
}
```

elder_guardian

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 7,
    "speed_multiplier": 0.5,
    "avoid_surface": false
}
```

cod

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

guardian

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 7,
    "speed_multiplier": 1.0,
    "interval": 80,
    "avoid_surface": false
}
```

pufferfish

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 3,
    "speed_multiplier": 1.0,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

salmon

```json title=""
"minecraft:behavior.random_swim": {
    "speed_multiplier": 1.0,
    "priority": 3,
    "xz_dist": 16,
    "y_dist": 4,
    "interval": 0
}
```

tadpole

```json title=""
"minecraft:behavior.random_swim": {
    "priority": 2,
    "interval": 100
}
```

</Spoiler>

## behavior.ranged_attack

<Spoiler title="显示">

blaze

```json title="#component_groups/ranged_mode"
"minecraft:behavior.ranged_attack": {
    "priority": 3,
    "burst_shots": 3,
    "burst_interval": 0.3,
    "charge_charged_trigger": 0.0,
    "charge_shoot_trigger": 4.0,
    "attack_interval_min": 3.0,
    "attack_interval_max": 5.0,
    "attack_radius": 16.0
}
```

bogged

```json title="#component_groups/minecraft:ranged_attack"
"minecraft:behavior.ranged_attack": {
    "priority": 0,
    "attack_interval": 3.5,
    "attack_radius": 15.0
}
```

drowned

```json title="#component_groups/minecraft:ranged_mode"
"minecraft:behavior.ranged_attack": {
    "priority": 3,
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 10.0,
    "swing": true
}
```

ghast

```json title=""
"minecraft:behavior.ranged_attack": {
    "priority": 1,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

llama

```json title="#component_groups/minecraft:llama_angry"
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

```json title="#component_groups/minecraft:llama_angry_wolf"
"minecraft:behavior.ranged_attack": {
    "priority": 2,
    "attack_radius": 64,
    "charge_shoot_trigger": 2,
    "charge_charged_trigger": 1
}
```

piglin

```json title="#component_groups/ranged_unit"
"minecraft:behavior.ranged_attack": {
    "priority": 8,
    "attack_interval_min": 1,
    "attack_interval_max": 1,
    "attack_radius": 8,
    "attack_radius_min": 4,
    "speed_multiplier": 1.0,
    "target_in_sight_time": 0.1
}
```

pillager

```json title="#component_groups/minecraft:ranged_attack"
"minecraft:behavior.ranged_attack": {
    "priority": 4,
    "attack_interval_min": 1.0,
    "attack_interval_max": 1.0,
    "attack_radius": 8.0
}
```

</Spoiler>

## behavior.receive_love

<Spoiler title="显示">

villager

```json title="#component_groups/adult"
"minecraft:behavior.receive_love": {
    "priority": 7
}
```

villager_v2

```json title="#component_groups/make_and_receive_love"
"minecraft:behavior.receive_love": {
    "priority": 6
}
```

</Spoiler>

## behavior.restrict_open_door

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

</Spoiler>

## behavior.rise_to_liquid_level

<Spoiler title="显示">

strider

```json title="#component_groups/minecraft:strider_pathing_behaviors"
"minecraft:behavior.rise_to_liquid_level": {
    "priority": 0,
    "liquid_y_offset": 0.25,
    "rise_delta": 0.01,
    "sink_delta": 0.01
}
```

</Spoiler>

## behavior.roar

<Spoiler title="显示">

warden

```json title=""
"minecraft:behavior.roar": {
    "priority": 2,
    "duration": 4.2
}
```

</Spoiler>

## behavior.roll

<Spoiler title="显示">

panda

```json title="#component_groups/minecraft:panda_baby"
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.0016
}
```

```json title="#component_groups/minecraft:panda_playful"
"minecraft:behavior.roll": {
    "priority": 12,
    "probability": 0.013
}
```

</Spoiler>

## behavior.run_around_like_crazy

<Spoiler title="显示">

donkey

```json title="#component_groups/minecraft:donkey_adult"
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

horse

```json title="#component_groups/minecraft:horse_adult"
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

llama

```json title=""
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

mule

```json title="#component_groups/minecraft:mule_adult"
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

trader_llama

```json title=""
"minecraft:behavior.run_around_like_crazy": {
    "priority": 1,
    "speed_multiplier": 1.2
}
```

</Spoiler>

## behavior.scared

<Spoiler title="显示">

panda

```json title="#component_groups/minecraft:panda_worried"
"minecraft:behavior.scared": {
    "priority": 1,
    "sound_interval": 20
}
```

</Spoiler>

## behavior.send_event

<Spoiler title="显示">

evocation_illager

```json title=""
"minecraft:behavior.send_event": {
    "priority": 3,
    "event_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 16.0,
            "cooldown_time": 5.0,
            "cast_duration": 3.0,
            "particle_color": "#FFB38033",
            "weight": 3,
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_color",
                        "subject": "other",
                        "value": "blue"
                    }
                ]
            },
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "base_delay": 2.0,
                    "event": "wololo",
                    "sound_event": "prepare.wololo"
                }
            ]
        }
    ]
}
```

</Spoiler>

## behavior.share_items

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.share_items": {
    "priority": 8,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

villager_v2

```json title=""
"minecraft:behavior.share_items": {
    "priority": 10,
    "max_dist": 3,
    "goal_radius": 2.0,
    "speed_multiplier": 0.5,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "villager"
            }
        }
    ]
}
```

</Spoiler>

## behavior.silverfish_merge_with_stone

<Spoiler title="显示">

silverfish

```json title=""
"minecraft:behavior.silverfish_merge_with_stone": {
    "priority": 5
}
```

</Spoiler>

## behavior.silverfish_wake_up_friends

<Spoiler title="显示">

silverfish

```json title="#component_groups/minecraft:silverfish_angry"
"minecraft:behavior.silverfish_wake_up_friends": {
    "priority": 1
}
```

</Spoiler>

## behavior.skeleton_horse_trap

<Spoiler title="显示">

skeleton_horse

```json title="#component_groups/minecraft:skeleton_trap"
"minecraft:behavior.skeleton_horse_trap": {
    "within_radius": 10.0,
    "duration": 900.0,
    "priority": 2
}
```

</Spoiler>

## behavior.sleep

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.sleep": {}
```

```json title="#component_groups/bed_schedule_villager"
"minecraft:behavior.sleep": {
    "priority": 3,
    "goal_radius": 1.5,
    "speed_multiplier": 0.6,
    "sleep_collider_height": 0.3,
    "sleep_collider_width": 1.0,
    "sleep_y_offset": 0.6,
    "timeout_cooldown": 10.0
}
```

</Spoiler>

## behavior.slime_attack

<Spoiler title="显示">

magma_cube

```json title=""
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

slime

```json title=""
"minecraft:behavior.slime_attack": {
    "priority": 3
}
```

</Spoiler>

## behavior.slime_float

<Spoiler title="显示">

magma_cube

```json title=""
"minecraft:behavior.slime_float": {
    "priority": 1,
    "jump_chance_percentage": 0.8,
    "speed_multiplier": 1.2
}
```

slime

```json title=""
"minecraft:behavior.slime_float": {
    "priority": 1,
    "jump_chance_percentage": 0.8,
    "speed_multiplier": 1.2
}
```

</Spoiler>

## behavior.slime_keep_on_jumping

<Spoiler title="显示">

magma_cube

```json title=""
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

slime

```json title=""
"minecraft:behavior.slime_keep_on_jumping": {
    "priority": 5,
    "speed_multiplier": 1.0
}
```

</Spoiler>

## behavior.slime_random_direction

<Spoiler title="显示">

magma_cube

```json title=""
"minecraft:behavior.slime_random_direction": {
    "priority": 4,
    "add_random_time_range": 3,
    "turn_range": 360,
    "min_change_direction_time": 2.0
}
```

slime

```json title=""
"minecraft:behavior.slime_random_direction": {
    "priority": 4,
    "add_random_time_range": 3,
    "turn_range": 360,
    "min_change_direction_time": 2.0
}
```

</Spoiler>

## behavior.snacking

<Spoiler title="显示">

panda

```json title=""
"minecraft:behavior.snacking": {
    "priority": 2,
    "snacking_cooldown": 22.5,
    "snacking_cooldown_min": 20,
    "snacking_stop_chance": 0.001334,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

```json title="#component_groups/minecraft:panda_lazy"
"minecraft:behavior.snacking": {
    "priority": 3,
    "snacking_cooldown": 17.5,
    "snacking_cooldown_min": 10,
    "snacking_stop_chance": 0.0011,
    "items": [
        "bamboo",
        "cake"
    ]
}
```

</Spoiler>

## behavior.sneeze

<Spoiler title="显示">

panda

```json title="#component_groups/minecraft:panda_baby"
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.0001666,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

```json title="#component_groups/minecraft:panda_sneezing"
"minecraft:behavior.sneeze": {
    "priority": 7,
    "probability": 0.002,
    "cooldown_time": 1.0,
    "within_radius": 10.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "has_component",
                        "subject": "other",
                        "operator": "!=",
                        "value": "minecraft:is_baby"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "panda"
                    },
                    {
                        "test": "in_water",
                        "subject": "other",
                        "operator": "!=",
                        "value": true
                    },
                    {
                        "test": "on_ground",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "max_dist": 10
        }
    ],
    "drop_item_chance": 0.001,
    "loot_table": "loot_tables/entities/panda_sneeze.json",
    "prepare_sound": "presneeze",
    "prepare_time": 1.0,
    "sound": "sneeze"
}
```

</Spoiler>

## behavior.sniff

<Spoiler title="显示">

warden

```json title=""
"minecraft:behavior.sniff": {
    "priority": 6,
    "duration": 4.16,
    "sniffing_radius": 24.0,
    "suspicion_radius_horizontal": 6.0,
    "suspicion_radius_vertical": 20.0,
    "cooldown_range": [
        5.0,
        10.0
    ]
}
```

</Spoiler>

## behavior.sonic_boom

<Spoiler title="显示">

warden

```json title=""
"minecraft:behavior.sonic_boom": {
    "priority": 3,
    "duration": 3.0,
    "speed_multiplier": 1.2,
    "attack_damage": 10,
    "attack_range_horizontal": 15,
    "attack_range_vertical": 20,
    "attack_cooldown": 2,
    "knockback_vertical_strength": 0.5,
    "knockback_horizontal_strength": 2.5,
    "knockback_height_cap": 0.5,
    "duration_until_attack_sound": 1.7,
    "charge_sound": "sonic_charge",
    "attack_sound": "sonic_boom"
}
```

</Spoiler>

## behavior.squid_dive

<Spoiler title="显示">

glow_squid

```json title=""
"minecraft:behavior.squid_dive": {
    "priority": 2
}
```

squid

```json title=""
"minecraft:behavior.squid_dive": {
    "priority": 2
}
```

</Spoiler>

## behavior.squid_flee

<Spoiler title="显示">

glow_squid

```json title=""
"minecraft:behavior.squid_flee": {
    "priority": 2
}
```

squid

```json title=""
"minecraft:behavior.squid_flee": {
    "priority": 2
}
```

</Spoiler>

## behavior.squid_idle

<Spoiler title="显示">

glow_squid

```json title=""
"minecraft:behavior.squid_idle": {
    "priority": 2
}
```

squid

```json title=""
"minecraft:behavior.squid_idle": {
    "priority": 2
}
```

</Spoiler>

## behavior.squid_move_away_from_ground

<Spoiler title="显示">

glow_squid

```json title=""
"minecraft:behavior.squid_move_away_from_ground": {
    "priority": 1
}
```

squid

```json title=""
"minecraft:behavior.squid_move_away_from_ground": {
    "priority": 1
}
```

</Spoiler>

## behavior.squid_out_of_water

<Spoiler title="显示">

glow_squid

```json title=""
"minecraft:behavior.squid_out_of_water": {
    "priority": 2
}
```

squid

```json title=""
"minecraft:behavior.squid_out_of_water": {
    "priority": 2
}
```

</Spoiler>

## behavior.stalk_and_pounce_on_target

<Spoiler title="显示">

fox

```json title=""
"minecraft:behavior.stalk_and_pounce_on_target": {
    "priority": 7,
    "stalk_speed": 1.2,
    "max_stalk_dist": 12.0,
    "leap_height": 0.9,
    "leap_dist": 0.8,
    "pounce_max_dist": 5.0,
    "interest_time": 2.0,
    "stuck_time": 2.0,
    "strike_dist": 2.0,
    "stuck_blocks": {
        "test": "is_block",
        "subject": "block",
        "operator": "==",
        "value": "snow_layer"
    }
}
```

</Spoiler>

## behavior.stay_near_noteblock

<Spoiler title="显示">

allay

```json title=""
"minecraft:behavior.stay_near_noteblock": {
    "priority": 5,
    "speed": 8,
    "start_distance": 16,
    "stop_distance": 4
}
```

</Spoiler>

## behavior.stay_while_sitting

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

ocelot

```json title="#component_groups/minecraft:ocelot_tame"
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

parrot

```json title="#component_groups/minecraft:parrot_tame"
"minecraft:behavior.stay_while_sitting": {
    "priority": 1
}
```

wolf

```json title=""
"minecraft:behavior.stay_while_sitting": {
    "priority": 3
}
```

</Spoiler>

## behavior.stomp_attack

<Spoiler title="显示">

polar_bear

```json title="#component_groups/minecraft:adult_hostile"
"minecraft:behavior.stomp_attack": {
    "priority": 1,
    "track_target": true,
    "require_complete_path": true,
    "stomp_range_multiplier": 2.0,
    "no_damage_range_multiplier": 2.0
}
```

</Spoiler>

## behavior.stomp_turtle_egg

<Spoiler title="显示">

drowned

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

husk

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

zombie

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

zombie_pigman

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 5,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

zombie_villager

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

zombie_villager_v2

```json title=""
"minecraft:behavior.stomp_turtle_egg": {
    "priority": 4,
    "speed_multiplier": 1,
    "search_range": 10,
    "search_height": 2,
    "goal_radius": 1.14,
    "interval": 20
}
```

</Spoiler>

## behavior.stroll_towards_village

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:fox_night"
"minecraft:behavior.stroll_towards_village": {
    "priority": 11,
    "speed_multiplier": 1.0,
    "goal_radius": 3.0,
    "cooldown_time": 10.0,
    "search_range": 32,
    "start_chance": 0.005
}
```

</Spoiler>

## behavior.summon_entity

<Spoiler title="显示">

evocation_illager

```json title=""
"minecraft:behavior.summon_entity": {
    "priority": 2,
    "summon_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 3.0,
            "cooldown_time": 5.0,
            "weight": 3,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 5,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 1.5,
                    "entity_lifespan": 1.1,
                    "sound_event": "prepare.attack"
                },
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 0.15,
                    "delay_per_summon": 0.0,
                    "num_entities_spawned": 8,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 2.5,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "min_activation_range": 3.0,
            "weight": 3,
            "cooldown_time": 5.0,
            "cast_duration": 2.0,
            "particle_color": "#FF664D59",
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "shape": "line",
                    "target": "self",
                    "base_delay": 1.0,
                    "delay_per_summon": 0.05,
                    "num_entities_spawned": 16,
                    "entity_type": "minecraft:evocation_fang",
                    "size": 20,
                    "entity_lifespan": 1.1
                }
            ]
        },
        {
            "weight": 1,
            "cooldown_time": 17.0,
            "cast_duration": 5.0,
            "particle_color": "#FFB3B3CC",
            "sequence": [
                {
                    "shape": "circle",
                    "target": "self",
                    "base_delay": 5.0,
                    "num_entities_spawned": 3,
                    "entity_type": "minecraft:vex",
                    "summon_cap": 8,
                    "summon_cap_radius": 16.0,
                    "size": 1.0,
                    "sound_event": "prepare.summon"
                }
            ]
        }
    ]
}
```

</Spoiler>

## behavior.swell

<Spoiler title="显示">

creeper

```json title=""
"minecraft:behavior.swell": {
    "start_distance": 2.5,
    "stop_distance": 6.0,
    "priority": 2
}
```

</Spoiler>

## behavior.swim_idle

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:behavior.swim_idle": {
    "priority": 7,
    "idle_time": 5.0,
    "success_rate": 0.05
}
```

cod

```json title=""
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

salmon

```json title=""
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

tropicalfish

```json title=""
"minecraft:behavior.swim_idle": {
    "priority": 5,
    "idle_time": 5.0,
    "success_rate": 0.1
}
```

</Spoiler>

## behavior.swim_wander

<Spoiler title="显示">

cod

```json title=""
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.1,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

pufferfish

```json title=""
"minecraft:behavior.swim_wander": {
    "priority": 5,
    "interval": 1.0,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

salmon

```json title=""
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.0166,
    "look_ahead": 5.0,
    "speed_multiplier": 0.014,
    "wander_time": 5.0
}
```

tropicalfish

```json title=""
"minecraft:behavior.swim_wander": {
    "priority": 4,
    "interval": 0.1,
    "look_ahead": 2.0,
    "speed_multiplier": 1.0,
    "wander_time": 5.0
}
```

</Spoiler>

## behavior.swim_with_entity

<Spoiler title="显示">

dolphin

```json title=""
"minecraft:behavior.swim_with_entity": {
    "priority": 4,
    "success_rate": 0.1,
    "chance_to_stop": 0.0333,
    "state_check_interval": 0.5,
    "catch_up_threshold": 12.0,
    "match_direction_threshold": 2.0,
    "catch_up_multiplier": 2.5,
    "speed_multiplier": 1.5,
    "search_range": 20.0,
    "stop_distance": 5.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            }
        }
    ]
}
```

</Spoiler>

## behavior.swoop_attack

<Spoiler title="显示">

phantom

```json title=""
"minecraft:behavior.swoop_attack": {
    "priority": 2,
    "damage_reach": 0.2,
    "speed_multiplier": 1.0,
    "delay_range": [
        10.0,
        20.0
    ]
}
```

</Spoiler>

## behavior.take_flower

<Spoiler title="显示">

villager

```json title="#component_groups/baby"
"minecraft:behavior.take_flower": {
    "priority": 7,
    "filters": {
        "all_of": [
            {
                "test": "is_daytime",
                "value": true
            }
        ]
    }
}
```

villager_v2

```json title="#component_groups/baby"
"minecraft:behavior.take_flower": {
    "priority": 9,
    "filters": {
        "all_of": [
            {
                "test": "is_daytime",
                "value": true
            }
        ]
    }
}
```

</Spoiler>

## behavior.target_when_pushed

<Spoiler title="显示">

iron_golem

```json title=""
"minecraft:behavior.target_when_pushed": {
    "priority": 1,
    "percent_chance": 5.0,
    "entity_types": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "monster"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "operator": "!=",
                        "value": "creeper"
                    }
                ]
            }
        }
    ]
}
```

</Spoiler>

## behavior.tempt

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 1.25,
    "can_tempt_vertically": true,
    "items": [
        "spider_eye"
    ]
}
```

axolotl

```json title=""
"minecraft:behavior.tempt": {
    "priority": 2,
    "speed_multiplier": 1.1,
    "can_tempt_vertically": true,
    "items": [
        "tropical_fish_bucket"
    ]
}
```

bee

```json title=""
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 1.25,
    "within_radius": 8,
    "can_tempt_vertically": true,
    "items": [
        "minecraft:poppy",
        "minecraft:blue_orchid",
        "minecraft:allium",
        "minecraft:azure_bluet",
        "minecraft:red_tulip",
        "minecraft:orange_tulip",
        "minecraft:white_tulip",
        "minecraft:pink_tulip",
        "minecraft:oxeye_daisy",
        "minecraft:cornflower",
        "minecraft:lily_of_the_valley",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sunflower",
        "minecraft:lilac",
        "minecraft:rose_bush",
        "minecraft:peony",
        "minecraft:flowering_azalea",
        "minecraft:azalea_leaves_flowered",
        "minecraft:mangrove_propagule",
        "minecraft:pitcher_plant",
        "minecraft:torchflower",
        "minecraft:cherry_leaves",
        "minecraft:pink_petals"
    ]
}
```

camel

```json title=""
"minecraft:behavior.tempt": {
    "priority": 3,
    "speed_multiplier": 2.5,
    "can_tempt_vertically": true,
    "items": [
        "cactus"
    ]
}
```

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "can_get_scared": true,
    "tempt_sound": "tempt",
    "sound_interval": [
        0,
        100
    ],
    "items": [
        "fish",
        "salmon"
    ]
}
```

```json title="#component_groups/minecraft:cat_tame"
"minecraft:behavior.tempt": {
    "priority": 5,
    "speed_multiplier": 0.5,
    "within_radius": 16,
    "items": [
        "fish",
        "salmon"
    ]
}
```

chicken

```json title=""
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.0,
    "items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds",
        "pitcher_pod",
        "torchflower_seeds"
    ]
}
```

cow

```json title=""
"minecraft:behavior.tempt": {
    "priority": 4,
    "speed_multiplier": 1.25,
    "items": [
        "wheat"
    ]
}
```

</Spoiler>

## behavior.timer_flag_1

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:rolled_up_with_threats"
"minecraft:behavior.timer_flag_1": {
    "priority": 0,
    "cooldown_range": 2.5,
    "duration_range": [
        5.0,
        20.0
    ],
    "on_start": {
        "event": "minecraft:stop_peeking"
    },
    "on_end": {
        "event": "minecraft:start_peeking"
    }
}
```

```json title="#component_groups/minecraft:rolled_up_without_threats"
"minecraft:behavior.timer_flag_1": {
    "priority": 0,
    "cooldown_range": 2.5,
    "duration_range": 1.5,
    "on_start": {
        "event": "minecraft:start_unrolling"
    }
}
```

sniffer

```json title=""
"minecraft:behavior.timer_flag_1": {
    "priority": 6,
    "control_flags": [
        "move",
        "look"
    ],
    "cooldown_range": [
        400.0,
        500.0
    ],
    "duration_range": 2.0,
    "on_end": {
        "event": "on_scenting_success",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.timer_flag_2

<Spoiler title="显示">

sniffer

```json title="#component_groups/stand_up"
"minecraft:behavior.timer_flag_2": {
    "priority": 2,
    "control_flags": [
        "move"
    ],
    "cooldown_range": 0.0,
    "duration_range": [
        2.0,
        5.0
    ],
    "on_end": {
        "event": "on_rising_end",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.timer_flag_3

<Spoiler title="显示">

sniffer

```json title="#component_groups/feeling_happy"
"minecraft:behavior.timer_flag_3": {
    "priority": 5,
    "cooldown_range": 0.0,
    "duration_range": [
        2.0,
        5.0
    ],
    "on_end": {
        "event": "on_feeling_happy_end",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.trade_interest

<Spoiler title="显示">

villager_v2

```json title="#component_groups/trade_components"
"minecraft:behavior.trade_interest": {}
```

```json title="#component_groups/farmer"
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

```json title="#component_groups/fisherman"
"minecraft:behavior.trade_interest": {
    "priority": 5,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

wandering_trader

```json title=""
"minecraft:behavior.trade_interest": {
    "priority": 3,
    "within_radius": 6.0,
    "interest_time": 45.0,
    "remove_item_time": 1.0,
    "carried_item_switch_time": 2.0,
    "cooldown": 2.0
}
```

</Spoiler>

## behavior.trade_with_player

<Spoiler title="显示">

villager

```json title=""
"minecraft:behavior.trade_with_player": {
    "priority": 1,
    "filters": {
        "all_of": [
            {
                "all_of": [
                    {
                        "test": "in_water",
                        "value": false
                    }
                ]
            },
            {
                "any_of": [
                    {
                        "test": "on_ground",
                        "value": true
                    },
                    {
                        "test": "is_sleeping",
                        "value": true
                    }
                ]
            }
        ]
    }
}
```

villager_v2

```json title=""
"minecraft:behavior.trade_with_player": {
    "priority": 2,
    "filters": {
        "all_of": [
            {
                "all_of": [
                    {
                        "test": "in_water",
                        "value": false
                    }
                ]
            },
            {
                "any_of": [
                    {
                        "test": "on_ground",
                        "value": true
                    },
                    {
                        "test": "is_sleeping",
                        "value": true
                    }
                ]
            }
        ]
    }
}
```

wandering_trader

```json title=""
"minecraft:behavior.trade_with_player": {
    "priority": 1,
    "filters": {
        "all_of": [
            {
                "all_of": [
                    {
                        "test": "in_water",
                        "value": false
                    }
                ]
            },
            {
                "any_of": [
                    {
                        "test": "on_ground",
                        "value": true
                    },
                    {
                        "test": "is_sleeping",
                        "value": true
                    }
                ]
            }
        ]
    }
}
```

</Spoiler>

## behavior.wither_random_attack_pos_goal

<Spoiler title="显示">

wither

```json title=""
"minecraft:behavior.wither_random_attack_pos_goal": {
    "priority": 3
}
```

</Spoiler>

## behavior.wither_target_highest_damage

<Spoiler title="显示">

wither

```json title=""
"minecraft:behavior.wither_target_highest_damage": {
    "priority": 1
}
```

</Spoiler>

## behavior.work

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.work": {}
```

```json title="#component_groups/work_schedule_villager"
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

```json title="#component_groups/work_schedule_fisher"
"minecraft:behavior.work": {
    "priority": 7,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

</Spoiler>

## behavior.work_composter

<Spoiler title="显示">

villager_v2

```json title="#component_groups/job_specific_goals"
"minecraft:behavior.work_composter": {}
```

```json title="#component_groups/work_schedule_farmer"
"minecraft:behavior.work_composter": {
    "priority": 9,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 100,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

</Spoiler>

## block_climber

<Spoiler title="显示">

endermite

```json title=""
"minecraft:block_climber": {}
```

fox

```json title=""
"minecraft:block_climber": {}
```

player

```json title=""
"minecraft:block_climber": {}
```

rabbit

```json title=""
"minecraft:block_climber": {}
```

silverfish

```json title=""
"minecraft:block_climber": {}
```

</Spoiler>

## block_sensor

<Spoiler title="显示">

bee

```json title=""
"minecraft:block_sensor": {
    "sensor_radius": 16,
    "sources": [
        {
            "test": "has_silk_touch",
            "subject": "other",
            "value": false
        }
    ],
    "on_break": [
        {
            "block_list": [
                "minecraft:beehive",
                "minecraft:bee_nest"
            ],
            "on_block_broken": "hive_destroyed"
        }
    ]
}
```

piglin

```json title="#component_groups/piglin_adult"
"minecraft:block_sensor": {
    "sensor_radius": 16,
    "on_break": [
        {
            "block_list": [
                "minecraft:gold_block",
                "minecraft:gilded_blackstone",
                "minecraft:nether_gold_ore",
                "minecraft:deepslate_gold_ore",
                "minecraft:raw_gold_block",
                "minecraft:gold_ore",
                "minecraft:chest",
                "minecraft:trapped_chest",
                "minecraft:ender_chest",
                "minecraft:barrel",
                "minecraft:shulker_box",
                "minecraft:undyed_shulker_box"
            ],
            "on_block_broken": "important_block_destroyed_event"
        }
    ]
}
```

</Spoiler>

## body_rotation_blocked

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:rolled_up"
"minecraft:body_rotation_blocked": {}
```

</Spoiler>

## boostable

<Spoiler title="显示">

pig

```json title="#component_groups/minecraft:pig_saddled"
"minecraft:boostable": {
    "speed_multiplier": 1.35,
    "duration": 3.0,
    "boost_items": [
        {
            "item": "carrotOnAStick",
            "damage": 2,
            "replace_item": "fishing_rod"
        }
    ]
}
```

strider

```json title="#component_groups/minecraft:strider_saddled"
"minecraft:boostable": {
    "speed_multiplier": 1.35,
    "duration": 16.0,
    "boost_items": [
        {
            "item": "warped_fungus_on_a_stick",
            "damage": 1,
            "replace_item": "fishing_rod"
        }
    ]
}
```

</Spoiler>

## boss

<Spoiler title="显示">

ender_dragon

```json title=""
"minecraft:boss": {
    "should_darken_sky": false,
    "hud_range": 125
}
```

wither

```json title=""
"minecraft:boss": {
    "should_darken_sky": true,
    "hud_range": 55
}
```

</Spoiler>

## break_blocks

<Spoiler title="显示">

ravager

```json title=""
"minecraft:break_blocks": {
    "breakable_blocks": [
        "bamboo",
        "bamboo_sapling",
        "beetroot",
        "brown_mushroom",
        "carrots",
        "carved_pumpkin",
        "chorus_flower",
        "chorus_plant",
        "deadbush",
        "double_plant",
        "leaves",
        "leaves2",
        "lit_pumpkin",
        "melon_block",
        "melon_stem",
        "potatoes",
        "pumpkin",
        "pumpkin_stem",
        "red_flower",
        "red_mushroom",
        "crimson_fungus",
        "warped_fungus",
        "reeds",
        "sapling",
        "snow_layer",
        "sweet_berry_bush",
        "tallgrass",
        "turtle_egg",
        "vine",
        "waterlily",
        "wheat",
        "yellow_flower",
        "azalea",
        "flowering_azalea",
        "azalea_leaves",
        "azalea_leaves_flowered",
        "cave_vines",
        "cave_vines_body_with_berries",
        "cave_vines_head_with_berries",
        "small_dripleaf_block",
        "big_dripleaf",
        "spore_blossom",
        "hanging_roots",
        "mangrove_leaves"
    ]
}
```

</Spoiler>

## breathable

<Spoiler title="显示">

allay

```json title=""
"minecraft:breathable": {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

armadillo

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

axolotl

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true,
    "breathes_air": true,
    "generates_bubbles": false
}
```

bat

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

bee

```json title=""
"minecraft:breathable": {
    "totalSupply": 15,
    "suffocateTime": 0
}
```

bogged

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0,
    "breathes_water": true
}
```

breeze

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

camel

```json title=""
"minecraft:breathable": {
    "total_supply": 15,
    "suffocate_time": 0
}
```

</Spoiler>

## breedable

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:adult"
"minecraft:breedable": {
    "love_filters": {
        "test": "enum_property",
        "domain": "minecraft:armadillo_state",
        "value": "unrolled"
    },
    "require_tame": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:armadillo",
            "baby_type": "minecraft:armadillo",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "spider_eye"
    ]
}
```

axolotl

```json title="#component_groups/axolotl_adult"
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "tropical_fish_bucket",
    "transform_to_item": "water_bucket:0",
    "breeds_with": {
        "mate_type": "minecraft:axolotl",
        "baby_type": "minecraft:axolotl",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "mutation_factor": {
        "variant": 0.00083
    }
}
```

bee

```json title="#component_groups/bee_adult"
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:bee",
        "baby_type": "minecraft:bee",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "minecraft:poppy",
        "minecraft:blue_orchid",
        "minecraft:allium",
        "minecraft:azure_bluet",
        "minecraft:red_tulip",
        "minecraft:orange_tulip",
        "minecraft:white_tulip",
        "minecraft:pink_tulip",
        "minecraft:oxeye_daisy",
        "minecraft:cornflower",
        "minecraft:lily_of_the_valley",
        "minecraft:yellow_flower",
        "minecraft:wither_rose",
        "minecraft:sunflower",
        "minecraft:lilac",
        "minecraft:rose_bush",
        "minecraft:peony",
        "minecraft:flowering_azalea",
        "minecraft:azalea_leaves_flowered",
        "minecraft:mangrove_propagule",
        "minecraft:pitcher_plant",
        "minecraft:torchflower",
        "minecraft:cherry_leaves",
        "minecraft:pink_petals"
    ]
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:camel",
            "baby_type": "minecraft:camel",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "cactus"
    ]
}
```

cat

```json title="#component_groups/minecraft:cat_adult"
"minecraft:breedable": {
    "require_tame": true,
    "require_full_health": true,
    "allow_sitting": true,
    "breeds_with": {
        "mate_type": "minecraft:cat",
        "baby_type": "minecraft:cat",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "fish",
        "salmon"
    ]
}
```

chicken

```json title="#component_groups/minecraft:chicken_adult"
"minecraft:breedable": {
    "require_tame": false,
    "breeds_with": {
        "mate_type": "minecraft:chicken",
        "baby_type": "minecraft:chicken",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    },
    "breed_items": [
        "wheat_seeds",
        "beetroot_seeds",
        "melon_seeds",
        "pumpkin_seeds",
        "pitcher_pod",
        "torchflower_seeds"
    ]
}
```

cow

```json title="#component_groups/minecraft:cow_adult"
"minecraft:breedable": {
    "require_tame": false,
    "breed_items": "wheat",
    "breeds_with": {
        "mate_type": "minecraft:cow",
        "baby_type": "minecraft:cow",
        "breed_event": {
            "event": "minecraft:entity_born",
            "target": "baby"
        }
    }
}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:breedable": {
    "parent_centric_attribute_blending": [
        "minecraft:health"
    ],
    "require_tame": true,
    "inherit_tamed": false,
    "breeds_with": [
        {
            "mate_type": "minecraft:donkey",
            "baby_type": "minecraft:donkey",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        },
        {
            "mate_type": "minecraft:horse",
            "baby_type": "minecraft:mule",
            "breed_event": {
                "event": "minecraft:entity_born",
                "target": "baby"
            }
        }
    ],
    "breed_items": [
        "golden_carrot",
        "golden_apple",
        "appleEnchanted"
    ]
}
```

</Spoiler>

## bribeable

<Spoiler title="显示">

dolphin

```json title="#component_groups/dolphin_adult"
"minecraft:bribeable": {
    "bribe_items": [
        "fish",
        "salmon"
    ]
}
```

</Spoiler>

## buoyant

<Spoiler title="显示">

boat

```json title=""
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ]
}
```

```json title="#component_groups/minecraft:floating"
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ]
}
```

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": false,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ],
    "drag_down_on_buoyancy_removed": 0.7
}
```

chest_boat

```json title=""
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ]
}
```

```json title="#component_groups/minecraft:floating"
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ]
}
```

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:buoyant": {
    "base_buoyancy": 1.0,
    "apply_gravity": true,
    "simulate_waves": false,
    "liquid_blocks": [
        "minecraft:water",
        "minecraft:flowing_water"
    ],
    "drag_down_on_buoyancy_removed": 0.7
}
```

xp_orb

```json title=""
"minecraft:buoyant": {
    "apply_gravity": false,
    "liquid_blocks": [
        "minecraft:flowing_water",
        "minecraft:water"
    ]
}
```

</Spoiler>

## burns_in_daylight

<Spoiler title="显示">

bogged

```json title=""
"minecraft:burns_in_daylight": {}
```

drowned

```json title=""
"minecraft:burns_in_daylight": {}
```

magma_cube

```json title=""
"minecraft:burns_in_daylight": false
```

phantom

```json title=""
"minecraft:burns_in_daylight": {}
```

skeleton

```json title=""
"minecraft:burns_in_daylight": {}
```

stray

```json title=""
"minecraft:burns_in_daylight": {}
```

zombie

```json title=""
"minecraft:burns_in_daylight": {}
```

zombie_villager

```json title=""
"minecraft:burns_in_daylight": {}
```

</Spoiler>

## can_climb

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:can_climb": {}
```

blaze

```json title=""
"minecraft:can_climb": {}
```

bogged

```json title=""
"minecraft:can_climb": {}
```

breeze

```json title=""
"minecraft:can_climb": {}
```

camel

```json title=""
"minecraft:can_climb": {}
```

cat

```json title=""
"minecraft:can_climb": {}
```

cave_spider

```json title=""
"minecraft:can_climb": {}
```

chicken

```json title=""
"minecraft:can_climb": {}
```

</Spoiler>

## can_fly

<Spoiler title="显示">

allay

```json title=""
"minecraft:can_fly": {}
```

bat

```json title=""
"minecraft:can_fly": {}
```

bee

```json title=""
"minecraft:can_fly": {}
```

ghast

```json title=""
"minecraft:can_fly": {}
```

parrot

```json title=""
"minecraft:can_fly": {}
```

wither

```json title=""
"minecraft:can_fly": {}
```

</Spoiler>

## can_join_raid

<Spoiler title="显示">

evocation_illager

```json title=""
"minecraft:can_join_raid": {}
```

pillager

```json title=""
"minecraft:can_join_raid": {}
```

ravager

```json title=""
"minecraft:can_join_raid": {}
```

vindicator

```json title=""
"minecraft:can_join_raid": {}
```

witch

```json title=""
"minecraft:can_join_raid": {}
```

</Spoiler>

## can_power_jump

<Spoiler title="显示">

donkey

```json title="#component_groups/minecraft:donkey_saddled"
"minecraft:can_power_jump": {}
```

horse

```json title="#component_groups/minecraft:horse_saddled"
"minecraft:can_power_jump": {}
```

mule

```json title="#component_groups/minecraft:mule_saddled"
"minecraft:can_power_jump": {}
```

skeleton_horse

```json title=""
"minecraft:can_power_jump": {}
```

</Spoiler>

## celebrate_hunt

<Spoiler title="显示">

piglin

```json title="#component_groups/piglin_adult"
"minecraft:celebrate_hunt": {
    "celebration_targets": {
        "all_of": [
            {
                "test": "is_family",
                "value": "hoglin"
            }
        ]
    },
    "broadcast": true,
    "duration": 10,
    "celebrate_sound": "celebrate",
    "sound_interval": {
        "range_min": 2.0,
        "range_max": 5.0
    },
    "radius": 16
}
```

</Spoiler>

## collision_box

<Spoiler title="显示">

allay

```json title=""
"minecraft:collision_box": {
    "width": 0.35,
    "height": 0.6
}
```

armadillo

```json title=""
"minecraft:collision_box": {
    "width": 0.7,
    "height": 0.65
}
```

armor_stand

```json title=""
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.975
}
```

arrow

```json title=""
"minecraft:collision_box": {
    "width": 0.25,
    "height": 0.25
}
```

axolotl

```json title=""
"minecraft:collision_box": {
    "width": 0.75,
    "height": 0.42
}
```

bat

```json title=""
"minecraft:collision_box": {
    "width": 0.5,
    "height": 0.9
}
```

bee

```json title=""
"minecraft:collision_box": {
    "width": 0.55,
    "height": 0.5
}
```

blaze

```json title=""
"minecraft:collision_box": {
    "width": 0.5,
    "height": 1.8
}
```

</Spoiler>

## color

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:color": {
    "value": 14
}
```

sheep

```json title="#component_groups/minecraft:sheep_white"
"minecraft:color": {
    "value": 0
}
```

```json title="#component_groups/minecraft:sheep_brown"
"minecraft:color": {
    "value": 12
}
```

```json title="#component_groups/minecraft:sheep_black"
"minecraft:color": {
    "value": 15
}
```

tropicalfish

```json title="#component_groups/minecraft:tropicalfish_base_white"
"minecraft:color": {
    "value": 0
}
```

```json title="#component_groups/minecraft:tropicalfish_base_orange"
"minecraft:color": {
    "value": 1
}
```

```json title="#component_groups/minecraft:tropicalfish_base_magenta"
"minecraft:color": {
    "value": 2
}
```

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:color": {
    "value": 14
}
```

</Spoiler>

## color2

<Spoiler title="显示">

tropicalfish

```json title="#component_groups/minecraft:tropicalfish_pattern_white"
"minecraft:color2": {
    "value": 0
}
```

```json title="#component_groups/minecraft:tropicalfish_pattern_orange"
"minecraft:color2": {
    "value": 1
}
```

```json title="#component_groups/minecraft:tropicalfish_pattern_magenta"
"minecraft:color2": {
    "value": 2
}
```

</Spoiler>

## combat_regeneration

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:combat_regeneration": {}
```

</Spoiler>

## conditional_bandwidth_optimization

<Spoiler title="显示">

allay

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

area_effect_cloud

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

armadillo

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

armor_stand

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

arrow

```json title=""
"minecraft:conditional_bandwidth_optimization": {
    "default_values": {
        "max_optimized_distance": 80.0,
        "max_dropped_ticks": 7,
        "use_motion_prediction_hints": true
    }
}
```

bat

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

bee

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

blaze

```json title=""
"minecraft:conditional_bandwidth_optimization": {}
```

</Spoiler>

## custom_hit_test

<Spoiler title="显示">

hoglin

```json title="#component_groups/minecraft:hoglin_baby"
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 1.0,
            "height": 0.85,
            "pivot": [
                0,
                0.5,
                0
            ]
        }
    ]
}
```

```json title="#component_groups/minecraft:hoglin_adult"
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 2.0,
            "height": 1.75,
            "pivot": [
                0,
                1,
                0
            ]
        }
    ]
}
```

zoglin

```json title="#component_groups/zoglin_baby"
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 1.0,
            "height": 0.85,
            "pivot": [
                0,
                0.5,
                0
            ]
        }
    ]
}
```

```json title="#component_groups/zoglin_adult"
"minecraft:custom_hit_test": {
    "hitboxes": [
        {
            "width": 2.0,
            "height": 1.75,
            "pivot": [
                0,
                1,
                0
            ]
        }
    ]
}
```

</Spoiler>

## damage_over_time

<Spoiler title="显示">

axolotl

```json title="#component_groups/axolotl_dried"
"minecraft:damage_over_time": {
    "damage_per_hurt": 1,
    "time_between_hurt": 0
}
```

dolphin

```json title="#component_groups/dolphin_dried"
"minecraft:damage_over_time": {
    "damage_per_hurt": 1,
    "time_between_hurt": 0
}
```

</Spoiler>

## damage_sensor

<Spoiler title="显示">

allay

```json title=""
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_owner",
                            "subject": "other",
                            "value": true
                        }
                    ]
                }
            },
            "deals_damage": false
        }
    ]
}
```

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "mob"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:threat_detected"
        }
    }
}
```

```json title="#component_groups/minecraft:rolled_up"
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "mob"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ]
                },
                "event": "minecraft:threat_detected"
            },
            "damage_multiplier": 0.5,
            "damage_modifier": -1.0
        },
        {
            "damage_multiplier": 0.5,
            "damage_modifier": -1.0
        }
    ]
}
```

axolotl

```json title=""
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "lightning",
        "deals_damage": true,
        "damage_multiplier": 2000.0
    }
}
```

bat

```json title=""
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

bee

```json title=""
"minecraft:damage_sensor": {
    "triggers": [
        {
            "cause": "fall",
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "test": "is_block",
                    "subject": "block",
                    "value": "minecraft:sweet_berry_bush"
                }
            },
            "deals_damage": false
        }
    ]
}
```

blaze

```json title=""
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": false
    }
}
```

breeze

```json title=""
"minecraft:damage_sensor": {
    "triggers": [
        {
            "cause": "fall",
            "deals_damage": false
        },
        {
            "on_damage": {
                "filters": {
                    "test": "is_family",
                    "subject": "damager",
                    "operator": "!=",
                    "value": "wind_charge"
                }
            },
            "cause": "projectile",
            "deals_damage": false
        }
    ]
}
```

</Spoiler>

## dash

<Spoiler title="显示">

camel

```json title="#component_groups/minecraft:camel_saddled"
"minecraft:dash": {
    "cooldown_time": 2.75,
    "horizontal_momentum": 20.0,
    "vertical_momentum": 0.6
}
```

</Spoiler>

## despawn

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

axolotl

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

bat

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

blaze

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

bogged

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

camel

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

cat

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

cave_spider

```json title=""
"minecraft:despawn": {
    "despawn_from_distance": {}
}
```

</Spoiler>

## drying_out_timer

<Spoiler title="显示">

axolotl

```json title="#component_groups/axolotl_on_land"
"minecraft:drying_out_timer": {
    "total_time": 300,
    "water_bottle_refill_time": 90,
    "dried_out_event": {
        "event": "dried_out"
    },
    "stopped_drying_out_event": {
        "event": "stop_drying_out"
    },
    "recover_after_dried_out_event": {
        "event": "recover_after_dried_out"
    }
}
```

dolphin

```json title="#component_groups/dolphin_on_land"
"minecraft:drying_out_timer": {
    "total_time": 120,
    "water_bottle_refill_time": 0,
    "dried_out_event": {
        "event": "dried_out"
    },
    "stopped_drying_out_event": {
        "event": "stop_dryingout"
    },
    "recover_after_dried_out_event": {
        "event": "recover_after_dried_out"
    }
}
```

</Spoiler>

## dweller

<Spoiler title="显示">

cat

```json title=""
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "passive",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

evocation_illager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

iron_golem

```json title="#component_groups/minecraft:village_created"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "defender",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

pillager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

ravager

```json title="#component_groups/minecraft:raid_configuration"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "hostile",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": false,
    "can_migrate": true,
    "first_founding_reward": 0
}
```

villager_v2

```json title=""
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json title="#component_groups/farmer"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "farmer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

```json title="#component_groups/fisherman"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "fisherman",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

</Spoiler>

## economy_trade_table

<Spoiler title="显示">

villager_v2

```json title="#component_groups/trade_components"
"minecraft:economy_trade_table": {}
```

```json title="#component_groups/farmer"
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/economy_trades/farmer_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -25,
        -20
    ],
    "max_cured_discount": [
        -25,
        -20
    ]
}
```

```json title="#component_groups/fisherman"
"minecraft:economy_trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/economy_trades/fisherman_trades.json",
    "new_screen": true,
    "persist_trades": true,
    "cured_discount": [
        -25,
        -20
    ],
    "max_cured_discount": [
        -25,
        -20
    ]
}
```

wandering_trader

```json title=""
"minecraft:economy_trade_table": {
    "display_name": "entity.wandering_trader.name",
    "table": "trading/economy_trades/wandering_trader_trades.json",
    "new_screen": true
}
```

</Spoiler>

## entity_sensor

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:entity_sensor": {
    "subsensors": [
        {
            "event": "minecraft:no_threat_detected",
            "cooldown": 0.2,
            "range": [
                7.0,
                2.0
            ],
            "minimum_count": 0,
            "maximum_count": 0,
            "event_filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "undead"
                    },
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "any_of": [
                                    {
                                        "test": "was_last_hurt_by",
                                        "subject": "other"
                                    },
                                    {
                                        "test": "is_sprinting",
                                        "subject": "other"
                                    },
                                    {
                                        "test": "is_riding",
                                        "subject": "other"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        {
            "event": "minecraft:threat_detected",
            "cooldown": 0.2,
            "range": [
                7.0,
                2.0
            ],
            "minimum_count": 1,
            "event_filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "undead"
                    },
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "any_of": [
                                    {
                                        "test": "was_last_hurt_by",
                                        "subject": "other"
                                    },
                                    {
                                        "test": "is_sprinting",
                                        "subject": "other"
                                    },
                                    {
                                        "test": "is_riding",
                                        "subject": "other"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

parrot

```json title="#component_groups/minecraft:parrot_not_riding_player"
"minecraft:entity_sensor": {
    "relative_range": false,
    "subsensors": [
        {
            "range": [
                2.0,
                2.0
            ],
            "event_filters": {
                "all_of": [
                    {
                        "test": "is_riding",
                        "subject": "self",
                        "operator": "equals",
                        "value": true
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "operator": "equals",
                        "value": "minecraft:behavior.look_at_player"
                    }
                ]
            },
            "event": "minecraft:on_riding_player"
        }
    ]
}
```

```json title="#component_groups/minecraft:parrot_riding_player"
"minecraft:entity_sensor": {
    "relative_range": false,
    "subsensors": [
        {
            "range": [
                2.0,
                2.0
            ],
            "event_filters": {
                "all_of": [
                    {
                        "test": "is_riding",
                        "subject": "self",
                        "operator": "equals",
                        "value": false
                    },
                    {
                        "test": "has_component",
                        "subject": "self",
                        "operator": "not",
                        "value": "minecraft:behavior.look_at_player"
                    }
                ]
            },
            "event": "minecraft:on_not_riding_player"
        }
    ]
}
```

pufferfish

```json title="#component_groups/minecraft:normal_puff"
"minecraft:entity_sensor": {
    "relative_range": false,
    "subsensors": [
        {
            "range": 2.5,
            "minimum_count": 1,
            "event_filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "mob"
                    },
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "has_ability",
                                "subject": "other",
                                "operator": "not",
                                "value": "instabuild"
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:start_half_puff"
        }
    ]
}
```

```json title="#component_groups/minecraft:half_puff_secondary"
"minecraft:entity_sensor": {
    "relative_range": false,
    "subsensors": [
        {
            "range": 2.5,
            "minimum_count": 1,
            "event_filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "mob"
                    },
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "has_ability",
                                "subject": "other",
                                "operator": "not",
                                "value": "instabuild"
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:start_full_puff"
        }
    ]
}
```

```json title="#component_groups/minecraft:deflate_sensor"
"minecraft:entity_sensor": {
    "relative_range": false,
    "subsensors": [
        {
            "range": 2.9,
            "minimum_count": 0,
            "maximum_count": 0,
            "event_filters": {
                "any_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "mob"
                    },
                    {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            },
                            {
                                "test": "has_ability",
                                "subject": "other",
                                "operator": "not",
                                "value": "instabuild"
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:from_full_puff"
        }
    ]
}
```

</Spoiler>

## environment_sensor

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:rolled_up"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "any_of": [
                    {
                        "test": "on_fire"
                    },
                    {
                        "test": "in_water"
                    },
                    {
                        "test": "is_panicking"
                    },
                    {
                        "test": "is_leashed"
                    },
                    {
                        "test": "is_riding"
                    }
                ]
            },
            "event": "minecraft:unroll"
        }
    ]
}
```

axolotl

```json title="#component_groups/axolotl_in_water"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water",
                "operator": "!=",
                "value": true
            },
            "event": "start_drying_out"
        }
    ]
}
```

```json title="#component_groups/axolotl_on_land_in_rain"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "in_water_or_rain",
                "operator": "!=",
                "value": true
            },
            "event": "start_drying_out"
        },
        {
            "filters": {
                "test": "in_water",
                "operator": "==",
                "value": true
            },
            "event": "enter_water"
        }
    ]
}
```

bee

```json title="#component_groups/shelter_detection"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "event": "seek_shelter",
            "filters": {
                "all_of": [
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": false
                            },
                            {
                                "test": "weather",
                                "operator": "==",
                                "value": "precipitation"
                            }
                        ]
                    },
                    {
                        "test": "bool_property",
                        "domain": "minecraft:has_nectar",
                        "operator": "!="
                    },
                    {
                        "test": "has_biome_tag",
                        "value": "overworld"
                    }
                ]
            }
        }
    ]
}
```

```json title="#component_groups/abort_shelter_detection"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "event": "abort_sheltering",
            "filters": {
                "all_of": [
                    {
                        "test": "weather",
                        "operator": "==",
                        "value": "clear"
                    },
                    {
                        "test": "is_daytime",
                        "value": true
                    }
                ]
            }
        }
    ]
}
```

bogged

```json title=""
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:melee_mode"
        },
        {
            "filters": {
                "test": "has_ranged_weapon",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            "event": "minecraft:melee_mode"
        }
    ]
}
```

```json title="#component_groups/minecraft:ranged_attack"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_underwater",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "event": "minecraft:melee_mode"
        },
        {
            "filters": {
                "test": "has_ranged_weapon",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            "event": "minecraft:melee_mode"
        }
    ]
}
```

```json title="#component_groups/minecraft:melee_attack"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "in_water",
                        "subject": "self",
                        "operator": "==",
                        "value": false
                    },
                    {
                        "test": "has_ranged_weapon",
                        "subject": "self",
                        "operator": "==",
                        "value": true
                    }
                ]
            },
            "event": "minecraft:ranged_mode"
        }
    ]
}
```

</Spoiler>

## equip_item

<Spoiler title="显示">

bogged

```json title=""
"minecraft:equip_item": {
    "excluded_items": [
        {
            "item": "minecraft:banner:15"
        }
    ]
}
```

drowned

```json title=""
"minecraft:equip_item": {
    "excluded_items": [
        {
            "item": "minecraft:banner:15"
        }
    ]
}
```

evocation_illager

```json title=""
"minecraft:equip_item": {}
```

fox

```json title=""
"minecraft:equip_item": {}
```

husk

```json title=""
"minecraft:equip_item": {
    "excluded_items": [
        {
            "item": "minecraft:banner:15"
        }
    ]
}
```

piglin

```json title=""
"minecraft:equip_item": {
    "excluded_items": [
        {
            "item": "minecraft:banner:15"
        }
    ]
}
```

pillager

```json title=""
"minecraft:equip_item": {}
```

skeleton

```json title=""
"minecraft:equip_item": {
    "excluded_items": [
        {
            "item": "minecraft:banner:15"
        }
    ]
}
```

</Spoiler>

## equipment

<Spoiler title="显示">

bogged

```json title=""
"minecraft:equipment": {
    "table": "loot_tables/entities/skeleton_gear.json"
}
```

drowned

```json title="#component_groups/minecraft:ranged_equipment"
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_ranged_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

```json title="#component_groups/minecraft:melee_equipment"
"minecraft:equipment": {
    "table": "loot_tables/entities/drowned_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.offhand",
            "drop_chance": 1.0
        }
    ]
}
```

fox

```json title="#component_groups/minecraft:fox_with_item"
"minecraft:equipment": {
    "table": "loot_tables/entities/fox_equipment.json",
    "slot_drop_chance": [
        {
            "slot": "slot.weapon.mainhand",
            "drop_chance": 1.0
        }
    ]
}
```

husk

```json title=""
"minecraft:equipment": {
    "table": "loot_tables/entities/zombie_equipment.json"
}
```

piglin

```json title="#component_groups/ranged_unit"
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_gear_ranged.json"
}
```

```json title="#component_groups/melee_unit"
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_gear_melee.json"
}
```

piglin_brute

```json title="#component_groups/melee_unit"
"minecraft:equipment": {
    "table": "loot_tables/entities/piglin_brute_gear.json"
}
```

</Spoiler>

## equippable

<Spoiler title="显示">

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:camel_saddled"
            },
            "on_unequip": {
                "event": "minecraft:camel_unsaddled"
            }
        }
    ]
}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:donkey_saddled"
            },
            "on_unequip": {
                "event": "minecraft:donkey_unsaddled"
            }
        }
    ]
}
```

horse

```json title=""
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:horse_saddled"
            },
            "on_unequip": {
                "event": "minecraft:horse_unsaddled"
            }
        },
        {
            "slot": 1,
            "item": "horsearmoriron",
            "accepted_items": [
                "horsearmorleather",
                "horsearmoriron",
                "horsearmorgold",
                "horsearmordiamond"
            ]
        }
    ]
}
```

llama

```json title="#component_groups/minecraft:llama_tamed"
"minecraft:equippable": {
    "slots": [
        {
            "slot": 1,
            "item": "carpet",
            "accepted_items": [
                "carpet"
            ]
        }
    ]
}
```

mule

```json title="#component_groups/minecraft:mule_tamed"
"minecraft:equippable": {
    "slots": [
        {
            "slot": 0,
            "item": "saddle",
            "accepted_items": [
                "saddle"
            ],
            "on_equip": {
                "event": "minecraft:mule_saddled"
            },
            "on_unequip": {
                "event": "minecraft:mule_unsaddled"
            }
        }
    ]
}
```

trader_llama

```json title="#component_groups/minecraft:llama_tamed"
"minecraft:equippable": {
    "slots": [
        {
            "slot": 1,
            "item": "carpet",
            "accepted_items": [
                "carpet"
            ]
        }
    ]
}
```

</Spoiler>

## exhaustion_values

<Spoiler title="显示">

player

```json title=""
"minecraft:exhaustion_values": {
    "heal": 6,
    "jump": 0.05,
    "sprint_jump": 0.2,
    "mine": 0.005,
    "attack": 0.1,
    "damage": 0.1,
    "walk": 0.0,
    "sprint": 0.1,
    "swim": 0.01
}
```

</Spoiler>

## experience_reward

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:adult"
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

axolotl

```json title="#component_groups/axolotl_adult"
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

bee

```json title="#component_groups/bee_adult"
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

blaze

```json title=""
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

bogged

```json title=""
"minecraft:experience_reward": {
    "on_death": "query.last_hit_by_player ? 5 + (query.equipment_count * Math.Random(1,3)) : 0"
}
```

breeze

```json title=""
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? 10 : 0"
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

cat

```json title="#component_groups/minecraft:cat_adult"
"minecraft:experience_reward": {
    "on_bred": "Math.Random(1,7)",
    "on_death": "query.last_hit_by_player ? Math.Random(1,3) : 0"
}
```

</Spoiler>

## explode

<Spoiler title="显示">

creeper

```json title="#component_groups/minecraft:exploding"
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json title="#component_groups/minecraft:charged_exploding"
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

```json title="#component_groups/minecraft:forced_exploding"
"minecraft:explode": {
    "fuse_length": 1.5,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

ender_crystal

```json title="#component_groups/crystal_exploding"
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 6,
    "causes_fire": false,
    "destroy_affected_by_griefing": true
}
```

fireball

```json title="#component_groups/minecraft:exploding"
"minecraft:explode": {
    "fuse_length": 0,
    "fuse_lit": true,
    "power": 1,
    "causes_fire": true,
    "fire_affected_by_griefing": true,
    "destroy_affected_by_griefing": true
}
```

tnt

```json title=""
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

```json title="#component_groups/from_explosion"
"minecraft:explode": {
    "fuse_length": {
        "range_min": 0.5,
        "range_max": 2.0
    },
    "fuse_lit": true,
    "power": 4,
    "causes_fire": false
}
```

tnt_minecart

```json title="#component_groups/minecraft:primed_tnt"
"minecraft:explode": {
    "fuse_length": 4,
    "fuse_lit": true,
    "power": 3,
    "causes_fire": false
}
```

</Spoiler>

## fire_immune

<Spoiler title="显示">

blaze

```json title=""
"minecraft:fire_immune": {}
```

ender_crystal

```json title=""
"minecraft:fire_immune": true
```

ender_dragon

```json title=""
"minecraft:fire_immune": true
```

ghast

```json title=""
"minecraft:fire_immune": {}
```

magma_cube

```json title=""
"minecraft:fire_immune": {}
```

npc

```json title=""
"minecraft:fire_immune": true
```

shulker

```json title=""
"minecraft:fire_immune": true
```

strider

```json title=""
"minecraft:fire_immune": {}
```

</Spoiler>

## flocking

<Spoiler title="显示">

dolphin

```json title=""
"minecraft:flocking": {
    "in_water": false,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 6.0,
    "breach_influence": 0.0,
    "separation_weight": 1.75,
    "separation_threshold": 3.0,
    "cohesion_weight": 1.85,
    "cohesion_threshold": 6.5,
    "innner_cohesion_threshold": 3.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.0
}
```

cod

```json title=""
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

pufferfish

```json title=""
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": true,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 1.75,
    "separation_threshold": 0.95,
    "cohesion_weight": 2.0,
    "cohesion_threshold": 1.95,
    "innner_cohesion_threshold": 1.25,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

salmon

```json title=""
"minecraft:flocking": {
    "in_water": true,
    "match_variants": false,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.25,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 4.0,
    "max_height": 4.0,
    "block_distance": 1.0,
    "block_weight": 0.75
}
```

tropicalfish

```json title=""
"minecraft:flocking": {
    "in_water": true,
    "match_variants": true,
    "use_center_of_mass": false,
    "low_flock_limit": 4,
    "high_flock_limit": 8,
    "goal_weight": 2.0,
    "loner_chance": 0.1,
    "influence_radius": 3.0,
    "breach_influence": 7.0,
    "separation_weight": 0.65,
    "separation_threshold": 0.15,
    "cohesion_weight": 2.75,
    "cohesion_threshold": 1.5,
    "innner_cohesion_threshold": 1.5,
    "min_height": 1.5,
    "max_height": 6.0,
    "block_distance": 2.0,
    "block_weight": 0.85
}
```

</Spoiler>

## flying_speed

<Spoiler title="显示">

allay

```json title=""
"minecraft:flying_speed": {
    "value": 0.1
}
```

bee

```json title=""
"minecraft:flying_speed": {
    "value": 0.15
}
```

ender_dragon

```json title=""
"minecraft:flying_speed": {
    "value": 0.6
}
```

</Spoiler>

## follow_range

<Spoiler title="显示">

allay

```json title=""
"minecraft:follow_range": {
    "value": 1024
}
```

bee

```json title=""
"minecraft:follow_range": {
    "value": 1024
}
```

blaze

```json title=""
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

breeze

```json title=""
"minecraft:follow_range": {
    "value": 32.0
}
```

dolphin

```json title=""
"minecraft:follow_range": {
    "value": 48,
    "max": 48
}
```

elder_guardian

```json title=""
"minecraft:follow_range": {
    "value": 16,
    "max": 16
}
```

enderman

```json title=""
"minecraft:follow_range": {
    "value": 64,
    "max": 64
}
```

evocation_illager

```json title=""
"minecraft:follow_range": {
    "value": 64
}
```

</Spoiler>

## game_event_movement_tracking

<Spoiler title="显示">

allay

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

bat

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

bee

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

chicken

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

ender_dragon

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

parrot

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

phantom

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_flap": true
}
```

vex

```json title=""
"minecraft:game_event_movement_tracking": {
    "emit_move": false,
    "emit_swim": false
}
```

</Spoiler>

## genetics

<Spoiler title="显示">

goat

```json title=""
"minecraft:genetics": {
    "mutation_rate": 0.02,
    "genes": [
        {
            "name": "goat_variant",
            "use_simplified_breeding": true,
            "allele_range": {
                "range_min": 1,
                "range_max": 100
            },
            "genetic_variants": [
                {
                    "main_allele": {
                        "range_min": 1,
                        "range_max": 2
                    },
                    "birth_event": {
                        "event": "minecraft:born_screamer",
                        "target": "self"
                    }
                },
                {
                    "main_allele": {
                        "range_min": 3,
                        "range_max": 100
                    },
                    "birth_event": {
                        "event": "minecraft:born_default",
                        "target": "self"
                    }
                }
            ]
        }
    ]
}
```

panda

```json title=""
"minecraft:genetics": {
    "mutation_rate": 0.03125,
    "genes": [
        {
            "name": "panda_variant",
            "allele_range": {
                "range_min": 0,
                "range_max": 15
            },
            "genetic_variants": [
                {
                    "main_allele": 0,
                    "birth_event": {
                        "event": "minecraft:panda_lazy",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 1,
                    "birth_event": {
                        "event": "minecraft:panda_worried",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 2,
                    "birth_event": {
                        "event": "minecraft:panda_playful",
                        "target": "self"
                    }
                },
                {
                    "main_allele": 3,
                    "birth_event": {
                        "event": "minecraft:panda_aggressive",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 4,
                        "range_max": 7
                    },
                    "birth_event": {
                        "event": "minecraft:panda_weak",
                        "target": "self"
                    }
                },
                {
                    "both_allele": {
                        "range_min": 8,
                        "range_max": 9
                    },
                    "birth_event": {
                        "event": "minecraft:panda_brown",
                        "target": "self"
                    }
                }
            ]
        }
    ]
}
```

</Spoiler>

## giveable

<Spoiler title="显示">

panda

```json title=""
"minecraft:giveable": {
    "triggers": {
        "cooldown": 3.0,
        "items": [
            "bamboo",
            "cake"
        ],
        "on_give": {
            "event": "minecraft:on_calm",
            "target": "self"
        }
    }
}
```

</Spoiler>

## group_size

<Spoiler title="显示">

hoglin

```json title="#component_groups/minecraft:hoglin_adult"
"minecraft:group_size": {
    "radius": 32,
    "filters": {
        "all_of": [
            {
                "test": "has_component",
                "operator": "!=",
                "value": "minecraft:is_baby"
            },
            {
                "test": "is_family",
                "value": "hoglin"
            }
        ]
    }
}
```

piglin

```json title="#component_groups/piglin_adult"
"minecraft:group_size": {
    "radius": 32,
    "filters": {
        "all_of": [
            {
                "test": "has_component",
                "operator": "!=",
                "value": "minecraft:is_baby"
            },
            {
                "test": "is_family",
                "value": "piglin"
            }
        ]
    }
}
```

</Spoiler>

## grows_crop

<Spoiler title="显示">

bee

```json title="#component_groups/has_nectar"
"minecraft:grows_crop": {
    "charges": 10,
    "chance": 0.03
}
```

</Spoiler>

## healable

<Spoiler title="显示">

camel

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "cactus",
            "heal_amount": 2
        }
    ]
}
```

cat

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "fish",
            "heal_amount": 2
        },
        {
            "item": "salmon",
            "heal_amount": 2
        }
    ]
}
```

donkey

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

horse

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

llama

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "hay_block",
            "heal_amount": 10
        }
    ]
}
```

mule

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "wheat",
            "heal_amount": 2
        },
        {
            "item": "sugar",
            "heal_amount": 1
        },
        {
            "item": "hay_block",
            "heal_amount": 20
        },
        {
            "item": "apple",
            "heal_amount": 3
        },
        {
            "item": "golden_carrot",
            "heal_amount": 4
        },
        {
            "item": "golden_apple",
            "heal_amount": 10
        },
        {
            "item": "appleEnchanted",
            "heal_amount": 10
        }
    ]
}
```

parrot

```json title=""
"minecraft:healable": {
    "force_use": true,
    "filters": {
        "test": "is_riding",
        "operator": "!=",
        "value": true
    },
    "items": [
        {
            "item": "cookie",
            "heal_amount": 0,
            "effects": [
                {
                    "name": "fatal_poison",
                    "chance": 1.0,
                    "duration": 1000,
                    "amplifier": 0
                }
            ]
        }
    ]
}
```

sniffer

```json title=""
"minecraft:healable": {
    "items": [
        {
            "item": "torchflower_seeds",
            "heal_amount": 2
        }
    ]
}
```

</Spoiler>

## health

<Spoiler title="显示">

allay

```json title=""
"minecraft:health": {
    "value": 20
}
```

armadillo

```json title=""
"minecraft:health": {
    "value": 12
}
```

armor_stand

```json title=""
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

axolotl

```json title=""
"minecraft:health": {
    "value": 14
}
```

bat

```json title=""
"minecraft:health": {
    "value": 6,
    "max": 6
}
```

bee

```json title=""
"minecraft:health": {
    "value": 10,
    "max": 10
}
```

blaze

```json title=""
"minecraft:health": {
    "value": 20,
    "max": 20
}
```

bogged

```json title=""
"minecraft:health": {
    "value": 16,
    "max": 16
}
```

</Spoiler>

## heartbeat

<Spoiler title="显示">

warden

```json title=""
"minecraft:heartbeat": {
    "interval": "2.0 - math.clamp(query.anger_level / 80 * 1.5, 0, 1.5)"
}
```

</Spoiler>

## hide

<Spoiler title="显示">

villager_v2

```json title=""
"minecraft:hide": {}
```

</Spoiler>

## home

<Spoiler title="显示">

bee

```json title=""
"minecraft:home": {
    "restriction_radius": 22,
    "home_block_list": [
        "minecraft:bee_nest",
        "minecraft:beehive"
    ]
}
```

elder_guardian

```json title=""
"minecraft:home": {
    "restriction_radius": 16
}
```

guardian

```json title=""
"minecraft:home": {
    "restriction_radius": 16
}
```

piglin_brute

```json title=""
"minecraft:home": {}
```

turtle

```json title=""
"minecraft:home": {}
```

wandering_trader

```json title=""
"minecraft:home": {
    "restriction_radius": 16
}
```

</Spoiler>

## horse.jump_strength

<Spoiler title="显示">

donkey

```json title=""
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

horse

```json title=""
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

mule

```json title=""
"minecraft:horse.jump_strength": {
    "value": 0.5
}
```

skeleton_horse

```json title=""
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

zombie_horse

```json title=""
"minecraft:horse.jump_strength": {
    "value": {
        "range_min": 0.4,
        "range_max": 1.0
    }
}
```

</Spoiler>

## hurt_on_condition

<Spoiler title="显示">

allay

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

armadillo

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self"
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

armor_stand

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

arrow

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

axolotl

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

bat

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

bee

```json title=""
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "in_lava",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            "cause": "lava",
            "damage_per_tick": 4
        }
    ]
}
```

```json title="#component_groups/perish"
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "cause": "none",
            "damage_per_tick": 999
        }
    ]
}
```

</Spoiler>

## input_ground_controlled

<Spoiler title="显示">

camel

```json title="#component_groups/minecraft:camel_saddled"
"minecraft:input_ground_controlled": {}
```

donkey

```json title="#component_groups/minecraft:donkey_saddled"
"minecraft:input_ground_controlled": {}
```

horse

```json title="#component_groups/minecraft:horse_saddled"
"minecraft:input_ground_controlled": {}
```

mule

```json title="#component_groups/minecraft:mule_saddled"
"minecraft:input_ground_controlled": {}
```

skeleton_horse

```json title=""
"minecraft:input_ground_controlled": {}
```

</Spoiler>

## inside_block_notifier

<Spoiler title="显示">

boat

```json title=""
"minecraft:inside_block_notifier": {
    "block_list": [
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": true
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_down",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        },
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": false
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_up",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        }
    ]
}
```

chest_boat

```json title=""
"minecraft:inside_block_notifier": {
    "block_list": [
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": true
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_down",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        },
        {
            "block": {
                "name": "minecraft:bubble_column",
                "states": {
                    "drag_down": false
                }
            },
            "entered_block_event": {
                "event": "minecraft:entered_bubble_column_up",
                "target": "self"
            },
            "exited_block_event": {
                "event": "minecraft:exited_bubble_column",
                "target": "self"
            }
        }
    ]
}
```

</Spoiler>

## insomnia

<Spoiler title="显示">

player

```json title=""
"minecraft:insomnia": {
    "days_until_insomnia": 3
}
```

</Spoiler>

## interact

<Spoiler title="显示">

allay

```json title=""
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_sneak_held",
                            "subject": "other",
                            "value": false
                        }
                    ]
                }
            },
            "give_item": true,
            "take_item": true,
            "interact_text": "action.interact.allay"
        }
    ]
}
```

armadillo

```json title="#component_groups/minecraft:adult"
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "brush"
                        }
                    ]
                }
            },
            "play_sounds": "mob.armadillo.brush",
            "interact_text": "action.interact.brush",
            "hurt_item": 16,
            "swing": true,
            "spawn_items": {
                "table": "loot_tables/entities/armadillo_brush.json"
            }
        }
    ]
}
```

bogged

```json title=""
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "shears"
                        },
                        {
                            "test": "has_component",
                            "operator": "!=",
                            "value": "minecraft:is_sheared"
                        }
                    ]
                },
                "event": "be_sheared",
                "target": "self"
            },
            "use_item": false,
            "hurt_item": 1,
            "play_sounds": "shear",
            "spawn_items": {
                "table": "loot_tables/entities/bogged_shear.json"
            },
            "interact_text": "action.interact.shear"
        }
    ]
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "saddle",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "self",
                            "domain": "inventory",
                            "operator": "not",
                            "value": "saddle"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "saddle"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_sneak_held",
                            "subject": "other",
                            "value": false
                        }
                    ]
                },
                "target": "self"
            },
            "equip_item_slot": "0",
            "interact_text": "action.interact.saddle"
        }
    ]
}
```

cow

```json title="#component_groups/minecraft:cow_adult"
"minecraft:interact": {
    "interactions": [
        {
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "bucket:0"
                        }
                    ]
                }
            },
            "use_item": true,
            "transform_to_item": "bucket:1",
            "play_sounds": "milk",
            "interact_text": "action.interact.milk"
        }
    ]
}
```

creeper

```json title=""
"minecraft:interact": {
    "interactions": {
        "on_interact": {
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    },
                    {
                        "test": "has_equipment",
                        "domain": "hand",
                        "subject": "other",
                        "value": "flint_and_steel"
                    },
                    {
                        "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:explode"
                    }
                ]
            },
            "event": "minecraft:start_exploding_forced",
            "target": "self"
        },
        "hurt_item": 1,
        "swing": true,
        "play_sounds": "ignite",
        "interact_text": "action.interact.creeper"
    }
}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "self",
                            "domain": "inventory",
                            "operator": "not",
                            "value": "saddle"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "saddle"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_sneak_held",
                            "subject": "other",
                            "value": false
                        }
                    ]
                },
                "target": "self"
            },
            "equip_item_slot": "0",
            "interact_text": "action.interact.equip"
        }
    ]
}
```

```json title="#component_groups/minecraft:donkey_unchested"
"minecraft:interact": {
    "interactions": [
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "has_equipment",
                            "subject": "self",
                            "domain": "inventory",
                            "operator": "not",
                            "value": "saddle"
                        },
                        {
                            "test": "has_equipment",
                            "subject": "other",
                            "domain": "hand",
                            "value": "saddle"
                        },
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_sneak_held",
                            "subject": "other",
                            "value": false
                        }
                    ]
                },
                "target": "self"
            },
            "equip_item_slot": "0",
            "interact_text": "action.interact.saddle"
        },
        {
            "play_sounds": "armor.equip_generic",
            "on_interact": {
                "filters": {
                    "all_of": [
                        {
                            "test": "is_family",
                            "subject": "other",
                            "value": "player"
                        },
                        {
                            "test": "is_sneaking",
                            "subject": "other",
                            "value": false
                        },
                        {
                            "test": "has_equipment",
                            "domain": "hand",
                            "subject": "other",
                            "value": "chest"
                        }
                    ]
                },
                "event": "minecraft:on_chest",
                "target": "self"
            },
            "use_item": true,
            "interact_text": "action.interact.attachchest"
        }
    ]
}
```

</Spoiler>

## inventory

<Spoiler title="显示">

allay

```json title=""
"minecraft:inventory": {
    "inventory_size": 1
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:inventory": {
    "container_type": "horse"
}
```

chest_boat

```json title=""
"minecraft:inventory": {
    "container_type": "chest_boat",
    "inventory_size": 27,
    "can_be_siphoned_from": true
}
```

chest_minecart

```json title=""
"minecraft:inventory": {
    "container_type": "minecart_chest",
    "inventory_size": 27,
    "can_be_siphoned_from": true
}
```

command_block_minecart

```json title=""
"minecraft:inventory": {}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:inventory": {
    "inventory_size": 16,
    "container_type": "horse"
}
```

hopper_minecart

```json title=""
"minecraft:inventory": {
    "container_type": "minecart_hopper",
    "inventory_size": 5,
    "can_be_siphoned_from": true
}
```

horse

```json title="#component_groups/minecraft:horse_tamed"
"minecraft:inventory": {
    "inventory_size": 2,
    "container_type": "horse"
}
```

</Spoiler>

## is_baby

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:baby"
"minecraft:is_baby": {}
```

axolotl

```json title="#component_groups/axolotl_baby"
"minecraft:is_baby": {}
```

bee

```json title="#component_groups/bee_baby"
"minecraft:is_baby": {}
```

camel

```json title="#component_groups/minecraft:camel_baby"
"minecraft:is_baby": {}
```

cat

```json title="#component_groups/minecraft:cat_baby"
"minecraft:is_baby": {}
```

chicken

```json title="#component_groups/minecraft:chicken_baby"
"minecraft:is_baby": {}
```

cow

```json title="#component_groups/minecraft:cow_baby"
"minecraft:is_baby": {}
```

dolphin

```json title="#component_groups/dolphin_baby"
"minecraft:is_baby": {}
```

</Spoiler>

## is_charged

<Spoiler title="显示">

creeper

```json title="#component_groups/minecraft:charged_creeper"
"minecraft:is_charged": {}
```

</Spoiler>

## is_chested

<Spoiler title="显示">

donkey

```json title="#component_groups/minecraft:donkey_chested"
"minecraft:is_chested": {}
```

llama

```json title="#component_groups/minecraft:llama_chested"
"minecraft:is_chested": {}
```

mule

```json title="#component_groups/minecraft:mule_chested"
"minecraft:is_chested": {}
```

trader_llama

```json title="#component_groups/minecraft:llama_chested"
"minecraft:is_chested": {}
```

</Spoiler>

## is_dyeable

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

sheep

```json title="#component_groups/minecraft:sheep_dyeable"
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:is_dyeable": {
    "interact_text": "action.interact.dye"
}
```

</Spoiler>

## is_hidden_when_invisible

<Spoiler title="显示">

allay

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

armadillo

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

axolotl

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

bat

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

bee

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

blaze

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

bogged

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

breeze

```json title=""
"minecraft:is_hidden_when_invisible": {}
```

</Spoiler>

## is_ignited

<Spoiler title="显示">

tnt_minecart

```json title="#component_groups/minecraft:primed_tnt"
"minecraft:is_ignited": {}
```

```json title="#component_groups/minecraft:instant_explode_tnt"
"minecraft:is_ignited": {}
```

</Spoiler>

## is_illager_captain

<Spoiler title="显示">

pillager

```json title="#component_groups/minecraft:illager_squad_captain"
"minecraft:is_illager_captain": {}
```

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:is_illager_captain": {}
```

vindicator

```json title="#component_groups/minecraft:illager_squad_captain"
"minecraft:is_illager_captain": {}
```

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:is_illager_captain": {}
```

</Spoiler>

## is_pregnant

<Spoiler title="显示">

sniffer

```json title="#component_groups/sniffer_pregnant"
"minecraft:is_pregnant": {}
```

</Spoiler>

## is_saddled

<Spoiler title="显示">

camel

```json title="#component_groups/minecraft:camel_saddled"
"minecraft:is_saddled": {}
```

donkey

```json title="#component_groups/minecraft:donkey_saddled"
"minecraft:is_saddled": {}
```

horse

```json title="#component_groups/minecraft:horse_saddled"
"minecraft:is_saddled": {}
```

mule

```json title="#component_groups/minecraft:mule_saddled"
"minecraft:is_saddled": {}
```

pig

```json title="#component_groups/minecraft:pig_saddled"
"minecraft:is_saddled": {}
```

strider

```json title="#component_groups/minecraft:strider_saddled"
"minecraft:is_saddled": {}
```

</Spoiler>

## is_shaking

<Spoiler title="显示">

hoglin

```json title="#component_groups/start_zombification"
"minecraft:is_shaking": {}
```

husk

```json title="#component_groups/minecraft:convert_to_zombie"
"minecraft:is_shaking": {}
```

```json title="#component_groups/minecraft:convert_to_baby_zombie"
"minecraft:is_shaking": {}
```

piglin

```json title="#component_groups/start_zombification"
"minecraft:is_shaking": {}
```

piglin_brute

```json title="#component_groups/start_zombification"
"minecraft:is_shaking": {}
```

skeleton

```json title="#component_groups/in_powder_snow"
"minecraft:is_shaking": {}
```

strider

```json title="#component_groups/minecraft:start_suffocating"
"minecraft:is_shaking": {}
```

zombie

```json title="#component_groups/minecraft:convert_to_drowned"
"minecraft:is_shaking": {}
```

</Spoiler>

## is_sheared

<Spoiler title="显示">

bogged

```json title="#component_groups/minecraft:bogged_sheared"
"minecraft:is_sheared": {}
```

sheep

```json title="#component_groups/minecraft:sheep_sheared"
"minecraft:is_sheared": {}
```

snow_golem

```json title="#component_groups/minecraft:snowman_sheared"
"minecraft:is_sheared": {}
```

</Spoiler>

## is_stackable

<Spoiler title="显示">

boat

```json title=""
"minecraft:is_stackable": {}
```

chest_boat

```json title=""
"minecraft:is_stackable": {}
```

chest_minecart

```json title=""
"minecraft:is_stackable": {
    "value": true
}
```

hopper_minecart

```json title=""
"minecraft:is_stackable": {}
```

minecart

```json title=""
"minecraft:is_stackable": {}
```

tnt_minecart

```json title=""
"minecraft:is_stackable": {}
```

</Spoiler>

## is_stunned

<Spoiler title="显示">

ravager

```json title="#component_groups/stunned"
"minecraft:is_stunned": {}
```

</Spoiler>

## is_tamed

<Spoiler title="显示">

camel

```json title=""
"minecraft:is_tamed": {}
```

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:is_tamed": {}
```

donkey

```json title="#component_groups/minecraft:donkey_tamed"
"minecraft:is_tamed": {}
```

horse

```json title="#component_groups/minecraft:horse_tamed"
"minecraft:is_tamed": {}
```

llama

```json title="#component_groups/minecraft:llama_tamed"
"minecraft:is_tamed": {}
```

mule

```json title="#component_groups/minecraft:mule_tamed"
"minecraft:is_tamed": {}
```

ocelot

```json title="#component_groups/minecraft:ocelot_tame"
"minecraft:is_tamed": {}
```

parrot

```json title="#component_groups/minecraft:parrot_tame"
"minecraft:is_tamed": {}
```

</Spoiler>

## item_controllable

<Spoiler title="显示">

pig

```json title="#component_groups/minecraft:pig_saddled"
"minecraft:item_controllable": {
    "control_items": "carrotOnAStick"
}
```

strider

```json title="#component_groups/minecraft:strider_saddled"
"minecraft:item_controllable": {
    "control_items": "warped_fungus_on_a_stick"
}
```

</Spoiler>

## item_hopper

<Spoiler title="显示">

hopper_minecart

```json title="#component_groups/minecraft:hopper_active"
"minecraft:item_hopper": {}
```

</Spoiler>

## jump.dynamic

<Spoiler title="显示">

rabbit

```json title=""
"minecraft:jump.dynamic": {}
```

</Spoiler>

## jump.static

<Spoiler title="显示">

allay

```json title=""
"minecraft:jump.static": {}
```

armadillo

```json title=""
"minecraft:jump.static": {}
```

axolotl

```json title=""
"minecraft:jump.static": {}
```

bat

```json title=""
"minecraft:jump.static": {}
```

bee

```json title=""
"minecraft:jump.static": {}
```

blaze

```json title=""
"minecraft:jump.static": {}
```

bogged

```json title=""
"minecraft:jump.static": {}
```

breeze

```json title=""
"minecraft:jump.static": {}
```

</Spoiler>

## knockback_resistance

<Spoiler title="显示">

armor_stand

```json title=""
"minecraft:knockback_resistance": {
    "value": 1.0
}
```

breeze

```json title=""
"minecraft:knockback_resistance": {
    "value": 0.0
}
```

ender_dragon

```json title=""
"minecraft:knockback_resistance": {
    "value": 100,
    "max": 100
}
```

hoglin

```json title=""
"minecraft:knockback_resistance": {
    "value": 0.6
}
```

iron_golem

```json title=""
"minecraft:knockback_resistance": {
    "value": 1.0
}
```

ravager

```json title=""
"minecraft:knockback_resistance": {
    "value": 0.75
}
```

warden

```json title=""
"minecraft:knockback_resistance": {
    "value": 1.0
}
```

zoglin

```json title=""
"minecraft:knockback_resistance": {
    "value": 0.6
}
```

</Spoiler>

## lava_movement

<Spoiler title="显示">

strider

```json title=""
"minecraft:lava_movement": {
    "value": 0.32
}
```

</Spoiler>

## leashable

<Spoiler title="显示">

allay

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

armadillo

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

axolotl

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

bee

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

boat

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

camel

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

cat

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

chest_boat

```json title=""
"minecraft:leashable": {
    "soft_distance": 4.0,
    "hard_distance": 6.0,
    "max_distance": 10.0
}
```

</Spoiler>

## lookat

<Spoiler title="显示">

enderman

```json title=""
"minecraft:lookat": {
    "search_radius": 64.0,
    "set_target": true,
    "look_cooldown": 5.0,
    "filters": {
        "all_of": [
            {
                "subject": "other",
                "test": "is_family",
                "value": "player"
            },
            {
                "test": "has_equipment",
                "domain": "head",
                "subject": "other",
                "operator": "not",
                "value": "carved_pumpkin"
            }
        ]
    }
}
```

</Spoiler>

## loot

<Spoiler title="显示">

armor_stand

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/armor_stand.json"
}
```

blaze

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/blaze.json"
}
```

boat

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/boat.json"
}
```

bogged

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/bogged.json"
}
```

breeze

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/breeze.json"
}
```

cat

```json title="#component_groups/minecraft:cat_adult"
"minecraft:loot": {
    "table": "loot_tables/entities/cat.json"
}
```

cave_spider

```json title=""
"minecraft:loot": {
    "table": "loot_tables/entities/spider.json"
}
```

chicken

```json title="#component_groups/minecraft:chicken_adult"
"minecraft:loot": {
    "table": "loot_tables/entities/chicken.json"
}
```

</Spoiler>

## managed_wandering_trader

<Spoiler title="显示">

wandering_trader

```json title="#component_groups/managed"
"minecraft:managed_wandering_trader": {}
```

</Spoiler>

## mark_variant

<Spoiler title="显示">

bee

```json title="#component_groups/countdown_to_perish"
"minecraft:mark_variant": {
    "value": 1
}
```

horse

```json title="#component_groups/minecraft:markings_none"
"minecraft:mark_variant": {
    "value": 0
}
```

```json title="#component_groups/minecraft:markings_white_details"
"minecraft:mark_variant": {
    "value": 1
}
```

```json title="#component_groups/minecraft:markings_white_fields"
"minecraft:mark_variant": {
    "value": 2
}
```

llama

```json title=""
"minecraft:mark_variant": {
    "value": 0
}
```

mooshroom

```json title=""
"minecraft:mark_variant": {
    "value": -1
}
```

```json title="#component_groups/minecraft:mooshroom_fed_nothing"
"minecraft:mark_variant": {
    "value": -1
}
```

```json title="#component_groups/minecraft:mooshroom_brown_fed_poppy"
"minecraft:mark_variant": {
    "value": 0
}
```

</Spoiler>

## mob_effect

<Spoiler title="显示">

pufferfish

```json title="#component_groups/minecraft:full_puff"
"minecraft:mob_effect": {
    "effect_range": 0.2,
    "mob_effect": "poison",
    "effect_time": 10,
    "entity_filter": {
        "any_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "test": "is_family",
                "subject": "other",
                "value": "monster"
            }
        ]
    }
}
```

warden

```json title=""
"minecraft:mob_effect": {
    "effect_range": 20,
    "effect_time": 13,
    "mob_effect": "darkness",
    "cooldown_time": 6,
    "entity_filter": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            {
                "operator": "not",
                "test": "has_ability",
                "subject": "other",
                "value": "invulnerable"
            }
        ]
    }
}
```

</Spoiler>

## mob_effect_immunity

<Spoiler title="显示">

silverfish

```json title=""
"minecraft:mob_effect_immunity": {
    "mob_effects": [
        "infested"
    ]
}
```

slime

```json title=""
"minecraft:mob_effect_immunity": {
    "mob_effects": [
        "oozing"
    ]
}
```

</Spoiler>

## movement

<Spoiler title="显示">

allay

```json title=""
"minecraft:movement": {
    "value": 0.1
}
```

armadillo

```json title="#component_groups/minecraft:unrolled"
"minecraft:movement": {
    "value": 0.14
}
```

```json title="#component_groups/minecraft:rolled_up"
"minecraft:movement": {
    "value": 0.0
}
```

axolotl

```json title=""
"minecraft:movement": {
    "value": 0.1
}
```

bat

```json title=""
"minecraft:movement": {
    "value": 0.1
}
```

bee

```json title=""
"minecraft:movement": {
    "value": 0.3
}
```

blaze

```json title=""
"minecraft:movement": {
    "value": 0.23
}
```

bogged

```json title=""
"minecraft:movement": {
    "value": 0.25
}
```

</Spoiler>

## movement.amphibious

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:movement.amphibious": {
    "max_turn": 15.0
}
```

frog

```json title=""
"minecraft:movement.amphibious": {}
```

turtle

```json title=""
"minecraft:movement.amphibious": {
    "max_turn": 5.0
}
```

</Spoiler>

## movement.basic

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:movement.basic": {}
```

bat

```json title=""
"minecraft:movement.basic": {}
```

blaze

```json title=""
"minecraft:movement.basic": {}
```

bogged

```json title=""
"minecraft:movement.basic": {}
```

breeze

```json title=""
"minecraft:movement.basic": {}
```

camel

```json title=""
"minecraft:movement.basic": {}
```

cat

```json title=""
"minecraft:movement.basic": {}
```

cave_spider

```json title=""
"minecraft:movement.basic": {}
```

</Spoiler>

## movement.fly

<Spoiler title="显示">

parrot

```json title=""
"minecraft:movement.fly": {}
```

</Spoiler>

## movement.generic

<Spoiler title="显示">

drowned

```json title=""
"minecraft:movement.generic": {}
```

</Spoiler>

## movement.glide

<Spoiler title="显示">

phantom

```json title=""
"minecraft:movement.glide": {
    "start_speed": 0.1,
    "speed_when_turning": 0.2
}
```

</Spoiler>

## movement.hover

<Spoiler title="显示">

allay

```json title=""
"minecraft:movement.hover": {}
```

bee

```json title=""
"minecraft:movement.hover": {}
```

</Spoiler>

## movement.jump

<Spoiler title="显示">

magma_cube

```json title=""
"minecraft:movement.jump": {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```json title="#component_groups/minecraft:slime_calm"
"minecraft:movement.jump": {
    "jump_delay": [
        2.0,
        6.0
    ]
}
```

```json title="#component_groups/minecraft:slime_aggressive"
"minecraft:movement.jump": {
    "jump_delay": [
        0.667,
        2.0
    ]
}
```

slime

```json title=""
"minecraft:movement.jump": {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```json title="#component_groups/minecraft:slime_calm"
"minecraft:movement.jump": {
    "jump_delay": [
        0.5,
        1.5
    ]
}
```

```json title="#component_groups/minecraft:slime_aggressive"
"minecraft:movement.jump": {
    "jump_delay": [
        0.16,
        0.5
    ]
}
```

</Spoiler>

## movement.skip

<Spoiler title="显示">

rabbit

```json title=""
"minecraft:movement.skip": {}
```

</Spoiler>

## movement.sway

<Spoiler title="显示">

elder_guardian

```json title=""
"minecraft:movement.sway": {}
```

cod

```json title=""
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

guardian

```json title=""
"minecraft:movement.sway": {}
```

pufferfish

```json title=""
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

salmon

```json title=""
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

tadpole

```json title=""
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

tropicalfish

```json title=""
"minecraft:movement.sway": {
    "sway_amplitude": 0.0
}
```

</Spoiler>

## movement_sound_distance_offset

<Spoiler title="显示">

warden

```json title=""
"minecraft:movement_sound_distance_offset": {
    "value": 0.55
}
```

</Spoiler>

## nameable

<Spoiler title="显示">

allay

```json title=""
"minecraft:nameable": {}
```

armadillo

```json title=""
"minecraft:nameable": {}
```

armor_stand

```json title=""
"minecraft:nameable": {}
```

axolotl

```json title=""
"minecraft:nameable": {}
```

bat

```json title=""
"minecraft:nameable": {}
```

bee

```json title=""
"minecraft:nameable": {}
```

blaze

```json title=""
"minecraft:nameable": {}
```

bogged

```json title=""
"minecraft:nameable": {}
```

</Spoiler>

## navigation.climb

<Spoiler title="显示">

cave_spider

```json title=""
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

spider

```json title=""
"minecraft:navigation.climb": {
    "can_path_over_water": true
}
```

</Spoiler>

## navigation.float

<Spoiler title="显示">

bat

```json title=""
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

ghast

```json title=""
"minecraft:navigation.float": {
    "can_path_over_water": true
}
```

</Spoiler>

## navigation.fly

<Spoiler title="显示">

parrot

```json title=""
"minecraft:navigation.fly": {
    "can_path_over_water": true,
    "can_path_from_air": true
}
```

</Spoiler>

## navigation.generic

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_sink": false,
    "avoid_damage_blocks": true
}
```

dolphin

```json title=""
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json title="#component_groups/dolphin_swimming_navigation"
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true,
    "can_sink": false
}
```

```json title="#component_groups/dolphin_on_land"
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": true,
    "can_swim": true,
    "can_walk": true,
    "can_breach": false,
    "can_jump": false
}
```

drowned

```json title=""
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

```json title="#component_groups/minecraft:hunter_mode"
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": true,
    "can_walk": true,
    "avoid_sun": true
}
```

```json title="#component_groups/minecraft:wander_mode"
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_break_doors": true,
    "can_swim": false,
    "can_walk": true,
    "avoid_sun": true
}
```

elder_guardian

```json title=""
"minecraft:navigation.generic": {
    "is_amphibious": true,
    "can_path_over_water": false,
    "can_swim": true,
    "can_walk": false,
    "can_breach": true
}
```

</Spoiler>

## navigation.hover

<Spoiler title="显示">

allay

```json title=""
"minecraft:navigation.hover": {
    "can_path_over_water": true,
    "can_sink": false,
    "can_pass_doors": false,
    "can_path_from_air": true,
    "avoid_water": true,
    "avoid_damage_blocks": true,
    "avoid_sun": false
}
```

bee

```json title=""
"minecraft:navigation.hover": {
    "can_path_over_water": true,
    "can_sink": false,
    "can_pass_doors": false,
    "can_path_from_air": true,
    "avoid_water": true,
    "avoid_damage_blocks": true,
    "avoid_sun": false
}
```

</Spoiler>

## navigation.walk

<Spoiler title="显示">

armadillo

```json title=""
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true,
    "avoid_water": true
}
```

blaze

```json title=""
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

bogged

```json title=""
"minecraft:navigation.walk": {
    "is_amphibious": true,
    "avoid_sun": true,
    "avoid_water": true
}
```

breeze

```json title=""
"minecraft:navigation.walk": {
    "blocks_to_avoid": [
        {
            "tags": "query.any_tag('trapdoors')"
        }
    ]
}
```

camel

```json title=""
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

cat

```json title=""
"minecraft:navigation.walk": {
    "can_float": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

chicken

```json title=""
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_damage_blocks": true
}
```

cow

```json title=""
"minecraft:navigation.walk": {
    "can_path_over_water": true,
    "avoid_water": true,
    "avoid_damage_blocks": true
}
```

</Spoiler>

## npc

<Spoiler title="显示">

npc

```json title=""
"minecraft:npc": {
    "npc_data": {
        "portrait_offsets": {
            "translate": [
                -7,
                50,
                0
            ],
            "scale": [
                1.75,
                1.75,
                1.75
            ]
        },
        "picker_offsets": {
            "translate": [
                0,
                20,
                0
            ],
            "scale": [
                1.7,
                1.7,
                1.7
            ]
        },
        "skin_list": [
            {
                "variant": 0
            },
            {
                "variant": 1
            },
            {
                "variant": 2
            },
            {
                "variant": 3
            },
            {
                "variant": 4
            },
            {
                "variant": 5
            },
            {
                "variant": 6
            },
            {
                "variant": 7
            },
            {
                "variant": 8
            },
            {
                "variant": 9
            },
            {
                "variant": 10
            },
            {
                "variant": 11
            },
            {
                "variant": 12
            },
            {
                "variant": 13
            },
            {
                "variant": 14
            },
            {
                "variant": 15
            },
            {
                "variant": 16
            },
            {
                "variant": 17
            },
            {
                "variant": 18
            },
            {
                "variant": 19
            },
            {
                "variant": 25
            },
            {
                "variant": 26
            },
            {
                "variant": 27
            },
            {
                "variant": 28
            },
            {
                "variant": 29
            },
            {
                "variant": 30
            },
            {
                "variant": 31
            },
            {
                "variant": 32
            },
            {
                "variant": 33
            },
            {
                "variant": 34
            },
            {
                "variant": 20
            },
            {
                "variant": 21
            },
            {
                "variant": 22
            },
            {
                "variant": 23
            },
            {
                "variant": 24
            },
            {
                "variant": 35
            },
            {
                "variant": 36
            },
            {
                "variant": 37
            },
            {
                "variant": 38
            },
            {
                "variant": 39
            },
            {
                "variant": 40
            },
            {
                "variant": 41
            },
            {
                "variant": 42
            },
            {
                "variant": 43
            },
            {
                "variant": 44
            },
            {
                "variant": 50
            },
            {
                "variant": 51
            },
            {
                "variant": 52
            },
            {
                "variant": 53
            },
            {
                "variant": 54
            },
            {
                "variant": 45
            },
            {
                "variant": 46
            },
            {
                "variant": 47
            },
            {
                "variant": 48
            },
            {
                "variant": 49
            },
            {
                "variant": 55
            },
            {
                "variant": 56
            },
            {
                "variant": 57
            },
            {
                "variant": 58
            },
            {
                "variant": 59
            }
        ]
    }
}
```

</Spoiler>

## on_death

<Spoiler title="显示">

ender_dragon

```json title=""
"minecraft:on_death": {
    "event": "minecraft:start_death",
    "target": "self"
}
```

</Spoiler>

## on_friendly_anger

<Spoiler title="显示">

panda

```json title="#component_groups/minecraft:panda_aggressive"
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

polar_bear

```json title="#component_groups/minecraft:adult_wild"
"minecraft:on_friendly_anger": {
    "event": "minecraft:on_anger",
    "target": "self"
}
```

trader_llama

```json title="#component_groups/minecraft:llama_wandering_trader"
"minecraft:on_friendly_anger": {
    "event": "minecraft:defend_wandering_trader",
    "target": "self"
}
```

</Spoiler>

## on_hurt

<Spoiler title="显示">

blaze

```json title=""
"minecraft:on_hurt": {
    "event": "minecraft:on_hurt_event",
    "target": "self"
}
```

ender_crystal

```json title=""
"minecraft:on_hurt": {
    "event": "minecraft:crystal_explode",
    "target": "self"
}
```

pillager

```json title="#component_groups/minecraft:illager_squad_captain"
"minecraft:on_hurt": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:on_hurt": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

```json title="#component_groups/minecraft:patrol_follower"
"minecraft:on_hurt": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

</Spoiler>

## on_hurt_by_player

<Spoiler title="显示">

blaze

```json title=""
"minecraft:on_hurt_by_player": {
    "event": "minecraft:on_hurt_event",
    "target": "self"
}
```

pillager

```json title="#component_groups/minecraft:illager_squad_captain"
"minecraft:on_hurt_by_player": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

```json title="#component_groups/minecraft:patrol_captain"
"minecraft:on_hurt_by_player": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

```json title="#component_groups/minecraft:patrol_follower"
"minecraft:on_hurt_by_player": {
    "event": "minecraft:ranged_mode",
    "target": "self"
}
```

</Spoiler>

## on_start_landing

<Spoiler title="显示">

ender_dragon

```json title=""
"minecraft:on_start_landing": {
    "event": "minecraft:start_land",
    "target": "self"
}
```

</Spoiler>

## on_start_takeoff

<Spoiler title="显示">

ender_dragon

```json title=""
"minecraft:on_start_takeoff": {
    "event": "minecraft:start_fly",
    "target": "self"
}
```

</Spoiler>

## on_target_acquired

<Spoiler title="显示">

bee

```json title=""
"minecraft:on_target_acquired": {
    "event": "attacked",
    "target": "self"
}
```

cave_spider

```json title="#component_groups/minecraft:spider_neutral"
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry"
}
```

dolphin

```json title=""
"minecraft:on_target_acquired": {
    "event": "become_angry",
    "target": "self"
}
```

```json title="#component_groups/dolphin_angry"
"minecraft:on_target_acquired": {}
```

drowned

```json title=""
"minecraft:on_target_acquired": {
    "event": "minecraft:has_target",
    "target": "self"
}
```

enderman

```json title="#component_groups/minecraft:enderman_calm"
"minecraft:on_target_acquired": {
    "event": "minecraft:become_angry",
    "target": "self"
}
```

hoglin

```json title="#component_groups/minecraft:hoglin_adult"
"minecraft:on_target_acquired": {
    "event": "become_angry_event",
    "target": "self"
}
```

llama

```json title=""
"minecraft:on_target_acquired": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:mad_at_wolf",
    "target": "self"
}
```

</Spoiler>

## on_target_escape

<Spoiler title="显示">

creeper

```json title=""
"minecraft:on_target_escape": {
    "event": "minecraft:stop_exploding",
    "target": "self"
}
```

```json title="#component_groups/minecraft:forced_exploding"
"minecraft:on_target_escape": {}
```

```json title="#component_groups/minecraft:forced_charged_exploding"
"minecraft:on_target_escape": {}
```

dolphin

```json title=""
"minecraft:on_target_escape": {
    "target": "self"
}
```

drowned

```json title=""
"minecraft:on_target_escape": {
    "event": "minecraft:lost_target",
    "target": "self"
}
```

llama

```json title=""
"minecraft:on_target_escape": {
    "filters": {
        "all_of": [
            {
                "test": "is_family",
                "subject": "target",
                "value": "wolf"
            },
            {
                "test": "has_component",
                "subject": "target",
                "operator": "!=",
                "value": "minecraft:is_tamed"
            }
        ]
    },
    "event": "minecraft:on_calm",
    "target": "self"
}
```

magma_cube

```json title=""
"minecraft:on_target_escape": {
    "event": "minecraft:become_calm",
    "target": "self"
}
```

panda

```json title="#component_groups/minecraft:panda_adult"
"minecraft:on_target_escape": {
    "event": "minecraft:on_calm",
    "target": "self"
}
```

</Spoiler>

## on_wake_with_owner

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:on_wake_with_owner": {
    "event": "minecraft:pet_slept_with_owner",
    "target": "self"
}
```

</Spoiler>

## out_of_control

<Spoiler title="显示">

boat

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:out_of_control": {}
```

```json title="#component_groups/minecraft:above_bubble_column_up"
"minecraft:out_of_control": {}
```

chest_boat

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:out_of_control": {}
```

```json title="#component_groups/minecraft:above_bubble_column_up"
"minecraft:out_of_control": {}
```

</Spoiler>

## peek

<Spoiler title="显示">

shulker

```json title=""
"minecraft:peek": {
    "on_open": {
        "event": "minecraft:on_open"
    },
    "on_close": {
        "event": "minecraft:on_close"
    },
    "on_target_open": {
        "event": "minecraft:on_open"
    }
}
```

</Spoiler>

## persistent

<Spoiler title="显示">

armor_stand

```json title=""
"minecraft:persistent": {}
```

breeze

```json title=""
"minecraft:persistent": {}
```

ender_dragon

```json title=""
"minecraft:persistent": {}
```

evocation_illager

```json title=""
"minecraft:persistent": {}
```

```json title="#component_groups/minecraft:raid_persistence"
"minecraft:persistent": {}
```

iron_golem

```json title=""
"minecraft:persistent": {}
```

npc

```json title=""
"minecraft:persistent": {}
```

pillager

```json title="#component_groups/minecraft:raid_persistence"
"minecraft:persistent": {}
```

</Spoiler>

## physics

<Spoiler title="显示">

allay

```json title=""
"minecraft:physics": {
    "has_gravity": false
}
```

area_effect_cloud

```json title=""
"minecraft:physics": {
    "has_collision": false
}
```

armadillo

```json title=""
"minecraft:physics": {}
```

armor_stand

```json title=""
"minecraft:physics": {}
```

arrow

```json title=""
"minecraft:physics": {}
```

axolotl

```json title=""
"minecraft:physics": {}
```

bat

```json title=""
"minecraft:physics": {}
```

bee

```json title=""
"minecraft:physics": {}
```

</Spoiler>

## player.exhaustion

<Spoiler title="显示">

player

```json title=""
"minecraft:player.exhaustion": {
    "value": 0,
    "max": 20
}
```

</Spoiler>

## player.experience

<Spoiler title="显示">

player

```json title=""
"minecraft:player.experience": {
    "value": 0,
    "max": 1
}
```

</Spoiler>

## player.level

<Spoiler title="显示">

player

```json title=""
"minecraft:player.level": {
    "value": 0,
    "max": 24791
}
```

</Spoiler>

## player.saturation

<Spoiler title="显示">

player

```json title=""
"minecraft:player.saturation": {
    "value": 5,
    "max": 20
}
```

</Spoiler>

## preferred_path

<Spoiler title="显示">

iron_golem

```json title=""
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "smooth_stone_slab",
                "sandstone_slab",
                "cobblestone_slab",
                "brick_slab",
                "stone_brick_slab",
                "quartz_slab",
                "nether_brick_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "white_stained_glass",
                "orange_stained_glass",
                "magenta_stained_glass",
                "light_blue_stained_glass",
                "yellow_stained_glass",
                "lime_stained_glass",
                "pink_stained_glass",
                "gray_stained_glass",
                "light_gray_stained_glass",
                "cyan_stained_glass",
                "purple_stained_glass",
                "blue_stained_glass",
                "brown_stained_glass",
                "green_stained_glass",
                "red_stained_glass",
                "black_stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

villager_v2

```json title="#component_groups/baby"
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "smooth_stone_slab",
                "sandstone_slab",
                "cobblestone_slab",
                "brick_slab",
                "stone_brick_slab",
                "quartz_slab",
                "nether_brick_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "white_stained_glass",
                "orange_stained_glass",
                "magenta_stained_glass",
                "light_blue_stained_glass",
                "yellow_stained_glass",
                "lime_stained_glass",
                "pink_stained_glass",
                "gray_stained_glass",
                "light_gray_stained_glass",
                "cyan_stained_glass",
                "purple_stained_glass",
                "blue_stained_glass",
                "brown_stained_glass",
                "green_stained_glass",
                "red_stained_glass",
                "black_stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

```json title="#component_groups/adult"
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 20,
    "default_block_cost": 3,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": [
                "grass_path"
            ]
        },
        {
            "cost": 1,
            "blocks": [
                "cobblestone",
                "stone",
                "stonebrick",
                "sandstone",
                "mossy_cobblestone",
                "smooth_stone_slab",
                "sandstone_slab",
                "cobblestone_slab",
                "brick_slab",
                "stone_brick_slab",
                "quartz_slab",
                "nether_brick_slab",
                "stone_slab2",
                "stone_slab3",
                "stone_slab4",
                "double_stone_slab",
                "double_stone_slab2",
                "double_stone_slab3",
                "double_stone_slab4",
                "wooden_slab",
                "double_wooden_slab",
                "planks",
                "brick_block",
                "nether_brick",
                "red_nether_brick",
                "end_bricks",
                "red_sandstone",
                "white_stained_glass",
                "orange_stained_glass",
                "magenta_stained_glass",
                "light_blue_stained_glass",
                "yellow_stained_glass",
                "lime_stained_glass",
                "pink_stained_glass",
                "gray_stained_glass",
                "light_gray_stained_glass",
                "cyan_stained_glass",
                "purple_stained_glass",
                "blue_stained_glass",
                "brown_stained_glass",
                "green_stained_glass",
                "red_stained_glass",
                "black_stained_glass",
                "glass",
                "glowstone",
                "prismarine",
                "emerald_block",
                "diamond_block",
                "lapis_block",
                "gold_block",
                "redstone_block",
                "purple_glazed_terracotta",
                "white_glazed_terracotta",
                "orange_glazed_terracotta",
                "magenta_glazed_terracotta",
                "light_blue_glazed_terracotta",
                "yellow_glazed_terracotta",
                "lime_glazed_terracotta",
                "pink_glazed_terracotta",
                "gray_glazed_terracotta",
                "silver_glazed_terracotta",
                "cyan_glazed_terracotta",
                "blue_glazed_terracotta",
                "brown_glazed_terracotta",
                "green_glazed_terracotta",
                "red_glazed_terracotta",
                "black_glazed_terracotta"
            ]
        },
        {
            "cost": 50,
            "blocks": [
                "bed",
                "lectern",
                "composter",
                "grindstone",
                "blast_furnace",
                "smoker",
                "fletching_table",
                "cartography_table",
                "brewing_stand",
                "smithing_table",
                "cauldron",
                "barrel",
                "loom",
                "stonecutter"
            ]
        }
    ]
}
```

warden

```json title=""
"minecraft:preferred_path": {
    "max_fall_blocks": 20
}
```

</Spoiler>

## projectile

<Spoiler title="显示">

arrow

```json title=""
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                4
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {
            "apply_effect_to_blocking_targets": false
        }
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```json title="#component_groups/minecraft:hard_arrow"
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": [
                1,
                5
            ],
            "knockback": true,
            "semi_random_diff_damage": false,
            "destroy_on_hit": true
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {
            "apply_effect_to_blocking_targets": false
        }
    },
    "hit_sound": "bow.hit",
    "power": 1.6,
    "gravity": 0.05,
    "uncertainty_base": 16,
    "uncertainty_multiplier": 4,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

```json title="#component_groups/minecraft:player_arrow"
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": true,
            "semi_random_diff_damage": true,
            "destroy_on_hit": true,
            "max_critical_damage": 10,
            "min_critical_damage": 9,
            "power_multiplier": 0.97
        },
        "stick_in_ground": {
            "shake_time": 0.35
        },
        "arrow_effect": {
            "apply_effect_to_blocking_targets": false
        }
    },
    "hit_sound": "bow.hit",
    "power": 5.0,
    "gravity": 0.05,
    "uncertainty_base": 1,
    "uncertainty_multiplier": 0,
    "anchor": 1,
    "should_bounce": true,
    "offset": [
        0,
        -0.1,
        0
    ]
}
```

breeze_wind_charge_projectile

```json title=""
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 1,
            "knockback": true
        },
        "remove_on_hit": {}
    },
    "power": 0.7,
    "gravity": 0.0,
    "inertia": 1.0,
    "liquid_inertia": 1.0,
    "uncertainty_base": 5.0,
    "uncertainty_multiplier": 4.0,
    "reflect_on_hurt": true,
    "ignored_entities": [
        "ender_crystal",
        "wind_charge_projectile",
        "breeze_wind_charge_projectile"
    ],
    "hit_nearest_passenger": true
}
```

dragon_fireball

```json title=""
"minecraft:projectile": {
    "on_hit": {
        "spawn_aoe_cloud": {
            "radius": 6.0,
            "radius_on_use": 0,
            "potion": 23,
            "particle": "dragonbreath",
            "duration": 120,
            "color": [
                220,
                0,
                239
            ],
            "affect_owner": false,
            "reapplication_delay": 20
        },
        "remove_on_hit": {}
    },
    "power": 1.3,
    "gravity": 0.0,
    "inertia": 1,
    "anchor": 2,
    "offset": [
        0,
        0.5,
        0
    ],
    "semi_random_diff_damage": true,
    "uncertainty_base": 10.0,
    "reflect_on_hurt": true,
    "hit_sound": "explode"
}
```

egg

```json title=""
"minecraft:projectile": {
    "on_hit": {
        "impact_damage": {
            "damage": 0,
            "knockback": true,
            "destroy_on_hit": true
        },
        "spawn_chance": {
            "first_spawn_chance": 8,
            "second_spawn_chance": 32,
            "first_spawn_count": 1,
            "second_spawn_count": 4,
            "spawn_definition": "minecraft:chicken",
            "spawn_baby": true
        },
        "remove_on_hit": {},
        "particle_on_hit": {
            "particle_type": "iconcrack",
            "num_particles": 6,
            "on_entity_hit": true,
            "on_other_hit": true
        }
    },
    "power": 1.5,
    "gravity": 0.03,
    "angle_offset": 0.0
}
```

ender_pearl

```json title=""
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "spawn_chance": {
            "first_spawn_percent_chance": 5.0,
            "first_spawn_count": 1,
            "spawn_definition": "minecraft:endermite"
        },
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

```json title="#component_groups/minecraft:no_spawn"
"minecraft:projectile": {
    "on_hit": {
        "teleport_owner": {},
        "remove_on_hit": {}
    },
    "power": 1.5,
    "gravity": 0.025,
    "angle_offset": 0.0,
    "inertia": 1,
    "liquid_inertia": 1
}
```

</Spoiler>

## pushable

<Spoiler title="显示">

allay

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

armadillo

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

armor_stand

```json title=""
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

arrow

```json title=""
"minecraft:pushable": {
    "is_pushable": false,
    "is_pushable_by_piston": true
}
```

axolotl

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

bee

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

blaze

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

boat

```json title=""
"minecraft:pushable": {
    "is_pushable": true,
    "is_pushable_by_piston": true
}
```

</Spoiler>

## raid_trigger

<Spoiler title="显示">

player

```json title="#component_groups/minecraft:raid_trigger"
"minecraft:raid_trigger": {
    "triggered_event": {
        "event": "minecraft:remove_raid_trigger",
        "target": "self"
    }
}
```

</Spoiler>

## rail_movement

<Spoiler title="显示">

chest_minecart

```json title=""
"minecraft:rail_movement": {}
```

command_block_minecart

```json title=""
"minecraft:rail_movement": {}
```

hopper_minecart

```json title=""
"minecraft:rail_movement": {}
```

minecart

```json title=""
"minecraft:rail_movement": {}
```

tnt_minecart

```json title=""
"minecraft:rail_movement": {}
```

</Spoiler>

## rail_sensor

<Spoiler title="显示">

command_block_minecart

```json title="#component_groups/minecraft:command_block_active"
"minecraft:rail_sensor": {
    "check_block_types": true,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_deactivate": {
        "event": "minecraft:command_block_deactivate"
    }
}
```

```json title="#component_groups/minecraft:command_block_inactive"
"minecraft:rail_sensor": {
    "check_block_types": false,
    "eject_on_activate": false,
    "eject_on_deactivate": false,
    "tick_command_block_on_activate": true,
    "tick_command_block_on_deactivate": false,
    "on_activate": {
        "event": "minecraft:command_block_activate"
    }
}
```

hopper_minecart

```json title="#component_groups/minecraft:hopper_active"
"minecraft:rail_sensor": {
    "on_activate": {
        "event": "minecraft:hopper_deactivate"
    }
}
```

```json title="#component_groups/minecraft:hopper_inactive"
"minecraft:rail_sensor": {
    "on_deactivate": {
        "event": "minecraft:hopper_activate"
    }
}
```

minecart

```json title=""
"minecraft:rail_sensor": {
    "eject_on_activate": true
}
```

tnt_minecart

```json title="#component_groups/minecraft:primed_tnt"
"minecraft:rail_sensor": {}
```

```json title="#component_groups/minecraft:instant_explode_tnt"
"minecraft:rail_sensor": {}
```

```json title="#component_groups/minecraft:inactive"
"minecraft:rail_sensor": {
    "on_activate": {
        "filters": {
            "all_of": [
                {
                    "test": "is_game_rule",
                    "domain": "tntexplodes",
                    "operator": "==",
                    "value": true
                }
            ]
        },
        "event": "minecraft:on_prime"
    }
}
```

</Spoiler>

## ravager_blocked

<Spoiler title="显示">

ravager

```json title=""
"minecraft:ravager_blocked": {
    "knockback_strength": 3.0,
    "reaction_choices": [
        {
            "weight": 1,
            "value": {
                "event": "minecraft:become_stunned",
                "target": "self"
            }
        },
        {
            "weight": 1
        }
    ]
}
```

</Spoiler>

## reflect_projectiles

<Spoiler title="显示">

breeze

```json title=""
"minecraft:reflect_projectiles": {
    "reflected_projectiles": [
        "xp_bottle",
        "thrown_trident",
        "shulker_bullet",
        "dragon_fireball",
        "arrow",
        "snowball",
        "egg",
        "fireball",
        "splash_potion",
        "ender_pearl",
        "wither_skull",
        "wither_skull_dangerous",
        "small_fireball",
        "lingering_potion",
        "llama_spit",
        "fireworks_rocket",
        "fishing_hook"
    ],
    "azimuth_angle": "180.0 + Math.random(-20.0, 20.0)",
    "reflection_scale": "0.5"
}
```

</Spoiler>

## rideable

<Spoiler title="显示">

boat

```json title=""
"minecraft:rideable": {
    "seat_count": 2,
    "passenger_max_width": 1.375,
    "interact_text": "action.interact.ride.boat",
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.0,
                -0.2,
                0.0
            ],
            "min_rider_count": 0,
            "max_rider_count": 1,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                0.2,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        },
        {
            "position": [
                -0.6,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        }
    ]
}
```

```json title="#component_groups/minecraft:can_ride_default"
"minecraft:rideable": {
    "seat_count": 2,
    "passenger_max_width": 1.375,
    "interact_text": "action.interact.ride.boat",
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.0,
                -0.2,
                0.0
            ],
            "min_rider_count": 0,
            "max_rider_count": 1,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                0.2,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        },
        {
            "position": [
                -0.6,
                -0.2,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        }
    ]
}
```

```json title="#component_groups/minecraft:can_ride_bamboo"
"minecraft:rideable": {
    "seat_count": 2,
    "passenger_max_width": 1.375,
    "interact_text": "action.interact.ride.boat",
    "pull_in_entities": true,
    "seats": [
        {
            "position": [
                0.0,
                0.1,
                0.0
            ],
            "min_rider_count": 0,
            "max_rider_count": 1,
            "rotate_rider_by": -90,
            "lock_rider_rotation": 90
        },
        {
            "position": [
                0.2,
                0.1,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        },
        {
            "position": [
                -0.6,
                0.1,
                0.0
            ],
            "min_rider_count": 2,
            "max_rider_count": 2,
            "rotate_rider_by": "query.has_any_family('blaze', 'creeper', 'enderman', 'illager', 'magmacube', 'piglin', 'player', 'skeleton', 'slime', 'villager', 'wandering_trader', 'witch', 'zombie', 'zombie_pigman') ? -90 : 0",
            "lock_rider_rotation": 90
        }
    ]
}
```

camel

```json title="#component_groups/minecraft:camel_adult"
"minecraft:rideable": {
    "seat_count": 2,
    "crouching_skip_interact": true,
    "pull_in_entities": true,
    "family_types": [
        "player"
    ],
    "interact_text": "action.interact.ride.horse",
    "seats": [
        {
            "min_rider_count": 0,
            "max_rider_count": 2,
            "position": [
                0.0,
                1.905,
                0.5
            ]
        },
        {
            "min_rider_count": 1,
            "max_rider_count": 2,
            "position": [
                0.0,
                1.905,
                -0.5
            ]
        }
    ]
}
```

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.35,
            0.0
        ]
    }
}
```

cave_spider

```json title=""
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "zombie"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            0.0
        ]
    }
}
```

```json title="#component_groups/minecraft:spider_jockey"
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            -0.1
        ]
    }
}
```

```json title="#component_groups/minecraft:spider_stray_jockey"
"minecraft:rideable": {
    "seat_count": 1,
    "family_types": [
        "skeleton"
    ],
    "seats": {
        "position": [
            0.0,
            0.3,
            -0.1
        ]
    }
}
```

</Spoiler>

## scale

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:baby"
"minecraft:scale": {
    "value": 0.6
}
```

axolotl

```json title="#component_groups/axolotl_baby"
"minecraft:scale": {
    "value": 0.5
}
```

bee

```json title="#component_groups/bee_baby"
"minecraft:scale": {
    "value": 0.5
}
```

camel

```json title="#component_groups/minecraft:camel_baby"
"minecraft:scale": {
    "value": 0.45
}
```

cat

```json title="#component_groups/minecraft:cat_baby"
"minecraft:scale": {
    "value": 0.4
}
```

```json title="#component_groups/minecraft:cat_adult"
"minecraft:scale": {
    "value": 0.8
}
```

chicken

```json title="#component_groups/minecraft:chicken_baby"
"minecraft:scale": {
    "value": 0.5
}
```

cow

```json title="#component_groups/minecraft:cow_baby"
"minecraft:scale": {
    "value": 0.5
}
```

</Spoiler>

## scale_by_age

<Spoiler title="显示">

donkey

```json title="#component_groups/minecraft:donkey_baby"
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

horse

```json title="#component_groups/minecraft:horse_baby"
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

mule

```json title="#component_groups/minecraft:mule_baby"
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

skeleton_horse

```json title="#component_groups/minecraft:skeleton_horse_baby"
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

zombie_horse

```json title="#component_groups/minecraft:horse_baby"
"minecraft:scale_by_age": {
    "start_scale": 0.5,
    "end_scale": 1.0
}
```

</Spoiler>

## scheduler

<Spoiler title="显示">

fox

```json title=""
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 0,
    "scheduled_events": [
        {
            "filters": [
                {
                    "test": "is_sleeping",
                    "value": true
                }
            ],
            "event": "minecraft:ambient_sleep"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_daytime",
                        "value": false
                    },
                    {
                        "test": "distance_to_nearest_player",
                        "operator": ">",
                        "value": 16
                    }
                ]
            },
            "event": "minecraft:ambient_night"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "is_sleeping",
                        "value": false
                    },
                    {
                        "any_of": [
                            {
                                "test": "is_daytime",
                                "value": true
                            },
                            {
                                "test": "distance_to_nearest_player",
                                "operator": "<=",
                                "value": 16
                            }
                        ]
                    }
                ]
            },
            "event": "minecraft:ambient_normal"
        }
    ]
}
```

villager_v2

```json title="#component_groups/work_schedule"
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_work_pro_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json title="#component_groups/basic_schedule"
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 8000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 8000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 10000
                    }
                ]
            },
            "event": "minecraft:schedule_gather_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 10000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_wander_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

```json title="#component_groups/child_schedule"
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 0
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 11000
                    }
                ]
            },
            "event": "minecraft:schedule_play_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 11000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 12000
                    }
                ]
            },
            "event": "minecraft:schedule_home_villager"
        },
        {
            "filters": {
                "all_of": [
                    {
                        "test": "hourly_clock_time",
                        "operator": ">=",
                        "value": 12000
                    },
                    {
                        "test": "hourly_clock_time",
                        "operator": "<",
                        "value": 24000
                    }
                ]
            },
            "event": "minecraft:schedule_bed_villager"
        }
    ]
}
```

</Spoiler>

## shareables

<Spoiler title="显示">

bogged

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:bow",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

drowned

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "items": [
        {
            "item": "minecraft:nautilus_shell",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:trident",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

evocation_illager

```json title=""
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:banner:15",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        }
    ]
}
```

fox

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "all_items": true,
    "all_items_max_amount": 1,
    "items": [
        {
            "item": "minecraft:apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:appleEnchanted",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:baked_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:beetroot_soup",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:bread",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:chorus_fruit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:clownfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_beef",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_chicken",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cooked_salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:cookie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:dried_kelp",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:fish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_apple",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:golden_carrot",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:melon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:mushroom_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonCooked",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:muttonRaw",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:poisonous_potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:porkchop",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:potato",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pufferfish",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:pumpkin_pie",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rabbit_stew",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:rotten_flesh",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:salmon",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:spider_eye",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:sweet_berries",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:glow_berries",
            "priority": 0,
            "max_amount": 1
        },
        {
            "item": "minecraft:suspicious_stew",
            "priority": 0,
            "max_amount": 1
        }
    ]
}
```

husk

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

piglin

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "items": [
        {
            "item": "minecraft:golden_sword",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_axe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_hoe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_pickaxe",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_shovel",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_rail",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_helmet",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_chestplate",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_leggings",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_boots",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_apple",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:appleEnchanted",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:golden_carrot",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_block",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_nugget",
            "priority": 2,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:raw_gold",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gold_ore",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:nether_gold_ore",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:deepslate_gold_ore",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:raw_gold_block",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:gilded_blackstone",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:horsearmorgold",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:crossbow",
            "priority": 2
        },
        {
            "item": "minecraft:porkchop",
            "consume_item": true,
            "priority": 3,
            "max_amount": 64
        },
        {
            "item": "minecraft:cooked_porkchop",
            "consume_item": true,
            "priority": 3,
            "max_amount": 64
        },
        {
            "item": "minecraft:netherite_helmet",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_helmet",
            "priority": 4
        },
        {
            "item": "minecraft:iron_helmet",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_helmet",
            "priority": 6
        },
        {
            "item": "minecraft:leather_helmet",
            "priority": 7
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:2",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:3",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:4",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:skull:5",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 8
        },
        {
            "item": "minecraft:netherite_chestplate",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_chestplate",
            "priority": 4
        },
        {
            "item": "minecraft:iron_chestplate",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "priority": 6
        },
        {
            "item": "minecraft:leather_chestplate",
            "priority": 7
        },
        {
            "item": "minecraft:elytra",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_leggings",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_leggings",
            "priority": 4
        },
        {
            "item": "minecraft:iron_leggings",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_leggings",
            "priority": 6
        },
        {
            "item": "minecraft:leather_leggings",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_boots",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_boots",
            "priority": 4
        },
        {
            "item": "minecraft:iron_boots",
            "priority": 5
        },
        {
            "item": "minecraft:chainmail_boots",
            "priority": 6
        },
        {
            "item": "minecraft:bell",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:clock",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:speckled_melon",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:light_weighted_pressure_plate",
            "priority": 2,
            "admire": true,
            "pickup_limit": 1,
            "stored_in_inventory": true
        },
        {
            "item": "minecraft:leather_boots",
            "priority": 7
        },
        {
            "item": "minecraft:netherite_sword",
            "priority": 3
        },
        {
            "item": "minecraft:diamond_sword",
            "priority": 4
        },
        {
            "item": "minecraft:iron_sword",
            "priority": 5
        },
        {
            "item": "minecraft:stone_sword",
            "priority": 6
        },
        {
            "item": "minecraft:wooden_sword",
            "priority": 7
        },
        {
            "item": "minecraft:shield",
            "priority": 7
        },
        {
            "item": "minecraft:gold_ingot",
            "priority": 1,
            "pickup_limit": 1,
            "admire": true,
            "barter": true
        }
    ]
}
```

pillager

```json title=""
"minecraft:shareables": {
    "items": [
        {
            "item": "minecraft:banner:15",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        }
    ]
}
```

skeleton

```json title=""
"minecraft:shareables": {
    "singular_pickup": true,
    "items": [
        {
            "item": "minecraft:netherite_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:stone_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:wooden_sword",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:bow",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:netherite_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:turtle_helmet",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 6
        },
        {
            "item": "minecraft:skull:0",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:skull:1",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:carved_pumpkin",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 7
        },
        {
            "item": "minecraft:netherite_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_chestplate",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_leggings",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        },
        {
            "item": "minecraft:netherite_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 0
        },
        {
            "item": "minecraft:diamond_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 1
        },
        {
            "item": "minecraft:iron_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 2
        },
        {
            "item": "minecraft:chainmail_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 3
        },
        {
            "item": "minecraft:golden_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 4
        },
        {
            "item": "minecraft:leather_boots",
            "want_amount": 1,
            "surplus_amount": 1,
            "priority": 5
        }
    ]
}
```

</Spoiler>

## shooter

<Spoiler title="显示">

blaze

```json title="#component_groups/ranged_mode"
"minecraft:shooter": {
    "def": "minecraft:small_fireball"
}
```

bogged

```json title="#component_groups/minecraft:ranged_attack"
"minecraft:shooter": {
    "def": "minecraft:arrow",
    "sound": "bow",
    "aux_val": 26
}
```

drowned

```json title="#component_groups/minecraft:ranged_mode"
"minecraft:shooter": {
    "def": "minecraft:thrown_trident",
    "sound": "item.trident.throw"
}
```

ender_dragon

```json title="#component_groups/dragon_flying"
"minecraft:shooter": {
    "type": "dragonfireball",
    "def": "minecraft:dragon_fireball"
}
```

ghast

```json title=""
"minecraft:shooter": {
    "def": "minecraft:fireball"
}
```

llama

```json title=""
"minecraft:shooter": {
    "def": "minecraft:llama_spit"
}
```

piglin

```json title="#component_groups/ranged_unit"
"minecraft:shooter": {
    "def": "minecraft:arrow"
}
```

pillager

```json title="#component_groups/minecraft:ranged_attack"
"minecraft:shooter": {
    "def": "minecraft:arrow"
}
```

</Spoiler>

## sittable

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_tame"
"minecraft:sittable": {}
```

ocelot

```json title="#component_groups/minecraft:ocelot_tame"
"minecraft:sittable": {}
```

parrot

```json title="#component_groups/minecraft:parrot_tame"
"minecraft:sittable": {}
```

wolf

```json title="#component_groups/minecraft:wolf_tame"
"minecraft:sittable": {}
```

</Spoiler>

## skin_id

<Spoiler title="显示">

villager_v2

```json title="#component_groups/villager_skin_0"
"minecraft:skin_id": {
    "value": 0
}
```

```json title="#component_groups/villager_skin_1"
"minecraft:skin_id": {
    "value": 1
}
```

```json title="#component_groups/villager_skin_2"
"minecraft:skin_id": {
    "value": 2
}
```

zombie_villager_v2

```json title="#component_groups/villager_skin_0"
"minecraft:skin_id": {
    "value": 0
}
```

```json title="#component_groups/villager_skin_1"
"minecraft:skin_id": {
    "value": 1
}
```

```json title="#component_groups/villager_skin_2"
"minecraft:skin_id": {
    "value": 2
}
```

</Spoiler>

## spawn_entity

<Spoiler title="显示">

armadillo

```json title="#component_groups/minecraft:adult"
"minecraft:spawn_entity": {
    "entities": {
        "min_wait_time": 300,
        "max_wait_time": 600,
        "spawn_sound": "mob.armadillo.scute_drop",
        "spawn_item": "armadillo_scute"
    }
}
```

chicken

```json title="#component_groups/minecraft:chicken_adult"
"minecraft:spawn_entity": {
    "entities": {
        "min_wait_time": 300,
        "max_wait_time": 600,
        "spawn_sound": "plop",
        "spawn_item": "egg",
        "filters": {
            "test": "rider_count",
            "subject": "self",
            "operator": "==",
            "value": 0
        }
    }
}
```

ocelot

```json title="#component_groups/minecraft:wild_child_ocelot_spawn"
"minecraft:spawn_entity": {
    "entities": {
        "filters": [
            {
                "test": "random_chance",
                "value": 7
            }
        ],
        "min_wait_time": 0,
        "max_wait_time": 0,
        "num_to_spawn": 2,
        "single_use": true,
        "spawn_entity": "minecraft:ocelot",
        "spawn_event": "minecraft:entity_born",
        "spawn_method": "born",
        "spawn_sound": ""
    }
}
```

sniffer

```json title="#component_groups/sniffer_pregnant"
"minecraft:spawn_entity": {
    "entities": {
        "min_wait_time": 0,
        "max_wait_time": 0,
        "spawn_sound": "plop",
        "spawn_item": "sniffer_egg",
        "spawn_item_event": {
            "event": "on_egg_spawned",
            "target": "self"
        },
        "single_use": true
    }
}
```

wandering_trader

```json title=""
"minecraft:spawn_entity": {
    "entities": [
        {
            "min_wait_time": 0,
            "max_wait_time": 0,
            "spawn_entity": "trader_llama",
            "spawn_event": "minecraft:from_wandering_trader",
            "single_use": true,
            "num_to_spawn": 2,
            "should_leash": true
        }
    ]
}
```

</Spoiler>

## spell_effects

<Spoiler title="显示">

player

```json title="#component_groups/minecraft:add_raid_omen"
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "raid_omen",
            "duration": 30,
            "display_on_screen_animation": true
        }
    ],
    "remove_effects": "bad_omen"
}
```

```json title="#component_groups/minecraft:clear_raid_omen_spell_effect"
"minecraft:spell_effects": {}
```

zombie_villager

```json title="#component_groups/to_villager"
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 100
        },
        {
            "effect": "heal",
            "duration": 100
        }
    ],
    "remove_effects": "weakness"
}
```

zombie_villager_v2

```json title="#component_groups/to_villager"
"minecraft:spell_effects": {
    "add_effects": [
        {
            "effect": "strength",
            "duration": 300
        },
        {
            "effect": "heal",
            "duration": 300
        }
    ],
    "remove_effects": "weakness"
}
```

</Spoiler>

## strength

<Spoiler title="显示">

llama

```json title="#component_groups/minecraft:strength_1"
"minecraft:strength": {
    "value": 1,
    "max": 5
}
```

```json title="#component_groups/minecraft:strength_2"
"minecraft:strength": {
    "value": 2,
    "max": 5
}
```

```json title="#component_groups/minecraft:strength_3"
"minecraft:strength": {
    "value": 3,
    "max": 5
}
```

trader_llama

```json title="#component_groups/minecraft:strength_1"
"minecraft:strength": {
    "value": 1,
    "max": 5
}
```

```json title="#component_groups/minecraft:strength_2"
"minecraft:strength": {
    "value": 2,
    "max": 5
}
```

```json title="#component_groups/minecraft:strength_3"
"minecraft:strength": {
    "value": 3,
    "max": 5
}
```

</Spoiler>

## suspect_tracking

<Spoiler title="显示">

warden

```json title=""
"minecraft:suspect_tracking": {}
```

</Spoiler>

## tameable

<Spoiler title="显示">

cat

```json title="#component_groups/minecraft:cat_wild"
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "fish",
        "salmon"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

parrot

```json title="#component_groups/minecraft:parrot_wild"
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": [
        "wheat_seeds",
        "pumpkin_seeds",
        "melon_seeds",
        "beetroot_seeds",
        "pitcher_pod",
        "torchflower_seeds"
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

wolf

```json title="#component_groups/minecraft:wolf_wild"
"minecraft:tameable": {
    "probability": 0.33,
    "tame_items": "bone",
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

</Spoiler>

## tamemount

<Spoiler title="显示">

donkey

```json title="#component_groups/minecraft:donkey_wild"
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

horse

```json title="#component_groups/minecraft:horse_wild"
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

llama

```json title="#component_groups/minecraft:llama_wild"
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 30,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "hay_block",
            "temper_mod": 6
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

mule

```json title="#component_groups/minecraft:mule_wild"
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 100,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "sugar",
            "temper_mod": 3
        },
        {
            "item": "apple",
            "temper_mod": 3
        },
        {
            "item": "golden_carrot",
            "temper_mod": 5
        },
        {
            "item": "golden_apple",
            "temper_mod": 10
        },
        {
            "item": "appleEnchanted",
            "temper_mod": 10
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

trader_llama

```json title="#component_groups/minecraft:llama_wild"
"minecraft:tamemount": {
    "min_temper": 0,
    "max_temper": 30,
    "feed_text": "action.interact.feed",
    "ride_text": "action.interact.mount",
    "feed_items": [
        {
            "item": "wheat",
            "temper_mod": 3
        },
        {
            "item": "hay_block",
            "temper_mod": 6
        }
    ],
    "auto_reject_items": [
        {
            "item": "horsearmorleather"
        },
        {
            "item": "horsearmoriron"
        },
        {
            "item": "horsearmorgold"
        },
        {
            "item": "horsearmordiamond"
        },
        {
            "item": "saddle"
        }
    ],
    "tame_event": {
        "event": "minecraft:on_tame",
        "target": "self"
    }
}
```

</Spoiler>

## target_nearby_sensor

<Spoiler title="显示">

blaze

```json title="#component_groups/mode_switcher"
"minecraft:target_nearby_sensor": {
    "inside_range": 2.0,
    "outside_range": 3.0,
    "must_see": true,
    "on_inside_range": {
        "event": "switch_to_melee",
        "target": "self"
    },
    "on_outside_range": {
        "event": "switch_to_ranged",
        "target": "self"
    }
}
```

creeper

```json title=""
"minecraft:target_nearby_sensor": {
    "inside_range": 2.5,
    "outside_range": 6.0,
    "must_see": true,
    "on_inside_range": {
        "event": "minecraft:start_exploding",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    },
    "on_vision_lost_inside_range": {
        "event": "minecraft:stop_exploding",
        "target": "self"
    }
}
```

```json title="#component_groups/minecraft:forced_exploding"
"minecraft:target_nearby_sensor": {}
```

```json title="#component_groups/minecraft:forced_charged_exploding"
"minecraft:target_nearby_sensor": {}
```

drowned

```json title="#component_groups/minecraft:mode_switcher"
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 5.0,
    "on_inside_range": {
        "event": "minecraft:switch_to_melee",
        "target": "self"
    },
    "on_outside_range": {
        "event": "minecraft:switch_to_ranged",
        "target": "self"
    }
}
```

guardian

```json title=""
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

```json title="#component_groups/minecraft:guardian_aggressive"
"minecraft:target_nearby_sensor": {
    "inside_range": 3.0,
    "outside_range": 4.0,
    "on_inside_range": {
        "event": "minecraft:target_too_close",
        "target": "self"
    }
}
```

</Spoiler>

## teleport

<Spoiler title="显示">

enderman

```json title=""
"minecraft:teleport": {
    "random_teleports": true,
    "max_random_teleport_time": 30,
    "random_teleport_cube": [
        32,
        32,
        32
    ],
    "target_distance": 16,
    "target_teleport_chance": 0.05,
    "light_teleport_chance": 0.05
}
```

</Spoiler>

## timer

<Spoiler title="显示">

allay

```json title="#component_groups/pickup_item_delay"
"minecraft:timer": {
    "looping": false,
    "time": 3,
    "time_down_event": {
        "event": "pickup_item_delay_complete"
    }
}
```

armadillo

```json title="#component_groups/minecraft:rolled_up_without_threats"
"minecraft:timer": {
    "looping": true,
    "time": 4,
    "randomInterval": false,
    "time_down_event": {
        "event": "minecraft:unroll"
    }
}
```

bee

```json title="#component_groups/escape_fire"
"minecraft:timer": {
    "looping": false,
    "time": [
        20,
        50
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "stop_panicking_after_fire",
        "target": "self"
    }
}
```

```json title="#component_groups/countdown_to_perish"
"minecraft:timer": {
    "looping": false,
    "time": [
        10,
        60
    ],
    "randomInterval": true,
    "time_down_event": {
        "event": "perish_event",
        "target": "self"
    }
}
```

```json title="#component_groups/take_nearest_target"
"minecraft:timer": {
    "looping": true,
    "time": 5,
    "time_down_event": {
        "event": "calmed_down",
        "target": "self"
    }
}
```

boat

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:timer": {
    "looping": false,
    "time": 3,
    "time_down_event": {
        "event": "minecraft:sink",
        "target": "self"
    }
}
```

chest_boat

```json title="#component_groups/minecraft:above_bubble_column_down"
"minecraft:timer": {
    "looping": false,
    "time": 3,
    "time_down_event": {
        "event": "minecraft:sink",
        "target": "self"
    }
}
```

guardian

```json title="#component_groups/minecraft:guardian_passive"
"minecraft:timer": {
    "time": [
        1,
        3
    ],
    "looping": false,
    "time_down_event": {
        "event": "minecraft:target_far_enough",
        "target": "self"
    }
}
```

</Spoiler>

## trade_resupply

<Spoiler title="显示">

villager_v2

```json title="#component_groups/trade_resupply_component_group"
"minecraft:trade_resupply": {}
```

</Spoiler>

## trade_table

<Spoiler title="显示">

villager

```json title="#component_groups/farmer"
"minecraft:trade_table": {
    "display_name": "entity.villager.farmer",
    "table": "trading/farmer_trades.json",
    "convert_trades_economy": true
}
```

```json title="#component_groups/fisherman"
"minecraft:trade_table": {
    "display_name": "entity.villager.fisherman",
    "table": "trading/fisherman_trades.json",
    "convert_trades_economy": true
}
```

```json title="#component_groups/shepherd"
"minecraft:trade_table": {
    "display_name": "entity.villager.shepherd",
    "table": "trading/shepherd_trades.json",
    "convert_trades_economy": true
}
```

</Spoiler>

## trail

<Spoiler title="显示">

snow_golem

```json title=""
"minecraft:trail": {
    "block_type": "minecraft:snow_layer",
    "spawn_filter": {
        "test": "is_temperature_value",
        "operator": "<",
        "value": 0.81
    }
}
```

</Spoiler>

## transformation

<Spoiler title="显示">

hoglin

```json title="#component_groups/become_zombie"
"minecraft:transformation": {
    "into": "minecraft:zoglin",
    "transformation_sound": "mob.hoglin.converted_to_zombified",
    "keep_level": true
}
```

husk

```json title="#component_groups/minecraft:convert_to_zombie"
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_adult>",
    "transformation_sound": "mob.husk.convert_to_zombie",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

```json title="#component_groups/minecraft:convert_to_baby_zombie"
"minecraft:transformation": {
    "into": "minecraft:zombie<minecraft:as_baby>",
    "transformation_sound": "mob.husk.convert_to_zombie",
    "drop_equipment": true,
    "delay": {
        "value": 15
    }
}
```

mooshroom

```json title="#component_groups/minecraft:mooshroom_become_cow"
"minecraft:transformation": {
    "into": "minecraft:cow"
}
```

pig

```json title="#component_groups/minecraft:pig_transform"
"minecraft:transformation": {
    "into": "minecraft:pig_zombie",
    "transformation_sound": "mob.pig.death",
    "delay": 0.5
}
```

piglin

```json title="#component_groups/become_zombie"
"minecraft:transformation": {
    "into": "minecraft:zombie_pigman",
    "transformation_sound": "converted_to_zombified",
    "keep_level": true,
    "drop_inventory": true,
    "preserve_equipment": true
}
```

piglin_brute

```json title="#component_groups/become_zombie"
"minecraft:transformation": {
    "into": "minecraft:zombie_pigman",
    "transformation_sound": "converted_to_zombified",
    "keep_level": true,
    "preserve_equipment": true
}
```

skeleton

```json title="#component_groups/become_stray"
"minecraft:transformation": {
    "into": "minecraft:stray",
    "transformation_sound": "convert_to_stray",
    "keep_level": true,
    "drop_inventory": true,
    "preserve_equipment": true
}
```

</Spoiler>

## trust

<Spoiler title="显示">

fox

```json title="#component_groups/minecraft:trusting_fox"
"minecraft:trust": {}
```

</Spoiler>

## trusting

<Spoiler title="显示">

ocelot

```json title="#component_groups/minecraft:ocelot_wild"
"minecraft:trusting": {
    "probability": 0.33,
    "trust_items": [
        "fish",
        "salmon"
    ],
    "trust_event": {
        "event": "minecraft:on_trust",
        "target": "self"
    }
}
```

</Spoiler>

## type_family

<Spoiler title="显示">

allay

```json title=""
"minecraft:type_family": {
    "family": [
        "allay",
        "mob"
    ]
}
```

armadillo

```json title=""
"minecraft:type_family": {
    "family": [
        "armadillo",
        "mob"
    ]
}
```

armor_stand

```json title=""
"minecraft:type_family": {
    "family": [
        "armor_stand",
        "inanimate",
        "mob"
    ]
}
```

axolotl

```json title=""
"minecraft:type_family": {
    "family": [
        "axolotl",
        "mob"
    ]
}
```

bat

```json title=""
"minecraft:type_family": {
    "family": [
        "bat",
        "mob"
    ]
}
```

bee

```json title=""
"minecraft:type_family": {
    "family": [
        "bee",
        "mob",
        "arthropod"
    ]
}
```

```json title="#component_groups/countdown_to_perish"
"minecraft:type_family": {
    "family": [
        "bee",
        "mob",
        "arthropod",
        "pacified"
    ]
}
```

blaze

```json title=""
"minecraft:type_family": {
    "family": [
        "blaze",
        "monster",
        "mob"
    ]
}
```

</Spoiler>

## underwater_movement

<Spoiler title="显示">

axolotl

```json title=""
"minecraft:underwater_movement": {
    "value": 0.2
}
```

dolphin

```json title=""
"minecraft:underwater_movement": {
    "value": 0.15
}
```

drowned

```json title=""
"minecraft:underwater_movement": {
    "value": 0.06
}
```

```json title="#component_groups/minecraft:baby_drowned"
"minecraft:underwater_movement": {
    "value": 0.08
}
```

elder_guardian

```json title=""
"minecraft:underwater_movement": {
    "value": 0.3
}
```

cod

```json title=""
"minecraft:underwater_movement": {
    "value": 0.1
}
```

frog

```json title=""
"minecraft:underwater_movement": {
    "value": 0.15
}
```

guardian

```json title=""
"minecraft:underwater_movement": {
    "value": 0.12
}
```

</Spoiler>

## variable_max_auto_step

<Spoiler title="显示">

camel

```json title=""
"minecraft:variable_max_auto_step": {
    "base_value": 1.5625,
    "controlled_value": 1.5625,
    "jump_prevented_value": 0.5625
}
```

enderman

```json title=""
"minecraft:variable_max_auto_step": {
    "base_value": 1.0625,
    "jump_prevented_value": 0.5625
}
```

</Spoiler>

## variant

<Spoiler title="显示">

axolotl

```json title="#component_groups/axolotl_lucy"
"minecraft:variant": {
    "value": 0
}
```

```json title="#component_groups/axolotl_cyan"
"minecraft:variant": {
    "value": 1
}
```

```json title="#component_groups/axolotl_gold"
"minecraft:variant": {
    "value": 2
}
```

cat

```json title="#component_groups/minecraft:cat_white"
"minecraft:variant": {
    "value": 0
}
```

```json title="#component_groups/minecraft:cat_tuxedo"
"minecraft:variant": {
    "value": 1
}
```

```json title="#component_groups/minecraft:cat_red"
"minecraft:variant": {
    "value": 2
}
```

fox

```json title="#component_groups/minecraft:fox_red"
"minecraft:variant": {
    "value": 0
}
```

```json title="#component_groups/minecraft:fox_arctic"
"minecraft:variant": {
    "value": 1
}
```

</Spoiler>

## vibration_damper

<Spoiler title="显示">

warden

```json title=""
"minecraft:vibration_damper": {}
```

</Spoiler>

## vibration_listener

<Spoiler title="显示">

allay

```json title=""
"minecraft:vibration_listener": {}
```

warden

```json title=""
"minecraft:vibration_listener": {}
```

</Spoiler>

## water_movement

<Spoiler title="显示">

panda

```json title=""
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

polar_bear

```json title=""
"minecraft:water_movement": {
    "drag_factor": 0.98
}
```

turtle

```json title=""
"minecraft:water_movement": {
    "drag_factor": 0.9
}
```

</Spoiler>

## wind_burst

<Spoiler title="显示">

breeze_wind_charge_projectile

```json title=""
"minecraft:wind_burst": {
    "radius": 3.0,
    "particle_effect": "breeze_wind_burst",
    "sound_effect": "breeze_wind_charge.burst",
    "knockback_scaling": 1.0,
    "negates_fall_damage": false
}
```

wind_charge_projectile

```json title=""
"minecraft:wind_burst": {
    "radius": 1.2,
    "particle_effect": "wind_burst",
    "sound_effect": "wind_charge.burst",
    "knockback_scaling": 1.1
}
```

</Spoiler>

