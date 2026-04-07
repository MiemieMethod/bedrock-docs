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
QuestConfig = {
	"逆行者": {
		"spot": [6978.0, 64.0, 87.0],
		"questMobType": "",
		"rewards": {"drugs": [{"type": "minecraft:wooden_sword", "n": 1}, {"type": "minecraft:chainmail_chestplate", "n": 1}], "exp": 10},
		"goal": 1,
		"preconditions": {"lv": 0, "stuff": [], "preQuest": ""},
		"radius": 5,
		"cost": False,
		"questItemType": "minecraft:apple",
		"questName": "逆行者",
		"amount": 1,
		"questType": 3,
		"desc": "找到士兵§a蒋壮",
		"npcEntityId": "-12884901870",
		"limit": 1,
		"naviDestinationDoing": [6978.0, 64.0, 87.0],
		"naviDestinationDone": [6978.0, 64.0, 87.0],
		"naviDestinationDoingServerType": "lobby",
		"naviDestinationDoneServerType": "lobby",
	},
	"提升等级": {
		"spot": None,
		"questMobType": "",
		"rewards": {"drugs": [], "exp": 20},
		"goal": 4,
		"preconditions": {"lv": 0, "stuff": [], "preQuest": "小试身手"},
		"radius": 0,
		"cost": False,
		"questItemType": "minecraft:apple",
		"questName": "提升等级",
		"amount": 1,
		"questType": 4,
		"desc": "达到等级%p，找到§a蒋壮",
		"npcEntityId": "-12884901870",
		"limit": 1,
	},
	"小试身手": {
		"spot": None,
		"questMobType": "ntestaskdemo:mon_pigman",
		"rewards": {"drugs": [{"type": "minecraft:diamond_sword", "n": 1}], "exp": 25},
		"goal": 1,
		"preconditions": {"lv": 0, "stuff": [], "preQuest": "逆行者"},
		"radius": 0,
		"cost": False,
		"questItemType": "minecraft:apple",
		"questName": "小试身手",
		"amount": 5,
		"questType": 1,
		"desc": "击败嗜血猪人%p，找到§a蒋壮",
		"npcEntityId": "-12884901870",
		"limit": 1,
	},
	"打火石": {
		"spot": [6983.0, 63.0, 28.0],
		"questMobType": "",
		"rewards": {"drugs": [{"type": "minecraft:flint_and_steel", "n": 1}], "exp": 50},
		"goal": 1,
		"preconditions": {"lv": 0, "stuff": [], "preQuest": "提升等级"},
		"radius": 5,
		"cost": False,
		"questItemType": "minecraft:apple",
		"questName": "打火石",
		"amount": 1,
		"questType": 3,
		"desc": "找到§a火焰祭司",
		"npcEntityId": "-12884901827",
		"limit": 1,
	},
}
# editor config end
