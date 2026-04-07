# -*- coding:utf-8 -*-
from guildConsts import PlayerAttrType

class PlayerGac(object):
	'''
	单个玩家的信息
	'''
	def __init__(self):
		self.mAttrsDictCurrent = {}  # 玩家属性
		
	def SyncAttrsDict(self, args):
		for attrType, attrValue in args.items():
			self.SetAttrCurrent(attrType, attrValue)
		print self.mAttrsDictCurrent
	
	def SetAttrCurrent(self, attrType, attrValue):
		self.mAttrsDictCurrent[attrType] = attrValue
		
	def GetAttr(self, attrType):
		'''
		查询属性
		'''
		return self.mAttrsDictCurrent.get(attrType, None)
