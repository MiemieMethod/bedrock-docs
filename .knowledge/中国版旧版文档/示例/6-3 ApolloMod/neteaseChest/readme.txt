插件介绍：
该服务器Mod隶属于“箱子”插件。
“箱子”插件用于在服务器中实现对玩家权限分组的基本功能，有以下三点：
-不同玩家对于放置的箱子有不同的使用权限，分为"拥有者"，"使用者"和"申请使用者"
-拥有者可以摧毁箱子、打开箱子、放入/取出物品；使用者可以打开箱子、放入/取出物品；其它玩家无法摧毁箱子、也无法打开箱子，但是可以申请使用。
-外部可通过运营指令让玩家是否成为某个箱子的使用者
备注：箱子拥有者在潜行状态下可以打开箱子管理界面，但是必须是手里没物品的情况

插件构成：
目前“箱子”插件包含以下Mod：
- neteaseChest: 部署于大厅服或游戏服。


使用步骤：
（1）在neteaseChest的develop_mods/neteaseChestDev/mod.json中配置是否让放置箱子的玩家成为拥有者，具体配置参数的意义见文件中的注释；
（2）该neteaseChest添加至大厅服或者游戏服的mods列表中
（3）部署并启动服务器后，就能使用。

插件api：
（1）开启/关闭某个玩家使用某个箱子的权限
函数: ChangeChestAuth(args):
参数:
    data:dict,包括 箱子坐标，玩家id，打开/关闭玩家使用箱子的权限
示例:
    import server.extraServerApi as serverApi
    neteaseChestServerSystem = serverApi.GetSystem("neteaseChest", "neteaseChestDev")
    args = {
	"playerUid":1221323256, #玩家UID
	"ChestPos":[1395, 67, 29], #箱子坐标
	"isOpen":true #true让玩家成为使用者，false让玩家不能使用某箱子
	}
    neteaseChestServerSystem.ChangeChestAuth(args)
（2）让某个玩家成为某个箱子拥有者
函数: ChangeChestOwn(args):
参数:
    data:dict,包括 箱子坐标，玩家id
示例:
    import server.extraServerApi as serverApi
    neteaseChestServerSystem = serverApi.GetSystem("neteaseChest", "neteaseChestDev")
    args = {
	"playerUid":1221323256, #玩家UID
	"ChestPos":[1395, 67, 29] #箱子坐标
	}
    neteaseChestServerSystem.ChangeChestOwn(args)


更新列表：
1.0.0版本：初始版本

1.0.1版本：修改机审错误

1.0.2版本：增加持久存储箱子数据功能，修复上个版本遍历获取箱子数据的弊端

1.0.3版本：优化了界面适配，在ipad也能够正常显示

1.0.4版本：扩展私有箱子插件，使私有箱子插件能使用于除了箱子之外的一些容器，如木桶，潜匿之贝箱子，陷阱箱，末影箱，发射器，投掷器

1.05版本：扩展私有箱子插件，增加漏斗可以使用私有箱子插件，同时对于一些拥有私有权限的容器，如果拥有者和漏斗不一样，将不能交互


