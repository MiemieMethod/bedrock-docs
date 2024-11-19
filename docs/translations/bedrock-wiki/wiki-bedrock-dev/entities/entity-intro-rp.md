---
title: 实体资源包简介
category: 一般
nav_order: 2
tags:
    - 指南
    - 初学者
mentions:
    - SirLich
    - MedicalJewel105
    - Overload1252
    - ChibiMango
    - Luthorius
    - TheItsNameless
    - SmokeyStack
    - ThomasOrs
description: 实体资源包简介。
---

资源包实体文件包含了构成我们实体视觉效果的资产引用。此外，它还包含了如何以及何时渲染这些视觉效果的信息。

本页将逐步解析实体文件的每个部分并解释每个部分。有关创建你自己实体的详细指南，请查看我们的[初学者指南](../guide/custom-entity.md)。

## 文件大纲

```json title="RP/entity/example.json"
{
    "format_version": "1.10.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "wiki:example",
            "materials": {...},
            "textures": {...},
            "geometry": {...},
            "render_controllers": [...],

            "animations": {...},
            "scripts": {...},

            "sound_effects": {...},
            "particle_effects": {...},

            "spawn_egg": {...},
            "enable_attachables": false,
            "hide_armor": false
        }
    }
}
```

虽然看起来可能有些复杂，但许多部分只是*短名称定义*。短名称定义是我们将资产（如纹理路径或几何体标识符）分配给短名称的地方，之后我们可以在其他地方引用。这意味着如果我们稍后更改资产的位置，只需更改一个地方。此外，它还使我们的代码更简洁，无需写出冗长的路径位置或标识符。

## 材料
材料描述了纹理的渲染方式。例如，骷髅有一种材料使其纹理透明，而末影人有一种材料使其眼睛发光。你可以使用许多现成的材料，而无需自己制作。

```json title="RP/entity/spider.entity.json#minecraft:client_entity/description"
"materials": {
    "default": "spider",
    "invisible": "spider_invisible"
}
```
这里的材料是`spider`和`spider_invisible`，短名称分别是`default`和`invisible`。请记住，这个键只是*定义*了附加到短名称的材料，我们的实体仍然不知道何时使用每一个。
有关现成材料的列表，请查看我们的页面[这里](../documentation/materials.md)。
有关制作你自己材料的指南，请查看此[页面](../visuals/materials.md)。请注意，这相对较为高级。

## 纹理
纹理是映射到我们几何体上的图像。每个实体都有不同的纹理。与材料类似，这个键也是一个短名称定义，但这里的引用是纹理的路径。

```json title="RP/entity/bee.entity.json#minecraft:client_entity/description"
"textures": {
    "default": "textures/entity/bee/bee",
    "angry": "textures/entity/bee/bee_angry",
    "nectar": "textures/entity/bee/bee_nectar",
    "angry_nectar": "textures/entity/bee/bee_angry_nectar"
}
```
如前所述，我们可以定义多个纹理。如果我们想要不同变体的实体，这将非常有用，比如上面的蜜蜂。此外，我们可以使用多个纹理在不同的基础上叠加不同的纹理，就像村民有不同的生物群落基础和不同的职业层次一样。你可以查看我们关于渲染控制器的页面[这里](../entities/render-controllers.md)，了解有关如何叠加纹理的更多细节。

## 几何体
几何体是一个定义组成我们实体形状的*骨骼*集合的文件。你可以使用像Blockbench这样的应用程序自动创建此文件。有关如何制作你自己模型的更多详细信息，请查看我们的[指南](../guide/blockbench.md)。

```json title="RP/entity/creeper.entity.json#minecraft:client_entity/description"
"geometry": {
    "default": "geometry.creeper",
    "charged": "geometry.creeper.charged"
}
```
这里我们的短名称引用了几何体的标识符。

```json title="RP/entity/creeper.entity.json#minecraft:client_entity/description"
{
	"format_version" : "1.12.0",
	"minecraft:geometry" : [
		{
			"description" : {
				"identifier" : "geometry.creeper",
                ...
            }
        }
}
```
同样，我们可以有多个几何体，例如苦力怕有两个模型，分别用于充能和非充能形态。

:::tip
如果你在视觉效果上遇到问题，可能是因为实体的短名称有拼写错误。请确保仔细检查。
:::

## 渲染控制器
渲染控制器简单地控制你的实体将如何被渲染。此文件使用材料、纹理和几何体的短名称，并通过它们定义何时渲染每个元素。

```json title="RP/render_controllers/example.rc.json"
{
	"format_version": "1.10.0",
	"render_controllers": {
		"controller.render.example": {
			"geometry": "geometry.default",
			"materials": [
				{
					"*": "material.default"
				}
			],
			"textures": ["texture.default"]
		}
	}
}
```
这里，这个渲染控制器表示始终使用`default`材料、纹理和几何体。你可以创建更复杂的渲染控制器，允许切换纹理或使几何体的某些部分不可见。有关更多信息，请参阅我们的渲染控制器页面[这里](../entities/render-controllers.md)。

要告诉我们的实体使用哪个渲染控制器，我们只需将渲染控制器标识符添加到我们的文件中。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"render_controllers": [
    "controller.render.example"
]
```

最基本的实体文件需要这四个键以正确渲染实体。

## 动画
动画描述了我们的实体可能如何移动。这可以包括行走动画、攻击或实体如何看向玩家。它们由代码定义，描述几何体在某些时间如何移动或使用数学方程。你需要一个几何体才能使动画正常工作。

```json title="RP/animations/example.a.json"
{
	"format_version" : "1.8.0",
	"animations" : {
		"animation.example.walk" : {...},
        "animation.example.attack" : {...}
	}
}
```
每个动画由其标识符定义。我们的动画键是动画的另一个短名称定义。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"animations": {
    "walk": "animation.example.walk",
    "attack": "animation.example.attack",
    "attack_controller": "controller.animation.example"
}
```

在这里，你会注意到我们还引用了一个动画控制器。这个控制器控制何时播放某些动画。这使我们能够定义动画之间的不同过渡。

此控制器使用在动画键中定义的短名称。我们还额外定义了我们的控制器，以便能够在稍后引用何时运行此控制器。我建议查看我们的指南，以获取有关动画控制器结构的更多信息。

/// tip | 重要提示
请记住，这个键只是*定义*了我们动画的短名称，并不会运行我们的动画。如果你只有这个键，你的动画将不会在游戏中运行。
///

## 脚本
脚本键定义了实体在某些时间运行的特定脚本。这使我们能够运行动画、设置变量甚至控制实体的大小。此外，我们可以使用*Molang*来定义这些。有关Molang的更深入了解，请查看我们的页面[这里](../concepts/molang.md)。总体而言，Molang本质上是一种使用变量的数学方程。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"scripts": {
    "initialize": [...],
    "pre_animation": [...],
    "animate": [...],

    "scale": "1",
}
```

Molang中的一些有用内容包括：
- 查询。这些是根据条件变化的值。例如，`query.time_of_day`或`q.time_of_day`查询返回一天中的时间。
- 变量。这些是你可以编辑以保存稍后使用的值。例如，你可以设置变量`variable.my_number`或`v.my_number`为2。
- 评估。在Molang中，我们可以使用运算符返回值。例如，如果`q.time_of_day`大于`v.my_number`，我们可以写`q.time_of_day > v.my_number`来返回值1。

### 初始化
此脚本在实体首次初始化时运行，即当它生成时以及每次加载时。这意味着每次你登录到你的世界时，它都会运行此脚本中的任何内容。这对于设置自定义变量的默认值非常有用。

### 动画前
此脚本在每帧动画播放之前运行。这对于计算将在动画中使用的变量非常有用，这些变量需要在动画运行之前计算。

### 动画
此脚本在`pre_animation`之后的每帧运行。在这里，你运行动画和动画控制器。每帧此键中的每个动画或动画控制器都将被运行。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"scripts": {
    "animate": [
        "attack_controller",
        {
            "walk": "q.modified_move_speed"
        }
    ],
}
```

在这里，`attack_controller`是我们动画控制器的短名称。每帧它将运行我们的动画控制器以及在控制器中发生的任何过渡。此外，在动画中我们可以使用Molang定义动画播放的速度。请记住，Molang会评估为一个值，这里我们有一个查询`q.modified_move_speed`。该查询返回实体的移动速度，正常行走速度返回`1`。因此，使用此设置，我们的`walk`动画会根据实体的移动速度播放。

如果我们将其改为`"walk": 2`，则行走动画将始终以两倍的速度播放。我们还可以在动画控制器中定义这项内容，这可以更好地控制何时播放这些动画。有关如何使用Molang进行动画的更多信息，请查看我们的页面[这里](../visuals/math-based-animations.md)。

如果你的动画没有播放，检查它们是否在`animate`中使用正确的短名称定义是个好主意。

### 缩放
缩放控制模型的大小。这与你可以在实体行为文件中定义的组件`minecraft:scale`略有不同。组件`minecraft:scale`缩放实体的模型和碰撞箱，而实体资源文件中的`scale`仅缩放模型。根据你的情况，任一项可能更有用。

`scale`的另一个不同之处在于，你可以使用Molang，并且有三个附加组件：`scaleX`、`scaleY`和`scaleZ`。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"scripts": {
    "scale": "q.variant",
    "scaleX": 2,
    "scaleY": 0.5
}
```

在这里，我们的实体将根据由`minecraft:variant`组件确定的变体进行缩放。如果你希望保持碰撞箱相同，但让实体看起来更大，这可能是有益的。
此外，模型将在`y`方向上按2的比例压缩，并在`x`方向上按2的比例拉伸。

一个使用案例可能是拥有一个随机大小的气氛实体。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"scripts": {
    "initialize": [
        "v.scale = math.random_integer(1, 5);"
    ],
    "scale": "v.scale"
}
```

此代码将使每次加载实体时，它的大小在我们选择的值之间随机生成。这里`math.random_integer`是一个Molang函数，它选择提供的数字之间的随机整数。

## 音效
音效是可以在游戏中某些时刻播放的音频文件。此键再次定义音效的短名称，实体可以在动画中使用。这对于创建更动态的声音非常有用，例如，你可能希望实体在攻击时播放3个声音。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"sound_effects": {
    "attack_1": "mob.entity.attack_1",
    "attack_2": "mob.entity.attack_2",
    "attack_3": "mob.entity.attack_3"
}
```

在这里，短名称引用了在`sound_definitions.json`文件中定义的声音短名称。在其他地方使用声音时，例如在命令中，你将使用`mob.entity.attack_1`，但在实体中定义的动画中，你将使用`attack_1`。

## 粒子效果
粒子效果是包含许多小尖刺运动信息的文件，用于创建烟雾或火焰等效果。与音效类似，此键定义了粒子效果的短名称，以便在动画中使用。例如，幻影在飞行时其翅膀上有粒子效果。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"particle_effects": {
    "smoke": "wiki:smoke_particle"
}
```

在这里，短名称引用了粒子的标识符。有关粒子及其制作的更多信息，请查看我们的粒子页面[这里](../particles/particles.md)。有关在动画中使用音效和粒子效果的更多信息，你还可以查看我们的页面[这里](../visuals/animation-effects.md)。

## 生成蛋
生成蛋键允许我们为实体生成一个生成蛋。使用时，这将生成我们的实体，并自动添加到创造模式物品栏中。生成蛋的外观有两种选择，颜色和纹理。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"spawn_egg": {
    "base_color": "#db7500",
    "overlay_color": "#242222"
}
```

使用`base_color`和`overlay_color`将创建一个类似于原版的纹理蛋，使用提供的颜色。

```json title="RP/entity/example.json#minecraft:client_entity/description"
"spawn_egg": {
    "texture": "wiki.example",
}
```

`texture`键接受在`item_texture.json`中定义的图像的纹理短名称，作为生成蛋的图像使用。如果省略此键，则不会生成生成蛋。

## 其他设置
`enable_attachments`决定实体是否可以使用附加物。例如，将其设置为false意味着实体无法持有剑或弓等武器。

`hide_armor`允许实体穿戴盔甲，但不会被渲染。