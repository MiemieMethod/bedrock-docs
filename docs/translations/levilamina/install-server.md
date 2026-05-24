---
title: 在服务器上安装
---

# 在服务器上安装

## 前提条件

- Windows 10、Windows 11、Windows Server 2019或Windows Server 2022。
- [Visual C++ Redistributable for Visual Studio 2015、2017、2019和2022](https://aka.ms/vs/17/release/vc_redist.x64.exe)。

## 安装方法

可以按需求选择不同的安装方式：

- [通过lip安装](#通过lip安装)，便于安装与升级，是官方推荐方式。
- [手动安装](#手动安装)，适用于需要完全手动管理文件，或无法直接联网安装的环境。

## 通过lip安装

1. 前往[lip发布页](https://github.com/futrime/lip/releases)，下载文件名以`setup.exe`结尾的安装程序并执行。
2. 如有需要，可以先设置镜像：

```powershell
lip config set go_module_proxy https://goproxy.cn
lip config set github_proxy https://github.bibk.top
```

3. 如有需要，可以通过定义`BDSDOWN_MIRROR_URL`环境变量来自定义BDS下载镜像站，例如`https://www.minecraft.net`。也可以手动从Minecraft官网下载BDS压缩包，再将压缩包放入{{file|.cache\bdsdown}}目录；如果该目录不存在，则需要手动创建。该目录位于BDS安装路径下，例如`C:\Users\YourName\BDS\.cache\bdsdown`。
4. 创建服务器目录并进入该目录：

```powershell
mkdir myserver
cd myserver
```

5. 运行：

```powershell
lip install github.com/LiteLDev/LeviLamina
```

6. 如需指定版本，可在包名后追加版本号：

```powershell
lip install github.com/LiteLDev/LeviLamina@x.y.z
```

7. 启动服务器：

```powershell
.\bedrock_server_mod.exe
```

可用版本号可在[LeviLamina releases](https://github.com/LiteLDev/LeviLamina/releases)查看。

如果需要升级，建议使用：

```powershell
lip update github.com/LiteLDev/LeviLamina
lip update github.com/LiteLDev/LeviLamina@x.y.z
```

/// warning | 升级前先备份
为确保数据安全，请勿在同一目录内更新LeviLamina。建议在独立文件夹内安装新版本，然后复制`worlds`目录并按需更新配置。
///

## 手动安装

手动安装时通常需要以下组件：

- [LeviLamina](https://github.com/LiteLDev/LeviLamina/releases)。
- 根据目标版本[tooth.json](https://github.com/LiteLDev/LeviLamina/blob/main/tooth.json)下载的[PreLoader](https://github.com/LiteLDev/PreLoader/releases)。
- 最新版[PeEditor](https://github.com/LiteLDev/PeEditor/releases)。
- 根据`tooth.json`下载的[bedrock-runtime-data](https://github.com/LiteLDev/bedrock-runtime-data/releases)。
- 最新版[CrashLogger](https://github.com/LiteLDev/CrashLogger/releases)。
- 根据[支持的版本](versions.md)选择并下载的BDS。
- 可选的[levilamina-loc](https://github.com/LiteLDev/levilamina-loc/releases)本地化文件。

完成下载后，先创建一个Minecraft服务器目录，并将各文件按下列结构解压。未列出的文件或文件夹同样可以存在：

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

然后运行以下命令生成{{file|bedrock_server_mod.exe}}：

```pwsh
.\PeEditor.exe -mb
```

## 搜寻模组

安装模组前，建议先了解可用来源。官方文档提到的首选来源是模组包索引[Bedrinth](https://pkg.levimc.org)，其他站点也可能提供更多模组包。

## 安装模组

模组包通常通过lip安装，例如：

```powershell
lip install github.com/LiteLDev/LeviAntiCheat
```

如有需要，还应继续遵循各模组开发者提供的附加说明。
