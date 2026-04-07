# -*- coding: utf-8 -*-
 # 上面这行是让这个文件按utf-8进行编码，这样就可以在注释中写中文了

# 这行import到的是引擎服务端的API模块
import server.extraServerApi as serverApi
# 获取引擎服务端System的基类，System都要继承于ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()
# 在modMain中注册的Server System类
class HelloServerSys(ServerSystem):
	# ServerSystem的初始化函数
	def __init__(self,namespace,systemName):
		# 首先调用父类的初始化函数
		ServerSystem.__init__(self, namespace, systemName)
		# 初始时调用监听函数监听事件
		#第一个参数是namespace，表示客户端名字空间，第二个是客户端System名称，第三个是监听事件的名字，第五个参数是回调函数（或者监听函数）
		self.ListenForEvent("hello", "helloClient", 'TestRequest', self, self.OnTestRequest)

	# 回调函数，用于处理客户端消息
	def OnTestRequest(self, args):
		print 'hello world'
		print 'request data', args

	# 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
	def Destroy(self):
		# 注销监听事件
		self.UnListenForEvent("hello", "helloClient", 'TestRequest', self, self.OnTestRequest)