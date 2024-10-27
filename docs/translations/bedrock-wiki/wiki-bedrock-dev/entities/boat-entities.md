---
title: 创建船只
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - Joelant05
    - MedicalJewel105
    - StealthyExpertX
    - TheItsNameless
description: 学习如何制作船只行为。
---
:::warning 需要格式版本 1.16.100 或更低

行为格式版本现在要求 `minecraft:behavior.rise_to_liquid_level` 和 `minecraft:buoyant` 方法在 1.16.100 或更低版本中才能正常工作。
如果你发现了在更新格式版本中有效的新方法，欢迎你通过更新维基来贡献你的力量。
:::

## 使用运行时标识符

你可以在[这里](../entities/runtime-identifier.md)了解更多关于运行时标识符的信息。使用运行时标识符，你可以实现大多数船只的硬编码行为。然而，你的船只不会随你旋转，并且始终面朝北方。

## 使用组件

目前，创建船只实体的最佳方法是使用组件。1.16 引入了新的组件，我们可以利用它们：`minecraft:behavior.rise_to_liquid_level` 和 `minecraft:buoyant`。在原版中，Strider 使用第一个组件使其在熔岩上漂浮，但我们也可以将其重新用于水中。

## 第一种方法：minecraft:behavior.rise_to_liquid_level

<CodeHeader>BP/entities/bar</CodeHeader>

```json
{
	"minecraft:entity": {
		"format_version": "1.14.0",
		"description": {
			"identifier": "wiki:boat",
			"is_summonable": true,
			"is_spawnable": true,
			"is_experimental": false
		},
		"components": {
			//这个组件实现了魔法
			"minecraft:behavior.rise_to_liquid_level": {
				"priority": 0,
				//此属性可以调整船只在水面上的高度
				"liquid_y_offset": 0.5,
				//正的垂直位移，换句话说，船只将上升的高度
				"rise_delta": 0.05,
				//负的垂直位移，换句话说，船只将下降的高度
				"sink_delta": 0.05
				//使用 rise_delta 和 sink_delta 模拟波浪/弹跳效果
			},

			//设置船只在水中的速度
			"minecraft:underwater_movement": {
				"value": 5
			},
			//这个组件很重要，缺少它船只会下沉
			"minecraft:navigation.walk": {
				"can_sink": false
			},
			"minecraft:rideable": {
				"seat_count": 1,
				"family_types": ["player"],
				"interact_text": "action.interact.enter_boat",
				"seats": {
					"position": [0, 0, 0]
				}
			},
			//如果你想用 WASD 控制船只，请添加此组件
			"minecraft:input_ground_controlled": {},
			"minecraft:health": {
				"value": 10,
				"max": 10
			},
			//设置船只在地面的速度（如果不想让船只在地面移动，请将其设置为零）
			"minecraft:movement": {
				"value": 3
			},
			//这是为了防止玩家退出时船只不停下
			"minecraft:movement.basic": {},
			"minecraft:collision_box": {
				"width": 1,
				"height": 1
			},
			"minecraft:physics": {}
		}
	}
}
```

## 第二种方法：minecraft:buoyant

<CodeHeader></CodeHeader>

```json
{
	"minecraft:entity": {
		"format_version": "1.14.0",
		"description": {
			"identifier": "wiki:boat",
			"is_summonable": true,
			"is_spawnable": true,
			"is_experimental": false
		},
		"components": {
			"minecraft:buoyant": {
				//决定是否考虑重力（在瀑布中很有用）
				"apply_gravity": true,
				//范围：0-1。控制船只在水面上的高度
				"base_buoyancy": 1.0,
				//“波浪”使实体上下弹跳。大波浪会放大这个效果。注意：将 simulate_waves 设置为 false 不会完全消除这个效果。
				"simulate_waves": true,
				//“大”波浪击中这艘船的概率
				"big_wave_probability": 0.03,
				//“大”波浪的强度
				"big_wave_speed": 10.0,
				//如果移除此组件，船只将被拖下的强度
				"drag_down_on_buoyancy_removed": 0,
				//此实体可以漂浮的液体块。仅允许实际液体：熔岩和水
				"liquid_blocks": ["water"]
			},

			//设置船只在水中的速度
			"minecraft:underwater_movement": {
				"value": 5
			},
			//这个组件很重要，缺少它船只会下沉
			"minecraft:navigation.walk": {
				"can_sink": false
			},
			"minecraft:rideable": {
				"seat_count": 1,
				"family_types": ["player"],
				"interact_text": "action.interact.enter_boat",
				"seats": {
					"position": [0, 0, 0]
				}
			},
			//如果你想用 WASD 控制船只，请添加此组件
			"minecraft:input_ground_controlled": {},
			"minecraft:health": {
				"value": 10,
				"max": 10
			},
			//设置船只在地面的速度（如果不想让船只在地面移动，请将其设置为零）
			"minecraft:movement": {
				"value": 3
			},
			//这是为了防止玩家退出时船只不停下
			"minecraft:movement.basic": {},
			"minecraft:collision_box": {
				"width": 1,
				"height": 1
			},
			"minecraft:physics": {}
		}
	}
}
```

## 使用哪种方法？

这两种方法都适用，但各有优缺点。如果你想禁用弹跳效果，请使用第一种方法。如果你想要更多的控制，请使用第二种方法。我使用第二种方法来处理静态物体，例如浮标，而使用第一种方法来处理可移动实体，例如船只，以模拟原版行为。

## 自定义受伤动画

你可能还对[自定义受伤动画](../visuals/custom-hurt-animations.md)感兴趣。