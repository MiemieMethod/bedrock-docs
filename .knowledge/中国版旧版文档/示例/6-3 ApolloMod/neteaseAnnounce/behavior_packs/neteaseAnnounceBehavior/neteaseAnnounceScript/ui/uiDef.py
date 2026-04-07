# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi

class UIDef:
	UILogin = "noticeUi"
	UIFloating = "carouselUI"
	UIMail = "mailUi"
	UIDesk = "mailbtnUi"

UIData = {
	UIDef.UILogin : {
		"cls":"neteaseAnnounceScript.ui.netease_announce_noticeUi.LoginPopupScreen",
		"screen":"netease_announce_noticeUi.main",
		"isHud":0,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
	UIDef.UIMail : {
		"cls":"neteaseAnnounceScript.ui.netease_announce_mailUi.MailScreen",
		"screen":"netease_announce_mailUi.main",
		"isHud":0,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIDesk : {
		"cls":"neteaseAnnounceScript.ui.netease_announce_mailbtnUi.MailBtnScreen",
		"screen":"netease_announce_mailbtnUi.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.Desk,
	},
	UIDef.UIFloating : {
		"cls":"neteaseAnnounceScript.ui.netease_announce_carouselUI.FloatingWindowScreen",
		"screen":"netease_announce_carouselUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.DeskFloat,
	},
}
