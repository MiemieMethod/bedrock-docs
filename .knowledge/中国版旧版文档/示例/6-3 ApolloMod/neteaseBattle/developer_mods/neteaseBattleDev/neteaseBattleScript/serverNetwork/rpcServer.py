# -*- coding: utf-8 -*-

import logout
from neteaseBattleScript.serverNetwork.rpcHandlerServer import RpcHandlerServer
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import ServerSpecEvent

# 服务端RPC工具类
class RpcServer(object):
	def __init__(self):
		super(RpcServer, self).__init__()
		self.mProxy = RpcProxyServer()
		self.mHandler = RpcHandlerServer()

	def ClientRpc(self, clientId):
		self.mProxy.mTargetClient = clientId #保存客户端Id
		return self.mProxy

	def Handle(self, methodName, args):
		method = getattr(self.mHandler, methodName, None)
		if not method:
			logout.error("RpcHandler has not method {}".format(methodName))
			return
		method(*args)

class RpcProxyServer(object):
	def __init__(self):
		super(RpcProxyServer, self).__init__()
		self.mTargetClient = None
		self.mMethod = None

	def __getattr__(self, method, *args, **kwargs):
		"""
		在服务端调用RPGClientRpc().function()的时候进行hook，保留function的方法名，之后发事件到客户端
		:param method: str
		:param args: tuple
		:param kwargs: dict
		:return:
		"""
		self.mMethod = method
		return self.CallClient

	def CallClient(self, *args, **kwargs):
		"""
		具体发事件到客户端的逻辑
		:param args:
		:param kwargs:
		:return:
		"""
		data = {
			'method' : self.mMethod,
			'args' : args
		}
		if self.mTargetClient == -1:
			apiUtil.GetServerSystem().BroadcastToAllClient(ServerSpecEvent.RpcEvent, data)
		elif self.mTargetClient is None:
			logout.error('RpcServer call method {} has not target'.format(self.mMethod))
		else:
			apiUtil.GetServerSystem().NotifyToClient(self.mTargetClient, ServerSpecEvent.RpcEvent, data)
