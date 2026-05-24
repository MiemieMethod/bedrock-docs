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
3. 如有需要，可以先设置镜像：

```powershell
lip config set go_module_proxy https://goproxy.cn
lip config set github_proxy <GitHub镜像地址>
```

4. 运行：

```powershell
lip install github.com/LiteLDev/LeviLamina
```

5. 如需指定版本，可在包名后追加版本号：

```powershell
lip install github.com/LiteLDev/LeviLamina@x.y.z
```

6. 启动服务器：

```powershell
.\bedrock_server_mod.exe
```

如果需要升级，建议使用：

```powershell
lip update github.com/LiteLDev/LeviLamina
lip update github.com/LiteLDev/LeviLamina@x.y.z
```

!!! warning
    为确保数据安全，请勿在同一目录内更新LeviLamina。建议在独立文件夹内安装新版本，然后复制`worlds`目录并按需更新配置。

## 手动安装

手动安装时通常需要以下组件：

- LeviLamina。
- PreLoader。
- PeEditor。
- bedrock-runtime-data。
- CrashLogger。
- 对应版本的BDS。
- 可选的levilamina-loc本地化文件。

常见目录结构会包含`bedrock_server_mod.exe`和`plugins\LeviLamina\`。完成解压后，通常还需要运行PeEditor生成处理后的启动程序：

```pwsh
.\PeEditor.exe -mb
```

典型布局会类似于：

```text
bedrock_runtime_data
bedrock_server.exe
PeEditor.exe
PreLoader.dll
plugins\
    LeviLamina\
        CrashLogger.exe
        LeviLamina.dll
        LeviLamina.pdb
        manifest.json
        lang\
            en_US.json
            zh_CN.json
```

## 模组安装

模组通常通过lip安装，例如：

```powershell
lip install github.com/LiteLDev/LeviAntiCheat
```

## 备注

安装与升级时，建议先核对[支持的版本](versions.md)。如果遇到启动失败、依赖诊断报错或连接兼容性错误，通常应优先检查BDS版本、LeviLamina版本和模组版本是否匹配。
