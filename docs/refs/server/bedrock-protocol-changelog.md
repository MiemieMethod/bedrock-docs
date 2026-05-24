# 基岩版协议变更索引

本文用于汇总官方协议仓库变更日志文件的结构与使用方式，便于在版本迁移时快速定位高风险兼容性变化。

## 来源

- 来源目录：`.knowledge\基岩版协议库`
- 主仓库：<https://github.com/Mojang/bedrock-protocol-docs>

## 文件结构

| 类别 | 路径 | 本轮扫描数量 | 作用 |
|---|---|---:|---|
| 当前变更日志 | `changelog_1001_05_18_26.md` | 1 | 记录最新原始协议版本变更。 |
| 历史变更日志 | `previous_changelogs\*.md` | 60 | 按协议版本持续记录增删改。 |
| 补充机制文档 | `additional_docs\*.md`与子目录 | 10 | 解释服务端权威运动、方块破坏、子区块请求、缓存校验、物品栏迁移等机制。 |
| 仓库说明 | `README.md` | 1 | 说明该仓库用途与基本边界。 |

## 近期高风险兼容性信号

以下变更类型在升级协议版本时通常需要优先复核：

- `Converted to Cereal`：读写布局变化，常导致旧二进制解析器直接失效。
- `Added/Removed/Modified Packets`：包级结构变化，常影响握手、同步和功能开关。
- `Modified Enums`与`Modified Types`：枚举位移与类型重排会影响分支判断和反序列化。
- 服务端权威迁移相关改动：运动输入、方块破坏与物品栏请求—响应路径发生替换。
- 字段表示扩张：字段可能从固定枚举演进为枚举或字符串变体，也可能新增可选字段与读写顺序修正。

## 近期重点文件与兼容性关注点

| 来源文件 | 关键变化 | 兼容性关注点 |
|---|---|---|
| `previous_changelogs\changelog_893_11_07_25.md` | 首轮显性Cereal迁移，涉及`CommandRequestPacket`、`CommandOutputPacket`、`AnimatePacket`、`InteractPacket`、`AvailableCommandsPacket`、`LegacyTelemetryEventPacket`、`ClientboundControlSchemeSetPacket`等；`TextPacket`调整消息体判别方式；`StartGamePacket`移除`mTickDeathSystemsEnabled`。 | 旧解析器不能再假定文本包与若干命令类数据包沿用原布局，登录阶段字段也需要按目标版本复核。 |
| `previous_changelogs\changelog_924_01_21_26.md` | `ServerBoundDiagnosticsPacket`新增客户端内存分类数据；`StartGamePacket`新增服务端遥测数据与加入信息；数据存储包开始跟踪路径更新；同时引入纹理偏移、体素形状、相机样条等新协议面。 | 登录元数据与诊断负载继续扩大，服务端若忽略新字段，可能导致诊断或会话配置能力失配。 |
| `previous_changelogs\changelog_944_03_04_26.md` | 新增数据包ID段330至347，包括数据存储、图形参数覆盖、数据驱动界面、纹理偏移、体素形状、世界时钟同步、属性层同步、商店信息与存在信息。 | 包ID表不应静态写死到旧范围；代理、抓包器和多版本库都应及时刷新分发表。 |
| `previous_changelogs\changelog_975_04_22_26.md` | `PlayerEnchantOptionsPacket`与`MobEquipmentPacket`转为Cereal；`ServerBoundDiagnosticsPacket`继续扩大到实体系统诊断；`ServerStoreInfoPacket`与`ServerPresenceInfoPacket`用于下发`ClientStoreEntryPointConfiguration`与`PresenceConfiguration`。 | 诊断、商店入口与存在信息已经成为运行期协议的一部分，不再只是外围平台功能。 |
| `changelog_1001_05_18_26.md` | `SubChunkRequestPacket`、`BossEventPacket`、`InventoryTransactionPacket`、`MobArmorEquipmentPacket`、`ClientCacheBlobStatusPacket`、`InventoryContentPacket`继续转向Cereal；`LevelSoundEventPacket`将`mSoundEvent`改为`SoundEventIdentifier`；`StartGamePacket`新增`isChatLogging`；`PresenceConfiguration`新增`richPresenceId`并将`mExperienceName`、`mWorldName`改为可选。 | 区块请求、缓存状态、物品栏与声音事件路径均出现破坏性变化，登录阶段还增加了聊天记录与存在信息字段，宜作为最新适配的最高优先级。 |

## 本轮新增落地点

- 概念补充页：[网络协议](../../docs/server/protocol.md)
- 原文脉络页：[基岩版协议库翻译分区](../../translations/protocol/index.md)
- 近期摘录页：[近期变更摘录](../../translations/protocol/recent-changelog-highlights.md)

## 使用建议

1. 先锁定目标协议版本，再对照相邻版本变更日志逐条复核。
2. 对出现`Converted to Cereal`的数据包，优先重做读写顺序验证。
3. 对服务端权威相关功能，需同时核对`StartGamePacket`开关、输入包和修正包三处行为。
4. 对区块与缓存系统，需同时核对`LevelChunkPacket`、`SubChunkRequestPacket`、`SubChunkPacket`与`ClientCacheMissResponsePacket`。
5. 对登录与会话配置路径，需额外复核`StartGamePacket`、`ServerStoreInfoPacket`、`ServerPresenceInfoPacket`、`GraphicsOverrideParameterPacket`与`ServerBoundDiagnosticsPacket`。
