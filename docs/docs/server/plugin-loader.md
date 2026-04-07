# 插件加载器

**插件加载器（Plugin Loader）**是Minecraft基岩版服务端生态中负责加载、管理和运行插件的核心软件组件。插件加载器为插件提供运行环境和API接口，使开发者能够编写扩展服务端功能的程序。

## 概述

基岩版没有官方提供的服务端插件接口（不同于Java版的Bukkit API等），因此社区开发了多种第三方服务端软件和插件加载器来填补这一空缺。不同的插件加载器在技术路线、支持的编程语言、API设计和生态规模上各有差异。

插件加载器大致可以按其底层技术分为两类：基于BDS的插件加载器和自实现服务端。

## 基于BDS的插件加载器

**BDS**即Bedrock Dedicated Server，是Mojang官方发布的基岩版专用服务端软件。基于BDS的插件加载器通过各种技术手段（如函数hook、内存修改、符号注入等）拦截和扩展BDS的原生功能。

### LeviLamina

LeviLamina是当前最为活跃的基于BDS的插件加载器。它是LiteLoaderBDS的继任项目，使用C++编写，通过hook BDS的原生函数来提供丰富的API。LeviLamina支持C++、JavaScript和Lua等语言编写的插件，并提供了lip包管理器用于插件的分发和版本管理。

### Endstone

Endstone是一个较新的基于BDS的插件加载器，旨在提供类似于Java版Bukkit的API设计。Endstone使用C++编写底层，但主要面向Python和C++开发者提供插件开发接口。

## 自实现服务端

自实现服务端不依赖BDS，而是从头实现基岩版的服务端逻辑（包括网络协议、世界管理、实体系统等）。

### Allay

Allay是使用Java语言从头实现的基岩版服务端软件，支持Java插件开发。Allay致力于提供高性能和高度可扩展的服务端架构。

### Nukkit系列

Nukkit是最早的基岩版Java实现服务端之一，衍生出了多个分支版本：

- **Nukkit**：原始项目，目前已停止维护。
- **PowerNukkitX**：活跃的Nukkit分支，增加了对新版基岩版特性的支持。
- **Nukkit-MOT**：另一活跃的分支，额外支持中国版客户端的连接。<!-- md:flag china -->

### PocketMine系列

PocketMine-MP是使用PHP语言实现的基岩版服务端软件，是基岩版（原Pocket Edition）最早的第三方服务端之一。PocketMine-MP拥有成熟的插件生态和丰富的文档。

### SerenityJS

SerenityJS是使用TypeScript/JavaScript语言实现的基岩版服务端软件，面向Node.js生态的开发者。

## 选择建议

不同的插件加载器适用于不同的场景：

- 追求与官方BDS最大兼容性和最丰富底层接口者，可选择LeviLamina。
- 偏好Python或类Bukkit API设计者，可考虑Endstone。
- 偏好Java生态且需要高度定制者，可考虑Allay或PowerNukkitX。
- 需要支持中国版客户端者，可考虑Nukkit-MOT。<!-- md:flag china -->
- 偏好PHP生态且需要成熟插件库者，可考虑PocketMine-MP。
- 偏好TypeScript/JavaScript者，可考虑SerenityJS。
