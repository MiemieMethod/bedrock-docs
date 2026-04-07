# -*- coding: utf-8 -*-

# import server.extraServerApi as serverApi
#
# ENTITY_TYPE = serverApi.GetMinecraftEnum().EntityType
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# Mod Version
ModName = "DialogueMod"
ModVersion = "0.0.1"

# Server System
ServerSystemName = "dialogueServerSystem"
ServerSystemClsPath = "neteaseQuestScript.modServer.serverSystem.dialogueServerSystem.DialogueServerSystem"

# Client System
ClientSystemName = "dialogueClientSystem"
ClientSystemClsPath = "neteaseQuestScript.modClient.clientSystem.dialogueClientSystem.DialogueClientSystem"

# Quest
QuestModName = "QuestMod"
QuestServerSystemName = "questServerSystem"

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

# Server Event
# Engine
ServerChatEvent = "ServerChatEvent"
OnScriptTickServer = "OnScriptTickServer"
AddServerPlayerEvent = "AddServerPlayerEvent"
PlayerAttackEntityEvent = 'PlayerAttackEntityEvent'
MobDieEvent = 'MobDieEvent'
AddLevelEvent = 'AddLevelEvent'
# Custom
DisplayDialogueEvent = 'DisplayDialogueEvent'
DisplayQuestEvent = 'DisplayQuestEvent'

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
PassPhraseEvent = 'PassPhraseEvent'

# UI
dialogueUIName = "dialogueUI"
dialogueUIClsPath = "neteaseQuestScript.modClient.ui.dialogueClientUI.DialogueScreen"
dialogueUIScreenDef = "dialogueUI.main"

# editor config begin
DialogueConfig = {}
# editor config end

APPEAR_CONDITION_NONE = 0
APPEAR_CONDITION_ELSE = 1
APPEAR_CONDITION_TODO = 2
APPEAR_CONDITION_DONE = 3
APPEAR_CONDITION_DOING = 4

NPC_ENTITY_ID_DICT = {}
[NPC_ENTITY_ID_DICT.setdefault(v['npcEntityId'], {i: set() for i in xrange(5)})[v['appearCondition']].add(k) for k, v in DialogueConfig.iteritems()]
