插件介绍：
该服务器Mod隶属于“主菜单”插件。
“主菜单”插件实现主菜单功能：
- 主菜单：定义并在游戏中生效主菜单（配置于lobby/game下的mod.json）

插件构成：
目前“主菜单”插件包含以下Mod：
- neteaseMenus：部署于大厅服或游戏服

使用步骤：
（1）在部署配置中，将neteaseMenus添加至需要的大厅服或者游戏服的mods列表中

插件api：
（1）设置主菜单按钮状态
适用范围：客户端
函数：UpdateMenus(data)
参数：
    data: dict, 设置按钮状态的字典，格式参照下面例子
返回：
    bool, 是否设置成功，注意设置失败也有可能已经改变了菜单状态
示例：
    import client.extraClientApi as clientApi
    data = {  # key对应按钮序号，从0开始，value为(0, 1)中的一个数字，【0】代表禁用该按钮，【1】代表开启该按钮
        1: 0,
        4: 1,
        16: -1,
    }
    menusSystem = clientApi.GetSystem("neteaseMenus", "neteaseMenusBeh")
    flag = menusSystem.UpdateMenus(data)

（2）获取主菜单所有按钮配置
适用范围：客户端
函数：GetMenus()
参数：
    无
返回：
    menus:dict 主菜单按钮配置，结构对应mod.json中的配置，详见mod.json
示例：
    import client.extraClientApi as clientApi
    menusSystem = clientApi.GetSystem("neteaseMenus", "neteaseMenusBeh")
    menus = menusSystem.GetMenus()  # 结构对应mod.json中的配置，详见mod.json

插件event：
（1）MenusNavigateEvent
适用范围：客户端
命名空间：namespace = 'neteaseMenus', systemname = 'neteaseMenusBeh'
描述：玩家点击了某按钮事件
参数：
    playerId: str, 点击按钮玩家的playerId
    order: int, 被点击按钮的序号，从0开始
示例：
    def __init__(self, namespace, systemName):
        self.ListenForEvent('neteaseMenus', 'neteaseMenusBeh', 'MenusNavigateEvent', self, self.OnMenusNavigate)

    def OnMenusNavigate(self, data):
        print 'OnMenusNavigate', data
        playerId = data["playerId"]
        order = data["order"]
        print '玩家 {} 点击了主菜单中的 {} 号按钮'.format(playerId, order)

更新列表：
1.0.0版本：
初始版本
1.0.1版本：
调整了UI资源，增加了代码注释
1.0.2版本：
按照新规范调整UI和代码
1.0.3版本：
迭代新UI和代码
1.0.4版本：
重构了UI和代码，配置方式也发生了变化
1.0.5版本：
优化插件readme文档描述
