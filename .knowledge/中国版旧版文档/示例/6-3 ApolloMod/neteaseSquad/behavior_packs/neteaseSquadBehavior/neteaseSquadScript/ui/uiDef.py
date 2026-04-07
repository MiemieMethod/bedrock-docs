# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
class UIDef:
	UISquadMain = "SquadMainUi"
	UISquadAlert = "SquadAlertUi"
	UISquadApply = "SquadApplyUi"
	UISquadClsBtn = "SquadClsBtnUi"
	UISquadReply = "SquadReplyUi"

UIData = {
	UIDef.UISquadMain : {
		"cls":"neteaseSquadScript.ui.netease_squadUI.SquadMainScreen",
		"screen":"netease_squadUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.Desk,
	},
	UIDef.UISquadAlert: {
		"cls": "neteaseSquadScript.ui.netease_squad_alertUI.SquadAlertScreen",
		"screen": "netease_squad_alertUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
	UIDef.UISquadApply: {
		"cls": "neteaseSquadScript.ui.netease_squad_applyUI.SquadApplyScreen",
		"screen": "netease_squad_applyUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UISquadClsBtn: {
		"cls": "neteaseSquadScript.ui.netease_squad_clsbtnUI.SquadClsBtnScreen",
		"screen": "netease_squad_clsbtnUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.Desk,
	},
	UIDef.UISquadReply: {
		"cls": "neteaseSquadScript.ui.netease_squad_replyUI.SquadReplyScreen",
		"screen": "netease_squad_replyUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	}
}