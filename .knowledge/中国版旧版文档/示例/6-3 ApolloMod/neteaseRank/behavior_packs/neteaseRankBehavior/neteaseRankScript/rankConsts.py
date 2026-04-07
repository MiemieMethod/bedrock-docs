# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseRank"
ClientSystemName = "neteaseRankBehavior"
ClientSystemClsPath = "neteaseRankScript.neteaseRankClientSystem.RankClientSystem"
ServerSystemName = "neteaseRankDev"
ServerSystemClsPath = "neteaseRankScript.neteaseRankServerSystem.RankServerSystem"
ServiceSystemName = "neteaseRankService"
ServiceSystemClsPath = "neteaseRankScript.neteaseRankServiceSystem.RankServiceSystem"


class ColDataType:
	dataInt = "int"
	dataStr = "str"
	dataNone = "None"


Refresh_Frequency = {
	"low": 48,
	"mid": 12,
	"high": 5
}


def typeof(variate):
	type = "None"
	if isinstance(variate, int):
		type = "int"
	elif isinstance(variate, str):
		type = "str"
	elif isinstance(variate, float):
		type = "float"
	elif isinstance(variate, list):
		type = "list"
	elif isinstance(variate, tuple):
		type = "tuple"
	elif isinstance(variate, dict):
		type = "dict"
	elif isinstance(variate, set):
		type = "set"
	return type

def CalNextFuncTime():
	'''
	计算距离下一个需要执行函数的时间间隔，单位为秒
	'''
	import datetime
	now_time = datetime.datetime.now()
	# 获取时间
	next_time = now_time + datetime.timedelta(minutes=+1)
	next_year = next_time.date().year
	next_month = next_time.date().month
	next_day = next_time.date().day
	next_hour = next_time.time().hour
	next_minute = next_time.time().minute
	next_second = "00"
	# 获取时间
	next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " " + str(next_hour) + ":" + str(next_minute) + ":00", "%Y-%m-%d %H:%M:%S")
	# 获取距离时间，单位为秒
	timer_start_time = (next_time - now_time).total_seconds()
	return timer_start_time


