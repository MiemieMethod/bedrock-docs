插件介绍：
地图属性插件，地图属性插件用于设置整个地图的一些通用属性，包括：
1、是否开启主城保护
2、是否禁止藤蔓生长
3、是否禁止流体流动
4、是否定时清理掉落物 与 定时清理掉落物间隔
5、在地图指定位置设置浮空文字
6、设置地图边界（玩家走出边界会被传送回最近离开的合法位置）
7、设置玩家是否可丢弃物品
8、玩家是否可捡起物品
9、可以根据针对地图编辑器导出的地图文件替换游戏地图


插件构成:
（1）neteaseMapAttrs:部署于大厅服或游戏服。
（2）neteaseMapAttrsMaster：部署于控制服，

使用步骤：
（1）配置game中的mod.json，请按照文件mod.json中"_comment"注释配置对应内容。
（2）MCStudio把neteaseMapAttrs添加到大厅服或游戏服，把neteaseMapAttrsMaster添加到控制服。
（3）使用本插件提供的运营指令完成游戏功能。

关于功能9的补充说明:
(0)由于现在mcstudio中的"地图保存"的功能只能在game服使用，因此本功能（功能9）只能在game服使用
(1)地图编辑器导出多个structure
(2)把这些mcstructure文件放置于behavior_packs/neteaseMapAttrsBehavior/structures/mapStructure目录下面
(3)把当中的json文件里面的内容拷贝覆盖到developer_mods/neteaseMapAttrsDev/mapStructureConfig之下，并命名为neteaseMapStructureConfig.json
(4)服主配置mod.json中的change_uid和change_map_dimension，详细见comment注释
(5)服主配置mod.json中的map_area_limit，使这个“地图边界”坐标范围大于自己需要替换地图的范围
(6)服主使用本插件，MCstudio游戏配置中选择“保存地图”，启动一个apollo游戏
(7)服主用change_uid的账号进入游戏，本插件将会把mcstructure文件的地图放置到指定位置
(8)服主退出游戏，关闭apollo，apollo将自动保存地图
(9)使用完这个功能之后，如果服主不再需要此插件的其余功能，可以把此插件从使用列表里去掉；如果还需使用本插件其余功能，则请自行删除behavior_packs/neteaseMapAttrsScript/structures/mapStructure下面的所有的mcsturcture文件，和developer_mods/neteaseMapAttrsDev/mapStructureConfig下面的neteaseMapStructureConfig.json文件
(10)服主在MCstudio中选择自己刚保存的地图，重新部署游戏，即可完成地图替换

插件api：
（1）判断指定区域是否在地图边界之内（服务端）
适用服务器：game/lobby
函数： IsInAreaLimit(minPos, maxPos)
参数：
    minPos: tuple(int,int,int), 指定区域(x, y, z)坐标的最小值
    maxPos: tuple(int,int,int), 指定区域(x, y, z)坐标的最大值
返回：
    bool: 指定区域全部在地图边界之内时返回True；指定区域部分或全部在地图边界之外时返回False
示例：
    import server.extraServerApi as serverApi
    mapSystem = serverApi.GetSystem("neteaseMapAttrs", "neteaseMapAttrsServer")
    inArea = mapSystem.IsInAreaLimit((-4, -4, -4), (4, 4, 4))
    if inArea:
        print "check IsInAreaLimit area is in limit"
    else:
        print "check IsInAreaLimit area is out of limit"
    
运营指令：
（1）设置指定服务器地图边界。
post url: http:masterip:masterport//mapAttrs/set-area-limit
post body:{
	"type": "gameA",      # 目标服务器类型。每种类型只有一个服务器，通过服务器类型区分不同服务器。
	"minPos" : [-50,0,-50], # 地图边界(x, y, z)坐标的最小值
	"maxPos": [50,20,50] # 地图边界(x, y, z)坐标的最大值
}
response:
{
    "message": "",
    "code": 1, #1表示成功，2表示失败
    "entity": ""
}

版本更新内容：
1.0.1版本
新增维度地图保存功能

1.0.2版本
新增API：
（1）判断指定区域是否在地图边界之内（服务端）




