# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi

class UIDef:
	UIResidenceApply = "ResidenceApplyUI"
	UIResidenceGive = "ResidenceGiveUI"
	UIResidenceManage = "ResidenceManageUI"
	UIResidenceMy = "ResidenceMyUI"
	UIResidenceTransfer = "ResidenceTransferUI"
	
UIData = {
	UIDef.UIResidenceApply: {
		"cls": "neteaseResidenceScript.ui.netease_residence_applyUI.ResidenceApplyUIScreen",
		"screen": "netease_residence_applyUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIResidenceGive: {
		"cls": "neteaseResidenceScript.ui.netease_residence_giveUI.ResidenceGiveUIScreen",
		"screen": "netease_residence_giveUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIResidenceManage: {
		"cls": "neteaseResidenceScript.ui.netease_residence_managerUI.ResidenceManageUIScreen",
		"screen": "netease_residence_managerUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIResidenceMy: {
		"cls": "neteaseResidenceScript.ui.netease_residence_myUI.ResidenceMyUIScreen",
		"screen": "netease_residence_myUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIResidenceTransfer: {
		"cls": "neteaseResidenceScript.ui.netease_residence_transferUI.ResidenceTransferUIScreen",
		"screen": "netease_residence_transferUI.main",
		"isHud": 1,
		"layer": extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	}
	
}