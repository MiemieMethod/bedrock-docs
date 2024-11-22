---
title: Minecraft Beta & Preview - 1.19.10.22
date: 2022-06-08T14:34:14Z
updated: 2022-06-08T15:46:46Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/6757843469453-Minecraft-Beta-Preview-1-19-10-22
---

**发布:** 2022年6月8日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Minecraft悦灵生物](https://feedback.minecraft.net/hc/article_attachments/6757809355277/beta19U1_3_16x9.jpg)

以下是本周测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](http://bugs.mojang.com/)并发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **新特性和漏洞修复**

## **原版趋同**

- 将“盛开的杜鹃树叶”更名为“杜鹃树叶”
- 山羊角的“呼唤”变种现在与Java版的声音相同（[MCPE-154886](https://bugs.mojang.com/browse/MCPE-154886)）
- 山羊角的最后一个声音从“抵抗”更名为“想象”，以匹配Java版（[MCPE-155059](https://bugs.mojang.com/browse/MCPE-155059)）

### **旁观模式（实验性）**

- 在旁观模式下，其他区块中的活动对象不再被剔除

## **悦灵**

- 悦灵现在可以通过下界传送门跟随玩家（[MCPE-155678](https://bugs.mojang.com/browse/MCPE-155678)）

## **悦灵复制**

- 当悦灵听到唱片机播放时，会进行舞蹈动画
- 如果唱片机停止播放，或者悦灵离唱片机太远，它将停止跳舞
- 如果在悦灵跳舞时给予它紫水晶碎片，它会发出小紫水晶的声音，产生一个心形，并复制成另一个悦灵
- 复制后，两个悦灵将有2.5分钟的冷却时间才能再次复制

## **深暗之域**

- 紫水晶簇如果连接到幽匿感测体将不再被摧毁

### **幽匿尖啸体**

- 幽匿尖啸体的粒子现在从后方正确渲染（[MCPE-153591](https://bugs.mojang.com/browse/MCPE-153591)）

## **幽匿催发体**

- 当生物在多个幽匿催发体附近死亡时，只有最近的一个会绽放
- 当幽匿催发体在携带无经验值的生物死亡后绽放时，“它传播”成就不再解锁

### **监守者**

- 不再出现监守者的图形伪影或挖掘粒子效果（[MCPE-153580](https://bugs.mojang.com/browse/MCPE-153580)）

## **青蛙**

- 青蛙不再在浅水流动的水面上产卵（[MCPE-152559](https://bugs.mojang.com/browse/MCPE-152559)）

## **游戏玩法**

- 修复了生物通过下界传送门后消失的问题（[MCPE-155678](https://bugs.mojang.com/browse/MCPE-155678)）
- 抗性效果不再比应有的弱一级（[MCPE-156012](https://bugs.mojang.com/browse/MCPE-156012)）
- 急迫I现在将正确提高玩家的开采速度（[MCPE-102237](https://bugs.mojang.com/browse/MCPE-102237)）
- 潮涌能量I现在赋予急迫I的效果，而不是急迫II
- 像运输船这样的容器实体现在可以在移动设备上无需蹲下即可打开，如果所有座位都已被占用

## **方块**

- 青金石块现在被称为青金石块（[MCPE-105452](https://bugs.mojang.com/browse/MCPE-105452)）
- 切制铜台阶及其变种现在可以在第一次尝试时放置在方块的上半部分（[MCPE-154302](https://bugs.mojang.com/browse/MCPE-154302)）

## **命令**

- 通过命令生成的掠夺者和卫道士队长再次默认是敌对的（[MCPE-116971](https://bugs.mojang.com/browse/MCPE-116971)）

## **常规**

- 确保在加载具有无效值类型的实体JSON架构时不忽略内容错误，涉及以下字段：“Runtime_Identifier”、“Is_Spawnable”和“Is_Summonable”字段的“description”，以及“component_groups”字段和“events”字段的“event”（[MCPE-151381](https://bugs.mojang.com/browse/MCPE-151381)）
- 修复了新用户默认获得操作员权限后无法使用操作员命令的问题
- 修复了给予新用户操作员权限的世界仅给予成员权限的问题

## **移动控制**

- 更新了交互按钮的图标

## **图形**

- 负迷雾开始的迷雾设置不再导致玩家模型在用户界面中的火焰被迷雾颜色污染
- “particles_blend”材质不再在RenderDragon中被剔除

## **物品**

- 修复了从发射器发射的雕刻南瓜未能装备到附近生物的问题

## **生物**

- 鹦鹉再次会被曲奇中毒（[MCPE-151671](https://bugs.mojang.com/browse/MCPE-151671)）

## **玩家**

- 玩家在进入船只时不再会在按住跳跃按钮后无休止地跳跃（[MCPE-155774](https://bugs.mojang.com/browse/MCPE-155774)）

## **稳定性和性能**

- 修复了如果生物具有聚集组件可能导致的崩溃

## **原版趋同**

# **技术更新**

## **附加包和脚本引擎**

- 修复了偏移的投射物未能根据玩家的旋转生成的问题（[MCPE-153880](https://bugs.mojang.com/browse/MCPE-153880)）

**常规**

- 蛋糕方块在切片被吃掉时会发出blockChange游戏事件

## **饥饿**

- 疲劳度组件现在使用新的正确默认值（[MCPE-154238](https://bugs.mojang.com/browse/MCPE-154238)）
  - 请注意，修改player.json的附加包可能需要确保玩家饱和度率设置正确，以匹配默认值（如有需要）

# **实验性特性**

## **常规**

- 将'minecraft:block_light_filter'组件更名为'minecraft:light_dampening'
- 将'part visibility'组件的字段'rules'更名为'conditions'
- 将'crafting_table'组件的字段'custom_description'更名为'table_name'

## **稳定性和性能**

- 启用假日创作者功能切换时，加载世界不再需要很长时间