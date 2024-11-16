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

<CodeHeader></CodeHeader>

```json
"minecraft:block": "minecraft:camera"
```

</Spoiler>

## camera

<Spoiler title="显示">

camera

<CodeHeader></CodeHeader>

```json
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

<CodeHeader></CodeHeader>

```json
"minecraft:cooldown": {
    "category": "wind_charge",
    "duration": 0.5
}
```

</Spoiler>

## display_name

<Spoiler title="显示">

apple

<CodeHeader></CodeHeader>

```json
"minecraft:display_name": {
    "value": "item.apple.name"
}
```

breeze_rod

<CodeHeader></CodeHeader>

```json
"minecraft:display_name": {
    "value": "item.breeze_rod.name"
}
```

ominous_trial_key

<CodeHeader></CodeHeader>

```json
"minecraft:display_name": {
    "value": "item.ominous_trial_key.name"
}
```

trial_key

<CodeHeader></CodeHeader>

```json
"minecraft:display_name": {
    "value": "item.trial_key.name"
}
```

wind_charge

<CodeHeader></CodeHeader>

```json
"minecraft:display_name": {
    "value": "item.wind_charge.name"
}
```

</Spoiler>

## foil

<Spoiler title="显示">

appleEnchanted

<CodeHeader></CodeHeader>

```json
"minecraft:foil": true
```

golden_apple

<CodeHeader></CodeHeader>

```json
"minecraft:foil": false
```

</Spoiler>

## food

<Spoiler title="显示">

apple

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": 0.3
}
```

appleEnchanted

<CodeHeader></CodeHeader>

```json
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

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

beef

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

beetroot

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "normal"
}
```

beetroot_soup

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

bread

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

carrot

<CodeHeader></CodeHeader>

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "normal"
}
```

</Spoiler>

## hand_equipped

<Spoiler title="显示">

appleEnchanted

<CodeHeader></CodeHeader>

```json
"minecraft:hand_equipped": false
```

</Spoiler>

## icon

<Spoiler title="显示">

apple

<CodeHeader></CodeHeader>

```json
"minecraft:icon": {
    "texture": "apple"
}
```

breeze_rod

<CodeHeader></CodeHeader>

```json
"minecraft:icon": {
    "texture": "breeze_rod"
}
```

ominous_trial_key

<CodeHeader></CodeHeader>

```json
"minecraft:icon": {
    "texture": "ominous_trial_key"
}
```

trial_key

<CodeHeader></CodeHeader>

```json
"minecraft:icon": {
    "texture": "trial_key"
}
```

wind_charge

<CodeHeader></CodeHeader>

```json
"minecraft:icon": {
    "texture": "wind_charge"
}
```

</Spoiler>

## max_damage

<Spoiler title="显示">

clownfish

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

cooked_fish

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

cooked_salmon

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

fish

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

pufferfish

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

salmon

<CodeHeader></CodeHeader>

```json
"minecraft:max_damage": 0
```

</Spoiler>

## max_stack_size

<Spoiler title="显示">

beetroot_soup

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

honey_bottle

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 16
```

mushroom_stew

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

rabbit_stew

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

suspicious_stew

<CodeHeader></CodeHeader>

```json
"minecraft:max_stack_size": 1
```

</Spoiler>

## projectile

<Spoiler title="显示">

wind_charge

<CodeHeader></CodeHeader>

```json
"minecraft:projectile": {
    "projectile_entity": "wind_charge_projectile"
}
```

</Spoiler>

## seed

<Spoiler title="显示">

beetroot_seeds

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "beetroot"
}
```

carrot

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "carrots"
}
```

glow_berries

<CodeHeader></CodeHeader>

```json
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

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "melon_stem"
}
```

nether_wart

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "plant_at": "soul_sand",
    "crop_result": "nether_wart"
}
```

pitcher_pod

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "pitcher_crop"
}
```

potato

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "potatoes"
}
```

pumpkin_seeds

<CodeHeader></CodeHeader>

```json
"minecraft:seed": {
    "crop_result": "pumpkin_stem"
}
```

</Spoiler>

## stacked_by_data

<Spoiler title="显示">

appleEnchanted

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

clownfish

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

cooked_fish

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

cooked_salmon

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

fish

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

golden_apple

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

pufferfish

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

salmon

<CodeHeader></CodeHeader>

```json
"minecraft:stacked_by_data": true
```

</Spoiler>

## tags

<Spoiler title="显示">

apple

<CodeHeader></CodeHeader>

```json
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

<CodeHeader></CodeHeader>

```json
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

<CodeHeader></CodeHeader>

```json
"minecraft:use_animation": "eat"
```

</Spoiler>

## use_duration

<Spoiler title="显示">

appleEnchanted

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

baked_potato

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

beef

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

beetroot

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

beetroot_soup

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

bread

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

camera

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 100000
```

carrot

<CodeHeader></CodeHeader>

```json
"minecraft:use_duration": 32
```

</Spoiler>

## use_modifiers

<Spoiler title="显示">

apple

<CodeHeader></CodeHeader>

```json
"minecraft:use_modifiers": {
    "use_duration": 1.6,
    "movement_modifier": 0.35
}
```

</Spoiler>