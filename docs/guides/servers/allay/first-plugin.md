---
comments: true
---

# 创建第一个插件

欢迎来到**Allay**！Allay提供了强大的插件系统，允许你使用多种语言编写插件——Java、Kotlin、Scala以及任何基于JVM的语言。本指南将逐步引导你用Java创建一个简单的插件。

## 前置条件

开始之前，请确保已安装以下内容：

- [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [JDK 21](installation.md#安装java-21)
- [Allay](installation.md#手动安装allay)

## 项目模板

为了快速开始，你可以使用以下插件模板之一：

- [JavaPluginTemplate](https://github.com/AllayMC/JavaPluginTemplate)
- [KotlinPluginTemplate](https://github.com/MineBuilders/allaymc-kotlin-plugin-template)
- [ScalaPluginTemplate](https://github.com/AllayMC/ScalaPluginTemplate)

本指南将使用**JavaPluginTemplate**。

## 创建新项目

1. 打开[JavaPluginTemplate](https://github.com/AllayMC/JavaPluginTemplate)页面
2. 点击`Use this template`按钮 → `Create a new repository`
3. 输入名称和描述，我们使用`MyPlugin`作为名称
4. 点击`Create repository`

创建完成后，你会被重定向到新仓库的页面。克隆项目到本地：

```bash
git clone https://github.com/yourusername/MyPlugin.git
cd MyPlugin
```

## 初始化项目

在IntelliJ IDEA中打开项目，然后打开`README.md`。按照文件中的说明初始化项目，之后重新加载gradle项目。

/// tip
如果你没有使用`JavaPluginTemplate`，则需要手动编写`plugin.json`文件：

```json linenums="1"
{
  "name": "MyPlugin",
  "entrance": "your.group.name.myplugin.MyPlugin",
  "authors": ["yourname"],
  "version": "0.1.0",
  "api_version": ">=0.1.0",
  "description": "你的插件描述",
  "website": "你的插件网站",
  "dependencies": [
     {
         "name": "AnotherPlugin1"
     },
     {
         "name": "AnotherPlugin2",
         "version": ">=0.1.0",
         "optional": true
     }
 ]
}
```

编辑`plugin.json`时，有几点需要注意：

- 字段`api_version`、`description`、`website`和`dependencies`可以省略
- 插件的`version`必须是有效的[语义版本](https://semver.org/spec/v2.0.0.html)，否则插件不会被加载
- 插件的`api_version`和`dependencies`中的条目`version`可以是表达式，以下是一些示例：
  - **单一版本**
    - `1.2.3`
  - **NPM风格**
    - `>1.2.2`
    - `1.1.1 || 1.2.3 - 2.0.0`
    - `1.1.*`
    - `~1.2.1`
    - `^1.1.1`
  - **COCOAPODS风格**
    - `> 1.2.2`
    - `~> 1.2.1`
    - `<= 1.1.1`
  - **IVY风格**
    - `1.2.+`
    - `(,1.8.9]`
    - `[0.2,1.4]`
///

## 运行包含插件的服务器

如果使用了`AllayGradle`插件（JavaPluginTemplate中已包含），可以直接从项目运行服务器：

```bash
./gradlew runServer
```

## 构建插件

要构建插件，运行：

```bash
./gradlew shadowJar
```

生成的文件会位于：

```
build/libs/MyPlugin-1.0.0-shaded.jar
```

然后将其复制到Allay服务器的`plugins`目录中使用。

---

现在你已经准备好为Allay创建自己的插件了！🎉

接下来，建议学习以下内容：

- [注册命令](command-guide.md) - 实现自定义命令
- [事件系统](event-guide.md) - 监听游戏事件
- [任务调度](schedule-guide.md) - 运行异步任务
