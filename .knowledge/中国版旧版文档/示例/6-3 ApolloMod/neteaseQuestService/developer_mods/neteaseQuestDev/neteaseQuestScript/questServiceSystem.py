# -*- coding: utf-8 -*-

import service.serviceConf as serviceConf
import neteaseQuestScript.questConst as questConst
import server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()


class QuestServiceSystem(ServiceSystem):
	"""
	该mod的service类
	主要逻辑位于questMgr.py
	"""

	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（模块对应的是neteaseQuest）
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(questConst.ModName):
				mgr = self.CreateQuestMgr(moduleName)
				self.mActionMgrs[moduleName] = mgr

	def CreateQuestMgr(self, moduleName):
		from neteaseQuestScript.questMgr import QuestMgr
		return QuestMgr(self, moduleName)

	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		super(QuestServiceSystem, self).Destroy()

	def Update(self):
		pass

	def InitQuestCfg(self):
		return True

	def GetQuestCfg(self):
		return
