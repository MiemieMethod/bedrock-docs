# 基岩版服务端软件生态

本文用于汇总Minecraft基岩版服务端软件与插件加载器生态的常见项目、技术路线和历史快照。本文是项目索引，不是功能等价声明；同名能力在不同服务端中往往由不同实现提供。

## 生态分层

| 分层 | 典型项目 | 说明 |
|------|----------|------|
| 官方服务端 | BDS | Mojang官方基岩版专用服务器，不提供通用第三方插件系统。 |
| 基于BDS的插件加载器 | LeviLamina、Endstone | 以BDS进程为运行基础，通过挂钩、包装或注入扩展服务端能力。 |
| 自实现服务端 | Allay、SerenityJS、Nukkit-MOT、PowerNukkitX、PocketMine-MP | 不依赖BDS二进制接口，自行实现协议、世界与插件系统。 |

## 当前重点项目

| 项目 | 技术路线 | 主要语言生态 | 插件或模组形态 | 备注 |
|------|----------|--------------|----------------|------|
| BDS | 官方服务端 | 无通用插件API | 主要依赖附加包与脚本API | 官方维护。 |
| LeviLamina | 基于BDS | C++ | 原生模组 | LiteLoaderBDS继任生态。 |
| Endstone | 基于BDS | Python、C++ | 插件 | 面向高层插件API。 |
| Allay | 自实现服务端 | Java、Kotlin等JVM语言 | 插件 | API与服务端实现分离。 |
| SerenityJS | 自实现服务端 | TypeScript、JavaScript | 插件与嵌入式服务端代码 | 面向Node.js与Bun生态。 |
| Nukkit-MOT | 自实现服务端 | Java | 插件 | 支持中国版客户端连接相关能力<!-- md:flag china -->。 |
| PowerNukkitX | 自实现服务端 | Java | 插件 | Nukkit分支之一。 |
| PocketMine-MP | 自实现服务端 | PHP | 插件 | 历史较久、生态成熟。 |

## 社区历史快照（EaseCation资料）

以下统计来自EaseCation Wiki相关页面的历史快照，反映的是该资料记录时的社区项目分布，不保证与当前实时状态一致。

| 语言 | 仍活跃项目数 | 已停更项目数 |
|------|--------------|--------------|
| PHP | 4 | 38 |
| Java | 4 | 14 |
| C++ | 1 | 5 |
| TypeScript | 4 | 1 |
| Go | 1 | 5 |
| JavaScript | 1 | 6 |
| Rust | 1 | 1 |
| C# | 0 | 3 |
| C | 0 | 1 |
| Python | 1 | 2 |
| D | 0 | 1 |
| Kotlin | 0 | 1 |

## 历史快照中的活跃项目名单

### C++

- LiteLoader

### Go

- DragonFly

### Java

- JukeBoxMC
- NukkitX-version
- NukkitPetteriM1Edition
- PowerNukkitX

### TypeScript

- BDSX
- JSPrismarine
- PowerAllay
- Serenity

### JavaScript

- GreenFrogMCBE

### Rust

- Netrex

### PHP

- BetterAltay
- PocketMine-MP
- NetherGamesMC/PocketMine-MP
- Symply

### Python

- PieMC

## 相关页面

- [插件加载器](../../docs/server/plugin-loader.md)
- [基岩版专用服务器](../../docs/server/bds.md)
- [Nukkit-MOT](../../docs/server/nukkit-mot.md)
- [PocketMine-MP](../../docs/server/pocketmine-mp.md)
- [网络协议](../../docs/server/protocol.md)