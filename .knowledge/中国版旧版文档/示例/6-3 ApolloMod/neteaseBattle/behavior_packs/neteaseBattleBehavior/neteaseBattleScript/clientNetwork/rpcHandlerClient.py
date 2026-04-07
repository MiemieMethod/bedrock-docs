# -*- coding:utf-8 -*-

from neteaseBattleScript.battleCommon.battleConsts import CInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts
import neteaseBattleScript.battleCommon.apiUtil as apiUtil

class RpcHandlerClient(object):
	"""
	客户端的
	供服务端可调用的方法集中区域
	服务端也有对应的类似类
	rpc方法名出现在下列方法中的即可成功调用
	"""

	def TestRpc(self, testList, testString):
		print "TestRpc {} {}".format(testList, testString)

	def SyncConfig(self, version, configDict):
		print "SyncConfig version=%s" % version
		for attrName, attrValue in configDict.iteritems():
			setattr(battleConsts, attrName, attrValue)
			#print "SyncConfig attr=%s value=%s" % (attrName, getattr(battleConsts, attrName, None))
		apiUtil.GetClientSystem().GetEventMgr().NotifyEvent(CInterEvent.UIDeskReinit, {})

	def SyncEntityStatic(self, entityAttrDict):
		for entityName, attrDict in entityAttrDict.iteritems():
			battleConsts.EntityAttrs[entityName] = attrDict
			#print "SyncEntityStatic entityName=%s" % entityName
			#for k, v in attrDict.iteritems():
			#	print "entity attr=%s value=%s" % (k, str(v))

	def SyncEquipStatic(self, equipAttrDict):
		for equipName, attrDict in equipAttrDict.iteritems():
			battleConsts.EquipAttrs[equipName] = attrDict
			#print "SyncEquipStatic equipName=%s" % equipName
			#for k, v in attrDict.iteritems():
			#	print "equip attr=%s value=%s" % (k, str(v))

	def DoAddItemFromCommand(self, itemDict):
		playerId = apiUtil.GetClientSystem().GetLocalPlayer()
		apiUtil.GetClientSystem().GetRpcUtil().ServerRpc().NotifyPlayerGetItem(playerId, playerId)

	def SyncGameObj(self, dataList):
		for data in dataList:
			apiUtil.GetClientSystem().GetObjMgr().OnSyncGameObj(data)

	def UpdateGameObj(self, guidList, dataList):
		for idx, guid in enumerate(guidList):
			apiUtil.GetClientSystem().GetObjMgr().OnUpdateGameObj(guid, dataList[idx])
			if guid == apiUtil.GetClientSystem().GetLocalPlayer():
				apiUtil.GetClientSystem().GetEventMgr().NotifyEvent(CInterEvent.UIStatusDraw, {"guid":guid})
				apiUtil.GetClientSystem().GetEventMgr().NotifyEvent(CInterEvent.UIDeskHealth, {"guid":guid})

	def DeleteGameObj(self, guidList):
		for idx, guid in enumerate(guidList):
			apiUtil.GetClientSystem().GetObjMgr().DelObjectById(guid)

	def SyncBagsInfo(self, playerId, diffBagInfo):
		player = apiUtil.GetClientSystem().GetObjMgr().GetObject(playerId)
		if not player:
			return
		player.UpdateBagsInfo(diffBagInfo)
		if playerId == apiUtil.GetClientSystem().GetLocalPlayer():
			apiUtil.GetClientSystem().GetEventMgr().NotifyEvent(CInterEvent.UIStatusDraw, {"guid": playerId})

	def EquipFlyAnimate(self, playerId, opList):
		print "EquipFlyAnimate player=%s length=%s" % (playerId, len(opList))
		for data in opList:
			print "single op", data

	def BagFlyAnimate(self, playerId, opList):
		print "BagFlyAnimate player=%s length=%s" % (playerId, len(opList))
		for data in opList:
			print "bag fly animate", data



