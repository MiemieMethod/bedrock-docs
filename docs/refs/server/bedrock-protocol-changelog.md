# 基岩版协议变更索引

本文用于汇总基岩版协议变更日志的结构与使用方式，便于在版本迁移时快速定位高风险兼容性变化。

## 常看文件

| 类别 | 路径 | 作用 |
|---|---|---|
| 当前变更日志 | `changelog_1001_05_18_26.md` | 记录最新一段协议版本变更。 |
| 历史变更日志 | `previous_changelogs\*.md` | 按协议版本持续记录增删改。 |
| 补充机制文档 | `additional_docs\*.md`与子目录 | 解释服务端权威运动、方块破坏、子区块请求、缓存校验、物品栏迁移等机制。 |
| 说明页 | `README.md` | 简述该协议仓库的用途与边界。 |

## 补充机制文档

| 文件 | 主题 | 站内落点 |
|---|---|---|
| `additional_docs\ConfiguringAntiCheat.md` | 运动修正阈值与反作弊配置 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\PlayerMovementOverview.md` | 回退、重放与带滴答修正 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\MovementProtocolDeprecation.md` | 服务端权威第三版迁移与弃用路径 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\BlockBreakingOverview.md` | 方块破坏预测与服务端校验 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\BuildActionSimulationRate.md` | 建造与破坏从渲染帧迁移到模拟刻 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\SubChunk Request System v1.18.10.md` | 子区块请求系统与批量偏移模式 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\ClientCacheMissResponsePacketValidation.md` | 客户端缓存响应校验与BlobID验证 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\ServerAuthInventory\PlayerUIContainer.md` | 玩家界面容器语义与槽位背景 | [网络协议](../../docs/server/protocol.md) |
| `additional_docs\ServerAuthInventory\ItemStackPackets_Disabled.md` | ItemStackNetManager禁用期兼容要求 | [网络协议](../../docs/server/protocol.md) |

## 近期高风险兼容性信号

以下变更类型在升级协议版本时通常需要优先复核：

- `Converted to Cereal`：读写布局变化，常导致旧二进制解析器直接失效。
- `Added/Removed/Modified Packets`：包级结构变化，常影响握手、同步和功能开关。
- `Modified Enums`与`Modified Types`：枚举位移与类型重排会影响分支判断和反序列化。
- 服务端权威迁移相关改动：运动输入、方块破坏与物品栏请求—响应路径发生替换。
- 字段表示扩张：字段可能从固定枚举演进为枚举或字符串变体，也可能新增可选字段与读写顺序修正。

## 近期重点版本链路

| 文件 | 关键变化 | 兼容性关注点 |
|---|---|---|
| `previous_changelogs\changelog_893_11_07_25.md` | 首轮显性Cereal迁移，涉及`CommandRequestPacket`、`CommandOutputPacket`、`AnimatePacket`、`InteractPacket`、`AvailableCommandsPacket`、`LegacyTelemetryEventPacket`、`ClientboundControlSchemeSetPacket`等；`TextPacket`调整消息体判别方式；`StartGamePacket`移除`mTickDeathSystemsEnabled`。 | 旧解析器不能再假定文本包与若干命令类数据包沿用原布局，登录阶段字段也需要按目标版本复核。 |
| `previous_changelogs\changelog_924_01_21_26.md` | `ServerboundDiagnosticsPacket`新增客户端内存分类数据；`StartGamePacket`新增服务端遥测数据与加入信息；数据存储包开始跟踪路径更新；同时引入纹理偏移、体素形状、相机样条等新协议面。 | 登录元数据与诊断负载继续扩大，服务端若忽略新字段，可能导致诊断或会话配置能力失配。 |
| `previous_changelogs\changelog_944_03_04_26.md` | 新增数据包ID段330至347，包括数据存储、图形参数覆盖、数据驱动界面、纹理偏移、体素形状、世界时钟同步、属性层同步、商店信息与存在信息。 | 包ID表不应静态写死到旧范围；代理、抓包器和多版本库都应及时刷新分发表。 |
| `previous_changelogs\changelog_975_04_22_26.md` | `PlayerEnchantOptionsPacket`与`MobEquipmentPacket`转为Cereal；`ServerboundDiagnosticsPacket`继续扩大到实体系统诊断；`ServerStoreInfoPacket`与`ServerPresenceInfoPacket`用于下发`ClientStoreEntryPointConfiguration`与`PresenceConfiguration`。 | 诊断、商店入口与存在信息已经成为运行期协议的一部分，不再只是外围平台功能。 |
| `changelog_1001_05_18_26.md` | `SubChunkRequestPacket`、`BossEventPacket`、`InventoryTransactionPacket`、`MobArmorEquipmentPacket`、`ClientCacheBlobStatusPacket`、`InventoryContentPacket`继续转向Cereal；`LevelSoundEventPacket`将`mSoundEvent`改为`SoundEventIdentifier`；`StartGamePacket`新增`isChatLogging`；`PresenceConfiguration`新增`richPresenceId`并将`mExperienceName`、`mWorldName`改为可选。 | 区块请求、缓存状态、物品栏与声音事件路径均出现破坏性变化，登录阶段还增加了聊天记录与存在信息字段，宜作为最新适配的最高优先级。 |

## 1.26.30中的结构信号

1.26.30对应的协议1001进一步表明，协议范围已经覆盖传统玩法同步之外的创作、界面、呈现与诊断通道：

- `EditorNetworkPacket`（190）是编辑器专用的通用载荷包，字段由`Route To Manager`、`Raw Variant Name`与`Raw Variant Data`组成。
- `ClientboundDataDrivenUIShowScreenPacket`（333）允许服务端要求客户端显示数据驱动界面屏幕，并以`ScreenId`、`FormId`和可选`DataInstanceId`跟踪实例。
- `GraphicsOverrideParameterPacket`（331）当前不仅可按生物群系覆盖图形参数，也已包含`Player Identifier`字段，用于按玩家下发覆盖。
- `ServerPresenceInfoPacket`（347）中的`PresenceConfiguration`当前包含`experienceName`、`worldName`与`richPresenceId`。
- `ClientboundUpdateSoundDataPacket`（348）已经引入独立的服务器声音句柄更新路径；现阶段快照中公开的事件值为`Stop`。
- `SubChunkRequestPacket`（175）当前结构明确为“维度+中心坐标+偏移列表”的批量请求模式，偏移列表上限为8192项。

## 使用建议

1. 先锁定目标协议版本，再对照相邻版本变更日志逐条复核。
2. 对出现`Converted to Cereal`的数据包，优先重做读写顺序验证。
3. 对服务端权威相关功能，需同时核对`StartGamePacket`开关、输入包和修正包三处行为。
4. 对区块与缓存系统，需同时核对`LevelChunkPacket`、`SubChunkRequestPacket`、`SubChunkPacket`与`ClientCacheMissResponsePacket`。
5. 对登录与会话配置路径，需额外复核`StartGamePacket`、`ServerStoreInfoPacket`、`ServerPresenceInfoPacket`、`GraphicsOverrideParameterPacket`与`ServerboundDiagnosticsPacket`。