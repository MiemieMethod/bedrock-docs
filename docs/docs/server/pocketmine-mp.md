# PocketMine-MP

**PocketMine-MP**是面向Minecraft基岩版的第三方**自实现服务端（Self-implemented Server）**软件。它使用PHP运行，拥有独立的世界实现、配置系统和插件生态，而不是在**基岩版专用服务器（Bedrock Dedicated Server）**进程内加载插件。

PocketMine-MP不是Mojang提供的官方服务端，也不是BDS的原生插件系统。其配置文件、插件清单、资源包管理方式和玩法实现边界都属于PocketMine-MP自身，不应直接等同于BDS或其他社区服务端。

## 定位

PocketMine-MP是基岩版社区中延续时间较长的一条PHP服务端路线。对服主而言，它提供独立运行的服务器程序、配置文件和插件目录；对开发者而言，它提供围绕PHP插件构建的一整套入口，包括插件清单、事件系统、命令系统和权限声明。

与基于BDS的插件加载器相比，PocketMine-MP不依赖官方服务端的二进制接口，因此可以跨平台运行，并保持自身的插件模型和发布节奏。与此同时，原版服务端中的世界生成、实体行为、红石、网络协议适配和其他玩法细节也需要由PocketMine-MP自行实现，其原版趋同程度取决于PocketMine-MP当前版本。

## 运行条件

PocketMine-MP的基础运行条件包括：

- 64位CPU。
- 64位操作系统。
- 至少1GB内存。
- 能运行带所需扩展的64位PHP环境。

Windows、Linux和macOS都在主要支持平台之列。硬件选择上，双核或更高规格处理器更适合长期运行，但PocketMine-MP更依赖较高的单核性能，而不是大量核心数。

## 配置文件

PocketMine-MP的主要行为由多种文本配置文件控制：

| 文件 | 作用 |
|------|------|
| `server.properties` | 基础服务器设置，例如名称、端口和视距。 |
| `pocketmine.yml` | 更进阶的运行设置，例如内存、线程和多世界相关选项。 |
| `resource_packs/resource_packs.yml` | 资源包加载相关配置。 |
| `ops.txt` | 操作员列表。 |
| `banned-players.txt` | 被封禁的玩家名称列表。 |
| `banned-ips.txt` | 被封禁的IP列表。 |

其中，`server.properties`适合日常服主管理；`pocketmine.yml`涉及更底层的运行行为，修改前通常需要先理解对应选项的影响。操作员、封禁与解封也可以通过命令完成，而不必直接编辑文本文件。

## 插件模型

PocketMine-MP插件通常放置在服务器的`plugins`目录中。公开分发时，常见形态是`.phar`插件包；开发阶段也可以直接以源代码目录形式组织插件。

插件以`plugin.yml`作为清单文件。该文件用于声明插件名称、版本、入口类和兼容的API版本。必选字段包括：

- `name`
- `version`
- `main`
- `api`

`api`字段决定插件能否在目标服务端版本上加载。PocketMine-MP使用与服务端版本一致的语义化API版本号；插件通常只应声明真正需要的最低兼容版本，而不是机械地把每一个补丁版本都写入清单。

除必选字段外，`plugin.yml`还可以声明加载顺序与运行边界，例如：

- `load`：决定在世界加载前还是加载后启用插件。
- `depend`、`softdepend`、`loadbefore`：决定依赖与加载先后关系。
- `extensions`：声明所需PHP扩展。
- `mcpe-protocol`：限制兼容的网络协议版本。
- `os`：限制运行平台。
- `commands`、`permissions`：声明命令与权限。
- `src-namespace-prefix`：调整源码目录与PHP命名空间的映射关系。

这些字段共同决定PocketMine-MP插件的加载、拒载、依赖检查与命令注册行为。

## 资源包与权限

PocketMine-MP支持通过`resource_packs/resource_packs.yml`管理资源包。资源包目录与配置方式属于PocketMine-MP服务器运行时的一部分，不应直接套用到BDS、Nukkit-MOT或其他服务端。

权限管理方面，PocketMine-MP同时使用操作员列表、封禁列表和插件自身声明的权限节点。很多插件会在`plugin.yml`中附带权限定义，再由服主结合操作员、权限插件或插件配置决定哪些玩家能够使用某项功能。

## 局限性

PocketMine-MP作为自实现服务端，具有以下常见限制：

- 原版生存相关机制并不完整，部署前尤其应核验生物、红石、矿车和维度等内容。
- 插件兼容性受PocketMine-MP大版本、API版本和网络协议版本共同影响。
- 插件生态以PHP为核心，不适用于BDS、LeviLamina、Endstone、Allay、SerenityJS或Nukkit插件。
- 更改`pocketmine.yml`等进阶设置时，错误配置可能直接影响稳定性或世界加载行为。

## 进一步阅读

- [Nukkit与PocketMine服务端](../../guides/servers/nukkit-pocketmine.md)
- [插件加载器](plugin-loader.md)
- [基岩版服务端软件生态](../../refs/server/server-software-ecosystem.md)
