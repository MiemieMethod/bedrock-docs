---
title: 在Docker上安装
---

# 在Docker上安装

## 安装

Linux容器：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:/data ghcr.io/liteldev/levilamina-server:latest-wine
```

如果需要使用国内镜像并加速安装，可以改为：

```sh
docker run -d -it -e EULA=TRUE -e GO_MODULE_PROXY_URL=https://goproxy.cn -e GITHUB_MIRROR_URL=https://github.bibk.top -p 19132:19132/udp -v levilamina-server-data:/data ghcr.nju.edu.cn/liteldev/levilamina-server:latest-wine
```

Windows容器：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:C:\data ghcr.io/liteldev/levilamina-server:latest-windows
```

如果需要使用国内镜像并加速安装，可以改为：

```sh
docker run -d -it -e EULA=TRUE -e GO_MODULE_PROXY_URL=https://goproxy.cn -e GITHUB_MIRROR_URL=https://github.bibk.top -p 19132:19132/udp -v levilamina-server-data:C:\data ghcr.nju.edu.cn/liteldev/levilamina-server:latest-windows
```

也可以使用仓库提供的Docker Compose文件，分别对应Linux和Windows容器；下载到空目录后运行`docker compose up -d`即可。

## 环境变量

- `EULA`：必须设置为`TRUE`，用于接受Minecraft最终用户许可协议。
- `GITHUB_MIRROR_URL`：可设置为GitHub镜像地址，以加速LeviLamina安装。
- `GO_MODULE_PROXY_URL`：可设置为Go模块代理地址，以加速LeviLamina安装。
- `PACKAGES`：可设置为首次运行时安装的lip包列表，支持本地和远程包。
- `VERSION`：可设置为特定LeviLamina版本，或使用`LATEST`自动下载最新版本。
- `WINEDEBUG`：可自定义Wine调试输出，仅Wine镜像可用。
- `LANG`、`LC_ALL`、`TZ`：用于设置容器语言环境与时区。

