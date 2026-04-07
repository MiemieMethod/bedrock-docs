插件介绍：
该服务器Mod隶属于“外观管理”插件。

插件构成：
目前“外观管理”插件包含以下Mod：
- neteaseAppear：部署于大厅服或游戏服


数据库：
- mysql


使用步骤：
（1）请在mysql中执行mod.sql
（2）在部署配置中，将neteaseAppear添加至需要的大厅服或者游戏服的mods列表中
（3）根据ModSDK文档需求使用编辑器输出外观资源
（4）根据注释要求填写mod.json

注意事项：
（1）由于特效和模型基本都只能绑定到骨骼模型，而不是原版模型上，所以特地制作了一个类steve的骨骼模型作为模型模型
（2）一个具体的外观可以由一个或多个挂接模型、序列帧特效、粒子特效组成，比如说示例中的光环特效就是使用了一个序列帧特效+一个粒子特效实现


插件api：
（1）打开外观商店
函数：OpenShopUI(playerId)
参数：
    playerId: 玩家的entityId
示例：
    import server.extraServerApi as serverApi
    dailySystem = serverApi.GetSystem("neteaseAppear", "neteaseAppearDev")
    dailySystem.OpenShopUI(playerId)


更新列表：
1.0.0版本：
初始版本
1.0.1版本：
按照新的插件标准实现了界面，解决了以下问题：
（1）多个插件之间界面穿插、按钮点击响应问题
1.0.2版本：
1、使用公开稳定的API：SetLayer和SetVisible替换set_visible和set_layer，避免有时候出现UI错乱问题
1.0.3版本：
1、提供UI工程