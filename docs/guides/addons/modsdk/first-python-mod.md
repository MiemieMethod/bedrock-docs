# 第一个Python脚本模组<!-- md:flag china -->

这一课会做一个很小的功能：玩家右击自定义方块时，服务端往玩家背包里放入一把钻石剑。它来自官方“脚本开发入门”的思路，重点不是钻石剑，而是让你看清楚事件监听和组件调用是怎样连起来的。

## 从入门模板开始

在MC Studio中创建“入门脚本模板”，进入开发测试。官方模板的默认效果是：进入世界后，在聊天栏输入“钻石剑”，背包中会出现一把钻石剑。这个效果说明脚本已经能够监听聊天事件，并调用物品组件修改玩家背包。

接下来可以把模板里的`tutorialScripts`复制到自己的行为包中，用编辑器打开行为包目录。脚本根目录至少要保留：

/// html | div.treeview
- tutorialScripts
    - `__init__.py`
    - `modMain.py`
    - `tutorialClientSystem.py`
    - `tutorialServerSystem.py`
///

`modMain.py`负责把客户端系统和服务端系统注册给引擎；真正的事件逻辑通常写在对应的系统类中。

如果你不是从模板开始，而是在MC Studio中创建了“空白附加包”，流程也类似：在作品库的基岩版组件中找到作品，使用“更多”菜单打开目录，然后在行为包文件夹内创建自己的脚本根目录。MC Studio可能会给`behavior_pack`和`resource_pack`目录追加后缀，这是正常现象；脚本应放在行为包一侧，而不是资源包一侧。

/// warning | 保留Python包标识文件
脚本根目录和需要被导入的子目录都应包含`__init__.py`。如果日志没有输出，也没有明显的语法错误，优先检查脚本目录、`modMain.py`中的类路径，以及各级目录中的`__init__.py`。
///

## 认识`modMain.py`

最小化入口大致如下：

```python title="tutorialScripts/modMain.py"
from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="TutorialMod", version="0.0.1")
class TutorialMod(object):

    @Mod.InitServer()
    def server_init(self):
        serverApi.RegisterSystem(
            "TutorialMod",
            "TutorialServerSystem",
            "tutorialScripts.tutorialServerSystem.TutorialServerSystem"
        )

    @Mod.InitClient()
    def client_init(self):
        clientApi.RegisterSystem(
            "TutorialMod",
            "TutorialClientSystem",
            "tutorialScripts.tutorialClientSystem.TutorialClientSystem"
        )

    @Mod.DestroyServer()
    def server_destroy(self):
        pass

    @Mod.DestroyClient()
    def client_destroy(self):
        pass
```

`@Mod.Binding`把这个类声明为模组入口；`@Mod.InitServer()`和`@Mod.InitClient()`分别在服务端与客户端启动时调用；销毁函数用于退出时保存数据、取消监听或恢复状态。

## 监听方块使用事件

打开服务端系统文件，在初始化时监听`ServerBlockUseEvent`。官方资料说明`ListenForEvent`会把回调函数注册到事件上，事件发生时会把一个字典参数传给回调。

```python title="tutorialScripts/tutorialServerSystem.py"
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

class TutorialServerSystem(ServerSystem):

    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)
        self.ListenEvent()

    def ListenEvent(self):
        self.ListenForEvent(
            serverApi.GetEngineNamespace(),
            serverApi.GetEngineSystemName(),
            "ServerBlockUseEvent",
            self,
            self.OnServerBlockUseEvent
        )

    def OnServerBlockUseEvent(self, args):
        if args["blockName"] == "sdkteam_test:block1":
            comp = serverApi.CreateComponent(
                serverApi.GetLevelId(),
                "Minecraft",
                "item"
            )
            comp.SpawnItemToPlayerInv(
                {"itemName": "minecraft:diamond_sword", "count": 1, "auxValue": 0},
                args["playerId"]
            )
```

把`sdkteam_test:block1`换成你自己的自定义方块赋命名空间标识符。`args["playerId"]`表示触发交互的玩家；`CreateComponent(...,"item")`创建物品组件；`SpawnItemToPlayerInv`把物品放进玩家背包。

/// warning | 注意事件触发频率
官方入门资料特别提醒，`ServerBlockUseEvent`可能每刻触发。如果玩家按住右键，逻辑会连续执行。真实玩法中要加冷却、状态判断或只在需要的时机给予物品。
///

## 测试和排错

1. 保存脚本。
2. 回到MC Studio或编辑器观察脚本测试日志，确认是否发生热更新。
3. 进入测试存档，右击目标方块。
4. 如果没有效果，检查方块标识符、事件名、脚本目录名、`modMain.py`中的类路径和`__init__.py`文件。

如果你新增了文件或类，热更新不一定完整生效。此时保存退出到菜单界面，再重新进入测试存档。
