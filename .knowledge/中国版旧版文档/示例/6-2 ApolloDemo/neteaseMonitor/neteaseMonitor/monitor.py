# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import workerpool
import time
import logout
from influxdb import InfluxDBClient
import netgame_api

TaskGetters = {}
def RegisterTaskGetter(name, func):
	'''
	往 TaskGetters 中注册自己的 TaskGetter function
	开发者应该在 mod 初始化的时候调用这个函数来注册自己的 TaskGetter function
	然后在自己的 TaskGetter function 中定义需要执行的 task 列表
	'''
	global TaskGetters
	if not isinstance(name, basestring):
		logout.error('----- RegisterTaskGetter failed: %s is not basestring'%name)
		return False
	if not callable(func):
		logout.error('----- RegisterTaskGetter failed: %s:%s is not callable'%(name, func))
		return False
	if name in TaskGetters:
		logout.error('----- RegisterTaskGetter failed: %s is already in TaskGetters'%name)
		return False
	else:
		TaskGetters[name] = func
		return True

def UnregisterTaskGetter(name):
	'''
	从 TaskGetters 中注销自己的 TaskGetter function
	应该在 mod 注销的时候做
	'''
	global TaskGetters
	if name in TaskGetters:
		del TaskGetters[name]

def UnregisterAllTaskGetter():
	'''
	Monitor 退出时清空所有任务函数
	'''
	global TaskGetters
	TaskGetters.clear()

# 上传influxdb的一条记录
# 所有上传数据请使用这个类生成
# 例如： return Point().measurement('playernum').tag('server', 'game01').field('num', 0)
class Point(object):
	def __init__(self):
		self.table = ''
		self.tags = {}
		self.fields = {}
		self.user_time = None
	
	def change_time(self, timestamp):
		self.user_time = int(round(timestamp))
		return self

	def measurement(self, measurement):
		# 设置表名
		self.table = measurement
		return self

	def field(self, key, value):
		# 设置列
		if key == 'time':
			logout.error('----- Monitor Point Error: key cannot be `time`')
			return None
		self.fields[key] = value
		return self

	def tag(self, key, value):
		# 设置索引
		if key == 'time':
			logout.error('----- Monitor Point Error: key cannot be `time`')
			return None
		self.tags[key] = value
		return self

	def pack(self, monitor):
		if len(self.table) == 0:
			logout.error('----- Monitor Point Error: measurement empty')
			return None
		if len(self.fields) == 0:
			logout.error('----- Monitor Point Error: fields empty')
			return None
		if self.user_time is None:
			now = int(round(time.time()))
		else:
			now = self.user_time
		self.tag('host', monitor.current_ip)
		self.tag('app_version', monitor.app_version)
		self.tag('type', monitor.type)
		self.tag('serverid', monitor.server_id)
		self.tag('server', monitor.type + '_' + str(monitor.server_id))
		points = dict(measurement=self.table, fields=self.fields, time=now)
		if len(self.tags) > 0:
			points['tags'] = self.tags
		return points

# 监控数据上报
class Monitor(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info('----- Monitor start')
		self.work_pool = workerpool.fork_new_pool(1)
		self.lastTime = int(round(time.time()))
		self.totalTick  = 0
		self.influxdb = None
		self.type = None
		self.current_ip = None
		self.app_version = None
		self.Connect()

		self.tasks = []
		self.taskId = 0#需要执行的task id
		self.packPoints = []

	def Connect(self):
		if self.influxdb is None:
			common_config = netgame_api.get_common_config()
			self.server_id = netgame_api.get_netgame_serverid()
			for server_info in common_config.get("serverlist", {}):
				if server_info.get("serverid") == self.server_id:
					self.app_version = server_info.get("app_version", "")
					self.current_ip = server_info.get("ip", "")
					self.type = server_info.get("type", "")
			if self.type is None or self.current_ip is None or self.app_version is None:
				logout.error('--------serverid is not in netgame_common.json---------')
				return
			influx_config = common_config.get("influxdb", {})
			if influx_config:
				host = influx_config.get("host", "127.0.0.1")
				port = influx_config.get("port", 8086)
				user = influx_config.get("user", "minecraft")
				password = influx_config.get("password", "minecraft")
				database = influx_config.get("database", "mydb")
				self.influxdb = InfluxDBClient(host=host, port=port, username=user, password=password, database=database, timeout=1, retries=2, pool_size=3)
				if self.influxdb is not None:
					logout.info('----- Connect to influxdb successfully!')
			else:
				logout.error('--------influxdb config empty!---------')

	def Destroy(self):
		logout.info('----- Monitor destroy')
		if self.work_pool:
			self.work_pool.finish(timeout=5.0)
			self.work_pool = None
		if self.influxdb:
			self.influxdb.close()
		UnregisterAllTaskGetter()

	def Update(self):
		now = int(round(time.time()))
		self.totalTick += 1
		common_config = netgame_api.get_common_config()
		influx_config = common_config.get("influxdb", {})
		interval = int(influx_config.get("interval", 10))
		if self.taskId or now - self.lastTime >= interval:
			# 每隔一定时间触发，分帧执行
			if not self.taskId:
				self.tasks = []
				self.lastTime = now
				global TaskGetters
				for name, tskGetter in TaskGetters.iteritems():
					tks = tskGetter()
					if isinstance(tks, list):
						self.tasks.extend(tks)
			if self.influxdb is not None:
				if self.taskId >= len(self.tasks):
					self.taskId = 0
					if self.packPoints:
						self.work_pool.emit_order("monitor_sender", self.influxdb.write_points, None, self.packPoints, 's')
					else:
						logout.verbose('----- Monitor Info: no points to write')
					self.packPoints = []
					return
				tsk = self.tasks[self.taskId]
				try:
					ps = tsk(self.totalTick)
				except:
					logout.error("Monitor update traceback.%s" % traceback.format_exc())
					ps = None
				if ps is not None:
					for p in ps:
						data = p.pack(self)
						if data is None:
							continue
						self.packPoints.append(data)
			self.taskId += 1
		if self.work_pool:
			self.work_pool.schedule()
