# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

class TestServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		self.ListenForEvent("neteaseShop", "neteaseShopDev", "ServerShipItemsEvent", self, self.OnServerShipItems)
	
	def StartShip(self):
		'''
		开始发货
		'''
		neteaseShopServerSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
		uid = 123456  # 传入的参数是玩家的uid
		neteaseShopServerSystem.StartShipProcess(uid)
		
	def OnServerShipItems(self, args):
		'''
		收到订单信息，执行发货逻辑
		'''
		uid = args["uid"]
		entities = args["entities"]
		#根据 entities 执行发货逻辑,entities参数如下
		# entities = [{
		# 	"item_id": 90027446413343740, #商品id，仅记录用
		# 	"uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",# 玩家的唯一编号
		# 	"item_num":1,#玩家购买的道具数量
		# 	"orderid":"1234", #订单id
		# 	"cmd":"test",#实现指令
		# 	"buy_time":1230782400,#购买时间戳
		# 	"group" : 1#道具分类
		# },
		# {
		# 	"item_id": 90027446413343740,
		# 	"uuid": "8a0886b5-eeb5-41f0-b517-f65691a2ce3b",
		# 	"item_num":1,
		# 	"orderid":"1235",
		# 	"cmd":"test",
		# 	"buy_time":1230782400,
		# 	"group" : 1
		# }
		# ]
		for entity in entities:
			itemNum = entity['item_num']
			cmd = entity['cmd']
			#todo:开发者在需要根据cmd给玩家发货
		#发货之后，需要通知Apollo发货成功了。
		self.ShipSuccess(args)
		
	def ShipSuccess(self,args):
		'''
		通知Apollo发货成功了
		'''
		neteaseShopServerSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
		neteaseShopServerSystem.ShipOrderSuccess(args)
		
	def Destroy(self):
		self.UnListenForEvent("neteaseShop", "neteaseShopDev", "ServerShipItemsEvent", self, self.test)
