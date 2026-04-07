# -*- coding: utf-8 -*-

import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst

# 创建新的持续效果对象
def CreateEffect(identifier):
	return Effect(identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Effect(object):
	def __init__(self, identifier):
		super(Effect, self).__init__()
		self.mIdentifier = identifier	# 唯一ID
		self.mCaster = None				# 效果释放者
		self.mDamage = 0
		self.mConfig = roundConst.ConfigEffectMap[identifier]	# 配置字典

	def UnPackSyncData(self, data):
		self.mId = data["mId"]
		self.mRound = data["mRound"]
		self.mEffectType = data["mEffectType"]

	def InitFromMonster(self, monster):
		self.mCaster = weakref.proxy(monster)

	def Destroy(self):
		self.mCaster = None

	def GetName(self):
		return self.mConfig.get("showName", "")
	
	def GetColor(self):
		if self.mConfig.get("positive", False):
			return (0, 1, 0, 0.8)
		else:
			return (1, 0, 0, 0.8)
	
	def GetDesc(self):
		desc = self.mConfig.get("desc", "")
		return "%s，剩余%d回合" % (desc, self.mRound)

	def GetImage(self):
		return self.mConfig.get("icon", "")
	

	
		
		




