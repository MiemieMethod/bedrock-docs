# -*- coding: utf-8 -*-

from neteaseBattleScript.clientNetwork.rpcHandlerClient import RpcHandlerClient
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import ClientSpecEvent

class RpcClient(object):
	"""
	封装的rpc类
	本质原理就是modsdk监听事件处仅设置1个事件
	事件的参数是方法名和方法执行参数
	双端传递调用各自的方法执行
	"""
	def __init__(self):
		super(RpcClient, self).__init__()
		self.mProxy = RpcProxyClient()
		self.mHandler = RpcHandlerClient()

	def ServerRpc(self):
		return self.mProxy

	def Handle(self, methodName, args):
		method = getattr(self.mHandler, methodName, None)
		if not method:
			print "RpcHandler has not method {}".format(methodName)
			return
		method(*args)

class RpcProxyClient(object):
	def __init__(self):
		super(RpcProxyClient, self).__init__()
		self.mMethod = None

	def __getattr__(self, method, *args, **kwargs):
		"""
		在客户端调用RPGServerRpc().function()的时候进行hook，保留function的方法名，之后发事件到服务端
		:param method: str
		:param args: tuple
		:param kwargs: dict
		:return:
		"""
		self.mMethod = method
		return self.CallServer  # 返回的是个方法对象，所以使用大致为ServerRpc().xxxxx(arg1, arg2.....)，这个xxxxx就会存到上面这个method变量中

	def CallServer(self, *args, **kwargs):
		"""
		正常调用的参数就会放置到下方data字典中
		发送事件到服务端
		:param args:
		:param kwargs:
		:return:
		"""
		data = {
			'method' : self.mMethod,
			'args' : args
		}
		apiUtil.GetClientSystem().NotifyToServer(ClientSpecEvent.RpcEvent, data)
