# -*- coding:utf-8 -*-
import time
_clientModSystem = None

import client.extraClientApi as extraClientApi
from neteaseFriendScript.friendConsts import ModNameSpace, ClientSystemName

def GetClientModSystem():
	"""
	:return: neteaseFriendScript.neteaseFriendClientSystem.FriendClientSystem
	:rtype: neteaseFriendScript.neteaseFriendClientSystem.FriendClientSystem
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None

def DrawButtonImage(ui, button, image):
	ui.SetSprite("%s/default" % button, "textures/ui/netease_friend/%s" % image)
	ui.SetSprite("%s/hover" % button, "textures/ui/netease_friend/%s" % image)
	ui.SetSprite("%s/pressed" % button, "textures/ui/netease_friend/%s" % image)

def GetTodayStart(now):
	local = time.localtime(now)
	return int(time.mktime((local.tm_year, local.tm_mon, local.tm_mday, 0, 0, 0, 0, 0, 0)))

def GetYesterdayStart(now):
	local = time.localtime(now - 86400)
	return int(time.mktime((local.tm_year, local.tm_mon, local.tm_mday, 0, 0, 0, 0, 0, 0)))

def GetWeekStart(now):
	localNow = time.localtime()
	local = time.localtime(now - 86400*localNow.tm_wday)
	return int(time.mktime((local.tm_year, local.tm_mon, local.tm_mday, 0, 0, 0, 0, 0, 0)))

DayToWeek = {
	0: "星期一",
	1: "星期二",
	2: "星期三",
	3: "星期四",
	4: "星期五",
	5: "星期六",
	6: "星期日",
}
def GetTalkTimeFormat(timestamp, todayS, yesterdayS, weekS, yearNow):
	local = time.localtime(timestamp)
	if timestamp >= todayS:
		return "%02d:%02d:%02d" % (local.tm_hour, local.tm_min, local.tm_sec)
	if timestamp >= yesterdayS:
		return "昨天 %02d:%02d" % (local.tm_hour, local.tm_min)
	if timestamp >= weekS:
		return "%s %02d:%02d" % (DayToWeek[local.tm_wday], local.tm_hour, local.tm_min)
	if yearNow == local.tm_year:
		return "%d月%d日 %02d:%02d" % (local.tm_mon, local.tm_mday, local.tm_hour, local.tm_min)
	return "%04d年%d月%d日 %02d:%02d" % (local.tm_year, local.tm_mon, local.tm_mday, local.tm_hour, local.tm_min)

def GetGbkLength(content):
	if isinstance(content, unicode):
		content = content.encode("gbk")
	else:
		content = content.decode("utf-8").encode("gbk")
	return len(content)

def GetUnicodeLength(content):
	if not isinstance(content, unicode):
		content = content.decode("utf-8")
	return len(content)

def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [UnicodeConvert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

def IsWordValidClient(input):
	comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
	return comp.CheckWordsValid(input)

def GetTextViewLength(content):
	gbkLength = GetGbkLength(content)
	unicodeLength = GetUnicodeLength(content)
	chLength = gbkLength - unicodeLength
	enLength = unicodeLength - chLength
	if chLength > 0:
		if enLength > 0: # 中英文混合的时候，中文是2，英文是1
			return chLength * 2 + enLength
		else:	# 纯中文的时候，中文是2
			return chLength * 2
	else:
		if enLength > 0:  # 纯英文的时候，英文是1.5
			return enLength * 1.5
		else:
			return 0
