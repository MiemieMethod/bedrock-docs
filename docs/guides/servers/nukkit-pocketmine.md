# Nukkit、PocketMine与旧生态

这一页用于整理基岩版社区自实现服务端中的旧生态入口。这里的“Nukkit”主要指Nukkit-MOT。它是第三方服务端，不是BDS，也不是Mojang提供的官方服务器软件；它的插件、配置项和中国版客户端兼容能力都只应放在Nukkit-MOT语境中理解。

想先了解概念定位，可以阅读[Nukkit-MOT](../../docs/server/nukkit-mot.md)。本页只讲怎样搭建一个最小可用服务器。

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

大多数插件会在首次加载后生成配置文件，通常位于`plugins/插件名称/config.yml`。修改插件配置后，优先重启服务器。Nukkit-MOT文档提示，频繁使用`reload`可能导致内存泄漏或其他问题，因此不建议把它当成日常重载方式。

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

## PocketMine-MP资料现状

知识库现已收录PocketMine-MP官方文档。当前能够直接核对到的内容包括安装条件、首次启动流程、配置文件、插件分发方式以及插件开发入口。

可以先把PocketMine-MP理解为一条面向PHP插件生态的独立服务端路线：

- 环境要求方面，官方文档要求64位CPU、64位操作系统和至少1GB内存，并说明Windows、Linux和macOS都在官方尽量支持的范围内。
- 启动方式方面，Windows可使用`start.cmd`或`start.ps1`，Linux与macOS使用`start.sh`。首次启动会进入设置向导，也可以通过`--no-wizard`跳过。
- 配置方面，`server.properties`负责名称、端口和视距等基础设置，`pocketmine.yml`负责更进阶的内存、线程和多世界相关设置。
- 插件方面，官方文档说明插件通常以`.phar`文件分发，放入`plugins`目录即可加载；公开插件主要集中在Poggit。插件描述文件是`plugin.yml`，关键字段包括`name`、`version`、`main`和`api`。

PocketMine-MP官方文档也明确提醒：它不是原版生存服务器实现，原版世界生成、红石、生物AI等能力并不完整。因此，如果目标是尽量贴近原版生存服，应优先考虑BDS；如果目标是PHP插件生态和高度定制能力，则PocketMine-MP仍然有独立价值。
