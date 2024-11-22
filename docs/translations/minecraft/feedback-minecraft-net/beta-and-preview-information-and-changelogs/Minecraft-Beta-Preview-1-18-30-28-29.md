---
标题: Minecraft Beta & Preview - 1.18.30.28/29
日期: 2022-03-23T08:44:18Z
更新: 2022-03-28T22:58:50Z
分类: Beta 和 Preview 信息与更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/5005390908301-Minecraft-Beta-Preview-1-18-30-28-29
---

**发布于:** 2022年3月23日

### **警告: 在测试版中打开你的世界可能会导致区块损坏！**

**更新:** 此问题已在版本1.18.30.30/31中解决。

我们发现当前的Beta和Preview版本存在一个问题，导致Y=0以下的区块可能会损坏。我们正在努力发布新版本以防止此问题的发生。为了避免区块损坏，请在更新发布之前不要打开你的世界。

 

## 关于Minecraft Preview和Beta的信息: 

- 预览版本: 1.18.30.29 \| Beta版本: 1.18.30.28
- 尽管预览和Beta的版本号不同，但游戏内容没有差异
- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft Preview可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![sculk_beta_16x9.jpg](https://feedback.minecraft.net/hc/article_attachments/5005341013389/sculk_beta_16x9.jpg)

嘿！谁关掉了光源？还有声音？这里非常黑暗，而且非常、非常安静。呃哦。这一定意味着……不。已经？好吧，根据我周围发光的幽匿块，深暗之域已经进入本周的Beta了！如果你敢的话，快来吧，这里有幽匿块可以研究，还有潜行可以进行。你这次不必特别小心，因为你在这里真的会是一个人。但要做好准备，监守者最终会出现。

以下是本周Beta中的新内容！和往常一样，请搜索并报告你可能发现的任何漏洞，访问[bugs.mojang.com](http://bugs.mojang.com/)。

 

# **实验性特性**

## **深暗之域**

- 深入地下深处，揭开Minecraft中最黑暗的生物群系——深暗之域
  - 昏暗而阴森，深暗之域肯定会让即使是最勇敢的玩家心生恐惧
  - 深暗之域的表面覆盖着幽匿块
  - 唯一在深暗之域栖息的生物是监守者
  - **请注意:** 监守者尚未进入游戏，但它正在为它的首次亮相做准备！

## **斧**

- 原版趋同: 用斧攻击抬起的盾牌将使盾牌失效5秒

## **运输船**

- 功能类似于矿车箱子，但在船上，因此你可以在水上旅行并携带你的物品
- 通过将箱子与任何船结合制作而成

## **悦灵**

- 悦灵在交付物品后现在有延迟才能拾取新物品 ([MCPE-152978](https://bugs.mojang.com/browse/MCPE-152978))
- 悦灵现在只会拾取它所持有的完全相同的物品
- 悦灵现在会保持靠近附近播放的音符盒
- 悦灵现在免疫来自其主人的伤害

## **数据驱动物品**

- 在伤害事件响应中添加了一个可选的"mob_amount"参数，用于指定被生物使用时的独特伤害量

**铜号角**

- 我们没有计划对铜号角进行任何额外更改，但我们很想听听你对这个实验性特性的看法，以及如果它进入最终更新你可能如何使用它！请在这里发送你的反馈: [aka.ms/MCGoatsFeedback](https://aka.ms/MCGoatsFeedback)

# **特性与漏洞修复**

## **移动控制**

- 修复了新触控控制方案中灵敏度过低的问题 ([MCPE-152985](https://bugs.mojang.com/browse/MCPE-152985))
- 修复了“始终高亮”选项在“触控”交互模式下可见的情况 ([MCPE-152972](https://bugs.mojang.com/browse/MCPE-152972))
- 修复了新移动控制方案的按钮在某些设备上过大且过高的问题

## **游戏玩法**

- 修复了在世界生成期间未将水下熔岩湖转化为黑曜石的问题 ([MCPE-128022](https://bugs.mojang.com/browse/MCPE-128022))
- 治疗不再使生物免疫伤害 ([MCPE-152957](https://bugs.mojang.com/browse/MCPE-152957))
- 修复了刻范围检查排除了实际上在范围内的区块
- 破坏与花朵在同一方块中放置的雪层不再摧毁花朵 ([MCPE-151512](https://bugs.mojang.com/browse/MCPE-151512))

### **疣猪兽**

- 幼年疣猪兽现在会攻击玩家 ([MCPE-152577](https://bugs.mojang.com/browse/MCPE-152577))

## **用户界面**

- 双击潜行按钮将不再切换飞行模式 ([MCPE-152973](https://bugs.mojang.com/browse/MCPE-152973))
- 修复了在按住Ctrl键时撞击障碍物后未恢复冲刺状态的问题 ([MCPE-152979](https://bugs.mojang.com/browse/MCPE-152979))

# **技术更新**

## **活动对象**

- 添加检查以防止作为乘客的活动对象被其所乘载具骑乘，从而防止无限循环查找根载具 ([MCPE-133774](https://bugs.mojang.com/browse/MCPE-133774))

## **生物**

- 骑乘具有锁定旋转的生物时，旋转将不再意外地向一侧跳转，当该生物正在旋转时

## **WebSocket** 

- 从WebSocket服务器和代码构建器API发送的事件的JSON格式已更新为层次JSON格式，而不是扁平格式
- 移除了不太有用的属性，方块和物品ID已移至基于名称的新格式，而不是数字格式
- WebSocket中的基于代理的命令已移至新的“action:agent”格式，所有命令现在都被排队并包含唯一ID以关联响应
- 未来对WebSocket和代码构建器API的任何重大更改将导致“protocolVersion”递增