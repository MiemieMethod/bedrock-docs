---
标题: Minecraft Beta & Preview - 1.19.50.24
日期: 2022-11-09T15:56:10Z
更新: 2022-11-09T16:44:33Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/10506822020877-Minecraft-Beta-Preview-1-19-50-24
---

**发布时间:** 2022年11月9日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![R19U5_5_1080.jpg](https://feedback.minecraft.net/hc/article_attachments/10506811228301)

以下是本周Minecraft预览版和测试版的新内容！请记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。  
  

# **新特性和漏洞修复**

## **生物**

- 更新了恼鬼的模型和纹理
  - 恼鬼保留了稍大的击中箱，以便于战斗

## **游戏玩法**

- 修复了一个漏洞，玩家在靠近收缩活塞时可能会被移动到墙的另一侧
- 修复了蜜蜂带着花蜜离开时蜂箱不获得蜂蜜的问题 ([MCPE-163938](https://bugs.mojang.com/browse/MCPE-163938))

## **触控控制**

- 在玩家飞行并使用触控控制时，使键盘输入与其他控制模式一致。现在，双击“空格”键可以正确禁用触控控制模式下的飞行
- 修复了一个问题，该问题阻止在扩展的创造模式物品栏中通过将物品丢弃到另一个物品上来丢弃物品 ([MCPE-162124](https://bugs.mojang.com/browse/MCPE-162124))

## **命令**

- 运行‘/execute align xyz entity’现在会产生命令错误，而不是崩溃 ([MCPE-162733](https://bugs.mojang.com/browse/MCPE-162733))

# **技术更新**

## **生物**

- "input_ground_controlled"不再意味着在玩家控制下增加自动步伐。可以使用"variable_max_auto_step"组件。为了与之前的版本保持一致，请使用"base_value": 1.0625和"jump_prevented_value": 0.5625