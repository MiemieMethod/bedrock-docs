# 搭建BDS

BDS是Mojang官方提供的基岩版专用服务器。它可以在Windows和Ubuntu Linux上运行，适合先学习基岩版服务器的目录结构、配置文件、端口和世界管理。

## 下载和启动

从Minecraft官网下载基岩版专用服务器压缩包，解压到空文件夹，例如Windows上的`C:\MinecraftServer`。

Windows中进入目录后执行：

```powershell
cd C:\MinecraftServer
.\bedrock_server.exe
```

Ubuntu Linux中进入目录后执行：

```bash
LD_LIBRARY_PATH=. ./bedrock_server
```

官方资料说明，Ubuntu是BDS唯一官方支持的Linux发行版。首次启动后，服务器会生成`worlds`、`behavior_packs`、`resource_packs`等目录。

## 开放端口

默认IPv4端口是`19132`，默认IPv6端口是`19133`。如果服务器运行在Linux并启用了`ufw`，可以开放端口：

```bash
sudo ufw allow 19132
sudo ufw allow 19133
sudo ufw reload
```

Windows Defender弹窗时，如果只给局域网玩家连接，选择专用网络；如果要让互联网玩家连接，还需要允许公用网络，并正确配置路由器和防火墙。

## 本机连接回环

Windows版Minecraft默认不能直接连接同一台机器上的BDS。停止服务器后，以管理员权限执行：

```text
CheckNetIsolation.exe LoopbackExempt -a -p=S-1-15-2-1958404141-86561845-1752920682-3514627264-368642714-62675701-733520436
```

如果使用预览版客户端和预览版服务器，需要使用预览版对应的回环命令。完成后，在游戏中添加服务器地址`127.0.0.1`，端口保持`19132`。

## 认识目录

/// html | div.treeview
- BDS根目录
    - `bedrock_server.exe`
    - `server.properties`
    - `allowlist.json`
    - `permissions.json`
    - `worlds`
    - `behavior_packs`
    - `resource_packs`
///

`worlds`保存服务器世界。只有`server.properties`中`level-name`指定的世界会被当前服务器加载。根目录下的`behavior_packs`和`resource_packs`是共享包目录；世界目录内部也可以有自己的包目录，后者只对该世界生效。

## 修改`server.properties`

`server.properties`是INI风格配置文件，每行一个`key=value`。常见字段包括：

```ini title="server.properties"
server-name=Dedicated Server
gamemode=survival
difficulty=easy
allow-cheats=false
max-players=10
online-mode=true
allow-list=false
server-port=19132
server-portv6=19133
level-name=Bedrock level
```

官方属性参考提醒，`online-mode=true`会要求玩家通过Xbox Live身份验证；如果服务器接受互联网连接，强烈建议保持开启。`view-distance`、`tick-distance`和`max-players`调高都会增加性能压力。

## 白名单和权限

把`allow-list=true`写入`server.properties`后，只有`allowlist.json`中的玩家能进入服务器。可以在游戏或控制台执行：

```text
allowlist add <玩家名>
allowlist remove <玩家名>
allowlist reload
```

常用控制台命令还包括`op <playername>`、`deop <playername>`、`gamerule`和`stop`。配置文件改完后，通常重启服务器最稳。
