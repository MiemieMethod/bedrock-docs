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
	"low" : 48,
	"mid" : 12,
	"high" : 5
}
	
def typeof(variate):
	type= "None"
	if isinstance(variate,int):
		type = "int"
	elif isinstance(variate,str):
		type = "str"
	elif isinstance(variate,float):
		type = "float"
	elif isinstance(variate,list):
		type = "list"
	elif isinstance(variate,tuple):
		type = "tuple"
	elif isinstance(variate,dict):
		type = "dict"
	elif isinstance(variate,set):
		type = "set"
	return type
	