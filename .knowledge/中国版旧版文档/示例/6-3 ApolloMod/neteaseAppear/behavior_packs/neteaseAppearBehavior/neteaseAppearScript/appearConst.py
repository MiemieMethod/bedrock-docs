# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseAppear"
ClientSystemName = "neteaseAppearBeh"
ClientSystemClsPath = "neteaseAppearScript.appearClientSystem.AppearClientSystem"
ServerSystemName = "neteaseAppearDev"
ServerSystemClsPath = "neteaseAppearScript.appearServerSystem.AppearServerSystem"

# 数据库表名
TableAppear = "neteaseAppearInfo"

# 模型的配置
PropModels = {}

# 特效的配置
PropEffects = {}

# 外观的配置
PropAppears = {}
FreeAppears = []
DefaultBody = None
EmptyAppearData = {}

# 外观的类型
AllAppearTypes = []

class AppearType(object):
	Body = "body"
	Mount = "mount"
	Wing = "wing"
	Aura = "aura"

# c/s交互
class ClientEvent(object):
	ClientEnter = "ClientEnter"
	BuyAppear = "BuyAppear"
	ChangeUseAppear = "ChangeUseAppear"

class ServerEvent(object):
	ServerReady = "ServerReady"
	ChangeUseAppearRet = "ChangeUseAppearRet"
	BuyAppearRet = "BuyAppearRet"
	SyncAppearInfo = "SyncAppearInfo"
	UpdateUseAppear = "UpdateUseAppear"
	PlayerDie = "PlayerDie"
	ShowShop = "ShowShop"
	SyncMoney = "SyncMoney"
	JudgePosAndRot = "JudgePosAndRot"

# 错误码
FMT = {}
CodeSuc = 0
FMT[CodeSuc] = ""
CodePlayerAlreadyLeave = 1
FMT[CodePlayerAlreadyLeave] = "玩家已经下线"
CodeAppearNotExist = 2
FMT[CodeAppearNotExist] = "目标外观不存在，无法穿戴"
CodeAppearWithWrongType = 3
FMT[CodeAppearWithWrongType] = "目标外观类型不符合，无法穿戴"
CodeAppearNotUnloked = 4
FMT[CodeAppearNotUnloked] = "目标外观类型尚未解锁，无法穿戴"
CodeCreateHorseFail = 5
FMT[CodeCreateHorseFail] = "当前位置无法开始骑乘"
CodeNeedUseBodyFirst = 6
FMT[CodeNeedUseBodyFirst] = "需要替换时装后才能装备"
CodeBuyNotExistAppear = 7
FMT[CodeBuyNotExistAppear] = "不存在的装备，无法购买外观"
CodeBuyWithoutTrade = 8
FMT[CodeBuyWithoutTrade] = "没有部署交易插件，无法购买外观"
CodeBuyLackMoney = 9
FMT[CodeBuyLackMoney] = "代币不足，无法购买外观"
CodeBuyUnlocked = 10
FMT[CodeBuyUnlocked] = "已经拥有的外观无需再次购买"
CodeAlreadyUse = 11
FMT[CodeAlreadyUse] = "当前已经使用了目标外观"


