# LeviLamina入门

LeviLamina是围绕BDS运行的第三方模组加载器。它不是BDS原生插件系统；你可以把它理解成一个把C++模组接入BDS或受支持客户端的运行时。概念说明见[LeviLamina](../../docs/server/levilamina.md)，API模块概览见[LeviLamina API模块](../../refs/server/levilamina-api.md)。

如果想沿着官方文档的原始脉络阅读，可先打开[LeviLamina文档归档](../../translations/levilamina/index.md)。

本页负责“怎么做”的入门路径；如果需要术语、定位和局限性说明，应回到[LeviLamina](../../docs/server/levilamina.md)。如果需要继续按官方开发者目录阅读，则转到[LeviLamina开发者指南](levilamina/index.md)；如果需要逐页核对官方资料原文，再进入翻译归档。

## 推荐起步链路

本页只保留站内最短实践链路；安装原文、镜像参数、手动安装文件清单与界面名称以翻译归档中的对应页面为准。若目标只是“先跑起来”，建议按以下顺序阅读：

1. 先看[支持的版本](../../translations/levilamina/versions.md)，确认客户端、BDS和LeviLamina三者匹配。
2. 按目标环境进入[在服务器上安装](../../translations/levilamina/install-server.md)或[在客户端上安装](../../translations/levilamina/install-client.md)。Docker只是服务端安装的分支，建议先跑通普通目录安装。
3. 只有在需要追溯官方入口职责时，再对照[官方文档首页](../../translations/levilamina/official-docs-home.md)与[仓库README](../../translations/levilamina/repository-readme.md)。
4. 环境确认可以启动后，再进入[LeviLamina开发者指南](levilamina/index.md)和各专题页面。

/// html | div.grid.cards
- :material-download: __[安装与版本](../../translations/levilamina/install-server.md)__
  先确认支持版本，再处理lip、PreLoader和BDS。
- :material-scale-balance: __[法律与更新](../../translations/levilamina/legal-release-notes.md)__
  区分LGPL-3.0、LeviMC闭源软件EULA与更新日志中的兼容和安全修复。
- :material-language-cpp: __[项目构建指南](levilamina/build-guide.md)__
  优先阅读站内实践版，再按需回看官方构建说明。
- :material-book-open-variant: __[官方脉络](../../translations/levilamina/index.md)__
  查看LeviLamina官方资料在本站的落位结果。
- :material-alert-outline: __[问题排除](../../translations/levilamina/troubleshooting.md)__
  快速定位126、127和1114等常见错误码。
///

## 先确认版本

LeviLamina的每个版本只对应特定BDS或客户端版本。安装前先查看[支持的版本](../../translations/levilamina/versions.md)，再下载匹配版本的服务端或客户端。如果客户端提示服务器过旧、服务器提示客户端过旧，或LeviLamina无法启动，首先检查这三个版本是否互相匹配：

- Minecraft基岩版客户端版本。
- BDS版本。
- LeviLamina版本。

## 先看协议与更新

在安装、转发包链接、整理说明或发布整合包之前，建议先阅读[法律与发布说明](../../translations/levilamina/legal-release-notes.md)。该页已经集中梳理许可证、EULA、使用指南与更新日志的分工；就入门部署而言，至少应先确认以下四点：

- LeviLamina仓库的非闭源部分按LGPL-3.0发行。
- PreLoader、PeEditor等LeviMC闭源软件适用单独的EULA。
- 名称、品牌和资产使用还要遵守使用指南。
- 更新日志中可能包含兼容性修复、崩溃修复和安全修复，升级前不应跳过。

## 安装服务端

本节只保留服务端最短命令链。前提条件、镜像设置、手动安装目录结构和升级说明以[在服务器上安装](../../translations/levilamina/install-server.md)为准。LeviLamina官方文档推荐通过lip安装；Windows环境需要Windows10、Windows11、Windows Server2019或Windows Server2022，并需要安装Visual C++ Redistributable for Visual Studio2015、2017、2019和2022。

安装lip后，新建服务器目录：

```powershell
mkdir myserver
cd myserver
```

安装LeviLamina：

```powershell
lip install github.com/LiteLDev/LeviLamina
```

如果需要安装指定版本，可以在包名后追加版本号：

```powershell
lip install github.com/LiteLDev/LeviLamina@x.y.z
```

启动服务器：

```powershell
.\bedrock_server_mod.exe
```

安装模组时，也使用对应包提供的lip命令。例如官方安装文档用LeviAntiCheat举例：

```powershell
lip install github.com/LiteLDev/LeviAntiCheat
```

/// warning | 升级前先备份
LeviLamina安装文档建议不要在同一目录内直接更新以保证数据安全。更稳妥的做法是在独立文件夹中安装新版本，再复制`worlds`目录并按需迁移配置。
///

## 手动安装时会看到什么

lip会替你处理大多数文件。手动安装时，官方文档列出的关键部件包括LeviLamina本体、PreLoader、PeEditor、bedrock-runtime-data、CrashLogger、对应版本的BDS和可选的本地化文件。处理完成后，服务端目录中通常会出现{{file|bedrock_server_mod.exe}}和{{file|plugins}}目录。

不要把这些文件理解成原版BDS的一部分。它们属于LeviLamina运行时；如果后续排查问题，应该同时检查BDS版本、LeviLamina版本、PreLoader和各个模组包。

## 使用Docker

Docker链路建立在已经理解服务端目录、端口和备份方式的前提上。LeviLamina官方资料提供了Linux容器和Windows容器镜像。最小示例类似于：详细参数见[在Docker上安装](../../translations/levilamina/install-docker.md)：

```shell
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:/data ghcr.io/liteldev/levilamina-server:latest-wine
```

常见环境变量包括：

| 变量 | 作用 |
|------|------|
| `EULA` | 必须设置为`TRUE`以接受Minecraft最终用户许可协议。 |
| `VERSION` | 指定LeviLamina版本；也可以使用`LATEST`。 |
| `PACKAGES` | 首次运行时安装的一组lip包。 |
| `GITHUB_MIRROR_URL` | 设置GitHub镜像地址。 |
| `GO_MODULE_PROXY_URL` | 设置Go模块代理地址。 |

如果你已经熟悉BDS的目录、端口和世界备份，再使用Docker会更稳妥。否则建议先在普通Windows目录中跑通一次。

/// warning | Docker中的`EULA`变量不等于LeviMC的EULA
Docker安装页中的`EULA=TRUE`只表示接受Minecraft最终用户许可协议，用于满足容器启动前提。若安装流程同时涉及PreLoader、PeEditor等LeviMC闭源软件，仍应另行阅读[最终用户许可协议](../../translations/levilamina/eula.md)。
///

## 安装客户端

本节只保留客户端最短链路。LeviLauncher中的原始界面步骤、升级命令和客户端依赖版本说明以[在客户端上安装](../../translations/levilamina/install-client.md)为准。客户端侧需要Windows10或Windows11、Visual C++运行库、LeviLauncher和lip。官方推荐在LeviLauncher中安装受支持的客户端版本，再通过启动器中名为“插件”的管理界面安装LeviLamina；也可以在客户端目录中使用类似命令安装指定版本：

```shell
lip install github.com/LiteLDev/LeviLamina#client@26.10.11
```

/// warning | 客户端模组不是服务器插件
客户端侧LeviLamina用于受支持的Windows版Minecraft客户端环境。不要把客户端输入、渲染或界面相关API写入服务端模组，也不要假定普通基岩版客户端可以加载这些模组。如果目标是客户端模组开发，构建时应优先查看`client`目标与`src-client/`中的专用代码。

客户端构建与客户端模组的概念、目录和接口范围，可继续查看[LeviLamina客户端模组](../../docs/client/levilamina-client.md)与[项目构建指南](levilamina/build-guide.md)。
///

## 创建第一个模组

LeviLamina开发教程以一个“自杀指令”模组为例：玩家可以输入`/suicide`自杀，首次进服获得一个钟，使用钟时弹出确认窗口。这个教程覆盖日志、事件订阅、指令注册、配置文件、数据库、表单、Minecraft对象构造和原版函数调用。更完整的官方脉络可从[LeviLamina文档归档](../../translations/levilamina/index.md)继续追溯。

开发前需要准备：

- C++基础。
- xmake。
- Visual Studio Code。
- Git。
- Visual Studio2022，并安装C++桌面应用开发工作负载。

创建项目时，使用`levilamina-mod-template`模板仓库。然后修改`xmake.lua`中的目标名、`tooth.json`中的包信息、依赖版本和放置路径，再修改命名空间与源文件名。

## 构建空模组

在模组仓库中先更新xmake仓库：

```powershell
xmake repo -u
```

配置调试构建：

```powershell
xmake f -m debug
```

开始构建：

```powershell
xmake
```

如果需要Visual Studio Code中的clangd正确识别项目，可以生成`compile_commands.json`：

```powershell
xmake project -k compile_commands
```

更完整的官方来源说明可见[官方构建指南](../../translations/levilamina/build-guide.md)；如果希望按站内术语和实践顺序阅读，则优先查看[项目构建指南](levilamina/build-guide.md)。

构建失败时，先检查Visual Studio2022、Microsoft C++构建工具、Windows SDK和xmake是否为较新版本。官方教程也建议在下载依赖失败时配置GitHub镜像或HTTP代理。

## 注意加载时机

LeviLamina教程提醒，模组构造函数只应做与游戏无关的初始化，例如日志、配置和数据库。事件订阅、指令注册等与游戏相关的操作，应放在模组启用阶段；指令注册尤其需要等到指令注册表可用后再进行。

常见模式如下：

- 在构造阶段准备日志器、默认配置和数据目录。
- 在启用阶段注册命令、订阅事件和获取服务。
- 在禁用阶段退订事件、解除命令或保存必要状态。

## 发布模组

LeviLamina官方发布教程要求模组包包含`tooth.json`。这个文件描述包名、版本、展示信息、依赖、资源文件和安装位置。通常需要把模组产物放入压缩包，并将放置位置指向{{file|plugins/模组名}}。如需完整的发布脉络，可继续参考官方教程归档中的发布页。

发布前可以先用lip在本地打包和安装，确认依赖版本、放置路径和启动结果都正确，再发布到GitHub发行页并提交到Bedrinth等模组包索引。

## 常见错误码

| 错误码 | 常见含义 | 处理方向 |
|--------|----------|----------|
| `126` | 缺少LeviLamina或模组依赖。 | 查看依赖诊断，确认LeviLamina和模组安装完整。 |
| `127` | LeviLamina或模组依赖版本不正确。 | 检查依赖诊断，统一相关包版本。 |
| `1114` | Visual C++运行库版本过旧。 | 更新Visual C++ Redistributable。 |

如果错误码之外仍然无法判断，优先收集启动日志、崩溃记录、BDS版本、LeviLamina版本、模组列表和最近修改过的配置。

## 进一步阅读

- [官方文档首页](../../translations/levilamina/official-docs-home.md)
- [LeviLamina开发者指南](levilamina/index.md)
- [项目构建指南](levilamina/build-guide.md)
- [法律与发布说明](../../translations/levilamina/legal-release-notes.md)
- [找函数指南](levilamina/find-function-guide.md)
- [接口导出指南](levilamina/interface-export-guide.md)
- [物品相关指南](levilamina/item-guide.md)
- [创建你的第一个模组](levilamina/create-your-first-mod.md)
- [发布你的第一个模组](levilamina/publish-your-first-mod.md)
- [发布你的第一个整合包](levilamina/publish-your-first-pack.md)
- [LeviLamina文档归档](../../translations/levilamina/index.md)
- [常见问题](../../translations/levilamina/faq.md)
- [问题排除](../../translations/levilamina/troubleshooting.md)
- [LeviLamina API模块](../../refs/server/levilamina-api.md)
