# -*- coding: utf-8 -*-
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# Mod Version
AwesomeModName = "AwesomeGame"
LobbyClientModName = "AwesomeBehavior"
LobbyServerModName = "AwesomeLobby"
MasterModName = "AwesomeMaster"
ModVersion = "0.0.1"

# Server System
FpsServerSystemName = "FpsServerSystem"
FpsServerSystemClsPath = "awesomeScripts.modServer.serverSystem.fpsServerSystem.FpsServerSystem"
LobbyServerSystemName = 'AwesomeLobby'
LobbyServerSystemClsPath = "awesomeScripts.awesomeServer.AwesomeServer"
MasterServerSystemClsPath = "awesomeScripts.awesomeMaster.AwesomeMaster"
ServiceServerSystemClsPath = "awesomeScripts.awesomeService.AwesomeService"

# Client System
FpsClientSystemName = "FpsClientSystem"
FpsClientSystemClsPath = "awesomeModScripts.modClient.clientSystem.fpsClientSystem.FpsClientSystem"

LobbyClientSystemClsPath = "awesomeScripts.awesomeClient.AwesomeClient"
LobbyClientSystemName = "AwesomeLobbyClient"

#From Service
ServiceSystemName = "AwesomeService"
#From Master
MasterSystemName = "AwesomeMaster"

# Engine
Minecraft = "Minecraft"

# Server Component
## Engine
EngineTypeComponent = "engineType"
ScriptTypeCompServer = "type"
PosComponent = "pos"
RotComponent = "rot"
BulletComponent = "bulletAttributes"
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
ClientShootComponent = "ClientShoot"
ClientShootCompClsPath = "awesomeModScripts.modClient.clientComponent.shootComponentClient.ShootComponentClient"

# Server Event
## Engine
ServerChatEvent = "ServerChatEvent"
ScriptTickServerEvent = "OnScriptTickServer"
AddServerPlayerEvent = "AddServerPlayerEvent"
ProjectileDoHitEffectEvent = "ProjectileDoHitEffectEvent"
EntityBeKnockEvent = "EntityBeKnockEvent"
##Custom
PlayShootAnimEvent = "PlayShootAnim"
BulletHitEvent = "BulletHit"
BulletFlyFrameEvent = "BulletFlyFrame"
# Client Event
## Engine
UiInitFinishedEvent = "UiInitFinished"
ScriptTickClientEvent = "OnScriptTickClient"
## Custom
ShootEvent = "Shoot"


# UI
FpsBattleUIName = "fpsBattle"
FpsBattleUIPyClsPath = "awesomeModScripts.modClient.ui.fpsBattle.FpsBattleScreen"
FpsBattleUIScreenDef = "fpsBattle.main"

# Client param
SightFieldOfView = -30
DatiangouModel = "datiangou"
DatiangouRunAnim = "run"
DatiangouFengxiAnim = "fengxi"
DatiangouFengxiAnimFrames = 35
BulletHitSound = "awesome.bullet_hit"
BulletHitEffect = "effects/burst.json"
BulletFlyFrameSfx = "textures/sfxs/snow_3"
ParticleControlFrames = 30

# Server param
BulletPower = 2
BulletGravity = 0.05

SyncUserDataEvent = "SyncUserDataEvent"
UiInitFinished = "UiInitFinished"

# UI
SureUIName = "Sure"
SureUIPyClsPath = "awesomeScripts.modUI.Sure.SureScreen"
SureUIScreenDef = "Sure.main"

#other
OnSureGameEvent = "OnSureGameEvent"
SureEnterGameEvent = "SureEnterGameEvent"
SureMatchGameEvent = "SureMatchGameEvent"
TipGameEvent = "TipGameEvent"
OnCancelGameEvent = "OnCancelGameEvent"
MatchResultTip = "MatchResultTip"

ServerPlayerBornPosEvent = "ServerPlayerBornPosEvent"
savePlayerDataEvent = "savePlayerDataEvent"
savePlayerDataOnShutDownEvent = "savePlayerDataOnShutDownEvent"
DelServerPlayerEvent = "DelServerPlayerEvent"
ServerWillShutDownEvent = "ServerWillShutDownEvent"
EntityBeKnockEvent = "EntityBeKnockEvent"
MatchResultEvent = "MatchResultEvent"
MatchNumEvent = "MatchNumEvent"
GetUserInfoRequestEvent = "GetUserInfoRequestEvent"
GetPlayerNumOfGameRequestEvent = "GetPlayerNumOfGameRequestEvent"
GetUserInfoResponseEvent = "GetUserInfoResponseEvent"
GetPlayerNumOfGameEvent = "GetPlayerNumOfGameEvent"
RequestMatchCancel = "RequestMatchCancel"
RequestMatchNum = "RequestMatchNum"
RequestMatch = "RequestMatch"
RequestLobby = "RequestLobby"
UpdateServerStatusEvent = "UpdateServerStatusEvent"
#ModuleName
AwesomeMatch = "awesome_match"

#TipType
class TipType(object):
	matching = 0
	levelNotEnough = 1
	toTransfer = 2