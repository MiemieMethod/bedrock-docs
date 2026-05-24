---
title: 在服务器上安装
---

# 在服务器上安装

## 前提条件

- Windows 10、Windows 11、Windows Server 2019或Windows Server 2022。
- [Visual C++ Redistributable for Visual Studio 2015、2017、2019和2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)。

## 通过lip安装

1. 下载并安装lip。
2. 创建服务器目录并进入该目录。
3. 运行：

```powershell
lip install github.com/LiteLDev/LeviLamina
```

4. 如需指定版本，可在包名后追加版本号：

```powershell
lip install github.com/LiteLDev/LeviLamina@x.y.z
```

5. 启动服务器：

```powershell
.\bedrock_server_mod.exe
```

## 手动安装

手动安装时通常需要以下组件：

- LeviLamina。
- PreLoader。
- PeEditor。
- bedrock-runtime-data。
- CrashLogger。
- 对应版本的BDS。
- 可选的levilamina-loc本地化文件。

常见目录结构会包含`bedrock_server_mod.exe`和`plugins\LeviLamina\`。

## 模组安装

模组通常通过lip安装，例如：

```powershell
lip install github.com/LiteLDev/LeviAntiCheat
```

## 备注

安装与升级时，建议先核对[支持的版本](versions.md)。

