# -*- coding: utf-8 -*-

# import server.extraServerApi as serverApi
#
# ENTITY_TYPE = serverApi.GetMinecraftEnum().EntityType
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# Mod Version
ModName = "QuestMod"
ModVersion = "0.0.1"

# Server System
ServerSystemName = "questServerSystem"
ServerSystemClsPath = "neteaseQuestScript.modServer.serverSystem.questServerSystem.QuestServerSystem"

# Dialogue
DialogueModName = "DialogueMod"
DialogueClientSystemName = "dialogueClientSystem"

# Engine
Minecraft = "Minecraft"

# Server Component
# Engine
EngineTypeComponent = "engineType"
ScriptTypeCompServer = "type"
PosComponent = "pos"
RotComponent = "rot"
ItemComponent = 'item'
NameComponent = 'name'
ExtraDataComponent = 'extraData'
CommandComponent = 'command'

# Server Event
# Engine
LoadServerAddonScriptsAfter = 'LoadServerAddonScriptsAfter'
ServerChatEvent = "ServerChatEvent"
OnScriptTickServer = "OnScriptTickServer"
AddServerPlayerEvent = "AddServerPlayerEvent"
MobDieEvent = 'MobDieEvent'
AddLevelEvent = 'AddLevelEvent'
# Custom
DisplayDialogueEvent = 'DisplayDialogueEvent'
DisplayQuestEvent = 'DisplayQuestEvent'
HustleEvent = 'HustleEvent'
RefreshEvent = 'RefreshEvent'

# Client Event
# Engine
UiInitFinishedEvent = "UiInitFinished"
OnScriptTickClient = "OnScriptTickClient"
# Custom
AcceptQuestEvent = 'AcceptQuestEvent'
SubmitQuestEvent = 'SubmitQuestEvent'
ShiftDialogueEvent = 'ShiftDialogueEvent'
GetQuestProgressesEvent = 'GetQuestProgressesEvent'
ArriveEvent = 'ArriveEvent'

# UI
dialogueUIName = "dialogueUI"
dialogueUIClsPath = "neteaseQuestScript.modClient.ui.dialogueClientUI.DialogueScreen"
dialogueUIScreenDef = "dialogueUI.main"

QUEST_KILL_MONSTER = 1
QUEST_COLLECT_ITEM = 2
QUEST_ARRIVE_PLACE = 3
QUEST_PLAYER_LEVEL = 4

# editor config begin
QuestConfig = {}
# editor config end
