---
title: 在Docker上安装
---

# 在Docker上安装

## 安装

要在Linux容器中启动服务器，请运行以下命令：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:/data ghcr.io/liteldev/levilamina-server:latest-wine
```

如果服务器位于中国大陆，可改用下列命令以加速安装：

```sh
docker run -d -it -e EULA=TRUE -e GO_MODULE_PROXY_URL=https://goproxy.cn -e GITHUB_MIRROR_URL=https://github.bibk.top -p 19132:19132/udp -v levilamina-server-data:/data ghcr.nju.edu.cn/liteldev/levilamina-server:latest-wine
```

如果要使用Windows容器，请运行以下命令：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:C:\data ghcr.io/liteldev/levilamina-server:latest-windows
```

如果服务器位于中国大陆，可改用下列命令以加速安装：

```sh
docker run -d -it -e EULA=TRUE -e GO_MODULE_PROXY_URL=https://goproxy.cn -e GITHUB_MIRROR_URL=https://github.bibk.top -p 19132:19132/udp -v levilamina-server-data:C:\data ghcr.nju.edu.cn/liteldev/levilamina-server:latest-windows
```

仓库还提供了分别用于Linux容器和Windows容器的Docker Compose文件：[wine/compose.yaml](https://github.com/LiteLDev/docker-levilamina-server/blob/main/wine/compose.yaml)与[windows/compose.yaml](https://github.com/LiteLDev/docker-levilamina-server/blob/main/windows/compose.yaml)。将对应文件下载到空目录后，运行`docker compose up -d`即可。

## 环境变量

- `EULA`：必须设置为`TRUE`，用于接受[Minecraft最终用户许可协议](https://minecraft.net/terms)。
- `GITHUB_MIRROR_URL`：可设置为GitHub镜像地址，以加速LeviLamina安装。
- `GO_MODULE_PROXY_URL`：可设置为Go模块代理地址，以加速LeviLamina安装。
- `PACKAGES`：可设置为首次运行时安装的lip包列表。每个包都必须符合[lip安装规范](https://lip.levimc.org/cli/commands/install.html)，并支持本地与远程lip包。
- `VERSION`(`LATEST`)：可设置为特定的[LeviLamina版本](https://github.com/LiteLDev/LeviLamina/tags)，或使用`LATEST`自动下载最新版本。
- `WINEDEBUG`(`-all`)：可自定义Wine调试输出，仅Wine镜像可用。更多信息见[Wine Debugging](https://wiki.winehq.org/Debugging)。
- `LANG`：用于设置容器的语言环境，默认值为`en_US.UTF-8`。
- `LC_ALL`：用于设置容器的语言环境，默认值为`en_US.UTF-8`。
- `TZ`：用于设置容器时区，默认值为`UTC`。