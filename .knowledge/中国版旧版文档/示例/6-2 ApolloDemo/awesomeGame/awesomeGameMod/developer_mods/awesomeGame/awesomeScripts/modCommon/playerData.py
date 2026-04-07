# -*- coding: utf-8 -*-
import time
class PlayerData(object):
	DEFAULT_VALUE = {
		'_id':-1,
		'nickname': '',
		'login_time':0
	}

	def initPlayer(self, player_id, info):
		for key,default in PlayerData.DEFAULT_VALUE.iteritems():
			v = info.get(key, default)
			setattr(self, key, v)
		self.player_id = player_id

	@property
	def playerId(self):
		return self.player_id

	@property
	def uid(self):
		return self._id
	
	@staticmethod
	def getNewPlayerInfo(uid, nickname):
		info = {}
		for key,default in PlayerData.DEFAULT_VALUE.iteritems():
			info[key] = default
		info['_id'] = uid
		info['nickname'] = nickname
		info['login_time'] = int(time.time())
		return info

	def refreshLoginTime(self):
		self.login_time = int(time.time())

	def toSaveDict(self):
		info = {}
		for key, default in PlayerData.DEFAULT_VALUE.iteritems():
			value = getattr(self, key, default)
			info[key] = value
		return info