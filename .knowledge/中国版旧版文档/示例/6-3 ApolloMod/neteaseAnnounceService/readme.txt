插件介绍：
该服务器Mod隶属于“公告”插件。
“公告”插件实现3个功能，1个是登录弹窗，1个是公告功能，1个是邮件功能：
- 登录弹窗：玩家登录游戏会看到一个自动弹出的界面，弹窗按弹出顺序依次弹出。
- 浮窗公告：在游戏屏幕中央弹出一条文字信息，实现指定时间后消失（或显示下一条）
- 邮件：标准的游戏内邮件功能，支持发送附件，领取附件中物品到背包，支持群发邮件
- 特殊事项：邮件附件中的物品，当前版本只支持发送普通物品，不支持发送方块。

插件构成：
目前“公告”插件包含以下Mod：
- neteaseAnnounce: 部署于大厅服或游戏服。
- neteaseAnnounceMaster：部署于控制服。
- neteaseAnnounceService：部署于功能服。

数据库：
- mysql

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseAnnounceService中）
（2）在部署配置中，将neteaseAnnounce添加至需要的大厅服或者游戏服的mods列表中；
（3）在部署配置中，将neteaseAnnounceMaster添加至控制服的mods列表中；
（4）在部署配置中，将neteaseAnnounceService添加至某一个功能服的mods列表中。若不是MCStudio添加该mod，则需要手动将字符串"neteaseAnnounce"添加到deploy.json中service下的module_names属性中
（3）部署并启动服务器后，就可以在主界面居中略偏右的位置看到打开邮件界面的按钮

插件api：
（1）向一组指定uid的玩家发送私人邮件（大厅服/游戏服）
函数：SendMailToUser(touids, title, content, itemList=[], expire=None, srcName="")
参数：
    touids:list(int), 玩家唯一ID的列表
    title:str, 邮件标题
    content:str, 邮件正文
    itemList:list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    expire:int, 邮件有效期，单位秒
    srcName:str, 邮件发送者名字
示例：
    import server.extraServerApi as serverApi
    itemDict = {
        'itemName': 'minecraft:bow',
        'count': 1,
        'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
        'auxValue': 0,
        'customTips':'§c new item §r',
        'extraId': 'abc'
    }
    mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
    mailSystem.SendMailToUser([123,234], "欢迎新人", "欢迎首次登录，开发组送上弓一把", [itemDict,], 86400, "开发组")
（2）向所有玩家（无论是否在线）群发邮件（大厅服/游戏服）
函数：SendMailToGroup(title, content, effectTime, itemList=[], expire=None, scrName="")
参数：
    title:str, 邮件标题
    content:str, 邮件正文
    effectTime:int, 时间戳，首次登录游戏时间小于此时间的玩家才会收到这封群发邮件
    itemList:list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    expire:int, 邮件有效期，单位秒
    srcName:str, 邮件发送者名字
示例：
    import server.extraServerApi as serverApi
    itemDict = {
        'itemName': 'minecraft:bow',
        'count': 1,
        'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
        'auxValue': 0,
        'customTips':'§c new item §r',
        'extraId': 'abc'
    }
    mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
    # 给所有2019年12月25日 23:59:59前登录过游戏玩家发送邮件
    mailSystem.SendMailToGroup("圣诞快乐", "圣诞礼物，开发组送上弓一把", 1577289600, [itemDict,], 86400, "开发组")
（3）打开邮件主界面（客户端）
函数：OpenMainUI()
参数：无
示例：
    import client.extraClientApi as clientApi
    system = clientApi.GetSystem("neteaseAnnounce", "neteaseAnnounceBeh")
    # 打开邮件主界面
    system.OpenMainUI()
（4）注册玩家收到邮件的回调函数（客户端）
函数：RegisterMailArriveCallback(cbFunc)
参数：
    cbFunc: function，异步回调函数。回调函数没有参数，每次有新邮件到达时会回调此函数
返回：
    int or None：返回注册函数的index，用于反注册回调函数，当注册失败时返回None
示例：
    import client.extraClientApi as clientApi
    mailSystem = clientApi.GetSystem("neteaseAnnounce", "neteaseAnnounceBeh")
    def hasMailArrive():
        print "hasMailArrive"
    mailSystem.RegisterMailArriveCallback(hasMailArrive)
（5）某UID玩家是否有未读邮件（服务端）
函数：CheckHasUnreadMail(uid, cbFunc)
参数：
    uid: int, 玩家唯一ID
    cbFunc: function，异步回调函数。回调函数包含两个参数：suc, hasUnread。suc：bool，是否成功获取信息。hasUnread：bool，True代表存在未读邮件，False代表不存在未读邮件
返回：
    无
示例：
    import server.extraServerApi as serverApi
    mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
    def hasMailUnread(suc, hasUnread):
        print "hasMailUnread", suc, hasUnread
    mailSystem.CheckHasUnreadMail(uid, hasMailUnread)
（6）反注册玩家收到邮件的回调函数（客户端）
函数：UnRegisterMailArriveCallback(index)
参数：
    index: int，RegisterMailArriveCallback的返回值
返回：
    bool：是否成功反注册
示例：
    import client.extraClientApi as clientApi
    mailSystem = clientApi.GetSystem("neteaseAnnounce", "neteaseAnnounceBeh")
    def hasMailArrive():
        print "hasMailArrive"
    index = mailSystem.RegisterMailArriveCallback(hasMailArrive)
    suc = mailSystem.UnRegisterMailArriveCallback(index)
    print "UnRegisterMailArriveCallback index={} suc={}".format(index, suc)
（7）向一组指定uid的玩家发送私人邮件（功能服用）
函数：OutSendMailToMany(touids, title, content, itemList=[], expire=None, srcName="")
参数：
    touids:list(int), 玩家唯一ID的列表
    title:str, 邮件标题
    content:str, 邮件正文
    itemList:list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    expire:int, 邮件有效期，单位秒
    srcName:str, 邮件发送者名字
示例：
    import server.extraServiceApi as serviceApi
    itemDict = {
        'itemName': 'minecraft:bow',
        'count': 1,
        'enchantData': [(19, 1),],
        'auxValue': 0,
        'customTips':'§c new item §r',
        'extraId': 'abc'
    }
    mailSystem = serviceApi.GetSystem("neteaseAnnounce", "neteaseAnnounceService")
    mailSystem.OutSendMailToMany([123,234], "欢迎新人", "欢迎首次登录，开发组送上弓一把", [itemDict,], 86400, "开发组")
（8）向所有玩家（无论是否在线）群发邮件（功能服用）
函数：OutSendMailToGroup(title, content, itemList=[], effectTime=None, expire=None, srcName="")
参数：
    title:str, 邮件标题
    content:str, 邮件正文
    effectTime:int, 时间戳，首次登录游戏时间小于此时间的玩家才会收到这封群发邮件
    itemList:list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    expire:int, 邮件有效期，单位秒
    srcName:str, 邮件发送者名字
示例：
    import server.extraServiceApi as serviceApi
    itemDict = {
        'itemName': 'minecraft:bow',
        'count': 1,
        'enchantData': [(19, 1),],
        'auxValue': 0,
        'customTips':'§c new item §r',
        'extraId': 'abc'
    }
    mailSystem = serviceApi.GetSystem("neteaseAnnounce", "neteaseAnnounceService")
    # 给所有2019年12月25日 23:59:59前登录过游戏玩家发送邮件
    mailSystem.OutSendMailToGroup("圣诞快乐", "圣诞礼物，开发组送上弓一把", [itemDict,], 1577289600, 86400, "开发组")


支持的运营指令：
运营指令：
（1）添加一个新的登录弹窗
post url: http:masterip:masterport/login-pop-new
post body:{
    "title": "带有图片",    # str, 弹窗标题
    "content": "我是内容哈哈哈哈",  # str, 弹窗正文
    "pic":"textures/ui/netease_announce/123.png",    # str, 弹窗图片路径，需要在res中存在
    "priority": 12, # int, 弹窗显示优先级，数字大的显示在前
    "beginTime": "2019-12-21 17:30:43", # str, 弹窗显示起始时间，超过这个时间后登录的玩家才会看到此弹窗，允许缺损，缺损时默认为当前时间
    "endTime": "2019-12-29 17:30:43"    # str, 弹窗显示结束时间，超过这个时间后登录的玩家不会再看到此弹窗，允许缺损，缺损时默认值为【起始时间】加上一个可配置的固定偏移值
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": { # 返回新建的弹窗记录
        "content": "我是内容哈哈哈哈",
        "endTime": "2019-12-29 17:30:43",
        "title": "带有图片",
        "pic": "textures/ui/netease_announce/123.png",
        "priority": 12,
        "beginTime": "2019-12-21 17:30:43",
        "_id": 25
    }
}
（2）查询当前弹窗列表
post url: http:masterip:masterport/login-pop-list
post body:{}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {
        "dataList": [   # 当前尚未过期的登录弹窗记录列表，这里包括了尚未到生效时间的
            {
                "content": "我是内容哈哈哈哈",
                "endTime": "2019-12-29 17:30:43",
                "title": "带有图片",
                "pic": "textures/ui/netease_announce/123.png",
                "priority": 12,
                "beginTime": "2019-12-21 17:30:43",
                "_id": 25
            },
            .
            .
            .
        ],
    "version": 1576303762   # 版本号，仅用于标识变化
    }
}
（3）移除一个登录弹窗
post url: http:masterip:masterport/login-pop-del
post body:{
    "_id": 25   # int, 想要移除的弹窗的唯一ID
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": { # 返回被移除的弹窗记录
        "content": "我是内容哈哈哈哈",
        "endTime": "2019-12-29 17:30:43",
        "title": "带有图片",
        "pic": "textures/ui/netease_announce/123.png",
        "priority": 12,
        "beginTime": "2019-12-21 17:30:43",
        "_id": 25
    }
}
（4）清空登录弹窗
post url: http:masterip:masterport/login-pop-clean
post body:{}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述。
    "entity": {
        "dataList": [   # 刚刚被移除的登录弹窗记录列表
            {
                "content": "我是内容哈哈哈哈",
                "endTime": "2019-12-29 17:30:43",
                "title": "带有图片",
                "pic": "textures/ui/netease_announce/123.png",
                "priority": 12,
                "beginTime": "2019-12-21 17:30:43",
                "_id": 26
            }
            .
            .
            .
        ],
        "version": 1577174776
    }
}
（5）新增浮窗公告
post url: http:masterip:masterport/float-win-new
post body:{
    "content": "我是第1条公告",   # str, 公告正文
    "displayTime": 10,  # int, 公告显示的时间，单位秒
    "lobbyShow": 1, # int, 公告是否在大厅服显示
    "gameShow": 1,  # int, 公告是否在游戏服显示
    "beginTime": "2019-12-21 17:30:43", # str, 显示起始时间，公告会在这个时间点开始显示，允许缺损，缺损时默认为当前时间
    "endTime": "2019-12-29 17:30:43"    # str, 显示结束时间，超过这个时间，公告不会再显示，允许缺损，缺损时默认值为【起始时间】加上一个计算出来的偏移值
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": { # 新增公告的完整信息
        "endTime": "2019-12-29 17:30:43",
        "gameShow": 1,
        "displayTime": 10,
        "content": "我是第1条公告",
        "lobbyShow": 1,
        "beginTime": "2019-12-21 17:30:43",
        "_id": 36
    }
}
（6）发送私人邮件
post url: http:masterip:masterport/mail-send-many
post body:{
    "touids": [12,2310039686],  # list(int), 发送目标的uid列表
    "title": "多人发标题",   # str, 邮件标题
    "content": "邮件内容哈哈哈哈",  # str, 邮件正文
    "itemList": [
        {"itemName": "minecraft:bow",
        "count": 1,
        "enchantData": [[19,1]],
        "auxValue": 0,
        "customTips":"§c new item §r",
        "extraId": "abc"}
    ],					# list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    "expire": 86400,    # int, 邮件有效期，允许缺损，缺损时默认为当前时间加上一个可配置的固定偏移时间
    "srcName": "开发组"    # str, 邮件发送者名字，允许缺损，缺损时默认为空字符串
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {     # 新增的邮件记录内容，同一封邮件发给多人时使用uidList返回对象列表
        "srcName": "开发组",
        "hasRead": 0,
        "cTime": "2019-12-24 16:20:32",
        "title": "多人发标题",
        "number": 2,
        "uidList": [    # 发送的邮件的目标uid列表
            12,
            2310039686
        ],
        "content": "邮件内容哈哈哈哈",
        "expire": "2019-12-25 16:20:32",
        "itemList": [
            {
                "count": 1,
                "enchantData": [
                    [
                        19,
                        1
                    ]
                ],
                "customTips": "§c new item §r",
                "extraId": "abc",
                "itemName": "minecraft:bow",
                "auxValue": 0
            }
        ],
        "getBonus": 0
    }
}
（7）向全部用户群发邮件
post url: http:masterip:masterport/mail-send-to-group
post body:{
    "title": "我是群发的邮件", # str, 邮件标题
    "content": "群邮件内容哈哈哈哈", # str, 邮件正文
    "itemList": [
        {"itemName": "minecraft:bow",
        "count": 1,
        "enchantData": [[19,1]],
        "auxValue": 0,
        "customTips":"§c new item §r",
        "extraId": "abc"}
    ],					# list(dict), 附件物品列表，格式与通用的【物品信息字典】相同（参照ModSDk中往背包中塞物品的字典），额外支持【durability】关键字定义耐久度
    "effectTime": "2019-12-25 23:59:59",    # str, 生效时间，首次登录时间早于此时间的玩家才会收到此邮件，允许缺损，缺损时默认为当前时间
    "expire": 86400,        # int, 邮件有效期，允许缺损，缺损时默认为当前时间加上一个可配置的固定偏移时间
    "srcName": "开发组"        # str, 邮件发送者名字，允许缺损，缺损时默认为空字符串
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，>1代表失败，具体返回码与失败的原因强相关。
    "message": "请求成功",  # 失败原因的具体描述
    "entity": {     # 新增的群发邮件记录
        "srcName": "开发组",
        "effectTime": "2019-12-25 23:59:59",
        "cTime": "2019-12-24 16:27:08",
        "title": "我是群发的邮件",
        "content": "群邮件内容哈哈哈哈",
        "expire": "2019-12-25 16:27:08",
        "itemList": [
            {
                "count": 1,
                "enchantData": [
                    [
                        19,
                        1
                    ]
                ],
                "customTips": "§c new item §r",
                "extraId": "abc",
                "itemName": "minecraft:bow",
                "auxValue": 0
            }
        ],
        "_id": 22
    }
}

更新列表：

1.0.0版本：
初始版本

1.0.1版本：
修正了邮件入口按钮界面遮挡其他同屏按钮响应问题，以及一些分辨率环境下的界面显示问题

1.0.2版本：
修改了返回码的格式定义，现在返回码【1】统一代码成功，>1的返回码与失败的具体原因一一对应

1.0.3版本：
1、邮件附件支持显示方块以及各种原版、自定义物品
2、邮件附件支持发送带耐久度、附魔、customTips\extraId的物品（发送格式有变化，详情请看（6）发送私人邮件与（7）向全部用户群发邮件）
3、增加是否可在未使用云端玩家信息的服务器中领取附件的配置，如果配置为否，那么未使用云端背包的服务器，领取按钮隐藏，且在按钮位置显示文本“当前无法领取”

1.0.4版本：
1、修正一些特殊分辨率下的屏幕适配问题
2、新增【一次登录只出现一次弹窗】配置与相对应的逻辑实现

1.0.5版本：
1、新增打开邮件主界面（客户端）的API
    （3）打开邮件主界面（客户端）
1.0.6版本：
调整UI资源
1.0.7版本：
拆分UI资源
1.0.8版本：
新增API：
    （4）注册玩家收到邮件的回调函数（客户端）
    （5）某UID玩家是否有未读邮件（服务端）
1.0.9版本：
修正API的BUG以及实现的功能：
    （4）注册玩家收到邮件的回调函数（客户端）
新增API：
    （6）反注册玩家收到邮件的回调函数（客户端）
1.0.10版本：
按照新的插件标准实现了界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题
（3）插件UI使用的图片文件尺寸过大影响界面加载速度和占用client内存的问题
1.0.11版本：
新增API
（7）向一组指定uid的玩家发送私人邮件（功能服用）
（8）向所有玩家（无论是否在线）群发邮件（功能服用）
1.0.12版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.13版本：
1、邮件界面的正文内容显示支持下拉
2、提供UI工程