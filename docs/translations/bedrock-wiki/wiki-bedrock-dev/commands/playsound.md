---
title: 播放声音
category: 命令
mentions:
    - BedrockCommands
    - zheaEvyline
    - jordanparki7
description: 理解 /playsound 命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

您可以使用 `/playsound` 命令在您的世界中向任何地方的玩家播放音效。

## 语法

`/playsound <sound> [player] [position] [volume] [pitch] [minimumVolume]`

## 定义

### 声音

- 这是您希望播放的音效。
- 您可以在以下链接找到当前可用的音效 ID 列表：
    - https://www.digminecraft.com/lists/sound_list_pe.php

### 玩家

- 这是一个可选参数。
- 它指的是您通常使用的目标选择器（您希望播放声音的对象）` @a `、` @r `等。然而，`@e`选择器在没有`type=player`参数的情况下不适用。

### 位置

- 这是一个可选参数。
- 它指的是播放声音的 `x y z` 位置，因此将成为播放声音半径的中心。

### 音量

- 这是一个可选参数。
- 它决定了声音效果可以被听到的球体的大小。
    - ` 0.0 ` 是最小值。
- 随着 `volume` 值的增加，听到的球体大小也会增加。
    - 播放音量为 `1` 相当于半径为 16 个区块的可听球体。
    - 同样，音量为 `4` 将相当于 64 个区块。

### 音调

- 这是一个可选参数。
- 它决定了声音效果的音调。
- 它可以是 ` 0.0 ` 到 ` 256.0 ` 之间的值。
    - 值越高，音调越高。
    - 小于或等于 `0.0` 的值会使声音变得不可听。

> 注意：音调影响声音效果播放的速度。例如，音调为 `0.5` 意味着声音效果以 ` 0.5× ` 的速度播放。

### 最小音量

- 这是一个可选参数。
- 它决定了声音在可听球体外被听到的最小音量。
- 它可以是 ` 0.0 ` 到 ` 1.0 ` 之间的值。

## 示例

```yaml
# 向最近的玩家播放随机爆炸音效
/playsound random.explode @p

# 向所有玩家在其位置播放随机 orb 音效，音量为 10000
/execute as @a at @s playsound random.orb @s ~ ~ ~ 10000
```

注意：由于 `/playsound` 命令是位置相关的，因此在玩家位置以较大音量播放音效是有帮助的，如上面的第二个示例所示。这可以防止在某些情况下声音效果被切断，例如在传送到远距离后。

**（推荐）接下来阅读: [声音](/concepts/sounds)**