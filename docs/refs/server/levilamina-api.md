# LeviLamina API模块

本页概述LeviLamina官方API参考中列出的主要模块。下列接口仅适用于LeviLamina模组开发，不属于BDS原生API。

LeviLamina的官方API按`ll/api`组织，覆盖基础设施、核心系统、输入输出、异步与线程、数据与工具、底层能力和仅客户端模块。各模块的细分参考页已拆分为独立页面，便于按需查阅。

## 模块总览

| 类别 | 模块 | 说明 | 参考页 | 适用范围 |
|------|------|------|--------|----------|
| 基础设施 | Base | 导出宏、基础类型、C++20概念、类型萃取、定长字符串和元编程工具。 | [Base](levilamina-api/base.md) | 通用 |
| 基础设施 | Expected | `Expected<T>`、多态错误容器和错误传播辅助函数。 | [Expected](levilamina-api/expected.md) | 通用 |
| 基础设施 | Config | 基于JSON和反射的配置加载、保存与版本迁移。 | [Config](levilamina-api/config.md) | 通用 |
| 基础设施 | Reflection | 聚合类型的编译期反射，以及JSON序列化和反序列化辅助能力。 | [Reflection](levilamina-api/reflection.md) | 通用 |
| 核心系统 | Mod | 模组生命周期、清单、目录结构、日志器、配置目录和数据目录。 | [Mod](levilamina-api/mod.md) | 通用 |
| 核心系统 | Event | 事件总线、监听器、优先级、可取消事件，以及玩家、世界、实体、服务端和客户端事件。 | [Event](levilamina-api/event.md) | 通用、服务端、客户端 |
| 核心系统 | Command | 自定义命令注册、重载、类型化参数、枚举、软枚举、运行时枚举、别名和权限等级。 | [Command](levilamina-api/command.md) | 通用 |
| 核心系统 | Service | 服务注册与发现，以及对`Minecraft`、`Level`、`ServerInstance`和`CommandRegistry`等Bedrock对象的访问器。 | [Service](levilamina-api/service.md) | 通用、服务端、客户端 |
| 核心系统 | Form | SimpleForm、ModalForm和CustomForm三类交互式表单。 | [Form](levilamina-api/form.md) | 通用 |
| 输入输出 | IO&Logger | 线程安全日志器、日志级别、输出目标、格式化器、文件工具和流重定向。 | [IO & Logger](levilamina-api/io.md) | 通用 |
| 输入输出 | I18n | 键值翻译文件加载、运行时翻译更新和用户自定义字面量。 | [I18n](levilamina-api/i18n.md) | 通用 |
| 异步与线程 | Coroutine | C++20协程任务、生成器、执行器、休眠和让出执行的等待器。 | [Coroutine](levilamina-api/coro.md) | 通用 |
| 异步与线程 | Thread | 线程池执行器、服务器线程执行器和并发同步工具。 | [Thread](levilamina-api/thread.md) | 通用 |
| 异步与线程 | Chrono | 游戏刻时长、游戏时间时钟、服务器时钟和时间字面量。 | [Chrono](levilamina-api/chrono.md) | 通用 |
| 数据与工具 | Data | LevelDB键值存储、依赖图、语义版本类型、可取消回调和线程安全容器。 | [Data](levilamina-api/data.md) | 通用 |
| 数据与工具 | Utils | 系统信息、字符串、文件、哈希、随机数、Base64和错误处理工具函数。 | [Utils](levilamina-api/utils.md) | 通用 |
| 底层 | Memory&Hook | 内存操作、函数钩子、签名扫描、符号解析和钩子优先级。 | [Memory & Hook](levilamina-api/memory.md) | 通用 |
| 底层 | Network | 客户端与服务端之间的自定义网络数据包注册、处理和发送。 | [Network](levilamina-api/network.md) | 通用 |
| 客户端 | Input | 键盘、鼠标输入绑定和输入事件。 | [Input](levilamina-api/input.md) | 仅客户端 |

其中，`Mod`、`Command`、`Event`、`Form`、`I18n`和`Coroutine`通常是服务端模组最常接触的入口；`Service`、`Memory&Hook`和`Network`则更靠近底层能力与版本适配。

## 头文件速查

下表列出各模块在文档中最常见的入口头文件，便于快速定位源码与参考页。

| 模块 | 常用头文件 |
|------|------------|
| Base | `ll/api/base/Macro.h`、`ll/api/base/Concepts.h`、`ll/api/base/TypeTraits.h`、`ll/api/base/StdInt.h` |
| Expected | `ll/api/Expected.h` |
| Config | `ll/api/Config.h` |
| Reflection | `ll/api/reflection/Reflection.h`、`ll/api/reflection/Serialization.h`、`ll/api/reflection/Deserialization.h` |
| Mod | `ll/api/mod/Mod.h`、`ll/api/mod/Manifest.h`、`ll/api/mod/ModManager.h`、`ll/api/mod/ModManagerRegistry.h` |
| Event | `ll/api/event/EventBus.h`、`ll/api/event/Event.h`、`ll/api/event/EventId.h`、`ll/api/event/Listener.h` |
| Command | `ll/api/command/CommandRegistrar.h`、`ll/api/command/CommandHandle.h`、`ll/api/command/Command.h`、`ll/api/command/Overload.h` |
| Service | `ll/api/service/Service.h`、`ll/api/service/ServiceManager.h`、`ll/api/service/Bedrock.h` |
| Form | `ll/api/form/SimpleForm.h`、`ll/api/form/ModalForm.h`、`ll/api/form/CustomForm.h`、`ll/api/form/FormBase.h` |
| IO & Logger | `ll/api/io/Logger.h`、`ll/api/io/LogLevel.h`、`ll/api/io/LoggerRegistry.h`、`ll/api/io/Sink.h` |
| I18n | `ll/api/i18n/I18n.h` |
| Coroutine | `ll/api/coro/CoroTask.h`、`ll/api/coro/CoroPromise.h`、`ll/api/coro/CoroTaskAwaiter.h`、`ll/api/coro/Generator.h` |
| Thread | `ll/api/thread/ThreadPoolExecutor.h`、`ll/api/thread/ServerThreadExecutor.h`、`ll/api/thread/GlobalThreadPauser.h`、`ll/api/thread/ThreadName.h` |
| Chrono | `ll/api/chrono/GameChrono.h` |
| Data | `ll/api/data/KeyValueDB.h`、`ll/api/data/DependencyGraph.h`、`ll/api/data/Version.h`、`ll/api/data/AnyFunction.h` |
| Utils | `ll/api/utils/SystemUtils.h`、`ll/api/utils/StringUtils.h`、`ll/api/utils/HashUtils.h`、`ll/api/utils/RandomUtils.h`、`ll/api/utils/FileUtils.h` |
| Memory & Hook | `ll/api/memory/Hook.h`、`ll/api/memory/Memory.h`、`ll/api/memory/Signature.h`、`ll/api/memory/Symbol.h` |
| Network | `ll/api/network/packet/PacketBase.h`、`ll/api/network/packet/PacketHandlerBase.h` |
| Input | `ll/api/KeyRegistry.h`、`ll/api/KeyHandle.h`、`ll/api/event/input/KeyInputEvent.h`、`ll/api/event/input/MouseInputEvent.h` |

## 适用范围

| 范围 | 含义 | 典型头文件根目录 |
|------|------|------------------|
| 通用 | 在LeviLamina服务端构建和客户端构建中均可能使用，但具体实现仍可能因目标环境不同而不同。 | `src/ll/api/` |
| 服务端 | 只在服务端构建中提供，通常依赖BDS服务端对象或服务端生命周期。 | `src-server/ll/api/` |
| 客户端 | 只在客户端构建中提供，通常依赖Windows版Minecraft客户端对象、输入或渲染生命周期。 | `src-client/ll/api/` |

## 文档约定

LeviLamina官方API参考中的示例和说明通常遵循以下约定：

- 示例默认面向C++20构建环境。
- 示例通常省略与主题无关的样板代码，但默认要求补齐必要的`#include`指令。
- 名称在首次出现时通常使用完整命名空间，以减少与Bedrock原生类型或第三方库的歧义。
- 需要导出给其他模组或加载器使用的符号，通常配合`LLAPI`、`LLNDAPI`等导出宏。
- 标记为客户端或服务端专用的能力，通常不应跨构建目标直接复用。

## 兼容性提示

- Command、Event、Form、Config和Mod等高层模块通常是普通模组开发最常接触的接口。
- Service、Memory&Hook和`mc`头文件相关能力更接近基岩版内部访问，版本耦合更强。
- Coroutine和Thread可用于异步任务，但对游戏对象的访问仍应遵守服务器线程和生命周期要求。
- Input只适用于LeviLamina客户端构建，不适用于BDS服务端。

## 客户端能力

LeviLamina的客户端构建将客户端专用能力集中在少数模块中：

- `Input`：键盘和鼠标输入绑定，仅客户端可用。
- `Event`：客户端生命周期事件、输入事件、渲染事件和界面渲染事件，仅在客户端构建中触发。
- `Service`：部分Bedrock访问器在客户端构建中也可用，但可用对象取决于客户端进程中的实际状态。

若需要把这些模块放回更大的模组语境中理解，可先阅读[LeviLamina客户端模组](../../docs/client/levilamina-client.md)。

## 参考脉络

当前API参考页以模块总览为主，适合快速定位能力边界。若需要从文档脉络理解相关模块，可参考[LeviLamina文档归档](../../translations/levilamina/index.md)；若需要直接对照开发流程，则可查看[LeviLamina入门](../../guides/servers/levilamina.md)。