# -*- coding: utf-8 -*-
import weakref

import server.extraServerApi as serverApi
import timer
from awesomeScripts.modCommon import modConfig

NPC_POS = {
	"gameA": (1396.273, 4, 57.163),
	"gameB": (1403.273, 4, 57.163),
	"gameC": (1410.273, 4, 57.163),
}
NPC_NAME = {
	"gameA": "NPC-A",
	"gameB": "NPC-B",
	"gameC": "NPC-C",
}


class NpcData(object):
	'''
	记录npc的数据
	'''
	def __init__(self, pos, name):
		super(NpcData, self).__init__()
		self.entity_id = None
		self.pos = pos
		self.inited = False
		self.name = name
		
	def init_success(self, id):
		'''
		npc初始化成功
		'''
		self.entity_id = id
		self.inited = True
		
class NpcManager(object):
	'''
	管理所有npc
	'''
	def __init__(self, server):
		super(NpcManager, self).__init__()
		global  NPC_POS
		self.server = weakref.proxy(server)
		self.waiting_npc = []#需要注册的npc列表
		self.active_npc_dict = {}#entity id => NpcData
		for name, pos in NPC_POS.iteritems():
			npc_data = NpcData(pos, name)
			self.waiting_npc.append(npc_data)
		#添加定时器，注册npc。
		self.register_npc_timer = timer.TimerManager.addTimer(10, self.TryCreateNpcs)
		
	def TryCreateNpcs(self):
		'''
		尝试创建npc
		'''
		self.register_npc_timer = None
		if not self.waiting_npc:
			return
		npc_num = len(self.waiting_npc)
		for id in xrange(npc_num):
			if self._CreateSingleNpc(id):
				npc_data = self.waiting_npc[id]
				self.active_npc_dict[npc_data.entity_id] = npc_data
				self.waiting_npc[id] = None
		self.waiting_npc = [one for one in self.waiting_npc if one]
		if self.waiting_npc:
			self.register_npc_timer = timer.TimerManager.addTimer(2, self.TryCreateNpcs)
		else:
			print 'create all npc success'


	def _CreateSingleNpc(self, id):
		'''
		创建一个npc
		'''
		npc_data = self.waiting_npc[id]
		#检查引擎是否已经加载了chunk。只有先加载chunk，然后才创建npc。
		chunkComp = self.server.CreateComponent(serverApi.GetLevelId(), "Minecraft", "chunkSource")
		exist = chunkComp.CheckChunkState(4, npc_data.pos)
		if (not exist) or (int(exist) == -1):
			return False
		#创建npc，并设置属性。
		temp_entity = self.server.CreateTempEntity()
		type_comp = self.server.CreateComponent(temp_entity.mId, modConfig.Minecraft, 'type')
		type_comp.type = serverApi.GetMinecraftEnum().EntityConst.TYPE_NPC
		engine_type = self.server.CreateComponent(temp_entity.mId, modConfig.Minecraft, 'engineType')
		engine_type.engineType = serverApi.GetMinecraftEnum().EntityType.Husk
		pos_comp = self.server.CreateComponent(temp_entity.mId, modConfig.Minecraft, 'pos')
		pos_comp.pos = (npc_data.pos[0], npc_data.pos[1], npc_data.pos[2])
		rot_comp = self.server.CreateComponent(temp_entity.mId, modConfig.Minecraft, 'rot')
		rot_comp.rot = (0, 180)
		dimesion_comp = self.server.CreateComponent(temp_entity.mId, modConfig.Minecraft, 'dimension')
		dimesion_comp.dimensionId = 4
		entity_id = self.server.CreateEntity(temp_entity)
		#检查npc是否成功创建。
		if (not entity_id) or (int(entity_id) == -1):
			return False
		npc_data.init_success(entity_id)
		name_comp = self.server.CreateComponent(entity_id, 'Minecraft', 'name')
		name_comp.SetName(NPC_NAME[npc_data.name])
		print 'create npc success.entity id:', entity_id
		return True

	def Destroy(self):
		'''
		清理工作。包括停止定时器。
		'''
		if self.register_npc_timer:
			self.register_npc_timer.cancel()
			self.register_npc_timer = None

	def GetNpcData(self, entity_id):
		return self.active_npc_dict.get(entity_id, None)
		
		
		