# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
class UIDef:
	InputBoardScreen = "InputBoardScreen"

UIData = {
	UIDef.InputBoardScreen : {
		"cls":"neteaseInputBoardScript.ui.netease_inputboard_screen.InputBoardScreen",
		"screen":"netease_inputboard_screen.main",
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
		"isHud":1
	}
}