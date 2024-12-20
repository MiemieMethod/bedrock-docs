---
title: 实体持有物品
category: 教程
tags:
    - 中级
mentions:
    - pieterdefour
    - SirLich
    - solvedDev
    - stirante
    - Joelant05
    - destruc7ion
    - Dreamedc2015
    - sermah
    - 7dev7urandom
    - legopitstop
description: 在本教程中，你将学习如何让实体手中持有物品。
---

/// tip
本教程假设你对实体、战利品表和Blockbench有基本的了解。
///

在本教程中，你将学习如何让实体手中持有物品。我将使用一个自定义的`mandalorian_armorer`实体和一个自定义的`hammer`物品作为示例。

## 模型

首先，你需要在Blockbench中创建一个名为`rightArm`的映射。在这个映射中，需要有一个名为`rightItem`的子映射。
现在设置这个子映射的支点位置，使其位于你希望实体持有物品的位置。

![](../assets/images/tutorials/entity-holds-item/blockbench.png)

## 行为包部分

接下来，你需要在实体的组件列表中添加一个`minecraft:equipment`组件，并添加一个包含所需物品的战利品表。

在我们的示例中，它将如下所示：

```json title="BP/entity/mandolorian.json#components"
"minecraft:equipment": {
    "table": "loot_tables/entities/gear/mandolorian.json"
}
```

## 战利品表

最后，为你的实体添加战利品表。它需要位于行为包中的`loot_tables/entities/<your_loot_table_name>.json`。在我们的案例中，它被称为`mandolorian.json`。

/// warning
这与实体死亡时掉落的物品战利品表不同。因此，请确保它有一个不同的名称。
///

要让实体始终持有相同的物品，请添加以下战利品表：

```json title="BP/loot_tables/entities/gear/mandolorian.json"
{
	"pools": [
		{
			"rolls": 1,
			"entries": [
				{
					"type": "item",
					"name": "dd:hammer",
					"weight": 1
				}
			]
		}
	]
}
```

如果一切顺利，你将得到如下所示的结果：

![](../assets/images/tutorials/entity-holds-item/finished_result.png)

## 常见问题

- 持有的物品未显示

你的实体包含多个几何变体。