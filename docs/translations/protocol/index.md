---
title: 基岩版协议库
---

# 基岩版协议库翻译

/// details-info | 来源信息
- 原文仓库：[github.com/Mojang/bedrock-protocol-docs](https://github.com/Mojang/bedrock-protocol-docs)
- 对应页面：`index.html`、`docs/index.html`
- 许可说明：以原仓库或原站点公开许可声明为准。
///

本页整理基岩版协议库当前可直接浏览的HTML入口，便于先判断该仓库该从哪里查数据包结构、字段类型和版本变化。

## 页面结构

当前仓库同时保留两套浏览入口：

| 入口 | 位置 | 适合查看的内容 |
| --- | --- | --- |
| 表格式入口 | `index.html` | 类型表、枚举表、数据包表、游戏数据包头、RakNet可靠性头 |
| 数据包文档入口 | `docs/index.html` | 当前数据包列表，以及每个数据包的说明、字段索引和嵌套类型展开 |

根页面直接给出五个入口：Types Table、Enumerations Table、Packets Table、Packet Header、RakNet Header。若已经知道自己要查的是“类型”“枚举”还是“包头”，从这里进入最快。

`docs/index.html`则更接近按包名浏览的手册。当前页面列出203个数据包，并在每个条目旁给出数据包ID和简短说明。

## 单个数据包页面能看到什么

- 数据包标题与数据包ID。
- 一段简短描述，用来判断数据包的大致用途。
- 字段表，包含字段名、类型、字段索引与补充说明。
- 若字段本身引用复合类型，页面会继续展开子结构或枚举值。

这种结构特别适合核对“某个字段现在还在不在”“顺序有没有变化”“某个枚举值现在有哪些成员”。

## 当前HTML文档透露出的协议范围

当前HTML页面中，协议已经不只覆盖登录、移动和区块同步，还直接覆盖创作、界面、图形和存在信息等运行期通道。例如：

| 数据包 | ID | 当前页面可见的结构信号 |
| --- | --- | --- |
| `EditorNetworkPacket` | 190 | 使用“Route To Manager + Raw Variant Name + Raw Variant Data”传输编辑器侧载荷。 |
| `ClientboundDataDrivenUIShowScreenPacket` | 333 | 服务端可要求客户端显示数据驱动界面，并携带`ScreenId`、`FormId`与可选`DataInstanceId`。 |
| `GraphicsOverrideParameterPacket` | 331 | 可下发图形参数关键帧映射，以及单独的浮点值或`Vec3`值。 |
| `ServerPresenceInfoPacket` | 347 | 直接传递`PresenceConfiguration`，其中包含`experienceName`、`worldName`与`richPresenceId`。 |
| `ClientboundUpdateSoundDataPacket` | 348 | 使用服务器声音句柄和字符串形式的声音事件更新声音数据。 |

这些条目说明：现在查协议时，不能只盯着传统玩法同步路径，也要同步关注界面调度、图形覆盖、声音控制和会话呈现配置。

## 建议的阅读顺序

1. 先看[项目说明页译文](source-readme.md)，了解协议库的用途和版本视角。
2. 再看[网络协议](../../docs/server/protocol.md)，先建立协议层次、登录流程和服务端权威机制的整体概念。
3. 需要追版本差异时，继续看[基岩版协议变更索引](../../refs/server/bedrock-protocol-changelog.md)。
4. 已经锁定具体数据包后，再回到来源仓库中的HTML页面逐字段核对。

## 相关页面

- [项目说明页译文](source-readme.md)
- [网络协议](../../docs/server/protocol.md)
- [基岩版协议变更索引](../../refs/server/bedrock-protocol-changelog.md)
- [RakNet](../../docs/server/raknet.md)
