# -*- coding: utf-8 -*-
import neteaseResidenceScript.util as apiUtil
import random


def DrawResidenceBox(minPos, maxPos, effectPath = "effects/line.json", show = True):
	"""
	利用特效拉伸绘制领地的包围盒（基于AABB）
	"""
	print "minPos, maxPos", minPos, maxPos
	x0, y0, z0 = minPos[0], minPos[1], minPos[2]
	x1, y1, z1 = maxPos[0], maxPos[1], maxPos[2]
	x0, y0, z0 = RandomNum(x0, y0, z0)
	x1, y1, z1 = RandomNum(x1, y1, z1)
	scaleX = (x1 - x0) / 2.0
	scaleY = (y1 - y0) / 2.0
	scaleZ = (z1 - z0) / 2.0
	point1 = ((x1 + x0) / 2.0, (y0 + y1) / 2.0, z0)
	point2 = (x0, (y0 + y1) / 2.0, (z1 + z0) / 2.0)
	point3 = ((x1 + x0) / 2.0, y1, (z1 + z0) / 2.0)
	point4 = ((x1 + x0) / 2.0, (y0 + y1) / 2.0, z1)
	point5 = (x1, (y0 + y1) / 2.0, (z1 + z0) / 2.0)
	point6 = ((x1 + x0) / 2.0, y0, (z1 + z0) / 2.0)
	
	frameEntityId1 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point1, (0, 0, 0),
	                                                                        (scaleX, scaleY, 1))
	frameEntityId2 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point2, (0, 90, 0),
	                                                                        (scaleZ, scaleY, 1))
	frameEntityId3 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point3, (90, 0, 0),
	                                                                        (scaleX, scaleZ, 1))
	frameEntityId4 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point4, (0, 0, 0),
	                                                                        (scaleX, scaleY, 1))
	frameEntityId5 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point5, (0, 90, 0),
	                                                                        (scaleZ, scaleY, 1))
	frameEntityId6 = apiUtil.GetClientModSystem().CreateEngineSfxFromEditor(effectPath, point6, (90, 0, 0),
	                                                                        (scaleX, scaleZ, 1))
	
	frameEntityIdList = [frameEntityId1, frameEntityId2, frameEntityId3, frameEntityId4, frameEntityId5, frameEntityId6]
	if show == True:
		for frameEntityId in frameEntityIdList:
			comp = apiUtil.GetClientModSystem().CreateComponent(frameEntityId, "Minecraft", "frameAniControl")
			comp.Play()  # 播放序列帧
	
	return [frameEntityId1, frameEntityId2, frameEntityId3, frameEntityId4, frameEntityId5, frameEntityId6]


def RandomNum(x, y, z):
	#add = random.randint(0, 1)
	delta = 0.5
	# if add == 0:
	# 	x = x - delta
	# 	y = y - delta
	# 	z = z - delta
	# else:
	x = x + delta
	y = y + delta
	z = z + delta
	return x, y, z


def StopResidenceBox(frameEntityIdList):
	for frameEntityId in frameEntityIdList:
		comp = apiUtil.GetClientModSystem().CreateComponent(frameEntityId, "Minecraft", "frameAniControl")
		comp.Stop()  # 停止序列帧


def SetSfxPos(frameEntityId, pos):
	"""
	设置序列帧位置
	:param frameEntityId:
	:param tuple pos:
	:return:
	"""
	comp = apiUtil.GetClientModSystem().CreateComponent(frameEntityId, "Minecraft", "frameAniTrans")
	comp.SetPos(pos)


def SetSfxRot(frameEntityId, rot):
	"""
	设置序列帧旋转角度
	:param frameEntityId:
	:param tuple rot:
	:return:
	"""
	comp = apiUtil.GetClientModSystem().CreateComponent(frameEntityId, "Minecraft", "frameAniTrans")
	comp.SetRot(rot)
