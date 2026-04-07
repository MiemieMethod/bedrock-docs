# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi

class UIDef:
	#UIFriendDesk = "friendDeskUi"
	UIFriendList = "friendListUi"
	UIFriendInvite = "friendInviteUi"
	UIFriendInvitePop = "friendInvitePopUi"
	UIFriendConfirmPop = "friendConfirmPopUi"

UIData = {
	UIDef.UIFriendList : {
		"cls":"neteaseFriendScript.ui.netease_friend_listUI.FriendListScreen",
		"screen":"netease_friend_listUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIFriendInvite : {
		"cls":"neteaseFriendScript.ui.netease_friend_inviteUI.FriendInviteScreen",
		"screen":"netease_friend_inviteUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1,
	},
	UIDef.UIFriendInvitePop : {
		"cls":"neteaseFriendScript.ui.netease_friend_invite_popUI.FriendInvitePopScreen",
		"screen":"netease_friend_invite_popUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv2,
	},
	UIDef.UIFriendConfirmPop : {
		"cls":"neteaseFriendScript.ui.netease_friend_confirmUI.FriendConfirmPopScreen",
		"screen":"netease_friend_confirmUI.main",
		"isHud":1,
		"layer":extraClientApi.GetMinecraftEnum().UiBaseLayer.PopUpModal,
	},
}
