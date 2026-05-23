# 脚本API<!-- md:flag vanilla -->

**脚本API（Script API）**是Minecraft基岩版提供的基于JavaScript的编程接口，允许附加包开发者通过编写脚本代码来与游戏世界进行交互。脚本API是附加包生态中功能最强大的扩展方式，能够实现数据驱动系统无法独立完成的复杂逻辑。

## 概述

脚本API由一系列**模块（Module）**组成，每个模块提供一组特定领域的功能接口。脚本代码以JavaScript文件的形式存放在行为包的`scripts/`目录中，游戏引擎在加载行为包时会启动一个JavaScript运行时环境来执行这些脚本。

脚本API的模块需要在行为包的清单文件中作为依赖声明，同时清单文件中需要包含一个类型为`script`的模块定义，并将`language`字段设置为`javascript`。

## 核心模块

脚本API的核心模块包括：

| 模块名称 | 描述 |
|----------|------|
| `@minecraft/server` | 服务端核心API，提供对实体、方块、维度、世界等游戏对象的访问和操控能力 |
| `@minecraft/server-ui` | 服务端UI模块，提供向玩家显示表单对话框的能力 |
| `@minecraft/server-gametest` | 游戏测试模块，提供自动化测试框架 |
| `@minecraft/server-admin` | 服务端管理模块，提供服务器配置的访问能力 |
| `@minecraft/server-net` | 网络模块，提供HTTP请求能力（仅BDS） |
| `@minecraft/server-editor` | 编辑器扩展模块，提供面向编辑器工具、面板和操作的接口 |

每个模块都有独立的版本号，遵循语义版本规范。部分模块的最新版本可能以`-beta`后缀标识实验性版本。

## 运行环境

脚本API可以在普通附加包世界、[基岩版专用服务器](../server/bds.md)和[编辑器](../general/editor.md)扩展环境中出现，但不同环境开放的模块并不完全相同。通用世界脚本主要依赖`@minecraft/server`和`@minecraft/server-ui`；BDS还提供面向服务端管理、网络通信和配置的实验性能力；编辑器扩展则依赖`@minecraft/server-editor`等编辑器相关模块。

BDS中的脚本模块权限由服务器配置控制。服务器首次运行后会创建{{file|config/default/permissions.json}}，其中保存默认允许脚本访问的内置模块列表。管理员还可以在{{file|config}}目录下按行为包脚本模块UUID建立独立配置目录，为不同脚本模块设置不同权限。此机制使服务器可以限制脚本可导入的模块范围，避免所有脚本共享过宽的默认权限。

Microsoft Learn当前说明，BDS额外脚本能力属于Beta APIs计划中的实验性功能，可能在后续版本中发生变化或被移除。这些能力适用于BDS环境，不适用于Minecraft Realms服务器。涉及外部服务连接、服务器管理控制台或自动化运维的脚本，应明确以BDS作为目标环境。

## 配置变量与机密值

BDS脚本环境允许服务器管理员通过配置文件向脚本提供可调整的值。{{file|variables.json}}可以定义脚本变量，脚本通过`@minecraft/server-admin`模块读取这些变量，用于控制难度、倍率、开关等可配置逻辑。

{{file|secrets.json}}用于保存机密值，例如外部服务令牌。机密值不会像普通变量一样在任意脚本上下文中直接暴露，而是只能在受限制的上下文中解析，例如构造某些网络请求头时使用。此设计用于降低脚本和配置文件直接泄露敏感数据的风险。

## 事件系统

脚本API采用**事件驱动（Event-Driven）**的编程模型。开发者通过订阅特定事件来响应游戏中发生的各种情况。事件分为两类：

### 前置事件

**前置事件（Before Event）**在行为发生之前触发，允许脚本取消该行为。例如，`world.beforeEvents.chatSend`在聊天消息发送之前触发，脚本可以通过设置`cancel`属性来阻止消息发送。

### 后置事件

**后置事件（After Event）**在行为发生之后触发，不可取消，主要用于对已发生的事件进行响应。例如，`world.afterEvents.entityHurt`在实体受到伤害之后触发。

## 脚本事件

**脚本事件（Script Event）**是一种从命令系统向脚本API传递消息的机制。通过`/scriptevent`命令发送的事件可以被脚本通过`system.afterEvents.scriptEventReceive`监听和处理，从而实现命令系统与脚本逻辑之间的通信。

## 系统调度

脚本API提供了基于刻的调度机制，允许脚本按照时间计划执行逻辑：

- `system.runTimeout(callback, delay)`：在指定的刻数后执行回调。
- `system.runInterval(callback, interval)`：每隔指定的刻数重复执行回调。
- `system.run(callback)`：在下一刻执行回调。

## TypeScript支持

虽然游戏引擎直接执行的是JavaScript代码，但开发者可以使用TypeScript编写脚本，然后在构建阶段将TypeScript编译为JavaScript。脚本API为所有模块提供了TypeScript类型声明文件，可以通过npm安装获取，以获得完整的类型检查和代码补全支持。

## 脚本引擎<!-- md:flag deprecated -->

**脚本引擎（Script Engine）**是脚本API的前身，是一套已被弃用的早期脚本系统。旧版脚本引擎提供了`client`和`server`两个脚本上下文，使用了不同于当前脚本API的接口设计。旧版脚本引擎已在较新的游戏版本中移除，所有新开发应使用当前的脚本API。

## 早期GameTest写法<!-- md:flag deprecated -->

早期GameTest实验性资料中可能出现`type`为`javascript`的清单文件模块、以UUID声明的`Minecraft`和`GameTest`模块依赖，以及`import * as GameTest from "GameTest"`、`import { BlockLocation } from "Minecraft"`等导入方式。这些写法属于1.16.210附近的历史API形态，不应作为当前脚本API教程使用。

当前脚本API使用`type`为`script`的清单文件模块，并通过`@minecraft/server`、`@minecraft/server-gametest`等模块名声明依赖和导入功能。维护旧包时若遇到早期GameTest写法，应按当前模块系统重新迁移。
