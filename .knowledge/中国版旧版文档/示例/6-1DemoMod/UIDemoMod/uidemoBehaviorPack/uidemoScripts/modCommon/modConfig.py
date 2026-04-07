# -*- coding: utf-8 -*-
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# Mod Version
ModName = "HugoUIDemoMod"
ModVersion = "0.0.1"

# Server System
ServerSystemName = "UIDemoServerSystem"
ServerSystemClsPath = "uidemoScripts.modServer.serverSystem.uidemoServerSystem.UIDemoServerSystem"

# Client System
ClientSystemName = "UIDemoClientSystem"
ClientSystemClsPath = "uidemoScripts.modClient.clientSystem.uidemoClientSystem.UIDemoClientSystem"

# Engine
Minecraft = "Minecraft"

# Server Component
## Engine
EngineTypeComponent = "engineType"
ScriptTypeCompServer = "type"
PosComponent = "pos"
RotComponent = "rot"
ModelCompServer = "model"

# Client Component
## Engine
CameraComponent = "camera"
ModelCompClient = "model"
AudioComponent = "customAudio"
ScriptTypeCompClient = "type"
PathComponent = "path"
FrameAniBindComponent = "frameAniEntityBind"
FrameAniTransComponent = "frameAniTrans"
FrameAniCtrlComponent = "frameAniControl"
ParticleTransComponent = "particleTrans"
ParticleControlComponent = "particleControl"
ParticleBindComponent = "particleEntityBind"
## Custom

# Server Event
## Engine
ServerChatEvent = "ServerChatEvent"
ScriptTickServerEvent = "OnScriptTickServer"
AddServerPlayerEvent = "AddServerPlayerEvent"
ProjectileDoHitEffectEvent = "ProjectileDoHitEffectEvent"
##Custom
# Client Event
## Engine
UiInitFinishedEvent = "UiInitFinished"
ScriptTickClientEvent = "OnScriptTickClient"
## Custom


# UI
UIDemoUIName = "UIDemo"
UIDemoUIPyClsPath = "uidemoScripts.modClient.ui.UIDemoScreen.UIDemoScreen"
UIDemoUIScreenDef = "UIDemo.main"

MainScreenUIName = "MainScreen"
MainScreenPyClsPath = "uidemoScripts.modClient.ui.MainScreen.MainScreen"
MainScreenScreenDef = "MainScreen.main"

PushScreenDemoUIName = "PushScreenDemo"
PushScreenPyClsPath = "uidemoScripts.modClient.ui.PushScreenDemo.PushScreenDemo"
PushScreenScreenDef = "PushScreenDemo.main"

# Client param

# Server param