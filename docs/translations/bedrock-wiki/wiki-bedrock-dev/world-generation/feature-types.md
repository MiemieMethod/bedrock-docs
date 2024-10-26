---
title: 地物类型
category: 通用
tags:
    - 实验性
mentions:
    - SirLich
    - MedicalJewel105
    - Luthorius
    - TheItsNameless
description: 世界生成地物类型说明。
---

_最后更新于1.17.10_

::: warning
一些旨在引用外部文档的链接无法正常工作，将在稍后更新以指向正确的资源。

许多此处提供的地物类型的屏幕截图和其他资源可能会在稍后提供。
:::

## 内容地物

内容地物是定义地物系统中方块放置的基本地物类型。它们在排列或组成方面没有任何内容。相反，它们定义了方块的基本排列，通常与[代理地物](#代理地物)结合或定位使用。

### 单方块地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:pier_planks"
		},

		"places_block": "minecraft:planks",

		"enforce_placement_rules": true,
		"enforce_survivability_rules": true,
		"may_replace": ["minecraft:water"],
		"may_attach_to": {
			"top": "minecraft:air",
			"sides": ["minecraft:planks", "minecraft:water"]
		}
	}
}
```

**单方块地物**在世界中放置单个方块。单方块地物单独使用通常无用；它们的真正力量来自与[代理地物](#代理地物)结合构建建筑。

**目标方块**，即要放置的方块，通过 `"places_block"` 属性指定。目前定义中无法实现变化能力；必须使用额外单方块地物的[加权随机地物](#加权随机地物)。

#### 条件

可以指定**条件**以限制放置成功。如果任何条件失败，方块将不会放置。

::: warning
为了放置成功，如果单方块地物替换自身，则视为失败。这对于[聚合地物](#聚合地物)、[条件列表](#条件列表)等是一个重要区别。当仅考虑放置限制成功时，请使用带有[搜索地物](#搜索地物)的代理单方块地物。
:::

##### 天生方块条件

单方块地物可以允许由于方块的天生条件而在游戏中不允许的方块放置。

当 `"enforce_placement_rules"` 布尔值为真时，确保方块的天生放置检查必须成功才能放置方块；设置为假则忽略此检查。例如，种子通常只能放置在耕地上，但禁用此检查可以允许它们在任何地方生成。

此外，必需的 `"enforce_survivability_rules"` 布尔属性将切换方块的生存性检查是否成功。如果为假，将忽略方块的生存性条件。一个原版生存性示例是活珊瑚块需要相邻有水。

::: tip 注意
仅因为在世界生成时忽略了方块的生存性检查，并不意味着在游戏过程中它会保持其无效状态。方块更新将修正无效的方块生存性。
:::

##### 替换条件

<CodeHeader></CodeHeader>

```json
"may_replace": [
	"minecraft:air",
	"minecraft:leaves",
	"minecraft:leaves2"
]
```

单方块地物可以通过 `"may_replace"` 数组可选地指定**替换列表**，以限制目标方块可以替换的方块集合。如果单方块地物的[input position](#)处的方块不在此列表中，放置将失败。

::: warning
与[附着属性](#附着条件)不同，`"may_replace"`必须是一个数组。不能声明为直接的方块引用。
:::

##### 附着条件

<CodeHeader></CodeHeader>

```json
"may_attach_to": {
	"top": "minecraft:air",
	"sides": [
		"minecraft:planks",
		"minecraft:water"
	]
}
```

通过可选的 `"may_attach_to"` 属性提供的**附着规范**限制方块的邻接。每个可附着的侧面都有一个属性：

-   `"top"`
-   `"bottom"`
-   `"north"`
-   `"south"`
-   `"east"`
-   `"west"`

每个属性接受一个单独的直接方块引用或此类引用的数组：

<CodeHeader></CodeHeader>

```json
"bottom": {
	"name": "minecraft:stone",

	"states": {
		"stone_type": "andesite"
	}
}
```

<CodeHeader></CodeHeader>

```json
"top": [
	"minecraft:netherrack",
	"minecraft:soul_sand"
]
```

`"sides"` 属性可作为通配符，匹配 `"north"`、`"west"`、`"east"` 和 `"south"`。最后，`"all"` 属性匹配所有6个面。所有8个属性都是可选的，但至少应该指定一个。

对于侧面附着（`"north"`、`"south"`、`"east"`、`"west"`），还有2个可选属性可用于精细控制。

`"min_sides_must_attach"` 设置提供的侧面属性中成功附着的最小数量，如果设置为 `4`，则所有四个侧面必须匹配。如果设置为 `2` 且只有1个侧面匹配，方块放置将失败。

`"auto_rotate"` 使侧面定义被解释为相对关联而不是严格方向。例如，如果一个方块应该在一个方向在两个其他方块之间被横向挤压，但方向不重要，启用自动旋转并指定相对侧面将允许任何方向的工作。

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:single_block_feature": {
		"description": {
			"identifier": "wiki:force_conduit_block"
		},

		"places_block": "wiki:force_conduit",

		"enforce_placement_rules": true,
		"enforce_survivability_rules": true,
		"may_replace": ["minecraft:air"],
		"may_attach_to": {
			"north": "minecraft:glass",
			"south": "minecraft:glass",

			"auto_rotate": true
		}
	}
}
```

具体来说，上述代码中，强制导管块将被夹在相对侧面的相邻玻璃之间——无论朝向如何。

### 矿石地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:ore_feature": {
		"description": {
			"identifier": "wiki:starlite_ore_cluster"
		},

		"count": 4,
		"replace_rules": [
			{
				"places_block": "wiki:starlite_ore",
				"may_replace": ["minecraft:stone"]
			}
		]
	}
}
```

**矿石地物**在目标位置周围放置方块簇。矿石地物放置的方块通过[替换规则](#替换规则)变化。矿石地物中的**方块数量**是全局的，由 `"count"` 属性控制。

::: tip 注意
无法控制簇的形状；若要实现此目的，请使用具有[自定义分布系统](#)的[散布地物](#散布地物)。
:::

#### 替换规则

<CodeHeader></CodeHeader>

```json
"replace_rules": [
	{
		"places_block": "infinitum:exposed_pylon",
		"may_replace": [
			"minecraft:air"
		]
	},
	{
		"places_block": "infinitum:submerged_pylon",
		"may_replace": [
			"minecraft:water"
		]
	}
]
```

在矿石地物中，**替换规则**将目标方块绑定到限制目标放置的替换列表；这些规则通过 `"replace_rules"` 提供。**目标方块**是由替换规则放置的方块，通过必需的 `"places_block"` 属性提供；**替换列表**（通过 `"may_replace"`）是可选的数组，仅允许替换特定方块。为簇中的给定位置选择的方块将是第一个匹配规则的目标方块。如果未提供替换列表，该规则将在其位置始终成功，忽略所有未来的规则。

### 结构模板地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:structure_template_feature": {
		"description": {
			"identifier": "wiki:blackmoor_castle_feature"
		},

		"structure_name": "wiki:blackmoor_castle",

		"facing_direction": "random",
		"constraints": {
			"block_intersection": {
				"block_allowlist": [
					"minecraft:air",
					"minecraft:stone",
					"minecraft:dirt",
					"minecraft:grass"
				]
			},
			"unburied": {}
		},
		"adjustment_radius": 4
	}
}
```

**结构模板地物**通过引用保存的结构文件生成结构。这些地物为了方便而牺牲了一部分力量和灵活性。

::: warning
与数据驱动地物不同，结构地物中的方块如果放置在水中将不会自动水logged。
:::

**目标结构**通过 `"structure_name"` 字符串属性放置。该字符串遵循独特的命名系统，从行为包中选择 `.mcstructure` 文件；其形式为 `namespace:path`。结构文件必须放置在顶级 `structures` 目录中；从这里开始的任何文件夹层次结构都是允许的，但不是必需的。如果结构文件直接放置在 `structures` 目录中，默认命名空间为 `mystructure`。否则，如果放置在 `structures` 内的目录中，该目录名将用作命名空间。如果此目录内有任何嵌套，则会反映在路径中。最后，省略文件扩展名（`.mcstructure`）。

一些示例：

| 结构文件位置                                           | 关联的 `"structure_name"`             |
|:------------------------------------------------------|:--------------------------------------|
| `/structures/well.mcstructure`                        | `"mystructure:well"`                  |
| `/structures/farmstead/silo.mcstructure`              | `"farmstead:silo"`                    |
| `/structures/campsites/taiga/rustic/tents/wool.mcstructure` | `"campsites:taiga/rustic/tents/wool"` |

::: warning
[由于地物系统的限制](#)，大型结构可能需要预切割为较小的结构并一起定位。
:::

#### 旋转

<CodeHeader></CodeHeader>

```json
"facing_direction": "south"
```

**结构旋转**使用 `"facing_direction"` 属性进行，该属性接受四个横向方向：`"north"`、`"south"`、`"east"` 和 `"west"`，以及一个额外的 `"random"` 属性以在每次实例中随机选择它们。南是“默认”方向；使用此方向，结构向正 _x_ 和 _z_ 方向扩展。

::: warning
对于非南向的结构，并非所有方块状态都会更新以适应旋转，导致一些可旋转方块（如藤蔓）悬挂在无效位置。
:::

旋转从俯视视角顺时针进行。不幸的是，旋转围绕[结构原点](#)进行，而不是中心，因此由于[地物限制](#)，大型结构可能会在随机旋转时被切断。然而，使用固定旋转将以可靠的（尽管不方便的）方式定位。所有旋转从[地物原点](#)开始，并以以下方向生成：

| 旋转方向   | _x_ 投影       | _z_ 投影       | 从上方顺时针旋转 |
|:------------|:---------------|:---------------|:------------------|
| `"east"`    | 正              | 负              | 270°              |
| `"south"`   | 正              | 正              | 0°                |
| `"west"`    | 负              | 正              | 90°               |
| `"north"`   | 负              | 负              | 180°              |

因此，如果从原点（64, 64）生成一个7 × 6的地物，东旋转将占据从（64, 58）到（70, 65）的横向区域。

::: warning
由于旋转的处理方式，结构地物通常需要通过[加权随机地物](#加权随机地物)和[散布代理](#散布地物)进行代理以偏移位置。
:::

#### 约束

<CodeHeader></CodeHeader>

```json
"constraints": {
	"block_intersection": {
		"block_whitelist": [
			"minecraft:sand",
			"minecraft:sandstone",
			"minecraft:stone"
		]
	},
	"unburied": {},
	"grounded": {}
}
```

结构地物可以使用必需的 `"constraints"` 属性强制执行**约束**，以限制方块交叉、调整放置位置，并通过空气清理特征上方的空间。虽然属性及其对象 (`{}`) 是必需的，但所有子属性都是可选的。

##### 方块交叉

<CodeHeader></CodeHeader>

```json
"block_intersection": {
	"block_whitelist": [
		"minecraft:end_stone"
	]
},
```

结构可以替换的方块集合由**方块白名单**提供，通过 `"block_whitelist"`。如果结构尝试体积中的任何一个方块不在白名单中，结构将不会放置在该位置。如果未提供方块交叉，结构可以替换所有方块。

::: tip 注意
奇怪的是，`"block_whitelist"` 属性也可以与 `"block_allowlist"` 一起提供。两者功能相同。
:::

##### 地面附着

<CodeHeader></CodeHeader>

```json
"grounded": {}
```

可选的 `"grounded"` 组件确保结构的基座不会悬挂到开放空间——空气、水或熔岩中。结构底层的所有非结构空隙、非空气方块都被考虑；如果这些方块下方有空气、水或熔岩，即使只有一个，这些约束也会导致生成失败。

##### 顶部净空

<CodeHeader></CodeHeader>

```json
"unburied": {}
```

`"unburied"` 组件确保结构的顶部在生成时暴露在空气中。仅考虑结构顶部层的非结构空隙、非空气方块，且所有这些方块上方必须暴露在空气中才能成功生成结构。

::: tip 注意
与[地面附着](#地面附着)不同，暴露于水不被考虑。
:::

#### 放置调整

<CodeHeader></CodeHeader>

```json
"adjustment_radius": 4
```

为了适应可能严格的[约束](#约束)，可选的 `"adjustment_radius"` 属性可用；它接受从 `0`（默认）到 `16` 的值。在放置过程中，Minecraft 将从输入位置开始，向侧面辐射搜索，最多搜索此属性指定的方块数；不尝试垂直调整。每个对应的体积将被检查其有效性；[方块交叉](#方块交叉)、[地面附着](#地面附着)和[顶部净空](#顶部净空)都将被考虑。如果存在第一成功，则使用它。

::: tip
如果应使用垂直调整，请使用带有[搜索地物](#搜索地物)的代理结构地物。
:::

### 生长植物地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:growing_plant_feature": {
		"description": {
			"identifier": "wiki:bulbous_cerulon"
		},

		"body_blocks": [
			["wiki:bulbous_cerulon_stem", 1],
			["wiki:bulbous_cerulon_spiked_stem", 1]
		],
		"head_blocks": [
			["wiki:bulbous_cerulon_bulb", 1],
			["wiki:bulbous_cerulon_bulb_exposed", 1]
		],
		"age": { "range_min": 1, "range_max": 15 },

		"growth_direction": "up",
		"height_distribution": [[{ "range_min": 4, "range_max": 12 }, 1]]
	}
}
```

**生长植物地物**在末端放置头部方块的柱状体方块。两者都可以通过每个方块随机化进行精细调整。

::: tip
对于高级柱生成，请使用具有[固定网格分布](#网格分布)的[散布地物](#散布地物)。
:::

#### 柱体方块

<CodeHeader></CodeHeader>

```json
"body_blocks" : [
	["arctica:ice", 4],
	["arctica:ice_crystallized", 1]
],
"head_blocks" : [
	["arctica:growing_ice", 1]
],
"age": 3
```

生长植物分为**柱体方块**，构成大部分地物，以及**头部方块**，仅作为植物生成的最后一个方块。两者都作为**方块条目**的数组提供。每个方块条目是一个将方块引用绑定到整数[权重](#)的数组：

<CodeHeader></CodeHeader>

```json
["crestfallen:fungi_stem", 2]
```

每个方块独立地为柱体或头部选择。使用生长植物地物无法使所有柱体方块相同。

可选的 `"age"` 属性用于设置头部方块的年龄状态。它接受两种形式，一个整数和一个范围对象。当使用范围对象时，每次生成地物时，年龄将在提供的两个整数范围之间均匀随机选择。

整数：

<CodeHeader></CodeHeader>

```json
"age": 12
```

范围对象：

<CodeHeader></CodeHeader>

```json
"age": {"range_min": 4, "range_max": 8}
```

::: warning
年龄配置目前仅适用于洞穴藤蔓。
:::

#### 柱体生成

<CodeHeader></CodeHeader>

```json
"growth_direction": "down",
"height_distribution":  [
	[{"range_min": 8, "range_max": 12}, 4],
	[{"range_min": 4, "range_max": 8}, 2],
	[2, 1]
],
"allow_water": true
```

柱体从必需的 `"growth_direction"` 属性指定的垂直方向上，从地物原点生成，该属性接受 `"up"` 或 `"down"`。

生长植物地物的**最大**可能长度由 `"height_distribution"` 数组给出。与之前的[方块声明](#柱体方块)类似，高度分布中的每个条目是一个将高度绑定到权重的**高度条目**。高度可以是固定整数或[范围对象](#柱体方块)。

作为整数：

<CodeHeader></CodeHeader>

```json
[6, 3]
```

作为范围对象：

<CodeHeader></CodeHeader>

```json
[{ "range_min": 2, "range_max": 8 }, 1]
```

从高度分布中选择一个条目，根据[权重](#）选择，如果提供了范围，则在给定的限度之间均匀随机选择一个值。

生长植物地物从[input position](#)开始，并根据 `"growth_direction"` 向上或向下生成。默认情况下，仅替换生成的柱体中的空气。如果不在空气中开始，柱体生成将在正确方向上的第一个可用空气块处开始。由于途中非空气块导致的错过的方块机会不会被重新尝试。这意味着如果地物原点必须搜索通过两个非空气块才能到达空气，则高度将减少2。

到达（或开始于）空气后，柱体生成体块直到遇到非空气块，此时柱体生成永久停止。当然，当穿越确定的高度时也会停止生成。无论如何，柱体中的最后一个方块将是头部方块，即使柱体高度只有一个方块。

当 `"allow_water"` 布尔值为真时，允许第一个可用替换为水而不是空气。如果此属性为 `true` 且第一个水块上方未附着空气，则整个柱体仅生成一个头部方块；否则，柱体生成照常继续。

### 树地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:tree_feature": {
		"description": {
			"identifier": "wiki:grand_oak"
		},

		"base_block": ["minecraft:dirt", "minecraft:coarse_dirt"],
		"base_cluster": {
			"num_clusters": 4,
			"cluster_radius": 3,
			"may_replace": ["minecraft:air"]
		},

		"may_replace": ["minecraft:air"],

		"fancy_trunk": {
			"trunk_block": "minecraft:log",

			"trunk_height": {
				"base": 24,
				"variance": 9,
				"scale": 1
			},
			"trunk_width": 3,
			"width_scale": 2,

			"foliage_altitude_factor": 0.5,
			"branches": {
				"slope": 0.33,
				"density": 0.25,
				"min_altitude_factor": 0
			}
		},

		"fancy_canopy": {
			"height": 3,
			"radius": 4,
			"leaf_block": "minecraft:leaves"
		}
	}
}
```

**树地物**生成类似树形的形状。树地物允许比任何其他地物类型更高的自定义，包括：

-   设置木材和叶块
-   添加树面装饰
-   限制基础和交叉方块
-   自定义分支频率和角度

树地物由许多子属性组成，以反映原版游戏中各种树形的多样性。通常，这些属性分为[设置](#设置属性)、[干干属性](#干干属性)和[冠层属性](#冠层属性)。

#### 设置属性

<CodeHeader></CodeHeader>

```json
"base_block": [
	"minecraft:dirt",
	"minecraft:grass"
],
"base_cluster": {
	"may_replace": [

	],
	"num_clusers": 2,
	"cluster_radius": 3
},

"may_grow_on": [

],
"may_replace": [

],
"may_grow_through": [

]
```

使用**设置属性**指定树的基础和交叉方块。

#### 干干属性

**干干属性**建立树干和分支。

##### 树干

<CodeHeader></CodeHeader>

```json

```

##### 金合欢树干

<CodeHeader></CodeHeader>

```json

```

##### 精致树干

<CodeHeader></CodeHeader>

```json

```

##### 巨型树干

<CodeHeader></CodeHeader>

```json

```

##### 倾倒树干

<CodeHeader></CodeHeader>

```json

```

#### 冠层属性

树冠是使用**冠层属性**构建的。

##### 冠层

<CodeHeader></CodeHeader>

```json

```

##### 精致冠层

<CodeHeader></CodeHeader>

```json

```

##### 巨型冠层

<CodeHeader></CodeHeader>

```json

```

##### 云杉冠层

<CodeHeader></CodeHeader>

```json

```

##### 松树冠层

<CodeHeader></CodeHeader>

```json

```

##### 巨型松树冠层

<CodeHeader></CodeHeader>

```json

```

##### 金合欢冠层

<CodeHeader></CodeHeader>

```json

```

##### 屋顶冠层

<CodeHeader></CodeHeader>

```json

```

##### 随机扩展冠层

<CodeHeader></CodeHeader>

```json

```

### 多面地物

::: warning
多面地物目前存在漏洞，不应使用。最多只会放置2次——无论扩展几率如何。[散布地物](#散布地物)目前是可行的替代方案。
:::

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:multiface_feature": {
		"description": {
			"identifier": "wiki:decay_spread"
		},

		"places_block": "wiki:decay",

		"search_range": 8,
		"chance_of_spreading": 0.5,

		"can_place_on_ceiling": false,
		"can_place_on_floor": false,
		"can_place_on_wall": true,
		"can_place_on": [
			"minecraft:stone",
			"minecraft:deepslate",
			"minecraft:tuff"
		]
	}
}
```

多面地物根据序列中前一个元素的成功情况，随机在表面上放置方块序列。**表面**定义为空气或水与任何其他方块之间。

#### 扩展机制

<CodeHeader></CodeHeader>

```json
"search_range": 4,
"chance_of_spreading": 0.75
```

多面地物开始于尝试在多面地物的[input position](#)处放置**目标方块**（通过 `"places_block"` 属性）。对于每个后续尝试，将根据**扩展几率**进行一次掷骰。扩展几率通过 `"chance_of_spreading"` 浮点属性给出，范围从 `0`（永不成功）到 `1`（总是成功）。如果成功，下一个方块将在以 `"search_range"` 值为半边长的立方体内随机放置，立方体以[input position](#)为中心。序列继续，直到一个方块放置失败。搜索范围可以在 `1` 到 `64` 之间。

#### 放置限制

<CodeHeader></CodeHeader>

```json
"can_place_on_ceiling": true,
"can_place_on_floor": false,
"can_place_on_wall": true,
"can_place_on": [
	"minecraft:log",
	"minecraft:log2",
	"minecraft:leaves"
]
```

多面地物使用**放置限制**来限制方块附着。对于任何迭代（包括第一次），如果放置检查失败，序列将终止。3个必需的布尔属性控制目标可以放置的位置：

-   `"can_place_on_floor"`
-   `"can_place_on_ceiling"`
-   `"can_place_on_wall"`

当这些属性为真时，其对应的表面有资格附着。当然，至少一个属性必须为真，否则序列永远不会开始。

::: tip 注意
这些属性**不**决定方块状态，仅决定附着。多面方块，如火把，不会自动朝向适当的面。此外，如果目标方块支持同时附着到多个面，并且附着到这些属性白名单的面，它也可能自动附着到未列入白名单的面。
:::

可以通过 `"can_place_on"` 数组属性可选地提供可附着的方块白名单。省略此属性默认为允许所有方块附着。

## 代理地物

代理地物用于分组、排列或控制地物，包括其他代理地物。代理地物本身无法对世界生成产生直接影响。

因此，所有代理地物都必须指向一个或多个**目标地物**：由代理地物放置、重新排列或选择的地物。目标地物以字符串引用的形式表示，指向预期地物的标识符。

### 散布地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:scatter_feature": {
		"description": {
			"identifier": "wiki:flower_patch"
		},

		"places_feature": "wiki:flowers",

		"scatter_chance": {
			"numerator": 2,
			"denominator": 3
		},
		"iterations": "v.flower_patch.size = math.random_integer(6, 14); return math.random_integer(math.pow(v.flower_patch.size, 2) / 4, math.pow(v.flower_patch.size, 2) / 3);",

		"project_input_to_floor": true,
		"x": {
			"distribution": "gaussian",
			"extent": [0, "v.flower_patch.size"]
		},
		"z": {
			"distribution": "gaussian",
			"extent": [0, "v.flower_patch.size"]
		},
		"y": 0
	}
}
```

**散布地物**是最灵活且有用的地物类型。散布地物可以：

- 在[区块的地物域](#)内任意次数地分布或重新定位地物
- 作为门控，条件性地启用地物放置
- 在当前[地物上下文](#)中执行Molang

散布地物每次迭代尝试放置一个[目标地物](#proxy-features)：

<CodeHeader></CodeHeader>

```json
"places_feature": "lostlands:shimmerfields_spire"
```

目标地物的放置位置、位置方式和放置方式取决于[生成潜力](#generation-potential)、[分布](#distribution)和[评估顺序](#evaluation-order)。

#### 生成潜力

<CodeHeader></CodeHeader>

```json
"scatter_chance": 25,
"iterations": 12
```

散布地物将使用`"scatter_chance"`和`"iterations"`属性确定其目标地物的放置尝试。

**散布几率**代表散布地物成功的潜力。它可以表示为…

数值字面量：

<CodeHeader></CodeHeader>

```json
"scatter_chance": 12.5
```

::: warning
数值字面量形式是基于100而非1。因此，`50`的散布几率有一半的成功机会。
:::

Molang表达式：

<CodeHeader></CodeHeader>

```json
"scatter_chance": "1 / 8"
```

分数对象：

<CodeHeader></CodeHeader>

```json
"scatter_chance": {
	"numerator": 1,
	"denominator": 8
}
```

所有这三种示例的成功几率都是12.5%。根据具体情况选择最合适的形式。如果省略散布几率，默认散布地物尝试放置其目标的几率为100%。

**迭代次数**是散布地物尝试放置其目标的次数。如果散布地物的一个实例成功（换句话说，如果其散布几率检查通过），则将尝试`"iterations"`指定的所有迭代次数。迭代次数可以表示为整数字面量或Molang表达式。与散布几率不同，迭代次数是必需的。

#### 分布

<CodeHeader></CodeHeader>

```json
"x": {
	"distribution": "fixed_grid",
	"extent": [0, 15]
},
"z": {
	"distribution": "fixed_grid",
	"extent": [0, 15]
},
"y": 0
```

分布主要通过**坐标属性**处理：`"x"`、`"z"`和`"y"`。所有这些属性可以使用…

整数字面量：

<CodeHeader></CodeHeader>

```json
"x": 0
```

Molang表达式：

<CodeHeader></CodeHeader>

```json
"x": "math.random_integer(0, v.surface_grass.spread - 1)"
```

或使用多种对象形式方便地分配坐标：

<CodeHeader></CodeHeader>

```json
"x": {
	"distribution": "uniform",
	"extent": [0, 16]
}
```

字面量和Molang表达式相对于[地物原点](#)。参见[分布类型](#distribution-types)了解可用的预构建分布系统。

由于地物放置通常相对于高度图，因此散布地物的输入**y**原点可以**投影到地面**：

<CodeHeader></CodeHeader>

```json
"project_input_to_floor": true
```

这意味着散布地物父级指定的**y**原点将被忽略，取而代之的是高度图在每次迭代的**x-z**位置的**y**坐标（[假设**y**坐标将在横向坐标之后计算](#evaluation-order)）。`"y"`属性仍然可以给定一个值，表示相对于高度图的偏移量。

::: tip 注意
在功能上，这与使用Molang表达式`"q.heightmap(v.worldx, v.worldz) + *offset*"`相同。
:::

##### 分布类型

可以使用Molang表达式构建自定义分布系统，但散布地物预装了一些常见的**分布类型**，以便于创作：

- 均匀分布
- 高斯分布
- 逆高斯分布
- 固定网格分布
- 抖动网格分布

每种分布类型都需要一个**范围**，表示该分布操作的值范围，从最小值到最大值。范围与基本的坐标声明形式一样，相对于[地物原点](#)。

###### 均匀分布

<CodeHeader></CodeHeader>

```json
"z": {
	"distribution": "uniform",
	"extent": ["v.boulder_spread.start", "v.boulder_spread.end"]
}
```

**均匀分布**是在两个值之间的半开区间上进行均匀随机分布。之所以称为“均匀”，是因为范围内的每个值被选中的机会相等；称为“半开”，因为范围的最小值是区间的成员，而最大值则不是：

_最小范围_ <= _x_ < _最大范围_

因此，如果均匀分布的范围为`[0, 16]`，块可以放置在大小为16的范围内：从0到15。第一个可能的位置从0开始，第15个可能的位置结束于16，与范围匹配。

###### 高斯分布

<CodeHeader></CodeHeader>

```json
"y": {
	"distribution": "gaussian",
	"extent": [0, "2 * v.vine_cluster.radius"]
}
```

**高斯分布**（`"gaussian"`）及其**逆分布**（`"inverse_gaussian"`）有助于将地物聚集到范围的中心或远离中心。高斯分布非常极端，通常不会选择远离中心的值，而逆高斯分布几乎不会选择接近中心的值。高斯分布的范围行为与[均匀分布](#uniform-distribution)相同。

###### 网格分布

<CodeHeader></CodeHeader>

```json
"x": {
	"distribution": "jittered_grid",
	"extent": [0, 15],
	"step_size": 2,
	"grid_offset": 4
}
```

**网格分布**是一种强大的系统，用于将块放置在坐标上的等间距区间内，或在这些区间内随机分布。与其他分布类型不同，网格的范围形成一个包括最大范围的区间：

_最小范围_ <= _x_ <= _最大范围_

网格分布仅提供两个属性以更精细地控制所使用的网格系统。步长（默认值为1）可以通过`"step_size"`属性进行自定义。初始偏移量（默认值为0）也可以通过`"grid_offset"`属性提供。

如果迭代计数结合步长和偏移量将坐标推到最大范围之外，则坐标将回绕到最小范围并从那里继续。

虽然网格在独立坐标上很有用，但它们的真正力量在于与其他坐标上的网格分布相结合时表现出来。放置优先考虑先评估的网格系统的增量，只有在先前的网格系统回绕时才考虑后续的系统。当先前评估坐标的放置回绕时，下一个评估的基于网格的坐标将根据发生的回绕次数进行偏移。

举个简单的例子：

<CodeHeader></CodeHeader>

```json
"iterations": 21,

"x": {
	"distribution": "fixed_grid",
	"extent": [0, 15]
},
"z": {
	"distribution": "fixed_grid",
	"extent": [0, 15]
}
```

放置首先在_x_方向开始：（0, 0）、（1, 0）等，直到范围结束于（15, 0）。然而，只有16次迭代中的21次已经完成；还剩下5次。现在，_x_坐标回绕到0，同时_z_坐标增至1：（0, 1）。

这种回绕在三维中也是如此，因此当最早评估的坐标系的平面回绕时（假设迭代次数足够高），另一个平面将根据最终坐标的步长开始形成。

::: warning
当0不在范围内时，网格范围会表现出意想不到的方式。特别是，范围将被最接近的边界投影到0。例如，给定范围`[-7, -2]`将被重新映射为`[-5, 0]`。`[13, 21]`将被重新映射为`[0, 8]`。因此，建议仅将范围指定为长度，例如在后一个示例中使用`[0, 8]`，并使用另一个散布地物通过字面量`13`定位该坐标。
  
当使用多个网格分布来形成一个表面或体积时，任何会扩展到`0`以下的坐标范围在该坐标的第一次传递中才能使用。后续的传递将仅限于非负值。
:::

#### 评估顺序

当包含散布几率时，它在任何其他属性之前被评估。如果该散布地物的实例的散布几率检查失败，则该实例内的下游内容不被评估。不会进一步解释Molang；[地物上下文](#)中的变量也不会被更新。目标地物将被完全忽略。

接下来，评估迭代次数。类似于散布几率，如果迭代次数未能解析为正数的放置尝试次数，则不会进一步评估。

接下来，每次迭代都会尝试，无论早期迭代是否因某种原因失败。对于每次迭代，每个坐标都会使用相同的顺序进行评估。

::: warning
坐标评估的顺序**不**依赖于JSON中声明坐标属性的顺序。
:::

默认情况下，坐标顺序为_x_，然后_z_，然后_y_。这涵盖了大多数用例：如果坐标不是独立的，很可能垂直位置依赖于横向坐标。然而，散布地物可以声明非典型的**坐标评估顺序**，以完全控制坐标依赖性：

<CodeHeader></CodeHeader>

```json
"coordinate_eval_order": "zyx"
```

在确定一次迭代的坐标后，世界生成将其焦点转移到目标内：认可其限制，尝试放置，评估其Molang，并（如果可能且相关）继续放置其子地物及其子地物，以此类推。

完成目标地物树的处理后，如果散布地物还有更多迭代未运行，焦点将返回到散布地物，从第一个评估的坐标开始并继续执行。

### 条件列表

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:conditional_list": {
		"description": {
			"identifier": "wiki:columns_selection"
		},

		"conditional_features": [
			{
				"places_feature": "wiki:columns_unweathered",
				"condition": "q.noise(v.originx, v.originz) < 0"
			},
			{
				"places_feature": "wiki:columns_weathered",
				"condition": 1
			}
		],

		"early_out_scheme": "placement_success"
	}
}
```

**条件列表**根据条件从集合中选择单个地物；它们类似于编程语言中的“if-else if”块。一旦条件被评估为成功（通过[成功判定](#success-determination)确定），条件列表将仅选择**该一个地物**进行放置。

::: tip 注意
如果希望_每个_成功都在同一位置放置一个地物，请使用指向[散布地物](#scatter-features)的[聚合地物](#aggregate-features)，以代理目标地物。
:::

#### 条件列表

<CodeHeader></CodeHeader>

```json
"conditional_features": [
	{
		"places_feature": "summer_fun:beachadjustment_water",
		"condition": "q.heightmap(v.originx, v.originz) < 63 && q.noise(v.originx, v.originz) < 0"
	},
	{
		"places_feature": "summer_fun:beachadjustment_coral",
		"condition": "q.heightmap(v.originx, v.originz) < 63 && q.noise(v.originx, v.originz) >= 0"
	},
	{
		"places_feature": "summer_fun:beachadjustment_air",
		"condition": 1
	}
]
```

**条件列表**，`"conditional_features"`，是一个有序数组，由**地物条目**对象组成。地物条目将[**目标地物**](#proxy-features)绑定到其**条件**：

<CodeHeader></CodeHeader>

```json
{
	"places_feature": "verona:evergreen_trees_stumps",
	"condition": "v.evergreen_forest.type == v.evergreen_forest.types.lumberjack_ruined"
}
```

条件通过必需的`"condition"`属性给出。条件通常通过Molang字符串表示，但也可以使用数字。`0`将始终导致该地物条目被禁用。非零值将始终导致该条目成功。通常，使用`1`可以被视为一个捕获所有的“else”或“默认”子句——它应该仅在条件列表的最后使用。

每个地物条目的条件按条件列表中的条目顺序进行评估。一旦某个地物条目[成功](#success-determination)，后续列表中的条件将不再被评估。

#### 成功判定

<CodeHeader></CodeHeader>

```json
"early_out_scheme": "placement_success"
```

地物条目的成功取决于可选的**提前退出方案**。提供了两种机制来控制地物条目是否成功。`"condition_success"`——如果未提供`"early_out_scheme"`，则使用默认值——当条件评估为true时，视为成功。`"placement_success"`进一步要求条件必须为true，且其目标地物的放置必须成功。

### 聚合地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:aggregate_feature": {
		"description": {
			"identifier": "wiki:village_center"
		},

		"features": [
			"wiki:village_center_well",
			"wiki:village_center_grass_path"
		],
		"early_out": "first_failure"
	}
}
```

**聚合地物**在输入位置依次放置给定列表中的地物。聚合地物通常用于构建由许多不同地物组成的自定义场景。

聚合地物要放置的地物由必需的**地物列表**给出。此列表中的每个地物——[如果被放置](#placement-escape)——将按声明顺序在同一位置放置。聚合地物通常需要指向[散布地物](#scatter-features)，以定位场景的元素。

#### 放置逃逸

<CodeHeader></CodeHeader>

```json
"early_out": "first_success"
```

默认情况下，地物列表中的每个条目都将尝试被放置。通过`"early_out"`属性提供了**放置逃逸**机制，它接受3个值：

| 值                 | 描述                                                      |
|:-------------------|:---------------------------------------------------------|
| `"none"`           | 尝试放置每个地物（默认）                                  |
| `"first_success"`  | 一旦第一次成功放置地物后停止放置                          |
| `"first_failure"`  | 一旦第一次放置失败后停止放置地物                          |

### 序列地物

::: warning
序列地物目前存在错误，不应使用。目前，地物列表中的所有地物都在相同的输入位置生成，类似于[聚合地物](#aggregate-features)。
:::

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:sequence_feature": {
		"description": {
			"identifier": "wiki:totem_pole"
		},

		"features": [
			"wiki:totem_pole_base",
			"wiki:totem_pole_body",
			"wiki:totem_pole_head"
		]
	}
}
```

**序列地物**在空间序列中放置一组地物。

地物通过**地物列表**进行排序，由`"features"`属性给出。前一个地物的输出位置成为下一个地物的输入位置。例如，如果序列地物的原点位于（0, 67, 0），且第一个列出的地物是垂直延伸10个块的柱子，则下一个列出地物的输入位置将是（0, 77, 0）。

### 对齐到表面地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.16.0",

	"minecraft:snap_to_surface_feature": {
		"description": {
			"identifier": "wiki:underground_silas_plant_snap"
		},

		"feature_to_snap": "wiki:underground_silas_plant",

		"surface": "floor",
		"vertical_search_range": 12
	}
}
```

地物可以通过**对齐到表面地物**固定到地板或天花板。目前，通过`"feature_to_snap"`指定的**目标地物**只能通过空气投射到实心表面。

#### 表面搜索

<CodeHeader></CodeHeader>

```json
"surface": "ceiling",
"vertical_search_range": 16
```

对齐到表面地物实际上将输入的_y_坐标重新映射到可用的表面。这**目标表面**通过可选的`"surface"`属性给出，该属性接受`"floor"`或`"ceiling"`，默认为`"floor"`。重新映射的过程是从[地物原点](#)开始，垂直向下（如果目标是地板）或向上（如果目标是天花板）搜索表面，这个表面似乎必须是实心块。

::: warning
地物原点必须从空气开始（即使只有一个块），否则表面搜索将立即失败。
:::

应搜索的距离通过必需的`"vertical_search_range"`属性给出，没有合理的限制。不幸的是，实际范围不是特别直观。范围行为类似于该值减去2。例如，从_y_为70并使用搜索范围为`5`时，可以在67到70之间放置地物。如果从48开始向天花板搜索，并使用范围`6`，则地物可以放置在48到52之间。

### 搜索地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:search_feature": {
		"description": {
			"identifier": "wiki:search_feature"
		},

		"places_feature": "wiki:search_feature_obsidian",

		"search_volume": {
			"min": [0, 0, 0],
			"max": [7, 7, 7]
		},

		"search_axis": "y",
		"required_successes": 512
	}
}
```

**搜索地物**在一个体积内搜索有效的放置位置以放置目标地物。这些地物是定位具有挑战性放置条件的地物的理想选择。

**目标地物**通过`"places_feature"`属性放置。其放置成功取决于是否在[搜索体积](#search-volume)内达到[成功阈值](#search-specifications)。在放置发生之前，会依次检查目标地物在体积内每个位置的放置条件。

#### 搜索体积

<CodeHeader></CodeHeader>

```json
"search_volume": {
	"min": [-12, 0, -12],
	"max": [11, 11, 11]
},
```

**搜索体积**声明搜索将发生的空间。两个向量定义了此体积的边界：`"min"`指向具有最低坐标的角，`"max"`指向棱柱对角面的块原点。因此，最大角的坐标在每个维度上延伸比`"max"`向量多1块。例如，以下搜索体积实际上覆盖了8个块（每个维度2块），而不是1：

<CodeHeader></CodeHeader>

```json
"search_volume": {
	"min": [0, 0, 0],
	"max": [1, 1, 1]
},
```

这些向量仅接受数字，并相对于[地物原点](#)。

#### 搜索规格

<CodeHeader></CodeHeader>

```json
"search_axis": "z",
"required_successes": 16
```

在给定的搜索体积内，位置按`"search_axis"`属性进行分层检查，该属性接受`"+x"`、`"-x"`、`"+y"`、`"-y"`、`"+z"`或`"-z"`。在指定搜索轴层内，其它维度将在网格中检查，直到达到各自的边界，然后再检查下一个搜索轴层。具体来说，检查的坐标顺序是：

- 不是搜索轴的最早的_x_或_y_
- 不是搜索轴的最早的_y_或_z_
- 指定的搜索轴

只有当在扫描搜索体积时找到的成功次数达到可选的`"required_successes"`属性时，地物才会被放置。如果省略该属性，整个体积中只需找到一次成功即可放置地物。

#### 搜索过程

搜索从相对于[地物原点](#)的[最小向量](#search-volume)位置开始。根据[搜索轴](#search-axis)的确定，逐个坐标更新位置。当某个坐标达到其最大值时，位置将回绕到下一个坐标的开始；如果在搜索轴上迭代，将考虑指定的方向（`+`或`-`）。在每个位置，检查[目标地物](#search-features)固有的搜索条件。一旦找到的成功次数达到[成功阈值](#search-specifications)（如果未提供阈值，则找到一次成功），目标地物将在**所有**这些成功的位置放置。在达到阈值之前，不会放置任何地物。

### 矩形布局

::: warning
矩形布局目前存在错误，不应使用。尚未提供其工作方式的任何信息。大概，矩形布局将区块的表面积划分为`"area_dimensions"`指定的矩形，并根据声明的空闲空间比例放置其关联的地物。
:::

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:rect_layout": {
		"description": {
			"identifier": "wiki:garden_maze"
		},

		"ratio_of_empty_space": 0.5,
		"feature_areas": [
			{
				"feature": "wiki:flower_patch",
				"area_dimensions": [2, 4]
			},
			{
				"feature": "wiki:garden_hedge",
				"area_dimensions": [1, 3]
			}
		]
	}
}
```

### 扫描表面地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:scan_surface": {
		"description": {
			"identifier": "wiki:fallen_leaves_cover"
		},

		"scan_surface_feature": "wiki:fallen_leaves"
	}
}
```

每个区块的表面上的每个块都可以通过地物使用**扫描表面地物**进行覆盖。因此，强烈建议选择仅占据区块空间的地物。

**目标地物**通过`"scan_surface_feature"`属性给出。放置位置与[Molang查询`heightmap`](#)相同，这意味着使用水面而非地面。因此，通常建议使用_y_表达式利用[`above_top_solid`查询](#)的[散布地物](#scatter-features)。

### 加权随机地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:weighted_random_feature": {
		"description": {
			"identifier": "wiki:gelatin"
		},

		"features": [
			["wiki:gelatin_green", 3],
			["wiki:gelatin_red", 3],
			["wiki:gelatin_blue", 2],
			["wiki:gelatin_purple", 1]
		]
	}
}
```

**加权随机地物**从列表中随机选择一个地物。它们通常用于在一组相关地物中提供变化。

加权随机地物从其**加权地物列表**中选择。列表中的每个条目都是由地物引用和整数权重组成的数组。每次运行加权随机地物时，可以选择不同的地物。

::: tip 注意
要了解权重的工作方式，请参见[概率相关部分](#)。
:::

## 场景地物

场景地物是一种内容地物和代理地物的组合。它们是围绕原版生成所需美学设计的地物类型。

场景地物仅允许对其形状进行最小的自定义，以实现其预期的美学。与内容地物类似，它们的方块可以方便地修改；与代理地物类似，它们可以在内部墙壁上放置自己的子地物。

### 晶体地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",
	"minecraft:geode_feature": {
		"description": {
			"identifier": "wiki:wasp_hive"
		},

		"max_radius": 12,

		"filler": "minecraft:air",

		"inner_layer": "wiki:wasp_hive_inside",
		"alternate_inner_layer": "wiki:wasp_hive_spawner_base",
		"use_alternate_layer0_chance": 0.125,

		"middle_layer": "wiki:wasp_hive_inside",

		"outer_layer": "wiki:wasp_hive_shell",

		"inner_placements": ["wiki:wasp_hive_spawner"],
		"placements_require_layer0_alternate": true,
		"use_potential_placements_chance": 1,

		"min_distribution_points": 2,
		"max_distribution_points": 4,
		"min_outer_wall_distance": 2,
		"max_outer_wall_distance": 4,
		"min_point_offset": 0,
		"max_point_offset": 2,
		"noise_multiplier": 0.125,
		"invalid_blocks_threshold": 64,

		"crack_point_offset": 0,
		"generate_crack_chance": 1,
		"base_crack_size": 1
	}
}
```

**晶体地物**构建由多个方块层组成的球形结构；它们允许在内部墙壁上放置子地物。

### 胡须与剃刀

::: warning
胡须与剃刀目前存在错误，应避免使用。特别是，该平台构造不佳，表面方块通常在错误的层上生成，形状被切割得很尴尬。
:::

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:beards_and_shavers": {
		"description": {
			"identifier": "wiki:highland_tower_foundation"
		},

		"places_feature": "wiki:highland_tower",
		"y_delta": 0,

		"bounding_box_min": [-4, 0, -4],
		"bounding_box_max": [5, 12, 5],
		"beard_raggedness_min": 0.25,
		"beard_raggedness_max": 0.5,

		"surface_block_type": "minecraft:grass",
		"subsurface_block_type": "minecraft:dirt"
	}
}
```

**胡须与剃刀**同时提供了一个平台（胡须）和一个清理空间（剃刀）供地物生成。

### 植被补丁地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:vegetation_patch_feature": {
		"description": {
			"identifier": "wiki:shiitake_patch"
		},

		"horizontal_radius": 4,
		"extra_edge_column_chance": 0.5,

		"surface": "floor",
		"vertical_range": 5,

		"ground_block": "minecraft:mycelium",
		"replaceable_blocks": ["minecraft:dirt", "minecraft:grass"],
		"depth": 4,
		"extra_deep_block_chance": 0.5,

		"vegetation_feature": "wiki:shiitake_mushroom",
		"vegetation_chance": 0.125
	}
}
```

**植被补丁**在方形边界（补丁）内放置子地物（通常是植被）。

植被补丁基本上执行四个操作：

-   从给定半径确定横向补丁形状
-   从每个方块的[输入位置](#)垂直搜索表面（天花板或地板）
-   将方块列放置到表面上
-   在创建的补丁内随机生成子地物

#### 补丁形状

<CodeHeader></CodeHeader>

```json
"horizontal_radius": 3,
"extra_edge_column_chance": 0.25
```

植被补丁首先构建补丁的横向形状。该形状以[输入位置](#)的_x_和_z_为中心。从这里，所需的`"horizontal_radius"`指定初始形状在所有横向方向上应延伸多远。该形状不使用[出租车距离](#)；相反，角落被填充，构建一个简单的正方形。该正方形的大小由以下公式给出：

_横向半径_ \* 2 + 1

因此，横向半径为4将生成一个边长为9的正方形，中心位于输入_x_和_z_。

补丁形状可以通过可选的`"extra_edge_column_chance"`属性进行轻微随机化。该属性接受介于`0`（默认值）和`1`之间的值，表示外围任何方块被包含在补丁形状中的几率。这些外围方块不包括外周角落。如果忽略角落，将该属性设置为`1`相当于将横向半径增加1。

#### 补丁搜索

<CodeHeader></CodeHeader>

```json
"surface": "ceiling",
"vertical_range": 8
```

植被补丁然后在确定的补丁形状内搜索每一列，从[输入位置](#)的_y_分量垂直查找适当的表面，给定可选的`"surface"`属性。可以提供`"floor"`（如果未指定则为默认值）或`"ceiling"`。表面搜索仅对空气有效；不能使用其他方块的对比。然而，搜索可以从任何方块内开始。

搜索的距离由`"vertical_range"`给出，这是必需的且没有实际限制。搜索是双向进行的。例如，如果从_y_为70开始，使用垂直范围为`5`，则65到75之间的表面都将成功。

在一列中，范围内的第一个匹配表面将被使用。当目标为地面表面时，第一个匹配是最高的表面；如果目标为天花板，则第一个匹配是最低的表面。

#### 补丁列放置

<CodeHeader></CodeHeader>

```json
"ground_block": "arabia:lush_sand",
"waterlogged": true,
"replaceable_blocks": [
	"minecraft:sand",
	"minecraft:sandstone"
],
"depth": 2,
"extra_deep_block_chance": 0.75
```

在每个表面搜索成功的列中尝试生成补丁列。列是程序生成的，从输入位置开始，继续向表面延伸。

构成补丁固体基础的方块由`"ground_block"`给出。其在表面中的长度由`"depth"`给出。如预期，深度为`0`将不会生成任何作为补丁列的一部分的方块，但负值将生成一个列，直到达到非白名单方块为止。

可选的`"extra_deep_block_chance"`属性为每列提供了尝试生成额外方块的几率，使该列的深度增加1。它的值介于`0`和`1`之间（包括0），默认为0。将该属性设置为`1`的效果与将深度增加1相同。

::: tip 注意
[垂直范围](#patch-search)在搜索阶段后对生成没有进一步影响。如果一列刚好在搜索范围内，其整个深度仍将被尝试。此外，如果某个表面超出垂直范围，但该列中的方块在范围内，则这些方块仍将被忽略。放置从表面开始，向下进行，当目标为[地面表面](#patch-search)时，反之亦然。
:::

必须通过`"replaceable_blocks"`属性提供方块白名单。在生成补丁列时，每个方块按顺序检查并放置。如果检测到非白名单方块，则该列的生成将停止。因此，列可能无法达到其目标深度。单个列的生成失败对其他列没有影响。

最后，可选的布尔值`"waterlogged"`属性在设置为true且`"surface"`为`"floor"`时，尝试用水替换补丁列中的最上方块。因此，水将在表面上暴露于空气中。如果其一个侧面与空气相连，则不会替换水，以防止水溢出。如果省略`"waterlogged"`，则默认禁用水生成。当`"depth"`为`0`且启用水浸时，未列入白名单的方块仍可能被替换为水。对于所有其他深度值，只有白名单方块才会被替换为水。

#### 植被放置

<CodeHeader></CodeHeader>

```json
"vegetation_feature": "tension:shiitake_mushroom",
"vegetation_chance": 0.125
```

最后，植被补丁采用一个植被地物和相应的生成几率，在补丁的表面随机位置放置子地物。子地物由必需的`"vegetation_feature"`属性给出。每个生成的表面方块都有机会支持此植被地物。

::: warning
与表面相连的多层植被地物仍会自然向上生成。它们必须以某种方式构建或代理，以便从天花板向下生成。
:::

任何方块表面被选为子地物输入位置的几率由可选的`"vegetation_chance"`浮点属性给出，默认为`0`。与植被补丁地物中的其他几率一样，它的范围从0到1（包括0），其中`0`将生成零个子地物，而`1`将尝试为每个表面方块生成一个。要注意跨越多个列的植被地物；可能会发生碰撞，将单个地物聚集成一个整体。

对于[地面绑定](#patch-search)的补丁，如果[`"waterlogged"`](#patch-column-placement)为`false`，植被地物直接在表面上生成，并有可能在表面边缘生成。然而，如果启用水浸，植被地物不能在表面边缘生成，但可以在水中生成，如果支持则会用水浸泡该方块。当[`"depth"`](#patch-column-placement)为`0`时，即使没有补丁方块支持它们，子地物仍然可以被放置。

::: warning
如果在目标为天花板的植被补丁地物上启用了水浸，则不会放置任何植被地物。
:::

## 切割地物

切割地物是用于修改原版洞穴生成的特殊地物类型。目前，使用切割器的自定义选项很少。切割器仅包括经典的意大利面洞穴，而不包括峡谷或结构。

所有切割地物都需要在[预生成阶段](#)中放置。因此，切割地物无法通过任何方式与其他地物结合，甚至不能通过代理。

切割器通过在预定路径周围剔除方块来工作；这些路径是不可更改的。相反，切割地物允许自定义**宽度修饰符**，该修饰符添加到游戏提供的基础宽度变化中。该属性在所有切割地物中都可用，称为`"width_modifier"`。宽度修饰符仅影响切割路径周围的横向距离，而不影响高度。负值的行为与正常减法相同：缩小切割器而不是扩张；足够低的值（约`-16`）可以用于原版切割器以移除洞穴。

::: warning
尽管在地物架构中列为可选，但`"width_modifier"`应始终提供；否则将不断抛出错误，整个区块将出现损坏。此外，不应使用大值的宽度修饰符（大于约`16`）：世界加载速度会变得极慢，区块可能会被完全剔除。
:::

切割器实际上并不真正“剔除”方块；相反，它们用**填充方块**替换现有方块（例如来自生物群系表面生成器或先前放置的切割器）。填充方块可以通过可选的`"fill_with"`属性提供，默认值取决于切割器类型；该属性同样适用于所有切割地物类型。

::: warning
切割器的方块交集集目前无法自定义。只有特定于每种切割器类型的原版方块会被替换；自定义方块无法被剥离以形成洞穴。
:::

### 洞穴切割地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:cave_carver_feature": {
		"description": {
			"identifier": "wiki:massive_cave"
		},

		"width_modifier": 4
	}
}
```

经典的下界洞穴系统由**洞穴切割地物**控制。这些切割器仅在下界中使用。

下界洞穴自然从床岩层上方的_y_-3延伸到超过100的任意_y_值。如果省略，洞穴切割地物的填充方块默认为空气。洞穴切割地物会剥离典型的下界表面和基础方块，例如石头变体、泥土变体、沙子变体和砂岩。然而，水不会被剔除，海洋和河流中的水会被积极避免。

### 水下洞穴切割地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:underwater_cave_carver_feature": {
		"description": {
			"identifier": "wiki:underwater_thick_caves"
		},

		"width_modifier": 8
	}
}
```

**水下洞穴切割地物**在下界较低的高度生成洞穴——低于63的海平面。这些切割器也仅在下界中工作。水下切割器接受一个额外的可选属性`"replace_air_with"`，旨在用给定方块替换预先存在的空气交集。

::: warning
该属性目前似乎无法正常工作。在测试中，无论是作用于基础为空气的生物群系，还是与先前放置的[洞穴切割地物](#cave-carver-feature)交集的空气，交集的空气都未能成功替换。
:::

水下切割器用与[洞穴切割地物](#cave-carver-features)相同的自然原版方块替换，唯一的补充是水。这意味着可以在水下环境中用填充方块构建螺旋状的结构。水下切割器可以从高度3开始；即使有机会这样做，它们也不会在_y_-63（下界海平面）以上运行。

::: warning
水下洞穴切割器在自定义生物群系中无法正常工作——即使该生物群系使用原版方块。
:::

### 地狱洞穴切割地物

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.13.0",

	"minecraft:hell_cave_carver_feature": {
		"description": {
			"identifier": "wiki:nether_caves"
		},

		"fill_with": "minecraft:magma",
		"width_modifier": 1
	}
}
```

地狱洞穴通过**地狱洞穴切割地物**形成。令人惊讶的是，这些切割器可以在下界和下界中使用；必须对地物规则应用[生物群系过滤器]()以限制这种情况。

地狱切割器从_y_为5延伸到121，其填充方块默认为空气。地狱切割器剥离与[洞穴切割地物](#cave-carver-features)相同的一组方块，但有几个例外：地狱切割器不会剥离沙子变体或砂岩，但会移除下界土和水。