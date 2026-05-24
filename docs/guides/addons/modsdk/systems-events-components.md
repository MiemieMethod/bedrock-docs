# 系统、事件与组件<!-- md:flag china -->

模组SDK脚本开发可以先用一句话概括：在系统里监听事件，在回调里调用组件。系统是代码的组织和运行单位；事件告诉你“发生了什么”；组件提供“读写游戏数据或执行功能”的接口。

## 系统

系统需要继承引擎提供的基类。服务端系统从`mod.server.extraServerApi.GetServerSystemCls()`取得基类，客户端系统从`mod.client.extraClientApi.GetClientSystemCls()`取得基类。

```python title="tutorialScripts/tutorialServerSystem.py"
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

class TutorialServerSystem(ServerSystem):

    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)
```

系统注册发生在`modMain.py`中。`RegisterSystem`会把系统注册到引擎，引擎随后创建系统实例，并在退出时回收。

```python title="tutorialScripts/modMain.py"
@Mod.InitServer()
def server_init(self):
    serverApi.RegisterSystem(
        "TutorialMod",
        "TutorialServerSystem",
        "tutorialScripts.tutorialServerSystem.TutorialServerSystem"
    )
```

命名空间建议使用模组名；系统名称建议足够独特，避免和其他模组冲突。

## 事件

事件依赖系统。监听事件就是把回调函数注册到某个事件上；事件发生时，引擎调用回调，并传入一个参数字典。官方资料强调：回调函数必须接收一个参数，且不要往引擎事件的回调参数字典里直接添加自定义键；需要额外数据时应复制出新的字典。

```python
def ListenEvent(self):
    self.ListenForEvent(
        serverApi.GetEngineNamespace(),
        serverApi.GetEngineSystemName(),
        "ServerChatEvent",
        self,
        self.OnServerChat
    )

def OnServerChat(self, args):
    player_id = args["playerId"]
    message = args["message"]
```

不再需要监听时，应使用`UnListenForEvent`取消监听。官方故障排查资料提到，如果模组卸载后没有清理事件监听，内存中可能残留数据并影响下一次安装的模组。

## 组件

组件是引擎封装的数据和功能集合。官方资料把组件分为引擎组件和自定义组件：引擎组件的参数和功能由引擎定义，自定义组件则由开发者定义数据结构和更新逻辑。

常见流程是创建组件、调用组件方法、把结果用于你的玩法逻辑。例如物品组件可以向玩家背包生成物品：

```python
comp = serverApi.CreateComponent(serverApi.GetLevelId(), "Minecraft", "item")
comp.SpawnItemToPlayerInv(
    {"itemName": "minecraft:diamond_sword", "count": 1, "auxValue": 0},
    player_id
)
```

## 服务端和客户端分工

服务端系统和客户端系统不是为了把同一段代码拆成两份，而是为了把“真实规则”和“表现反馈”分开。服务端系统维护权威状态，适合写给物品、修改记分板、处理实体、保存数据、校验玩家操作等逻辑；客户端系统面向本地玩家体验，适合写界面、镜头、音效、粒子和输入反馈。

这种分工可以用一个简单规则记住：服务端决定发生什么，客户端决定如何展示。不要在客户端直接改写应由服务端决定的数据，也不要把界面和渲染细节放到服务端系统里。双端需要协作时，应使用自定义事件在系统之间传递必要的参数。

| 需求 | 建议位置 | 原因 |
| ---- | -------- | ---- |
| 玩家右击方块后获得物品 | 服务端系统 | 背包变化属于真实游戏状态，应由服务端决定。 |
| 播放一次本地粒子或打开自定义界面 | 客户端系统 | 这类效果主要影响玩家看到的表现。 |
| 服务端计算结果后通知客户端显示提示 | 服务端系统发送事件，客户端系统监听事件 | 规则和表现分离，参数通过事件传递。 |

/// tip | 一开始就养成清理习惯
在销毁函数里关闭定时器、取消事件监听、保存必要数据。小项目里看不出问题，大型模组或频繁热更时，残留监听会非常难查。
///