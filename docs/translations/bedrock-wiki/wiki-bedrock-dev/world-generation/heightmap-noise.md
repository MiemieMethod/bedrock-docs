---
title: 高度图噪声
category: 教程
tags:
    - 实验性
mentions:
    - Apex360
    - SirLich
description: 基于噪声的地形。
---

:::tip
本教程假设你对Molang、地物和地物规则有基本了解。
:::

在本教程中，我们将学习如何使用`q.noise` Molang查询创建基于噪声的地形。

## 单块地物

首先，我们将定义单块地物。它将定义要生成的方块。在本教程中，我将使用石头。

<CodeHeader>BP/features/stone_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:stone_feature"
		},
		"places_block": "minecraft:stone",
		"enforce_survivability_rules": false,
		"enforce_placement_rules": false
	}
}
```

## 散布地物

散布地物是我们将用于生成地形的主要地物。

<CodeHeader>BP/features/column.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:scatter_feature": {
		"description": {
			"identifier": "wiki:column"
		},
		"iterations": "t.height=64+(q.noise(v.originz/64,v.originx/64))*16; return t.height;",
		"places_feature": "wiki:stone_feature",
		"x": 0,
		"z": 0,
		"y": {
			"extent": [-64, "t.height"],
			"distribution": "fixed_grid"
		}
	}
}
```

让我解释一下`iterations`中发生的事情：
在迭代中，我们定义了一个临时变量`t.height`，在其中定义了我们的主要噪声函数。
在`t.height`中，我们首先添加的值是基础高度，基本上是函数开始的高度。
之后，我们使用`q.noise`查询Perlin噪声，返回的值范围从-1到1，并将其除以一个值以平滑函数。
然后，我们将整个函数乘以一个值，简单来说就是地形的变化。

因此，这里发生的事情是我们从`t.height`临时变量中获取值，并将其分配给y范围，从-64到该值，从而生成一个柱状结构。现在这个值会在每个柱子之间变化，但并不是随机的，因为`q.noise`查询的是Perlin噪声，这意味着这些值是相互关联的。因此，我们得到的值不是像64,69,45,100,7,56这样的，而是像64,65,66,68,69,68,66,65这样的。

## 地物规则

<CodeHeader>BP/feature_rules/column_grid_placement.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:feature_rules": {
		"description": {
			"identifier": "wiki:column_grid_placement",
			"places_feature": "wiki:column"
		},
		"conditions": {
			"placement_pass": "first_pass",
			"minecraft:biome_filter": {
				"any_of": [
					{
						"test": "has_biome_tag",
						"value": "overworld"
					},
					{
						"test": "has_biome_tag",
						"value": "overworld_generation"
					}
				]
			}
		},
		"distribution": {
			"iterations": 256,
			"x": {
				"extent": [0, 15],
				"distribution": "fixed_grid"
			},
			"y": 0,
			"z": {
				"extent": [0, 15],
				"distribution": "fixed_grid"
			}
		}
	}
}
```

在这里，我们将`iterations`设置为256，因为整个区块的面积是256（16x16），以便在整个区块中生成柱状结构。

我们的自定义基于噪声的地形完成了！欢迎随意调整这些值。