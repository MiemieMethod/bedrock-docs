# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi

class UIDef:
	UIBattleControl = "UIBattleControl"
	UIBattleStart = "UIBattleStart"
	UIBattleWin = "UIBattleWin"
	UIBattleLose = "UIBattleLose"

UIData = {
	UIDef.UIBattleControl : {
		"cls":"neteaseRoundScript.ui.netease_roundUI.BattleControlScreen",
		"screen":"netease_roundUI.main",
		"isHud":1,
		"layer":clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIBattleStart : {
		"cls":"neteaseRoundScript.ui.netease_round_beginUI.BattleStartScreen",
		"screen":"netease_round_beginUI.main",
		"isHud":1,
		"layer":clientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
	UIDef.UIBattleWin : {
		"cls":"neteaseRoundScript.ui.netease_round_victoryUi.BattleWinScreen",
		"screen":"netease_round_victoryUi.main",
		"isHud":1,
		"layer":clientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
	UIDef.UIBattleLose : {
		"cls":"neteaseRoundScript.ui.netease_round_loseUi.BattleLoseScreen",
		"screen":"netease_round_loseUi.main",
		"isHud":1,
		"layer":clientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
}
