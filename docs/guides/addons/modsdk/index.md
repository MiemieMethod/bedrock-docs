# 模组SDK<!-- md:flag china -->

这一组教程只讲中国版模组SDK。它使用MC Studio、Python脚本、`mod.server.extraServerApi`和`mod.client.extraClientApi`，属于中国版附加包开发体系；它不讲国际版脚本API，也不使用`@minecraft/server`。

/// html | div.grid.cards
- :material-language-python: __[第一个Python脚本模组](first-python-mod.md)__
  从“入门脚本模板”开始，认识`modMain.py`、脚本目录和一次简单的方块交互。
- :material-lan: __[系统、事件与组件](systems-events-components.md)__
  学会注册服务端系统和客户端系统，监听引擎事件，并调用组件接口完成逻辑。
- :material-monitor-dashboard: __[制作中国版模组SDK界面](custom-ui.md)__
  从UI编辑器、JSON界面文件到`ScreenNode`脚本类，走通中国版自定义UI的基本工作流。
- :material-image-filter-hdr: __[中国版数据驱动维度与地形](custom-dimensions-and-terrain.md)__
  使用中国版专有的`netease_dimension`、`netease_biomes`和地物目录创建维度、生物群系与地形内容。
- :material-book-open-page-variant: __[制作自定义书本](custom-books.md)__
  使用`customBooks`、书本JSON和`BookManager`制作可翻阅的中国版模组内说明书。
///

## 开发环境

中国版模组SDK通常从MC Studio开始。官方入门资料要求先安装我的世界开发工作台、登录网易通行证并注册开发者账号，然后新建基岩版组件。你可以从空白附加包开始，也可以直接使用“入门脚本模板”来观察官方提供的目录结构。

Python脚本开发使用Python2。官方资料还提供了两种补全库安装方式：

```powershell
python -m pip install mc-netease-sdk
```

或在MC Studio菜单中下载稳定版或测试版补全库。补全库只帮助编辑器提示接口，不等于把脚本运行环境改成Python3。

/// warning | 不要把Python3写法直接搬进项目
中国版模组SDK脚本运行环境按官方资料使用Python2。编写脚本时要避免只在Python3中存在的语法和库行为。
///

## 一个模组里有什么

脚本通常放在行为包中的一个独立脚本根目录里。官方入门模板的结构类似这样：

/// html | div.treeview
- behavior_pack_xxx
    - entities
    - tutorialScripts
        - `__init__.py`
        - `modMain.py`
        - `tutorialClientSystem.py`
        - `tutorialServerSystem.py`
    - `manifest.json`
///

其中`__init__.py`表示这是可导入的Python模块；`modMain.py`是模组初始化入口，必须存在；客户端系统处理界面、特效等表现逻辑，服务端系统处理给予物品、记分、实体逻辑等游戏规则。

## 客户端和服务端要分开想

中国版模组SDK明确区分客户端脚本和服务端脚本。服务端负责游戏逻辑，客户端负责用户界面和表现效果；服务端事件、服务端组件只能在服务端系统中使用，客户端事件、客户端组件只能在客户端系统中使用。两边需要通信时，应使用自定义事件，而不是互相导入对方代码。

## 调试方式

模组SDK资料说明当前Mod代码不支持断点调试，常用方式是在关键位置打印日志。可以使用`print`，也可以使用`mod_log`：

```python
from mod_log import logger

logger.info("mod log: %s", "OK")
```

MC Studio支持Python脚本热更新。修改函数内部实现时通常可以自动重载；新增类、文件或全局变量变动不一定生效，这时需要保存退出到菜单界面，再重新进入存档。

/// note | 旧版MC Studio资料
如果项目来自2020年至2021年前后的旧版MC Studio教程，可能还会遇到地图编辑器、关卡编辑器、逻辑编辑器、特效编辑器、界面编辑器和调试工具等历史入口。它们与当前国际版编辑器无关，维护时可参见[旧版中国版MC Studio工具链](../../outdated/china-legacy-mc-studio.md)。
///