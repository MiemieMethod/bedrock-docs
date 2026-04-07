# -*- coding: utf-8 -*-
import time
import json

def CheckFormatValue(value, style):
	if style == "int" and type(value) != int:
		return False, "style[int]和value[%s]不匹配" % value
	if style == "float" and type(value) not in (int, float):
		return False, "style[float]和value[%s]不匹配" % value
	return True, ""

def GetFormatValue(value, style):
	if style == "int":
		return int(value)
	elif style == "float":
		return float(value)
	else:
		return None

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
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

def UnpackItemExtra(itemDict):
	extraId = itemDict.get("extraId", "")
	if not extraId:
		return True, {}
	try:
		data = json.loads(extraId)
	except:
		return False, None
	data = UnicodeConvert(data)
	return True, data

def PackItemExtra(data):
	return json.dumps(data, ensure_ascii=False)

def PackDict(_dict):
	return json.dumps(_dict, ensure_ascii=False)

def UnpackDict(_string):
	try:
		_dict = json.loads(_string)
	except:
		return None
	return UnicodeConvert(_dict)

def GetTextLength(input):
	if isinstance(input, unicode):
		return len(input.encode("gbk"))
	else:
		return len(input.decode("utf-8").encode("gbk"))

def CheckInputOverLimit(input, limit):
	if isinstance(input, unicode):
		length = len(input)
	else:
		length = len(input.decode("utf8"))
	return length > limit

def SortById(left, right):
	return cmp(left["_id"], right["_id"])

def SortByIdReverse(left, right):
	return cmp(right["_id"], left["_id"])

def MakeTime(args, key, default):
	value = args.get(key, None)
	if value is None:
		return default
	if type(value) in (int, float):
		return int(value)
	if type(value) in (str,):
		try:
			local = time.strptime(value, "%Y-%m-%d %H:%M:%S")
		except:
			return default
		return int(time.mktime(local))
	return default

ServerSystemInstance = None
ClientSystemInstance = None
def GetServerSystem():
	"""
	返回当前Mod的system对象
	:return: 当前Mod的system对象
	:rtype: neteaseBattleScript.battleServerSystem.BattleServerSystem
	"""
	global ServerSystemInstance
	if not ServerSystemInstance:
		import server.extraServerApi as extraServerApi
		from neteaseBattleScript.battleCommon.battleConsts import ModNameSpace, ServerSystemName
		ServerSystemInstance = extraServerApi.GetSystem(ModNameSpace, ServerSystemName)
	return ServerSystemInstance

def GetClientSystem():
	"""
	返回当前Mod的system对象
	:return: 当前Mod的system对象
	:rtype: neteaseBattleScript.battleClientSystem.BattleClientSystem
	"""
	global ClientSystemInstance
	if not ClientSystemInstance:
		import client.extraClientApi as extraClientApi
		from neteaseBattleScript.battleCommon.battleConsts import ModNameSpace, ClientSystemName
		ClientSystemInstance = extraClientApi.GetSystem(ModNameSpace, ClientSystemName)
	return ClientSystemInstance


