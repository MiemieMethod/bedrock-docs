# Endstone入门

Endstone为官方BDS提供第三方插件API，支持Python和C++插件。它适合想保留BDS行为，又希望用较高层接口扩展服务器的人。本文只说明Endstone生态的使用方式，不把Endstone能力视为BDS原生能力。

/// info | 本系列后续页面
- [EndstonePython插件工作流](python-plugin-workflow.md)
- [Endstone命令、事件与调度实战](command-event-task.md)
///

/// tip | 先理解定位
如果还不熟悉BDS目录、{{file|server.properties|txt}}和服务端端口，请先阅读[搭建BDS](../bds.md)。Endstone仍以BDS为基础，客户端版本、世界目录、资源包和行为包规则不会因此变成另一套系统。
///

## 安装

Endstone官方文档推荐Python3.10或更高版本。Windows需要Windows10或更新系统；Linux发行版以Ubuntu22.04或Debian12等较新的环境为宜。若准备开发Python插件，建议始终使用虚拟环境：

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install endstone
```

Linux中的虚拟环境激活命令通常是：

```bash
. venv/bin/activate
```

如果不想配置Python环境，也可以使用Docker：

```powershell
docker pull endstone/endstone
```

## 启动服务器

进入希望作为服务器根目录的文件夹，执行：

```powershell
endstone
```

第一次运行时，Endstone会引导下载官方BDS。若终端提示确认下载，按提示确认即可。Docker方式可以用端口映射启动：

```powershell
docker run --rm -it -v ${PWD}:/home/endstone -p 19132:19132/udp endstone/endstone
```

在Command Prompt中，当前目录变量写法不同：

```cmd
docker run --rm -it -v "%cd%":/home/endstone -p 19132:19132/udp endstone/endstone
```

启动完成后，服务器目录会逐步出现BDS文件、世界目录、日志目录以及Endstone使用的{{file|plugins}}目录。插件安装与开发通常围绕这个{{file|plugins}}目录进行。

## 第一个Python插件

Endstone教程要求Python插件项目名使用`lower-case-with-dash`，并且项目名以`endstone-`开头。包名则通常把短横杠换成下划线。

最小项目需要`pyproject.toml`：

```toml title="pyproject.toml"
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "endstone-my-plugin"
version = "0.1.0"
description = "My first Python plugin for Endstone servers!"

[project.entry-points."endstone"]
my-plugin = "endstone_my_plugin:MyPlugin"
```

`[project.entry-points."endstone"]`用于让Endstone发现插件入口。入口点名称应为项目名去掉`endstone-`前缀后的部分；入口点值使用`模块:类`格式。

然后创建插件类：

```python title="src/endstone_my_plugin/my_plugin.py"
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    def on_load(self) -> None:
        self.logger.info("on_load is called!")

    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")

    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")
```

`api_version`应与目标Endstone API主次版本匹配。实际编写时请按当前安装的Endstone版本填写，不要照抄旧教程中的版本号。

在同包的`__init__.py`中导出类：

```python title="src/endstone_my_plugin/__init__.py"
from endstone_my_plugin.my_plugin import MyPlugin

__all__ = ["MyPlugin"]
```

## 安装正在开发的Python插件

插件完成后，可以先构建轮子包：

```powershell
pip install pipx
pipx run build --wheel
```

构建产物位于{{file|dist}}目录。把生成的`.whl`文件复制到Endstone服务器的{{file|plugins}}目录，然后重启服务器即可加载。

开发阶段可以改用可编辑安装。确认当前虚拟环境中已经安装Endstone后，在插件项目根目录执行：

```powershell
pip install --editable .
```

之后修改源码并在Endstone中执行`/reload`，通常即可让变更生效。若修改了依赖、入口点或插件元数据，仍建议重启服务器。

## 注册命令

Python插件可以在插件类中声明`commands`和`permissions`。Endstone教程指出，命令默认需要操作员权限；若希望所有玩家都能执行，应显式设置权限默认值。

```python title="src/endstone_my_plugin/my_plugin.py"
from endstone.command import Command, CommandSender
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    commands = {
        "hello": {
            "description": "Greet the command sender.",
            "usages": ["/hello [msg: message]"],
            "permissions": ["my_plugin.command.hello"],
        }
    }

    permissions = {
        "my_plugin.command.hello": {
            "description": "Allow users to use the /hello command.",
            "default": True,
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if command.name == "hello":
            sender.send_message(args[0] if args else "Hello World!")
        return True
```

`[msg: message]`表示可选的消息参数。Endstone支持的命令参数类型和权限默认值见[Endstone命令与文本格式](../../../refs/server/endstone-command-format.md)。

## 监听事件

Endstone事件处理器使用`@event_handler`装饰器声明，并在插件启用阶段注册。下面的示例在玩家加入时广播一条黄色消息：

```python title="src/endstone_my_plugin/my_plugin.py"
from endstone import ColorFormat
from endstone.event import PlayerJoinEvent, event_handler
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent) -> None:
        self.server.broadcast_message(ColorFormat.YELLOW + f"{event.player.name}加入了服务器" + ColorFormat.RESET)
```

并非所有事件都可以取消。编写实际插件时，应查阅对应事件类的API文档或类型提示，确认事件对象是否提供取消、修改消息、修改目标等能力。

## 调度任务

Endstone调度器可以在未来刻执行任务，也可以按固定周期重复执行。下面的示例每20刻向所有在线玩家发送一次弹出文本：

```python title="src/endstone_my_plugin/my_plugin.py"
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    def on_enable(self) -> None:
        self.server.scheduler.run_task(self, self.say_hi, delay=0, period=20)

    def say_hi(self) -> None:
        for player in self.server.online_players:
            player.send_popup("Hi!")
```

20刻约等于1秒，但服务器卡顿时实际耗时会随服务端滴答速度变化。需要等待真实时间或进行外部网络请求时，应避免在主服务器线程中长时间阻塞。

## C++方向

如果选择C++插件，Endstone教程要求CMake不低于3.15，Windows上使用Visual Studio2017或更新版本，Linux上使用带Clang和libc++的LLVM工具链。C++插件通过`endstone_add_plugin`添加目标，并继承`endstone::Plugin`。

最小CMake配置大致如下：

```cmake title="CMakeLists.txt"
cmake_minimum_required(VERSION 3.15)

project(my_plugin CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
    endstone
    GIT_REPOSITORY https://github.com/EndstoneMC/endstone.git
    GIT_TAG v0.11
)
FetchContent_MakeAvailable(endstone)

endstone_add_plugin(${PROJECT_NAME} src/my_plugin.cpp)
```

插件类继承`endstone::Plugin`，并通过`ENDSTONE_PLUGIN`声明插件元数据：

```cpp title="src/my_plugin.cpp"
#include "my_plugin.h"

ENDSTONE_PLUGIN("my_plugin", "0.1.0", MyPlugin)
{
    description = "My first C++ plugin for Endstone servers";
}
```

C++插件名应只包含小写字母、数字和下划线。构建产物通常是动态库；将其复制到Endstone服务器的{{file|plugins}}目录后，重启服务器即可加载。

## 发布Python插件

Python插件可以按普通Python包发布。官方教程使用`twine`上传到TestPyPI或PyPI：

```powershell
pip install twine
pipx run build
twine upload -r testpypi dist/*
twine upload -r pypi dist/*
```

正式发布前应更新版本号、补充发布说明，并优先使用API令牌而非账号密码上传。若使用GitHub Actions等自动化流程，应把令牌保存为仓库机密，不要写入源码。

/// tip | 先从Python开始
如果你的目标是快速验证服务器玩法，Python插件的上手成本通常更低。确认API模型后，再决定是否为了性能或二进制集成转向C++。
///

## 进一步阅读

- [EndstonePython插件工作流](python-plugin-workflow.md)
- [Endstone命令、事件与调度实战](command-event-task.md)
- [颜色代码](color-codes.md)
- [Endstone API总览](../../../refs/server/endstone-api.md)
- [Endstone命令与文本格式](../../../refs/server/endstone-command-format.md)
- [Endstone原文目录](../../../translations/endstone/index.md)
