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
QuestConfig = {'\xe6\x89\x93\xe7\x81\xab\xe7\x9f\xb3': {'rewards': {'drugs': [{'type': 'minecraft:flint_and_steel', 'n': 1}], 'exp': 50}, 'questName': '\xe6\x89\x93\xe7\x81\xab\xe7\x9f\xb3', 'spot': [6983.0, 63.0, 28.0], 'cost': False, 'preconditions': {'lv': 0, 'stuff': [], 'preQuest': '\xe6\x8f\x90\xe5\x8d\x87\xe7\xad\x89\xe7\xba\xa7'}, 'desc': '\xe6\x89\xbe\xe5\x88\xb0\xc2\xa7a\xe7\x81\xab\xe7\x84\xb0\xe7\xa5\xad\xe5\x8f\xb8', 'questMobType': '', 'goal': 1, 'questItemType': 'minecraft:apple', 'questType': 3, 'amount': 1, 'limit': 1, 'radius': 5, 'npcEntityId': '-12884901827'}, '\xe5\xb0\x8f\xe8\xaf\x95\xe8\xba\xab\xe6\x89\x8b': {'rewards': {'drugs': [{'type': 'minecraft:diamond_sword', 'n': 1}], 'exp': 25}, 'questName': '\xe5\xb0\x8f\xe8\xaf\x95\xe8\xba\xab\xe6\x89\x8b', 'spot': None, 'cost': False, 'preconditions': {'lv': 0, 'stuff': [], 'preQuest': '\xe9\x80\x86\xe8\xa1\x8c\xe8\x80\x85'}, 'desc': '\xe5\x87\xbb\xe8\xb4\xa5\xe5\x97\x9c\xe8\xa1\x80\xe7\x8c\xaa\xe4\xba\xba%p\xef\xbc\x8c\xe6\x89\xbe\xe5\x88\xb0\xc2\xa7a\xe8\x92\x8b\xe5\xa3\xae', 'questMobType': 'ntestaskdemo:mon_pigman', 'goal': 1, 'questItemType': 'minecraft:apple', 'questType': 1, 'amount': 5, 'limit': 1, 'radius': 0, 'npcEntityId': '-12884901870'}, '\xe9\x80\x86\xe8\xa1\x8c\xe8\x80\x85': {'questMobType': '', 'rewards': {'drugs': [{'type': 'minecraft:wooden_sword', 'n': 1}, {'type': 'minecraft:chainmail_chestplate', 'n': 1}], 'exp': 10}, 'naviDestinationDoingServerType': 'lobby', 'goal': 1, 'questItemType': 'minecraft:apple', 'naviDestinationDoneServerType': 'lobby', 'questName': '\xe9\x80\x86\xe8\xa1\x8c\xe8\x80\x85', 'spot': [6978.0, 64.0, 87.0], 'limit': 1, 'naviDestinationDoing': [6978.0, 64.0, 87.0], 'questType': 3, 'amount': 1, 'cost': False, 'preconditions': {'lv': 0, 'stuff': [], 'preQuest': ''}, 'radius': 5, 'npcEntityId': '-12884901870', 'naviDestinationDone': [6978.0, 64.0, 87.0], 'desc': '\xe6\x89\xbe\xe5\x88\xb0\xe5\xa3\xab\xe5\x85\xb5\xc2\xa7a\xe8\x92\x8b\xe5\xa3\xae'}, '\xe6\x8f\x90\xe5\x8d\x87\xe7\xad\x89\xe7\xba\xa7': {'rewards': {'drugs': [], 'exp': 20}, 'questName': '\xe6\x8f\x90\xe5\x8d\x87\xe7\xad\x89\xe7\xba\xa7', 'spot': None, 'cost': False, 'preconditions': {'lv': 0, 'stuff': [], 'preQuest': '\xe5\xb0\x8f\xe8\xaf\x95\xe8\xba\xab\xe6\x89\x8b'}, 'desc': '\xe8\xbe\xbe\xe5\x88\xb0\xe7\xad\x89\xe7\xba\xa7%p\xef\xbc\x8c\xe6\x89\xbe\xe5\x88\xb0\xc2\xa7a\xe8\x92\x8b\xe5\xa3\xae', 'questMobType': '', 'goal': 4, 'questItemType': 'minecraft:apple', 'questType': 4, 'amount': 1, 'limit': 1, 'radius': 0, 'npcEntityId': '-12884901870'}}
# editor config end
