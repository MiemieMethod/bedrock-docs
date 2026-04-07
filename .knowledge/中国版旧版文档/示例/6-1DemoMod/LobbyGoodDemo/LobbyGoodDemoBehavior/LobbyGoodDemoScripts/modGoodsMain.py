from mod.common.modGoods import ModGoods
import mod.server.extraServerApi as serverApi

@ModGoods.Binding(name = "LobbyGoodDemo", version = "0.1")
class LobbyGoodDemoGoodsMain(object):
	def __init__(self):
		pass

	@ModGoods.DeliverGoods()
	def deliver_bb(self, entityId, type, iid):
		serverSystem = serverApi.GetSystem("LobbyGoodDemo", "LobbyGoodDemoServer")
		serverSystem.Deliver(entityId)
