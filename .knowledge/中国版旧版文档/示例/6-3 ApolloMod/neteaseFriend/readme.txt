插件介绍：
该服务器Mod隶属于“好友”插件。
该插件实现了玩家之间的好友关系以及基本的聊天功能。具体包含以下功能：
（1）玩家的搜索功能，包括名字的搜索和附近玩家的搜索
（2）玩家的关系管理功能，包括增删好友和黑名单功能，申请和删除好友申请的功能
（3）好友之间的聊天功能
（4）同玩一个网络服的好友，在游戏中会自动成为好友


插件构成：
目前“好友插件”包括以下mod
（1）neteaseFriend:部署大厅服或者游戏服
（2）neteaseFriendService:部署功能服

数据库:
-mysql


使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseFriendService中）
（2）在部署配置中，将neteaseFriend添加至需要的大厅服或者游戏服的mods列表中；
（3）在部署配置中，将neteaseFriendService添加至功能服的mods列表中；
（4）部署并启动服务器后，即可使用好友插件

插件api
（1）增加好友
函数：OnADD
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":0, "message": "成功"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "friendUid":12343, #目标玩家ID
    }
    neteaseFriendServiceSystem.OnADD(data, callback)
（2）删除好友
函数：OnDEL
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":0, "message": "成功"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "friendUid":12343, #目标玩家ID
    }
    neteaseFriendServiceSystem.OnDEL(data, callback)
（3）拉黑好友
函数：OnBLACK
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":0, "message": "成功"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "friendUid":12343, #目标玩家ID
    }
    neteaseFriendServiceSystem.OnBLACK(data, callback)
（4）判断玩家是否好友
函数：OnIsFriend
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":7, "message": "是好友!"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "friendUid":12343, #目标玩家ID
    }
    neteaseFriendServiceSystem.OnIsFriend(data, callback)
（5）给某个玩家发消息
函数：OnCHAT
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)，具体消息内容(message)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":0, "message": "成功"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "friendUid":12343, #目标玩家ID
         "message":"你好"
    }
    neteaseFriendServiceSystem.OnCHAT(data, callback)
（6）打开好友界面
函数：OpenFriendListUI
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)
示例:
    import server.extraServerApi as serverApi
    neteaseFriendSystem = serverApi.GetSystem("neteaseFriend", "neteaseFriendDev")
    data = {
         "selfUid":12343, #传入玩家ID
    }
    neteaseFriendSystem.OpenFriendListUI(data)
（7）修改玩家头像
函数：OnChangeHead
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)，玩家头像地址(head_image)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息
示例:
    def callback(args):
        print args#{"code":0, "message": "成功"}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
         "head_image":"textures/ui/netease_friend/img01@3x" #目标玩家ID
    }
    neteaseFriendServiceSystem.OnChangeHead(data, callback)

（8）查找好友列表
函数：OnGetFriends
参数：
    args：dict，包括的字段有传入玩家ID(selfUid)
    callback:回调函数，参数是dict，返回本次操作成功或者失败的信息,friendsList字段代表着返回的好友uid列表
示例:
    def callback(args):
        print args#{"code":0, "message": "成功", "friendsList":[1,2,3]}
    import server.extraServiceApi as serviceApi
    neteaseFriendServiceSystem = serviceApi.GetSystem("neteaseFriend", "neteaseFriendService")
    data = {
         "selfUid":12343, #传入玩家ID
    }
    neteaseFriendServiceSystem.OnGetFriends(data, callback)

（9）判断玩家是否打开好友界面客户端接口
函数：GetFriendListUIisShow
参数：
	无
示例：
	import client.extraClientApi as extraClientApi
	_clientModSystem = extraClientApi.GetSystem("neteaseFriend", "neteaseFriendBehavior")
	flag = _clientModSystem.GetFriendListUIisShow()
	print flag

（10）创建临时聊天
函数：CreateTempChat
参数：
	args：dict，包括的字段有传入玩家ID(selfUid)，目标玩家ID(friendUid)
示例：
	import server.extraServerApi as serverApi
	neteaseFriendSystem = serverApi.GetSystem("neteaseFriend", "neteaseFriendDev")
	data = {
		"selfUid":12343, #传入玩家ID
		"friendUid":12343, #目标玩家ID
	}
	neteaseFriendSystem.CreateTempChat(data)
	
插件事件:
（1）NewChatOrApplyEvent
ListenForEvent("neteaseFriend", "neteaseFriendBehavior", 'NewChatOrApplyEvent',instance,func)
适用服务器：lobby、game的客户端
命名空间：namespace = 'neteaseFriend',systemname = 'neteaseFriendBehavior'
描述：聊天消息或者好友请求到来触发的event
参数：
    fromUid: int,来源玩家id
    type:str,类型，"chat"聊天，"request"申请
（2）ServiceAcceptFriendBroadCastEvent
ListenForEvent("neteaseFriend", "neteaseFriendService", 'ServiceAcceptFriendBroadCastEvent',instance,func)
适用服务器：service
命名空间：namespace = 'neteaseFriend',systemname = 'neteaseFriendService'
描述：接受好友申请时触发的事件
参数：
    selfUid: int,操作者的Uid
    friendUid: int,被接受者的Uid
（3）ServiceRefuseFriendBroadCastEvent
ListenForEvent("neteaseFriend", "neteaseFriendService", 'ServiceRefuseFriendBroadCastEvent',instance,func)
适用服务器：service
命名空间：namespace = 'neteaseFriend',systemname = 'neteaseFriendService'
描述：拒绝好友申请时触发的事件
参数：
    selfUid: int,操作者的Uid
    friendUid: int,被拒绝者的Uid

更新列表：

1.0.0版本：
初始版本
1.0.1版本:	service新增接口OnGetFriends，用于获取好友列表
1.0.2版本:	新增PVP插件的支持
1.0.3版本:	新增接收到好友信息或者申请时回调，判断玩家是否打开好友界面客户端接口
1.0.4版本:	修复UI显示的一些问题
1.0.5版本:	修复NewChatOrApplyEvent事件新来聊天不能触发的bug
1.0.6版本:	新增同意、拒绝好友申请回调
1.0.7版本：
补充代码注释
按照新的插件标准，重新实现了领地界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题
（3）插件UI使用的图片文件尺寸过大影响界面加载速度和占用client内存的问题
1.0.8版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.9版本：
删除mod.json中gameId和gameKey配置，服主可以在MCStudio中配置，配置方法：服务器配置-->更多-->游戏ID，gameKey会自动生成。服主可以从服务器公共配置中获取对应配置内容，具体可以参看【GetCommonConfig】接口
1.0.10版本：
提供UI工程
1.0.11版本：
使用官方接口GetUserFriend获取好友列表，去除isTestServer配置