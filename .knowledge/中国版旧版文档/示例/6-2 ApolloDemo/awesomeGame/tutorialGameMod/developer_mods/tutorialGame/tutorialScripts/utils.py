# -*- coding: utf-8 -*-

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def unicode_convert(input):
	if isinstance(input, dict):
		return {unicode_convert(key): unicode_convert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [unicode_convert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [unicode_convert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input