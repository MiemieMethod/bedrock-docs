---
title: 在客户端上安装
---

# 在客户端上安装

## 前提条件

- Windows10(64位)或Windows11(64位)。
- [Visual C++ Redistributable for Visual Studio 2015、2017、2019和2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)。
- [LeviLauncher](https://github.com/LiteLDev/LeviLauncher/releases)。
- [lip](https://github.com/futrime/lip/releases)。

## 使用LeviLauncher自动安装

1. 点击启动器导航栏中的“设置”按钮，向下滚动到lip区域并点击“安装”。
2. 点击启动器导航栏中的“下载”按钮，安装LeviLamina支持的Minecraft基岩版客户端版本。
3. 在启动器的“启动”页面，将版本切换到新安装的版本。
4. 将鼠标悬停在“Mods”选项卡上，再点击选项卡右下角的“管理模组”按钮。
5. 在弹出的模组管理页面中，点击右上角的“安装LeviLamina”按钮。

## 使用lip安装

1. 先通过LeviLauncher安装受支持的客户端版本。具体版本可参考[支持的版本](versions.md)。
2. 通过LeviLauncher打开客户端所在目录，然后在该目录中打开命令行终端。
3. 运行：

```shell
lip install github.com/LiteLDev/LeviLamina#client@版本号
```

示例：

```shell
lip install github.com/LiteLDev/LeviLamina#client@26.10.3
```

## 升级

例如，要升级到26.10.3版本，可以运行：

```shell
lip update github.com/LiteLDev/LeviLamina#client@26.10.3
```

如果需要同时显式更新客户端运行时数据，官方英文页给出的示例如下：

```shell
lip update github.com/LiteLDev/LeviLamina#client@26.10.3 github.com/LiteLDev/bedrock-runtime-data@1.21.132-client.3
```
