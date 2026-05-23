# UI与交互接口<!-- md:flag china -->

本页列出中国版模组SDK中与自定义UI创建管理、原生HUD控制、按键控制、音效及游戏设置相关的客户端接口。所有接口均仅在客户端可用，服务端若需触发UI操作，需通过事件通知机制（`NotifyToClient`）向客户端发送消息后由客户端执行。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK客户端体系，与国际版`@minecraft/server`或`@minecraft/server-ui`脚本API无关。中国版自定义UI使用JSON UI格式（`.json`定义文件），与原版UI文件格式共用但命名空间不同。
///

## 自定义UI创建与管理

自定义UI全部通过`mod.client.extraClientApi`的直接方法创建，无需通过组件工厂。UI类需继承`ScreenNode`基类，并在模组初始化时通过`RegisterUI`注册。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `RegisterUI(nameSpace,uiKey,cls,uiScreenDef)` | 客户端 | `nameSpace:str`、`uiKey:str`、`cls:class`（继承ScreenNode的UI类）、`uiScreenDef:str`（UI定义文件路径，格式为`命名空间.文件名`） | 无 | 注册UI类与其对应的JSON UI定义。必须在模组加载初始化时调用，通常在`ClientSystem.__init__`中执行。 |
| `CreateUI(nameSpace,uiKey,createParams)` | 客户端 | `nameSpace:str`、`uiKey:str`（须与注册时相同且全局唯一）、`createParams:dict` | `ScreenNode` | 创建并显示UI实例。`createParams`支持以下键：`isHud`（`int`，0=普通界面，1=HUD界面）、`bindEntityId`（`str`，绑定实体ID，绑定后UI悬浮在实体头顶）、`bindOffset`（`tuple`，偏移量，默认`(0,1,0)`）、`autoScale`（`int`，绑定实体时是否随距离缩放，默认1）、`bindWorldPosition`（`(int,(float,float,float))`，绑定到世界坐标）。注意同一`uiKey`不能创建两次。 |
| `GetUI(nameSpace,uiKey)` | 客户端 | `nameSpace:str`、`uiKey:str` | `ScreenNode`或`None` | 获取已创建的UI实例。 |
| `DestroyUI(nameSpace,uiKey)` | 客户端 | `nameSpace:str`、`uiKey:str` | 无 | 销毁并移除指定UI实例。 |
| `PopScreen()` | 客户端 | 无 | 无 | 关闭当前最顶层显示的UI屏幕，类似按下返回键。 |
| `CheckCanBindUI(entityId)` | 客户端 | `entityId:str` | `bool` | 检查实体是否可以绑定头顶UI；实体刚创建时可能需等待1–3帧后再绑定。 |

```python
import mod.client.extraClientApi as clientApi

class MyClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super().__init__(namespace, systemName)
        # 注册UI
        clientApi.RegisterUI("myMod", "hud_ui", MyHudScreen, "myMod.hud_ui")

    def ShowHud(self):
        ui = clientApi.CreateUI("myMod", "hud_ui", {"isHud": 1})
        return ui

    def ShowEntityLabel(self, entityId):
        if clientApi.CheckCanBindUI(entityId):
            clientApi.CreateUI("myMod", "label_" + entityId, MyLabelScreen, {
                "bindEntityId": entityId,
                "bindOffset": (0, 2, 0),
                "autoScale": 1
            })
```

## 原生HUD控制

原生UI控制接口均为`mod.client.extraClientApi`的直接方法，全部为客户端接口，可控制原版HUD各元素的显示与隐藏。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `HideHudGUI(hide)` | 客户端 | `hide:bool` | 无 | 整体隐藏/显示游戏HUD（等同F1键效果），点击区域仍可响应操作。 |
| `HideHealthGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示HUD血量界面。 |
| `HideHungerGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示HUD饥饿值界面。 |
| `HideArmorGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示HUD护甲值界面。 |
| `HideExpGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示非创造模式下的经验条。 |
| `HideAirSupplyGUI(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示玩家氧气值界面。 |
| `HideSlotBarGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示底部物品栏（快捷栏）。 |
| `HideCrossHairGUI(hide)` | 客户端 | `hide:bool` | 无 | 隐藏/显示十字准心。 |
| `HideMoveGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏游戏中移动摇杆按钮，隐藏后点击原位置不再响应。 |
| `HideJumpGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏跳跃按钮，隐藏后点击原位置不再响应。 |
| `HideSneakGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏潜行按钮，隐藏后点击原位置不再响应。 |
| `HideInteractGui(hide)` | 客户端 | `hide:bool` | 无 | 隐藏交互按钮（如喂食、交易等场景中的按钮），隐藏后不响应。 |
| `HideChatGUI(hide)` | 客户端 | `hide:bool` | 无 | 隐藏聊天按钮（新版聊天模式下不生效）。 |
| `HidePauseGUI(hide)` | 客户端 | `hide:bool` | 无 | 隐藏暂停按钮。 |
| `OpenInventoryGui()` | 客户端 | 无 | 无 | 打开原版背包界面。 |
| `OpenChatGui()` | 客户端 | 无 | 无 | 打开原版聊天栏。 |
| `GetScreenSize()` | 客户端 | 无 | `tuple(int,int)` | 获取游戏当前分辨率`(宽,高)`，单位像素。 |
| `GetScreenViewInfo()` | 客户端 | 无 | `tuple(float,float,float,float)` | 获取当前游戏视角信息（视角宽、高及偏移），用于UI精确适配计算。 |
| `SetResponse(uiName,enable)` | 客户端 | `uiName:str`、`enable:bool` | 无 | 设置指定原生UI是否响应触摸/点击操作。 |
| `ChangeSneakState()` | 客户端 | 无 | 无 | 切换玩家潜行状态（等同按下潜行键）。 |
| `SimulateJump()` | 客户端 | 无 | 无 | 模拟玩家跳跃操作。 |
| `PlayHudHeartBlinkAnim()` | 客户端 | 无 | 无 | 播放原版受伤时血量变化的动效（心跳动画）。 |

## 音效

音效接口通过`GetEngineCompFactory().CreateCustomAudio(levelId)`获取`AudioCustomComponentClient`，仅客户端可用。音效资源文件需位于资源包的`sounds/`目录下，并在`sound_definitions.json`中注册。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `DisableOriginMusic(disable)` | 客户端 | `disable:bool` | `bool` | 禁用/启用原版背景音乐；为`True`时停止播放原版BGM，通常在自定义音乐播放前调用。 |
| `PlayCustomMusic(name,pos,volume,pitch,loop,entityId)` | 客户端 | `name:str`（音效标识符）、`pos:tuple(float,float,float)`（播放位置）、`volume:float`（音量，默认1.0）、`pitch:float`（音调，默认1.0）、`loop:bool`（是否循环）、`entityId:str`或`None`（跟随实体） | `bool` | 在世界中的指定位置或绑定实体处播放音效，距离远则音量衰减。 |
| `PlayCustomUIMusic(name,volume,pitch,loop)` | 客户端 | `name:str`、`volume:float`、`pitch:float`、`loop:bool` | `bool` | 播放UI音效（全局等音量，不受位置影响），适合按钮音效、背景音乐等。 |
| `PlayGlobalCustomMusic(name,volume,pitch,loop)` | 客户端 | `name:str`、`volume:float`、`pitch:float`、`loop:bool` | `bool` | 播放全局广播音效，所有客户端玩家均可听到（需服务端分别向各客户端发送事件）。 |
| `StopCustomMusic(name,fadeOutTime)` | 客户端 | `name:str`、`fadeOutTime:float`（淡出时间，秒） | `bool` | 停止指定音效播放，支持淡出效果。 |
| `StopCustomMusicById(musicId,fadeOutTime)` | 客户端 | `musicId:int`、`fadeOutTime:float` | `bool` | 通过播放返回的音效ID停止指定音效实例。 |
| `SetCustomMusicLoop(name,loop)` | 客户端 | `name:str`、`loop:bool` | `bool` | 更改正在播放的音效的循环状态。 |
| `SetCustomMusicLoopById(musicId,loop)` | 客户端 | `musicId:int`、`loop:bool` | `bool` | 通过音效ID更改指定音效实例的循环状态。 |

```python
import mod.client.extraClientApi as clientApi

levelId = clientApi.GetLevelId()
audioComp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)

# 禁用原版背景音乐并播放自定义BGM
audioComp.DisableOriginMusic(True)
audioComp.PlayCustomUIMusic("mymod:custom_bgm", 0.8, 1.0, True)

# 在某位置播放3D音效
audioComp.PlayCustomMusic("mymod:explosion", (10, 64, 10), 1.0, 1.0, False, None)
```

## 按键控制

按键控制接口通过`mod.client.extraClientApi`直接调用（`接口\控制.md`中的接口），仅客户端可用，用于监听和模拟玩家按键操作。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetKeyState(key)` | 客户端 | `key:int`（键码枚举） | `bool` | 获取指定按键的当前按下状态；`True`表示正在按住。 |
| `SetOperationType(opType)` | 客户端 | `opType:int`（操作类型枚举）| `bool` | 切换玩家操作类型（如从触屏模式切换到键鼠模式）。 |
| `GetCurrentInputMode()` | 客户端 | 无 | `int` | 获取当前输入模式枚举值（触屏/键鼠/手柄等）。 |

## 游戏设置

游戏设置接口通过`mod.client.extraClientApi`直接调用（`接口\游戏设置.md`中的接口），仅客户端可用。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetPlatform()` | 客户端 | 无 | `int` | 获取当前设备平台类型枚举值（安卓/iOS/PC等），用于针对不同平台做差异化处理。 |
| `GetDeviceType()` | 客户端 | 无 | `int` | 获取设备类型（手机/平板/PC）。 |
| `GetEngineVersion()` | 客户端 | 无 | `str` | 获取当前客户端引擎版本字符串。 |
| `SetRenderDistance(distance)` | 客户端 | `distance:int`（区块数） | `bool` | 设置客户端渲染距离（区块单位）。 |
| `GetRenderDistance()` | 客户端 | 无 | `int` | 获取当前客户端渲染距离。 |

/// note | 客户端游戏设置作用域
`SetRenderDistance`等接口只修改客户端本地设置，不影响服务端的模拟范围。渲染距离的调整只影响当前客户端的图像渲染，服务端区块加载仍遵循服务端配置。
///
