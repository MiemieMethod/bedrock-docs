# 基岩版专用服务器

**基岩版专用服务器（Bedrock Dedicated Server）**，通称**BDS**，是Mojang Studios官方发布的Minecraft基岩版多人游戏服务器软件。BDS允许玩家在不依赖Realms或局域网房主的前提下搭建和运营持久运行的多人服务器。

## 概述

BDS是基岩版生态中的官方服务器软件，使用与客户端相同的基岩版引擎运行。BDS以命令行方式运行，不提供图形界面，适合部署在长期在线的Windows或Ubuntu Linux主机上。Microsoft Learn当前列出的推荐系统包括Windows10版本1703或更高版本、Windows Server2016或更高版本，以及Ubuntu Linux18或更高版本；其中Ubuntu是官方支持的Linux发行版。

BDS可以从Minecraft官方网站免费下载。官方提供正式版和预览版的Windows与Linux构建，不提供macOS构建。每当游戏发布新版本时，BDS通常会同步发布对应版本。由于基岩版网络协议会随版本变化，客户端与服务器必须使用兼容的游戏版本，否则会出现“客户端过旧”或“服务器过旧”等连接错误。预览版BDS也需要预览版客户端连接。

## 功能

BDS提供以下核心功能：

- **多人游戏**：允许多位玩家同时连接到同一个世界进行游戏。
- **附加包支持**：支持在服务器上加载行为包和资源包。服务器可以在玩家连接时要求客户端下载资源包。
- **命令系统**：支持通过服务器控制台执行基岩版命令，常见命令包括`op`、`deop`、`gamerule`和`stop`。
- **权限与名单管理**：通过配置文件和命令管理操作员、允许列表和封禁列表。
- **世界管理**：通过{{file|worlds}}目录保存世界，并通过配置文件选择当前加载的世界。
- **脚本环境**：在启用相应实验性功能和模块权限时，可运行脚本API并使用BDS特有的服务端管理能力。

## 目录结构

BDS首次启动后会在安装目录生成运行所需的文件和目录。常见结构如下：

/// html | div.treeview
- BDS根目录
    - {{file|bedrock_server.exe}}
    - {{file|server.properties|txt}}
    - {{file|allowlist.json}}
    - {{file|permissions.json}}
    - {{file|worlds}}
        - 世界目录
            - {{file|behavior_packs}}
            - {{file|resource_packs}}
    - {{file|behavior_packs}}
    - {{file|resource_packs}}
    - {{file|config}}
///

{{file|worlds}}目录保存服务器可以加载的世界。BDS同一时间只加载一个世界，具体由{{file|server.properties|txt}}中的`level-name`指定。世界目录内部的{{file|behavior_packs}}和{{file|resource_packs}}只对该世界生效；BDS根目录下的同名目录则提供跨世界共享的包。

## 配置

BDS的主要行为由{{file|server.properties|txt}}文件控制。该文件是INI风格的键值配置文件，每行使用`key=value`表示一个设置，井号`#`开头的行表示注释。常见配置项包括：

| 配置项 | 说明 |
|--------|------|
| `server-name` | 服务器名称，显示在服务器列表中 |
| `gamemode` | 新玩家的默认游戏模式 |
| `force-gamemode` | 是否强制向客户端发送配置文件中的游戏模式 |
| `difficulty` | 世界难度 |
| `allow-cheats` | 是否允许使用作弊命令 |
| `max-players` | 最大玩家数量 |
| `online-mode` | 是否要求Xbox Live认证 |
| `allow-list` | 是否只允许允许列表中的玩家连接 |
| `server-port` | 服务器IPv4端口，默认`19132` |
| `server-portv6` | 服务器IPv6端口，默认`19133` |
| `level-name` | 当前加载或生成的世界目录名 |
| `level-seed` | 新世界使用的种子 |
| `view-distance` | 服务器允许的最大视距 |
| `tick-distance` | 围绕玩家保持模拟的区块距离 |

完整属性、默认值和取值范围见[BDS的server.properties](../../refs/server/bds-server-properties.md)参考。

## 权限与允许列表

BDS使用多个JSON文件保存玩家访问和权限信息：

- {{file|permissions.json}}：定义操作员及其权限级别。
- {{file|allowlist.json}}：保存允许列表。仅当`allow-list`为`true`时生效。

允许列表条目通常包含玩家名、可选的XUID，以及是否忽略玩家上限的标记。可以通过`allowlist add <玩家名>`、`allowlist remove <玩家名>`和`allowlist reload`命令维护允许列表，也可以直接编辑文件后重新加载。

## 与脚本API

BDS可以运行行为包中的脚本API代码，并额外提供部分更偏向服务器管理的实验性模块。脚本模块的默认权限位于{{file|config/default/permissions.json}}，也可以按行为包脚本模块UUID建立单独的配置目录，以便为不同脚本模块设置不同的允许模块列表。BDS脚本还可以通过配置文件提供变量和机密值，使服务器管理员能够调整脚本配置或安全地注入外部服务凭据。关于脚本API本身，见[脚本API](../addon/script-api.md)。

## 与编辑器

Windows版BDS可以承载编辑器项目。若使用`bedrock_server.exe Editor=true`从空世界启动，服务器会创建编辑器项目；也可以将已有编辑器项目复制到{{file|worlds}}目录，并在{{file|server.properties|txt}}中将`level-name`指向该项目。此时客户端连接会进入编辑器会话，客户端版本仍必须与服务器版本匹配。关于编辑器概念，见[编辑器](../general/editor.md)。

## BDS与插件加载器

BDS本身不提供通用插件系统。社区开发的插件加载器（如LeviLamina、Endstone等）通过注入、挂钩或包装BDS进程的方式为其扩展插件加载能力。使用这些插件加载器时，实际运行环境仍以BDS版本、平台和二进制接口为基础。

## 局限性

- BDS不提供原生跨版本兼容支持，客户端和服务端版本必须兼容。
- BDS同一进程同一时间只加载一个活动世界。
- BDS没有原生图形管理界面，日常管理依赖控制台、配置文件、脚本或第三方工具。
- BDS的性能受主机硬件、视距、模拟距离、脚本负载、玩家数量和网络环境影响，大规模多人服务器通常需要额外优化。
