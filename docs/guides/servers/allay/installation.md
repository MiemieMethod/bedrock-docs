---
comments: true
---

# 安装Allay

要运行Allay服务端非常简单！本指南将逐步引导你安装和启动第一个Allay服务器。

## 安装Java 21

Allay需要**Java 21**才能运行。有多个Java发行版可供选择，我们推荐以下几个：

- [**GraalVM**](https://www.graalvm.org/) – 性能最佳
- [**OpenJDK**](https://adoptium.net/) – 更稳定和熟悉

/// tip
如果选择GraalVM，我们建议安装最新的**LTS**版本（如22.3 LTS），而不是具体的Java 21版本。
///

安装完成后，使用以下命令验证Java是否正确设置：

```shell
java --version
```

如果一切安装正确，你应该能看到版本信息输出且无错误消息。

## 使用AllayLauncher <small>（推荐）</small>

[AllayLauncher](https://github.com/AllayMC/AllayLauncher)是一个轻量级、快速的工具（使用C++编写），可以帮助你下载、更新和管理Allay服务器。

安装方法非常简单，只需运行一条命令：

/// tab | Windows

```powershell
Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AllayMC/AllayLauncher/refs/heads/main/scripts/install_windows.ps1").Content
```

///
/// tab | Linux

```bash
wget -qO- https://raw.githubusercontent.com/AllayMC/AllayLauncher/refs/heads/main/scripts/install_linux.sh | bash
```

///

## 手动安装Allay

### 下载Allay

从[**GitHub Releases**](https://github.com/AllayMC/Allay/releases/latest)页面获取最新版本。

如需最新功能，也可以尝试从`master`分支构建的[**Nightly Build**](https://github.com/AllayMC/Allay/releases/tag/nightly)。

你会得到一个名称类似于以下格式的文件：

```
allay-server-<版本>-<提交哈希>[-dev]-shaded.jar
```

示例：

```
allay-server-0.1.0-dev-shaded.jar
```

/// note
`-dev`后缀表示开发版本。
///

### 运行服务器

如果你的系统有图形界面（GUI），直接**双击** `.jar`文件即可。

如果Java正确安装，会出现一个类似的窗口。

如果你在无头服务器上运行（没有图形界面），使用以下命令启动服务器：

```bash
java -jar allay-server-*-shaded.jar
```

你会在终端看到相同的启动输出。

## 后续步骤

现在你已经有一个运行中的Allay服务器！接下来可以：

1. 查看[创建第一个插件](first-plugin.md)指南开始开发
2. 探索[命令系统](command-guide.md)文档
3. 了解[事件系统](event-guide.md)的工作方式
