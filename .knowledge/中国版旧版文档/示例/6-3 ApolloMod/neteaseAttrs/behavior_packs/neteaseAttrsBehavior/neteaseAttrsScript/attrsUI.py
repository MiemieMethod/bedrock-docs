# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class AttrsScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init AttrsScreen'

		self.m_empty = '/empty'
		self.m_bg = '/bg'
		self.m_name = '/bg/name'
		self.m_pinzhi = '/bg/pinzhi'
		self.m_quality = '/bg/pinzhi/quality'
		self.m_part = '/bg/pinzhi/part'
		self.m_desc = '/bg/desc'
		self.m_descs = [self.m_desc]
		self.m_naijiu = '/bg/naijiu'
		self.m_durability = '/bg/naijiu/durability'
		self.m_value = '/bg/naijiu/value'
		self.m_shuxing = '/bg/shuxing'
		self.m_shuxings = [self.m_shuxing]
		self.m_attr = '{}/attr'
		self.m_attrv = '{}/attrv'
		self.m_baoshi = '/bg/baoshi'
		self.m_baoshis = [self.m_baoshi]
		self.m_fumo = '/bg/fumo'
		self.m_fumos = [self.m_fumo]

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'AttrsScreen Create'

		self.AddTouchEventHandler(self.m_empty, self.on_touch_btn_empty)

		self.m_bg_w = self.GetSize(self.m_bg)[0]
		self.m_pinzhi_pos = self.GetPosition(self.m_pinzhi)
		self.m_desc_pos = self.GetPosition(self.m_desc)
		self.m_desc_h = self.GetSize(self.m_desc)[1]
		self.m_naijiu_pos = self.GetPosition(self.m_naijiu)
		self.m_shuxing_pos = self.GetPosition(self.m_shuxing)
		self.m_shuxing_h = self.GetSize(self.m_shuxing)[1]
		self.m_baoshi_pos = self.GetPosition(self.m_baoshi)
		self.m_fumo_pos = self.GetPosition(self.m_fumo)

	def InitScreen(self):
		print '==== %s ====' % 'AttrsScreen Init'
		self.SetVisible(self.m_bg, False)
		self.SetVisible(self.m_empty, False)

	def on_touch_btn_empty(self, kws):
		if kws["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetVisible(self.m_bg, False)
			self.SetVisible(self.m_empty, False)

	def detail(self, detail, x, y):
		self.SetText(self.m_name, detail['name'])

		pinzhi_offset = self.m_pinzhi_pos[1] - self.m_desc_pos[1]
		if 'pinzhi' in detail:
			pinzhi_offset = 0
			self.SetVisible(self.m_pinzhi, True)
			self.SetText(self.m_quality, detail['pinzhi'][0])
			self.SetText(self.m_part, detail['pinzhi'][1])
		else:
			self.SetVisible(self.m_pinzhi, False)

		desc_offset = self.m_desc_pos[1] - self.m_naijiu_pos[1]
		if 'desc' in detail:
			demand = len(detail['desc'])
			total = len(self.m_descs)
			if demand > total:
				for i in xrange(total, demand):
					s = 'desc{}'.format(i)
					self.Clone(self.m_desc, self.m_bg, s)
					self.m_descs.append(self.m_bg + '/{}'.format(s))
					self.SetPosition(self.m_descs[-1], (self.m_desc_pos[0], self.m_desc_pos[1] + self.m_desc_h * i))
			desc_offset = self.m_desc_h * (demand - 1)
			for i in xrange(len(self.m_descs)):
				if i < demand:
					self.SetText(self.m_descs[i], detail['desc'][i])
					self.SetPosition(
						self.m_descs[i], (self.m_desc_pos[0], self.m_desc_pos[1] + pinzhi_offset + self.m_desc_h * i))
				self.SetVisible(self.m_descs[i], i < demand)
		else:
			for p in self.m_descs:
				self.SetVisible(p, False)

		naijiu_offset = self.m_naijiu_pos[1] - self.m_shuxing_pos[1]
		if 'naijiu' in detail:
			naijiu_offset = 0
			self.SetVisible(self.m_naijiu, True)
			self.SetText(self.m_durability, detail['naijiu'][0])
			self.SetText(self.m_value, detail['naijiu'][1])
			self.SetPosition(self.m_naijiu, (self.m_naijiu_pos[0], self.m_naijiu_pos[1] + pinzhi_offset + desc_offset))
		else:
			self.SetVisible(self.m_naijiu, False)

		shuxing_offset = self.m_shuxing_pos[1] - self.m_baoshi_pos[1]
		if 'shuxing' in detail:
			demand = len(detail['shuxing'])
			total = len(self.m_shuxings)
			if demand > total:
				for i in xrange(total, demand):
					s = 'shuxing{}'.format(i)
					self.Clone(self.m_shuxing, self.m_bg, s)
					self.m_shuxings.append(self.m_bg + '/{}'.format(s))
					self.SetPosition(
						self.m_shuxings[-1], (self.m_shuxing_pos[0], self.m_shuxing_pos[1] + self.m_shuxing_h * i))
			shuxing_offset = self.m_shuxing_h * (demand - 1)
			for i in xrange(len(self.m_shuxings)):
				if i < demand:
					self.SetText(self.m_attr.format(self.m_shuxings[i]), detail['shuxing'][i][0])
					self.SetText(self.m_attrv.format(self.m_shuxings[i]), detail['shuxing'][i][1])
					self.SetPosition(
						self.m_shuxings[i], (
							self.m_shuxing_pos[0],
							self.m_shuxing_pos[1] + pinzhi_offset + desc_offset + naijiu_offset + self.m_shuxing_h * i
						)
					)
				self.SetVisible(self.m_shuxings[i], i < demand)
		else:
			for p in self.m_shuxings:
				self.SetVisible(p, False)

		baoshi_offset = self.m_baoshi_pos[1] - self.m_fumo_pos[1]
		if 'baoshi' in detail:
			demand = len(detail['baoshi'])
			total = len(self.m_baoshis)
			if demand > total:
				for i in xrange(total, demand):
					s = 'baoshi{}'.format(i)
					self.Clone(self.m_baoshi, self.m_bg, s)
					self.m_baoshis.append(self.m_bg + '/{}'.format(s))
					self.SetPosition(
						self.m_baoshis[-1], (self.m_baoshi_pos[0], self.m_baoshi_pos[1] + self.m_shuxing_h * i))
			baoshi_offset = self.m_shuxing_h * (demand - 1)
			for i in xrange(len(self.m_baoshis)):
				if i < demand:
					self.SetText(self.m_attr.format(self.m_baoshis[i]), detail['baoshi'][i][0])
					self.SetText(self.m_attrv.format(self.m_baoshis[i]), detail['baoshi'][i][1])
					self.SetPosition(
						self.m_baoshis[i], (
							self.m_baoshi_pos[0],
							self.m_baoshi_pos[
								1] + pinzhi_offset + desc_offset + naijiu_offset + shuxing_offset + self.m_shuxing_h * i
						)
					)
				self.SetVisible(self.m_baoshis[i], i < demand)
		else:
			for p in self.m_baoshis:
				self.SetVisible(p, False)

		fumo_offset = -self.m_desc_h
		if 'fumo' in detail:
			demand = len(detail['fumo'])
			total = len(self.m_fumos)
			if demand > total:
				for i in xrange(total, demand):
					s = 'fumo{}'.format(i)
					self.Clone(self.m_fumo, self.m_bg, s)
					self.m_fumos.append(self.m_bg + '/{}'.format(s))
					self.SetPosition(self.m_fumos[-1], (self.m_fumo_pos[0], self.m_fumo_pos[1] + self.m_desc_h * i))
			fumo_offset = self.m_desc_h * (demand - 1)
			for i in xrange(len(self.m_fumos)):
				if i < demand:
					self.SetText(self.m_fumos[i], detail['fumo'][i])
					self.SetPosition(
						self.m_fumos[i], (self.m_fumo_pos[0], self.m_fumo_pos[
							1] + pinzhi_offset + desc_offset + naijiu_offset + shuxing_offset + baoshi_offset + self.m_desc_h * i))
				self.SetVisible(self.m_fumos[i], i < demand)
		else:
			for p in self.m_fumos:
				self.SetVisible(p, False)

		self.SetSize(self.m_bg, (
			100.0, 80 + pinzhi_offset + desc_offset + naijiu_offset + shuxing_offset + baoshi_offset + fumo_offset))
		self.SetPosition(self.m_bg, (x, y))
		self.SetVisible(self.m_bg, True)
		self.SetVisible(self.m_empty, True)
