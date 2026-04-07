插件介绍：
该服务器Mod隶属于“宝石”插件。
“宝石”插件实现为装备镶嵌宝石功能，属于战斗插件的扩展（属性相关的配置需根据战斗插件的配置规则配置于战斗插件下），类似于一个属性养成系统的模板，部分配置与说明详见mod.json

插件构成：
目前“宝石”插件包含以下Mod：
- neteaseJewel：部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseJewel添加至需要的大厅服或者游戏服的mods列表中

插件api：
（1）打开宝石镶嵌操作面板
函数：OpenJewelBoard(uid)
参数：
    uid: 玩家的uid
示例：
    import server.extraServerApi as serverApi
    jewelSystem = serverApi.GetSystem("neteaseJewel", "neteaseJewelDev")
    jewelSystem.OpenJewelBoard(uid)

（2）获取指定物品的可镶嵌的插槽总数（包括已经镶嵌宝石的和尚未镶嵌宝石的）-- 客户端接口
函数：GetAvailableSlot(identifier, auxValue=0)
参数：
    identifier: str, 物品的identifier
    auxValue： int，物品的auxValue，可缺损，缺损时默认值为0
返回值：
    slot：int，物品的插槽总数，没有插槽时返回0
示例：
    import client.extraClientApi as clientApi
    jewelSystem = clientApi.GetSystem("neteaseJewel", "neteaseJewelBeh")
    slot = jewelSystem.GetAvailableSlot("minecraft:diamond_sword", 0)

（3）判定指定物品是否是可镶嵌到装备中的宝石 -- 客户端接口
函数：IsAvailableJewel(identifier, auxValue=0)
参数：
    identifier: str, 物品的identifier
    auxValue： int，物品的auxValue，可缺损，缺损时默认值为0
返回值：
    isGem：bool，True代表是可镶嵌宝石、False代表不是可镶嵌宝石
示例：
    import client.extraClientApi as clientApi
    jewelSystem = clientApi.GetSystem("neteaseJewel", "neteaseJewelBeh")
    isGem = jewelSystem.IsAvailableJewel("minecraft:diamond_sword", 0)


属性计算说明：
宝石相关的数据直接存放于物品的extraId之中，存储结构详见文件jewelServerSystem.py中的第110行至第117行
其中key值以"calculator:"开头的，战斗插件计算属性时
会将整个key里面"calculator:"之后的部分当作ModName，取到在modMain.py中RegisterSystem固定名称为'calc'的类（详见本插件的两个modMain.py文件）,调用固定名称为calc的方法计算本系统提供的属性值（详见calcClientSystem.py与calcServerSystem.py）
开发者可以以这种固定好的规则实现新的养成系统

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
调整了UI与交互方式，增加装备指定槽位个数
1.0.2版本：
新增API共外部mod查询指定装备的插槽数量与判定指定物品是否是宝石
    （2）获取指定物品的可镶嵌的插槽总数（包括已经镶嵌宝石的和尚未镶嵌宝石的）-- 客户端接口
    （3）判定指定物品是否是可镶嵌到装备中的宝石 -- 客户端接口
1.0.3版本：
优化UI资源
1.0.4版本：
修改ui的json名称
1.0.5版本：
补充代码注释
按照新的插件标准，重新实现了宝石镶嵌界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
（2）多个插件之间资源文件重名问题
（3）插件UI使用的图片文件尺寸过大影响界面加载速度和占用client内存的问题
1.0.6版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.7版本：
提供UI工程

