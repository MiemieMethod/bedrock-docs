# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi

class UIDef:
	UIBattle = "battleUi"
	UIDesk = "battleDeskUi"

UIData = {
	UIDef.UIBattle : {
		"cls":"neteaseBattleScript.ui.netease_battle_battleUi.BattleMobScreen",
		"screen":"netease_battle_battleUi.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIDesk : {
		"cls":"neteaseBattleScript.ui.netease_battle_battleDeskUi.BattleDeskScreen",
		"screen":"netease_battle_battleDeskUi.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.Desk,
	}
}
