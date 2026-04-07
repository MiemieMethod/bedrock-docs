# -*- coding: utf-8 -*-

class PlayerData(object):
	def __init__(self, pid, exp=0, level=1):
		super(PlayerData, self).__init__()
		self.pid = pid
		self.exp = exp
		self.level = level
		self.netgame_uid = None
		self.netgame_nickname = None
		self.recent_weapon = None
	
	def update_from_server(self, exp, level):
		self.exp = exp
		self.level = level
	
	def addExp(self, exp):
		self.exp += exp
		while self.exp >= self.getLevelExp():
			if self.level >= 99:
				break
			self.exp -= self.getLevelExp()
			self.addLevel(1)
	
	def addLevel(self, level):
		self.level += level
	
	def getLevelExp(self):
		return self.level * 10
		
	def get_power_string(self):
		return "Lv.%d  %d/%d" % (self.level, self.exp, self.getLevelExp())
		