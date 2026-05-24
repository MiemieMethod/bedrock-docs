# 创建自定义实体

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/guide/custom-entity](https://wiki.bedrock.dev/guide/custom-entity)
///

与自定义物品类似，我们也可以创建具有与游戏中原版实体相似机制的自定义实体。这些实体可以非常强大，允许你制作可繁殖驯养的动物，或是会攻击所见一切的敌对生物。

本文将创建一个幽灵实体，它会漂浮移动、攻击玩家，并在死亡时掉落我们之前制作的灵质物品。

<br>
<img src="/assets/images/guide/custom_entity/ghost_view.png" width=150>
<br>
<br>

和物品一样，实体由两部分组成：

-   视觉部分（纹理、名称、动画、音效）
-   行为部分（移动、攻击）

不同的是，我们需要为实体创建两个主文件：分别放在行为包（BP）和资源包（RP）中的 _服务端_ 文件和 _客户端_ 文件。此外还需要额外的文件来描述实体的几何模型和动画，这些将在后续章节中介绍。

首先我们将介绍如何创建实体并定义其行为，然后再添加视觉效果。

## 实体行为

与物品类似，我们需要一个文件来定义实体行为，通过标识符关联到具体的行为组件。这个文件的结构与物品行为文件非常相似，但包含更多组件。

我们在行为包的`BP/entities/`文件夹下创建服务端文件，命名为`ghost.se.json`。这里的`.se`代表 _server entity_（服务端实体），这是为了清晰起见，符合[样式指南](../meta/style-guide.md)的推荐。

文件基本结构如下：

```json title="BP/entities/ghost.se.json"
{
	"format_version": "1.16.0",
	"minecraft:entity": {
		"description": {...},
		"components": {...}
	}
}
```

与物品文件类似，我们有格式版本标识，这里使用`"minecraft:entity"`表示这是实体文件。后续我们将不再赘述格式版本，建议直接使用示例中的版本。

实体在`description`部分包含更多信息：

```json title="BP/entities/ghost.se.json > minecraft:entity"
"description": {
	"identifier": "wiki:ghost",
	"is_summonable": true,
	"is_spawnable": true,
	"is_experimental": false
}
```

`identifier`键的作用与之前相同，用于标识这个实体。其他键决定了实体加入世界的方式：

-   `is_summonable`：是否可以通过`/summon`命令召唤
-   `is_spawnable`：是否可以通过刷怪蛋或生成规则在世界中自然生成
-   `is_experimental`：是否为实验性实体（如果是则只能添加到实验性世界）

建议保持这些设置不变，因为任何更改都会使你在游戏中测试实体变得更加困难。

### 组件

实体比物品拥有更多行为，因此需要定义更多组件。我们将这些组件分类并详细讲解。更多关于实体组件的信息，可以参考[此页面](https://wiki.bedrock.dev/entities/entity-intro-bp)。

### 基础属性组件

这些是每个实体通常都会具备的组件，定义了实体的核心属性。

```json title="BP/entities/ghost.se.json > minecraft:entity > components"
"minecraft:type_family": {
	"family": ["ghost", "monster"]
},
"minecraft:health": {
	"value": 20,
	"max": 20
},
"minecraft:attack": {
	"damage": 3
},
"minecraft:movement": {
	"value": 0.2
},
"minecraft:collision_box": {
	"width": 1,
	"height": 2
},
"minecraft:loot": {
	"table": "loot_tables/entities/ghost.json"
},
```

`minecraft:health`、`minecraft:attack`和`minecraft:movement`组件直接设置实体的生命值、攻击伤害和移动速度。实体的碰撞箱是它与方块或其他实体交互/碰撞的范围，由`minecraft:collision_box`定义，这个箱子会以实体为中心。

`minecraft:type_family`为实体添加家族标签。家族标签用于将相似类别的实体分组。例如`monster`包括僵尸、骷髅和苦力怕，这样我们就可以选择所有带有`monster`标签的实体。

`minecraft:loot`定义了实体死亡时掉落的战利品表路径。我们将在后续章节使用这个路径创建战利品表。

### 移动组件

为了让实体能够移动，我们需要定义两件事： _如何_ 移动和 _可以_ 移动到哪里。这分别通过`movement`和`navigation`组件实现。

如果你希望实体能够移动，就必须包含`movement`和`navigation`组件。

```json title="BP/entities/ghost.se.json > minecraft:entity > components"
"minecraft:physics": {},
"minecraft:jump.static": {},
"minecraft:movement.basic": {},
"minecraft:navigation.walk": {
	"can_walk": true,
	"avoid_sun": true,
	"can_pass_doors": true,
	"can_open_doors": true
}
```

`minecraft:physics`用于给实体应用重力和碰撞。注意：你不能通过组件组来修改这个组件。
`minecraft:jump.static`允许你的实体跳跃以跨越障碍。这两个组件几乎用于所有实体。

有几种不同的移动组件允许不同类型的移动，例如海豚使用的`minecraft:movement.swim`、鹦鹉使用的`minecraft:movement.fly`和蜜蜂使用的`minecraft:movement.hover`。
`minecraft:movement.basic`组件允许我们的实体通过在地面上行走来移动。为了让实体看起来像是在漂浮，我们将使用几何模型。

导航组件是一个路径寻找器，定义了允许实体遵循的路径。例如骷髅会尽量避免走在阳光下，所以它们的路径规划会阻止它们选择阳光下的路径。此外，鹦鹉可以飞行，所以它们可以在空中移动，这与行走的生物不同。

这些组件有许多不同的设置，可以实现有趣的路径规划。我们选择的设置让幽灵可以在地面上行走，避免阳光直射，穿过门道并开门。

### 行为组件

虽然我们已经定义了实体 _如何_ 做事情，但还没有定义 _何时_ 或 _做什么_ 。这就是`.behavior`组件的作用。这些组件定义了实体将执行的特定动作。
例如，村民会尝试繁殖，所以他们有`minecraft:behavior.breed`组件，而被驯服的狼会跟随主人，所以他们有`minecraft:behavior.follow_owner`组件。

我们希望幽灵能够闲逛和环顾四周，在玩家靠近时锁定目标并攻击。以下是使用的组件：

```json title="BP/entities/ghost.se.json > minecraft:entity > components"
// 允许随机移动和环顾四周
"minecraft:behavior.random_stroll": {...},
"minecraft:behavior.random_look_around": {...},
"minecraft:behavior.look_at_player": {...},
// 允许锁定目标
"minecraft:behavior.hurt_by_target": {...},
"minecraft:behavior.nearest_attackable_target": {...},
// 允许攻击
"minecraft:behavior.delayed_attack": {...}
```

第一个组件`minecraft:behavior.random_stroll`允许我们的实体定期选择一个附近的随机点进行移动。这个路径由我们的`navigation`组件创建，然后移动类型由`movement`组件定义。

接下来的两个组件允许实体随机环顾四周，并在玩家进入范围内时注视玩家。

为了攻击，实体需要一个`target`。`minecraft:behavior.hurt_by_target`和`minecraft:behavior.nearest_attackable_target`行为会使实体锁定任何伤害它的目标，并在范围内锁定最近的敌人。

最后，`minecraft:behavior.delayed_attack`是实体实际攻击目标的方式。

每个行为都有更多设置可以调整具体行为。

```json title="BP/entities/ghost.se.json > minecraft:entity > components"
"minecraft:behavior.random_stroll": {
	"priority": 6,
	"speed_multiplier": 1
},
"minecraft:behavior.random_look_around": {
	"priority": 7
},
"minecraft:behavior.look_at_player": {
	"priority": 7,
	"look_distance": 6,
	"probability": 0.02
},
"minecraft:behavior.hurt_by_target": {
	"priority": 1
},
"minecraft:behavior.nearest_attackable_target": {
	"priority": 2,
	"within_radius": 25,
	"reselect_targets": true,
	"entity_types": [
		{
			"filters": {
				"any_of": [
					{
						"test": "is_family",
						"subject": "other",
						"value": "player"
					}
				]
			},
			"max_dist": 35
		}
	]
},
"minecraft:behavior.delayed_attack": {
	"priority": 0,
	"attack_once": false,
	"track_target": true,
	"require_complete_path": false,
	"random_stop_interval": 0,
	"reach_multiplier": 1.5,
	"speed_multiplier": 1,
	"attack_duration": 0.75,
	"hit_delay_pct": 0.5
}
```

有关这些选项的更多详细信息，可以在文档[bedrock.dev](https://bedrock.dev/docs/stable/Entities)上阅读。

#### 优先级

所有行为都包含一个`"priority"`字段。这个字段用于决定当多个行为可以运行时选择哪一个。

当实体选择要执行的动作时，它会从最低优先级到最高优先级搜索所有行为，并选择第一个可以执行的行为。因此，你需要将重要的行为（如`minecraft:behavior.nearest_attackable_target`）设置为比`minecraft:behavior.look_at_player`等行为更低的优先级。如果`look_at_player`行为的优先级较低，当玩家靠近时，实体总是会先执行这个行为，而永远不会攻击。

一般来说，重要行为的优先级为`0`或`1`。

### 完整实体服务端文件

/// details | 完整的ghost.se.json
```json title="BP/entities/ghost.se.json"
{
	"format_version": "1.16.0",
	"minecraft:entity": {
		"description": {
			"identifier": "wiki:ghost",
			"is_summonable": true,
			"is_spawnable": true,
			"is_experimental": false
		},
		"components": {
			"minecraft:type_family": {
				"family": ["ghost", "monster"]
			},
			"minecraft:health": {
				"value": 20,
				"max": 20
			},
			"minecraft:attack": {
				"damage": 3
			},
			"minecraft:movement": {
				"value": 0.2
			},
			"minecraft:collision_box": {
				"width": 1,
				"height": 2
			},
			"minecraft:loot": {
				"table": "loot_tables/entities/ghost.json"
			},
			"minecraft:physics": {},
			"minecraft:jump.static": {},
			"minecraft:movement.basic": {},
			"minecraft:navigation.walk": {
				"can_walk": true,
				"avoid_sun": true,
				"can_pass_doors": true,
				"can_open_doors": true
			},

			"minecraft:behavior.random_stroll": {
				"priority": 6,
				"speed_multiplier": 1
			},
			"minecraft:behavior.random_look_around": {
				"priority": 7
			},
			"minecraft:behavior.look_at_player": {
				"priority": 7,
				"look_distance": 6,
				"probability": 0.02
			},
			"minecraft:behavior.hurt_by_target": {
				"priority": 1
			},
			"minecraft:behavior.nearest_attackable_target": {
				"priority": 2,
				"within_radius": 25,
				"reselect_targets": true,
				"entity_types": [
					{
						"filters": {
							"any_of": [
								{
									"test": "is_family",
									"subject": "other",
									"value": "player"
								}
							]
						},
						"max_dist": 35
					}
				]
			},
			"minecraft:behavior.delayed_attack": {
				"priority": 0,
				"attack_once": false,
				"track_target": true,
				"require_complete_path": false,
				"random_stop_interval": 0,
				"reach_multiplier": 1.5,
				"speed_multiplier": 1,
				"attack_duration": 0.75,
				"hit_delay_pct": 0.5
			}
		}
	}
}
```
///

至此我们完成了实体行为文件。

更复杂的实体还可以有不同的_状态_，根据所处状态表现出不同行为。例如，野生的狼会自由走动，但被驯服后会跟随玩家。一个_事件_（被驯服）导致狼改变了_状态_。这个功能允许我们创建动态实体，在不同事件发生时执行不同动作。你可以在[本指南](https://wiki.bedrock.dev/entities/entity-intro-bp)中了解更多。

如果你现在打开世界并尝试用`/summon wiki:ghost`召唤实体，它的行为应该符合预期，但地面上只会显示一个影子。你可能还会看到它的名称显示为翻译键，就像我们的物品一样。

接下来我们将学习如何创建资源（客户端）文件，以及如何分配纹理、几何模型和动画。

## 实体资源

为实体添加视觉效果与物品截然不同。由于涉及更多组成部分，我们需要一个专门的文件来定义资源。这个文件称为实体_客户端文件_，我们将其命名为`ghost.ce.json`，存放在`RP/entity/`文件夹中。

本节将使用为幽灵实体创建的示例资源，演示如何将它们添加到实体中。在指南的下一节中，我们将介绍如何使用专业3D编辑器Blockbench创建自己的实体几何模型和动画。

### 模型

实体的"模型"即其形状，也称为"几何模型"。这描述了实体的外形，比如猪是由一个箱体和四条腿加头部组成，而鸡则有两条腿、一个头部和翅膀。几何模型以JSON格式存储在`RP/models/entity/`目录下，我们的文件将命名为`ghost.geo.json`。

这个文件由Blockbench自动生成，因此无需手动学习其语法。所以我们不会深入分析文件细节。它存储了模型中每个方块的数据，包括大小、位置和旋转等。

```json title="RP/models/entity/ghost.geo.json"
{
	"format_version": "1.12.0",
	"minecraft:geometry": [
		{
			"description": {
				"identifier": "geometry.ghost",
				"texture_width": 64,
				"texture_height": 64,
				"visible_bounds_width": 3,
				"visible_bounds_height": 3.5,
				"visible_bounds_offset": [0, 1.25, 0]
			},
			"bones": [
				{ "name": "root", "pivot": [0, 3, 0] },
				{
					"name": "body",
					"parent": "root",
					"pivot": [0, 4.625, 0],
					"cubes": [
						{
							"origin": [-4, 3, -4],
							"size": [8, 13, 8],
							"uv": [0, 20]
						}
					]
				},
				{
					"name": "leftArm",
					"parent": "body",
					"pivot": [4.6, 15.5, 0.5],
					"cubes": [
						{
							"origin": [4.1, 7, -1],
							"size": [3, 9, 3],
							"uv": [32, 32]
						}
					]
				},
				{
					"name": "rightArm",
					"parent": "body",
					"pivot": [-4.5, 15.5, 0.5],
					"cubes": [
						{
							"origin": [-7.1, 7, -1],
							"size": [3, 9, 3],
							"uv": [32, 20]
						}
					]
				},
				{
					"name": "head",
					"parent": "body",
					"pivot": [0, 16, 0],
					"cubes": [
						{
							"origin": [-5, 16, -5],
							"size": [10, 10, 10],
							"uv": [0, 0]
						}
					]
				}
			]
		}
	]
}
```

我们需要的关键信息是`identifier`，这里为`geometry.ghost`，这将用于引用我们的几何模型文件。

### 纹理

现在实体有了形状，但还需要纹理。这个纹理也可以在Blockbench中创建，是一个简单的`.png`文件。

`RP/textures/entity/ghost.png`

![ectoplasm.png](https://raw.githubusercontent.com/Bedrock-OSS/wiki-addon/main/ma-guide/guide_RP/textures/entity/ghost.png)

[点击下载纹理](https://raw.githubusercontent.com/Bedrock-OSS/wiki-addon/main/ma-guide/guide_RP/textures/entity/ghost.png){ .md-button }
