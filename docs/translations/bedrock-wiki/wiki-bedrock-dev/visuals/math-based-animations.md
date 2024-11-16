---
title: 基于数学的动画
tags:
    - 中级
category: 一般
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - MedicalJewel105
    - yanasakana
    - Luthorius
    - TheItsNameless
    - SmokeyStack
    - ThomasOrs
description: 使用数学创建流畅而惊艳的动画。
---

数学动画是关键帧动画的强大替代方案。一般来说，“基于数学的动画”是使用Molang表达式来动画化实体几何体的概念。所有原版动画都是基于数学的，以下是一个示例：

<CodeHeader></CodeHeader>

```json
"leftarm" : {
    "rotation" : [ "((-0.2 + 1.5 * (math.abs(math.mod(q.modified_distance_moved, 13) - 6.5) - 3.25) / 3.25) * q.modified_move_speed) * 57.3 - v.agent.armxrotationfactor", 0.0, "-v.agent.armzrotation" ]
},
```

如你所见，基于数学的动画可能相当复杂且难以理解。因此，它们应被视为使用关键帧的_专业替代方案_——而不是*完全*替代。

这是动画平滑和理想循环的代价。

![](../assets/images/visuals/math-based-animations/animation-1.gif)

## 编写数学动画

### 手动编写

要手动编写这样的动画，只需创建一个动画文件，并将关键帧替换为单一值数组；字符串值是被接受的，并且可以在字符串中放置数学表达式。原版文件可以作为这些类型动画的宝贵参考，**强烈**建议你下载并预览它们！

对于希望*可视化*其过程的人，一个重要的提示是，[Molang Grapher](https://jannisx11.github.io/molang-grapher/)工具来自[Jannis](https://twitter.com/jannisx11)，可以在适当的图形上模拟表达式！

### 在Blockbench中

Blockbench在一定程度上允许创建和实时预览大多数基于数学的动画。
首先，在时间轴的第0帧创建一个新的关键帧。然后，你可以在左侧边栏的关键帧面板中添加和编辑Molang表达式。支持混合关键帧和数学。
**请记住**，你应始终省略表达式周围的引号；它们仅在原始JSON编辑中是必需的！

请注意，并非所有Molang查询在Blockbench中都受支持，部分原因是缺少游戏上下文。如果你希望预览使用上下文特定查询的动画，可以将其添加到关键帧面板下方的变量占位符部分，以模拟一个值。
例如，添加`q.modified_distance_moved = time*8`可以模拟以每秒8个区块的速度移动的`modified_distance_moved`查询。

## 使用查询

我们数学工具库中最大且最有用的工具是各种Molang“查询”。查询可以用来将外部信息添加到你的数学表达式中。

常见查询包括：

-   `q.modified_distance_moved`
-   `q.modified_move_speed`
-   `q.anim_time`
-   `q.life_time`

这些在动画中用于绘制诸如攻击时间或从游戏世界移动的距离等内容，以提供更动态和同步的流动。

### 避免动画控制器

通过使用查询，你可以避免创建动画控制器的需要。如果实体的速度与行走动画的速度直接相关，则默认情况下，未移动的实体将不会被动画化。

## 示例

以下是基于数学动画的具体应用示例。该示例利用了Molang查询`"q.modified_distance_moved"`：

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.12.0",
	"animations": {
		"animation.car.wheel_spin": {
			"loop": true,
			"bones": {
			
				"front_wheels": {
					"rotation": [ "q.modified_distance_moved * -30", 0, 0 ]
				},
				
				"back_wheels": {
					"rotation": [ "q.modified_distance_moved * -30", 0, 0 ]
				}
				
			}
		}
	}
}
```

在这个示例中，模型的骨骼`front_wheels`和`back_wheels`根据从`q.modified_distance_moved`传递的信息在X轴上旋转，然后乘以-30。

这意味着一辆*静止*的汽车**不会**旋转，而一辆*行驶*的汽车**会旋转**——旋转速度与汽车的移动速度成正比。