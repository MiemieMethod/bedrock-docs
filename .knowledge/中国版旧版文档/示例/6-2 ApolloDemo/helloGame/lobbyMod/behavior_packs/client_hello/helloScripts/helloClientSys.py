# -*- coding: utf-8 -*-
 # 上面这行是让这个文件按utf-8进行编码，这样就可以在注释中写中文了

# 获取客户端引擎API模块
import client.extraClientApi as clientApi
# 获取客户端system的基类ClientSystem
ClientSystem = clientApi.GetClientSystemCls()
# 在modMain中注册的Client System类
class HelloClientSys(ClientSystem):
	# ServerSystem的初始化函数
	def __init__(self,namespace,systemName):
		# 首先调用父类的初始化函数
		ClientSystem.__init__(self, namespace, systemName)
		print "==== HelloClientSys Init ===="
		# 定义一个event,TestRequest方法可以通过这个event给服务端发送消息。
		self.DefineEvent('TestRequest')
		self.TestRequest()

	def TestRequest(self):
		#创建自定义事件的数据。data其实是个dict。
		data = self.CreateEventData()#等价于:data = {}
		data['test1'] = 'value1'
		data['test2'] = 'value2'
		#给服务端发送消息。服务端通过监听“TestRequest”事件处理消息，消息内容是data。
		self.NotifyToServer('TestRequest', data)

	# 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
	def Destroy(self):
		pass