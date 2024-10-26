---
title: 地物的区块条件
category: 教程
tags:
    - 实验性
mentions:
    - PavelDobCZ23
    - SmokeyStack
    - ThomasOrs
description: 学习如何使用区块条件。
---

有时你可能需要根据其下方或上方的区块来有条件地放置某个地物。例如，并不是所有地物都有这样的条件放置选项，但通过一个简单的技巧，我们可以在任何我们想要的地方使用它。

:::tip
此技巧利用了 `aggregate_feature` 和 `single_block_feature` 地物。如果你想了解更多关于这些内容的信息，请访问 [地物类型](/world-generation/feature-types) 文章。
:::

## 文件

### 地物

此地物放置一个 `single_block_feature`，可以根据我们需要的其他地物的条件进行指定。如果该区块不会干扰你想要的地物，可以保留它，但我们将在下一个地物中将其替换为空气，以避免后续出现任何问题。此地物充当“虚拟”地物，因为我们只需要它的条件部分，而不需要它实际放置任何东西。

<CodeHeader>BP/features/block_condition_feature.json</CodeHeader>

```json
{
    "format_version": "1.18.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:block_condition_feature"
        },
        "places_block": "minecraft:cobblestone", //任何不在 "may_replace" 列表中的区块。
        "enforce_placement_rules": false,
        "enforce_survivability_rules": false,
        "may_replace": ["minecraft:air"], //地物允许放置的区块。
        "may_attach_to": { //附加条件 - 地物放置时可以被哪些区块包围
            "bottom": ["minecraft:grass"] //地物只能放置在这些区块上方。
        }
    }
}
//此“虚拟”地物将仅允许地物在空气中生成，正好在草方块上方。
```

下一个地物将把原本的空气区块替换为石头，但如果你选择一个你实际想要的区块，或者它不会在后续造成任何问题，则可以省略此地物。

<CodeHeader>BP/features/block_replacement_feature.json</CodeHeader>

```json
{
    "format_version": "1.18.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:block_replacement_feature"
        },
        "places_block": "minecraft:air", //将区块替换为另一个不会造成问题的区块。
        "enforce_placement_rules": false,
        "enforce_survivability_rules": false,
        "may_replace": ["minecraft:cobblestone"] //我们在前一个地物中指定的区块。
    }
}
//此地物将把原本存在的区块替换为空气，以避免我们出现任何问题。
```

这是一个放置条件“虚拟”地物的地物，该地物去掉由条件放置的“虚拟”区块，然后放置我们想要有条件放置的实际地物。它使用 `early_out` 设置为 `first_failure`，以确保如果条件放置失败，聚合将停止。它是由地物规则放置的地物。

<CodeHeader>BP/features/aggregate_placement_rock_feature.json</CodeHeader>

```json
{
    "format_version": "1.18.0",
    "minecraft:aggregate_feature": {
        "description": {
            "identifier": "wiki:aggregate_placement_rock_feature"
        },
        "features": [
            "wiki:block_condition_feature", //作为“虚拟”地物的单个区块地物，用于作为我们的条件。
            "wiki:block_replacement_feature", //此地物替换我们在上一个地物中使用的“虚拟”区块，以避免后续出现任何问题。
            //从此点开始的任何地物都是我们实际想要放置的地物。
            "wiki:rock_ore_feature"
        ],
        "early_out": "first_failure" //确保如果第一个（或任何）地物失败，则不会继续放置列表中的其他内容。
    }
}
//这是一个逐个按顺序放置所有地物的地物，并由地物规则放置。
```

这是我们想要有条件放置的实际地物。它是 `ore_feature`，没有实际条件来允许它仅放置在空气中和草方块上，因此这个技巧帮助我们实现了这一点。

<CodeHeader>BP/features/rock_ore_feature.json</CodeHeader>

```json
{
	"format_version": "1.18.0",
	"minecraft:ore_feature": {
		"description": {
			"identifier": "wiki:rock_ore_feature"
		},
		"count": 12,
		"replace_rules": [
			{
				"places_block": "minecraft:stone",
				"may_replace": ["minecraft:air","minecraft:grass"]
			},
			{
				"places_block": {
                    "name": "minecraft:dirt",
                    "states": {
                      "dirt_type": "coarse"
                    }
                },
				"may_replace": ["minecraft:dirt"]
			}
		]
	}
}
```
:::tip
如果你想了解更多关于矿石地物的信息，可以访问 [生成自定义矿石](/world-generation/custom-ores) 教程。
:::

### 地物规则

<CodeHeader>BP/feature_rules/overworld_after_surface_rock_feature.json</CodeHeader>

```json
{
	"format_version": "1.18.0",
	"minecraft:feature_rules": {
		"description": {
			"identifier": "wiki:overworld_after_surface_rock_feature",
			"places_feature": "wiki:aggregate_placement_rock_feature"
		},
		"conditions": {
			//在任何地表生物群系中放置地物，并与 after_surface_pass 中的地物一起放置
			"placement_pass": "after_surface_pass",
			"minecraft:biome_filter": [
				{
					"any_of": [
						{
							"test": "has_biome_tag",
							"operator": "==",
							"value": "overworld"
						},
						{
							"test": "has_biome_tag",
							"operator": "==",
							"value": "overworld_generation"
						}
					]
				}
			]
		},
		"distribution": {
			//在区块中有 1/3 的机会尝试放置 1 个地物
            "scatter_chance": 33,
			"iterations": 1, 
			"coordinate_eval_order": "xzy",
			"x": {
				"distribution": "uniform",
				"extent": [0, 15]
			},
			//沿着高度图放置地物
			"y": "q.heightmap(v.worldx,v.worldz)",
			"z": {
				"distribution": "uniform",
				"extent": [0, 15]
			}
		}
	}
}
```

## 总结

阅读完本教程后，你应该能够在任何你想要的地物上使用区块条件。这是一个非常基础的示例，因为这可以用于更复杂的创作，并且可以与任何地物一起使用。

就这样，我们创建了一个只能放置在空气区块和草方块上方的岩石地物。

生成截图：

![](/assets/images/world-generation/rock_feature.png)