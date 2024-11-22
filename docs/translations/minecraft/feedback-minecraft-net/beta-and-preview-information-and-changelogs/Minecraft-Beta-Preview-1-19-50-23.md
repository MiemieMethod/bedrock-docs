---
标题: Minecraft Beta & Preview - 1.19.50.23
日期: 2022-11-01T17:54:50Z
更新: 2022-11-03T15:26:57Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/10309733836429-Minecraft-Beta-Preview-1-19-50-23
---

**发布于:** 2022年11月3日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![Picture1.jpg](https://feedback.minecraft.net/hc/article_attachments/10309737817741)

以下是本周Minecraft预览和Beta中的新内容！请记得通过 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback) 向我们反馈您的意见，并将任何漏洞报告给 [bugs.mojang.com](http://bugs.mojang.com/)。  

**实验性功能**

**API**

- 修复了在某些情况下属性速度返回不正确值的漏洞 ([MCPE-152715](https://bugs.mojang.com/browse/MCPE-152715))
- 添加了函数 *canPlace* - 返回在指定位置（和可选的方块面）放置所需方块类型或方块排列是否有效
- 添加了函数 *trySetPermutation* - 通过首先检查 *canPlace* 来尝试在指定位置放置所需的方块排列

**竹木系列**

- “运输竹筏”的显示名称现在为“带箱子的筏子” ([MCPE-163327](https://bugs.mojang.com/browse/MCPE-163327))
- 从筏子和带箱子的筏子上下来时，现在显示正确的提示框 ([MCPE-163326](https://bugs.mojang.com/browse/MCPE-163326))

**方块**

- 使用控制器时，所有变种的告示牌和悬挂式告示牌的“放置”提示现在正确显示
- 生物现在能够正确在侧附悬挂式告示牌上进行寻路

**骆驼**

- 玩家不再能在深水中骑乘骆驼 ([MCPE-163608](https://bugs.mojang.com/browse/MCPE-163608))
- 坐着的骆驼在加载时不再播放坐下动画，而是直接以坐姿加载
- 骆驼现在可以在不跳跃的情况下自动跨越一块半的高度 ([MCPE-163322](https://bugs.mojang.com/browse/MCPE-163322))

**命令**

- 从命令方块运行 '/execute as' 不再继承实体的旋转 ([MCPE-162680](https://bugs.mojang.com/browse/MCPE-162680))

**游戏玩法**

- 修复了悬挂式告示牌可以替代孢子花和大型垂滴叶的问题
- 修复了悬挂式告示牌可以附着在竹子树苗上的问题
- 修复了在双层竹马赛克台阶上使用取块时或破坏它时会得到竹台阶的问题 ([MCPE-163906](https://bugs.mojang.com/browse/MCPE-163906))
- 修复了被活塞推动时竹子树苗不破坏的问题

**常规**

- 修复了链式命令方块在延迟刻数大于0时不会激活的漏洞

**声音**

- 修复了悬挂式告示牌不受方块音量影响的问题  

**功能** **和漏洞修复**

**游戏玩法**

- 船和带箱子的船在被活塞推动时不再传送到 (0, 0, 0) ([MCPE-163330](https://bugs.mojang.com/browse/MCPE-163330))

**常规**

- 修复了升级前1.18世界时不正确的LevelChunk混合问题 ([MCPE-162480](https://bugs.mojang.com/browse/MCPE-162480))

**图形**

- 为兼容驱动程序添加了对Intel集成/独立显卡的D3D12支持

**物品**

- 修复了书与羽毛笔无法签署和关闭的问题 ([MCPE-163325](https://bugs.mojang.com/browse/MCPE-163325))

**领域**

- 上传世界和附加包时缩短文本以适应对话框
- 加入空置数分钟的领域时不再出现错误消息

**稳定性和性能**

- 玩家在物品栏中有包含生物的物品时，浏览配方书不再导致显著的性能下降 ([MCPE-146462](https://bugs.mojang.com/browse/MCPE-146462))
- 减少物品进出漏斗时的服务器延迟 ([MCPE-68796](https://bugs.mojang.com/browse/MCPE-68796))

**触控控制**

- 修复了新触控控制方案中卸下按钮模糊的问题 ([MCPE-156722](https://bugs.mojang.com/browse/MCPE-156722))

**用户** **界面**

- 修复了口袋UI物品栏屏幕中的一个漏洞，导致在创造模式下无法将物品放回物品栏
- 修复了口袋UI物品栏屏幕中的一个漏洞，导致“可制作/所有”切换只能在搜索标签中更改，而不能在其他标签中更改
- 在Xbox上，使用鼠标移动相机时，重新打开菜单时不再改变鼠标位置 ([MCPE-162890](https://bugs.mojang.com/browse/MCPE-162890))
- 选定物品堆叠数量的文本颜色现在为白色而不是黄色

**原版趋同**

- 被重命名武器击杀时不再产生带有多余's'的死亡消息 ([MCPE-163283](https://bugs.mojang.com/browse/MCPE-163283))

**旁观模式**

- 在告示牌上输入时进入旁观模式时，告示牌文本屏幕现在会关闭
- 如果在压力板上单独站立时切换到旁观模式，您将失去重量，压力板会释放 ([MCPE-163177](https://bugs.mojang.com/browse/MCPE-163177))  

**技术更新**

**稳定性和性能**

- 修复了Xbox控制器摇杆死区和灵敏度的问题 ([MCPE-162847](https://bugs.mojang.com/browse/MCPE-162847))

**命令**

- 移除了新执行命令语法的即将到来的创作者功能要求
- 现在需要版本1.19.50才能运行新命令语法
- 当前在命令方块中使用新执行命令语法的创作者需要修改这些命令方块以更新命令
- 当前在行为包中使用新执行命令的创作者需要将最小引擎版本更改为1.19.50
- 之前的执行命令语法仍可通过使用版本1.19.40或更低版本来使用