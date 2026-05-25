---
title: 创作与呈现数据包译文
---

# 创作与呈现数据包译文

/// details-info | 来源信息
- 原文仓库：[github.com/Mojang/bedrock-protocol-docs](https://github.com/Mojang/bedrock-protocol-docs)
- 对应页面：`docs/EditorNetworkPacket.html`、`docs/ClientboundDataDrivenUIShowScreenPacket.html`、`docs/GraphicsOverrideParameterPacket.html`、`docs/ServerPresenceInfoPacket.html`、`docs/ClientboundUpdateSoundDataPacket.html`
- 对应结构文件：`json/EditorNetworkPacket.json`、`json/ClientboundDataDrivenUIShowScreenPacket.json`、`json/GraphicsOverrideParameterPacket.json`、`json/ServerPresenceInfoPacket.json`、`json/ClientboundUpdateSoundDataPacket.json`
- 对应版本：Minecraft1.26.30，协议版本1001
- 许可说明：以原仓库或原站点公开许可声明为准。
///

这一页把当前协议库里几类和创作工具、界面调度、图形覆盖、存在信息与声音控制直接相关的数据包整理到一起，便于快速判断最近的协议范围已经扩展到了哪里。

## 总览

| 数据包 | ID | 方向或范围 | 当前公开作用 |
| --- | --- | --- | --- |
| `EditorNetworkPacket` | 190 | 编辑器会话内 | 承载编辑器专用的通用序列化载荷。 |
| `GraphicsOverrideParameterPacket` | 331 | 服务端→客户端 | 下发图形参数覆盖。 |
| `ClientboundDataDrivenUIShowScreenPacket` | 333 | 服务端→客户端 | 要求客户端显示数据驱动界面屏幕。 |
| `ServerPresenceInfoPacket` | 347 | 服务端→客户端 | 下发存在信息配置。 |
| `ClientboundUpdateSoundDataPacket` | 348 | 服务端→客户端 | 更新服务器声音句柄对应的声音数据。 |

这些条目共同说明：当前协议已经不只是“让玩家进服、同步实体、同步区块”，还直接覆盖了编辑器工作流、运行期界面调度、图形表现、会话展示与声音控制。

## `EditorNetworkPacket`

来源页将它描述为“编辑器专用的通用用途数据包”，用于承载各个编辑器载荷类型自行序列化后的数据。

当前结构只有三个字段：

| 字段 | 类型 | 索引 | 含义 |
| --- | --- | --- | --- |
| `Route To Manager` | `boolean` | 0 | 是否把该载荷路由到管理器侧处理路径。 |
| `Raw Variant Name` | `string` | 1 | 当前载荷变体名。 |
| `Raw Variant Data` | `string` | 2 | 当前变体的原始序列化数据。 |

这一结构的关键信号在于：协议层只保证“路由标记+变体名+原始数据”这三个外壳字段，而不在这一页继续展开具体编辑器消息体。换言之，编辑器会话已经拥有独立的数据包通道，但实际载荷细节仍由更上层的编辑器网络负载类型决定。

## `ClientboundDataDrivenUIShowScreenPacket`

来源页将它描述为“允许服务端告知客户端显示一个数据驱动界面屏幕”。

当前结构如下：

| 字段 | 类型 | 索引 | 含义 |
| --- | --- | --- | --- |
| `ScreenId` | `string` | 0 | 要显示的屏幕标识符。 |
| `FormId` | `uint32` | 1 | 该界面实例的唯一标识符，用于脚本侧跟踪。 |
| `DataInstanceId` | `uint32` | 2 | 与该界面实例关联的数据实例标识符，可选。 |

这里最值得注意的是`FormId`与`DataInstanceId`的并存：前者标记“这是哪一个界面实例”，后者标记“它附带的是哪一份数据实例”。这意味着协议层里的数据驱动界面已经不仅是一次性弹窗，而更接近可被脚本跟踪、可和运行期数据绑定的界面实例。

## `GraphicsOverrideParameterPacket`

来源页将它描述为“当服务端脚本修改渲染设置时，由服务端发送给客户端的数据包”。

当前结构比普通同步包更像一组图形参数命令：

| 字段 | 类型 | 索引 | 含义 |
| --- | --- | --- | --- |
| `Parameter Keyframe Values` | `object<float, Vec3>` | 0 | 以一天中的时间值为键、以`Vec3`为值的关键帧映射，最多255项。 |
| `Float Value` | `float` | 1 | 单个浮点参数值。 |
| `Vec3 Value` | `Vec3` | 2 | 单个三分量参数值。 |
| `Biome Identifier` | `string` | 3 | 该覆盖要应用到哪个生物群系。 |
| `Player Identifier` | `string` | 4 | 该覆盖要应用到哪个玩家，可选。 |
| `Identifier for Parameter` | `uint8`枚举 | 5 | 指定当前修改的是哪一种图形参数。 |
| `Reset Parameter` | `boolean` | 6 | 为真时重置目标参数；为假时按包中数据设置参数。 |

其中，参数枚举当前已经覆盖多类图形项目，例如：

- 天空颜色与地平线混合，例如`SkyZenithColor`、`SkyHorizonColor`、`HorizonBlendMin`、`HorizonBlendMax`。
- 大气散射相关参数，例如`RayleighStrength`、`SunMieStrength`、`MoonMieStrength`。
- 水体波浪相关参数，例如`WavesDepth`、`WavesFrequency`、`WavesSpeed`、`WavesShape`。
- 色调映射相关参数，例如`HighlightsContrast`、`MidtonesGamma`、`ShadowsSaturation`。
- 光照颜色与亮度相关参数，例如`SunColor`、`SunIlluminance`、`MoonColor`、`AmbientIlluminance`。

这一页透露出的信号非常明确：图形覆盖已经不只是“按生物群系切一套固定迷雾值”，而是允许服务端在运行期按参数类型、时间关键帧、目标生物群系，甚至按玩家粒度下发更细的呈现配置。

## `ServerPresenceInfoPacket`

来源页将它描述为“由服务端发送，用于向客户端提供`PresenceConfiguration`”。

当前包体只有一个`presence_configuration`字段，但其内部结构已经包含三项存在信息：

| 字段 | 类型 | 索引 | 含义 |
| --- | --- | --- | --- |
| `experienceName` | `string` | 0 | 当前体验名称。 |
| `worldName` | `string` | 1 | 当前世界名称。 |
| `richPresenceId` | `string` | 2 | 可选的富存在标识符，用于覆盖客户端自行驱动的存在信息。 |

这说明“玩家当前正在什么体验里、世界叫什么、存在信息如何展示”已经被纳入协议级配置，而不是只留在平台侧或客户端本地拼装。

## `ClientboundUpdateSoundDataPacket`

来源页将它描述为“用于更新声音数据”。

当前结构很小，但已经足以说明服务器声音控制正在独立成一条新路径：

| 字段 | 类型 | 索引 | 含义 |
| --- | --- | --- | --- |
| `Server Sound Handle` | `uint64`封装结构 | 0 | 服务器声音句柄。 |
| `Sound Event` | `int32`枚举 | 1 | 当前对该声音句柄执行的声音事件。 |

当前公开枚举值只有一个：

- `Stop`：停止该服务器声音句柄对应的声音。

虽然现阶段公开的动作还很少，但这里已经能看出协议在向“服务端维护声音句柄，再通过独立数据包更新其状态”的方向推进，而不再只依赖传统的关卡声音事件广播。

## 该如何使用这些页面

如果当前目标是追踪最新版协议的新增能力，可以按下面的顺序阅读：

1. 先看[协议库导览译文](index.md)，确认来源仓库的入口结构。
2. 再看本页，快速识别创作、界面、图形、存在信息与声音控制这几条新增协议面。
3. 需要整体理解时，继续看[网络协议](../../docs/server/protocol.md)。
4. 需要追逐版本变更时，再看[基岩版协议变更索引](../../refs/server/bedrock-protocol-changelog.md)。

## 相关页面

- [协议库导览译文](index.md)
- [项目说明页译文](source-readme.md)
- [网络协议](../../docs/server/protocol.md)
- [基岩版协议变更索引](../../refs/server/bedrock-protocol-changelog.md)
