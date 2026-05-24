# 战利品表、生成规则与合成配方

/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/guide/loot-table](https://wiki.bedrock.dev/guide/loot-table)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

接下来我们将为自定义的幽灵实体添加更多基础机制：

## 战利品表

首先让幽灵死亡时掉落灵质，创建以下文件：

```json title="BP/loot_tables/entities/ghost.json"
{
	"pools": [
		{
			"rolls": 1,
			"entries": [
				{
					"type": "item",
					"name": "wiki:ectoplasm",
					"weight": 1,
					"functions": [
						{
							"function": "set_count",
							"count": {
								"min": 1,
								"max": 3
							}
						}
					]
				}
			]
		}
	]
}
```

- 战利品表由`"pools"`（池）组成，每个池定义不同的战利品。每个池包含三部分：`"rolls"`（随机次数）、`"entries"`（条目）和可选的`"conditions"`（条件）。关于条件的详细信息请参阅[战利品表](https://wiki.bedrock.dev/loot/loot-tables)
- `"rolls"`定义从`"entries"`中随机选择物品的次数
- `"entries"`定义可供选择的物品列表，每次roll会从中选取一个新物品
- `"type"`决定选取类型，可设置为`"item"`（物品）或`"loot_table"`（其他战利品表）
- `"name"`使用命名空间格式指定具体物品
- `"weight"`（权重）决定物品被选中的概率，默认值为1
- `"functions"`提供强大的物品自定义功能，可通过`"set_count"`设置掉落数量范围

更多战利品表知识请参阅进阶指南：[战利品表](https://wiki.bedrock.dev/loot/loot-tables)

## 生成规则

接下来配置幽灵在沙漠生物群系的夜间生成规则：

```json title="BP/spawn_rules/ghost.json"
{
	"format_version": "1.8.0",
	"minecraft:spawn_rules": {
		"description": {
			"identifier": "wiki:ghost",
			"population_control": "monster"
		},
		"conditions": [
			{
				"minecraft:spawns_on_surface": {},
				"minecraft:brightness_filter": {
					"min": 0,
					"max": 7,
					"adjust_for_weather": true
				},
				"minecraft:difficulty_filter": {
					"min": "easy",
					"max": "hard"
				},
				"minecraft:weight": {
					"default": 80
				},
				"minecraft:herd": {
					"min_size": 1,
					"max_size": 3
				},
				"minecraft:biome_filter": {
					"test": "has_biome_tag",
					"operator": "==",
					"value": "desert"
				}
			}
		]
	}
}
```

- `"description"`定义基础属性：
  - `"identifier"`指定应用此规则的实体
  - `"population_control"`控制实体生成数量上限
- `"conditions"`包含生成条件：
  - `"spawns_on_surface"`限制地表生成
  - `"brightness_filter"`设置光照范围（0-7），`"adjust_for_weather"`忽略天气影响
  - `"difficulty_filter"`设置生效难度范围
  - `"weight"`控制生成频率（数值越高越常见）
  - `"herd"`设置单次生成数量
  - `"biome_filter"`限定沙漠生物群系

详细生成规则请参考：[原版生成规则](https://wiki.bedrock.dev/entities/vanilla-usage-spawn-rules)

## 合成配方

最后实现将灵质合成史莱姆方块的功能：

```json title="BP/recipes/ectoplasm_slime_blocks.json"
{
	"format_version": "1.12.0",
	"minecraft:recipe_shaped": {
		"description": {
			"identifier": "wiki:ectoplasm_slime_block"
		},
		"tags": ["crafting_table"],
		"pattern": ["###", "###", "###"],
		"key": {
			"#": {
				"item": "wiki:ectoplasm"
			}
		},
		"result": {
			"item": "minecraft:slime"
		}
	}
}
```

- `"recipe_shaped"`表示有序合成配方
- `"tags"`指定适用的工作台类型
- `"pattern"`定义3x3网格布局，`#`符号对应`"key"`中指定的灵质
- `"result"`设置输出为原版史莱姆方块

完整配方教程请查看：[合成配方](https://wiki.bedrock.dev/loot/recipes)

## 知识总结

/// tip | 学习要点
- 创建战利品表配置生物掉落
- 设置生物生成规则
- 制作合成配方
///

## 当前进度

**已完成内容：**

-   [x] 资源包初始化
-   [x] 创建自定义物品
-   [x] 创建自定义实体
-   [x] 添加实体掉落、生成规则与合成配方

恭喜！你已完成全部教程并创建了第一个附加包 🎉