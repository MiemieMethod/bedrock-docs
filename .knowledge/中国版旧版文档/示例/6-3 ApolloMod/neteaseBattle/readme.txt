插件介绍：
该服务器Mod隶属于“战斗系统”插件。
“战斗系统”插件实现的功能：
- 可以为实体设置多种属性（可扩展属性种类）；支持一个简单的玩家属性显示界面；
- 实现基于插件属性的战斗结算，不走原生的伤害结算；
- 投掷物的伤害结算也走统一的插件属性；也就是说，玩家射出一只箭，这只箭对目标造成的伤害是和玩家的近战攻击一样；
- 支持装备能够为玩家增加额外属性，且装备的属性会显示在tips中；
- 特殊事项：“战斗系统”插件不支持创造模式，在创造模式下部分逻辑表现可能存在异常
- 特殊事项：对应无源伤害（例如掉落，日照引燃僵尸等），目前统一处理为归零
- 特殊事项：当前额外装备穿戴数据记录在地图中，云端玩家信息插件的后续版本将支持在不同的地图中同步这些信息。

插件构成：
目前“公告”插件包含以下Mod：
- neteaseBattle: 部署于大厅服或游戏服。



数据库：
- 无

使用步骤：
（1）在部署配置中，将neteaseBattle添加至需要的大厅服或者游戏服的mods列表中；
（2）参照下方的配置说明和mod.json中的注释，配置好生物与装备的属性。
（3）部署并启动服务器后，就可以在主界面左上角看到玩家新的血条，在居中略偏右的位置看到打开玩家属性详情的按钮，

mod.json配置说明：
- 支持属性类型列表配置
"extra_attrs":[		# 配置生物/装备一共有哪些自定义属性（类型为List），此列表中属性的先后顺序等于界面中属性的显示顺序（最大生命值和当前生命值必然显示在第一、第二行）
  {						# int类型的属性配置举例
    "key":"health",		# 属性字符串ID，不允许重复
    "style":"int",		# 属性数据类型，【int】代表整数，默认值为0；【float】代表浮点数，默认值为0.0
    "name":"生命值"		# 属性的显示名字
  },
  {
    "key":"attack",
    "style":"int",
    "name":"攻击"
  },
  {
    "key":"defence",
    "style":"int",
    "name":"防御"
  },
  {						# float类型的属性配置举例
    "key":"crit",		# 属性字符串ID，不允许重复
    "style":"float",	# 属性数据类型，【int】代表整数，默认值为0；【float】代表浮点数，默认值为0.0
    "name":"暴击",		# 属性的显示名字
    "view":"百分数",	# 属性显示方式，当属性数据类型为浮点数时生效，可选类型为【百分数】和【小数】
    "view_acc":1		# 属性显示精确度，当属性数据类型为浮点数时生效，如果设置为1，表示显示到小数点后1位，如0
  },
  {
    "key":"hit",
    "style":"float",
    "name":"命中",
    "view":"百分数",
    "view_acc":2
  },
  {
    "key":"dodge",
    "style":"float",
    "name":"闪避",
    "view":"百分数",
    "view_acc":2
  }
],
- 支持配置实体的初始属性，配置形式类似以下方式：
"entity_attrs":{		# 固定关键字，用于配置生物属性（类型为Dict）
  "default":{			# 【default】用于没有独立配置的其他生物，default中没有配置的属性，默认值将会是0或者0.0，属性字典的每一个key就是上文【extra_attrs】属性列表中的key
    "health":100,
    "attack":2,
    "defence":1,
    "crit":0.0,
    "hit":0.95,
    "dodge":0.05
  },
  "player":{			# 【player】用于配置玩家的基础属性
    "health":200,
    "attack":10,
    "defence":0,
    "crit":0.1,
    "hit":0.95,
    "dodge":0.05
  },
  "minecraft:sheep":{	# 其他生物的key为其字符串ID。
    "health":200,
    "attack":0,
    "defence":0,
    "crit":0.0,
    "hit":0.0,
    "dodge":0.0
  }
},
- 支持配置装备提供的额外属性，配置形式类似以下方式：
- 假如配置的物品格式为[namespace:name:auxvalue]那么只有符合auxvalue的物品才被认为是装备物品
- 假如配置物品格式为[namespace:name]，那么任意auxvalue的此类物品均为同种装备物品
"equip_attrs":{					# 固定关键字，用于配置装备提供的额外属性（类型为Dict），装备额外属性没有默认值，此处没有配置的物品，不被认为是装备
  "minecraft:diamond_sword":{	# 装备品的key为其字符串ID。
    "name": "绝世好剑",			# 固定关键字，装备的自定义名字，目前只影响背包界面上的tips
    "attack":10,
    "hit":0.2
  },
  "minecraft:diamond_helmet":{
    "name": "绝世好头",
    "health":1000,
    "defence":10
  },
  "minecraft:diamond_chestplate":{
    "name": "绝世好胸",
    "health":1000,
    "defence":10
  },
  "minecraft:diamond_leggings":{
    "name": "绝世好腿",
    "health":1000,
    "defence":10
  },
  "minecraft:diamond_boots":{
    "name": "绝世好脚",
    "health":1000,
    "defence":10
  },
  "minecraft:shield":{
    "name": "绝世好盾",
    "health":1000,
    "defence":10
  }
}
- 其他配置项请关注mod.json的注释

插件api：
（1）打开属性界面（客户端）
函数：OpenStatusUi()
参数：无
返回值：无
示例：
    import client.extraClientApi as clientApi
    system = clientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
    system.OpenStatusUi()
（2）获取物品属性字典（客户端）
函数：GetEquipAttrDict(itemName, auxValue)
参数：
    itemName:str 物品的identifier例如"minecraft:apple"
    auxValue:int 物品的扩展值
返回值：
    attrDict:dict(attrName:attrValue) 字典形式返回此物品的附加属性
示例：
    import client.extraClientApi as clientApi
    system = clientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
    attrDict = system.GetEquipAttrDict(itemName, auxValue)
    for attrName, attrValue in attrDict.iteritems():
        print "attrName=%s attrValue=%s" % (attrName, attrValue)
（3）获取属性格式化字符（客户端）
函数：GetFormatAttr(attrName, attrValue)
参数：
    attrName:str 属性关键字，例如attack等
    attrValue:int/float 属性值，例如10，0.1等
返回值：
    data:tuple(strName,strValue) strName（属性的格式化文字名）；strValue（属性的格式化数组，百分比类型的属性，0.1会转化为10%）
示例：
    import client.extraClientApi as clientApi
    system = clientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
    strName, strValue = system.GetFormatAttr(attrName, attrValue)
    print "strName=%s strValue=%s" % (strName, strValue)
（4）获取物品属性字典（服务端）
函数：GetEquipAttrDict(itemName, auxValue)
参数：
    itemName:str 物品的identifier例如"minecraft:apple"
    auxValue:int 物品的扩展值
返回值：
    attrDict:dict(attrName:attrValue) 字典形式返回此物品的附加属性
示例：
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    attrDict = system.GetEquipAttrDict(itemName, auxValue)
    for attrName, attrValue in attrDict.iteritems():
        print "attrName=%s attrValue=%s" % (attrName, attrValue)
（5）获取属性格式化字符（服务端）
函数：GetFormatAttr(attrName, attrValue)
参数：
    attrName:str 属性关键字，例如attack等
    attrValue:int/float 属性值，例如10，0.1等
返回值：
    data:tuple(strName,strValue) strName（属性的格式化文字名）；strValue（属性的格式化数组，百分比类型的属性，0.1会转化为10%）
示例：
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    strName, strValue = system.GetFormatAttr(attrName, attrValue)
    print "strName=%s strValue=%s" % (strName, strValue)
（6）通知控件刷新背包界面物品显示（服务端）
函数：DeclareBagChanged(playerId)
参数：
    playerId:str 需要刷新背包物品显示的玩家的entityId
返回值：无
示例：
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    system.DeclareBagChanged(playerId)
（7）注册新增装备位装备被替换的侦听事件（服务端）
函数：RegisterExtraEquipChangeCallback(func)
参数：
    func： function 新装备位装备被替换的回调函数，函数定义为func(eventData)，eventData为一个字典，具体数据如下：
        slot：int 装备的位置，6=耳环，7=项链，8=腰带，9=戒指
        playerId：str 玩家的entityId
        oldItemName：str 旧装备的identifier，即"命名空间:物品名"，minecraft:air代表旧装备为空
        oldItemAuxValue：int 旧装备的附加值，当oldItemName=minecraft:air时，此属性不存在
        oldItemModExtralId：str 旧装备的自定义标识符。可以用于保存数据， 区分物品，当oldItemName=minecraft:air时，此属性不存在
        newItemName：str 新装备的identifier，即"命名空间:物品名"，minecraft:air代表新装备为空
        newItemAuxValue：int 新装备的附加值，当oldItemName=minecraft:air时，此属性不存在
        newItemModExtralId：str 新装备的自定义标识符。可以用于保存数据， 区分物品，当oldItemName=minecraft:air时，此属性不存在
返回值：
        idxKey：int 回调函数的唯一ID，用于取消回调
示例：
    def OnEquipChange(eventData):
        print "OnEquipChange", eventData
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    idxKey = system.RegisterExtraEquipChangeCallback(OnEquipChange)
（8）取消注册的新增装备位装备被替换的侦听事件（服务端）
函数：CancelExtraEquipChangeCallback(idxKey)
参数：
    idxKey：int RegisterExtraEquipChangeCallback函数返回的唯一ID
返回值：无
示例：
    def OnEquipChange(eventData):
        print "OnEquipChange", eventData
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    idxKey = system.RegisterExtraEquipChangeCallback(OnEquipChange)
    system.CancelExtraEquipChangeCallback(idxKey)
（9）设置为和平模式（服务端）
函数：SetPeaceMode(isPease)
参数：
    isPease：bool 是否设置为和平模式。True的时候表示为和平模式，无法造成伤害，适合非战斗场景使用；False的时候表示为非和平模式，适合战斗场景
返回值：无
示例：
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    system.SetPeaceMode(True)
（10）设置玩家指定等级的属性（服务端）
函数：SetPlayerAttrBaseWithLevel(level, extraAttrs)
参数：
    level：int 需要设置属性的等级
    extraAttrs：dict(string=>int/float) 属性名==》属性值的字典，假如某个属性名缺损，则会使用mod.json中的配置的默认值替换
返回值：无
示例：
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    extraAttrs = {
        "health":100,
        "attack":2,
        "defence":1,
        "crit":0.1,
        "hit":0.95,
        "dodge":0.05,
    }
    system.SetPlayerAttrBaseWithLevel(0, extraAttrs)
（11）设置返回玩家指定等级属性的回调函数（服务端）
函数：RegisterPlayerAttrBaseWithLevelCallback(func)
参数：
    func：function 定义为func(level)，传入参数为需要获取属性的等级，返回值为属性名==》属性值的字典，使用此接口可以实现玩家属性随等级变化
返回值：无
示例：
    system = serverApi.GetSystem("neteaseBattle", "neteaseBattleDev")
    def levelCallback(level):
        return {
            "health":100+20*level,
            "attack":2+2*level,
            "defence":1+2*level,
            "crit":0.1,
            "hit":0.95+0.05*level,
            "dodge":0.05,
        }
    system.RegisterPlayerAttrBaseWithLevelCallback(levelCallback)

聊天巫师指令：
1、mod.json支持“是否开启查看属性指令”开关，							
开启该开关时，在聊天中输入@op showinfo指令，就会在聊天栏中打印范围5以内的实体属性。							

与面板描述插件联动说明：
若该插件联动面板描述插件，则需要设置某物品格式化规则，更新战斗插件后在behavior_packs下找到与modMain.py同级目录下的fmt.py文件
若不填写该文件或删除该文件则走预设代码显示规则（具体效果请自行查看）
下面简述fmt.py文件填写规则（战斗插件附魔没有效果，则不显示附魔栏）
-示例：
FMT = {
    "minecraft:diamond_sword": {  # 此处对应战斗插件物品配置属性时的名称，如果某种装备不需要定制物品面板显示逻辑则不要出现在FMT字典中，若物品名称出现于FMT字典中但下列键均缺失则正常走预设逻辑显示该装备的物品面板
        "name": "§g大宝剑",  # 定义装备的名称，缺失则代表自动获取，必须完整填写，要么不要出现键'name'
        "part": "§g太刀",  # 定义装备的部位名称，缺失则代表自动获取，必须完整填写，要么不要出现键'part'
        "quality": "§g史诗",  # 定义装备的品质文字，缺失则显示空字符串，必须完整填写，要么不要出现键'part'，若该键与键'part'均缺失，则不显示品质栏
        "desc": ["此刀只应天上有，", "即出入无人之境。"],  # 定义装备的描述文本，若需要显示这一栏则对应值必须是长度大于1的列表或元组，不需要显示这一栏则不要设置'desc'键
        "durability": ["§g久耐", "§g"],  # 定义装备的耐久文字，若需要显示这一栏则对应值必须是长度为2的列表或元组，其中的第一个元素为替换“耐久”的文本，第二个元素为当前物品耐久值的颜色符号，不需要颜色则填空字符串，，不需要显示这一栏则不要设置'durability'键
        "attrs": ["§g", "§g"],  # 定义装备的属性格式，左侧写法为定义属性文本与属性值的颜色（一一对应）并自动获取改装备的属性值与属性文本，若想只显示某些属性，则参考下一个装备该处的配置，不需要显示这一栏则不要设置'attrs'键
        "gem": ["§g", "§g"]  # 宝石同上
    },
    "minecraft:golden_sword": {
        'attrs': [("§g(health)", "§g(health)"), ("§g避闪", "§g可以打字(dodge)都行")]  # 文本均不宜过长，具体显示效果自行调试，一个字符串内括号只能出现一组
    }
}
FMT配置中，某个特定物品，假设此物品的identifier为(nameSpace:uniqueName)，附加值为(auxValue)，那么此物品的面板显示逻辑按照以下的优先级选择具体的配置，高优先级的key不存在的情况下，才会选择相对低优先级的key：
1、第一优先级为（nameSpace:uniqueName:auxValue）
2、第二优先级为（nameSpace:uniqueName）
3、第三优先级为（nameSpace:default）
4、第四优先级为（default）

更新列表：
1.0.0版本：
初始版本
1.0.1版本
1、增加玩家的Paperdoll显示。
2、提供9个装备位：
    5个原生装备位：头盔、胸甲、裤子、鞋子、盾牌，这5个装备位的装备会显示模型效果，同原生
    4个新增装备位：耳环、项链、腰带、戒指，这4个装备位没有模型效果，但会增加玩家的属性
    显示背包栏，背包栏会显示物品
3、增加配置：
    9个部位的可装备物品列表						
4、增加API接口：
    （1）打开属性界面（客户端）
    （2）获取物品属性字典（客户端）
    （3）获取属性格式化字符（客户端）
    （4）获取物品属性字典（服务端）
    （5）获取属性格式化字符（服务端）
    （6）通知控件刷新背包界面物品显示（服务端）
5、当前额外装备穿戴数据记录在地图中，云端玩家信息插件的后续版本将支持在不同的地图中同步这些信息。
1.0.2版本
修正机审错误
优化部分界面
1.0.3版本
1、添加对宝石插件的支持
2、再次优化部分界面，适应一些手机的特殊界面
1.0.4版本
1、调整部分代码逻辑
2、增加新装备替换的侦听事件
    （7）注册新增装备位装备被替换的侦听事件（服务端）
    （8）取消注册的新增装备位装备被替换的侦听事件（服务端）
1.0.5版本
增加对称号属性的支持
1.0.6版本
增加对PVP插件的支持
1.0.7版本
1、可以在lobby服等和平场景打开属性展示界面以及完成装备脱穿。
    新增API：（9）设置为和平模式（服务端）
2、支持接口，指定角色在不同等级的属性。（属性需在extra_attrs中配置）
    新增API：（10）设置玩家指定等级的属性（服务端）
    新增API：（11）设置返回玩家指定等级属性的回调函数（服务端）
    mod.json新增配置：【player_status_change_with_level】玩家属性是否与等级相关
3、支持调整是否在主界面显示玩家属性的入口按钮
    mod.json新增配置：【show_status_btn_on_desk】是否在主界面显示打开属性的按钮
1.0.8版本
调整UI资源，增加注释
1.0.9版本：
上传了由大贴图拆分的小贴图
1.0.10版本
1、完善与面板描述插件联动逻辑，具体见【与面板描述插件联动说明】
1.0.11版本
重新整合了界面UI，解决多插件并存时，界面穿插与阻挡响应问题
1.0.12版本
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.13版本
提供UI工程


