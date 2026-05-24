# LeviLamina

**LeviLamina**是面向Minecraft基岩版的第三方模组加载器。它以**基岩版专用服务器（Bedrock Dedicated Server）**，通称BDS，为主要运行基础，通过预加载、钩子和公共API为C++模组提供命令、事件、表单、服务访问、配置、数据存储、日志和底层内存操作等能力。

LeviLamina不是BDS的原生组成部分，也不是Mojang提供的官方插件系统。使用LeviLamina时，服务器仍然受BDS版本、平台、网络协议和二进制接口限制；LeviLamina提供的能力应理解为第三方加载器能力，而不是BDS原生能力。

若需要按原始文档脉络阅读，可先查看[LeviLamina文档归档](../../translations/levilamina/index.md)。

## 概述

LeviLamina是LiteLoaderBDS的继任项目。其官方资料将它描述为轻量级、模块化、多功能的基岩版模组加载器，目标是为基岩版提供必要的模组API和开发基础设施。与以高层抽象为主的插件API不同，LeviLamina更接近原生模组开发框架：开发者通常使用C++编写模组，并在需要时访问或拦截基岩版引擎内部对象。

LeviLamina官方文档也包含客户端安装与客户端构建相关内容。客户端侧能力属于LeviLamina客户端模组生态，不代表普通基岩版客户端原生支持加载第三方C++模组。

## 与BDS的关系

在服务端场景中，LeviLamina运行在BDS进程内。典型安装会生成或使用经过处理的{{file|bedrock_server_mod.exe}}启动程序，并将LeviLamina本体、运行时数据和模组文件放入服务器目录。PreLoader负责在进程启动阶段加载LeviLamina，随后LeviLamina再管理模组生命周期并提供公共API。

这种关系带来以下结果：

- LeviLamina服务器仍然以BDS世界、配置、资源包、行为包和网络协议为基础。
- LeviLamina版本必须匹配对应的BDS版本；BDS更新可能导致钩子、符号和内部布局发生变化。
- 模组可以使用LeviLamina封装的接口访问BDS内部对象，但未被公开或未被适配的内部能力不一定稳定可用。
- 崩溃、兼容性问题和性能问题可能来自BDS、LeviLamina、PreLoader、模组或它们之间的版本组合。

## 支持的版本

LeviLamina版本与BDS或客户端版本强绑定，具体对照应以[支持的版本](../../translations/levilamina/versions.md)为准。版本不匹配通常会直接表现为启动失败、依赖诊断报错或连接兼容性错误。

## 架构

LeviLamina的官方架构文档将项目分为通用代码、服务端专用代码和客户端专用代码。公共API位于`ll/api`，内部实现位于`ll/core`，基岩版引擎头文件位于`mc`。`mc`头文件来自对基岩版专用服务器和客户端的分析，用于描述引擎内部C++接口；这些头文件不是官方稳定SDK。

| 层级 | 作用 |
|------|------|
| `mc` | 描述基岩版引擎内部类型，例如`Player`、`Level`、`ServerInstance`、`CommandRegistry`和`Packet`。 |
| `ll/core` | 实现模组注册、原生模组加载、内置命令、崩溃记录和内部调整等LeviLamina核心功能。 |
| `ll/api` | 向模组开发者公开事件、命令、表单、配置、服务、协程、日志、数据、反射、网络和钩子等接口。 |

LeviLamina的服务端构建通过PreLoader加载到BDS进程，提供服务端事件和服务；客户端构建通过PreLoader加载到Windows版Minecraft客户端进程，提供输入、渲染和客户端生命周期相关能力。两者共享部分通用API，但并非所有模块都在两个环境中可用。

## 安装与分发

LeviLamina生态通常通过lip安装和升级。官方安装流程会同时涉及LeviLamina本体、PreLoader、PeEditor、bedrock-runtime-data、CrashLogger和对应版本的BDS；手动安装时，`bedrock_server_mod.exe`和`plugins`目录是最容易识别的运行时产物。

如果网络环境受限，安装前通常还可以先配置Go模块代理、GitHub镜像或BDS下载镜像；升级时则应尽量在独立目录中完成，避免直接覆盖现有世界和配置。

模组包通常由`tooth.json`描述包名、版本、依赖、资源文件和放置位置，并可通过Bedrinth等包索引分发。对服主而言，LeviLamina是随BDS版本一起维护的运行时；对开发者而言，它也是一套原生C++模组框架。

## 模组模型

LeviLamina官方资料将被加载的扩展称为模组。服务端模组通常是C++项目，使用LeviLamina模组模板、xmake和Visual Studio2022工具链构建。模组通常包含以下信息：

- 模组元数据与包信息，例如名称、版本、依赖和安装位置。
- 生命周期代码，例如构造、启用和禁用阶段。
- 对LeviLamina API的调用，例如注册命令、订阅事件、显示表单和读写配置。
- 对基岩版内部对象的访问，例如玩家、世界、物品、命令源和命令输出。

LeviLamina教程特别强调，模组构造函数只应执行与游戏状态无关的初始化，例如日志、配置和数据库初始化。命令注册、事件订阅等需要游戏系统可用的操作，应放在启用阶段或相应的生命周期时机执行。

## API范围

LeviLamina的API覆盖基础类型、错误处理、配置、反射、模组生命周期、事件、命令、服务、表单、日志、国际化、协程、线程、游戏时间、数据结构、工具函数、内存钩子、自定义网络数据包和客户端输入等模块。概览见[LeviLamina API模块](../../refs/server/levilamina-api.md)。其中，`Mod`、`Command`、`Event`、`Form`、`I18n`和`Coroutine`是服务端开发最常接触的一组入口。

这些接口的可用性取决于LeviLamina版本、目标环境和底层BDS或客户端版本。低层内存、钩子和引擎内部访问接口尤其依赖二进制布局，通常比高层事件、命令和表单接口具有更高的兼容风险。

## 局限性

LeviLamina提供的扩展能力建立在非官方二进制接入之上，因此具有以下限制：

- Minecraft基岩版更新可能使旧版LeviLamina或旧模组失效。
- 模组之间可能因钩子顺序、依赖版本或对同一内部对象的修改而冲突。
- 低层接口需要开发者理解C++、BDS内部结构和内存安全问题。
- 客户端侧能力只适用于LeviLamina支持的客户端环境，不适用于所有平台和所有基岩版客户端。
- 官方资料中的版本表、安装命令和支持范围会随项目发布变化，应以LeviLamina当前官方文档和发行页为准。

## 进一步阅读

- [在服务器上安装](../../translations/levilamina/install-server.md)
- [构建指南](../../translations/levilamina/build-guide.md)
- [问题排除](../../translations/levilamina/troubleshooting.md)
- [常见问题](../../translations/levilamina/faq.md)
- [LeviLamina入门](../../guides/servers/levilamina.md)
- [LeviLamina API模块](../../refs/server/levilamina-api.md)
