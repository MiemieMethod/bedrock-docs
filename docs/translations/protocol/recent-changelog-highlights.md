---
title: 近期变更摘录
---

# 近期变更摘录

本页按本轮扫描中最值得保留原文语境的协议变更日志文件，整理其关键信号与中文注记。正文不替代完整变更日志，仅用于帮助定位近几个版本链路中的高风险迁移点。

## 来源文件

- `.knowledge\基岩版协议库\previous_changelogs\changelog_893_11_07_25.md`
- `.knowledge\基岩版协议库\previous_changelogs\changelog_924_01_21_26.md`
- `.knowledge\基岩版协议库\previous_changelogs\changelog_944_03_04_26.md`
- `.knowledge\基岩版协议库\previous_changelogs\changelog_975_04_22_26.md`
- `.knowledge\基岩版协议库\changelog_1001_05_18_26.md`

## 893：Cereal迁移开始显性化

该文件的开发说明直接指出，协议开始迁移到Cereal序列化后，必选字段与可选字段约束会更严格，且部分枚举在过渡期可能临时表现为字符串表示。

本轮显著变化包括：

- `CommandRequestPacket`、`CommandOutputPacket`、`AnimatePacket`、`InteractPacket`、`AvailableCommandsPacket`、`LegacyTelemetryEventPacket`、`ClientboundControlSchemeSetPacket`等数据包转向Cereal。
- `TextPacket`的二进制格式调整，消息类型不再保持旧式固定布局，而是作为消息体中的判别信息出现。
- `StartGamePacket`移除了`mTickDeathSystemsEnabled`。

这一阶段的意义在于：协议风险不再只来自“新增字段”，而开始大量来自“同名数据包仍存在，但读写布局已经不兼容”。

## 924：登录元数据与诊断负载继续扩张

该文件显示，协议层开始承载更多与会话元数据和诊断有关的信息，而不再局限于世界同步本身。

重点包括：

- `ServerBoundDiagnosticsPacket`增加客户端内存分类数据。
- `StartGamePacket`增加服务端遥测数据与服务器加入信息。
- `ServerboundDataStorePacket`与`ClientboundDataStorePacket`改为跟踪路径更新。
- 同期还引入了`ClientboundTextureShiftPacket`、`VoxelShapesPacket`、`CameraSplinePacket`与相机辅助瞄准相关更新。

这意味着实现登录流程时，需要同时考虑玩法配置、平台配置和诊断上报字段的增长。

## 944：新增一段高编号数据包族

该文件在数据包ID枚举中新增了330至347这一整段数据包，反映出协议面的横向扩张。

新增项包括：

- `ClientboundDataStorePacket`
- `GraphicsParameterOverridePacket`
- `ServerboundDataStorePacket`
- 一组数据驱动界面数据包
- `ClientboundTextureShiftPacket`
- `VoxelShapesPacket`
- `CameraSplinePacket`
- `CameraAimAssistActorPriorityPacket`
- `ResourcePacksReadyForValidationPacket`
- `SyncWorldClocksPacket`
- `ClientboundAttributeLayerSyncPacket`
- `ServerStoreInfoPacket`
- `ServerPresenceInfoPacket`

对于代理、协议库和抓包工具而言，这类变化首先影响的是数据包分发表与未知包处理逻辑，而不是某个单独字段。

## 975：存在信息、商店入口与更多Cereal迁移

该文件延续了上一阶段的方向，继续扩大诊断与外围配置通道，并把更多传统玩法数据包迁移到Cereal。

可直接抽取的重点包括：

- `PlayerEnchantOptionsPacket`转为Cereal。
- `MobEquipmentPacket`转为Cereal。
- `ServerBoundDiagnosticsPacket`增加实体系统诊断数据。
- `ServerStoreInfoPacket`与`ServerPresenceInfoPacket`用于向客户端发送`ClientStoreEntryPointConfiguration`与`PresenceConfiguration`。
- `PlaySoundPacket`增加可选的声音句柄。

这一阶段说明，商店入口、存在信息和诊断通道已经成为需要稳定实现的协议组成部分，而不是可以长期忽略的外围分支。

## 1001：声音标识、聊天记录与物品栏路径继续变化

当前根目录变更日志对应的是最新一段原始版本链路，重点集中在Cereal扩张、声音标识形式变化和登录期新字段上。

关键变化包括：

- `ClientboundUpdateSoundDataPacket`加入协议。
- `ServerBoundDiagnosticsPacket`增加分析器范围诊断数据。
- `SubChunkRequestPacket`、`BossEventPacket`、`InventoryTransactionPacket`、`MobArmorEquipmentPacket`、`ClientCacheBlobStatusPacket`与`InventoryContentPacket`继续转向Cereal。
- `GraphicsOverrideParameterPacket`增加`PlayerID`，用于按玩家下发图形覆盖。
- `LevelSoundEventPacket`的`mSoundEvent`从`LevelSoundEvent`改为`SoundEventIdentifier`，即枚举或字符串变体。
- `StartGamePacket`增加`isChatLogging`。
- `PresenceConfiguration`增加`richPresenceId`，并将`mExperienceName`与`mWorldName`改为可选字段。

从兼容性角度看，这一阶段需要同时重查区块请求、客户端缓存、物品栏同步、声音事件解码与登录期会话字段。

## 相关页面

- [网络协议](../../docs/server/protocol.md)
- [基岩版协议变更索引](../../refs/server/bedrock-protocol-changelog.md)
- [变更日志索引](changelog-index.md)
