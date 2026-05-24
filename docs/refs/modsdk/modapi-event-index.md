# 中国版ModAPI事件域索引<!-- md:flag china -->


/// warning | 使用边界
以下事件属于中国版模组SDK事件系统，通过中国版系统监听接口订阅。不要将这些事件名直接套用到国际版`@minecraft/server`事件对象，也不要与Apollo网络服事件名混用。
///

## 事件域统计

| 事件域 | 条目数 | 对应知识文件 |
| --- | ---: | --- |
| 物理 | 2 | `事件\物理.md` |
| 世界 | 44 | `事件\世界.md` |
| 实体 | 43 | `事件\实体.md` |
| 玩家 | 43 | `事件\玩家.md` |
| 方块 | 52 | `事件\方块.md` |
| 物品 | 46 | `事件\物品.md` |
| 模型 | 9 | `事件\模型.md` |
| UI | 17 | `事件\UI.md` |
| 音效 | 3 | `事件\音效.md` |
| 控制 | 23 | `事件\控制.md` |
| 联机大厅 | 1 | `事件\联机大厅.md` |
| 游戏设置 | 4 | `事件\游戏设置.md` |

## 常见事件域示例

| 事件域 | 代表事件 | 说明 |
| --- | --- | --- |
| 世界 | `LoadServerAddonScriptsAfter`、`OnScriptTickServer`、`ServerChatEvent` | 覆盖脚本加载、滴答与聊天等全局生命周期。 |
| 实体 | `ActorHurtServerEvent`、`DamageEvent`、`EntityTickServerEvent` | 侧重受伤、伤害计算、实体滴答与状态变化。 |
| 玩家 | `AddExpEvent`、`DimensionChangeFinishServerEvent`、`PlayerAttackEntityEvent` | 覆盖玩家成长、维度切换和交互行为。 |
| 方块 | `BlockNeighborChangedServerEvent`、`PistonActionServerEvent`、`DestroyBlockEvent` | 覆盖邻居更新、活塞行为与方块破坏。 |
| 物品 | `ActorUseItemServerEvent`、`OnItemPutInEnchantingModelServerEvent`、`AnvilUseEvent` | 覆盖物品使用、附魔与铁砧流程。 |
| UI与控制 | `ClientUiInitFinishedEvent`、`UiScreenChangedClientEvent`、`ClientJumpButtonPressDownEvent` | 覆盖界面生命周期与输入事件。 |

## 相关页面

- 中国版通用运行时接口：见[世界控制接口](world-control.md)。
- 中国版全域接口索引：见[中国版ModAPI接口域索引](modapi-interface-index.md)。
- 中国版枚举值：见[中国版ModAPI枚举值索引](modapi-enum-index.md)。
- Apollo网络服事件：见[Apollo网络服事件](apollo-events.md)。