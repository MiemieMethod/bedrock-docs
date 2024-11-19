---
title: 原版使用组件
category: 文档
mentions:
    - MedicalJewel105
description: 自动生成的原版物品组件列表。
---

此页面由[Wiki内容生成器](https://github.com/Bedrock-OSS/bedrock-wiki-content-generator)创建。如有问题，请在[Bedrock OSS](https://discord.gg/XjV87YN) Discord服务器上联系我们。
请注意，每个组件最多显示8个示例，以保持页面加载速度。命名空间`minecraft`也已移除。
如果你想查看完整页面，可以[点击这里](/items/vui-full)。_最后更新于1.21.0_

## block

<Spoiler title="显示">

camera

```json title=""
"minecraft:block": "minecraft:camera"
```

</Spoiler>

## camera

<Spoiler title="显示">

camera

```json title=""
"minecraft:camera": {
    "black_bars_duration": 0.2,
    "black_bars_screen_ratio": 0.08,
    "shutter_duration": 0.2,
    "picture_duration": 1.0,
    "slide_away_duration": 0.2
}
```

</Spoiler>

## cooldown

<Spoiler title="显示">

wind_charge

```json title=""
"minecraft:cooldown": {
    "category": "wind_charge",
    "duration": 0.5
}
```

</Spoiler>

## display_name

<Spoiler title="显示">

apple

```json title=""
"minecraft:display_name": {
    "value": "item.apple.name"
}
```

breeze_rod

```json title=""
"minecraft:display_name": {
    "value": "item.breeze_rod.name"
}
```

ominous_trial_key

```json title=""
"minecraft:display_name": {
    "value": "item.ominous_trial_key.name"
}
```

trial_key

```json title=""
"minecraft:display_name": {
    "value": "item.trial_key.name"
}
```

wind_charge

```json title=""
"minecraft:display_name": {
    "value": "item.wind_charge.name"
}
```

</Spoiler>

## foil

<Spoiler title="显示">

appleEnchanted

```json title=""
"minecraft:foil": true
```

golden_apple

```json title=""
"minecraft:foil": false
```

</Spoiler>

## food

<Spoiler title="显示">

apple

```json title=""
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": 0.3
}
```

appleEnchanted

```json title=""
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "supernatural",
    "can_always_eat": true,
    "effects": [
        {
            "name": "regeneration",
            "chance": 1.0,
            "duration": 30,
            "amplifier": 4
        },
        {
            "name": "absorption",
            "chance": 1.0,
            "duration": 120,
            "amplifier": 3
        },
        {
            "name": "resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        },
        {
            "name": "fire_resistance",
            "chance": 1.0,
            "duration": 300,
            "amplifier": 0
        }
    ]
}
```

baked_potato

```json title=""
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

beef

```json title=""
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

beetroot

```json title=""
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "normal"
}
```

beetroot_soup

```json title=""
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

bread

```json title=""
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

carrot

```json title=""
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "normal"
}
```

</Spoiler>

## hand_equipped

<Spoiler title="显示">

appleEnchanted

```json title=""
"minecraft:hand_equipped": false
```

</Spoiler>

## icon

<Spoiler title="显示">

apple

```json title=""
"minecraft:icon": {
    "texture": "apple"
}
```

breeze_rod

```json title=""
"minecraft:icon": {
    "texture": "breeze_rod"
}
```

ominous_trial_key

```json title=""
"minecraft:icon": {
    "texture": "ominous_trial_key"
}
```

trial_key

```json title=""
"minecraft:icon": {
    "texture": "trial_key"
}
```

wind_charge

```json title=""
"minecraft:icon": {
    "texture": "wind_charge"
}
```

</Spoiler>

## max_damage

<Spoiler title="显示">

clownfish

```json title=""
"minecraft:max_damage": 0
```

cooked_fish

```json title=""
"minecraft:max_damage": 0
```

cooked_salmon

```json title=""
"minecraft:max_damage": 0
```

fish

```json title=""
"minecraft:max_damage": 0
```

pufferfish

```json title=""
"minecraft:max_damage": 0
```

salmon

```json title=""
"minecraft:max_damage": 0
```

</Spoiler>

## max_stack_size

<Spoiler title="显示">

beetroot_soup

```json title=""
"minecraft:max_stack_size": 1
```

honey_bottle

```json title=""
"minecraft:max_stack_size": 16
```

mushroom_stew

```json title=""
"minecraft:max_stack_size": 1
```

rabbit_stew

```json title=""
"minecraft:max_stack_size": 1
```

suspicious_stew

```json title=""
"minecraft:max_stack_size": 1
```

</Spoiler>

## projectile

<Spoiler title="显示">

wind_charge

```json title=""
"minecraft:projectile": {
    "projectile_entity": "wind_charge_projectile"
}
```

</Spoiler>

## seed

<Spoiler title="显示">

beetroot_seeds

```json title=""
"minecraft:seed": {
    "crop_result": "beetroot"
}
```

carrot

```json title=""
"minecraft:seed": {
    "crop_result": "carrots"
}
```

glow_berries

```json title=""
"minecraft:seed": {
    "crop_result": "cave_vines",
    "plant_at": [
        "cave_vines",
        "cave_vines_head_with_berries"
    ],
    "plant_at_any_solid_surface": true,
    "plant_at_face": "DOWN"
}
```

melon_seeds

```json title=""
"minecraft:seed": {
    "crop_result": "melon_stem"
}
```

nether_wart

```json title=""
"minecraft:seed": {
    "plant_at": "soul_sand",
    "crop_result": "nether_wart"
}
```

pitcher_pod

```json title=""
"minecraft:seed": {
    "crop_result": "pitcher_crop"
}
```

potato

```json title=""
"minecraft:seed": {
    "crop_result": "potatoes"
}
```

pumpkin_seeds

```json title=""
"minecraft:seed": {
    "crop_result": "pumpkin_stem"
}
```

</Spoiler>

## stacked_by_data

<Spoiler title="显示">

appleEnchanted

```json title=""
"minecraft:stacked_by_data": true
```

clownfish

```json title=""
"minecraft:stacked_by_data": true
```

cooked_fish

```json title=""
"minecraft:stacked_by_data": true
```

cooked_salmon

```json title=""
"minecraft:stacked_by_data": true
```

fish

```json title=""
"minecraft:stacked_by_data": true
```

golden_apple

```json title=""
"minecraft:stacked_by_data": true
```

pufferfish

```json title=""
"minecraft:stacked_by_data": true
```

salmon

```json title=""
"minecraft:stacked_by_data": true
```

</Spoiler>

## tags

<Spoiler title="显示">

apple

```json title=""
"minecraft:tags": {
    "tags": [
        "minecraft:is_food"
    ]
}
```

</Spoiler>

## throwable

<Spoiler title="显示">

wind_charge

```json title=""
"minecraft:throwable": {
    "do_swing_animation": true,
    "launch_power_scale": 1.5,
    "max_launch_power": 1.5,
    "default_offset_scale": 0.8,
    "inside_block_offset_scale": 0.05
}
```

</Spoiler>

## use_animation

<Spoiler title="显示">

apple

```json title=""
"minecraft:use_animation": "eat"
```

</Spoiler>

## use_duration

<Spoiler title="显示">

appleEnchanted

```json title=""
"minecraft:use_duration": 32
```

baked_potato

```json title=""
"minecraft:use_duration": 32
```

beef

```json title=""
"minecraft:use_duration": 32
```

beetroot

```json title=""
"minecraft:use_duration": 32
```

beetroot_soup

```json title=""
"minecraft:use_duration": 32
```

bread

```json title=""
"minecraft:use_duration": 32
```

camera

```json title=""
"minecraft:use_duration": 100000
```

carrot

```json title=""
"minecraft:use_duration": 32
```

</Spoiler>

## use_modifiers

<Spoiler title="显示">

apple

```json title=""
"minecraft:use_modifiers": {
    "use_duration": 1.6,
    "movement_modifier": 0.35
}
```

</Spoiler>