---
标题: Minecraft Beta - 1.16.220.50 (Xbox One/Windows 10/Android)
日期: 2021-03-04T16:09:30Z
更新: 2021-03-05T08:18:56Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360057402352-Minecraft-Beta-1-16-220-50-Xbox-One-Windows-10-Android
---

**发布于:** 2021年3月4日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防止丢失
- Beta构建可能不稳定，并且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

## **新实验性功能：**

在本周的Beta中，我们有一些令人兴奋的新洞穴和悬崖特性，可以通过在您的世界中启用“实验性功能”开关来访问！（您可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)了解有关使用开关的更多信息。）

**请注意：** 在此Beta中，旧生成和新生成之间的融合尚未最终确定。我们希望确保尊重玩家的旧世界升级到新的世界生成，并努力改善生物群系的融合，以便在完整的洞穴和悬崖发布时达到最佳效果！

您可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中留下对这些功能的反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的任何新漏洞。

 

![img_752.JPG](https://feedback.minecraft.net/hc/article_attachments/360088354971/img_752.JPG)

## **山脉**

- 引入新的山脉子生物群系：高耸的山峰、雪盖山峰、积雪山坡、山脉林地和山脉草甸！
- 为了适应新的山脉，我们将世界高度从256提升到320个区块，新的山脉生成高度最高可达256个区块
- 对于真正的登山者：铁矿、煤矿和绿宝石矿石在山脉中生成
- 更新了铁矿、煤矿、绿宝石、钻石、金矿、青金石、铜矿和红石矿石的纹理
- 山脉地形现在将作为主世界生成的一部分生成
- 将山羊的生成位置从极端丘陵移至积雪山坡，并允许兔子在山脉林地中生成

## **发光鱿鱼**

- 发光鱿鱼已重新引入Beta！
- 发光鱿鱼在受到伤害时现在会发出发光的墨水粒子（[MCPE-117500](https://bugs.mojang.com/browse/MCPE-117500)）
- 玩家现在可以使用染料为告示牌文本上色
- 鱿鱼的模型不再在-Y方向上偏移（[MCPE-114253](https://bugs.mojang.com/browse/MCPE-114253)）
- 添加了发光鱿鱼、荧光墨囊和荧光物品展示框

# **漏洞修复**

**滴水石修复：**

- 在水中放置小型滴水石块不再导致水被移除
- 当悬挂的小型滴水石开始掉落时，其位置现在具有正确的偏移
- 调整了小型滴水石的视觉形状以匹配Java版
- 在放置小型滴水石时下蹲可以防止对立的钟乳石和石笋合并
- 站在石笋上跳跃时着陆会造成半颗心的跌落伤害
- 小型滴水石现在具有正确的击中箱
- 小型滴水石块不再被流动的熔岩摧毁
- 小型滴水石在手中时现在具有正确的大小和旋转
- 钟乳石死亡消息不再以句号结束
- 掉落的钟乳石现在造成正确的跌落伤害
- 小型滴水石在下界中仅滴落熔岩（[MCPE-115393](https://bugs.mojang.com/browse/MCPE-115393)）
- 被滴水石杀死时现在显示正确的死亡消息
- 现在为滴水石和小型滴水石块播放正确的声音（[MCPE-115283](https://bugs.mojang.com/browse/MCPE-115283)）
- 当在滴水的钟乳石下方时，炼药锅现在可以填充水或熔岩（[MCPE-115363](https://bugs.mojang.com/browse/MCPE-115363)）
- 将三叉戟扔在小型滴水石块上会摧毁它（[MCPE-115281](https://bugs.mojang.com/browse/MCPE-115281)）
- 添加了滴水石块。它可以由四个小型滴水石制作而成

**性能和稳定性：**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了在铁砧上尝试重命名地图时可能发生的崩溃，当第二个槽位被占用时（[MCPE-112905](https://bugs.mojang.com/browse/MCPE-112905)）

**一般：**

- 细雪不再可以放置在已经包含其他方块的位置，例如栅栏柱或铁栏杆
- 发光告示牌在DX11和移动平台上不再未点亮（[MCPE-117524](https://bugs.mojang.com/browse/MCPE-117524)）
- 活动对象选择器不再允许在禁用作弊时自我选择（[MCPE-92635](https://bugs.mojang.com/browse/MCPE-92635)）
- 投射物现在可以穿过结构空位方块（[MCPE-103579](https://bugs.mojang.com/browse/MCPE-103579)）
- 僵尸、僵尸村民、尸壳、掠夺者和卫道士使用正确的骨骼来附着盾牌（[MCPE-98606](https://bugs.mojang.com/browse/MCPE-98606)）
- 拾取盾牌的生物现在将其放置到副手中
- 访客在死亡时现在会掉落物品栏（[MCPE-47563](https://bugs.mojang.com/browse/MCPE-47563)）
- 改进了在台阶、台阶块和顶部雪块侧面放置方块的规则
- 控制器现在能够在侏罗纪世界包的高级设置NPC屏幕中选择“按钮模式”开关（[MCPE-66446](https://bugs.mojang.com/browse/MCPE-66446)）

**命令**

- 命令方块链中的命令方块在添加新的常加载区域之前将列出正确数量的常加载区域
- 标题命令不再在消息中重复%符号（[MCPE-51033](https://bugs.mojang.com/browse/MCPE-51033)）
- 使用执行命令的传送现在使用原点的维度进行操作（[MCPE-44104](https://bugs.mojang.com/browse/MCPE-44104)）

**市场**

- 市场库存内搜索的“结果”字段现在在屏幕的不同部分之间正确更新

**辅助功能**

- 在新的成就屏幕上启用了触控输入的屏幕朗读功能
- 修复了在使用VR时文本转语音读取错误文本的漏洞

**村庄**

- 村民不再能够穿过墙壁在床旁边睡觉

## **技术修复和更改**

**GameTest框架的各种更新：**

- 更新了方块简写助手为驼峰命名法
- 更新了方块简写，仅包含原版方块
- 添加了Blocks.get以获取方块并在不存在时返回null
- 添加了BlockStates以枚举所有方块状态
- 添加了setState到方块以更新其方块状态
- 添加了BlockPos类
- 添加了ItemStack类游戏测试模块：
- 添加了Tags以枚举所有内置标签
- 更新了所有接受x、y、z位置的方法以接受BlockPos
- 在注册游戏测试时暴露填充
- 修复了先前失败的GameTest标记仍在新世界中显示的问题

**移动预测**

- 修复了在第三方服务器上投射物忽略服务器移动数据包的问题
- 当检测到玩家移动修正或异常时，服务器将调整玩家的下落距离，以考虑客户端玩家的位置

**其他：**

- 更改了GameTest包的加载方式。附加文件由主文件引用，如manifest.json中的“entry”字段所指定
- 在某些世界中，黑屏不再覆盖暂停菜单中的玩家图标。内容创作者不再需要同时覆盖focus_border_frame.png和pause_screen_border.png以获得正确的行为
- 由于市场世界模板的过时资源包导致的缺失纹理的断言已更改为内容日志错误
- 物品现在可以应用“transparentattachable”标签，使附着物品在第一人称视角中不渲染给玩家
- 修复了V2村民在初始化时未正确更新其molang变量的问题

**网络数据包**

- 将UDP流的密码算法更改为AESGCM256