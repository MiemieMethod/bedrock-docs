# -*- coding: utf-8 -*-
import neteaseRoundScript.roundConst as roundConst

# --------------------------------------------------------------------------------------------------------------------------------------
# 战斗场景初始化
# 参战角色站位
centerX, centerY, centerZ = 0, 0, -14
R = 5
r = 4
R1 = 3
r1 = 5
LeftSideToPos = {
	roundConst.BattlePos.StandPos1: (centerX-R, centerY, centerZ+R),
	roundConst.BattlePos.StandPos2: (centerX-R-r, centerY, centerZ+R-r),
	roundConst.BattlePos.StandPos3: (centerX-R+r, centerY, centerZ+R+r),
	roundConst.BattlePos.StandPos4: (centerX-R-r, centerY, centerZ+R),
	roundConst.BattlePos.StandPos5: (centerX-R, centerY, centerZ+R+r),
}
RightSideToPos = {
	roundConst.BattlePos.StandPos1: (centerX+R1, centerY, centerZ-R1+r1*0.5),
	roundConst.BattlePos.StandPos2: (centerX+R1+r1, centerY, centerZ-R1+r1),
	roundConst.BattlePos.StandPos3: (centerX+R1-r1, centerY, centerZ-R1-r1),
	roundConst.BattlePos.StandPos4: (centerX+R1+r1, centerY, centerZ-R1),
	roundConst.BattlePos.StandPos5: (centerX+R1, centerY, centerZ-R1-r1),
}
# 参战角色面向
RotAxis = (0.0, 1.0, 0.0)
LeftDegreeAngle = 135
RightDegreeAngle = -45
# 角色血条偏移
LeftSideToHeadUI = {
	roundConst.BattlePos.StandPos1: (0.5, 3.2, 0),
	roundConst.BattlePos.StandPos2: (0.5, 3.2, 0),
	roundConst.BattlePos.StandPos3: (0.1, 3.2, 0),
	roundConst.BattlePos.StandPos4: (0.5, 3.2, 0),
	roundConst.BattlePos.StandPos5: (0.5, 3.2, 0),
}
RightSideToHeadUI = {
	roundConst.BattlePos.StandPos1: (0.2, 3.2, 0),
	roundConst.BattlePos.StandPos2: (0.2, 3.2, 0),
	roundConst.BattlePos.StandPos3: (0.0, 3.2, 0),
	roundConst.BattlePos.StandPos4: (0.2, 3.2, 0),
	roundConst.BattlePos.StandPos5: (0.0, 3.2, 0),
}
# --------------------------------------------------------------------------------------------------------------------------------------
# 特效绑定
EffectConfig = {
	"netease_round_guanghuan": {
		"style": "sfx",
		"path": "effects/netease_round_guanghuan.json",
		"pos": (0, 0, 0),
		"rot": (0, 0, 0),
		"bone": "root",
	},
	"netease_round_guanghuan_lizi": {
		"style": "particle",
		"path": "effects/netease_round_guanghuan_lizi.json",
		"pos": (0, 0, 0),
		"rot": (0, 0, 0),
		"bone": "root",
	},
	"netease_round_guanghuan_big": {
		"style": "sfx",
		"path": "effects/netease_round_guanghuan.json",
		"pos": (0, 0, 0),
		"rot": (0, 0, 0),
		"scale": (2.0, 2.0, 2.0),
		"bone": "root",
	},
	"netease_round_guanghuan_lizi_big": {
		"style": "particle",
		"path": "effects/netease_round_guanghuan_lizi.json",
		"pos": (0, 0, 0),
		"rot": (0, 0, 0),
		"bone": "root",
	},
	"netease_round_shilaimu": {
		"style": "model",
		"model": "netease_round_shilaimu",
		"animate": "",
		"pos": (0, 0, 0),
		"rot": (0, 0, 0),
		"bone": "root",
	},
}
# --------------------------------------------------------------------------------------------------------------------------------------
# 模型动画
ModelAnimateToName = {
	"netease_round_jmm": {
		"stand": "netease_round_jmm_idle",
		"die": "netease_round_jmm_die",
		"attack": "netease_round_jmm_hit",
		"skill1": "netease_round_jmm_skill1",
		"skill2": "netease_round_jmm_skill2",
	},
	"netease_round_xn": {
		"stand": "netease_round_xn_idle",
		"die": "netease_round_xn_die",
		"skill1": "netease_round_xn_skill1",
		"skill2": "netease_round_xn_skill2",
	},
	"netease_round_shilaimu": {
		"jump": "qd_shilaimu_jump",
	},
	"v_unvisible_bind": {
		"stand": "idle",
	}
}

def GetModelAnimate(modelName, animate):
	config = ModelAnimateToName.get(modelName, {})
	return config.get(animate, "")
	