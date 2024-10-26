---
title: 原版使用组件 - 完整版
category: 文档
mentions:
    - MedicalJewel105
description: 自动生成的原版物品组件列表。
hidden: true
---

此页面是使用 [Wiki 内容生成器](https://github.com/Bedrock-OSS/bedrock-wiki-content-generator) 创建的。如有问题，请在 [Bedrock OSS](https://discord.gg/XjV87YN) Discord 服务器上联系我们。
包含所有示例。已移除命名空间 `minecraft` 和一些格式，以加快页面加载速度。_最后更新于 1.21.0_

## 区块

相机

```json
"minecraft:block": "minecraft:camera"
```

## 相机

相机

```json
"minecraft:camera": {
    "black_bars_duration": 0.2,
    "black_bars_screen_ratio": 0.08,
    "shutter_duration": 0.2,
    "picture_duration": 1.0,
    "slide_away_duration": 0.2
}
```

## 冷却时间

风能充能

```json
"minecraft:cooldown": {
    "category": "wind_charge",
    "duration": 0.5
}
```

## 显示名称

苹果

```json
"minecraft:display_name": {
    "value": "item.apple.name"
}
```

微风杖

```json
"minecraft:display_name": {
    "value": "item.breeze_rod.name"
}
```

不祥试炼钥匙

```json
"minecraft:display_name": {
    "value": "item.ominous_trial_key.name"
}
```

试炼钥匙

```json
"minecraft:display_name": {
    "value": "item.trial_key.name"
}
```

风能充能

```json
"minecraft:display_name": {
    "value": "item.wind_charge.name"
}
```

## 镀膜

附魔苹果

```json
"minecraft:foil": true
```

金苹果

```json
"minecraft:foil": false
```

## 食物

苹果

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": 0.3
}
```

附魔苹果

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

烤土豆

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

牛肉

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

甜菜根

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "normal"
}
```

甜菜根汤

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

面包

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

胡萝卜

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "normal"
}
```

鸡肉

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low",
    "effects": [
        {
            "name": "hunger",
            "chance": 0.3,
            "duration": 30,
            "amplifier": 0
        }
    ]
}
```

合唱果

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "low",
    "on_use_action": "chorus_teleport",
    "on_use_range": [
        8,
        8,
        8
    ],
    "cooldown_type": "chorusfruit",
    "cooldown_time": 20,
    "can_always_eat": true
}
```

小丑鱼

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "poor"
}
```

熟牛肉

```json
"minecraft:food": {
    "nutrition": 8,
    "saturation_modifier": "good"
}
```

熟鸡肉

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal"
}
```

熟鱼

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

熟猪排

```json
"minecraft:food": {
    "nutrition": 8,
    "saturation_modifier": "good"
}
```

熟兔肉

```json
"minecraft:food": {
    "nutrition": 5,
    "saturation_modifier": "normal"
}
```

熟三文鱼

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "good"
}
```

饼干

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

干海带

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "poor"
}
```

鱼

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

荧光浆果

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low",
    "is_meat": false
}
```

金苹果

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "supernatural",
    "can_always_eat": true,
    "effects": [
        {
            "name": "regeneration",
            "chance": 1.0,
            "duration": 5,
            "amplifier": 1
        },
        {
            "name": "absorption",
            "chance": 1.0,
            "duration": 120,
            "amplifier": 0
        }
    ]
}
```

金胡萝卜

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "supernatural"
}
```

蜂蜜瓶

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "poor",
    "can_always_eat": true,
    "using_converts_to": "glass_bottle",
    "remove_effects": [
        "poison"
    ]
}
```

西瓜

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low"
}
```

蘑菇汤

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

熟羊肉

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "good"
}
```

生羊肉

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low"
}
```

有毒土豆

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low",
    "effects": [
        {
            "name": "poison",
            "chance": 0.6,
            "duration": 5,
            "amplifier": 0
        }
    ]
}
```

猪排

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

土豆

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "low"
}
```

河豚

```json
"minecraft:food": {
    "nutrition": 1,
    "saturation_modifier": "poor",
    "effects": [
        {
            "name": "poison",
            "duration": 60,
            "amplifier": 1
        },
        {
            "name": "nausea",
            "duration": 15,
            "amplifier": 1
        },
        {
            "name": "hunger",
            "duration": 15,
            "amplifier": 2
        }
    ]
}
```

南瓜派

```json
"minecraft:food": {
    "nutrition": 8,
    "saturation_modifier": "low"
}
```

兔肉

```json
"minecraft:food": {
    "nutrition": 3,
    "saturation_modifier": "low"
}
```

兔肉汤

```json
"minecraft:food": {
    "nutrition": 10,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl"
}
```

腐肉

```json
"minecraft:food": {
    "nutrition": 4,
    "saturation_modifier": "poor",
    "effects": [
        {
            "name": "hunger",
            "chance": 0.8,
            "duration": 30,
            "amplifier": 0
        }
    ]
}
```

三文鱼

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "poor"
}
```

蜘蛛眼

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "good",
    "effects": [
        {
            "name": "poison",
            "chance": 1.0,
            "duration": 5,
            "amplifier": 0
        }
    ]
}
```

可疑汤

```json
"minecraft:food": {
    "nutrition": 6,
    "saturation_modifier": "normal",
    "using_converts_to": "bowl",
    "on_use_action": "suspicious_stew_effect",
    "can_always_eat": true
}
```

甜浆果

```json
"minecraft:food": {
    "nutrition": 2,
    "saturation_modifier": "low",
    "is_meat": false
}
```

## 手持装备

附魔苹果

```json
"minecraft:hand_equipped": false
```

## 图标

苹果

```json
"minecraft:icon": {
    "texture": "apple"
}
```

微风杖

```json
"minecraft:icon": {
    "texture": "breeze_rod"
}
```

不祥试炼钥匙

```json
"minecraft:icon": {
    "texture": "ominous_trial_key"
}
```

试炼钥匙

```json
"minecraft:icon": {
    "texture": "trial_key"
}
```

风能充能

```json
"minecraft:icon": {
    "texture": "wind_charge"
}
```

## 最大耐久

小丑鱼

```json
"minecraft:max_damage": 0
```

熟鱼

```json
"minecraft:max_damage": 0
```

熟三文鱼

```json
"minecraft:max_damage": 0
```

鱼

```json
"minecraft:max_damage": 0
```

河豚

```json
"minecraft:max_damage": 0
```

三文鱼

```json
"minecraft:max_damage": 0
```

## 最大堆叠数量

甜菜根汤

```json
"minecraft:max_stack_size": 1
```

蜂蜜瓶

```json
"minecraft:max_stack_size": 16
```

蘑菇汤

```json
"minecraft:max_stack_size": 1
```

兔肉汤

```json
"minecraft:max_stack_size": 1
```

可疑汤

```json
"minecraft:max_stack_size": 1
```

## 投射物

风能充能

```json
"minecraft:projectile": {
    "projectile_entity": "wind_charge_projectile"
}
```

## 种子

甜菜种子

```json
"minecraft:seed": {
    "crop_result": "beetroot"
}
```

胡萝卜

```json
"minecraft:seed": {
    "crop_result": "carrots"
}
```

荧光浆果

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

西瓜种子

```json
"minecraft:seed": {
    "crop_result": "melon_stem"
}
```

下界疣

```json
"minecraft:seed": {
    "plant_at": "soul_sand",
    "crop_result": "nether_wart"
}
```

瓶子草种子

```json
"minecraft:seed": {
    "crop_result": "pitcher_crop"
}
```

土豆

```json
"minecraft:seed": {
    "crop_result": "potatoes"
}
```

南瓜种子

```json
"minecraft:seed": {
    "crop_result": "pumpkin_stem"
}
```

甜浆果

```json
"minecraft:seed": {
    "crop_result": "sweet_berry_bush",
    "plant_at": [
        "farmland",
        "grass",
        "dirt",
        "podzol",
        "moss_block",
        "mycelium",
        "mud",
        "muddy_mangrove_roots",
        "dirt_with_roots"
    ]
}
```

火把花种子

```json
"minecraft:seed": {
    "crop_result": "torchflower_crop"
}
```

小麦种子

```json
"minecraft:seed": {
    "crop_result": "wheat"
}
```

## 按数据堆叠

附魔苹果

```json
"minecraft:stacked_by_data": true
```

小丑鱼

```json
"minecraft:stacked_by_data": true
```

熟鱼

```json
"minecraft:stacked_by_data": true
```

熟三文鱼

```json
"minecraft:stacked_by_data": true
```

鱼

```json
"minecraft:stacked_by_data": true
```

金苹果

```json
"minecraft:stacked_by_data": true
```

河豚

```json
"minecraft:stacked_by_data": true
```

三文鱼

```json
"minecraft:stacked_by_data": true
```

## 标签

苹果

```json
"minecraft:tags": {
    "tags": [
        "minecraft:is_food"
    ]
}
```

## 可投掷

风能充能

```json
"minecraft:throwable": {
    "do_swing_animation": true,
    "launch_power_scale": 1.5,
    "max_launch_power": 1.5,
    "default_offset_scale": 0.8,
    "inside_block_offset_scale": 0.05
}
```

## 使用动画

苹果

```json
"minecraft:use_animation": "eat"
```

## 使用持续时间

附魔苹果

```json
"minecraft:use_duration": 32
```

烤土豆

```json
"minecraft:use_duration": 32
```

牛肉

```json
"minecraft:use_duration": 32
```

甜菜根

```json
"minecraft:use_duration": 32
```

甜菜根汤

```json
"minecraft:use_duration": 32
```

面包

```json
"minecraft:use_duration": 32
```

相机

```json
"minecraft:use_duration": 100000
```

胡萝卜

```json
"minecraft:use_duration": 32
```

鸡肉

```json
"minecraft:use_duration": 32
```

合唱果

```json
"minecraft:use_duration": 32
```

小丑鱼

```json
"minecraft:use_duration": 32
```

熟牛肉

```json
"minecraft:use_duration": 32
```

熟鸡肉

```json
"minecraft:use_duration": 32
```

熟鱼

```json
"minecraft:use_duration": 32
```

熟猪排

```json
"minecraft:use_duration": 32
```

熟兔肉

```json
"minecraft:use_duration": 32
```

熟三文鱼

```json
"minecraft:use_duration": 32
```

饼干

```json
"minecraft:use_duration": 32
```

干海带

```json
"minecraft:use_duration": 16
```

鱼

```json
"minecraft:use_duration": 32
```

荧光浆果

```json
"minecraft:use_duration": 32
```

金苹果

```json
"minecraft:use_duration": 32
```

金胡萝卜

```json
"minecraft:use_duration": 32
```

蜂蜜瓶

```json
"minecraft:use_duration": 40
```

西瓜

```json
"minecraft:use_duration": 32
```

蘑菇汤

```json
"minecraft:use_duration": 32
```

熟羊肉

```json
"minecraft:use_duration": 32
```

生羊肉

```json
"minecraft:use_duration": 32
```

有毒土豆

```json
"minecraft:use_duration": 32
```

猪排

```json
"minecraft:use_duration": 32
```

土豆

```json
"minecraft:use_duration": 32
```

河豚

```json
"minecraft:use_duration": 32
```

南瓜派

```json
"minecraft:use_duration": 32
```

兔肉

```json
"minecraft:use_duration": 32
```

兔肉汤

```json
"minecraft:use_duration": 32
```

腐肉

```json
"minecraft:use_duration": 32
```

三文鱼

```json
"minecraft:use_duration": 32
```

蜘蛛眼

```json
"minecraft:use_duration": 32
```

可疑汤

```json
"minecraft:use_duration": 32
```

甜浆果

```json
"minecraft:use_duration": 32
```

## 使用修饰符

苹果

```json
"minecraft:use_modifiers": {
    "use_duration": 1.6,
    "movement_modifier": 0.35
}
```