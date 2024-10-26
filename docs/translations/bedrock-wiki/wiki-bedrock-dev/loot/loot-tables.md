---
title: 战利品表
category: 文档
nav_order: 1
mentions:
    - Ciosciaa
    - Etanarvazac
    - SmokeyStack
description: 关于战利品表的所有内容。
---

::: warning
本文件仍在完善中。
:::

战利品表用于从声明的集合中选择一组物品。战利品表可以通过以下方式使用：

- `/loot` 命令
- 容器内容
- 方块掉落
- 钓鱼
- 生物掉落
- 生成生物的装备
- 其他各种生物行为

每次使用相同战利品表时，可能会根据 [外部条件](#) 和 [内在随机性](#) 选择不同的物品集合。这种变化对于可玩性和冒险体验至关重要，尤其是在更具角色扮演游戏驱动的系统中。

## 集成
战利品表不是注册的附加包条目，而是通过上述来源的路径进行引用。战利品表可以放置在行为包的任何位置，但建议将其放置在顶层的 `loot_tables` 目录下，以遵循原版约定。

<FolderView
	:paths="[
		'BP/loot_tables/blocks/cypress_door.json',
		'BP/loot_tables/blocks/cypress_door.json',
		'BP/loot_tables/blocks/cypress_door.json'
	]"
/>

## 结构
战利品表表示为具有单个必需的 `"pools"` 数组属性的 JSON 对象。

<CodeHeader>#</CodeHeader>

```json
{
	"pools": [
		…
	]
}
```

从战利品表调用返回的战利品将是此处提供的所有池的 *总和*。

### 池
池作为选择物品的独立构造；池的结果不能受到其他池的影响。

<CodeHeader>#</CodeHeader>

```json
{
	"rolls": 1,
	
	"entries": [
		{
			"type": "item",
			"name": "wiki:silver"
		}
	]
}
```

可用两种类型的池：通用的 [加权随机池](#weighted-random-pools) 和 [分层池](#tiered-pools)，后者通常用于选择生物装备。

#### 加权随机池
传统的加权随机池根据相对权重选择物品，根据配置的投掷次数选择一定数量的产出。

<CodeHeader>artifacts.json/pools/0</CodeHeader>

```json
{
	"rolls": {
		"min": 2,
		"max": 4
	},
	
	"entries": [
		{
			"type": "item",
			"name": "minecraft:golden_apple",
			"weight": 20
		},
		{
			"type": "item",
			"name": "minecraft:appleEnchanted",
			"weight": 1
		},
		{
			"type": "item",
			"name": "minecraft:name_tag",
			"weight": 30
		}
	]
}
```

##### 投掷

###### 奖励投掷
加权随机池的投掷次数可以通过可选的 `"bonus_rolls"` 属性根据玩家的运气进行调整。

```json

```

##### 条目权重
权重是选择此条目的机会。与此 "entries" 数组中的其他条目相比，权重越高，选择该条目的机会就越大。

```json
"weight": 3
```

###### 质量
条目的权重可以通过质量属性根据玩家的运气进行更改。

```json
"quality": 2
```

目前，运气仅在使用附有海之运的钓竿钓鱼时体现。

#### 分层池
分层池用于从集合中精确选择一个条目。

```json
{
	"tiers": {
		"initial_range": 2,
		
		"bonus_rolls": 3,
		"bonus_chance": 0.095
	},

	"entries": [
		{
			"type": "loot_table",
			"name": "loot_tables/entities/armor_set_leather.json"
		},
		{
			"type": "loot_table",
			"name": "loot_tables/entities/armor_set_gold.json"
		},
		{
			"type": "loot_table",
			"name": "loot_tables/entities/armor_set_chain.json"
		},
		{
			"type": "loot_table",
			"name": "loot_tables/entities/armor_set_iron.json"
		},
		{
			"type": "loot_table",
			"name": "loot_tables/entities/armor_set_diamond.json"
		}
	]
}
```

通过包含 `"tiers"` 对象属性，池变为分层：

```json
"tiers": {
	"initial_range": 2,
	
	"bonus_rolls": 3,
	"bonus_chance": 0.095
}
```

分层池中的条目是 *有序的*。分层池的选定条目基于其索引。为了确定此索引，首先随机投掷一个起始索引，然后进行一批成功投掷尝试以增加此起始索引。

起始索引通过在 1 和整数属性 `"initial_range"` 之间投掷一个随机整数来决定。如果未提供初始范围，则默认为 `1`，强制起始索引为 1。

接下来，尝试使用额外的投掷来推进索引。这些投掷尝试的数量作为整数提供给 `"bonus_rolls"`。任何此类投掷成功的机会通过 `"bonus_chance"` 给出。`"bonus_chance"` 的机会以 1 为基数，意味着 `0.5` 将是任何奖励投掷成功的 50% 的机会。每次成功的投掷将索引增加 1。这两个属性默认为 `0`，意味着必须提供这两个属性才能使用此额外投掷机制。

最终确定的索引用于选择作为该池的产出对应的条目。分层池中的索引是从 1 开始的，这意味着第一个条目的索引为 1，第二个为 2，依此类推。如果确定的索引大于该池的条目数量，则不会提供任何产出。

::: warning
分层池中条目的所有 [条件](#) 都会被忽略。池本身的条件仍然允许。
:::

### 条目
条目是池中可选择的单位。可用三种不同类型的条目。

```json

```

#### 物品条目
物品条目是选择战利品的基本条目类型。物品条目指的是

```json

```

#### 战利品表条目
可以使用战利品表条目形成战利品层次结构。

```json

```

#### 空条目
当被选择时，空条目不会为该投掷提供任何战利品。

```json
"type": "empty",
"weight": 4
```

空条目通常可以通过 [投掷次数](#) 的范围包括 0、[随机机会条件](#) 或 [计数函数](#) 来模拟，这些函数可能随机选择 0。它们的主要优势在于在使用 [加权随机池](#) 时的可读性：通过权重表示投掷不会产生条目的情况可能更易于理解。

### 函数
函数使战利品表如此强大。它们可以为战利品表中的每个条目执行广泛的任务。例如，它们可以改变掉落物品的数量、物品上存在的附魔（即使在通常不能附魔的物品上）、物品名称、物品描述，甚至可以写书！查看 [物品函数](/loot/item-functions) 以获取完整的函数列表及其用法。

<CodeHeader>artifacts.json/pools/entries</CodeHeader>

```json
{
	"type": "item",
	"name": "minecraft:dirt",
	"weight": 10,
	"functions": [
		{
			"function": "set_count",
			"count": {
				"min": 16,
				"max": 64
			}
		},
		{
			"function": "set_name",
			"name": "一堆泥土"
		}
	]
}
```

### 条件
条件用于检查某个标准是否满足。例如：“僵尸是被玩家杀死的”、“剑上是否有掠夺附魔？如果有，是什么等级？”

<CodeHeader>artifacts.json/pools/entries</CodeHeader>

```json
{
	"conditions": [
		{
			"condition": "killed_by_player"
		},
		{
			"condition": "random_chance_with_looting",
			"chance": 0.025,
			"looting_multiplier": 0.01
		}
	],
	"rolls": 1,
	"entries": [
		{
			"type": "item",
			"name": "minecraft:iron_ingot",
			"weight": 1
		},
		{
			"type": "item",
			"name": "minecraft:carrot",
			"weight": 1
		},
		{
			"type": "item",
			"name": "minecraft:potato",
			"weight": 1
		}
	]
}
```

## 覆盖