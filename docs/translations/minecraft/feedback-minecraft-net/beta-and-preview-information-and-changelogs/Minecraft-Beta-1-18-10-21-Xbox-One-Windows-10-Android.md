---
title: Minecraft Beta - 1.18.10.21 (Xbox One/Windows 10/Android)
date: 2021-12-01T16:10:31Z
updated: 2021-12-01T17:10:10Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4415247692173-Minecraft-Beta-1-18-10-21-Xbox-One-Windows-10-Android
---

**发布于：** 2021年12月1日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明。

 

![Minecraft中的恶地生物群系](https://feedback.minecraft.net/hc/article_attachments/4415268992013/Screen_Shot_12-01-21_at_03.59_PM.JPG)

 

又到了Bedrock测试版的时间！一如既往，我们非常感谢您发送给我们的所有反馈，请在[bugs.mojang.com](http://bugs.mojang.com/)搜索并报告您可能发现的任何漏洞。

 

# **实验性特性**

- 添加了新的实验性开关“荒野更新”
  - 通过启用此开关，现在可以访问幽匿块的特性
  - 更多特性将在未来的测试版中推出。这仅仅是开始！

# **非实验性特性和漏洞修复**

## **世界生成**

- 风蚀恶地生物群系中的石柱底部不再在下面的洞穴中形成平坦的天花板（[MCPE-146984](https://bugs.mojang.com/browse/MCPE-146984)）
- 睡莲不再在沼泽生物群系下的含水层中生成（[MCPE-125913](https://bugs.mojang.com/browse/MCPE-125913)）
- 化石现在可以在Y=0以下生成，使用深层钻石矿石方块而不是煤矿石方块（[MCPE-144065](https://bugs.mojang.com/browse/MCPE-144065)）
- 化石不再在洞穴或水中漂浮生成
- 废弃矿井现在总是在基岩层上方生成（[MCPE-147575](https://bugs.mojang.com/browse/MCPE-147575)）
- 洞穴生物群系中的生物群系装饰特性现在与Java版具有相似的频率

## **游戏玩法**

- 熔炉现在在完成烧炼后始终输出预期数量的物品（[MCPE-126004](https://bugs.mojang.com/browse/MCPE-126004)）
- 光源方块的光强度现在可以在按住右键/互动时定期增加（[MCPE-137647](https://bugs.mojang.com/browse/MCPE-137647)）
- 光源方块的光强度现在可以在触控输入设备上更改
- 当'checkForBlocks'为真且目标被阻挡时，传送命令将不再成功
- 修复了第一人称副手盾牌防御动画（[MCPE-125340](https://bugs.mojang.com/browse/MCPE-125340)）
- 修复了双持盾牌时的第一人称防御动画

## **生物**

- 美西螈的行走动画现在受到迅捷的影响（[MCPE-131322](https://bugs.mojang.com/browse/MCPE-131322)）
- 狼现在会正确反应受到伤害
- 生物再次可以跳过方块以拾取物品
- 当物品放置在生物手中时，物品数据不再损坏（[MCPE-145034](https://bugs.mojang.com/browse/MCPE-145034)）

## **用户界面**

- 修复了使用游戏手柄导航时设置菜单的标签顺序
- 删除了多个屏幕上的双空格拼写问题，包括反馈提示（[MCPE-104037](https://bugs.mojang.com/browse/MCPE-104037)）
- 修复了“将购买保存到Microsoft帐户”屏幕上的屏幕阅读器问题

## **原版趋同**

- 袭击Boss条现在显示“袭击 - 胜利”，并且在击败袭击后从地面发射烟花（[MCPE-51267](https://bugs.mojang.com/browse/MCPE-51267)）

## **Android**

- 添加了警告提示，解释在Android设备上将文件存储位置设置为外部时可能会丢失数据

# **技术更新**

## **稳定性和性能**

- 执行命令时性能有所改善

## **动画**

- 修复了在默认状态中定义的动画控制器事件在控制器立即过渡到另一个状态时被跳过的问题（这是一个版本更改，仅适用于从format_version 1.18.10开始的动画控制器）

## **命令**

- 通过/execute触发的函数调用顺序现在是一致的（[MCPE-111849](https://bugs.mojang.com/browse/MCPE-111849)）
- 添加了带有生成战利品重载的/loot命令

## **JumpToBlockGoal**

- 当生物在水中时，JumpToBlockGoal不再可用

# **实验性特性**

## **GameTest框架**

### **mojang-minecraft**

- 世界
  - 添加了blockBreak和blockPlace事件，当玩家在世界中破坏或放置方块时调用
- BlockExplodeEvent
  - 将destroyedBlock重命名为block
- 玩家
  - 添加了方法startItemCooldown(itemCategory : string, durationTicks : int) - 为给定持续时间（以刻为单位）开始或重置物品类别（例如，ender_pearl）的冷却时间
  - 添加了方法getItemCooldown(itemCategory : string) - 返回该玩家在给定物品类别上的剩余持续时间（以刻为单位）。如果没有冷却时间，则返回0。
- ItemCooldownComponent
  - 添加了ItemCooldownComponent（item.getComponent("minecraft:cooldown")）
  - 只读属性cooldownCategory : string - 表示此物品的冷却类别。
  - 只读属性cooldownTicks : int - 表示如果启用冷却，此物品的冷却时间（以刻为单位）
  - 方法startCooldown(player : Player) - 如果启用此物品的冷却，则为给定玩家开始或重置此物品的冷却时间
- ItemType
  - 移除了getName方法，添加了只读属性.id

### **mojang-gametest**

- 测试
  - 添加了gameMode: GameMode参数到spawnSimulatedPlayer方法
- SimulatedPlayer
  - 将destroyBlock重命名为breakBlock
  - 将stopDestroyingBlock重命名为stopBreakingBlock
  - 移除了selectSlot方法
  - 添加了属性selectedSlot : int - 获取或设置玩家当前选择的快捷栏槽位
