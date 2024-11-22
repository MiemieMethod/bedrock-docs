---
标题: Minecraft Beta & Preview - 1.19.30.21
日期: 2022-08-10T14:11:52Z
更新: 2022-08-10T16:02:41Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/8316873349901-Minecraft-Beta-Preview-1-19-30-21
---

**发布于:** 2022年8月10日

## **Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta可在Android（Google Play）上使用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，展示了悦灵携带物品，还有一些熊猫和鹦鹉在丛林环境中。](https://feedback.minecraft.net/hc/article_attachments/8316783630733/beta19U3_2_16x9.jpg)

以下是本周Minecraft预览和Beta中的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](https://bugs.mojang.com/)并发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

 

# **新特性和漏洞修复**

## **原版趋同**

### **旁观模式（实验性）**

- 玩家肩上的鹦鹉在进入旁观模式时会跳下
- 具有*follow_owner*行为的动物和生物不再跟随旁观者
- 具有*find_mount*行为的动物和生物不再尝试骑乘旁观者
- 旁观模式的玩家不会感到寒冷，冰霜行者附魔现在不再影响水

### **一般**

- 修复了在盔甲架上放置时光源方块会被移除的问题（[MCPE-151856](https://bugs.mojang.com/browse/MCPE-151856)）

### **生物**

- 修复了疣猪兽和僵尸疣猪兽的击中箱大小和击中范围，使其与Java版一致（[MCPE-65424](https://bugs.mojang.com/browse/MCPE-65424)）

## **命令**

- 更改了/locate命令中某些结构的名称，添加了下划线，类似于Java版（例如：ancientcity -\> ancient_city）；旧名称仍然有效，但不会出现在自动补全中

# **新特性和漏洞修复**

## **游戏玩法**

- 在/structure命令和结构方块的加载选项卡中添加了一个含水字段，以便玩家在结构放置在水下时能够正确含水
- 添加了键盘快捷键，允许玩家复制当前坐标或方块的坐标
  - Control + Alt + C是复制当前坐标的默认快捷键
  - Control + Alt + X是复制选定方块坐标的默认快捷键
  - 需要在创作者设置中启用“启用复制坐标UI”
- 同时按下Ctrl和Alt键将不再导致Alt键被卡住

## **物品**

- 铁栏杆不再缺失于创造模式物品栏，并且可以通过命令再次访问（[MCPE-160253](https://bugs.mojang.com/browse/MCPE-160253)）
- 白色带釉陶瓦不再缺失于创造模式物品栏，并且可以通过命令再次访问

## **市场**

- 市场中的角色创建器在退出更衣室时不再丢失缩略图

## **用户界面**

- 在Xbox云同步提示中添加了重试按钮
- 海草和海带不再被归类为创造模式物品栏中的珊瑚装饰（[MCPE-44034](https://bugs.mojang.com/browse/MCPE-44034)）
- 在着火时，火焰覆盖层不再穿透持有的物品（[MCPE-147776](https://bugs.mojang.com/browse/MCPE-147776)）

# **技术更新**

## **稳定性和性能**

- 浏览市场时游戏不再崩溃

# **实验性特性**

## **活动对象属性**

- 限制可以在活动对象属性相关的Molang表达式中使用的查询。属性默认只能使用query.had_component_group，*set_property*只能使用*property*和*query.has_property*

## **一般**

- *BlockDisplayNameComponent*将不再在给定的显示名称前附加'tile.'和'.name'，如果找不到适当的本地化，将显示其给定的原始字符串