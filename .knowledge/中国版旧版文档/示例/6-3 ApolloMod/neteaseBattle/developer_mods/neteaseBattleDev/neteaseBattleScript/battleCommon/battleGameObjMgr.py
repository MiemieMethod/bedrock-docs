# -*- coding: utf-8 -*-

class GameObjMgrBase(object):
	def __init__(self):
		# guid -> obj
		self.mObjMap = {}
		self.mObjToRemove = set()

	def Init(self):
		pass

	def Destroy(self):
		self.DelAllObj()

	def Tick(self, frame):
		if self.mObjToRemove:
			for guid in self.mObjToRemove:
				self.DelObjectById(guid)
			self.mObjToRemove = set()

	def GetObjectDict(self):
		"""
		:rtype: dict
		:return:
		"""
		return self.mObjMap

	def AddObject(self, obj):
		"""
		:param IdentifierBase obj:
		:rtype: bool
		:return:
		"""
		objectId = obj.GetId()
		if objectId in self.mObjMap:
			print 'Object %s already added' % objectId
			return False
		self.mObjMap[objectId] = obj
		return True

	def UpdateObject(self, obj):
		"""
		:param IdentifierBase obj:
		"""
		self.mObjMap[obj.GetId()] = obj

	def MarkRemove(self, guid):
		"""
		标志实体为待删除实体，延迟一帧删除
		:param guid:
		:type guid:
		:return:
		:rtype:
		"""
		if guid in self.mObjMap:
			self.mObjToRemove.add(guid)

	def DelObjectById(self, guid):
		"""
		这里执行Destroy函数
		:param str guid:
		"""
		if guid not in self.mObjMap:
			print 'Delete a nonexistent object', guid
			return None
		obj = self.mObjMap.pop(guid)
		obj.Destroy()

	def GetObject(self, guid):
		"""
		:param str guid:
		:rtype: None or IdentifierBase or RPGBattleScripts.modCommon.commonEntity.entityBase.EntityBase
		:return:
		"""
		return self.mObjMap.get(guid)

	def DelAllObj(self):
		for _,obj in self.mObjMap.iteritems():
			obj.Destroy()
		# map(IdentifierBase.Destroy, self.objMap.itervalues())
		self.mObjMap.clear()

class GameObjMgr(GameObjMgrBase):
	def __init__(self):
		self.mTypeToObjs = {} #GameObjType: set
		super(GameObjMgr, self).__init__()
		self.mTickGameObjSet = set() # 存放需要tick的实体的id

	def Tick(self, frame):
		super(GameObjMgr, self).Tick(frame)
		for guid in self.mTickGameObjSet:
			if guid in self.mObjMap and guid not in self.mObjToRemove:
				self.mObjMap[guid].Tick()

	def RegisterTickGameObj(self, guid):
		if guid in self.mTickGameObjSet:
			print 'obj {} already regsiter tick'.format(guid)
		else:
			self.mTickGameObjSet.add(guid)

	def AddObject(self, obj):
		"""
		:param obj:
		:type obj: RPGBattleScripts.modCommon.commonEntity.entityBase.EntityBase
		:return:
		:rtype:
		"""
		suc = super(GameObjMgr, self).AddObject(obj)
		if not suc:
			return suc
		objType = obj.GetGameObjType()
		if objType not in self.mTypeToObjs:
			self.mTypeToObjs[objType] = set()
		self.mTypeToObjs[objType].add(obj.GetId())
		if obj.mNeedTick:
			self.RegisterTickGameObj(obj.GetId())
		return True

	def UpdateObject(self, obj):
		"""
		:param EntityBase obj:
		"""
		guid = obj.GetId()
		if guid in self.mObjMap:
			old = self.mObjMap[guid]
			self.mTypeToObjs[old.GetGameObjType()].discard(guid)
			self.mTypeToObjs[old.GetGameObjType()].add(guid)
		return super(GameObjMgr, self).UpdateObject(obj)

	def DelObjectById(self, guid):
		"""
		基类执行了entity的Destroy函数，一般情况外部不要直接调用这个，调用MarkRemove函数
		:param str guid:
		"""
		obj = self.mObjMap.get(guid)
		if obj:
			self.mTypeToObjs[obj.GetGameObjType()].discard(guid)
		if guid in self.mTickGameObjSet:
			self.mTickGameObjSet.remove(guid)
		return super(GameObjMgr, self).DelObjectById(guid)

	def GetSetByType(self, objType):
		"""
		:param objType:
		:return:
		"""
		return self.mTypeToObjs.get(objType, set())

	def DelAllObj(self):
		"""
		基类执行了所有entity的Destroy函数
		:return:
		"""
		self.mTypeToObjs = {}
		self.mTickGameObjSet = set()
		super(GameObjMgr, self).DelAllObj()