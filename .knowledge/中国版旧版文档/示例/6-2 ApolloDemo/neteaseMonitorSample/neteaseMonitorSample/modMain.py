# -*- coding: utf-8 -*-
import logout
import time
from common.mod import Mod
import neteaseMonitor.monitor as monitor
import netgame_api

'''
监控mod的示范例子
请一定要包含这个mod，因为这个mod包含了人数监控等基础监控
'''
@Mod.Binding(name = "neteaseMonitorSample", version = "1.0")
class NeteaseMonitorSampleMod(object):
	def __init__(self):
		self.lastGatherTime = int(round(time.time()))
		self.lastTick = 0

	@Mod.InitServer()
	def initServer(self):
		logout.info('----- NeteaseMonitorSampleMod init')
		# 注册监控函数获取器
		monitor.RegisterTaskGetter('NeteaseMonitorSampleGetter', self.NeteaseMonitorSampleGetter)

	@Mod.DestroyServer()
	def destroyServer(self):
		logout.info('----- NeteaseMonitorSampleMod destroy')
		# 注销监控函数获取器
		monitor.UnregisterTaskGetter('NeteaseMonitorSampleGetter')

	def NeteaseMonitorSampleGetter(self):
		'''
		在这里注册所有定时触发的监控函数，函数需要返回 <None> 或者 <Point的列表>
		本例的 TaskGetter，定制了要监控的内容如下：
		1. 获取各服人数
		2. 获取自身的TPS
		'''
		tsks = []
		tsks.append(self.GatherPlayerNum)
		tsks.append(self.GatherTps)
		return tsks

	# 脚本执行tps
	def GatherTps(self, totalTick):
		ps = []
		now = int(round(time.time()))
		if now - self.lastGatherTime == 0:
			tps = 0
		else:
			tps = (totalTick - self.lastTick) / (now - self.lastGatherTime)
		self.lastGatherTime = now
		self.lastTick = totalTick
		ps.append(monitor.Point().measurement('server_tps').field('num', tps))
		return ps

	# 获取在线人数
	def GatherPlayerNum(self, totalTick):
		ps = []
		num = netgame_api.get_online_player_num()
		ps.append(monitor.Point().measurement('server_playernum').field('num', num))
		return ps
