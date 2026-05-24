# Nukkit-MOT

**Nukkit-MOT**是面向Minecraft基岩版的第三方**自实现服务端（Self-implemented Server）**软件。它属于Nukkit系列分支，基于NukkitPetteriM1Edition的最后一个开源版本继续开发，而不是在BDS进程内加载插件。

Nukkit-MOT不是Mojang提供的官方服务端，也不是BDS的原生组成部分。其服务端行为、插件接口、配置项、世界生成器和客户端兼容能力均属于Nukkit-MOT项目本身，不能视为BDS或原版客户端直接具备的能力。

## 定位

Nukkit-MOT的定位接近Java生态中的社区服务端。它尝试以Java实现基岩版服务端逻辑，并延续Nukkit生态的插件模型。服务器管理员通常以独立JAR文件启动Nukkit-MOT；开发者则通过Nukkit-MOT公开或继承自Nukkit的API编写Java插件。

与基于BDS的插件加载器相比，Nukkit-MOT不依赖BDS的二进制接口，因此更容易跨平台运行，并可在服务端内部实现上自行扩展。然而，这也意味着原版服务端行为、网络协议、世界机制、实体AI、方块实体和容器行为需要由项目自行实现，其趋同程度取决于当前Nukkit-MOT版本。Nukkit-MOT简介页还把Java17或更高版本列为基础运行条件。

## 与Nukkit系列的关系

Nukkit是较早出现的基岩版Java实现服务端之一，后来衍生出多个分支。Nukkit-MOT是其中仍在维护的分支之一。其文档将其描述为基于NukkitPetteriM1Edition最后开源版本开发的特殊版本，并提示需要更高版本功能时可评估PowerNukkitX。

Nukkit-MOT、PowerNukkitX、Allay和PocketMine-MP都属于自实现服务端生态，但它们的代码基础、插件API、配置文件和世界实现并不相同。Nukkit插件通常不能不经检查地直接用于其他服务端；即使同属Nukkit系列，也应确认目标分支、游戏版本、依赖和API差异。

## 客户端兼容

Nukkit-MOT文档列出的目标之一是支持多个基岩版协议版本，并允许通过配置设置最低协议。具体可连接的客户端版本应以当前构建、协议库和配置文件为准。

Nukkit-MOT还提供中国版客户端连接相关配置。`server.properties`中的`netease-client-support=true`用于启用网易我的世界客户端连接支持<!-- md:flag china -->。该能力属于Nukkit-MOT的兼容扩展，不表示BDS或其他第三方服务端自动支持中国版客户端。

## 功能范围

Nukkit-MOT文档列出的服务端能力包括：

- 较多带AI实体。
- 下界和末地。
- 地牢和洞穴生成。
- 原版命令。
- Nukkit插件加载与管理。
- 面向插件的方块、物品栏、世界和维度相关接口。

这些能力应按Nukkit-MOT项目的实现理解。对于需要高度还原BDS行为的服务器，仍应测试红石、实体AI、村民、方块实体、世界生成、命令和多人交互等关键机制。

## 插件模型

Nukkit-MOT继承Nukkit生态的Java插件模型。插件通常以JAR文件放置在服务器的`plugins`目录中，由服务端在启动时加载。插件可以调用`cn.nukkit`包下的API来访问玩家、世界、方块、物品栏、命令、事件和调度器等对象。

开发插件时，需要关注目标Nukkit-MOT构建、Nukkit API兼容性和插件依赖。Nukkit-MOT文档还给出了Maven与Gradle依赖入口，常用依赖坐标为`cn.nukkit:Nukkit:MOT-SNAPSHOT`，仓库地址为`https://repo.lanink.cn/repository/maven-public/`。具体版本和可用性应以项目当前仓库为准。

Nukkit-MOT文档还将内容分成“用户文档”和“开发者文档”两条路径：前者面向服主管理、安装和配置，后者面向插件与工具开发。查阅资料时，应先确认当前问题属于服主运维还是插件编写，以免误用面向另一类读者的说明。

## 限制

Nukkit-MOT的主要限制来自自实现服务端路线和Nukkit旧生态兼容：

- 原版机制需要由项目自行实现，不能默认等同于BDS。
- 基岩版协议更新可能要求服务端同步更新协议、方块、物品和运行时数据。
- Nukkit旧插件可能依赖旧API、旧方块ID或旧数据值，需要逐项验证。
- 支持中国版客户端的能力属于Nukkit-MOT特性，不应迁移为其他服务端的通用结论<!-- md:flag china -->。
- 自定义方块等高级插件功能可能需要额外的Bin数据文件和特定插件实现配合。

运行与开发Nukkit-MOT前，建议先阅读[Nukkit、PocketMine与旧生态](../../guides/servers/nukkit-pocketmine.md)和[Nukkit-MOT API概览](../../refs/server/nukkit-mot-api.md)。