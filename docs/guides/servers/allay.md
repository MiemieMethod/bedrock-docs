# Allay入门

Allay是一个使用Java21运行的社区基岩版自实现服务端。它不是BDS插件加载器，而是重新实现服务端逻辑并提供自己的JVM插件API。想先了解它的定位、架构和限制，可以先读[Allay](../../docs/server/allay.md)。

/// warning | 不要把Allay能力当成BDS能力
Allay的插件、配置文件、世界生成器和线程模型都属于Allay生态。BDS、LeviLamina、Endstone、Nukkit和PocketMine-MP的插件不能直接放到Allay中运行。
///

## 准备Java21

Allay要求Java21运行。官方资料推荐GraalVM以获得较好的性能，也推荐OpenJDK作为更稳定、熟悉的选择。安装后先在终端确认版本：

```powershell
java --version
```

输出中应能看到Java21或更新的兼容运行时。如果系统同时安装了多个Java版本，请确认`JAVA_HOME`和终端中的`java`命令指向同一套JDK或JRE。

## 安装Allay

文档推荐使用AllayLauncher下载、更新和管理服务器。Windows可以在PowerShell中运行官方安装脚本：

```powershell
Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/AllayMC/AllayLauncher/refs/heads/main/scripts/install_windows.ps1").Content
```

Linux可以运行：

```bash
wget -qO- https://raw.githubusercontent.com/AllayMC/AllayLauncher/refs/heads/main/scripts/install_linux.sh | bash
```

如果当前平台不适合使用AllayLauncher，也可以从Allay发行页手动下载服务器JAR。文件名通常类似：

```text
allay-server-<version>-<commit-hash>[-dev]-shaded.jar
```

`-dev`后缀表示开发构建。把JAR放入单独的服务器目录后，在无图形界面的服务器中执行：

```bash
java -jar allay-server-*-shaded.jar
```

有图形界面的系统也可以双击JAR启动，但实际部署时更推荐使用终端，以便观察日志、停止服务器和排查错误。

## 认识服务器目录

Allay会在工作目录下生成配置、世界和插件相关文件。反复出现的几个路径如下：

| 路径 | 作用 |
|------|------|
| `plugins` | 放置Allay插件JAR。 |
| `worlds` | 存放Allay世界数据和世界设置。 |
| `worlds/world-settings.yml` | 配置世界、维度高度和世界生成器。 |
| `dimension-ids.yml` | 较新版本用于持久保存自定义维度标识符和数值ID映射。 |
| `biome_ids.yml` | 较新版本用于持久保存自定义生物群系ID映射。 |

这些文件属于Allay服务器结构，不应直接套用BDS的目录说明。

## 创建第一个插件

Allay插件可以使用Java、Kotlin、Scala以及其他JVM语言编写。官方教程推荐从模板项目开始：

- `JavaPluginTemplate`
- `KotlinPluginTemplate`
- `ScalaPluginTemplate`

以Java模板为例：

1. 打开`JavaPluginTemplate`仓库。
2. 使用`Use this template`创建自己的仓库。
3. 克隆仓库到本地。
4. 在IntelliJ IDEA中打开项目。
5. 按模板`README.md`完成项目初始化。
6. 重新加载Gradle项目。

如果不用模板，需要自己编写`plugin.json`：

```json title="plugin.json"
{
  "name": "MyPlugin",
  "entrance": "your.group.name.myplugin.MyPlugin",
  "authors": ["yourname"],
  "version": "0.1.0",
  "description": "The description of your plugin",
  "website": "The website of your plugin",
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

其中`version`必须是合法语义化版本，否则插件不会加载。当前公开的插件描述文件架构还列出了`description`、`website`和`dependencies`等可选字段；`dependencies`中的每一项可填写`name`、`version`和`optional`。

## 运行和构建

如果模板已经包含AllayGradle插件，可以从项目目录直接启动带插件的测试服务器：

```bash
./gradlew runServer
```

构建插件：

```bash
./gradlew shadowJar
```

产物通常位于：

```text
build/libs/MyPlugin-1.0.0-shaded.jar
```

把生成的`.jar`复制到Allay服务器的`plugins`目录，然后重启服务器即可加载插件。

## 编写插件入口

Allay插件主类继承`Plugin`。旧插件开发资料说明，插件会经历加载、启用和禁用阶段：

```java title="MyPlugin.java"
import org.allaymc.api.plugin.Plugin;

public class MyPlugin extends Plugin {
    @Override
    public void onLoad() {
        getPluginLogger().info("Loading MyPlugin");
    }

    @Override
    public void onEnable() {
        getPluginLogger().info("Enabling MyPlugin");
    }

    @Override
    public void onDisable() {
        getPluginLogger().info("Disabling MyPlugin");
    }
}
```

`onLoad()`只适合做与游戏状态无关的准备。注册命令、监听事件、创建调度任务和访问世界等操作应放到`onEnable()`或更晚的时机。

## 常见API入口

Allay教程覆盖了命令、事件、调度器、容器、表单、Boss栏、记分板、配置、国际化、权限、持久化数据容器、方块API、物品API以及高级自定义方块和物品。概要可查[Allay API概览](../../refs/server/allay-api.md)。

最常见的几个入门动作如下：

- 注册命令：继承`Command`，在`prepareCommandTree()`中构造命令树，然后注册到命令注册表。
- 监听事件：编写带`@EventHandler`的方法，并在事件总线注册监听器。
- 定时任务：根据访问范围选择服务器、世界、维度或实体调度器。
- 保存数据：简单配置使用`Config`，绑定到物品、实体、方块实体或世界的数据可考虑持久化数据容器。

## 使用Terra世界生成器

Allay官方资料还给出Terra插件示例。下载`Terra-allay-<version>-shaded.jar`后，把它移动到Allay的`plugins`目录。然后编辑`worlds/world-settings.yml`，把目标维度的生成器改为`TERRA`：

```yaml title="worlds/world-settings.yml"
worlds:
  world:
    storage-type: LEVELDB
    dimensions:
      minecraft:overworld:
        generator-type: TERRA
        generator-preset: meta-pack=DEFAULT;seed=114514
```

如果世界已经生成过，修改生成器后通常需要删除旧世界数据库，或者另建新世界测试。Terra是Allay插件生态能力，不是BDS原生世界生成插件接口。

## 下一步

- 如果要比较服务端生态，继续阅读[插件加载器](../../docs/server/plugin-loader.md)。
- 如果要查Allay概念和限制，阅读[Allay](../../docs/server/allay.md)。
- 如果要查Allay接口分类，阅读[Allay API概览](../../refs/server/allay-api.md)。