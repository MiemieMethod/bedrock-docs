# SerenityJS

**SerenityJS**是面向Minecraft基岩版的第三方自实现服务端软件。它以TypeScript工作区和多包结构组织，目标是在Node.js和Bun等JavaScript运行时中提供可编程、可嵌入的基岩版服务端能力。

SerenityJS不是BDS的插件加载器，也不是Mojang提供的官方服务端插件系统。其网络、协议、存档、方块、命令和插件接口均属于SerenityJS项目本身，不应视为BDS、官方脚本API或原版附加包系统的原生能力。

## 概述

SerenityJS的定位接近一个面向开发者的基岩版服务端框架。它既提供预构建的服务器可执行文件，也允许开发者在Node.js或Bun项目中直接创建`Serenity`实例，从而把服务器生命周期、世界提供器、事件监听器和自定义玩法逻辑组合到同一个应用程序中。

与基于BDS的插件加载器相比，SerenityJS不需要挂钩BDS进程，也不依赖BDS的封闭二进制接口。这使其可以用TypeScript公开较高层的服务器对象和工具，并在协议、世界数据和玩法逻辑实现上保持自身架构。与此同时，自实现服务端必须自行追踪基岩版协议、世界格式、方块与物品数据以及原版机制，因此其原版趋同程度取决于SerenityJS当前版本。

SerenityJS资料显示，项目处于活跃开发状态，并在靠近第一个稳定版本的过程中仍缺少部分原版功能。实际部署前应以当前发行说明、协议版本和项目文档为准。

## 架构

SerenityJS仓库以多个NPM包组织主要功能：

| 包 | 作用 |
|----|------|
| `@serenityjs/core` | 核心服务端结构与行为，包含`Serenity`实例、世界提供器、事件、方块类型、区块和子区块等实现。 |
| `@serenityjs/protocol` | 基岩版网络协议相关结构。 |
| `@serenityjs/raknet` | RakNet传输层相关实现。 |
| `@serenityjs/nbt` | NBT数据读写。 |
| `@serenityjs/data` | 服务端所需数据包与运行时数据。 |
| `@serenityjs/emitter` | 事件发射与监听基础设施。 |
| `@serenityjs/logger` | 日志输出。 |
| `@serenityjs/plugins` | 插件系统相关工具。 |
| `@serenityjs/internal-config` | 内部配置工具。 |

`@serenityjs/core`可以独立用于创建精简服务端软件。示例使用`LevelDBProvider`注册世界提供器，并通过`Serenity`实例启动服务器。这说明SerenityJS既是一个服务端程序，也是一组可嵌入的服务器库。

## 安装与运行模型

SerenityJS提供两种主要使用路径：

- 下载预构建服务器可执行文件。该方式更接近传统服主使用的服务端软件，通常依赖服务器目录和插件扩展。
- 使用`npm create serenity`、`yarn create serenity`或`pnpm create serenity`创建Node.js项目。该方式会初始化带有SerenityJS包的项目，更适合需要深度集成服务端逻辑的开发者。

当前仓库根工作区声明的运行时门槛为Node.js25及以上或Bun1.3.0及以上，并使用Yarn4工作区组织本体开发流程。计划直接修改SerenityJS仓库本体时，应先确认本机运行时版本满足这一要求。

如果需要修改SerenityJS本体，项目资料要求先安装Yarn，再在仓库中执行`yarn install`和`yarn build`，随后进入`devapp`目录通过`yarn dev`启动开发服务器。这属于SerenityJS本体开发流程，不是普通插件或服务器部署所必需的步骤。

## 事件模型

SerenityJS事件系统公开了`before`、`on`和`after`三类监听方式。三者表示不同的事件处理阶段：

| 阶段 | 语义 |
|------|------|
| `before` | 在其他监听器前执行。监听器可通过返回布尔值影响后续处理；资料示例使用返回`false`取消后续事件循环。 |
| `on` | 在同一进程刻中、`before`阶段之后执行。该阶段本身不用于取消事件。 |
| `after` | 在其他处理完成后，于后续进程刻执行。适合读取已经应用后的结果。 |

这种事件阶段属于SerenityJS的事件基础设施。它与官方脚本API中的事件阶段、BDS内部事件或其他插件加载器的事件系统不是同一套接口。

## 命令系统

SerenityJS命令按世界注册。每个世界实例通过`commandPalette`维护自己的命令集合，因此不同世界可以拥有不同的命令集。这种“按世界暴露命令”的设计是SerenityJS命令系统的重要特征，不应简单类比为所有世界共享一张全局命令表。

命令注册过程通常包含命令名称、描述、可选的注册器函数和执行器函数。注册器函数可声明权限、调试标记和重载；重载用于定义不同参数结构。示例使用`TargetEnum`表示目标参数，并通过继承`CustomEnum`定义自定义枚举参数。

执行器可以读取命令上下文中的`origin`、参数结果和目标实体，并返回消息对象或抛出错误。此命令系统是SerenityJS服务端框架提供的API，不属于Minecraft原生命令系统本身。

## 自定义方块

SerenityJS允许通过`CustomBlockType`创建自定义方块类型。方块类型使用赋命名空间标识符表示，并可设置组件、方块置换和方块萃取。

自定义方块模型包含以下概念：

- 基础组件：例如发光等级、几何体标识符、材质实例、是否可交互等。
- 方块置换：通过状态集合创建同一方块类型的不同变体，状态值可以是字符串、数字或布尔值。
- 方块萃取：通过继承`BlockTrait`定义可复用行为，例如在交互时切换方块状态。
- 方块调色板注册：通过世界实例的`blockPalette.registerType()`注册方块类型，也可以注册方块萃取。

SerenityJS文档指出其方块组件设计与原版附加包中的自定义方块组件相近，便于将附加包中的自定义方块概念迁移到SerenityJS中。但这种迁移仍发生在SerenityJS服务端运行时中，不表示BDS或官方附加包系统可以直接执行SerenityJS的TypeScript代码。

## 插件系统

SerenityJS插件用于对基础服务端软件进行服务端侧修改或扩展。当前工作区单独提供`@serenityjs/plugins`包，`devapp`也直接依赖该包，说明插件系统仍是当前SerenityJS工作区中的独立组成部分。

SerenityJS插件运行在SerenityJS服务端中。它们不能直接放入BDS、LeviLamina、Endstone、Allay、Nukkit或PocketMine-MP中运行；其他服务端的插件也不能直接作为SerenityJS插件使用。

## 局限性

SerenityJS作为自实现服务端具有以下限制：

- 原版机制、方块行为、实体行为、世界生成和红石等内容需要由SerenityJS逐步实现，不能默认等同于BDS。
- 基岩版协议版本更新可能要求SerenityJS同步更新`@serenityjs/protocol`、`@serenityjs/raknet`和相关运行时数据。
- 自定义方块、命令、事件和插件能力受SerenityJS当前API范围限制，不代表官方客户端或BDS具备相同能力。
- 项目变更记录多数仅为版本初始化信息，对具体兼容范围和功能完整性说明有限；实际使用时仍应查阅当前发行页和源码类型定义。