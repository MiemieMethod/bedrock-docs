# -*- coding:utf-8 -*-
import Queue
from guildConsts import GuildAttrType

class GuildGas(object):
	'''
	单个公会的信息
	'''
	def __init__(self):
		self.mAttrsDictCurrent = {}  # 公会属性
	
	def SyncAttrsDict(self, args):
		for attrType, attrValue in args.items():
			self.SetAttrCurrent(attrType, attrValue)
	
	def SetAttrCurrent(self, attrType, attrValue):
		self.mAttrsDictCurrent[attrType] = attrValue
	
	def GetAttrsDictCurrent(self):
		return self.mAttrsDictCurrent
		
	def GetAttr(self, attrType):
		'''
		查询属性
		'''
		return self.mAttrsDictCurrent.get(attrType, None)
	