插件介绍：
该服务器Mod隶属于“PVP”插件。
“PVP”插件可以控制玩家部分PVP相关行为


插件构成：
目前“PVP”插件包含以下Mod：
- neteasePeace：部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteasePeace添加至需要的大厅服或者游戏服的mods列表中
（2）请在mysql中执行mod.sql（位于neteasePeace中）

插件api：
（1）使一个玩家打开PVP管理界面
函数：OpenPeaceBoard(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    peaceSystem.OpenPeaceBoard(uid)
（2）获取一个玩家是否开启了PVP，当玩家在本服才可能返回True
函数：GetPVPStatus(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    flag = bool(peaceSystem.GetPVPStatus(uid))  # True为开启状态，False为关闭状态
（3）本服PVPMode的getter和setter
函数：GetPVPMode(), SetPVPMode(mode)
参数：
    mode: 0或1，详细解释见mod.json
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    peaceSystem.SetPVPMode(1)
    print(peaceSystem.GetPVPMode())
（4）设置一个玩家当前是否开启PVP（玩家依旧能自己手动关闭或开启），当玩家在本服才可能返回True
函数：SetPVPStatus(uid, switch)
参数：
    uid: 玩家的uid
    switch: 开启为True
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    flag = peaceSystem.SetPVPStatus(uid, True)  # True为设置成功，False为设置失败
（5）获得一个玩家PVP相关信息（包含击败对象与仇敌）
函数：QueryPVPInfo(uid, cb)
参数：
    uid: 玩家的uid
    cb: 回调函数
示例：
    def p(data):
        if data:
            print(data['l1'])  # 击败对象列表，为mod.sql中数据库表对应字段的值
            print(data['l2'])  # 仇敌列表，为mod.sql中数据库表对应字段的值
        else:
            print('error')

    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    peaceSystem.QueryPVPInfo(uid, p)
（6）获得一个玩家PVP相关信息（包含击败对象与仇敌），需要初始化过mysqlPool
示例：
    ....
    class DemoServerSystem(ServerSystem):
        ...

        def p(self, data):
            print(data)  # 为mod.sql中数据库表对应字段的值

        ...

        def foo(self, ...):
            ...

            def demo(conn, uid):
                try:
                    c = conn.cursor()
                    c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC', (uid, 0))
                    l1 = [{'uname': row[3], 'ts': row[4], 't': row[5]} for row in c.fetchall()]  # 击败对象列表
                    c.execute('SELECT * FROM neteasePVPRec WHERE uid1=%s AND foe=%s ORDER BY t DESC', (uid, 1))
                    l2 = [{'uname': row[3], 'ts': row[4], 't': self.Fmt(row[5])} for row in c.fetchall()]  # 仇敌列表
                    return {'l1': l1, 'l2': l2}
                except:
                    conn.rollback()
                    return False

            mysqlPool.AsyncExecuteFunctionWithOrderKey(
                demo,
                'DEMO',
                lambda data: self.p(data),
                uid
            )
（7）获得一个玩家PVP伤害过滤对象设置
函数：GetPVPSwitchInfo(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    info = peaceSystem.GetPVPSwitchInfo(uid)
    if not info:
        print('no this player')
    else:
        print(bool(info['hood']))  # True为攻击好友不造成伤害
        print(bool(info['crew']))  # True为攻击队友不造成伤害
        print(bool(info['gang']))  # True为攻击公会成员不造成伤害
（8）设置一个玩家PVP伤害过滤对象
函数：SetPVPSwitchInfo(uid, info)
参数：
    uid: 玩家的uid
    info: 过滤设置
示例：
    import server.extraServerApi as serverApi
    peaceSystem = serverApi.GetSystem("neteasePeace", "neteasePeaceDev")
    print(peaceSystem.SetPVPSwitchInfo(uid, {'hood': 1, 'crew': 0, 'gang': 1}))  # 设置攻击好友或公会成员不造成伤害，攻击队友会造成伤害，打印True则为设置成功

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
优化贴图资源，增加部分代码注释
1.0.2版本：
添加大量注释
1.0.3版本:
调整UI，使用MC Studio导出的UI工程，同时把UI工程放在stdio_res路径下，并用UI面向对象基类重写UI逻辑
1.0.4版本：
提供UI工程
