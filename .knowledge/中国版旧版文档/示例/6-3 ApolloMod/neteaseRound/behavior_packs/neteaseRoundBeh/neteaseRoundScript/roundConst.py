# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 支援函数

# 去掉配置里面的"_comment"
def CleanDict(_dict, exKey):
	if exKey in _dict:
		del _dict[exKey]
	for v in _dict.values():
		if type(v) == dict:
			CleanDict(v, exKey)

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [UnicodeConvert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

# 获取演出效果定义
def GetSkillPerformIdentifier(identifier):
	data = identifier.split(":")
	return "%s:skill:%s" % (data[0], data[1])

def GetEffectPerformIdentifier(identifier):
	data = identifier.split(":")
	return "%s:effect:%s" % (data[0], data[1])
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置

ModVersion = "1.0.0"
ModName = "neteaseRound"
# 负责战斗逻辑的system
ClientBattleSystemName = "neteaseBattleRoundBeh"
ClientBattleSystemClsPath = "neteaseRoundScript.roundBattleCSystem.RoundBattleClientSystem"
ServerBattleSystemName = "neteaseBattleRoundDev"
ServerBattleSystemClsPath = "neteaseRoundScript.roundBattleSSystem.RoundBattleServerSystem"
# 负责战斗外逻辑的system（示例system）
ClientSampleSystemName = "neteaseSampleRoundBeh"
ClientSampleSystemClsPath = "neteaseRoundScript.roundSampleCSystem.RoundSampleClientSystem"
ServerSampleSystemName = "neteaseSampleRoundDev"
ServerSampleSystemClsPath = "neteaseRoundScript.roundSampleSSystem.RoundSampleServerSystem"
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 角色、技能、持续效果等配置内容

# 角色配置
ConfigMonsterMap = {}
# 技能配置
ConfigSkillMap = {}
# 持续效果配置
ConfigEffectMap = {}
# 演出配置
ConfigPerformMap = {}

# 全部配置
ConfigAllTypeMap = {
	"monster": ConfigMonsterMap,
	"skill": ConfigSkillMap,
	"effect": ConfigEffectMap,
	"perform": ConfigPerformMap,
}

# 初始能量值
BattleStartEnergy = 2
# 每回合恢复能量值
RoundStartEnergy = 2
# -----------------------------------------------------------------------------------------------------------------------------------------------
# 宏定义

# 战斗角色配置属性
BattleAttrKeys = (
	"health",
	"attack",
	"defence",
	"crit",
	"tough",
	"critDamage",
	"critImmune",
	"effectHit",
	"effectResist",
	"speed",
	"energy",
)

BattleIntAttrKeys = (
	"health",
	"attack",
	"defence",
	"speed",
	"energy",
)

# 效果类型
# 当前分为影响基本属性的和添加特殊状态的
# 同类效果会顶替
class BattleEffectType(object):
	Empty = 0
	Weak1 = 1
	Slow1 = 2
	Haste1 = 3
	Stun1 = 4


# 战斗模式
class BattleStyle(object):
	PVP = "PVP"
	PVE = "PVE"

# 战斗双方
class BattleSide(object):
	SideA = "SideA"
	SideB = "SideB"

# 战斗位置
class BattlePos(object):
	StandPos1 = 1
	StandPos2 = 2
	StandPos3 = 3
	StandPos4 = 4
	StandPos5 = 5
	
# 战斗指挥
BattleControlAI = "AI01"

# 战斗状态机
class BattleState(object):
	BattleInit = 0 
	BattleStartWaitClientAck = 1 
	BattleRoundStart = 2
	BattleActionSelect = 3
	BattleActionPlay = 4
	BattleActionPlayEnd = 5
	BattleActionFin = 6
	BattleRoundFinish = 7
	BattleFinishWaitServerAck = 8
	BattleFinishWaitClientAck = 9

# 战斗结果
class BattleResult(object):
	Draw = 0
	SideAWin = 1
	SideBWin = 2

# 等待客户端初始化战场的最长时间
BattleStartWaitTick = 30
# 回合开始服务端等待时间
BattleRoundStartWaitTick = 3
# 单个角色行动结束后，服务端等待时间
BattleActionFinWaitTick = 1
# 单个角色选择行动时间
BattleActionSelectServerTick = 24
BattleActionSelectClientTick = 20
# 单个角色播放技能动画的最长时间
BattleActionPlayWaitTick = 30
# 单个角色技能实际生效等待时间
BattleActionPlayEndWaitTick = 1
# 回合结束服务端等待时间
BattleRoundFinishWaitTick = 1
# 战斗结束等待客户端显示结算完成最长等待时间
BattleFinishWaitTick = 20

# 技能的对象选择
class SkillTargetType(object):
	Self = 0
	ChoiceFriendOne = 1
	ChoiceEnemyOne = 2
	RandomFriendSome = 3
	RandomEnemySome = 4

# 持续效果/技能的伤害计算类型
class DamageStyle(object):
	StyleNone = 0
	StyleNormal = 1

# 持续效果的命中计算类型
class HitStyle(object):
	StyleMustHit = 0
	StyleNormal = 1

# 技能释放的效果类型
class SkillResultType(object):
	Damage = 0	# 造成伤害
	Heal = 1	# 造成治疗
	Effect = 2	# 生成持续效果
# -----------------------------------------------------------------------------------------------------------------------------------------------
# c/s交互

class SampleClientEvent(object):
	ClientEnter = "ClientEnter"

class SampleServerEvent(object):
	ServerReady = "ServerReady"
	SyncConfig = "SyncConfig"

class BattleClientEvent(object):
	BattleStartAck = "BattleStartAck"
	ActionSkillSelect = "ActionSkillSelect"
	ActionSkillAck = "ActionSkillAck"
	BattleFinishAck = "BattleFinishAck"

class BattleServerEvent(object):
	BattleStart = "BattleStart"
	RoundStart = "RoundStart"
	ActionStart = "ActionStart"
	SkillSelectResponse = "SkillSelectResponse"
	SkillPlayStart = "SkillPlayStart"
	ActionFinish = "ActionFinish"
	RoundFinish = "RoundFinish"
	BattleFinish = "BattleFinish"
	MonsterAddEffect = "MonsterAddEffect"
	MonsterDiscardEffect = "MonsterDiscardEffect"
	MonsterUpdate = "MonsterUpdate"
	EffectUpdate = "EffectUpdate"
	EffectAction = "EffectAction"
	EnergyRestore = "EnergyRestore"
	UpdateNextOrder = "UpdateNextOrder"


