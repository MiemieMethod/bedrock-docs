# -*- coding: utf-8 -*-

from collections import Counter
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class CalcClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)

	def calc(self, p0, p1, p2):
		"""
		计算镶嵌了宝石的装备的战斗属性（依赖battle插件）
		"""
		c = Counter()
		s = clientApi.GetSystem("neteaseBattle", "neteaseJewelBeh")
		if not s:
			return {}
		if p0:
			c.update(s.GetEquipAttrDict(p0['itemName'], p0['auxValue']))
		if p1:
			c.update(s.GetEquipAttrDict(p1['itemName'], p1['auxValue']))
		if p2:
			c.update(s.GetEquipAttrDict(p2['itemName'], p2['auxValue']))
		return dict(c)
