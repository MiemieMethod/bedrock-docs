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
- `system.runJob(generator)`：将一个生成器函数分散到多个刻中执行，适合大量数据的遍历处理。

## 执行权限

脚本API对不同执行阶段设有访问权限限制。**受限执行模式**（只读模式）在前置事件回调和脚本刻开始之前生效，此时不允许修改世界状态的调用；**早期执行模式**在世界加载完成之前生效（脚本API 2.0.0+），此时大多数世界查询API不可用。通过`system.run()`或`world.afterEvents.worldLoad`订阅可以脱离这两种受限状态。

## 看门狗

**看门狗（Watchdog）**是脚本引擎内置的性能监控系统，自1.19.20版本起默认启用。它监控脚本的执行时间和内存占用，在超出阈值时输出警告或终止行为包脚本运行，以防止脚本导致服务器崩溃或严重卡顿。

看门狗会在内容日志中以`[Watchdog]`标签输出警告和错误，常见消息如下：

- **Slow-running script detected** — 脚本平均执行时间超过阈值（默认2毫秒）。
- **script spike detected** — 单刻内脚本执行时间超过峰值阈值（默认100毫秒）。
- **script hang detected** — 脚本在单刻内冻结超过挂起阈值（默认3000毫秒），通常由`while`或`for`循环陷入无限迭代引起。
- **Stack overflow detected** — 存在无出口的递归函数调用。
- **Out of memory exception** — 内存占用超过内存上限（默认250 MB），触发后会保存并关闭世界，**无法**通过事件取消。
- **High memory usage detected** — 内存占用超过内存警告阈值（默认100 MB）。
- **Unhandled critical exception** — 出现了未被捕获的严重异常。

在BDS环境下，可以通过`server.properties`调整看门狗阈值；这些配置在普通世界和Realms中不可修改。

### 取消看门狗终止

脚本API允许通过`system.beforeEvents.beforeWatchdogTerminate`事件拦截看门狗终止行为（内存溢出除外）：

```javascript
import { system } from "@minecraft/server";

system.beforeEvents.beforeWatchdogTerminate.subscribe((event) => {
    event.cancel = true;
    console.warn(`[Watchdog] 拦截了${event.terminateReason}类型的终止`);
});
```

### 导出性能统计

在游戏中执行`/script watchdog exportstats`可以导出脚本引擎的性能分析数据，包括各行为包句柄和运行时信息。

## TypeScript支持

虽然游戏引擎直接执行的是JavaScript代码，但开发者可以使用TypeScript编写脚本，然后在构建阶段将TypeScript编译为JavaScript。脚本API为所有模块提供了TypeScript类型声明文件，可以通过npm安装获取，以获得完整的类型检查和代码补全支持。

## 模块UUID参考

每个脚本API模块拥有唯一的UUID，用于在`manifest.json`的`dependencies`中通过`uuid`字段（旧格式）引用。当前规范推荐使用`module_name`字段引用，不应同时使用两种方式。

| 模块名称 | UUID | 旧版名称/别名 | 首次可用引擎版本 |
|---|---|---|---|
| `@minecraft/common` | `77ec12b4-1b2b-4c98-8d34-d1cd63f849d5` | — | 1.20.40 |
| `@minecraft/debug-utilities` | `1796ea86-0daf-4409-99ee-fd6467cf1203` | — | 1.20.70 |
| `@minecraft/server` | `b26a4d4c-afdf-4690-88f8-931846312678` | `Minecraft`、`mojang-minecraft` | 1.16.210 |
| `@minecraft/server-ui` | `2bd50a27-ab5f-4f40-a596-3641627c635e` | `mojang-minecraft-ui` | 1.18.20 |
| `@minecraft/server-gametest` | `6f4b6893-1bb6-42fd-b458-7fa3d0c89616` | `GameTest`、`mojang-gametest` | 1.16.210 |
| `@minecraft/server-net` | `777b1798-13a6-401c-9cba-0cf17e31a81b` | `mojang-net` | 1.19.10 |
| `@minecraft/server-admin` | `53d7f2bf-bf9c-49c4-ad1f-7c803d947920` | `mojang-minecraft-server-admin` | 1.19.10 |
| `@minecraft/server-editor-bindings` | `8518d9c7-a1f5-4bf3-acc7-78e87df595fc` | — | 1.19.80 |
| `@minecraft/server-editor` | `1d565354-296d-11ed-a261-0242ac120002` | — | 1.19.80 |

<!-- md:sortable -->

## JavaScript运行环境

脚本API使用基于**QuickJS**引擎的JavaScript运行时，采用ECMAScript模块（ESM）系统组织和加载代码。

### 支持的全局对象

| 类别 | 内容 |
|------|------|
| 基本类型构造器 | `Number`、`Boolean`、`String`、`Symbol`、`BigInt` |
| 对象与函数 | `Object`、`Function`（需`script_eval`功能）、`Proxy`、`Reflect` |
| 集合 | `Map`、`Set`、`WeakMap`、`WeakSet` |
| 数组 | `Array`、`Int8Array`、`UInt8Array`、`Int16Array`、`UInt16Array`、`Int32Array`、`UInt32Array`、`Float32Array`、`Float64Array`、`SharedArrayBuffer`、`ArrayBuffer`、`UInt8ClampedArray`、`DataView` |
| 工具类 | `JSON`、`Math`、`Date`、`RegExp`、`Promise`、`Error`（及其所有子类） |
| 全局函数 | `parseInt`、`parseFloat`、`isNaN`、`isFinite`、`decodeURI`、`encodeURI`、`decodeURIComponent`、`encodeURIComponent`、`eval`（需`script_eval`功能） |
| 控制台 | `console`（`log`、`warn`、`error`、`info`） |
| 特殊 | `globalThis`、`NaN`、`Infinity`、`undefined`、`print`（`console.log`的别名）、`__date_clock`（QuickJS内置，返回微秒时间戳） |

### 不支持的全局对象

标准Web API中的`setTimeout`、`setInterval`、`clearTimeout`、`clearInterval`均**不可用**。时间调度请使用`system.runTimeout`和`system.runInterval`。

### 启用eval

`eval()`和`Function()`构造器默认禁用。如需使用，在`manifest.json`的`capabilities`中声明`"script_eval"`：

```json
{
    "capabilities": ["script_eval"]
}
```

### JavaScript引擎更新历史

自1.21（诡异试炼更新）起，引擎新增了以下全局支持：

- `BigInt` — 任意精度整数（如`123n`）。
- `Object.hasOwn(obj, prop)` — 检查对象是否拥有自有属性。
- `Array.prototype.findLast(callbackFn)` — 返回最后一个匹配的元素。
- `Array.prototype.at(index)` — 支持负索引访问数组元素。

## 脚本引擎<!-- md:flag deprecated -->

**脚本引擎（Script Engine）**是脚本API的前身，是一套已被弃用的早期脚本系统。旧版脚本引擎提供了`client`和`server`两个脚本上下文，使用了不同于当前脚本API的接口设计。旧版脚本引擎已在较新的游戏版本中移除，所有新开发应使用当前的脚本API。

## 早期GameTest写法<!-- md:flag deprecated -->

早期GameTest实验性可能出现`type`为`javascript`的清单文件模块、以UUID声明的`Minecraft`和`GameTest`模块依赖，以及`import * as GameTest from "GameTest"`、`import { BlockLocation } from "Minecraft"`等导入方式。这些写法属于1.16.210附近的历史API形态，不应作为当前脚本API教程使用。

当前脚本API使用`type`为`script`的清单文件模块，并通过`@minecraft/server`、`@minecraft/server-gametest`等模块名声明依赖和导入功能。维护旧包时若遇到早期GameTest写法，应按当前模块系统重新迁移。