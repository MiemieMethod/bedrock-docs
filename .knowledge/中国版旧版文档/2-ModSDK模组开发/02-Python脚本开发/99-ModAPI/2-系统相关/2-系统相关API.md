---
sidebarDepth: 1
---

# <span id="系统System相关API"></span>系统System相关API

<span id="平台"></span>
## 平台

<span id="GetPlatform"></span>
### GetPlatform

- 描述

    获取脚本运行的平台

- 参数

    无

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 0：Window；1：IOS；2：Android；-1：其他 |

<span id="事件"></span>
## 事件

<span id="BroadcastEvent"></span>
### BroadcastEvent

- 描述

    本地广播事件，客户端system广播的事件仅客户端system能监听，服务器同理。

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def BroadCastEventTest(self, args):
                self.BroadcastEvent("bulletShootEvent", args)
```

<span id="BroadcastToAllClient"></span>
### BroadcastToAllClient

- 描述

    服务器广播事件到所有客户端，该接口仅服务器system有效。

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def BroadCastEventTest(self, args):
                self.BroadcastToAllClient("bulletShootEvent", args)

```

<span id="CreateEventData"></span>
### CreateEventData

- 描述

    创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple

- 参数

    无

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 事件数据 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def shoot(self):
                shootData = self.CreateEventData()
                shootData["id"] = self.mPlayerId
                # 向客户端发送事件，传递了一个playerId
                self.NotifyToClient('-12345678910','BulletHit', shootData)
```

<span id="DefineEvent"></span>
### DefineEvent

- 描述

    定义自定义事件

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def DefineEventTest(self):
                self.DefineEvent('BulletHit')
```

<span id="ListenForEvent"></span>
### ListenForEvent

- 描述

    注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace()和GetEngineSystemName()。具体每个事件的详细事件data可以参考[服务端事件](../3-事件/2-服务端事件.md#服务端事件)和[客户端事件](../3-事件/3-客户端事件.md#客户端事件)

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 所监听事件的来源系统的namespace |
    | systemName | str | 所监听事件的来源系统的systemName |
    | eventName | str | 事件名 |
    | instance | any | 回调函数所属的类的实例 |
    | func | function | 回调函数 |
    | priority | int | 这个回调函数的优先级。默认值为0，这个数值越大表示被执行的优先级越高，最高为10。 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def ListenEvent(self):
                # 服务端脚本自定义了1个事件
                self.DefineEvent('BulletHit')
                # 服务器端脚本监听了引擎的1个事件'ServerChatEvent'
                self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
```

<span id="NotifyToClient"></span>
### NotifyToClient

- 描述

    服务器发送事件到指定客户端，该接口仅服务器system有效。

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 客户端对应的Id，一般就是玩家Id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def NotifyToClientTest(self, args):
                self.NotifyToClient('-1234567890',"bulletShootEvent", args)
```

<span id="NotifyToServer"></span>
### NotifyToServer

- 描述

    客户端发送事件到服务器，该接口仅客户端system有效。

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
        def NotifyToServerTest(self, args):
                self.NotifyToServer("bulletShootEvent", args)
```

<span id="UnDefineEvent"></span>
### UnDefineEvent

- 描述

    取消自定义事件

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def UnDefineEventTest(self):
                self.UnDefineEvent('BulletHit')
```

<span id="UnListenAllEvents"></span>
### UnListenAllEvents

- 描述

    反注册监听某个系统抛出的所有事件，即不再监听。

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def ListenEvent(self):
                # 服务端脚本自定义了1个事件
                self.DefineEvent('BulletHit')
                # 服务器端脚本监听了引擎的1个事件'ServerChatEvent'
                # 具体每个事件的详细事件data可以参考《MODSDK文档》
                self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
        def UnListenEvent(self):
                # 取消自定义的事件
                self.UnDefineEvent('BulletHit')
                # 取消监听的系统事件
                self.UnListenAllEvents()
```

<span id="UnListenForEvent"></span>
### UnListenForEvent

- 描述

    反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为GetEngineNamespace()和GetEngineSystemName()。与ListenForEvent对应。具体每个事件的详细事件data可以参考[服务端事件](../3-事件/2-服务端事件.md#服务端事件)和[客户端事件](../3-事件/3-客户端事件.md#客户端事件)

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 所监听事件的来源系统的namespace |
    | systemName | str | 所监听事件的来源系统的systemName |
    | eventName | str | 事件名 |
    | instance | any | 回调函数所属的类的实例 |
    | func | function | 回调函数 |
    | priority | int | 这个回调函数的优先级。默认值为0，这个数值越大表示被执行的优先级越高。 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
        def ListenEvent(self):
                # 服务端脚本自定义了1个事件
                self.DefineEvent('BulletHit')
                # 服务器端脚本监听了引擎的1个事件'ServerChatEvent'
                self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
        def UnListenEvent(self):
                # 取消自定义的事件
                self.UnDefineEvent('BulletHit')
                # 取消监听的系统事件
                self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
```

<span id="实体"></span>
## 实体

<span id="CreateEngineEntityByTypeStr"></span>
### CreateEngineEntityByTypeStr

- 描述

    **服务端系统接口**，利用字符串创建引擎实体，主要用于微软自定义物体，具体参见创建实体部分内容

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | engineTypeStr | str | 例如'minecraft:husk' |
    | pos | tuple(float,float,float) | 生成坐标 |
    | rot | tuple(float,float) | 生物面向 |
    | dimensionId | int | 生成的维度，默认值为0（0为主世界，1为地狱，2为末地） |
    | isNpc | bool | 是否为npc，默认值为False。npc不会移动、转向、存盘。 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str或None | 实体Id或者None |

- 备注
    - 生成村民请使用"minecraft:villager_v2"

<span id="CreateEngineItemEntity"></span>
### CreateEngineItemEntity

- 描述

    **服务端系统接口**，用于创建物品实体，功能与item组件的SpawnItemToLevel接口作用类似，该接口返回物品的entityId，具体参见item组件

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | [物品信息字典](../0-名词解释.html#物品信息字典) |
    | dimensionId | int | 设置dimension，默认为主世界 |
    | pos | tuple(float,float,float) | 生成坐标 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str或None | 实体Id或者None |

- 示例

```python
import mod.server.extraServerApi as serverApi
itemDict = {
        'itemName': 'minecraft:bow',
        'count': 1,
        'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
        'auxValue': 0,
        'customTips':'§c new item §r',
        'extraId': 'abc',
        'userData': { 'color': { '__type__':8, '__value__':'gray'} },
}
itemEntityId = self.CreateEngineItemEntity(itemDict, 0, (0, 5, 0))
```

<span id="DestroyEntity"></span>
### DestroyEntity

- 描述

    实体销毁接口

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 销毁的实体ID |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |

<span id="特效"></span>
## 特效

<span id="CreateEngineEffect"></span>
### CreateEngineEffect

- 描述

    **客户端系统接口**，用于创建模型挂接特效，具体参见创建特效部分内容。

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，需要加上后缀名（一般是json） |
    | bindEntity | str | 绑定实体的Id |
    | aniName | str | 选择使用哪个模型动作的特效 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int或None | effectEntityId或者None |

<span id="CreateEngineParticle"></span>
### CreateEngineParticle

- 描述

    **客户端系统接口**，用于创建粒子特效，具体参见创建特效部分内容

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，需要加上后缀名（一般是json） |
    | pos | tuple(float,float,float) | 创建位置坐标 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int或None | particleEntityId或者None |

<span id="CreateEngineSfx"></span>
### CreateEngineSfx

- 描述

    **客户端系统接口**，用于创建序列帧特效，具体参见创建特效部分内容

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，不用后缀名 |
    | pos | tuple(float,float,float) | 创建位置，可选 |
    | rot | tuple(float,float) | 角度，可选 |
    | scale | float | 缩放系数，可选 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int或None | frameEntityId或者None |

<span id="CreateEngineSfxFromEditor"></span>
### CreateEngineSfxFromEditor

- 描述

    **客户端系统接口**，用于创建序列帧特效，具体参见创建特效部分内容

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，需要加上后缀名（一般是json） |
    | pos | tuple(float,float,float) | 创建位置，可选 |
    | rot | tuple(float,float) | 角度，可选 |
    | scale | float | 缩放系数，可选 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int或None | frameEntityId或者None |

<span id="组件"></span>
## 组件

<span id="CreateComponent"></span>
### CreateComponent

- 描述

    给实体创建组件

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# entityId 根据游戏实际Id获取，这里'-12345678910'只是随便写的
comp = serverApi.CreateComponent('-12345678910', "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，与GetComponent类似，如果已经创建会自动直接Get
```

<span id="DestroyComponent"></span>
### DestroyComponent

- 描述

    删除实体的组件

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
# entityId 根据游戏实际Id获取，这里'-12345678910'只是随便写的
comp = serverApi.DestroyComponent('-12345678910', "Minecraft", "item")
```

<span id="GetComponent"></span>
### GetComponent

- 描述

    获取实体的组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent

- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例或者None |

- 示例

```python
import mod.server.extraServerApi as serverApi
# entityId 根据游戏实际Id获取，这里'-12345678910'只是随便写的
comp = serverApi.GetComponent(‘-12345678910’, "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，如果没有创建过会返回None
```

