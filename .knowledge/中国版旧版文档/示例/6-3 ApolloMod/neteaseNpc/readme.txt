插件介绍：
该服务器Mod隶属于“功能NPC”插件。
“功能NPC”插件用于在服务器中添加各种功能NPC，当前支持的功能NPC有：
- 转服NPC：玩家点击转服NPC后，会弹出对话框，点击“确认”可转往对应的服务器。


插件构成：
目前“功能NPC”插件包含以下Mod：
- neteaseNpc: 部署于大厅服或游戏服。

数据库：
该插件无需数据库。

使用步骤：
（1）在neteaseNpc的develop_mods/neteaseNpcDev/mod.json中配置要添加的NPC，具体配置参数的意义见文件中的注释；
（2）在部署配置中，将该neteaseNpc添加至需要的大厅服或者游戏服的mods列表中；
（3）部署并启动服务器后，在设定的位置上就能看到功能NPC了。

插件api：
（1）新增一个npc
适用服务器：game, lobby
函数：RegisterExtraNpc(identifier, name, dimensionId, pos, rot, callbackFunc)
参数：
    identifier: str，实体的identifier，建议使用minecraft:npc，假如想使用其他实体的模型，建议使用studio创造基于原版模型的自定义生物，否则可能部分原版实体的额外互动依旧会保留下来（比如说使用村民会在玩家靠近时出现交易按钮）；或者无法正常创建（比如说无法在和平难度下创建基于原版怪物的NPC）
    name：str，NPC头顶的名字
    dimensionId: int，npc出现的维度
    pos: tuple(float,float,float)，npc出现的位置
    rot: tuple(float,float)	，npc的朝向
    callbackFunc: function，npc会敲击之后的回调函数。回调函数包含两个参数：entityId, playerId。entityId：str，被敲击的npc的entityId；playerId：str，敲击npc的玩家的entityId；
返回：
    无
示例：
    import server.extraServerApi as serverApi
    npcSystem = serverApi.GetSystem("neteaseNpc", "npcServer")
    def callbackFunc(entityId, playerId):
        print "callbackFunc entityId={} playerId={}".format(entityId, playerId)
    identifier = "minecraft:npc"
    name = "道具商人"
    dimensionId = 0
    pos = (0, 10, 0)
    rot = (0, 180)
    npcSystem.RegisterExtraNpc(identifier, name, dimensionId, pos, rot, callbackFunc)

版本更新内容：
1.0.2 优化了界面适配，在ipad也能够正常显示

1.0.3 修复了和简易网络服模板UI冲突的问题

1.0.4版本： 
1、新增可通过配置identifier修改NPC外观
2、新增可通过配置调整敲击npc的回调
3、新增动态添加npc的API：
    （1）新增一个npc
