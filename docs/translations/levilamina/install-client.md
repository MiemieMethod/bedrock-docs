---
title: 在客户端上安装
---

# 在客户端上安装

## 前提条件

- Windows 10(64位)或Windows 11(64位)。
- [Visual C++ Redistributable for Visual Studio 2015、2017、2019和2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)。
- [LeviLauncher](https://github.com/LiteLDev/LeviLauncher/releases)。
- [lip](https://github.com/futrime/lip/releases)。

## 使用LeviLauncher自动安装

1. 在启动器设置中安装lip。
2. 下载LeviLamina支持的基岩版客户端版本。
3. 切换到新安装的版本。
4. 打开插件管理页面并安装LeviLamina。

## 使用lip安装

1. 先通过LeviLauncher安装受支持的客户端版本。
2. 在客户端目录中打开命令行终端。
3. 运行：

```shell
lip install github.com/LiteLDev/LeviLamina#client@版本号
```

示例：

```shell
lip install github.com/LiteLDev/LeviLamina#client@26.10.3
```

## 升级

```shell
lip update github.com/LiteLDev/LeviLamina#client@26.10.3
```

