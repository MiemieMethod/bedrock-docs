# -*- coding: utf-8 -*-

import neteaseAlertScript.alertConst as alertConst  # 配置文件
import client.extraClientApi as clientApi  # MODSDK提供的库模块
import heapq

ClientSystem = clientApi.GetClientSystemCls()  # MODSDK提供的客户端基类


class MyAlert:
	"""
	提示任务封装类
	将服务端推送下来的提示文本相关信息封装成一个对象
	即可分离显示逻辑相关代码
	解除耦合
	"""
	def __init__(self, text, seconds, xratio, yratio):
		self.text = text  # 提示文本
		self.xratio = xratio  # 文本框中心点于屏幕横轴方向的偏移百分比
		self.yratio = yratio  # 文本框中心点于屏幕纵轴方向的偏移百分比
		# 生成一个任务链条
		# 长度为总时长（秒数） * 帧率
		# 每一个元素即为每一帧应当执行的方法
		# 该处头元素为显示提示文本框
		# 尾元素为关闭提示文本框
		# 中部均不做任何操作
		# 全部组成了弹出提示文本到关闭的任务链
		self.chain = [self.debut] + [None for i in xrange(seconds * 30 - 2)] + [
			lambda node: node.mBg.SetVisible(False)]

	def debut(self, node):
		node.mText.SetText(self.text)  # 按照初始化时的参数设置文本内容
		node.mBg.SetVisible(True)  # 将文本框打开显示
		screenSize = node.mMainPanel.GetSize()
		bgSize = node.mBg.GetSize() # 先SetVisible(True)才能拿到size，否则size为(0, 0)
		node.mBg.SetPosition((screenSize[0] * self.xratio - bgSize[0]/2, screenSize[1] * self.yratio - bgSize[1]/2))  # 按照初始化时的参数设置文本框的位置

	def tick(self, node):
		if self.chain:
			do = self.chain.pop(0)  # 每帧从链表中弹出头部元素
			do and do(node)  # 不为空则执行
	
	# 任务链是否完成
	def finish(self):
		return not self.chain


# 任务优先级队列
class TaskPriorityQueue(object):
	def __init__(self):
		self._queue = []
		self._index = 0
	
	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1
	
	def replace(self, item ,priority):
		self._queue = []
		self.push(item, priority)
	
	def pop(self):
		return heapq.heappop(self._queue)[-1] if self._queue else None
	
	def top(self):
		return self._queue[0][-1]

	def empty(self):
		return True if not self._queue else False

class AlertClientSystem(ClientSystem):
	@property
	def task(self):  # 提供一个属性供外部访问获取当前应该展示的提示任务
		while not self.mTaskQueue.empty():
			task = self.mTaskQueue.top()
			if not task.finish():
				return task
			self.mTaskQueue.pop()
		return None

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mLocalPlayerId = clientApi.GetLocalPlayerId()
		self.mLastAlert = None  # 提示任务对象的引进
		self.mTaskQueue = TaskPriorityQueue()

		self.mDefaultShowTime = 0
		self.mXRatio = 0
		self.mYRatio = 0

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), alertConst.UiInitFinishedEvent, self, self.OnUiInitFinished)  # 监听原生UI初始化完毕事件
		self.ListenForEvent(alertConst.ModName, alertConst.ServerSystemName, alertConst.NewAlertEvent, self, self.OnNewAlert)  # 监听该Mod的服务端推送提示事件
		self.ListenForEvent(alertConst.ModName, alertConst.ServerSystemName, alertConst.ModConfigResponseFromServerEvent, self, self.OnModConfigResponseFromServerEvent)

	def Destroy(self):
		self.mAlertUINode = None  # 清除引用
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), alertConst.UiInitFinishedEvent, self, self.OnUiInitFinished)  # 清除引用
		self.UnListenForEvent(alertConst.ModName, alertConst.ServerSystemName, alertConst.NewAlertEvent, self, self.OnNewAlert)  # 清除引用
		self.UnListenForEvent(alertConst.ModName, alertConst.ServerSystemName, alertConst.ModConfigResponseFromServerEvent, self, self.OnModConfigResponseFromServerEvent)  # 清除引用

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(alertConst.ModName, alertConst.alertUIName, alertConst.alertUIClsPath, alertConst.alertUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(alertConst.ModName, alertConst.alertUIName, {"isHud": 1})
		self.mAlertUINode = clientApi.GetUI(alertConst.ModName, alertConst.alertUIName)  # 存储UI类对象
		if self.mAlertUINode:
			# UI成功创建
			self.mAlertUINode.InitScreen()  # 执行一些该Mod的UI创建成功后的逻辑
		else:
			print '==== %s ====' % 'create UI: %s failed' % alertConst.alertUIScreenDef

		data = self.CreateEventData()
		data["entityId"] = self.mLocalPlayerId
		self.NotifyToServer(alertConst.ClientUiInitFinished, data)

	def OnModConfigResponseFromServerEvent(self, modConfig):
		self.modConfig = modConfig
		self.mDefaultShowTime = self.modConfig["default_show_time"]
		self.mXRatio = self.modConfig["default_xratio"]
		self.mYRatio = self.modConfig["default_yratio"]

	def Alert(self, text, seconds=None, xratio=None, yratio=None, priority=-1):
		"""
		提供一个函数供外部调用
		用于调用客户端的提示文本UI弹出并显示一些提示文字于指定的位置
		:param text: 提示文本字符串
		:param seconds: 需要停留的秒数
		:param xratio: 文本框中心点于屏幕横轴方向的偏移百分比，取值为0到1间的小数
		:param yratio: 文本框中心点于屏幕纵轴方向的偏移百分比，取值为0到1间的小数
		:param priority: 显示优先级
		"""
		seconds = seconds if seconds != None else self.mDefaultShowTime
		xratio = xratio if xratio != None else self.mXRatio
		yratio = yratio if yratio != None else self.mYRatio
		if isinstance(seconds, int) and seconds > 0:
			self.OnNewAlert({
				'text': text,
				'seconds': seconds,
				'xratio': xratio,
				'yratio': yratio,
				'priority': priority
			})

	def OnNewAlert(self, alert):
		if isinstance(alert['seconds'], int) and alert['seconds'] > 0:  # 验证该次推送下来的消息非“无用功”
			task = MyAlert(alert['text'], alert['seconds'], alert['xratio'], alert['yratio'])
			if alert['priority'] < 0:
				# 优先级小于0，覆盖显示
				self.mTaskQueue.replace(task, alert['priority'])
			else:
				self.mTaskQueue.push(task, alert['priority'])  # 创建并存储封装的弹出提示任务对象供UI类的tick中获取
