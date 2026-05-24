# Endstone

**Endstone**是面向Minecraft基岩版专用服务器的第三方插件加载器与插件API。它通过接入BDS进程，在尽量保留原版服务端行为的前提下，为Python和C++插件提供事件、命令、权限、调度器、表单、记分板、物品栏、地图、NBT和网络数据包等高层接口。

Endstone不是BDS的原生组成部分，也不是Mojang提供的官方插件系统。它属于社区服务端生态，其功能边界、兼容性与更新节奏均由Endstone项目本身决定。

## 概述

Endstone的定位接近Java版服务端生态中的Bukkit、Spigot、Paper一类插件API：插件不直接操作BDS内部实现，而是通过稳定程度更高的抽象接口访问服务器对象。对于开发者而言，这种模型降低了直接处理原生函数、内存布局和版本差异的成本；对于服主而言，它能够在保留BDS世界、配置和原版行为的同时，引入更丰富的服务器扩展能力。

Endstone主要面向两类插件：

- **Python插件**：以Python包的形式分发，通过入口点声明插件主类，适合快速开发、测试和迭代。
- **C++插件**：以共享库形式加载，通过Endstone提供的C++接口和宏声明插件元数据，适合对性能、二进制集成或底层访问有更高要求的场景。

## 与BDS的关系

Endstone以BDS为运行基础。它的服务器启动程序会在服务器目录中引导或使用官方BDS，并在运行时通过挂钩和包装BDS内部对象实现插件能力。因此，Endstone服务器仍受BDS版本、平台支持、网络协议和官方服务端行为的限制。

这种关系带来两类结果：

- Endstone通常能够继续使用BDS世界目录、{{file|server.properties|txt}}、资源包和行为包等既有文件。
- Endstone的底层兼容性会随BDS更新而变化，新的BDS版本可能要求Endstone发布对应更新。

Endstone变更记录显示，Endstone持续按BDS版本更新兼容性，并在不同版本中加入了对1.20.72、1.21系列以及后续BDS版本的支持。具体可用版本应以当前Endstone发行页、PyPI包信息和文档为准。

## 版本节奏与兼容策略

根据当前版本的Endstone说明页与CHANGELOG，Endstone近期版本延续了“跟进BDS正式版并快速修复兼容问题”的策略。以0.11.x分支为例，其已连续声明对BDS1.26.0、1.26.1.1、1.26.3.1和1.26.12的支持，并在同一分支内持续修复数据包序列化、事件触发与网络稳定性问题。

这意味着实际部署时应把“Endstone版本”和“BDS版本”作为一组来验证，而不是单独升级其中之一。服主在升级前通常需要同步核对：

- Endstone发行说明中的目标BDS版本；
- 插件声明的`api_version`是否覆盖目标大版本；
- 是否存在破坏性变更（如类型替换、属性重命名、参数顺序调整）。

若仅参考旧教程而不核对版本，常见后果包括插件加载失败、事件不触发或命令行为与预期不一致。

## 架构

Endstone项目大致由以下部分组成：

| 组成部分 | 作用 |
|----------|------|
| Endstone API | 面向C++插件开发者的头文件接口层。 |
| Endstone Python Bindings | 将Endstone API暴露给Python插件使用的绑定层。 |
| Endstone Core | API的核心实现层，将插件侧调用转化为对BDS对象和系统的操作。 |
| Endstone Runtime | 对BDS可执行文件和运行时对象进行挂钩的部分，用于注入事件、命令和修正逻辑。 |
| Endstone DevTools | 用于从原版服务端导出数据的开发工具。项目结构文档将其描述为带图形界面的高级工具，目前仅在Windows上启用，并要求系统具备OpenGL功能。 |
| Python包 | 提供`endstone`命令行入口、Python插件加载器、绑定库和相关工具。 |

这种分层使插件开发者通常只需要面对API层，而不必直接依赖BDS内部结构。与此同时，Endstone自身仍需要维护与BDS二进制接口之间的适配。

## 功能

Endstone的功能随版本扩展。说明页、教程和变更记录共同显示，其公开能力主要包括：

- 插件生命周期：加载、启用、禁用和重载插件。
- 命令系统：声明自定义命令、命令用法、参数类型和权限要求。
- 权限系统：为命令和插件功能设置默认权限，并支持操作员、非操作员、控制台等权限默认值。
- 事件系统：监听玩家、活动对象、方块、天气、聊天、命令、网络和插件生命周期等事件，部分事件可取消。
- 调度器：按延迟或周期在服务器刻中执行任务。
- 玩家与世界接口：访问在线玩家、发送消息、传送、操作游戏模式、读取位置、访问维度和存档对象等。
- 物品栏与物品接口：读取和修改物品栏、物品元数据、魔咒、耐久、NBT等数据。
- 表单、Boss栏和文本格式：向玩家显示交互界面、Boss栏、提示、弹窗和带颜色格式的文本。
- 记分板与地图接口：创建或操作记分板对象，并对游戏内地图进行自定义渲染。
- 网络与数据包事件：在特定版本中观察或修改低层网络载荷。
- 度量与崩溃诊断：记录日志、生成崩溃报告，并可与bStats一类统计服务集成。

这些功能均是Endstone向插件公开的第三方接口，不应视为BDS原生插件能力。

## 插件模型

Python插件通常是一个普通Python项目。项目名按Endstone教程要求使用`endstone-`前缀和短横线小写形式；包名通常将短横线改为下划线。插件入口通过`pyproject.toml`中的`[project.entry-points."endstone"]`声明，入口值使用`模块:类`格式。插件主类继承`endstone.plugin.Plugin`，并通过`api_version`声明目标API主次版本。

C++插件通常通过CMake构建，并使用Endstone提供的`endstone_add_plugin`函数和`ENDSTONE_PLUGIN`宏。插件名要求使用小写字母、数字和下划线。编译产物以共享库形式放入服务器的插件目录。

Endstone插件目录通常位于服务器根目录下的{{file|plugins}}。Python插件可以以轮子包形式放入该目录，也可以在开发模式中通过可编辑安装直接从项目目录加载。C++插件则通常将生成的动态库复制到该目录。

## 命令与权限

Endstone允许插件在元数据中声明命令。Python插件可以通过插件类的`commands`和`permissions`类属性声明命令及权限；C++插件可以在`ENDSTONE_PLUGIN`块中链式声明命令和权限。Endstone教程指出，命令默认需要操作员权限，若需要向所有玩家开放，应显式声明对应权限的默认值。

命令用法支持必选参数、可选参数、内置参数类型和自定义枚举参数。相关语法和类型见[Endstone命令与文本格式](../../refs/server/endstone-command-format.md)。

## 局限性

Endstone并不等同于完全可控的自实现服务端。它依赖BDS的封闭二进制程序，因此以下限制始终存在：

- BDS更新可能破坏底层挂钩或二进制接口，Endstone需要随版本适配。
- 未公开或尚未封装的BDS能力不能直接通过稳定API使用。
- 插件能力受Endstone当前API范围限制，而不是受BDS内部所有能力限制。
- 低层网络、NBT、方块实体、世界生成等接口可能具有更高的兼容风险。

路线图还列出了若干尚待完善的方向，例如插件配置、持久化数据容器、状态效果管理、实体特性访问、配方、方块实体、富文本、区块控制、结构、相机和世界生成等。这些内容代表项目规划或讨论，不应写作已经稳定可用的能力。

## 教程

- [Endstone入门](../../guides/servers/endstone/index.md)
- [Python插件工作流](../../guides/servers/endstone/python-plugin-workflow.md)
- [命令、事件与调度实战](../../guides/servers/endstone/command-event-task.md)
- [颜色代码](../../guides/servers/endstone/color-codes.md)

## 参考

- [Endstone API总览](../../refs/server/endstone-api.md)
- [Endstone命令与文本格式](../../refs/server/endstone-command-format.md)

## 参考阅读

- [Endstone文档首页](../../translations/endstone/index.md)
- [Endstone参考目录](../../translations/endstone/reference/index.md)
- [注册命令（Endstone翻译）](../../translations/endstone/tutorials/register-commands.md)
- [使用颜色代码（Endstone翻译）](../../translations/endstone/tutorials/use-color-codes.md)