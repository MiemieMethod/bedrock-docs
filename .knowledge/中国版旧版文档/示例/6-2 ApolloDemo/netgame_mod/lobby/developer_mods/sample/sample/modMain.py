# -*- coding: utf-8 -*-
#

from common.mod import Mod
import server.extraServerApi as serverApi
import client.extraClientApi as clientApi


'''
大型示例Mod
实现最简单的Lobby（主城）逻辑

创建自定义NPC，并响应敲击NPC的事件弹出菜单（通过向客户端发送事件的方式）
监测到和Master进程的连接，并且在连接建立后定时请求排行榜数据
注册玩家上线、下线事件，维护在脚本层的玩家额外数据对象
使用脚本设置玩家的出生点
响应来自Master的公告事件并广播给客户端
敲击特定的NPC触发配对开始和中止，并响应Master的配对成功消息，自动跳转到指定的游戏进程
'''

@Mod.Binding(name = "SAMPLE", version = "0.5")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_sample_mod!==============================='
		self.server = serverApi.RegisterSystem("Minecraft", "SampleServer", "sample.modSystem.sampleServer.SampleServer")

	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='
		
	@Mod.InitClient()
	def initClient(self):
		print '===========================init_sample_mod!==============================='
		self.client = clientApi.RegisterSystem("Minecraft","SampleClient","sample.modSystem.sampleClient.SampleClient")
		
	@Mod.DestroyClient()
	def destroyClient(self):
		pass
