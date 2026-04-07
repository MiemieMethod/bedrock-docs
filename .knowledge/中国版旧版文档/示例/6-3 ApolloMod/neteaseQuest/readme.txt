插件介绍：
该服务器Mod隶属于“任务”插件。
“任务”插件实现游戏任务功能：
- 任务：定义并生效游戏中常见的任务系统（部分任务相关配置于lobby/game下的mod.json）


插件构成：
目前“任务”插件包含以下Mod：
- neteaseQuest：部署于大厅服或游戏服
- neteaseQuestMaster：部署于控制服
- neteaseQuestService：部署于功能服

数据库：
- mysql(rdb)
- redis(nosql)

使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseQuestService中）
（2）在部署配置中，将neteaseQuest添加至需要的大厅服或者游戏服的mods列表中
（3）在部署配置中，将neteaseQuestMaster添加至控制服的mods列表中
（4）在部署配置中，将neteaseQuestService添加至某一个功能服的mods列表中

配置说明：
该插件为MC Studio中组件模板下“任务链模板”的网络游戏版实现
在MC Studio编辑地图，于“关卡编辑器”中配置可运行的任务与对话系统后
**将配置文件dialogueConfigForApollo.py和questConfigForApollo.py复制于本插件的raw目录下（直接将编辑器导出的配置替换插件中的配置未必能成功运行），执行concat.bat（详见"INSTRUCTION.txt"）
即可实现在网络游戏中运行在编辑器中一模一样的任务系统
相应的配置需对应配置时使用的地图文件
建议地图文件单独建立一个服务器mod与该插件共同部署（可参考下方例子）
****注意：behavior与developer中均有dialogueConfig.py配置，两者文件内容需完全一致
例：
（1）创建一个MC Studio中组件模板下的“任务链模板”
（2）于左侧基岩版“组件”标签中找到创建好的“任务链模板”组件，点击“更多”中的“转换为服务器Mod”选项，修改Mod名字（仅限使用英文字母），点击转换按钮
（3）于左侧基岩版“服务器”标签中找到转换好的服务器Mod，点击“更多”中的“打开目录”选项
（4）删除该服务器Mod目录下的developer_mods文件夹（我们只需要配置时的地图）
（5）删除该服务器Mod目录下behavior_packs文件夹（打开至包含entities文件夹那一层）中"script"开头的文件夹（因为“任务链模板”包含单机逻辑这里不需要）
（6）删除该服务器Mod目录下resource_packs文件夹（打开至包含entity文件夹那一层）中的ui文件夹（插件中自带了）
（7）删除该服务器Mod目录下resource_packs文件夹（打开至包含entity文件夹那一层）中textures内的ui文件夹（插件中自带了）
（8）至此我们已获得了一个仅含“任务链模板”组件地图的服务器Mod

配置附加说明：
以下配置中是可扩展字段的示例
dialogueConfig.py
原始部分：
"""
DialogueConfig = {
    ...,
    "2小试身手-交任务": {
        "postAppearDone": "小试身手",
        "npcEntityId": "-12884901870",
        "postAppearDoing": "",
        "dialogueName": "2小试身手-交任务",
        "compositions": [{"select": [{"reply": "领取奖励", "option": {"todo": "", "continue": False, "shift": "", "done": "小试身手"}}], "content": "想不到你有两下子，这些奖励是你该得的。"}],
        "appearCondition": 3,
        "postAppearTodo": "",
	},
	...
}
"""
对话添加部分（自行添加）：
"""
DialogueConfig = {
    ...,
    "2小试身手-交任务": {
        "postAppearDone": "小试身手",
        "npcEntityId": "-12884901870",
        "postAppearDoing": "",
        "dialogueName": "2小试身手-交任务",
        "compositions": [{"select": [{"reply": "领取奖励", "option": {"todo": "", "continue": False, "shift": "", "done": "小试身手"}}], "content": "想不到你有两下子，这些奖励是你该得的。"}],
        "appearCondition": 3,
        "postAppearTodo": "",
→      "npcName": "蒋壮",  # 该NPC生物的名字，编辑器中设置场景中该生物的名字，对应"name"组件GetName方法取到的值
→      "npcEngineIdentifier": "ntestaskdemo:soldier",  # 该NPC生物的引擎identifier
	},
	...
}
"""
- 添加部分补充说明：添加npcName字段与npcEngineIdentifier字段是为了解决于两张不同地图中实体id可能相同但并非同一生物的情况
- npcName: 当配置了该字段（只要出现该字段）且值不为None时，玩家击打NPC触发对话将判断攻击对象的名字，若与该值不相等，则判定攻击对象不能触发此对话，不配置将不做判断
- npcEngineIdentifier: 当配置了该字段（只要出现该字段）且值不为None时，玩家击打NPC触发对话将判断攻击对象的引擎identifier，若与该值不相等，则判定攻击对象不能触发此对话，不配置将不做判断
**该插件实现了NPC头顶显示UI的效果，当玩家附近的NPC有可触发对话时，会根据可触发对话的种类于该NPC头顶显示一个UI图标（闲谈对话类型显示蓝色气泡图标，可接受任务对话类型显示黄色叹号图标，未完成任务对话类型显示灰色问号图标，可完成任务对话类型显示黄色问号图标）
questConfig.py
原始部分：
"""
QuestConfig = {
    ...,
    "逆行者": {
        "spot": [6978.0, 64.0, 87.0],
        "questMobType": "",
        "rewards": {"drugs": [{"type": "minecraft:wooden_sword", "n": 1}, {"type": "minecraft:chainmail_chestplate", "n": 1}], "exp": 10},
        "goal": 1,
        "preconditions": {"lv": 0, "stuff": [], "preQuest": ""},
        "radius": 5,
        "cost": False,
        "questItemType": "minecraft:apple",
        "questName": "逆行者",
        "amount": 1,
        "questType": 3,
        "desc": "找到士兵§a蒋壮",
        "npcEntityId": "-12884901870",
        "limit": 1,
	},
	...
}
"""
对话添加部分（自行添加）：
"""
QuestConfig = {
    ...,
    "逆行者": {
        "spot": [6978.0, 64.0, 87.0],
→      "spotServerType": "gameA",  # 针对于到达地点的任务，标明该点所处服务器的类型
        "questMobType": "",
        "rewards": {"drugs": [{"type": "minecraft:wooden_sword", "n": 1}, {"type": "minecraft:chainmail_chestplate", "n": 1}], "exp": 10},
        "goal": 1,
        "preconditions": {"lv": 0, "stuff": [], "preQuest": ""},
        "radius": 5,
        "cost": False,
        "questItemType": "minecraft:apple",
        "questName": "逆行者",
        "amount": 1,
        "questType": 3,
        "desc": "找到士兵§a蒋壮",
        "npcEntityId": "-12884901870",
        "limit": 1,
→      "naviDestinationDoing": [6978.0, 64.0, 87.0],  # 任务处于进行状态的寻路点，任务结束前都会向该点寻路，前提是mod.json中QuestEnableDefaultNavi的值为true
→      "naviDestinationDone": [6978.0, 64.0, 87.0],  # 任务处于完成状态的寻路点，提交任务前都会向该点寻路，前提是mod.json中QuestEnableDefaultNavi的值为true
→      "naviDestinationDoingServerType": "gameA",  # 标明naviDestinationDoing点所处服务器的类型
→      "naviDestinationDoneServerType": "gameA",  # 标明naviDestinationDone点所处服务器的类型
	},
	...
}
"""
- 添加部分说明：标识了各个点配置所处的服务器
- spotServerType: 当配置了该字段（只要出现该字段）时，将判断玩家所处的服务器类型，不配置将不做判断
- naviDestinationDoing: 当配置了该字段（只要出现该字段）且值不为None时，将为玩家寻路，不配置将不做处理
- naviDestinationDone: 当配置了该字段（只要出现该字段）且值不为None时，将为玩家寻路，不配置将不做处理
- naviDestinationDoingServerType: 当配置了该字段（只要出现该字段）且值不为None时，将判断玩家所处的服务器类型，不配置将不做判断
- naviDestinationDoneServerType: 当配置了该字段（只要出现该字段）且值不为None时，将判断玩家所处的服务器类型，不配置将不做判断

配置整合说明：详见"INSTRUCTION.txt"

插件api：
（1）更改一个玩家的任务数据
函数：UpdateQuestData(uid, mod)
参数：
    uid: 玩家的uid
    mod: 修改任务数据的字典
示例：
    import server.extraServerApi as serverApi
    questSystem = serverApi.GetSystem("QuestMod", "questServerSystem")
    mod = {
        # '逆行者': 1,  # 无视条件直接完成该id的任务
        # '逆行者': 0,  # 无视条件直接添加该id的任务
        '逆行者': -1,  # 从当前未完成的任务中删除该id的任务
    }
    success, msg = questSystem.UpdateQuestData(uid, mod)  # 返回成功与否和对应信息文字
    print(success, msg)

支持的运营指令：
运营指令：
（1）查询一个玩家所有的的任务数据
post url: http:masterip:masterport/query-quest-data
post body:{
    "uid": 996  # 玩家的uid
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，因为需要到游戏服查找，所以没收到返回则代表失败
    "message": "请求成功",
    "entity": {
        "uid": 996,
        "doing": {},  # 所有进行中任务的数据
        "done": {}  # 所有已完成任务的数据
    }
}
（2）更改一个玩家的任务数据
post url: http:masterip:masterport/update-quest-data
post body:{
    "uid": 996,  # 玩家的uid
    "mod": {
        "逆行者": 1
    }
}
response:
{
    "code": 1,  # 返回码，【1】代表成功，因为需要到游戏服操作，所以没收到返回则代表失败，可通过查看游戏服日志获得失败信息
    "message": "操作成功",
    "entity": {}
}

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
添加部分说明，优化concat.py兼容python3
1.0.2版本：
调整UI大小
1.0.3版本：
优化贴图资源，增加部分代码注释
1.0.4版本：
增加部分代码注释

