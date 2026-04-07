# -*- coding: utf-8 -*-
import logout
from common.mod import Mod
import server.extraServerApi as serverApi

'''
monitor监控的基础mod，必须保留！！！
monitor监控的基础mod，必须保留！！！
monitor监控的基础mod，必须保留！！！
'''
@Mod.Binding(name = "neteaseMonitor", version = "2.0")
class MonitorMod(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		import netgame_api
		enabled = False
		common_config = netgame_api.get_common_config()
		influx_config = common_config.get("influxdb", {})
		if influx_config:
			enabled = influx_config.get("enabled", False)
		if enabled is True:
			logout.info('----- neteaseMonitor init')
			self.server = serverApi.RegisterSystem("Minecraft", "MonitorServer", "neteaseMonitor.monitor.Monitor")
		else:
			logout.info('----- no config, neteaseMonitor disabled')

	@Mod.DestroyServer()
	def destroyServer(self):
		logout.info('----- neteaseMonitor destroy')
