# 插件加载器

**插件加载器（Plugin Loader）**是Minecraft基岩版服务端生态中负责加载、管理和运行插件的核心软件组件。插件加载器为插件提供运行环境和API接口，使开发者能够编写扩展服务端功能的程序。

## 概述

基岩版没有官方提供的服务端插件接口（不同于Java版的Bukkit API等），因此社区开发了多种第三方服务端软件和插件加载器来填补这一空缺。不同的插件加载器在技术路线、支持的编程语言、API设计和生态规模上各有差异。

插件加载器大致可以按其底层技术分为两类：基于BDS的插件加载器和自实现服务端。

## 基于BDS的插件加载器

**BDS**即Bedrock Dedicated Server，是Mojang官方发布的基岩版专用服务端软件。基于BDS的插件加载器通过各种技术手段（如函数hook、内存修改、符号注入等）拦截和扩展BDS的原生功能。

值得注意的是，BDS自1.21.10版本起移除了符号（即映射表），使基于符号注入和静态分析的BDS-Based方案的开发和维护难度大幅上升，导致部分此类项目停止维护，社区生态中自实现服务端的比例因此有所提升。

### LeviLamina

LeviLamina是当前活跃的基于BDS的第三方模组加载器。它是LiteLoaderBDS的继任项目，核心面向C++原生模组开发，通过预加载、钩子和公共API接入BDS或受支持的Windows客户端。LeviLamina生态使用lip包管理器进行安装、分发和版本管理。关于其定位、架构和限制，见[LeviLamina](levilamina.md)。

### Endstone

Endstone是一个基于BDS的插件加载器与插件API，旨在提供类似于Java版Bukkit的高层接口。Endstone通过运行时挂钩和包装BDS对象，为Python和C++插件提供命令、事件、权限、调度器、表单、记分板、物品栏和NBT等接口。关于其定位、架构和限制，见[Endstone](endstone.md)。

## 自实现服务端

自实现服务端不依赖BDS，而是从头实现基岩版的服务端逻辑（包括网络协议、世界管理、实体系统等）。

### Allay

Allay是使用Java语言从头实现的基岩版服务端软件，支持Java、Kotlin、Scala以及其他JVM语言编写插件。Allay将API和服务端实现分离，提供命令、事件、调度器、方块、物品、容器、表单、Boss栏、记分板、配置、国际化、权限、持久化数据容器以及自定义方块和物品等接口。关于其定位、架构和限制，见[Allay](allay.md)。

### SerenityJS

SerenityJS是使用Rust和TypeScript从头实现的基岩版服务端软件，面向Node.js和Bun生态的开发者。SerenityJS可以作为预构建服务器运行，也可以通过`@serenityjs/core`嵌入到Node.js项目中；其插件、事件、命令、自定义方块和协议相关接口均属于SerenityJS生态。关于其定位、架构和限制，见[SerenityJS](serenity.md)。

### Nukkit系列

Nukkit是最早的基岩版Java实现服务端之一，衍生出了多个分支版本：

- **Nukkit**：原始项目，目前已停止维护。
- **PowerNukkitX**：活跃的Nukkit分支，增加了对新版基岩版特性的支持。
- **Nukkit-MOT**：另一活跃的分支，额外支持中国版客户端的连接。<!-- md:flag china -->

### PocketMine系列

PocketMine-MP是使用PHP语言实现的基岩版服务端软件，是基岩版（原Pocket Edition）最早的第三方服务端之一。PocketMine-MP拥有成熟的插件生态和丰富的文档。

## 选择建议

不同的插件加载器适用于不同的场景：

- 追求与官方BDS最大兼容性和最丰富底层接口者，可选择LeviLamina。
- 偏好Python、C++或类Bukkit API设计者，可考虑Endstone。
- 偏好JVM生态、自实现服务端和Allay插件API者，可考虑Allay。
- 偏好TypeScript/JavaScript并希望从Node.js项目直接控制服务端者，可考虑SerenityJS。
- 偏好Nukkit兼容生态者，可考虑PowerNukkitX或Nukkit-MOT。
- 需要支持中国版客户端者，可考虑Nukkit-MOT。<!-- md:flag china -->
- 偏好PHP生态且需要成熟插件库者，可考虑PocketMine-MP。
