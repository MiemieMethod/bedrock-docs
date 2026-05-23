# 通用接口<!-- md:flag china -->

本页列出中国版模组SDK中与系统注册、组件框架、事件通信、定时器、工具函数、数学工具、本地设备及本地存储相关的基础接口。这些接口是所有中国版Python模组的核心基础设施，无论模组功能如何，均依赖这些接口完成注册、通信和工具调用。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK（`mod.server.extraServerApi`/`mod.client.extraClientApi`），不得与国际版`@minecraft/server`脚本API混用。两套体系在架构、语言和运行时环境上均不相同。
///

## 端与访问方式

中国版ModAPI的核心访问入口是服务端API模块与客户端API模块：

| 模块 | 导入方式 | 主要用途 |
| --- | --- | --- |
| 服务端API | `import mod.server.extraServerApi as serverApi` | 注册服务端系统、服务端组件操作、服务端工具函数 |
| 客户端API | `import mod.client.extraClientApi as clientApi` | 注册客户端系统、客户端组件操作、客户端工具函数 |

所有接口均以这两个模块作为调用入口，部分接口需进一步通过组件工厂获取组件实例后调用。

## 系统注册

**系统**（System）是模组逻辑的主要载体。每个模组通常在服务端和客户端各注册一个系统类。系统类继承自`ServerSystem`或`ClientSystem`基类，通过`RegisterSystem`注册后，引擎会在游戏初始化阶段自动实例化并调用生命周期回调（`__init__`、`Update`、`Destroy`等）。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetServerSystemCls()` | 服务端 | 无 | `class` | 获取`ServerSystem`基类，用于继承，在模组服务端入口文件中调用。 |
| `GetClientSystemCls()` | 客户端 | 无 | `class` | 获取`ClientSystem`基类，用于继承，在模组客户端入口文件中调用。 |
| `RegisterSystem(nameSpace,systemName,cls)` | 服务端、客户端 | `nameSpace:str`、`systemName:str`、`cls:class` | `None` | 注册系统。`nameSpace`为模组命名空间，`systemName`为系统名称，`cls`为继承基类的系统类。 |
| `GetSystem(nameSpace,systemName)` | 服务端、客户端 | `nameSpace:str`、`systemName:str` | 系统实例或`None` | 获取已注册系统的实例，常用于跨系统调用。 |
| `GetEngineNamespace()` | 服务端、客户端 | 无 | `str` | 获取引擎事件命名空间字符串，用于监听引擎内置事件。 |
| `GetEngineSystemName()` | 服务端、客户端 | 无 | `str` | 获取引擎事件系统名称字符串，用于监听引擎内置事件。 |

```python
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

class MyServerSystem(ServerSystem):
    def __init__(self, namespace, name):
        ServerSystem.__init__(self, namespace, name)
        self.ListenForEvent(
            serverApi.GetEngineNamespace(),
            serverApi.GetEngineSystemName(),
            "ServerChatEvent", self, self.OnChat
        )

    def OnChat(self, args):
        print("玩家说：", args.get("Message", ""))

    def Destroy(self):
        self.UnListenAllEvents()

def RegisterMyMod():
    serverApi.RegisterSystem("myMod", "myServerSystem", MyServerSystem)
```

## 组件框架

**组件**（Component）是附加在实体或世界（关卡）上的功能单元，分为引擎原生组件和自定义组件两类。引擎原生组件通过`GetEngineCompFactory()`工厂对应的`CreateXxx(entityId/levelId)`方法创建，自定义组件则需先注册类型再创建实例。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetEngineCompFactory()` | 服务端、客户端 | 无 | 引擎组件工厂实例 | 获取引擎原生组件工厂，然后通过`CreateXxx(entityId/levelId)`创建具体组件实例。 |
| `GetComponentCls()` | 服务端、客户端 | 无 | `class` | 获取自定义组件基类，用于继承以定义模组自定义组件。 |
| `RegisterComponent(nameSpace,compName,compCls)` | 服务端、客户端 | `nameSpace:str`、`compName:str`、`compCls:class` | `bool` | 注册自定义组件类型，通常在模组初始化阶段调用。 |
| `CreateComponent(entityId,nameSpace,compName)` | 服务端、客户端 | `entityId:str`、`nameSpace:str`、`compName:str` | 组件实例或`None` | 在指定实体上创建已注册的自定义组件实例。 |
| `GetComponent(entityId,nameSpace,compName)` | 服务端、客户端 | `entityId:str`、`nameSpace:str`、`compName:str` | 组件实例或`None` | 获取指定实体上已创建的自定义组件实例。 |
| `DestroyComponent(entityId,nameSpace,compName)` | 服务端、客户端 | `entityId:str`、`nameSpace:str`、`compName:str` | `bool` | 销毁指定实体上的自定义组件实例。 |
| `GetLevelId()` | 服务端、客户端 | 无 | `str` | 获取当前世界（关卡）ID，大多数组件工厂方法以此作为`levelId`参数。 |

引擎原生组件工厂的常用创建方法如下：

| 组件用途 | 创建方法 | 可用端 | 典型目标 |
| --- | --- | --- | --- |
| 实体特性 | `CreateAttr(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体位置 | `CreatePos(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体旋转 | `CreateRot(entityId)` | 服务端、客户端 | 实体、玩家 |
| 身体旋转 | `CreateBodyRot(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体缩放 | `CreateScale(entityId)` | 服务端 | 实体、玩家 |
| 引擎类型与标识 | `CreateEngineType(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体名称 | `CreateName(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体事件与组件组 | `CreateEntityEvent(entityId)` | 服务端 | 实体、玩家 |
| 实体运动器 | `CreateActorMotion(entityId)` | 服务端、客户端 | 实体 |
| 实体状态效果 | `CreateEffect(entityId)` | 服务端、客户端 | 实体、玩家 |
| 物品操作 | `CreateItem(entityId)` | 服务端、客户端 | 实体、玩家 |
| 实体维度传送 | `CreateDimension(entityId/levelId)` | 服务端 | 实体、玩家 |
| 玩家经验 | `CreateExp(playerId)` | 服务端 | 玩家 |
| 玩家等级 | `CreateLv(playerId)` | 服务端 | 玩家 |
| 玩家特有操作 | `CreatePlayer(playerId)` | 服务端、客户端 | 玩家 |
| 游戏规则与定时器 | `CreateGame(levelId)` | 服务端、客户端 | 世界 |
| 指令执行 | `CreateCommand(levelId)` | 服务端 | 世界 |
| 天气控制 | `CreateWeather(levelId)` | 服务端 | 世界 |
| 时间控制 | `CreateTime(levelId)` | 服务端、客户端 | 世界 |
| 方块状态 | `CreateBlockState(levelId)` | 服务端 | 世界 |
| 方块信息读写 | `CreateBlockInfo(levelId)` | 服务端、客户端 | 世界 |
| 自定义音效 | `CreateCustomAudio(levelId)` | 客户端 | 世界 |
| 本地配置存储 | `CreateConfig(entityId)` | 客户端 | 玩家 |
| 摄像机 | `CreateCamera(levelId)` | 服务端、客户端 | 世界、玩家 |
| 记分板 | `CreateGame(levelId)` | 服务端、客户端 | 世界（记分板相关接口也挂在Game组件上） |

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
# 使用gameComp进行游戏规则、定时器、记分板等操作
```

## 事件通信

事件通信接口是`ServerSystem`和`ClientSystem`实例的方法，用于系统间通信及客户端与服务端之间的数据传递。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `ListenForEvent(nameSpace,systemName,eventName,instance,func)` | 服务端、客户端 | `nameSpace:str`、`systemName:str`、`eventName:str`、`instance:object`、`func:function` | 无 | 监听事件。引擎内置事件使用`GetEngineNamespace()`和`GetEngineSystemName()`指定来源。 |
| `UnListenForEvent(nameSpace,systemName,eventName,instance,func)` | 服务端、客户端 | 同上 | 无 | 取消监听指定事件。 |
| `UnListenAllEvents()` | 服务端、客户端 | 无 | 无 | 取消当前系统实例的全部事件监听，建议在`Destroy`中调用。 |
| `BroadcastEvent(eventName,eventData)` | 服务端 | `eventName:str`、`eventData:dict` | 无 | 在服务端系统间广播事件，所有服务端系统中监听该事件的回调均会收到。 |
| `BroadcastToAllClient(eventName,eventData)` | 服务端 | `eventName:str`、`eventData:dict` | 无 | 向所有在线玩家的客户端广播事件。 |
| `NotifyToClient(playerId,eventName,eventData)` | 服务端 | `playerId:str`、`eventName:str`、`eventData:dict` | 无 | 向指定玩家的客户端发送事件。 |
| `NotifyToMultiClients(playerIds,eventName,eventData)` | 服务端 | `playerIds:list(str)`、`eventName:str`、`eventData:dict` | 无 | 向多个指定玩家的客户端发送事件。 |
| `NotifyToServer(eventName,eventData)` | 客户端 | `eventName:str`、`eventData:dict` | 无 | 从客户端向服务端发送事件。 |
| `CreateEventData(eventName)` | 服务端、客户端 | `eventName:str` | `dict` | 创建指定事件的空数据字典，填充字段后再广播或发送。 |

```python
# 服务端系统接收攻击事件后通知客户端
class MyServerSystem(ServerSystem):
    def __init__(self, namespace, name):
        ServerSystem.__init__(self, namespace, name)
        ns = serverApi.GetEngineNamespace()
        sn = serverApi.GetEngineSystemName()
        self.ListenForEvent(ns, sn, "PlayerAttackEntityEvent", self, self.OnAttack)
        self.ListenForEvent("myMod", "myClientSystem", "myMod:AskHealth", self, self.OnAskHealth)

    def OnAttack(self, args):
        playerId = args["playerId"]
        self.NotifyToClient(playerId, "myMod:HitFeedback", {"victimId": args["victimId"]})

    def OnAskHealth(self, args):
        pass  # 处理来自客户端的请求
```

## 定时器

定时器接口通过`GetEngineCompFactory().CreateGame(levelId)`获取的`GameComponent`实例调用。服务端定时器在服务端刻中触发，客户端定时器在客户端帧中触发。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddTimer(delay,func,*args,**kwargs)` | 服务端、客户端 | `delay:float`、`func:function`、`*args`、`**kwargs` | `CallLater`或`None` | 添加单次定时器，`delay`单位为秒，到期后执行一次。`func`非函数时返回`None`。 |
| `AddRepeatedTimer(delay,func,*args,**kwargs)` | 服务端、客户端 | `delay:float`、`func:function`、`*args`、`**kwargs` | `CallLater`或`None` | 添加重复定时器，以`delay`秒为间隔持续循环执行。 |
| `CancelTimer(timer)` | 服务端、客户端 | `timer:CallLater` | 无 | 取消一个定时器，之后不再触发。 |

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)

def onRepeated():
    print("每5秒触发一次")

timer = gameComp.AddRepeatedTimer(5.0, onRepeated)
# 需要取消时：gameComp.CancelTimer(timer)

# 单次延迟任务
gameComp.AddTimer(2.0, lambda: print("2秒后执行一次"))
```

## 工具函数

以下接口为`extraServerApi`或`extraClientApi`的直接方法。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetMinecraftEnum()` | 服务端、客户端 | 无 | 枚举表对象 | 获取引擎枚举表，包含`AttrType`、`GameType`、`ItemPosType`等所有枚举类型。 |
| `GetModConfigJson(path)` | 服务端、客户端 | `path:str` | `dict`或`None` | 读取模组资源包中的JSON配置文件，`path`相对于模组资源根目录（不含资源包名称）。 |
| `GetLocalPlayerId()` | 客户端 | 无 | `str` | 获取本地玩家的实体ID，仅在客户端可用。 |
| `GetFps()` | 客户端 | 无 | `int` | 获取当前客户端帧率。 |
| `GetHostPlayerId()` | 服务端 | 无 | `str`或`None` | 获取本地游戏房主玩家的实体ID；Apollo网络服环境下返回`None`。 |
| `GetServerTickTime()` | 服务端 | 无 | `int` | 获取当前服务端累计游戏刻数。 |
| `ImportModule(modName,libFolder)` | 服务端、客户端 | `modName:str`、`libFolder:str` | `module` | 从行为包内指定的库文件夹导入Python模块，绕过普通`import`的路径限制。 |
| `StartCoroutine(generator)` | 服务端、客户端 | `generator:generator` | 协程任务对象 | 启动一个Python生成器协程，每刻推进一次。 |
| `StopCoroutine(task)` | 服务端、客户端 | `task` | 无 | 停止一个正在运行的协程。 |
| `CheckNameValid(name)` | 服务端 | `name:str` | `bool` | 检查玩家名是否只包含合法字符集。 |
| `CheckWordsValid(words,callback)` | 服务端、客户端 | `words:str`、`callback:function` | 无 | 异步检查词语是否通过内容审核，回调参数为`(result:bool, words:str)`。 |
| `GetChinese(s)` | 服务端、客户端 | `s:str` | `str` | 将非标准编码的中文字符串转换为标准中文字符串。 |
| `IsMultiPlayer()` | 服务端、客户端 | 无 | `bool` | 获取当前是否为多人游戏。 |
| `IsSinglePlayer()` | 服务端、客户端 | 无 | `bool` | 获取当前是否为单人游戏。 |
| `GenerateColor(colorName)` | 服务端、客户端 | `colorName:str` | `str` | 根据颜色名称（如`"RED"`、`"GREEN"`）返回Minecraft格式化颜色代码。 |

## 数学工具

数学工具为`extraServerApi`/`extraClientApi`的直接方法，用于方向向量与旋转角度的互相转换及坐标变换。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetDirFromRot(rot)` | 服务端、客户端 | `rot:tuple(float,float)` | `tuple(float,float,float)` | 将`(俯仰角, 偏航角)`旋转元组（度数）转换为归一化方向向量。 |
| `GetRotFromDir(dir)` | 服务端、客户端 | `dir:tuple(float,float,float)` | `tuple(float,float)` | 将方向单位向量转换为`(俯仰角, 偏航角)`旋转元组（度数）。 |
| `GetIntPos(pos)` | 服务端、客户端 | `pos:tuple(float,float,float)` | `tuple(int,int,int)` | 将浮点坐标各分量向下取整，返回所在方块的整数坐标。 |
| `GetLocalPosFromWorld(pos,entityId)` | 服务端、客户端 | `pos:tuple(float,float,float)`、`entityId:str` | `tuple(float,float,float)` | 将世界坐标转换为相对于指定实体的局部坐标，可能存在浮点精度偏差。 |
| `GetWorldPosFromLocal(pos,entityId)` | 服务端、客户端 | `pos:tuple(float,float,float)`、`entityId:str` | `tuple(float,float,float)` | 将相对于指定实体的局部坐标转换为世界坐标，可能存在浮点精度偏差。 |

```python
import mod.server.extraServerApi as serverApi

comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
rot = comp.GetRot()
direction = serverApi.GetDirFromRot(rot)
# direction 为实体当前朝向的单位向量 (x, y, z)

blockPos = serverApi.GetIntPos(someFloatPos)
```

## 本地设备

以下接口用于获取客户端或服务端设备相关信息，均为`extraServerApi`/`extraClientApi`的直接方法。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetEngineVersion()` | 客户端 | 无 | `tuple(int,int,int)` | 获取引擎版本号，格式为`(主版本, 次版本, 修订版本)`。 |
| `GetMinecraftVersion()` | 服务端、客户端 | 无 | `str` | 获取Minecraft游戏版本字符串，如`"1.20.10.01"`。 |
| `GetPlatform()` | 客户端 | 无 | `int` | 获取当前运行平台枚举值，对应`MinecraftEnum.GamePlatform`。 |
| `IsInApollo()` | 服务端 | 无 | `bool` | 判断当前是否运行在Apollo网络服环境中。 |
| `IsInServer()` | 客户端 | 无 | `bool` | 判断客户端当前是否处于连接服务器状态（非本地单人存档）。 |
| `GetIP()` | 服务端 | 无 | `tuple(str,int)` | 获取服务器IP地址和端口号，格式为`(IP字符串, 端口号)`。 |

## 本地存储

本地存储接口仅在客户端可用，通过`GetEngineCompFactory().CreateConfig(entityId)`（`entityId`传入本地玩家ID）获取`ConfigCompClient`实例后调用。配置数据持久化存储在本地设备，适合保存玩家个人偏好设置，不依赖服务器。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetConfigData(name)` | 客户端 | `name:str` | `object`或`None` | 读取以`name`为键的本地持久化配置数据，若不存在则返回`None`。 |
| `SetConfigData(name,value)` | 客户端 | `name:str`、`value:object` | `bool` | 以`name`为键存储本地持久化配置数据，支持基本Python数据类型。 |

```python
import mod.client.extraClientApi as clientApi

localPlayerId = clientApi.GetLocalPlayerId()
configComp = clientApi.GetEngineCompFactory().CreateConfig(localPlayerId)

# 存储设置
configComp.SetConfigData("myMod:ui:scale", 1.5)

# 读取设置，提供默认值
scale = configComp.GetConfigData("myMod:ui:scale") or 1.0
```
