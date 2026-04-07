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
DialogueConfig = {
	"3提升等级-接任务": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "3提升等级-接任务",
		"compositions": [{"select": [{"reply": "怎么封住裂隙？", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "想必你也发现了，不断的有怪物从裂隙冒出来，要想彻底解决问题，就要封住裂隙。"}, {"select": [{"reply": "那会很危险", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "看到我身边的传送门了吗，通过传送门进入地狱，找到裂隙彻底封死。"}, {"select": [{"reply": "我还有父母需要赡养……", "option": {"todo": "", "continue": False, "shift": "3提升等级-不愿意分支", "done": ""}}, {"reply": "我愿意", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "是的，那么，你是否愿意进入地狱，拯救世界？"}, {"select": [{"reply": "接受任务", "option": {"todo": "提升等级", "continue": False, "shift": "", "done": ""}}], "content": "哇——你是第一个同意的人，你的勇气会被大家永远铭记于心。进入地狱非常危险，你要先把等级提升到5级。"}],
		"appearCondition": 2,
		"postAppearTodo": "提升等级",
	},
	"2小试身手-接任务": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "2小试身手-接任务",
		"compositions": [{"select": [{"reply": "接取任务", "option": {"todo": "小试身手", "continue": False, "shift": "", "done": ""}}], "content": "村庄旁边有几只弱小的僵尸猪人，你先去收拾了他们，证明你有和我继续对话的实力。"}],
		"appearCondition": 2,
		"postAppearTodo": "小试身手",
	},
	"3提升等级-未完成时": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "提升等级",
		"dialogueName": "3提升等级-未完成时",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "你的等级还太低，还不适合进入地狱。"}],
		"appearCondition": 4,
		"postAppearTodo": "",
	},
	"闲话-苏小陆": {
		"postAppearDone": "",
		"npcEntityId": "-21474836475",
		"postAppearDoing": "",
		"dialogueName": "闲话-苏小陆",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "小花，我真没用……"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
	"4打火石-交任务": {
		"postAppearDone": "打火石",
		"npcEntityId": "-12884901827",
		"postAppearDoing": "",
		"dialogueName": "4打火石-交任务",
		"compositions": [{"select": [{"reply": "……", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "我的火焰告诉我，你就是那个最有勇气的人……"}, {"select": [{"reply": "……", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "不要说话，火焰正在低语……"}, {"select": [{"reply": "……", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "火焰说你需要打火石……"}, {"select": [{"reply": "完成任务（任务链完结）", "option": {"todo": "", "continue": False, "shift": "", "done": "打火石"}}], "content": "不要说话，火焰正在低语……火焰说赶紧给你打火石，不要耽误你的时间了……哦，好吧，给你打火石……"}],
		"appearCondition": 3,
		"postAppearTodo": "",
	},
	"4打火石-接任务": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "4打火石-接任务",
		"compositions": [{"select": [{"reply": "接受任务", "option": {"todo": "打火石", "continue": False, "shift": "", "done": ""}}], "content": "现在，去找火焰祭司拿打火石吧，只有打火石才能够启动传送门。"}],
		"appearCondition": 2,
		"postAppearTodo": "打火石",
	},
	"闲话-刘二锅": {
		"postAppearDone": "",
		"npcEntityId": "-21474836477",
		"postAppearDoing": "",
		"dialogueName": "闲话-刘二锅",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "大哥等等我！"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
	"3提升等级-不愿意分支": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "3提升等级-不愿意分支",
		"compositions": [{"select": [{"reply": "对不起……", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "嗯，这的确需要莫大的勇气，你不是第一个拒绝的人。"}, {"select": [{"reply": "好的（任务链完结）", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "没事，你也可以护送那些逃难的村民，他们很需要保护。"}],
		"appearCondition": 1,
		"postAppearTodo": "",
	},
	"1逆行者-接任务": {
		"postAppearDone": "",
		"npcEntityId": "-21474836475",
		"postAppearDoing": "",
		"dialogueName": "1逆行者-接任务",
		"compositions": [{"select": [{"reply": "你们怎么这么慌张？", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "不行了，不行了，跑不动了……"}, {"select": [{"reply": "到底发生了什么？", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "呼——你是从外地来的吧，赶紧逃吧！"}, {"select": [{"reply": "我武功高强，不用逃", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "村庄的地底突然冒出几个怪物，杀了好多村民，我心爱的小花也……据说地狱的怪物打开了来到主世界的裂隙，怪物会越来越多。总之，你想活命的话，就赶紧和我们一起逃吧。"}, {"select": [{"reply": "接受任务", "option": {"todo": "逆行者", "continue": False, "shift": "", "done": ""}}], "content": "既然你这么自信，去找找把守传送门的那些士兵吧。传送门就在不远处的湖边。"}],
		"appearCondition": 2,
		"postAppearTodo": "逆行者",
	},
	"3提升等级-交任务": {
		"postAppearDone": "提升等级",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "3提升等级-交任务",
		"compositions": [{"select": [{"reply": "领取奖励", "option": {"todo": "", "continue": False, "shift": "", "done": "提升等级"}}], "content": "你的身板强壮了不少，这些奖励请收下，可以帮助你在地狱杀敌。"}],
		"appearCondition": 3,
		"postAppearTodo": "",
	},
	"2小试身手-交任务": {
		"postAppearDone": "小试身手",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "2小试身手-交任务",
		"compositions": [{"select": [{"reply": "领取奖励", "option": {"todo": "", "continue": False, "shift": "", "done": "小试身手"}}], "content": "想不到你有两下子，这些奖励是你该得的。"}],
		"appearCondition": 3,
		"postAppearTodo": "",
	},
	"闲话-火焰祭司": {
		"postAppearDone": "",
		"npcEntityId": "-12884901827",
		"postAppearDoing": "",
		"dialogueName": "闲话-火焰祭司",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "火焰啊火焰，谁是天下最漂亮的女人。"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
	"闲话-李一一": {
		"postAppearDone": "",
		"npcEntityId": "-21474836476",
		"postAppearDoing": "",
		"dialogueName": "闲话-李一一",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "呜呜呜……"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
	"闲话-刘大锅": {
		"postAppearDone": "",
		"npcEntityId": "-21474836478",
		"postAppearDoing": "",
		"dialogueName": "闲话-刘大锅",
		"compositions": [{"select": [{"reply": "你们怎么了", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "呼——呼——呼——"}, {"select": [{"reply": "那我问其他人吧", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "快让开，快让开……"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
	"1逆行者-交任务": {
		"postAppearDone": "逆行者",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "1逆行者-交任务",
		"compositions": [{"select": [{"reply": "需要我帮忙吗？", "option": {"todo": "", "continue": True, "shift": "", "done": ""}}], "content": "唔……不知道下一波地狱怪物哪个时候过来……"}, {"select": [{"reply": "领取奖励", "option": {"todo": "", "continue": False, "shift": "", "done": "逆行者"}}], "content": "居然有人敢逆逃难队伍前行！你很有勇气，我很欣赏你！不过，地狱怪物可是很强的，给你几件装备，先穿上再说。"}],
		"appearCondition": 3,
		"postAppearTodo": "",
	},
	"闲话-蒋壮": {
		"postAppearDone": "",
		"npcEntityId": "-12884901870",
		"postAppearDoing": "",
		"dialogueName": "闲话-蒋壮",
		"compositions": [{"select": [{"reply": "离开", "option": {"todo": "", "continue": False, "shift": "", "done": ""}}], "content": "怪物越来越多了！！！"}],
		"appearCondition": 0,
		"postAppearTodo": "",
	},
}
# editor config end

APPEAR_CONDITION_NONE = 0
APPEAR_CONDITION_ELSE = 1
APPEAR_CONDITION_TODO = 2
APPEAR_CONDITION_DONE = 3
APPEAR_CONDITION_DOING = 4

NPC_ENTITY_ID_DICT = {}
[NPC_ENTITY_ID_DICT.setdefault(v['npcEntityId'], {i: set() for i in xrange(5)})[v['appearCondition']].add(k) for k, v in DialogueConfig.iteritems()]
