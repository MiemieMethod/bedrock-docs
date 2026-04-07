# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseTrade"
ClientSystemName = "neteaseTradeBeh"
ClientSystemClsPath = "neteaseTradeScript.tradeClientSystem.TradeClientSystem"
ServerSystemName = "neteaseTradeDev"
ServerSystemClsPath = "neteaseTradeScript.tradeServerSystem.TradeServerSystem"
ServiceSystemName = "neteaseTradeService"
ServiceSystemClsPath = "neteaseTradeScript.tradeServiceSystem.TradeServiceSystem"
MasterSystemName = "neteaseTradeMaster"
MasterSystemClsPath = "neteaseTradeScript.tradeMasterSystem.TradeMasterSystem"

# UI
tradeUIName = "tradeUI"
tradeUIClsPath = "neteaseTradeScript.tradeClientUI.TradeScreen"
tradeUIScreenDef = "tradeUI.main"
saleUIName = "saleUI"
saleUIClsPath = "neteaseTradeScript.saleUI.SaleScreen"
saleUIScreenDef = "saleUI.main"

# 配置名称
CfgKeyDoughs = 'Doughs'
CfgKeyGroceries = 'Groceries'
CfgKeySales = 'Sales'
CfgKeyDealers = 'Dealers'
CfgKeyRefreshGroceries = 'RefreshGroceries'

# 数据库表名
# 玩家货币持有信息表
TableTradeDough = "neteaseTradePlayerDoughInfo"
# 玩家商店购买信息表
TableTradeGrocery = "neteaseTradePlayerGroceryInfo"
# 商店刷新表
TableTradeGroceryRefresh = 'neteaseTradeGroceryRefreshInfo'
# 摆摊商品表
TableTradeSaleMerch = 'neteaseTradeSaleMerchInfo'

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"

# 事件
QueryPlayerDoughsEvent = 'QueryPlayerDoughsEvent'
UpdatePlayerDoughsEvent = 'UpdatePlayerDoughsEvent'
DisplayGroceryEvent = 'DisplayGroceryEvent'
PlayerPurchaseEvent = 'PlayerPurchaseEvent'
PlayerOpenStallEvent = 'PlayerOpenStallEvent'
PlayerCloseStallEvent = 'PlayerCloseStallEvent'
MerchOnSaleEvent = 'MerchOnSaleEvent'
PlayerWithdrawMerchEvent = 'PlayerWithdrawMerchEvent'
StallSaleUpdateEvent = 'StallSaleUpdateEvent'
PlayerSpotMerchEvent = 'PlayerSpotMerchEvent'
DisplayStallEvent = 'DisplayStallEvent'


# 玩家货币指令
class TradeRequestMapping(object):
	Query = "/query-player-doughs"
	Update = "/update-player-doughs"
	Count = '/count-stalls'


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
