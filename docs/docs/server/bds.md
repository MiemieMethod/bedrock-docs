# 基岩版专用服务器

**基岩版专用服务器（Bedrock Dedicated Server）**，通称**BDS**，是Mojang Studios官方发布的Minecraft基岩版多人游戏服务器软件。BDS允许玩家在不依赖第三方平台的前提下搭建和运营自己的多人游戏服务器。

## 概述

BDS是目前基岩版生态中唯一的官方服务器软件，使用与客户端相同的基岩版引擎运行。BDS支持Windows和Linux（Ubuntu）平台，以命令行方式运行，没有图形界面。

BDS可以从Minecraft官方网站免费下载。每当游戏发布新版本时，BDS通常会同步发布对应版本的更新。BDS的版本号必须与客户端的版本号匹配，否则客户端无法连接。

## 功能

BDS提供以下核心功能：

- **多人游戏**：允许多位玩家同时连接到同一个世界进行游戏。
- **附加包支持**：支持在服务器上加载行为包和资源包。资源包会在玩家连接时自动推送给客户端。
- **命令系统**：支持所有基岩版命令，可通过服务器控制台执行。
- **权限管理**：通过配置文件管理操作员、白名单和封禁列表。
- **世界备份**：支持通过命令对当前世界进行热备份。

## 配置

BDS的行为通过{{file|server.properties|txt}}文件进行配置。主要配置项包括：

| 配置项 | 说明 |
|--------|------|
| `server-name` | 服务器名称，显示在服务器列表中 |
| `gamemode` | 默认游戏模式 |
| `difficulty` | 游戏难度 |
| `max-players` | 最大玩家数量 |
| `server-port` | 服务器IPv4端口 |
| `server-portv6` | 服务器IPv6端口 |
| `level-name` | 世界名称 |
| `level-seed` | 世界种子 |
| `online-mode` | 是否要求Xbox Live认证 |
| `allow-cheats` | 是否允许使用作弊命令 |
| `view-distance` | 服务器允许的最大视距 |
| `tick-distance` | 模拟距离 |

## 权限文件

BDS使用以下JSON文件管理玩家权限：

- {{file|permissions.json}}：定义操作员列表及其权限级别。
- {{file|allowlist.json}}：白名单，仅允许列表中的玩家连接。

## BDS与插件加载器

BDS本身不提供插件系统。社区开发的插件加载器（如LeviLamina、Endstone等）通过注入或挂钩BDS进程的方式为其扩展插件加载能力。使用这些插件加载器需要与BDS配合部署。

## 局限性

- BDS不支持从Minecraft Realms导入世界。
- BDS的性能受限于单线程的游戏逻辑，大规模多人服务器可能需要额外优化。
- BDS不提供原生的跨版本兼容支持，客户端和服务端版本必须严格匹配。
