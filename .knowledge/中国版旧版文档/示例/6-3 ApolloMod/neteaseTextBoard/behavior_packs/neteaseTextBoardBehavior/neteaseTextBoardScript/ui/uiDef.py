# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
class UIDef:
	TextBoardScreen = "TextBoardScreen"

UIData = {
	UIDef.TextBoardScreen : {
		"cls":"neteaseTextBoardScript.ui.netease_textboard_screen.TextBoardScreen",
		"screen":"netease_textboard_screen.main",
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.Desk,
		"isHud":1
	}
}