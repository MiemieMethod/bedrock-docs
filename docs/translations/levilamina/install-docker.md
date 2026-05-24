---
title: 在Docker上安装
---

# 在Docker上安装

## 安装

Linux容器：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:/data ghcr.io/liteldev/levilamina-server:latest-wine
```

Windows容器：

```sh
docker run -d -it -e EULA=TRUE -p 19132:19132/udp -v levilamina-server-data:C:\data ghcr.io/liteldev/levilamina-server:latest-windows
```

也可以使用仓库提供的Docker Compose文件，再运行`docker compose up -d`。

## 环境变量

- `EULA`：必须为`TRUE`。
- `GITHUB_MIRROR_URL`：GitHub镜像地址。
- `GO_MODULE_PROXY_URL`：Go模块代理地址。
- `PACKAGES`：首次运行时安装的lip包列表。
- `VERSION`：指定LeviLamina版本，或使用`LATEST`。
- `WINEDEBUG`：仅Wine镜像可用。
- `LANG`、`LC_ALL`、`TZ`：容器语言环境与时区。

