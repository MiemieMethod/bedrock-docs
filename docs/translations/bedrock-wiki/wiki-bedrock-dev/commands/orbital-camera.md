---
title: 轨道相机
category: 技术
mention:
  - BedrockCommands
  - zheaEvyline
description: 此技术允许您将相机旋转限制在围绕玩家、实体或位置的轨道上，轨道的高度和半径均可完全调整。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

此技术允许您将相机旋转限制在围绕玩家、实体或位置的轨道上，轨道的高度和半径均可完全调整。

## 视频演示

<YouTubeEmbed
    id="yOlWjTpInFE"
/>

## 命令

<CodeHeader>BP/functions/cameras/orbital.mcfunction</CodeHeader>

```yaml
execute as @p at @s anchored eyes rotated ~ 0 positioned ^^1^-2 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @s
```
![一个重复命令方块](/assets/images/commands/commandBlockChain/1.png)

**二维可视化：**

![OrbitCamVisualRep](/assets/images/commands/orbitcam/OrbitCamVisualRep.gif)

**命令解析：**

- `as @p`
  - 将执行目标设置为最近的玩家。
- `at @s`
  - 将执行位置设置为目标玩家的位置。
- `anchored eyes`
  - 将执行位置提升到目标玩家的视线高度。
- `rotated ~ 0`
  - 将执行旋转设置为相对于目标玩家的水平旋转，但将垂直旋转限制为 0°（水平）。
  - 如果您希望锁定水平旋转，只需使用：`rotated 0 ~`
     - 注意：值 `0` 可以更改为您需要的方向。有关更多信息，请参见 [旋转](/commands/selectors#rotation)。
  - 如果您不希望锁定垂直旋转，只需完全省略此部分，以获得完整的球形旋转。然而，这不会阻止相机进入地下。
- `positioned ^^1^-2`
  - 将执行位置推送到玩家上方 1 个区块并向后 2 个区块。
  - 增加或减少值 1 以增加/减少轨道高度。
  - 增加或减少值 -2 以增加/减少轨道半径。
     - 负值将设置位置在玩家后方。
     - 正值将设置位置在玩家前方。
     - 要了解更多，请参见：[坐标系统](/commands/relative-coordinates)。
- `run camera @s set minecraft:free ease 0.1 linear pos ~~~`
  - 为目标玩家设置相机，使用 `minecraft:free` 预设，线性缓动值为 `0.1`，相对坐标为（目标玩家视线的上方 1 个区块和后方 2 个区块）。
  - 要调整相机移动速度，请增加/减少缓动值 `0.1`。
  - 要了解 `/camera` 命令及其可用选项（如预设和缓动），请参见以下资源：
     - [相机命令介绍](https://learn.microsoft.com/en-us/minecraft/creator/documents/cameracommandintroduction)
     - [相机命令视频教程](https://youtu.be/GnYrZlBCyWg)
- `facing @s`
  - 将相机视角方向调整为面向目标玩家的位置。

**类似示例：**

<CodeHeader>BP/functions/cameras/orbital.mcfunction</CodeHeader>

```yaml
# 使相机围绕标记为 'orbit_center' 的实体旋转
execute as @p at @e [tag=orbit_center] anchored eyes rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing @e [tag=orbit_center]
```
![一个重复命令方块](/assets/images/commands/commandBlockChain/1.png)

<CodeHeader>BP/functions/cameras/orbital.mcfunction</CodeHeader>

```yaml
# 使相机围绕位置 6 7 8 旋转
execute as @p positioned 6 7 8 rotated as @s rotated ~ 0 positioned ^^1^-5 run camera @s set minecraft:free ease 0.1 linear pos ~~~ facing 6 7 8
```
![一个重复命令方块](/assets/images/commands/commandBlockChain/1.png)