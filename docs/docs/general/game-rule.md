# 游戏规则

**游戏规则（Game Rule）**是Minecraft基岩版中控制世界行为的一组可配置参数。游戏规则决定了世界中各种基础机制的开关和行为方式，如生物生成、天气变化、火焰蔓延等。

## 概述

每个存档拥有一组独立的游戏规则设置。游戏规则可以通过世界设置界面进行调整，也可以通过`/gamerule`命令在游戏中动态修改。游戏规则的值为布尔值或整数值。

游戏规则不会因附加包的安装而改变，它们始终属于世界层面的设置。游戏规则的值存储在存档的`level.dat`文件中。

## 常用游戏规则

以下为基岩版中部分重要的游戏规则：

### 生物与生成

| 游戏规则 | 类型 | 默认值 | 描述 |
|---------|------|-------|------|
| `doMobSpawning` | 布尔 | `true` | 是否允许生物自然生成 |
| `doMobLoot` | 布尔 | `true` | 生物死亡时是否掉落物品 |
| `mobGriefing` | 布尔 | `true` | 生物是否可以破坏方块 |
| `doEntityDrops` | 布尔 | `true` | 非生物实体是否掉落物品 |

### 玩家

| 游戏规则 | 类型 | 默认值 | 描述 |
|---------|------|-------|------|
| `keepInventory` | 布尔 | `false` | 玩家死亡时是否保留物品 |
| `naturalRegeneration` | 布尔 | `true` | 是否允许自然恢复生命值 |
| `pvp` | 布尔 | `true` | 是否允许玩家间战斗 |
| `drowningDamage` | 布尔 | `true` | 是否受到溺水伤害 |
| `fallDamage` | 布尔 | `true` | 是否受到摔落伤害 |
| `fireDamage` | 布尔 | `true` | 是否受到火焰伤害 |
| `freezeDamage` | 布尔 | `true` | 是否受到冰冻伤害 |
| `respawnBlocksExplode` | 布尔 | `true` | 重生点方块在非对应维度使用时是否爆炸 |

### 世界

| 游戏规则 | 类型 | 默认值 | 描述 |
|---------|------|-------|------|
| `doDaylightCycle` | 布尔 | `true` | 是否进行昼夜更替 |
| `doWeatherCycle` | 布尔 | `true` | 是否进行天气变化 |
| `doFireTick` | 布尔 | `true` | 是否允许火焰蔓延和自然熄灭 |
| `randomTickSpeed` | 整数 | `1` | 随机刻的速度 |
| `tntExplodes` | 布尔 | `true` | TNT是否会爆炸 |
| `doTileDrops` | 布尔 | `true` | 方块被破坏时是否掉落物品 |
| `doInsomnia` | 布尔 | `true` | 是否生成幻翼 |

### 命令与显示

| 游戏规则 | 类型 | 默认值 | 描述 |
|---------|------|-------|------|
| `commandBlocksEnabled` | 布尔 | `true` | 命令方块是否可以执行 |
| `commandBlockOutput` | 布尔 | `true` | 命令方块是否在聊天栏显示输出 |
| `sendCommandFeedback` | 布尔 | `true` | 命令执行结果是否在聊天栏显示 |
| `showCoordinates` | 布尔 | `false` | 是否在屏幕上显示玩家坐标 |
| `showDaysPlayed` | 布尔 | `false` | 是否在屏幕上显示游戏天数 |
| `showTags` | 布尔 | `true` | 是否显示物品的标签信息 |

### 其他

| 游戏规则 | 类型 | 默认值 | 描述 |
|---------|------|-------|------|
| `maxCommandChainLength` | 整数 | `65536` | 命令方块链的最大长度 |
| `functionCommandLimit` | 整数 | `10000` | 函数内可执行命令的最大数量 |
| `spawnRadius` | 整数 | `5` | 玩家重生点的随机扩散半径 |

## 游戏规则与存档

游戏规则的值以键值对形式存储在`level.dat`的NBT数据中。修改游戏规则的效果是即时的，无需重新加载世界。世界模板可以通过其清单文件或`level.dat`预设游戏规则的值。