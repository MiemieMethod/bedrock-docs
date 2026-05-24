# NetherNet

**NetherNet**是Minecraft基岩版所使用的网络协议之一，基于WebRTC，主要用于Xbox Live会话的多人连接。

## 概述

基岩版采用多种网络协议栈处理不同来源的连接。其中，[RakNet](raknet.md)用于面向公网IP和端口的直接服务器连接（即外部服务器）；NetherNet则用于基于Xbox Live配对服务的连接，包括通过Xbox Live好友列表、邀请或Realms加入游戏的场景。

NetherNet基于WebRTC，通过Xbox Live的信令服务建立点对点或中继连接，因此不依赖固定的公网IP地址和端口即可在两台设备之间建立游戏连接。

NetherNet是一种相对较新的协议，目前在社区中的逆向分析和文档化程度尚不及RakNet。已知规格请参阅[df-mc/nethernet-spec](https://github.com/df-mc/nethernet-spec)。

## 实现

| 名称 | 说明 | 语言 |
|------|------|------|
| [go-nethernet](https://github.com/df-mc/go-nethernet) | Go实现（基本版本） | Go |
| [bedrock-crustaceans/nethernet](https://github.com/bedrock-crustaceans/nethernet) | Rust实现 | Rust |
| [node-nethernet](https://github.com/PrismarineJS/node-nethernet) | Node.js实现 | JavaScript/TypeScript |