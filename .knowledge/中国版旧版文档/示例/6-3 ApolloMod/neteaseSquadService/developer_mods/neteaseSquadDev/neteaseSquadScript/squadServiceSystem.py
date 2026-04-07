# -*- coding: utf-8 -*-

import service.serviceConf as serviceConf
import logout
import neteaseSquadScript.squadConst as squadConst
import neteaseSquadScript.timermanager as timermanager
import server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()


class SquadServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		self.mSquadMemberCountLimit = 5
		self.mSquadApplicantCountLimit = 5
		self.mSquadRecruitCD = 5
		self.mSquadAssembleCD = 5
		self.mAssembleForbiddenServerKinds = set()
		self.mLeaveForbiddenServerKinds = set()
		self.mServerId2ServerKind = {}
		self.mRecruitmentShowLimit = -1
		self.FillServerKindCfg()
		if not self.InitSquadCfg():
			return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（模块对应的是neteaseSquad）
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(squadConst.ModName):
				mgr = self.CreateSquadMgr(moduleName)
				self.mActionMgrs[moduleName] = mgr

		self.ListenForEvent(
			serviceApi.GetEngineNamespace(),
			serviceApi.GetEngineSystemName(),
			'NetGameCommonConfChangeEvent',
			self, self.OnNetGameCommonConfChange
		)

	def CreateSquadMgr(self, moduleName):
		from neteaseSquadScript.squadMgr import SquadMgr
		return SquadMgr(self, moduleName)

	# service的关闭
	def Destroy(self):
		self.UnListenForEvent(
			serviceApi.GetEngineNamespace(),
			serviceApi.GetEngineSystemName(),
			'NetGameCommonConfChangeEvent',
			self, self.OnNetGameCommonConfChange
		)

		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		super(SquadServiceSystem, self).Destroy()

	def Update(self):
		timermanager.timerManager.tick()

	def OnNetGameCommonConfChange(self, *args):
		self.FillServerKindCfg()

	def FillServerKindCfg(self):
		import service.netgameApi as netServiceApi
		conf = netServiceApi.GetCommonConfig()
		serverlist = conf['serverlist']
		for cfg in serverlist:
			serverId = cfg['serverid']
			if serverId not in self.mServerId2ServerKind or cfg['type'] != self.mServerId2ServerKind[serverId]:
				self.mServerId2ServerKind[serverId] = cfg['type']

	def InitSquadCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseSquadScript")
		if not cfg:
			logout.error("nothing in InitSquadCfg")
		else:
			print 'InitSquadCfg', cfg
			self.mSquadMemberCountLimit = cfg.get('SquadMemberCountLimit')
			if not self.mSquadMemberCountLimit or self.mSquadMemberCountLimit < 1:
				self.mSquadMemberCountLimit = 5
			self.mSquadApplicantCountLimit = cfg.get('SquadApplicantCountLimit')
			if not self.mSquadApplicantCountLimit or self.mSquadApplicantCountLimit < 1:
				self.mSquadApplicantCountLimit = 5
			self.mSquadRecruitCD = cfg.get('SquadRecruitCD')
			if not self.mSquadRecruitCD or self.mSquadRecruitCD < 1:
				self.mSquadRecruitCD = 5
			self.mSquadAssembleCD = cfg.get('SquadAssembleCD')
			if not self.mSquadAssembleCD or self.mSquadAssembleCD < 1:
				self.mSquadAssembleCD = 5
			try:
				self.mAssembleForbiddenServerKinds = set(cfg.get('AssembleForbiddenServerKinds'))
			except:
				self.mAssembleForbiddenServerKinds = set()
			try:
				self.mLeaveForbiddenServerKinds = set(cfg.get('LeaveForbiddenServerKinds'))
			except:
				self.mLeaveForbiddenServerKinds = set()
			self.mRecruitmentShowLimit = cfg.get('RecruitmentShowLimit', -1)
		return True

	def GetSquadCfg(self):
		return self.mSquadMemberCountLimit, self.mSquadApplicantCountLimit, self.mSquadRecruitCD, self.mSquadAssembleCD, self.mRecruitmentShowLimit

	def GetSquadRestrictions(self, serverId):
		restrictions = {}
		if serverId in self.mServerId2ServerKind:
			kind = self.mServerId2ServerKind.get(serverId)
			if kind in self.mAssembleForbiddenServerKinds:
				restrictions['lost'] = 1
			if kind in self.mLeaveForbiddenServerKinds:
				restrictions['trap'] = 1
		return restrictions
