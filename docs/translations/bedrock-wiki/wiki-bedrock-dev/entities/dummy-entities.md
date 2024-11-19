---
title: 虚拟实体
category: 教程
tags:
    - 初学者
mentions:
    - SirLich
    - Joelant05
    - MedicalJewel105
    - aexer0e
description: 虚拟实体是用于游戏玩法目的的隐形实体。
---

虚拟实体是用于游戏玩法目的的隐形实体。虚拟实体是一个非常有用的工具，本文将介绍它们的一些用法，并展示如何设置资源方面的内容。

## 使用虚拟实体

以下是虚拟实体的一些非详尽使用方式：

-   **用于数据存储**：通过为实体添加标签，我们可以将其用作“游戏管理器”，类似于以前使用的盔甲架。
-   **作为命名实体**：通过为虚拟实体添加名称标签，然后使用 `execute` 进行选择，你可以使命令方块以美观的显示名称执行 `/say`。
-   **作为位置标记**：你可以在虚拟实体处运行 `execute` 命令，以获取该位置的相对坐标。
-   **作为航点**：通过制作对你的虚拟实体具有攻击性的实体，你可以通过在该位置放置虚拟实体来引导实体到达任何位置。

## 创建虚拟实体

### 行为实体

你可以使用任何你喜欢的行为，但这里有一个不错的模板。重要的方面是：无伤害，且无法被推动。

```json title="BP/entities/dummy.json"
{
	"format_version": "1.16.0",
	"minecraft:entity": {
		"description": {
			"identifier": "wiki:dummy",
			"is_summonable": true,
			"is_spawnable": false,
			"is_experimental": false
		},
		"components": {
			"minecraft:breathable": { //可选，允许实体在水下呼吸
				"breathes_water": true
			},
			"minecraft:physics": { 
				"has_gravity": false, //可选，允许实体不受重力或水的影响
				"has_collision": false
			},
			"minecraft:custom_hit_test": {
				"hitboxes": [
					{
						"pivot": [0, 100, 0],
						"width": 0,
						"height": 0
					}
				]
			},
			"minecraft:damage_sensor": {
				"triggers": {
					"deals_damage": false
				}
			},
			"minecraft:pushable": {
				"is_pushable": false,
				"is_pushable_by_piston": false
			},
			"minecraft:collision_box": {
				"width": 0.0001,
				"height": 0.0001
			}
		}
	}
}
```

如果你希望完全禁用碰撞（以便可以在其位置放置方块），你可以使用箭头运行时标识符，但可能会有一些副作用。

### 资源实体

```json title="RP/entity/dummy.json"
{
	"format_version": "1.10.0",
	"minecraft:client_entity": {
		"description": {
			"identifier": "wiki:dummy",
			"materials": {
				"default": "entity_alphatest"
			},
			"geometry": {
				"default": "geometry.dummy"
			},
			"render_controllers": ["controller.render.dummy"],
			"textures": {
				"default": "textures/entity/dummy"
			}
		}
	}
}
```

### 几何体

```json title="RP/models/entity/dummy.json"
{
	"format_version": "1.12.0",
	"minecraft:geometry": [
		{
			"description": {
				"identifier": "geometry.dummy",
				"texture_width": 16,
				"texture_height": 16
			}
		}
	]
}
```

### 渲染控制器（可选）

```json title="RP/render_controllers/dummy.json"
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.dummy": {
			"geometry": "Geometry.default",
			"textures": ["Texture.default"],
			"materials": [
				{
					"*": "Material.default"
				}
			]
		}
	}
}
```

### 纹理（可选）

你可以选择将纹理位置留空，或者在Blockbench中打开模型并创建一个空白纹理。