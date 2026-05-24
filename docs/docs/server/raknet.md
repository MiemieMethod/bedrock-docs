# RakNet

**RakNet**是一套跨平台、开源的C++游戏网络引擎，最初由Jenkins Software开发，后移交至Facebook Archive进行维护。Minecraft基岩版将RakNet**（RakNet）**用作面向外部服务器连接的主要传输层协议。

## 概述

RakNet基于UDP，在其上提供可靠性保证、数据包排序、分片重组和连接管理等功能，使游戏网络通信在低延迟的UDP基础上具有类TCP的可靠性。

基岩版默认使用端口**19132**（IPv4）和**19133**（IPv6）进行RakNet通信，端口可按需更改。

RakNet中的未连接消息（如Unconnected Ping与Unconnected Pong）携带一个固定的16字节离线消息标识，通称**Magic**：

```
0x00ffff00fefefefefdfdfdfd12345678
```

每个RakNet数据包的第一个字节为包类型标识符。

## 数据类型

| 类型 | 大小（字节） | 范围 | 说明 |
|------|------|------|------|
| `u8`（byte） | 1 | 0–255 | 单字节无符号整数 |
| `i16`（short） | 2 | −32768–32767 | 有符号16位整数 |
| `u16`（unsigned short） | 2 | 0–65535 | 无符号16位整数 |
| `u24`（unsigned int24） | 3 | 0–2²⁴−1 | 无符号24位整数 |
| `i64`（long） | 8 | −2⁶³–2⁶³−1 | 有符号64位整数 |
| `bool`（boolean） | 1 | 0–1 | `0`为`false`，`1`为`true` |
| `String` | 不定 | — | 以大端序u16前缀表示长度，后跟字节序列 |
| `Guid` | 8 | — | 以i64存储的全局唯一标识符 |
| `Socket Address` | 7 | — | 1字节IP版本（4/6），4字节IP地址，2字节端口 |
| `Magic` | 16 | — | 常量字节序列`0x00ffff00fefefefefdfdfdfd12345678` |

## MOTD格式

服务器在Unconnected Pong中向客户端广播其MOTD。MOTD是以分号`;`分隔的字符串，格式如下：

```
版本标识;MOTD第一行;协议版本;版本名;当前玩家数;最大玩家数;服务端唯一ID;MOTD第二行;游戏模式;游戏模式（数字）;IPv4端口;IPv6端口;
```

版本标识字段取值为`MCPE`（基岩版）或`MCEE`（教育版）。游戏模式和游戏模式数字字段目前不被原版客户端使用。

示例：

```
MCPE;Dedicated Server;527;1.19.1;0;10;13253860892328930865;Bedrock level;Survival;1;19132;19133;
```

## 连接流程

RakNet连接的建立分为**握手阶段**和**连接阶段**。握手阶段用于发现服务端并协商MTU大小；连接阶段在握手完成后正式建立可靠通道。

### 握手阶段

握手阶段共4个数据包：

**Open Connection Request 1**（客户端→服务端）

```
0x05 | Magic | 协议版本（当前为11，即0x0b）| 空白填充
```

空白填充用于探测网络MTU。客户端以递减的填充大小不断重试，直到服务端回复。

**Open Connection Reply 1**（服务端→客户端）

```
0x06 | Magic | 服务端GUID | 是否有安全性（bool）| Cookie（u32，仅当有安全性时）| MTU大小（u16）
```

**Open Connection Request 2**（客户端→服务端）

```
0x07 | Magic | Cookie（u32，仅当有安全性时）| 客户端是否支持安全性（bool，原版始终为false）| 服务端地址 | MTU大小（u16）| 客户端GUID（i64）
```

**Open Connection Reply 2**（服务端→客户端）

```
0x08 | Magic | 服务端GUID（i64）| 客户端地址 | MTU大小（u16）| 是否有安全性（bool）
```

自此，RakNet连接建立，后续所有RakNet消息均通过**帧集合数据包（Frame Set Packet）**传输。

### 连接阶段

连接阶段共3个数据包：

**Connection Request**（客户端→服务端）

```
0x09 | 客户端GUID（i64）| 请求时间戳（i64）| 是否安全（bool）
```

**Connection Request Accepted**（服务端→客户端）

```
0x10 | 客户端地址 | 系统索引（i16）| 系统地址数组 | Ping时间（i64）| Pong时间（i64）
```

**New Incoming Connection**（客户端→服务端）

```
0x13 | 服务端地址 | 内部地址数组 | 客户端发送时间（u64）| 服务端发送时间（u64）
```

### 连接保活

连接建立后，双方须周期性交换**Connected Ping**与**Connected Pong**以维持连接：

- **Connected Ping**：`0x00 | 时间戳（u64）`（以不可靠方式传输）
- **Connected Pong**：`0x03 | 客户端时间戳（u64）| 服务端时间戳（u64）`（以不可靠方式传输）

/// note | 批量发送
原版客户端通常将New Incoming Connection、Connected Ping以及第一个游戏数据包（Network Settings Request）合并为一批发送。自定义RakNet实现需注意处理此种情况，因为部分服务器可能未针对此模式进行测试。
///

## 与基岩版网络协议的关系

RakNet只负责传输层，基岩版游戏协议在RakNet连接建立之上运行。RakNet连接完成后，游戏层登录流程随即开始。详见[网络协议](protocol.md)。

## 实现

| 名称 | 说明 | 语言 |
|------|------|------|
| [RakNet（官方）](https://github.com/facebookarchive/RakNet) | 跨平台开源C++游戏网络引擎 | C++ |
| [bedrock-crustaceans/raknet](https://github.com/bedrock-crustaceans/raknet) | Rust实现 | Rust |
| [NetrexMC/RakNet](https://github.com/NetrexMC/RakNet) | Rust实现 | Rust |
| [rust-raknet](https://github.com/b23r0/rust-raknet) | Rust实现 | Rust |
| [tokio-raknet](https://github.com/iAldrich23xX/tokio-raknet) | 基于tokio异步生态的Rust实现 | Rust |
| [transport-raknet](https://github.com/CloudburstMC/Network/tree/develop/transport-raknet) | Java实现 | Java |
| [RakLib](https://github.com/pmmp/RakLib) | PHP服务端实现 | PHP |
| [go-raknet](https://github.com/Sandertv/go-raknet) | Go实现 | Go |
| [raknet-python](https://github.com/raknet-python/raknet-python) | Python绑定 | Python |
| [JSPrismarine/raknet](https://github.com/JSPrismarine/JSPrismarine/tree/master/packages/raknet) | JavaScript/TypeScript实现 | JavaScript/TypeScript |
