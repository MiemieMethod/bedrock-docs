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

## 本轮新增落地点

- 概念补充页：[网络协议](../../docs/server/protocol.md)
- 原文脉络页：[基岩版协议库翻译分区](../../translations/protocol/index.md)

## 使用建议

1. 先锁定目标协议版本，再对照相邻版本变更日志逐条复核。
2. 对出现`Converted to Cereal`的数据包，优先重做读写顺序验证。
3. 对服务端权威相关功能，需同时核对`StartGamePacket`开关、输入包和修正包三处行为。
4. 对区块与缓存系统，需同时核对`LevelChunkPacket`、`SubChunkRequestPacket`、`SubChunkPacket`与`ClientCacheMissResponsePacket`。
