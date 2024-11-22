---
标题: Minecraft Beta - 1.18.20.27 (Xbox / Windows / Android)
日期: 2022-02-17T15:23:18Z
更新: 2022-02-17T16:45:57Z
类别: Beta 和预览信息及变更日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4438936661517-Minecraft-Beta-1-18-20-27-Xbox-Windows-Android
---

**发布于:** 2022年2月17日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问真实世界，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明
- Minecraft预览版玩家可能会收到略有不同的版本号，但这里的修复和功能应该是相同的。更多信息可以在这里找到：[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)。

![carrots_bees.jpg](https://feedback.minecraft.net/hc/article_attachments/4438927740429/carrots_bees.jpg)

 

是时候进行另一次更新了，以下是本周测试版的新内容！如往常一样，请在[bugs.mojang.com](http://bugs.mojang.com/)搜索并报告您可能发现的任何漏洞。

 

## **Minecraft预览版：**

- Windows和iOS上的Minecraft预览版玩家现在可以加入彼此的游戏！

## **已知问题：**

- 我们知道某些Android设备在创建世界时可能会崩溃。这种情况最多只会发生一次，之后您可以正常创建世界。

# **功能和漏洞修复**

## **游戏玩法**

- 修复了如果物品或区块名称包含“.”，则活动对象定义标识符无法被识别的问题
- 伤害现在计算得更准确，我们现在正确计算并存储较大伤害的部分伤害
- 在高难度和低难度下的生物伤害略有调整
- 盔甲和保护减少的计算变得更加准确
- 龙息攻击现在正确造成伤害（[MCPE-94317](https://bugs.mojang.com/browse/MCPE-94317)）
- 玩家在重新加入世界时，如果在熔岩中退出，位置将保持不变（[MCPE-82480](https://bugs.mojang.com/browse/MCPE-82480)）
- 玩家现在可以在创造模式中通过梯子和其他可攀爬的方块（如藤蔓）向下飞行而不停止（[MCPE-82480](https://bugs.mojang.com/browse/MCPE-82480)）
- 修复了一个漏洞，导致盾牌阻挡动画在阻挡一次后停止平滑播放（[MCPE-149838](https://bugs.mojang.com/browse/MCPE-149838)）

## **图形**

- 修复了“carrots_stage_3”纹理文件名不正确且未在游戏中显示的问题（[MCPE-152175](https://bugs.mojang.com/browse/MCPE-152175)）

## **生物**

- 蜜蜂在被精准采集摧毁蜂箱时不再变得愤怒（[MCPE-83550](https://bugs.mojang.com/browse/MCPE-83550)）
- 烈焰人的火球、尖牙攻击伤害和潜影弹现在在所有难度下造成一致的伤害
- 小岩浆怪的伤害略有增加，从普通模式下的2提高到3
- 蜘蛛的伤害略有减少，从普通模式下的3降低到2（[MCPE-94878](https://bugs.mojang.com/browse/MCPE-94878)）
- 幼年僵尸疣猪兽的伤害略有减少，从普通模式下的1降低到0.5
- 骷髅的近战攻击伤害略有减少，从普通模式下的3降低到2
- 狼的伤害略有增加，从普通模式下的3提高到4
- 幼年疣猪兽不再攻击玩家
- 牛、猪、鸡和绵羊不再在寒冷的针叶林生物群系中生成

## **用户界面**

- 触控控制中的按钮在玩家超出按钮区域时不再卡在按下状态（[MCPE-151921](https://bugs.mojang.com/browse/MCPE-151921)）
- 修复了在新用户界面中，某些Android设备上的文本显示不正确的问题（[MCPE-151916](https://bugs.mojang.com/browse/MCPE-151916)）
- 修复了在使用控制器玩时，悬停在合成菜单的搜索栏上可能发生崩溃的问题

## **市场**

- 硬币购买界面现在包括“硬币起始收纳袋”可在某些平台上购买
- 点击“查看更多”时游戏不再卡住/崩溃
- 市场标签现在适合描述部分
- 下载弹出窗口在关闭时不再闪烁
- 客户端现在支持市场页面中的多个玩家数量标签
- 当尝试在角色创建器物品装备时装备皮肤包皮肤时，市场页面添加了警告弹出窗口

## **角色创建器**

- 修复了导致某些表情在动画结束时出现意外旋转的问题（[MCPE-134328](https://bugs.mojang.com/browse/MCPE-134328)）

# **技术更新**

## **AI意向**

- 为回家意向暴露了新的数据参数“calculate_new_path_radius”。这是用于指定生物被认为足够接近当前路径末端的区块距离。然后将计算新的路径以继续朝向家
- 为击退咆哮意向添加了击退高度上限值

## **动画**

- 修复了时间轴事件在0.0时有时不在循环动画中运行的漏洞

## **生物**

- 修复了命令方块在极限速度跑者市场地图中无法召唤生物的问题

# **技术实验性功能**

- 由于引擎限制，使用假日创作者功能实验性切换的方块的“minecraft:geometry”数据现在限制为仅允许在\[0,0,0\]到\[15,15,15\]的空间中使用几何体。任何从行为包加载的超出此限制的方块将呈现为info_update方块，并在日志中显示内容错误。

## **GameTest框架**

- 为活动对象暴露以下组件。每个组件都有一个value属性，包含组件的数据。
  - minecraft:variant
  - minecraft:skin_id
  - minecraft:mark_variant
  - minecraft:friction_modifier
  - minecraft:ground_offset
  - minecraft:scale
  - minecraft:push_through

**mojang-gametest模块：**

- 从命令/gametest clearall中移除radius参数
- 修改了函数attack()的行为，使模拟玩家即使在未找到目标时也能挥动

**mojang-minecraft模块：**

- 添加事件entityHit(entityHitEvent: EntityHitEvent, options?: EntityEventOptions) - 当一个实体或区块被另一个实体击中时触发
- 函数playSound(soundID: String, soundOptions: SoundOptions) - 为玩家播放声音，其他实体无法听到该特定玩家的声音  

## **交互组件**

- 现在有两个新字段，GiveItem和TakeItem，指定是否可以从实体的主手槽中给/取物品。取走物品也会掉落生物的物品栏

## **物品**

- 当武器被生物使用时，武器事件正确应用（[MCPE-118692](https://bugs.mojang.com/browse/MCPE-118692)）