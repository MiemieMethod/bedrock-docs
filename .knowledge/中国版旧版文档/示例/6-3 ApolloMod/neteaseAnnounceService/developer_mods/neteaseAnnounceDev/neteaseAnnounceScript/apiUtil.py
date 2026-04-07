# -*- coding: utf-8 -*-
import time

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


