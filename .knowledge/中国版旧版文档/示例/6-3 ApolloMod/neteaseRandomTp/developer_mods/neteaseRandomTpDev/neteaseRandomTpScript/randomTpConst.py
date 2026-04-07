# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseRandomTp"
ClientSystemName = "neteaseRandomTpBeh"
ClientSystemClsPath = "neteaseRandomTpScript.randomTpClientSystem.RandomTpClientSystem"
ServerSystemName = "neteaseRandomTpDev"
ServerSystemClsPath = "neteaseRandomTpScript.randomTpServerSystem.RandomTpServerSystem"
ServiceSystemName = "neteaseRandomTpService"
ServiceSystemClsPath = "neteaseRandomTpScript.randomTpServiceSystem.RandomTpServiceSystem"

# 传送类型
class TpType(object):
	TpTypeInDimension = "InDimension" # 本维度传送
	TpTypeCrossDimension = "CrossDimension" # 跨维度传送
	TpTypeCrossServer = "CrossServer" # 跨服传送

# 打断类型
class InterruptType(object):
	Cannot = 0
	Moving = 1
	Hurting = 2
	MovingOrHurting = 3

# 默认参数（在配置文件不生效的时候作为默认值）
class DefaultParams(object):
	CoolingTime = 10 # 冷却时间
	ReadingTime = 3 # 读秒时间
	InterruptType = InterruptType.Moving # 打断类型
	IsCoolingAfterInterrupt = 0 # 被打断后是否进入冷却
	RandomRange = [-64, -64, 64, 64] # 随机范围
	BlockBlackList = [ # 禁止传送的方块黑名单
		"minecraft:water", 
		"minecraft:flowing_water", 
		"minecraft:lava", 
		"minecraft:flowing_lava"
		]
	TpBlackList = [] # 传送黑名单，在范围内的区域禁止发起传送
	SafePosRange = 7 # 安全位置搜索范围，默认 15*15*15 的方块区域，出于性能考虑，最好不要超过15

# 配置文件中的配置
ConfigParams = {}


# 客户端和服务器交互
class ClientEvent(object):
	ReadingStarted = "ReadingStartedToClientEvent"
	ReadingInterrupted = "ReadingInterruptedToClientEvent"
	TpFinished = "TpFinishedToClientEvent"

# 服务器间通信
class ServerEvent(object):
	CheckTpCD = "CheckTpCDFromServerEvent" # 请求service检查CD
	StartTp = "StartTpFromServerEvent" # 请求service开始传送
	TpInterrupt = "TpInterruptFromServerEvent" # 通知service传送被打断

# 抛出的事件
class OutputEvent(object):
	TpStarted = "TpStartedOutputEvent" # 发起传送的时刻
	ReadingInterrupted = "ReadingInterruptedOutputEvent" # 读秒被打断的时刻
	ReadingFinished = "ReadingFinishedOutputEvent" # 读秒完成的时刻
	TpFinished = "TpFinishedOutputEvent" # 传送完成的时刻

# 错误码
MsgTpForbiden = "当前场景禁止传送"
MsgTpTargetPosEmpty = "传送目标点随机范围未明，无法传送"
MsgInCD = "冷却中，还有%s秒可以再次传送"
MsgReadingTime = "%s秒后开始传送"
MsgTpInterrupt = "传送已被打断"
MsgInDimensionTpFinished = "你已传送到 (%s, %s, %s)"
MsgCrossDimensionTpFinished = "你已传送到 %s维度，(%s, %s, %s)"
MsgCrossServerTpFinished = "你已传送到 %s服务器，%s维度，(%s, %s, %s)"
