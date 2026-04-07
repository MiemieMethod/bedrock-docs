插件介绍：
领地插件，领地插件可将1个区域设置为某个玩家专属领地。服主使用该插件后，开发者可以设置领地内的一些规则，比如设置可使用方块列表、可破坏方块列表、是否可伤害其他玩家等。

插件构成:
（1）neteaseResidence:部署于游戏服。
（2）neteaseResidenceMaster：部署于控制服，


使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseResidence中）
（2）配置game中的mod.json，请按照文件mod.json中"_comment"注释配置对应内容。
（3）MCStudio把neteaseResidence添加到游戏服，把neteaseResidenceMaster添加到控制服。
（4）使用本插件提供的api完成游戏功能。

名词解释：
领地信息字典
{
    "minPos": [800,-19,656],	# list(int,int,int)：领地区域(x, y, z)坐标的最小值
    "name": "redss1",			# str：领地名称
    "parentResId": 0,			# int：子领地对应父领地的ID，假如是零级领地，则父领地ID为0
    "serverType": "lobby",		# str：领地所属的server的type
    "authority": {},			# dict：领地的权限字典
    "id": 1,					# int：领地的唯一ID
    "bornPos": [829,-8,666],	# list(int,int,int)：此领地的传送点坐标
    "maxPos": [859,4,676],		# list(int,int,int)：领地区域(x, y, z)坐标的最大值
    "resLevel": 0,				# int：领地的层级，零级领地的层级为0，依次递加
    "dimension": 1				# int：领地所在的维度
}
权限信息字典：
每个项的具体含义请参考mod.json的注释
{
    "can_destroy_block_limit": ["minecraft:planks:2", "minecraft:planks:3"],
    "can_block_be_stepon": false,
    "place_on_block_items_limit": [],
    "cannot_interact_block_list": ["minecraft:planks:0","minecraft:planks:1"]
}
权限修改字典：
{
    "can_piston_effect_into": null,		# 此权限的类型为bool，输入参数null代表需要删除此领地的特殊配置权限，使用上级领地的权限设置或mod.json中的配置
    "place_on_block_items_limit": {"remove":["minecraft:planks:0"]},	# 此权限的类型为list，输入参数必须是dict，remove关键字说明需要在现有配置项中去除对应value里面的值
    "can_destroy_block_limit": {"add":["minecraft:planks:2", "minecraft:planks:3"]},	# 此权限的类型为list，输入参数必须是dict，add关键字说明需要在现有配置项中添加对应value里面的值
    "cannot_interact_block_list": {"set":["minecraft:planks:0", "minecraft:planks:1"]},	# 此权限的类型为list，输入参数必须是dict，set关键字说明需要使用value里面的值覆盖现有配置项
    "can_block_be_exploded":false	# 此权限的类型为bool，输入非null值的bool值代表需要替换对应权限配置值
}


插件api：
（1）创建零级领地
适用服务器：game
函数：CreateTopLevelResidence(cbFunc, uid, name, minPos, maxPos, dimension, bornPos)
参数：
    cbFunc: function，回调函数。有两个参数：suc，reasonOrResInfo。suc：bool，是否成功；reasonOrResInfo：str or dict，当suc=True时，返回新建的领地的信息字典（见名词解释：领地信息词典），当suc=False的时候，返回失败的理由
    uid: int，玩家uid
    name：str，领地名字
    minPos：tuple(int,int,int)，(x, y ,z)坐标，表示领地区域坐标最小值。
    maxPos：tuple(int,int,int)，(x, y ,z)坐标，表示领地区域坐标最大值。
    dimension：int，领地区域所在的维度，可以缺损，缺损时默认为0（主世界）。
    bornPos：tuple(int,int,int)，领地传送点坐标，可以缺损，缺损时默认传送点为领地中心XZ坐标的最顶端方块
返回：
    无
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    def callback(suc, reasonOrResInfo):
        if suc:
            print "CreateTopLevelResidence success, resInfo =", reasonOrResInfo
        else:
            print "CreateTopLevelResidence fail, reason is", reasonOrResInfo
    residenceSystem.CreateTopLevelResidence(callback， 123, 'testResName', (0,0,0), (20,50,20), 0, (10,0,10))
        
（2）创建子领地
适用服务器：game
函数：CreateSubResidence(parentResId, name, minPos, maxPos, bornPos)
参数：
    parentResId: int，父领地的唯一ID
    name：str，领地名字
    minPos：tuple(int,int,int)，(x, y ,z)坐标，表示领地区域坐标最小值。
    maxPos：tuple(int,int,int)，(x, y ,z)坐标，表示领地区域坐标最大值。
    bornPos：tuple(int,int,int)，领地传送点坐标，可以缺损，缺损时默认传送点为领地中心XZ坐标的最顶端方块
返回：
    tuple(suc, resInfo or reason)， 成功时返回领地信息字典，失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    suc, resInfoOrReason = residenceSystem.CreateSubResidence(233, 'testSubResName', (0,0,0), (20,50,20), (10,0,10))
    if suc:
        print "CreateSubResidence success!", resInfoOrReason
    else:
        print "CreateSubResidence fail! reason is", resInfoOrReason

（3）撤销某个领地
适用服务器：game
函数：DeleteResidenceById(resId)
参数：
    resId： int，领地的唯一ID
返回：
    tuple(suc, resInfoList or reason)， 成功时返回被删除的领地信息字典列表，失败时返回失败原因描述。由于父领地被删除时，子领地都会被伴随删除，所以返回的结果是一个列表
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    suc, resInfoListOrReason = residenceSystem.DeleteResidenceById(2)
    if suc:
        print "DeleteResidenceById success!", resInfoListOrReason
    else:
        print "DeleteResidenceById fail! reason is", resInfoListOrReason
        
（4）获取指定维度的指定位置所在的领地列表，从子领地到父领地，按照领地层级从大到小排序
适用服务器：game
函数：FindResidenceByPos(dimension, pos)
参数：
    dimension： int，指定维度
    pos： tuple(float,float,float)，指定位置的坐标，支持浮点数
返回：
    list(resInfo)， 返回位置所属的领地信息字典列表，按照领地层级从大到小排序，返回空列表代表位置不处于任何领地范围内
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    resInfoList = residenceSystem.FindResidenceByPos(0, (10.5, 4, 10.5))
    
（5）获取指定ID领地的在线所有者的uid列表
适用服务器：game
函数：FindResidenceOnlineOwners(resId)
参数：
    resId： int，领地的唯一ID
返回：
    list(int)，返回全部在线所有者的uid列表
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    uidList = residenceSystem.FindResidenceOnlineOwners(2)
    
（6）异步获取指定ID领地的全部所有者的uid列表
适用服务器：game
函数：QueryResidenceAllOwners(resId, callback)
参数：
    resId： int，领地的唯一ID
    callback：function(suc, message, uidList)，suc(bool)：是否成功；message(str)：失败时返回原因说明；uidList(list(int))：领地所有者的uid列表，无论是否在线
返回：
    无
示例：
    def AsyncCallBack(suc, message, result):
        print "AsyncCallBack suc=%s" % suc
        if suc:
            for one in result:
                print "single :", one
        else:
            print "fail reason =", message
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    residenceSystem.QueryResidenceAllOwners(2, AsyncCallBack)
    
（7）异步获取指定uid的玩家的所有零级领地的简单信息（仅领地ID，名称，所属服务器type，仅限于零级领地）
适用服务器：game
函数：QueryAllPlayerResidence(uid, callback)
参数：
    uid： int，需要查询的玩家的uid
    callback：function(suc, message, resInfoList)，suc(bool)：是否成功；message(str)：失败时返回原因说明；resInfoList(list(dict))：领地简单信息列表
返回：
    无
示例：
    def AsyncCallBack(suc, message, result):
        print "AsyncCallBack suc=%s" % suc
        if suc:
            for one in result:
                print "single :", one
        else:
            print "fail reason =", message
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    residenceSystem.QueryAllPlayerResidence(2236755, AsyncCallBack)
    
（8）获取指定领地当前的特殊权限设置
适用服务器：game
函数： GetAllAuthorityByResidence(resId)
参数：
    resId： int，领地的唯一ID
返回：
    dict/None，权限字典，权限的关键字和类型与mod.json中的权限配置相同，当对应领地不存在时返回None
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    authority = residenceSystem.GetAllAuthorityByResidence(2)

（9）获取指定uid的玩家在指定领地的特殊权限设置
适用服务器：game
函数： GetAllAuthorityByUid(uid, resId)
参数：
    uid： int，玩家的uid
    resId： int，领地的唯一ID
返回：
    dict/None，权限字典，权限的关键字和类型与mod.json中的权限配置相同，当对应领地或玩家不存在时返回None
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    authority = residenceSystem.GetAllAuthorityByUid(234435345, 2)
    
（10）设置指定领地的特殊权限
适用服务器：game
函数： ChangeResidenceAuthority(resId, authority)
参数：
    resId： int，领地的唯一ID
    authority：dict，权限修改字典（见名词解释：权限修改字典）
返回：
    tuple(suc, authority or reason)， 成功时返回指定领地当前的完整的权限信息字典（见名词解释：权限信息字典），失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    authority = {
        "can_piston_effect_into": null,
        "place_on_block_items_limit": {"remove":["minecraft:planks:0"]},
        "can_destroy_block_limit": {"add":["minecraft:planks:2", "minecraft:planks:3"]},	
        "cannot_interact_block_list": {"set":["minecraft:planks:0", "minecraft:planks:1"]},
        "can_block_be_exploded":false
    }
    suc, newAuthority = residenceSystem.ChangeResidenceAuthority(2, authority)
    
（11）设置指定玩家在指定领地的特殊权限
适用服务器：game
函数： ChangePlayerResidenceAuthority(uid, resId, authority)
参数：
    uid： int，玩家uid
    resId： int，领地的唯一ID
    authority：dict，权限修改字典（见名词解释：权限修改字典）
返回：
    tuple(suc, authority or reason)， 成功时返回指定玩家在指定领地当前的完整的权限信息字典（见名词解释：权限信息字典），失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    authority = {
        "can_piston_effect_into": null,
        "place_on_block_items_limit": {"remove":["minecraft:planks:0"]},
        "can_destroy_block_limit": {"add":["minecraft:planks:2", "minecraft:planks:3"]},
        "cannot_interact_block_list": {"set":["minecraft:planks:0", "minecraft:planks:1"]},
        "can_block_be_exploded":false
    }
    suc, newAuthority = residenceSystem.ChangePlayerResidenceAuthority(2343454, 2, authority)
    
（12）设置指定领地的传送点坐标
适用服务器：game
函数： ChangeResidenceTeleportPos(resId, pos)
参数：
    resId： int，领地的唯一ID
    pos：tuple(int,int,int)，传送点坐标
返回：
    tuple(suc, resInfo or reason)， 成功时返回领地的信息字典，失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    suc, resInfo = residenceSystem.ChangeResidenceTeleportPos(2, (15, 4, 15))
    
（13）把某个玩家加入某个零级领地的所有者列表中
适用服务器：game
函数： AddPlayerToResidence(cbFunc, uid, resId)
参数：
    cbFunc: function，回调函数。有两个参数：suc，reasonOrResInfo。suc：bool，是否成功；reasonOrResInfo：str or dict，当suc=True时，返回新建的领地的信息字典（见名词解释：领地信息词典），当suc=False的时候，返回失败的理由
    uid： int，玩家uid
    resId： int，领地的唯一ID，因为只有零级领地才有所有者的概念，所以对应领地必须是零级领地
返回：
    无
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    def callback(suc, reasonOrResInfo):
        if suc:
            print "AddPlayerToResidence success, resInfo =", reasonOrResInfo
        else:
            print "AddPlayerToResidence fail, reason is", reasonOrResInfo
    residenceSystem.AddPlayerToResidence(callback, 256587421, 2)
    
（14）把某个玩家从某个零级领地的所有者列表中剔除
适用服务器：game
函数： RemovePlayerFromResidence(uid, resId)
参数：
    uid： int，玩家uid
    resId： int，领地的唯一ID，因为只有零级领地才有所有者的概念，所以对应领地必须是零级领地
返回：
    tuple(suc, resInfo or reason)， 成功时返回领地的信息字典，失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    suc, resInfo = residenceSystem.RemovePlayerFromResidence(256587421, 2)
    
（15）把指定玩家传送到指定领地的传送点
适用服务器：game
函数： TeleportPlayerToRedidence(uid, resId)
参数：
    uid： int，玩家uid
    resId： int，领地的唯一ID，因为只有零级领地才有所有者的概念，所以对应领地必须是零级领地
返回：
    tuple(suc, resInfo or reason)， 成功时返回领地的信息字典，失败时返回失败原因描述。
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    suc, resInfo = residenceSystem.TeleportPlayerToRedidence(256587421, 2)

（16）转移领地领主
适用服务器：game
函数： TransferResidenceOwner(resId, toUid, callback = None)
参数：
    resId: 领地Id
    toUid： int，转给的玩家uid,其中如果传入1,则说明把领地转给服务器
    callback 回调函数，参数是suc, resId, toUid, message，依次是是否成功(bool)，领地Id，转给的玩家uid，提示消息
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    def callback(suc, resId, toUid, message):
    print suc, resId, toUid, message
    residenceSystem.TransferResidenceOwner(1, 1, callback)

（17）打开/关闭创建领地的预览光圈
适用服务器：game
函数： SetShowResPreEffect(args)
参数：
    showResPreEffect: bool，是否显示预览光圈
示例：
    import client.extraClientApi as clientApi
    residenceSystem = clientApi.GetSystem("neteaseResidence", "neteaseResidenceClient")
    residenceSystem.SetShowResPreEffect({"showResPreEffect":False})

（18）打开/关闭创建领地光圈
适用服务器：game
函数： SetShowResEffect(args)
参数：
    showResEffect: bool，是否显示预览光圈
示例：
    import client.extraClientApi as clientApi
    residenceSystem = clientApi.GetSystem("neteaseResidence", "neteaseResidenceClient")
    residenceSystem.SetShowResEffect({"showResEffect":False})

（19）申请指定数量的预备用领地ID（服务端）
适用服务器：game
函数： PrepareBatchResidenceId(batchNum, cbFunc)
参数：
    batchNum: int, 申请领地ID的数量
    cbFunc: function，回调函数。有两个参数：suc，idList。suc：bool，是否成功；idList：list，当suc=True时，返回新申请的ID列表，当suc=False时，返回空列表
返回：
    无
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    def callback(suc, idList):
        if suc:
            print "PrepareBatchResidenceId success, idList =", idList
        else:
            print "PrepareBatchResidenceId fail"
    residenceSystem.PrepareBatchResidenceId(100, callback)

（20）获取与指定区域有重叠的顶级领地的ID列表（服务端）
适用服务器：game
函数： FindOverlapResidenceByArea(dimension, minPos, maxPos)
参数：
    dimension: int, 指定区域所在的维度
    minPos: tuple(int,int,int), 指定区域(x, y, z)坐标的最小值
    maxPos: tuple(int,int,int), 指定区域(x, y, z)坐标的最大值
返回：
    list(int)：指定区域有重叠的顶级领地的ID列表，返回空列表时代表指定区域与任何领地都不重叠
示例：
    import server.extraServerApi as serverApi
    residenceSystem = serverApi.GetSystem("neteaseResidence", "neteaseResidenceServer")
    resIdList = residenceSystem.FindOverlapResidenceByArea(0, (-4, -4, -4), (4, 4, 4))
    if resIdList:
        print "FindOverlapResidenceByArea area in some residence"
    else:
        print "FindOverlapResidenceByArea area not in any residence"
    
运营指令：
（1）查询指定服务器中的所有领地信息，但不包括对应所有者玩家列表。
备注：本请求最多只会返回一定数量的领地信息，假如需要获取全部领地信息，则需要调整查询参数分段获取
post url: http:masterip:masterport/residence/query/server-residence-info
post body:{
    "type": "lobby",	# str：对应服务器进程的type
    "startId": 0		# int：查询中最小的领地ID，返回的领地列表中的领地ID均为大于此ID，且按照从小到大排序
}
response:
{
    "message": "",			# str：失败原因描述
    "code": 1,				# int：返回码，1表示成功，其他表示失败
    "entity": {
        "reachEnd": false,	# bool：是否已经查询到了ID最大的领地了
        "resList": [	# list(dict)：每个元素代表一个领地的基础信息，不包括领地的所有者列表
            {
                "minPos": [	# list(int,int,int)：领地区域(x, y, z)坐标的最小值
                    800,
                    -19,
                    656
                ],
                "name": "redss1",	# str：领地名称
                "parentResId": 0,	# int：子领地对应父领地的ID，假如是零级领地，则父领地ID为0
                "serverType": "lobby",	# str：领地所属的server的type
                "authority": {},		# dict：领地的权限字典
                "id": 1,			# int：领地的唯一ID
                "bornPos": [		# list(int,int,int)：此领地的传送点坐标
                    829,
                    -8,
                    666
                ],
                "maxPos": [			# list(int,int,int)：领地区域(x, y, z)坐标的最大值
                    859,
                    4,
                    676
                ],
                "resLevel": 0,		# int：领地的层级，零级领地的层级为0，依次递加
                "dimension": 1,		# int：领地所在的维度
            },
            .
            .
            .
        ]
        "startId": 0				# int：本次查询起始的领地ID，返回的领地列表中的领地，均为大于此ID的
    }
}
（2）查询某个玩家的全部领地
post url: http:masterip:masterport/residence/query/player-residence-info
post body:{
    "uid": 2310039686	# int：想要查询的玩家uid
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": [			# list(dict)：返回此玩家的在整个服务器组的全部领地
        {
            "minPos": [
                -50,
                -64,
                -50
            ],
            "name": "res001",
            "parentResId": 0,
            "serverType": "lobby",
            "authority": {},
            "id": 1,
            "bornPos": [
                0,
                0,
                0
            ],
            "maxPos": [
                50,
                64,
                50
            ],
            "resLevel": 0,
            "dimension": 0
        }
    ]
}
（3）创建新领地。
备注：即将某个服务器地图的某个区域指定为某个玩家的领地
post url: http:masterip:masterport/residence/create-residence
post body:{
    "uid":2310039686,		# int：玩家唯一ID，创建零级领地时，要求对应玩家必须在线且正好在对应type的服务器进程中，创建子领地时此项无效，可缺损
    "type": "lobby",		# str：领地所在服务器类型。每种类型只有一个服务器，通过服务器类型区分不同服务器。
    "name": "res003",		# str：领地名字，在单个服务器进程内，要求领地名字唯一
    "dimension": 0,			# int：领地所属的维度
    "parentResId": 0,		# int：创建子领地时，指定的对应父领地的唯一ID，创建零级领地时可缺损
    "minPos": [60,0,60],	# list(int,int,int)：领地区域(x, y, z)坐标的最小值
    "maxPos": [100,20,100],	# list(int,int,int)：领地区域(x, y, z)坐标的最大值
    "bornPos": null			# list(int,int,int)/null：领地的传送点，可缺损时传送点为领地中心XZ坐标的最顶端方块
}
response:
{
    "message": "",			# str：失败原因描述
    "code": 1,				# int：返回码，1表示成功，其他表示失败
    "entity": {
        "minPos": [			# list(int,int,int)：领地区域(x, y, z)坐标的最小值
            60,
            -64,
            60
        ],
        "name": "res003",	# str：领地名称
        "parentResId": 0,	# int：子领地对应父领地的ID，假如是零级领地，则父领地ID为0
        "serverType": "lobby",	# str：领地所属的server的type
        "authority": {},		# dict：领地的权限字典
        "dimension": 0,			# int：领地所在的维度
        "bornPos": [			# list(int,int,int)：此领地的传送点坐标
            80,
            64,
            80
        ],
        "maxPos": [				# list(int,int,int)：领地区域(x, y, z)坐标的最大值
            100,
            64,
            100
        ],
        "resLevel": 0,			# int：领地的层级，零级领地的层级为0，依次递加
        "id": 3					# int：领地的唯一ID
    }
}

（4）删除某个领地
post url: http:masterip:masterport/residence/delete-residence
post body:{
    "resId": 3,				# int：领地的唯一ID
    "type": "lobby"			# str：领地所在服务器类型。
}
response:
{
    "message": "",			# str：失败原因描述
    "code": 1,				# int：返回码，1表示成功，其他表示失败
    "entity": [				# list(dict)：由于删除某个领地会导致所有其子领地自动删除，所以返回了所有被删除的领地信息字典列表，可以参考【创建新领地】
        {
            "minPos": [
                60,
                -64,
                60
            ],
            "name": "res003",
            "parentResId": 0,
            "serverType": "lobby",
            "authority": {},
            "id": 3,
            "bornPos": [
                80,
                64,
                80
            ],
            "maxPos": [
                100,
                64,
                100
            ],
            "resLevel": 0,
            "dimension": 0
        },
        {
            "minPos": [
                60,
                -64,
                60
            ],
            "name": "res004",
            "parentResId": 3,
            "serverType": "lobby",
            "authority": {},
            "id": 4,
            "bornPos": [
                80,
                64,
                80
            ],
            "maxPos": [
                100,
                64,
                100
            ],
            "resLevel": 1,
            "dimension": 0
        },
        {
            "minPos": [
                60,
                -64,
                60
            ],
            "name": "res005",
            "parentResId": 4,
            "serverType": "lobby",
            "authority": {},
            "id": 5,
            "bornPos": [
                80,
                64,
                80
            ],
            "maxPos": [
                100,
                64,
                100
            ],
            "resLevel": 2,
            "dimension": 0
        }
    ]
}

（5）给已经存在的领地添加一个新的所有者
post url: http:masterip:masterport/residence/add-player-to-residence
post body:{
    "uid": 1,		# int：新增的所有者uid
    "resId": 1,		# int：需要新增所有者的领地的id
    "type": "lobby"	# str：领地所在服务器类型。每种类型只有一个服务器，通过服务器类型区分不同服务器。
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": {			# dict：返回玩家成功加入的领地的基本信息，具体每项的含义见上文【创建新领地】
        "minPos": [
            101,
            -64,
            101
        ],
        "name": "res006",
        "parentResId": 0,
        "serverType": "lobby",
        "authority": {},
        "id": 6,
        "bornPos": [
            115,
            64,
            115
        ],
        "maxPos": [
            130,
            64,
            130
        ],
        "resLevel": 0,
        "dimension": 0
    }
}

（6）为已经存在的领地移除一个所有者
post url: http:masterip:masterport/residence/remove-player-from-residence
post body:{
    "uid": 1,		# int：需要移除的所有者uid
    "resId": 1,		# int：需要移除所有者的领地的id
    "type": "lobby"	# str：领地所在服务器类型。每种类型只有一个服务器，通过服务器类型区分不同服务器。
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": {			# dict：返回之前玩家所在领地的基本信息，具体每项的含义见上文【创建新领地】
        "minPos": [
            101,
            -64,
            101
        ],
        "name": "res006",
        "parentResId": 0,
        "serverType": "lobby",
        "authority": {},
        "id": 6,
        "bornPos": [
            115,
            64,
            115
        ],
        "maxPos": [
            130,
            64,
            130
        ],
        "resLevel": 0,
        "dimension": 0
    }
}
（7）强制释放玩家领地操作锁
post url: http:masterip:masterport/residence/release-player-residence-lock
post body:{
    "uid": 1,		# int：需要移除锁所有者uid
    "type": "lobby"	# str：领地所在服务器类型。
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": {}
}
（8）修改指定领地权限
post url: http:masterip:masterport/residence/change-residence-authority
post body:{
    "type": "lobby",	# str：领地所在服务器类型。
    "resId": 6,			# int：领地的唯一ID
    "authority":{		# dict：需要修改的权限内容。
        "can_piston_effect_into": null,		# 此权限的类型为bool，输入参数null代表需要删除此领地的特殊配置权限，使用上级领地的权限设置或mod.json中的配置
        "place_on_block_items_limit": {"remove":["minecraft:planks:0"]},	# 此权限的类型为list，输入参数必须是dict，remove关键字说明需要在现有配置项中去除对应value里面的值
        "can_destroy_block_limit": {"add":["minecraft:planks:2", "minecraft:planks:3"]},	# 此权限的类型为list，输入参数必须是dict，add关键字说明需要在现有配置项中添加对应value里面的值
        "cannot_interact_block_list": {"set":["minecraft:planks:0", "minecraft:planks:1"]},	# 此权限的类型为list，输入参数必须是dict，set关键字说明需要使用value里面的值覆盖现有配置项
        "can_block_be_exploded":false	# 此权限的类型为bool，输入非null值的bool值代表需要替换对应权限配置值
    }
}
response:
{
    "message": "",			# str：失败原因描述
    "code": 1,				# int：返回码，1表示成功，其他表示失败
    "entity": {				# dict：当前对应领地的权限配置属性
        "can_destroy_block_limit": [
            "minecraft:planks:0",
            "minecraft:planks:1",
            "minecraft:planks:2",
            "minecraft:planks:3"
        ],
        "cannot_interact_block_list": [
            "minecraft:planks:0",
            "minecraft:planks:1"
        ],
        "place_on_block_items_limit": [
            "minecraft:planks:1"
        ],
        "can_block_be_exploded": false
    }
}
（9）修改指定玩家在指定领地的权限
post url: http:masterip:masterport/residence/change-player-residence-authority
post body:{
    "type": "lobby",	# str：领地所在服务器类型。
    "resId": 6,			# int：领地的唯一ID
    "uid": 2310039686,	# int：需要特殊设置权限的玩家uid，只有非领地所有者的才能设置特殊权限
    "authority":{		# dict：需要修改的权限内容。
        "can_piston_effect_into": null,		# 此权限的类型为bool，输入参数null代表需要删除此领地的特殊配置权限，使用上级领地的权限设置或mod.json中的配置
        "place_on_block_items_limit": {"remove":["minecraft:planks:0"]},	# 此权限的类型为list，输入参数必须是dict，remove关键字说明需要在现有配置项中去除对应value里面的值
        "can_destroy_block_limit": {"add":["minecraft:planks:2", "minecraft:planks:3"]},	# 此权限的类型为list，输入参数必须是dict，add关键字说明需要在现有配置项中添加对应value里面的值
        "cannot_interact_block_list": {"set":["minecraft:planks:0", "minecraft:planks:1"]},	# 此权限的类型为list，输入参数必须是dict，set关键字说明需要使用value里面的值覆盖现有配置项
        "can_block_be_exploded":false	# 此权限的类型为bool，输入非null值的bool值代表需要替换对应权限配置值
    }
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": {			# dict：当前玩家对应指定领地的特殊权限内容
        "can_destroy_block_limit": [
            "minecraft:planks:2",
            "minecraft:planks:3"
        ],
        "can_block_be_stepon": false,
        "place_on_block_items_limit": [],
        "cannot_interact_block_list": [
            "minecraft:planks:0",
            "minecraft:planks:1"
        ]
    }
}
（10）修改一个领地的传送点
post url: http:masterip:masterport/residence/change-residence-teleport-pos
post body:{
    "resId": 1,		# int：领地的id
    "type": "lobby"	# str：领地所在服务器类型
    "pos": [0,0,0]	# list(int,int,int)：传送到领地API对应的目标坐标点，不要求一定在领地内
}
response:
{
    "message": "",		# str：失败原因描述
    "code": 1,			# int：返回码，1表示成功，其他表示失败
    "entity": {			# dict：返回指定领地的基本信息，具体每项的含义见上文【创建新领地】
        "minPos": [
            -50,
            -64,
            -50
        ],
        "name": "res001",
        "parentResId": 0,
        "serverType": "lobby",
        "authority": {},
        "id": 1,
        "bornPos": [
            0,
            0,
            0
        ],
        "maxPos": [
            50,
            64,
            50
        ],
        "resLevel": 0,
        "dimension": 0
    }
}

更新列表：

1.0.0版本：
初始版本

1.0.1版本：
本次版本更新有数据库表格结构变化，具体见mod.sql
1、领地支持维度设置，不再限于主世界
2、优化领地算法，支持单个服务器进程数以万计的领地
3、支持子领地的创建
4、每个领地均可单独设置领地权限，并且可以对非所有者的外部玩家设置特殊权限
5、支持简单的客户端领地区域预览与领地创建
6、修改与新增大量API，旧版API全部废弃
    （1）创建零级领地
    （2）创建子领地
    （3）撤销某个领地
    （4）获取指定维度的指定位置所在的领地列表，从子领地到父领地，按照领地层级从大到小排序
    （5）返回指定ID领地的在线所有者的uid列表
    （6）异步获取指定ID领地的全部所有者的uid列表
    （7）异步获取指定uid的玩家的所有领地的简单信息（仅领地ID，名称，所属服务器type，领地层级）
    （8）返回指定领地当前的特殊权限设置
    （9）返回指定uid的玩家在指定领地的特殊权限设置
    （10）设置指定领地的特殊权限
    （11）设置指定玩家在指定领地的特殊权限
    （12）设置指定领地的传送点坐标
    （13）把某个玩家加入某个零级领地的所有者列表中
    （14）把某个玩家从某个零级领地的所有者列表中剔除
    （15）把指定玩家传送到指定领地的传送点
7、修改与新增大量运营指令，旧版运营指令全部废弃
    （1）查询指定服务器中的所有领地信息，但不包括对应所有者玩家列表。
    （2）查询某个玩家的全部领地
    （3）创建新领地。
    （4）删除某个领地
    （5）给已经存在的领地添加一个新的所有者
    （6）为已经存在的领地移除一个所有者
    （7）强制释放玩家领地操作锁
    （8）修改指定领地权限
    （9）修改指定玩家在指定领地的权限
    （10）修改一个领地的传送点

1.0.2版本：
新增可视化操作UI

1.0.3版本：
新建、修改领地时可以移动，旋转视角。

1.0.4版本
新增领地转让接口

1.0.5版本
修复某些情况下领地内设置了不能和方块交互仍然可以和方块交互的bug

1.0.6版本
优化贴图资源，增加部分代码注释

1.0.7版本
添加大量注释

1.0.8版本
修改创建领地与添加新玩家为指定领地所有者的API，支持玩家不在线时也可以创建领地
（1）创建零级领地
（13）把某个玩家加入某个零级领地的所有者列表中
新增可以关闭领地创建预览光圈的接口, 新增可以关闭领地光圈的接口

1.0.9版本
修正一组服务器中，多个服务器进程都有领地插件时，领地ID冲突的问题
（1）mod.sql中新增了生成唯一领地ID用到的表，需要执行新建【neteaseResidenceUniqueId】表的sql
（2）修复了不能跨服传送至领地的bug
新增API：
（19）申请指定数量的预备用领地ID（服务端）

1.0.10版本
按照新的插件标准，重新实现了领地界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题
（3）插件UI使用的图片文件尺寸过大影响界面加载速度和占用client内存的问题
修正一些客户端判定领地所有权出Trace的问题

1.0.11版本
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题

1.0.12版本
新增API：
（20）获取与指定区域有重叠的顶级领地的ID列表（服务端）

1.0.13版本：
1、提供UI工程
2、修改领地各种配置参数的的配置方式，以服务器类型为一级的Key，支持基于服务器类型分别配置