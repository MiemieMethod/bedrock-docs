---
title: 在任意空间之间转换坐标（世界、实体、骨骼）
category: 教程
tags:
    - 中级
mentions:
    - Johnb003
    - SmokeyStack
description: 本页将讨论如何在Minecraft中不同坐标系之间进行转换。
---

## 概述

本页将讨论如何在Minecraft中不同坐标系之间进行转换。你可能会出于多种原因想要进行这种转换：

-   如果你想使用细长的立方体构建3D线条以可视化某些3D空间，你需要将世界坐标转换为实体骨骼坐标。
-   如果你想进行精确的头部追踪，并希望从实体的特定关节测量到目标的角度。
-   如果你想从武器的尖端发射投射物。
-   如果你想解决四肢的IK链以匹配地面接触点。

## 背景

在我们开始指南之前，有几个背景主题值得讨论。

### 矩阵

通常，在我们将所有内容发送到图形卡之前，我们会将其转换为矩阵，因为通过一组矩阵转换多个顶点（例如网格的顶点）是非常高效的。游戏通常使用其他表示方式，例如四元数，或者在Minecraft中使用欧拉旋转，但对矩阵有一个扎实的理解是一个良好的开始。

如果你看到一个充满值的4x4矩阵，如果你不习惯使用它们，可能会觉得需要特殊的能力才能理解它们，如下所示。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-1.png" />

但通常我们处理的3D变换矩阵只是简单的位移和由描述X、Y和Z轴的“轴向量”表示的旋转，每个轴向量都是一个3分量向量。

当以3x3矩阵书写时，方向向量是单位长度向量（除非有缩放），这些向量就像你习惯看到的任何方向向量一样，它们有定义该空间轴向的x、y、z分量。

<WikiImage src="../assets/images/tutorials/entity-transforms/image.png" />

在3x3矩阵中（尤其是在教科书中），它们沿列以二维数组的形式排列，如下所示：

```
[ XAxis.x  YAxis.x  ZAxis.x ]
[ XAxis.y  YAxis.y  ZAxis.y ]
[ XAxis.z  YAxis.z  ZAxis.z ]
```

在程序中，你总是会将数据存储在内存中为`<XAxis.x, XAxis.y, XAxis.z, YAxis.x, YAxis.y, YAxis.z, ZAxis.x, ZAxis.y, ZAxis.z>`，无论你是行主序还是列主序（[关于行主序与列主序的维基](https://en.wikipedia.org/wiki/Row-_and_column-major_order)），这意味着如果你是行主序，你将XAxis放在行中。如果你的数学库遵循这些规则，那么它影响**乘法的顺序**：

所有矩阵乘法始终是，行 x 列。

因此，对于**行主序**，向量和矩阵的乘法是：`row_vector * matrix = row_vector`：

<WikiImage src="../assets/images/tutorials/entity-transforms/image-2.png" />

对于**列主序**，要进行与行主序相同的乘法，你需要反转顺序：

<WikiImage src="../assets/images/tutorials/entity-transforms/image-3.png" />

上述区别非常重要，特别是如果你在线阅读一些材料，以便理解数据转换的顺序将如何受到影响。

这意味着，如果我们有一个相对于我们的右手的位置，并且我们想知道在世界中的位置，我们首先必须通过我们的右手进行转换，然后是右肘、右肩、脊柱、骨盆、根、实体等，一直到它在世界空间中。以列主序书写将是：

```
Entity * RootBone * Pelvis * Spine0 .. SpineN * RShoulder * RightElbow * RightHand * point;
```

如果你进入更复杂的变换，强烈建议你命名你的变换，以反映它们转换的空间。因此，对于上述内容，我们可以使用类似的命名：

```
World_To_Entity * Entity_To_Root * Root_To_Pelvis * Pelvis_To_Spine0 .. Spine(N-1)_To_SpineN * SpineN_To_RShoulder * RShoulder_To_RElbow * RElbow_To_RHand * RHand_point;
```

这样我们就不容易混淆我们所处的“空间”。上述描述为“局部空间”。每个关节相对于父关节。但如果我们从`Root`乘以到`RHand`，结果变换仍然是`RHand`变换，只是处于“角色或实体空间”。要将其转换为世界空间，我们必须乘以`World_To_Entity * Entity_To_RHand = World_To_RHand`。

从技术上讲，这种“To”命名有点混淆，因为应用于点的实体变换实际上是转换`EntityToWorld`，但它是从右到左应用的，因此`World_To_Entity`从右到左读为`Entity_To_World`。我还见过：`WorldFromEntity * EntityFromRoot`。无论是“From”还是“To”，使用这种相对而非绝对的命名方式的好处在于，当你看到它写出来时，你也可以验证你的数学是正确的：

```
A_To_B = A_To_Something * Something_To_B
              ^^^^^^^^^^^^^^^^^^^^^
```

标记的区域：`^`应该始终匹配。结合它去掉中间部分会给你它所做的自然名称。

最后，转到Minecraft。在撰写本文时，Minecraft没有可以相乘的变换，因此它们没有推断出列主序或行主序标记。你只需获得一个变换，如何应用它取决于你。但选择了列主序后，我们可以将操作写成一个序列，只要你按顺序应用它们，你就可以了。

此外，无论我们使用TRS（变换旋转缩放组合对象）、四元数、矩阵还是欧拉角，当涉及到旋转时，顺序是重要的。先旋转A再旋转B，与先旋转B再旋转A是不同的。

## 在开始之前了解世界

让我们考虑一下未旋转的标准情况下的轴向量。我们实际上可以通过在世界中移动来确定正X、Y和Z的方向。当你第一次进入游戏时，你面朝北，游戏称之为北。如果你向前走，你会看到这会增加你的Z值。如果你跳跃，你会看到Y值上升。而X呢？这不对！其实并没有错，它是左边！当你继续面朝北时，如果你向左移动，这会增加你的X值。这是一个右手坐标系（如果你将手指指向一个轴，并将它们弯曲到下一个连续的轴，你的拇指指向第三个轴。XY->Z，YZ->X，Z的包裹：ZX->Y）。

## 最后！！让我们开始创建一个实体

在创建实体时，我建议从Blockbench开始，并使你创建的第一个实体成为一个简单的三轴框架，如下所示：

<WikiImage src="../assets/images/tutorials/entity-transforms/image-4.png" />

此时有几个奇怪的事情需要注意。请密切关注Blockbench标记的“北、东、南和西”的方向。

1. 首先要注意的是，这与Minecraft世界坐标系旋转了180度。你应该让你的实体面朝“北”，这在游戏世界坐标中是负Z。
2. 事情变得更加奇怪。如果你在正X方向移动框，框的坐标显示为正x值，但是如果你创建一个骨骼，并转到动画选项卡，尝试调整骨骼的位置，移动手柄仍然是预期的，但现在在正方向拖动手柄，实际上会在X上给出负值。在动画中，+X朝西，而+Y仍然向上，+Z仍然朝南。因此，与Minecraft世界相比，我们必须翻转Z，并开始在实体中使用左手坐标框架。
3. 实体的缩放因子为16倍。在世界中，一个“方块”或1个单位实际上在实体中是16个单位。

让我们尝试将我们的三轴框架归类到一个骨骼下。
然后复制该组，这样我们就可以在实体中保留一个，并将另一个移动到世界位置。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-5.png" />

1. 转到动画选项卡。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-6.png" />

2. 创建一个新动画。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-7.png" />

3. 为移动器添加一个位置关键帧。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-8.png" />

4. 尝试在X轴上移动并确认情况很奇怪。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-9.png" />

6. 现在让我们使用变量设置位置，我们将在`pre_animation`脚本中设置。

<WikiImage src="../assets/images/tutorials/entity-transforms/image-11.png" />

7. 你应该能够从最小机器人示例中混合搭配，以了解如何启动你的实体。此外，你将保存你的Blockbench几何体和动画。在行为方面，目前你不需要太多。也许只需：

```json
"minecraft:physics": {},
"minecraft:collision_box": {},
```

在实体方面，你只需要最小的内容来播放你的动画：

```json
"animations": {
    "myAnim": "animation.tut_transform.move"
},
"scripts": {
    "pre_animation": [
        "// TODO -- 我们将在下一个步骤中填充此内容。"
    ],
    "animate": [
        "myAnim"
    ]
}
```

最后，对于脚本我们可以这样做：

```json
"
v.target.x = 10;
v.target.y = q.position(1);
v.target.z = 10;

v.target.x = v.target.x - q.position(0);
v.target.y = v.target.y - q.position(1);
v.target.z = v.target.z - q.position(2);

t.cos_yaw = math.cos(q.body_y_rotation);
t.sin_yaw = math.sin(q.body_y_rotation);
t.x = v.target.x;
v.target.x=t.cos_yaw * t.x + t.sin_yaw * v.target.z;
v.target.z=-t.sin_yaw * t.x + t.cos_yaw * v.target.z;

v.target.x = v.target.x * 16;
v.target.y = v.target.y * 16;
v.target.z = -v.target.z * 16;
"
```

让我们稍微分解一下：

`pre_animation`在动画之前运行，并运行此脚本。该脚本旨在给出一个位置，也许你的附加包将通过脚本从你的行为中提供输入参数？

目前你可以将这些硬编码到世界位置10,y,10，其中y与实体的高度相同。

```
v.target.x = 10;
v.target.y = q.position(1);
v.target.z = 10;
```

因此，通常我们所做的是应用一个“TRS”变换，旋转和缩放，以便从一个空间到另一个空间。

从技术上讲，请记住我们将变换堆栈写成这样：

```
Translation * RotationZ * RotationY * RotationX * Scale * point;
```

但是，在我们的情况下，我们不是从实体转换到世界，而是从世界转换到实体。当我们有可逆的非交换数学运算时，应用此逆的方式是这样的：

```
inverse(A*B) = inverse(B) * inverse(A)
```

这意味着，执行操作的相反方向，以相反的顺序。因此，我们按以下顺序将这些操作应用于我们的向量。

1. inverse(Translation)
2. inverse(RotationZ)
3. inverse(RotationY)
4. inverse(RotationX)
5. inverse(Scale)

在数学上，这看起来像：

```
Inverse(Scale) * Inverse(RotationX) * Inverse(RotationY) * Inverse(RotationZ) * Inverse(Translation) * point;
```

这实际上是从右到左发生的。

#### 1: Inverse(Translation)

如果通常（在前进方向上）你是从实体到世界，你会将你的实体相对位置（例如关节位置）与实体的位置相加。因此在反向中，我们减去实体的位置。

```
v.target_x = v.target_x - q.position(0);
v.target_y = v.target_y - q.position(1);
v.target_z = v.target_z - q.position(2);
```

#### 2: Inverse(RotationZ)

目前实体似乎只能通过俯仰和偏航从控制器进行调整。因此我们跳过这一步。

#### 3: Inverse(RotationY)

要查询实体的偏航，有一个查询方法：`q.body_y_rotation`。我们将使用它，但要考虑到正旋转应该使角色向左转。通过角度旋转向量是一个相当简单的公式，使用正弦和余弦，但正确的符号很重要。想象一下，如果你有一个向世界+z方向的向量，然后向左旋转，+X轴最初会变成正值还是负值？在我们的情况下，X向左实际上仍然是世界空间，因此X向左是正值。同样，如果我们有一个朝向正X（向左）的向量，然后开始向左旋转，Z轴将开始变成？是的，负值。你只需否定正弦项。最后一点，t.x是一个临时变量，用于保存目标的值。

```
t.cos_yaw = math.cos(q.body_y_rotation);
t.sin_yaw = math.sin(q.body_y_rotation);
t.x = v.target_x;
v.target_x=t.cos_yaw * t.x + t.sin_yaw * v.target_z;
v.target_z=-t.sin_yaw * t.x + t.cos_yaw * v.target_z;
```

注意，通常我喜欢将其写成：

```
new_first_axis = cos(angle) * first_axis - sin(angle) * second_axis;
new_second_axis = sin(angle) * first_axis + cos(angle) * second_axis;
```

其中first和second轴是与被旋转的轴垂直的两个轴，但按照右手法则排列。因此：XY、YZ或ZX。

换句话说，这里有另一个替代方案，将与其他欧拉角（XY和YZ）更一致。

```
t.cos_yaw = math.cos(q.body_y_rotation);
t.sin_yaw = math.sin(q.body_y_rotation);
t.z = v.target.z;
v.target.z=t.cos_yaw * t.z - t.sin_yaw * v.target.x;
v.target.x=t.sin_yaw * t.z + t.cos_yaw * v.target.x;
```

#### 4: Inverse(RotationX)

我认为实体确实有可能俯仰，但实际上我没有见过。因此我跳过了它。

这是读者的练习，不过稍后在涉及骨骼变换时会有更多信息，因此你可以从该部分获取一些额外的上下文（当我到达时）。

#### 5: Inverse(Scale)

最后一步是将缩放应用于从世界到实体。实体需要用更小的单位表示，因此在这个方向上的操作是乘法。如果我们是从实体到世界，则应除以16。

这里还有一个微妙的最后否定，正如在Blockbench中动画时所指出的，技术上X与看起来应该的相反，但这实际上将其与世界坐标框架对齐，而Z仍然是相反的。因此，我们只需在缩放步骤中翻转Z。

```
v.target.x = v.target.x * 16;
v.target.y = v.target.y * 16;
v.target.z = -v.target.z * 16;
```