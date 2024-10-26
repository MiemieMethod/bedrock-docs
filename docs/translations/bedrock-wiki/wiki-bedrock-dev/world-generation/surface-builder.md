---
title: 生成地物
category: 教程
mentions:
    - DerpMcaddon
    - SirLich
tags:
    - 实验性
description: 基于地物的地表构建器是一个将一组方块组合在一起的特性，旨在为下界表面增加多样性和装饰。
---

基于地物的地表构建器是一个将一组方块组合在一起的特性，旨在为下界表面增加多样性和装饰。本教程将解释创建此特性所需的内容，包括大小、频率、生成位置等！

## 单方块地物

单方块地物将是我们地表构建器的基础。它们将定义我们将使用哪些方块。在本教程中，我将使用粗糙土、腐殖土和圆石。

了解更多关于单方块地物的信息 [这里](/world-generation/feature-types#single-block-features)

粗糙土文件

<CodeHeader>BP/features/coarse_dirt_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:coarse_dirt_feature"
		},
		"places_block": {
			//粗糙土与土壤共享相同的标识符，使用名称和状态进行设置
			"name": "minecraft:dirt",
			"states": {
				"dirt_type": "coarse"
			}
		},
		"enforce_survivability_rules": false,
		"enforce_placement_rules": false,
		"may_replace": [
			"minecraft:grass" //该方块只能替换草方块
		]
	}
}
```

腐殖土文件

<CodeHeader>BP/features/podzol_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:podzol_feature"
		},
		"places_block": "minecraft:podzol", //腐殖土可以使用直接标识符定义
		"enforce_survivability_rules": false,
		"enforce_placement_rules": false,
		"may_replace": [
			"minecraft:grass" //该方块只能替换草方块
		]
	}
}
```

圆石文件

<CodeHeader>BP/features/cobblestone_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:cobblestone_feature"
		},
		"places_block": "minecraft:cobblestone", //圆石可以使用直接标识符定义
		"enforce_survivability_rules": false,
		"enforce_placement_rules": false,
		"may_replace": [
			"minecraft:grass" //该方块只能替换草方块
		]
	}
}
```

## 加权随机地物

加权随机地物将是我们选择每种类型方块的随机器。

了解更多关于加权随机地物的信息 [这里](/world-generation/feature-types#weighted-random-features)

<CodeHeader>BP/features/select_surface_block_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:weighted_random_feature": {
		"description": {
			"identifier": "wiki:select_surface_block_feature"
		},
		"features": [
			[
				"wiki:coarse_dirt_feature", //粗糙土的权重为5
				5
			],
			[
				"wiki:podzol_feature", //腐殖土的权重为3
				3
			],
			[
				"wiki:cobblestone_feature", //圆石的权重为2
				2
			]
		]
	}
}
```

## 散布地物

散布地物是我们地表构建器的重要组成部分。它将决定一个块状物的大小、形状和方块数量。

了解更多关于散布地物的信息 [这里](/world-generation/feature-types#scatter-features)

<CodeHeader>BP/features/scatter_surface_block_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:scatter_feature": {
		"description": {
			"identifier": "wiki:scatter_surface_block_feature"
		},
		"iterations": "math.random_integer(20,25)",
		"x": {
			"extent": [0, 8],
			"distribution": "gaussian"
		},
		"z": {
			"extent": [0, 8],
			"distribution": "gaussian"
		},
		"y": "q.heightmap(v.worldx, v.worldz) -1",
		"places_feature": "wiki:select_surface_block_feature" //加权随机地物标识符
	}
}
```

-   `iterations` 决定将放置多少方块。我将使用Molang的 `math.random_integer` 函数来随机化方块数量。在这种情况下，它将是20到25个方块。

-   `extent` 使用数组来确定块状物的大小。`[0, 8]` 意味着大小从0扩展到8个方块。因此，我们的块状物在X轴和Z轴上都是8个方块长。**仅将其用于X和Z分布**。

-   `"y": "q.heightmap(v.worldx, v.worldz) -1` 意味着它将在y坐标上最高的方块下方放置方块-1。因此，它将始终将地物放置在表面上。

-   `distribution` 指定要使用的分布类型。可用的包括 `高斯分布`、`逆高斯分布`、`均匀分布`、`固定网格` 和 `抖动网格`。

## 地物规则

这是我们地表构建器的最后一步。我们地表构建器的地物规则略有不同。

<CodeHeader>BP/feature_rules/overworld_surface_blocks_feature.json</CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:feature_rules": {
		"description": {
			"identifier": "wiki:overworld_surface_blocks_feature",
			"places_feature": "wiki:scatter_surface_block_feature"
		},
		"conditions": {
			"placement_pass": "surface_pass",
			"minecraft:biome_filter": {
				"test": "has_biome_tag",
				"operator": "==",
				"value": "overworld" //您可以将其更改为您想要的任何生物群系标签
			}
		},
		"distribution": {
			"iterations": 1,
			"x": {
				"extent": [0, 16],
				"distribution": "uniform"
			},
			"y": 0,
			"z": {
				"extent": [0, 16],
				"distribution": "uniform"
			},
			"scatter_chance": {
				//每个区块生成块状物的概率
				"numerator": 1,
				"denominator": 5
			}
		}
	}
}
```

我们的地表构建器完成了！欢迎随意修改和尝试！