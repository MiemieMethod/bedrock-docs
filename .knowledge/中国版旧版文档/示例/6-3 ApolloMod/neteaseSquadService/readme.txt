插件介绍：
该服务器Mod隶属于“队伍”插件。
“队伍”插件实现玩家组队功能：
- 队伍：定义并生效游戏中常见的玩家组队系统（部分队伍相关配置于service下的mod.json）

插件构成：
目前“队伍”插件包含以下Mod：
- neteaseSquad：部署于大厅服或游戏服
- neteaseSquadService：部署于功能服

使用步骤：
（1）在部署配置中，将neteaseSquad添加至需要的大厅服或者游戏服的mods列表中
（2）在部署配置中，将neteaseSquadService添加至某一个功能服的mods列表中

插件api：
（1）创建一个队伍
函数：SetupSquad(uid)
说明：以传入uid对应的玩家作为队长创建一个队伍，若传入uid对应的玩家为已组队状态，则不会创建队伍
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.SetupSquad(uid)
（2）解散一个队伍
函数：DissolveSquad(uid)
说明：解散传入uid对应的玩家为队长的队伍，若传入uid对应的玩家非一个队伍的队长，则不会解散队伍
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.DissolveSquad(uid)
（3）将一个玩家踢出队伍
函数：KickSquadPlayer(chief, uid)
说明：从队伍中踢出传入uid对应的玩家，若传入chief对应的玩家非队长，或传入uid对应的玩家与传入chief对应的玩家非同队，则不会踢出玩家
参数：
    chief: 操作者的uid
    uid: 目标玩家的uid
示例：
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.KickSquadPlayer(chief, uid)
（4）向队伍添加一个玩家
函数：SquadAppendPlayer(uid, chief, dealer, cb)
说明：使传入uid对应的玩家加入以传入chief对应的玩家为队长的队伍
参数：
    uid: 目标玩家的uid
    chief: 队长的uid
    dealer: 操作者的uid
    cb: 返回后调用的cb函数
示例：
    # cb = lambda rtn, data: self.do_something("-445201314", dealer, rtn, data)
    import lobbyGame.netgameApi as netgameApi
    dealer = netgameApi.GetPlayerUid("-445201314")
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.SquadAppendPlayer(uid, chief, dealer, lambda rtn, data: self.do_something("-445201314", dealer, rtn, data))

    ...

    def do_something(self, player_id, player_uid, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            print('玩家id player_id : {}'.format(player_id))
            print('玩家id player_uid : {}'.format(player_uid))
            print('返回数据为 data: {}'.format(data))
            if data['code'] == 1:
                print('操作成功')
                print('uid为{}的玩家加入队伍成功'.format(data['entity']['uid']))
            else:
                print('操作失败')
                print('uid为{}的玩家加入队伍失败'.format(data['entity']['uid']))
                print('失败信息为 message: {}'.format(data['message']))
（5）邀请一个玩家加入队伍
函数：SquadInvitePlayer(uid, chief, dealer, cb)
说明：向传入uid对应的玩家发出加入以传入chief对应的玩家为队长的队伍的组队邀请，收到邀请的玩家将弹窗提示
参数：
    uid: 目标玩家的uid
    chief: 队长的uid
    dealer: 操作者的uid
    cb: 返回后调用的cb函数
示例：
    # cb = lambda rtn, data: self.do_something("-445201314", dealer, rtn, data)
    import lobbyGame.netgameApi as netgameApi
    dealer = netgameApi.GetPlayerUid("-445201314")
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.SquadInvitePlayer(uid, chief, dealer, lambda rtn, data: self.do_something("-445201314", dealer, rtn, data))

    ...

    def do_something(self, player_id, player_uid, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            print('玩家id player_id : {}'.format(player_id))
            print('玩家id player_uid : {}'.format(player_uid))
            print('返回数据为 data: {}'.format(data))
            if data['code'] == 1:
                print('操作成功')
                print('返回信息为 message: {}'.format(data['message']))
            else:
                print('操作失败')
                print('失败信息为 message: {}'.format(data['message']))
（6）查询一个玩家所在队伍
函数：CheckPlayerSquad(uid, cb)
说明：获取传入uid对应的玩家所在队伍的信息
参数：
    uid: 玩家的uid
    cb: 返回后调用的cb函数
示例：
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.CheckPlayerSquad(uid, self.do_something)

    ...

    def do_something(self, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print('请求成功')
                squad = data['entity'].get('squad')
                if not squad:
                    print('uid为{}的玩家暂未组队'.format(data['entity']['uid']))
                else:
                    print('队伍数字编号 order: {}'.format(squad['order']))
                    print('队长uid chief: {}'.format(squad['chief']))
                    print('队伍招募信息 label: {}'.format(squad.get('label')))
                    print('队伍成员信息 members: {}'.format(squad['members']))
            else:
                print('请求失败')
                print('失败信息为 message: {}'.format(data['message']))
（7）根据队伍编号获得队伍信息
函数：QuerySquadByOrder(order, cb)
参数：
    order: 队伍数字编号
    cb: 返回后调用的cb函数
示例：
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    order = 4
    squadSystem.QuerySquadByOrder(order, lambda rtn, data: self.do_something(order, rtn, data))  # 获取队伍数字编号为1的队伍信息

    ...

    def do_something(self, order, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print('请求成功')
                squad = data['entity'].get('squad')
                if not squad:
                    print('不存在队伍编号为{}的队伍'.format(order))
                else:
                    print('队伍数字编号 order: {}'.format(squad['order']))
                    print('队长uid chief: {}'.format(squad['chief']))
                    print('队伍招募信息 label: {}'.format(squad.get('label')))
                    print('队伍成员信息 members: {}'.format(squad['members']))
            else:
                print('请求失败')
                print('失败信息为 message: {}'.format(data['message']))
（8）队伍创建事件
事件名：SetupSquadEvent
说明：该事件为“服务端”事件，可于“服务端”监听此事件，有队伍被成功创建时“服务端”会广播此事件
响应参数：
    squad: 队伍信息
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseSquad', 'neteaseSquadDev', 'SetupSquadEvent', self, self.OnSomeoneSetupSquad)

    def OnSomeoneSetupSquad(self, data):
        print 'OnSomeoneSetupSquad', data
        squad = data["squad"]
        print('队伍数字编号 order: {}'.format(squad['order']))
        print('队长uid chief: {}'.format(squad['chief']))
        print('队伍招募信息 label: {}'.format(squad.get('label')))
        print('队伍成员信息 members: {}'.format(squad['members']))
（9）队伍解散事件
事件名：DissolveSquadEvent
说明：该事件为“服务端”事件，可于“服务端”监听此事件，有队伍被队长点击“解散队伍”按钮成功解散时“服务端”会广播此事件
响应参数：
    squad: 队伍信息
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseSquad', 'neteaseSquadDev', 'DissolveSquadEvent', self, self.OnSomeoneDissolveSquad)

    def OnSomeoneDissolveSquad(self, data):
        print 'OnSomeoneDissolveSquad', data
        squad = data["squad"]
        print('队伍数字编号 order: {}'.format(squad['order']))
        print('队长uid chief: {}'.format(squad['chief']))
        print('队伍招募信息 label: {}'.format(squad.get('label')))
        print('队伍成员信息 members: {}'.format(squad['members']))
（10）将一个队伍内的所有玩家传送到某个服务器的某个位置
函数：Teleport(uid, serverId, dimensionId, pos, label='')
说明：使传入uid对应玩家所在队伍内的所有玩家传送到某个服务器的某个位置
参数：
    uid: 玩家的uid
    serverId: 目的地服务器id
    dimensionId: 目的地维度
    pos: 目的地坐标
    label: 目的地昵称
示例：
    import lobbyGame.netgameApi as netgameApi
    uid = netgameApi.GetPlayerUid("-445201314")
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    squadSystem.Teleport(uid, 2000000, 0, (44, 520, 1314), '通利福尼亚')
（11）禁用或开启一个队伍的“召集队友”功能
函数：AssembleOption(uid, ban, cb)
说明：禁用或开启传入uid对应玩家所在队伍的“召集队友”功能
参数：
    uid: 玩家的uid
    ban: 禁用或开启
    cb: 返回后调用的cb函数
示例：
    import lobbyGame.netgameApi as netgameApi
    uid = netgameApi.GetPlayerUid("-445201314")
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    ban = True  # 禁用
    # ban = False  # 开启
    squadSystem.AssembleOption(uid, ban, self.do_something)

    ...

    def do_something(self, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print('操作成功')
                print('uid为{}的玩家所在队伍已{}“召集队友”功能'.format(data['entity']['uid'], data['entity']['ban'] and '禁用' or '开启'))
            else:
                print('操作失败')
                print('失败信息为 message: {}'.format(data['message']))
（12）禁用或开启一个队伍的“离开队伍”功能
函数：LeaveOption(uid, ban, cb)
说明：禁用或开启传入uid对应玩家所在队伍的“离开队伍”功能，禁用时也无法踢出玩家
参数：
    uid: 玩家的uid
    ban: 禁用或开启
    cb: 返回后调用的cb函数
示例：
    import lobbyGame.netgameApi as netgameApi
    uid = netgameApi.GetPlayerUid("-445201314")
    import server.extraServerApi as serverApi
    squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
    ban = True  # 禁用
    # ban = False  # 开启
    squadSystem.LeaveOption(uid, ban, self.do_something)

    ...

    def do_something(self, success, data):
        if not success:
            print('请求超时')
            print('返回数据为 data: {}'.format(data))
        else:
            if data['code'] == 1:
                print('操作成功')
                print('uid为{}的玩家所在队伍已{}“离开队伍”功能'.format(data['entity']['uid'], data['entity']['ban'] and '禁用' or '开启'))
            else:
                print('操作失败')
                print('失败信息为 message: {}'.format(data['message']))

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
调整UI大小
1.0.2版本：
在配置了提示插件的场合使用提示插件弹出提示
1.0.3版本：
对PVP插件增加支持
1.0.4版本：
调整了UI结构
1.0.5版本：
优化UI资源，增加了代码注释
1.0.6版本：
新增和聊天插件的互动功能
1.0.7版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.8版本：
mod.json新增RecruitmentShowLimit配置项，限制查询招募队伍的显示数量，减少数据量太大引起的卡顿
