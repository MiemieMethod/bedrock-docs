# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
class UIDef:
	MixedBoardScreen = "MixedBoardScreen"

UIData = {
	UIDef.MixedBoardScreen : {
		"cls":"neteaseMixedBoardScript.ui.netease_mixedboard_screen.MixedBoardScreen",
		"screen":"netease_mixedboard_screen.main",
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
		"isHud":1
	}
}