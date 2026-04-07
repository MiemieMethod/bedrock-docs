# -*- coding: utf-8 -*-
import weakref

import server.extraServerApi as serverApi
import serverlevel

class NpcData(object):
	def __init__(self, pid, key):
		super(NpcData, self).__init__()
		self.pid = pid
		self.speckey = key
		self.init_pos = (0, 0, 0)
		self.engine_id = None
		self.inited = False
	
	def load_extra_data(self, data):
		pos = data.get("pos", None)
		if pos:
			self.init_pos = (int(pos[0]), int(pos[1]), int(pos[2]))
		
	def init_success(self, engine_id):
		self.engine_id = engine_id
		self.inited = True
		
class Manager(object):
	def __init__(self, server):
		self.server = weakref.proxy(server)
		self.recent_pid = 1
		self.waiting_list = []
		self.activeDic = {}
		
	def register_npc(self, key, extra_data):
		pid = self.recent_pid
		npc = NpcData(pid, key)
		npc.load_extra_data(extra_data)
		self.waiting_list.append(npc)
		#
		self.recent_pid += 1
		return pid
	
	def try_init_npc(self):
		for idx, npc_data in enumerate(self.waiting_list):
			if npc_data.inited:
				continue
			exist = serverlevel.check_chunk_state(npc_data.init_pos)
			if not exist:
				continue
			entityid = self.create_single_npc(npc_data)
			if (not entityid) or (entityid < 0):
				print "create npc fail entityid=%s" % entityid
				continue
			npc_data.init_success(entityid)
			print "create npc success entityid=%s" % entityid
			self.activeDic[entityid] = npc_data
			self.waiting_list[idx] = None
		while (None in self.waiting_list):
			self.waiting_list.remove(None)
	
	def create_single_npc(self, npc_data):
		tempEntity = self.server.CreateTempEntity()
		typeComp = self.server.CreateComponent(tempEntity.mId, 'Minecraft', 'type')
		typeComp.type = serverApi.GetMinecraftEnum().EntityConst.TYPE_NPC
		typeComp = self.server.CreateComponent(tempEntity.mId, 'Minecraft', 'engineType')
		typeComp.engineType = serverApi.GetMinecraftEnum().EntityType.Husk
		posComp = self.server.CreateComponent(tempEntity.mId, 'Minecraft', 'pos')
		posComp.pos = (npc_data.init_pos[0], npc_data.init_pos[1], npc_data.init_pos[2])
		rotComp = self.server.CreateComponent(tempEntity.mId, 'Minecraft', 'rot')
		rotComp.rot = (0, 0)
		entityId = self.server.CreateEntity(tempEntity)
		return entityId
		
	def waiting_create_npc(self):
		return len(self.waiting_list) > 0
	
	def get_npc(self, npc_id):
		return self.activeDic.get(npc_id, None)
		
		
		
		
		