# Nukkit与PocketMine服务端

这一页用于整理两条常见的自实现服务端路线：Nukkit-MOT和PocketMine-MP。两者都不是BDS，也不是Mojang提供的官方服务器软件；它们的配置项、插件文件和兼容边界都应放在各自生态中理解。

想先了解概念定位，可以阅读[Nukkit-MOT](../../docs/server/nukkit-mot.md)与[PocketMine-MP](../../docs/server/pocketmine-mp.md)。本页只讲怎样先把服务器跑起来，再完成最基本的配置与插件安装。

## 准备环境

Nukkit-MOT要求Java17或更高版本。测试环境至少应准备1GB内存、500MB可用存储空间；如果要让多人进入服务器，建议准备2GB或更多内存。

安装Java后，在终端或命令提示符中运行：

```bash
java -version
```

看到`openjdk version "17.0.x"`或更高版本输出后，就可以继续。若系统提示找不到`java`命令，通常需要重新安装Java、配置环境变量，或重新打开终端。

## 下载与启动

从Nukkit-MOT项目提供的Jenkins或GitHub Actions构建下载`Nukkit-MOT-SNAPSHOT.jar`。新建一个服务器文件夹，例如`NukkitServer`，把这个JAR文件放进去。

Windows可以创建`start.bat`：

```bat title="start.bat"
@echo off
java -Xms1G -Xmx1G -jar Nukkit-MOT-SNAPSHOT.jar
pause
```

Linux或macOS可以创建`start.sh`：

```bash title="start.sh"
#!/bin/bash
java -Xms1G -Xmx1G -jar Nukkit-MOT-SNAPSHOT.jar
```

然后赋予执行权限：

```bash
chmod +x start.sh
```

`-Xms1G`表示初始内存为1GB，`-Xmx1G`表示最大内存为1GB。服务器人数更多时，可以把最大内存调高，例如`-Xmx2G`。

首次启动会生成`server.properties`等配置文件、创建默认世界并加载资源。看到类似`Done (xx.xxs)! For help, type "help"`的提示时，说明服务器已启动。随后可以先在控制台输入：

```text
stop
```

等待服务器完整关闭，再修改配置文件。

/// tip | 自定义方块插件所需数据
如果计划使用带自定义方块功能的插件，Nukkit-MOT文档要求额外下载Bin数据文件，并把`bin`文件夹放到服务器根目录。若不使用这类插件，可以跳过这一步。
///

## 配置服务器

主要配置文件是`server.properties`。下面是常见配置项：

```properties title="server.properties"
server-port=19132
server-ip=0.0.0.0
gamemode=0
difficulty=1
max-players=20
white-list=false
motd=A Nukkit Server
```

修改配置后需要重启服务器才会生效。常见调整包括：

- 玩家较多时降低`view-distance`以减少区块负载。
- 需要限制进入者时启用`white-list=true`。
- 需要正版账号验证时启用`xbox-auth=true`。
- 需要允许网易我的世界客户端连接时启用`netease-client-support=true`<!-- md:flag china -->。

`netease-client-support`是Nukkit-MOT对中国版客户端连接的兼容配置，不是BDS原生能力，也不代表其他社区服务端支持相同开关<!-- md:flag china -->。

除`server.properties`外，Nukkit-MOT首次启动后还会生成以下管理文件：

| 文件名 | 用途 |
|--------|------|
| `ops.txt` | 管理员（OP）玩家列表 |
| `white-list.txt` | 白名单玩家列表 |
| `banned-players.txt` | 封禁玩家列表 |
| `banned-ips.txt` | 封禁IP列表 |

## 连接服务器

如果客户端和服务端在同一台电脑上，可以在Minecraft基岩版的服务器列表中添加地址`127.0.0.1`，端口使用`19132`或你在配置中设置的端口。

Windows版Minecraft在本机连接时可能受到回环限制影响。可以以管理员身份运行PowerShell，并执行：

```powershell
CheckNetIsolation LoopbackExempt -a -n="Microsoft.MinecraftUWP_8wekyb3d8bbwe"
```

如果是局域网连接，需要在服务器设备上查询局域网IP地址，然后让客户端连接该地址。Windows可用`ipconfig`查看IPv4地址，Linux或macOS可用`ifconfig`或`ip addr`查看。

如果是公网服务器，需要确认云服务器安全组、防火墙和路由器端口转发允许UDP端口19132入站。Linux上常见开放命令包括：

```bash
sudo ufw allow 19132/udp
```

## 安装插件

Nukkit插件通常是`.jar`文件。可以从以下渠道获取插件：

- [Cloudburst（Nukkit官方论坛）](https://cloudburstmc.org/resources/categories/nukkit-plugins.1/) — 官方插件库，主要面向国际版用户。
- [Nukkit-MOT论坛](https://bbs.nukkit-mot.com/resources/) — 面向Nukkit-MOT的插件资源站。
- [MineBBS](https://www.minebbs.com/resources/categories/nukkit.40/) — 中文社区插件库。
- GitHub — 搜索开源Nukkit插件项目。

下载插件时请注意确认插件支持的Nukkit版本，并查看其依赖说明。

安装步骤如下：

1. 下载插件，并确认它支持目标Nukkit-MOT版本。
2. 检查插件是否依赖其他插件。
3. 把`.jar`放入服务器的`plugins`文件夹。
4. 重启服务器。
5. 在控制台执行`plugins`或`pl`查看插件列表。

绿色插件名表示加载成功，红色插件名表示加载失败。加载失败时先检查版本兼容、缺少依赖和控制台报错。

大多数插件会在首次加载后生成配置文件，通常位于`plugins/插件名称/config.yml`。修改插件配置后，优先重启服务器。频繁使用`reload`可能导致内存泄漏或其他问题，因此不建议把它当成日常重载方式。

如果你想编写插件，而不是只安装插件，可以继续阅读[Nukkit-MOT API概览](../../refs/server/nukkit-mot-api.md)。

## 常见问题

### 服务器无法启动

先检查Java版本：

```bash
java -version
```

如果Java版本低于17，重新安装Java17或更高版本。如果启动窗口一闪而过，还应检查启动脚本中的JAR文件名是否与实际文件名一致。

如果出现：

```text
Could not reserve enough space for object heap
```

说明内存分配过高或系统剩余内存不足。可以把`-Xmx1G`临时改成`-Xmx512M`测试。

### 玩家无法连接

无法连接时，按顺序检查：

1. 服务端控制台是否已经出现启动完成提示。
2. 客户端填写的地址和端口是否正确。
3. 防火墙是否允许UDP端口入站。
4. 端口是否已被其他程序占用。
5. 中国版客户端是否已开启`netease-client-support`<!-- md:flag china -->。

端口被占用时，控制台可能出现`Address already in use`。可以关闭占用程序，或修改`server.properties`中的`server-port`。

### 插件加载失败

插件在`plugins`命令结果中显示为红色时，通常是版本不兼容、缺少依赖或配置文件格式错误。先阅读控制台完整报错，再对照插件文档处理。必要时可以删除插件生成的配置文件，让插件重新生成默认配置。

### 服务器卡顿

常见原因包括内存不足、视距过高、加载区块过多和插件性能问题。可以先降低`view-distance`，减少同时在线玩家数，再逐个停用插件排查。

### 世界或数据损坏

服务器无法加载世界时，先停止服务器并备份`worlds`文件夹，再尝试处理具体错误。不要在服务器运行时直接编辑世界数据库。日常运维中应定期备份`worlds`文件夹，并使用`stop`命令正常关闭服务器。

### 控制台乱码

Windows系统下控制台可能显示乱码。在启动脚本的第一行添加以下命令后重新运行即可解决：

```bat title="start.bat"
chcp 65001
```

## PocketMine-MP

PocketMine-MP适合需要PHP插件生态的场景。与Nukkit-MOT的JAR启动方式不同，它是一条围绕PHP、`.phar`插件包和`plugin.yml`清单展开的独立路线。

### 准备环境

PocketMine-MP要求64位CPU、64位操作系统和至少1GB内存。Windows、Linux和macOS都在支持范围内。硬件选择上，较高的单核性能通常比单纯堆更多核心更有帮助。

### 下载与启动

进入PocketMine-MP下载页后，选择适合当前平台的安装包或启动脚本。常见启动入口如下：

- Windows：`start.cmd`或`start.ps1`
- Linux与macOS：`start.sh`

首次启动通常会进入设置向导；如果想跳过向导，可以在启动参数中添加`--no-wizard`。启动完成后，PocketMine-MP会生成`server.properties`、`pocketmine.yml`和插件目录等基础文件。

### 配置服务器

PocketMine-MP最常改的两个配置文件是：

- `server.properties`：基础设置，例如服务器名称、端口和视距。
- `pocketmine.yml`：更进阶的运行设置，例如内存、线程和多世界相关选项。

如果只是先把服务器开起来，优先改`server.properties`即可。`pocketmine.yml`中的选项更靠近运行时行为，不理解含义时最好先保持默认值。

资源包相关配置位于`resource_packs/resource_packs.yml`。权限与封禁相关文件则包括：

- `ops.txt`
- `banned-players.txt`
- `banned-ips.txt`

这些名单既可以直接编辑，也可以通过命令维护。

### 安装插件

PocketMine-MP插件通常放在`plugins`目录中，公开分发时常见格式是`.phar`。常见获取渠道包括：

- [Poggit](https://poggit.pmmp.io/plugins)
- GitHub
- 社区论坛或插件发布帖

插件清单文件是`plugin.yml`。至少需要注意以下字段：

- `name`
- `version`
- `main`
- `api`

其中，`api`决定插件是否会被目标服务端加载。它不是随便改一个数字就能兼容的开关；如果插件实际没有覆盖对应版本，就算强行改清单也仍然可能崩溃或行为异常。

`plugin.yml`还常见这些附加字段：

- `load`
- `depend`
- `softdepend`
- `loadbefore`
- `commands`
- `permissions`

看到插件无法加载时，先检查服务端版本、`api`字段、依赖插件和控制台报错，再决定是否更换版本。

### 何时选PocketMine-MP

如果目标是尽量贴近原版生存服，应优先考虑BDS或基于BDS的插件加载器。PocketMine-MP更适合下面这些情况：

- 需要PHP插件生态。
- 已经维护PocketMine-MP插件或插件包。
- 需要独立于BDS的跨平台自实现服务端。

在上线前，仍应单独测试生物、红石、矿车和维度等机制，而不要默认把PocketMine-MP视为完整原版生存服替代品。