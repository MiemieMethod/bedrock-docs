# -*- coding: utf-8 -*-
class MapGas(object):
	"""
	单个公会驻地信息
	"""
	def __init__(self, args):
		self.mMapId = args.get('mapId')
		self.mServerType = args.get('serverType')
		self.mPos1 = args.get('pos1')
		self.mPos2 = args.get('pos2')
		self.mUsed = args.get('used')
		self.mTranPos = args.get('tranPos')
		
	def SetMapUsed(self, used = True):
		self.mUsed = used
		
	def GetMapUsed(self):
		return self.mUsed
	
	def GetMapId(self):
		return self.mMapId
	
	def GetServerType(self):
		return self.mServerType
	
	def GetBornPos(self):
		return self.mTranPos