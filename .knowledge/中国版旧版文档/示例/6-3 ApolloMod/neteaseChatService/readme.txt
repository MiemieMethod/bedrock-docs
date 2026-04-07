插件介绍：
聊天插件，使用了富文本实现了一个简易的网络服聊天窗口，玩家名称可以点击，点击后弹出一个按钮列表，已经实现的有“私聊”、“加为好友”与“加入黑名单”三个功能，
需要更多按钮可于mod.json中配置

****聊天输入框使用说明（必读）:
1. 当一个玩家处于一个队伍时（依赖队伍插件），于聊天框输入"/[team]"（只能打这个），即可发送“邀请大家一起加入队伍【申请入队】”字样的超链接文本，其他玩家点击该文本即可向该队伍发送入队申请
2. 当一个玩家需要展示自己背包格子中某个道具时（依赖物品面板插件），于聊天框输入带有"/[item 33]"（包含此段即可，item空格后面的数字取值必须为0-35），如“大家快来看看我的/[item 3]”，就会将玩家背包格子中第三格子的物品发送，最终显示为“大家快来看看我的[钻石剑]”超链接文本，点击方括号中的超链接即可展示该道具的属性

插件构成：
目前“聊天”插件包含以下Mod：
- neteaseChat：部署于大厅服或游戏服
- neteaseChatService：部署于功能服

使用步骤：
（1）在部署配置中，将neteaseChat添加至需要的大厅服或者游戏服的mods列表中
（2）在部署配置中，将neteaseChatService添加至需要的功能服的mods列表中

插件api：
（1）打开大聊天输入窗口
函数：ShowFullChatPane(show)
参数：
    show: True or False
示例：
    import client.extraClientApi as clientApi
    chatSystem = clientApi.GetSystem("neteaseChat", "neteaseChatBehavior")
    chatSystem.ShowFullChatPane(True)  # 开启，False为关闭
（2）关闭左侧聊天滚动小窗口
函数：ShowSideChatPane(show)
参数：
    show: True or False
示例：
    import client.extraClientApi as clientApi
    chatSystem = clientApi.GetSystem("neteaseChat", "neteaseChatBehavior")
    chatSystem.ShowSideChatPane(False)  # 关闭，True为开启

插件事件:
（1）ChatUICloseEvent
ListenForEvent("neteaseChat", "neteaseChatBehavior", 'ChatUICloseEvent',instance,func)
适用服务器：lobby、game的客户端
命名空间：namespace = 'neteaseChat',systemname = 'neteaseChatBehavior'
描述：聊天UI关闭的事件event
参数：无
示例:
    self.ListenForEvent("neteaseChat", "neteaseChatBehavior", "ChatUICloseEvent", self, self.test)
    def test(self, args):
        pass
（2）ChatClickExBtnEvent
ListenForEvent('neteaseChat', 'neteaseChatBehavior', 'ChatClickExBtnEvent', instance, func)
适用服务器：lobby、game的客户端
命名空间：namespace = 'neteaseChat',systemname = 'neteaseChatBehavior'
描述：玩家点击了额外配置按钮事件
参数：
    idx: 被点击按钮的序号，对应额外配置按钮列表的下标号
    cfg: 该按钮mod.json中的配置，是个字典
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseChat', 'neteaseChatBehavior', 'ChatClickExBtnEvent', self, self.OnChatClickExBtn)

    def OnChatClickExBtn(self, data):
        print 'OnChatClickExBtn', data
        cfg = data["cfg"]
        idx = data["idx"]
        print '玩家点击了额外配置按钮中的 {} 号按钮且该按钮的配置字典为 {}'.format(idx, cfg)

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
新增聊天UI关闭的事件event
1.0.2版本：
新增和组队插件的关联功能
1.0.3版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.4版本：
优化插件readme文档描述
1.0.5版本：
聊天框不显示聊天文字bug修复