---
title: 基岩版建模
nav_order: 2
category: 一般
mentions:
    - SirLich
    - solvedDev
    - MedicalJewel105
description: 在为Minecraft基岩版建模时需要了解的技巧、窍门和注意事项。
---

本文将指导您在为Minecraft基岩版建模时需要了解的技巧、窍门和注意事项。

## 纹理故障

有时某些（较小）面的纹理会出现故障或不可见。这是因为立方体的大小在UV贴图计算时被向下取整。这意味着任何小于1的大小都会导致0像素宽的UV贴图，从而看起来会出现故障。为避免此问题，请确保所有立方体在每个方向上的长度至少为1个单位。要创建较小的立方体，请使用膨胀滑块。
如果您必须使用较小的纹理，另一个解决方法是**在每个方向上将元素大小增加1**，然后**将元素膨胀-1**，但请注意，这将导致较小的像素纹理不正确，从而产生混合像素。

## 顶点捕捉

顶点捕捉是Blockbench中的一个方便工具，任何建模者都应该使用。它在处理轮子等圆形物体时特别有用。
您可以在右上角找到此工具，位于移动和缩放工具旁边。它有两种模式，移动和缩放。该工具的工作原理可以在以下GIF中看到。
![](/assets/images/visuals/bedrock-modeling/vertex_snap.gif)

## 透明度

如果您使用半透明纹理（如彩色玻璃），则需要将带有该纹理的元素移动到元素列表的底部。否则，位于这些半透明元素后面的元素在游戏中将无法渲染。

## 纹理处理

在学习纹理处理时，您最好的选择是参考其他人如何处理类似物体和表面的纹理。木材和金属的纹理模式是不同的，您应该考虑这一点。好的指南包括
[Masteriano的纹理处理技巧](https://www.blockbench.net/wiki/guides/minecraft-style-guide)
以及一般的像素艺术指南。

## 材质

模型中透明或发光纹理的工作与否，取决于应用于它们的材质。

| 材质                | 描述                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------|
| entity              | 基本不透明材质                                                                                    |
| entity_alphatest    | 支持透明像素                                                                                      |
| entity_alphablend   | 支持半透明像素                                                                                    |
| entity_emissive     | 实心，alpha通道用作发光通道                                                                      |
| entity_emissive_alpha | alpha通道用于发光，完全黑色+透明像素将透明渲染                                                   |

## Z轴冲突

当两个元素的面位于同一位置时，称为Z轴冲突，您可以同时看到它们或其中一部分，如下图所示。
![](/assets/images/visuals/bedrock-modeling/z-fighting.png)
您可以通过将其中一个元素膨胀`0.01`或`-0.01`来解决此问题，具体取决于哪个元素应优先。

## 动画基础

在Blockbench中进行动画时，您可以手动设置每个关键帧，或者可以使用变量和函数。
在这里，您将学习基础知识。
让我们从这张图片开始。

![](/assets/images/visuals/bedrock-modeling/animations-1.png)

名称或`animation.cuack`是至关重要的。您不能在这里使用符号或大写字母，并且它必须以`animation.`开头，以便动画正常工作。我们将使用的函数是

`Base + Math.sin((q.life_time + Offset) * Speed) _ pitch`

-   Base是骨骼的起始旋转/位置
-   Sin是我们都知道的数学函数
-   `q.life_time`是一个变量。它是一个数字，随着动画的进行而增加
-   Offset是一个数字，我们用它来使动画在其“原始”位置之前或之后开始
-   Speed是从顶部到底部所需的时间
-   Pitch是它从原点偏移的距离

![](/assets/images/visuals/bedrock-modeling/animations-2.gif)

使用的函数：

`Math.sin((q.life_time+0.5)*150)*15`

一个用于位置，另一个用于旋转。

<MolangGraph code="Math.sin((q.life_time+0.5)*150)*15" :toY="2" :stepSize="0.001"/>

请记住，为了使动画成为完美的循环，您需要将sin方程的`speed`与动画的`time`相关联。
以下是获得完美循环的值表，尽管您可以发现更多。

| Speed | Time | Group |
|-------|------|-------|
| 150   | 2.4  | 1     |
| 100   | 3.6  | 2     |

这些数字可以相乘，但不能相除，因此这些也可以工作
但只能是相同选项的倍数

| Speed | Time | Group |
|-------|------|-------|
| 150   | 4.8  | 1     |
| 200   | 3.6  | 2     |
| 300   | 2.4  | 1     |
| 300   | 3.6  | 1 & 2 |

并非所有这些都会“循环”在一起。这就是组列的意义。具有相同数字的将一起工作。否则，它们将在循环中出现明显的“故障”。

:::tip
您可以通过单击以下设置来使动画循环：
![](/assets/images/visuals/bedrock-modeling/setting-loop.png)
:::

通过这个函数和创造力，动物和恐龙被动画化为行走、奔跑和攻击。
您可以在[这里](https://bedrock.dev/docs/stable/Molang)了解更多关于查询和函数的信息。

## 动画速度

要轻松更改动画的速度，您只需在我们的动画中乘以`anim_time_update`的默认值（默认为`q.delta_time + q.anim_time`）：

<CodeHeader>RP/animations/myentity.animation.json#animations</CodeHeader>

```json
"animation.myentity.myanimation": {
    "anim_time_update":"2 * q.delta_time + q.anim_time"
    //您的动画在这里！
}
```

这将使动画运行速度加快2倍。我们可以将值调整为任何浮动值，因此我们甚至可以减慢动画。例如，使用0.5，动画将运行速度减慢2倍，依此类推。