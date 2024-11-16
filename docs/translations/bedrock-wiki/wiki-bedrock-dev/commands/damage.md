---
title: 伤害
category: 命令
mentions:
    - BedrockCommands
    - cda94581
description: /damage 命令说明。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

在Minecraft版本 `1.18.10` 中引入的 /damage 命令可以对指定实体造成精确的伤害。随着这一变化，使用 `/effect` 命令对实体造成伤害的笨拙方法已被淘汰，使得地图和其他创作变得更加强大。

## 语法

- /damage 命令可以通过两种方式使用：
    - `/damage <目标> <数量> [原因]`
    - `/damage <目标> <数量> <原因> entity <伤害者>`

## 参数

- 尖括号 `< >` 或方括号 `[ ]` 外的短语指示你按原样输入。
- 方括号内的短语是变量，需要替换：
    - **` <> `** 尖括号表示该变量是必需的。
    - **` [] `** 方括号表示该变量是可选的。

## 变量

- **` 目标 `** 这是你典型的实体选择器，例如 `@s`、`@e` 或 `"cda94581"`。可以同时选择多个实体以对多个目标造成伤害。

- **` 数量 `** 这是一个整数，指定要对目标造成的伤害量。最小值为 `0`，最大值为 `2147483647`，即有符号32位整数的限制。

- **` 原因 `** 这指定了造成伤害的“原因”。该原因将出现在死亡消息中（`X 因为原因：跌落而重重摔倒`），并在与盔甲的伤害计算中使用（`根据穿戴的盔甲，造成的伤害值可能会不同`），还可用于行为包/附加包中的多种其他情况。所有伤害原因的完整列表可以在 [下方](#伤害原因列表) 找到。

- **` 伤害者 `** 如果原因与实体有关（如 `entity_attack`），则指定伤害的来源（造成攻击的实体）。这仅限于一个目标。如果选择器找到多个目标，将抛出错误。

> 注意：`<原因> entity <伤害者>` 仅在原因与另一个实体有关时（`entity_attack`）是必需的。否则，请遵循第一种语法。

## 示例

<CodeHeader></CodeHeader>

```yaml
# 对所有玩家造成4点伤害
/damage @a 4

# 对所有类型为'sheep'的实体造成3点'火焰'伤害
/damage @e [type=sheep] 3 fire

# 从随机玩家对所有类型为'sheep'的实体造成40点'实体攻击'伤害
/damage @e [type=sheep] 40 entity_attack entity @r
```

## 伤害原因列表

以下是当前在MCBE中可用于 `/damage` 命令的所有“伤害来源”：

<CodeHeader></CodeHeader>

```
all
anvil
block_explosion
campfire
charging
contact
drowning
entity_attack
entity_explosion
fall
falling_block
fire
fire_tick
fireworks
fly_into_wall
freezing
lava
lightning
magic
magma
none
override
piston
projectile
self_destruct
ram_attack
sonic_boom
soul_campfire
stalactite
stalagmite
starve
suffocation
temperature
thorns
void
wither
```

有关最新列表，请访问官方附加包文档页面 **[这里](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/examples/addonentities?view=minecraft-bedrock-stable#entity-damage-source)**。