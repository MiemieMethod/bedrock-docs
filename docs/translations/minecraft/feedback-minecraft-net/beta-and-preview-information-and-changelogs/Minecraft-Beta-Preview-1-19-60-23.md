---
title: Minecraft Beta & Preview - 1.19.60.23
date: 2022-12-07T16:11:52Z
updated: 2022-12-08T09:32:40Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/11259038367245-Minecraft-Beta-Preview-1-19-60-23
---

**发布于：** 2022年12月7日

**注意：** ~~本周的预览版本在iOS上不可用。我们为此带来的不便表示歉意，并正在努力解决该问题。~~ **更新：** 我们现在已解除阻碍，希望也能在iOS上发布预览版本。

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一张Minecraft截图，展示了雕纹书架和骆驼。](https://feedback.minecraft.net/hc/article_attachments/11258984583053)

以下是本周Minecraft预览和Beta中的新内容！记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。  
  

# **实验性特性**

## **游戏玩法**

- 雕纹书架在世界加载时不再触发侦测器方块

# **特性和漏洞修复**

## **方块**

- 重生锚在用精准采集开采或拾取时不再保留其充能 ([MCPE-145682](https://bugs.mojang.com/browse/MCPE-145682))
- 脚手架现在在其下方的方块被摧毁时会显示粒子并产生振动 ([MCPE-163738](https://bugs.mojang.com/browse/MCPE-163738))
- 幽匿尖啸体的尖啸声现在可以在32个区块的更远距离被听到 ([MCPE-163989](https://bugs.mojang.com/browse/MCPE-163989))

## **游戏玩法**

- 竹子树苗放置时不再替换双植物 ([MCPE-99806](https://bugs.mojang.com/browse/MCPE-99806))
- 营火不再点燃玩家和生物，但仍会造成伤害 ([MCPE-98931](https://bugs.mojang.com/browse/MCPE-98931))
- 营火不再摧毁矿车和船 ([MCPE-109489](https://bugs.mojang.com/browse/MCPE-109489))
- 末影珍珠不再传送正在睡觉的玩家 ([MCPE-161189](https://bugs.mojang.com/browse/MCPE-161189))

## **图形**

- 玩家在骑马、骡或驴时不再能透视2个方块高的空间的地形 ([MCPE-133984](https://bugs.mojang.com/browse/MCPE-133984))

## **物品**

- 需要支撑方块的方块在放置在部分方块或空气上时现在能正确显示在地图上 ([MCPE-159713](https://bugs.mojang.com/browse/MCPE-159713))

## **生物**

- 劫掠兽现在能够在泥巴等各种部分方块上攻击 ([MCPE-162483](https://bugs.mojang.com/browse/MCPE-162483))
- 发光鱿鱼在水外生成时现在会发出粒子

## **用户界面**

- 修复了结构方块用户界面，使Y值字段可以仅通过键盘访问 ([MCPE-164148](https://bugs.mojang.com/browse/MCPE-164148))

# **技术更新**

## **组件**

- 扩展了“minecraft:shooter”组件，以定义多个可以指定不同投射物定义和条件过滤器的投射物
- 暴露了更多字段给射手组件，以允许更多投射物自定义，例如投掷力量、声音，以及攻击是否为魔法攻击

## **Molang**

- 修复了一个漏洞，即在Molang中将任何值除以动态确定的负变量时，结果变为除以正（绝对）值
  - 这是一个Molang版本变更，仅对使用min_engine_version为1.19.60或更高版本的包中的Molang表达式生效

## **投射物**

### **组件**

- 传送其拥有者的投射物在拥有者睡觉时不再进行传送 ([MCPE-161189](https://bugs.mojang.com/browse/MCPE-161189))

## **API（实验性）**

- 添加了方法 setOnFire(seconds: number, useEffects?: boolean = true): boolean)，该方法将实体点燃（如果它不在水中或降雨中）。
- 添加了方法 extinguishFire(useEffects?: boolean = true): void，该方法将火熄灭。
- 如果实体着火，可以调用 getComponent('minecraft:onfire')，返回类型为 EntityOnFireComponent的对象，该对象具有属性 onFireTicksRemaining。
- 修复了一个漏洞，即 viewDirection将返回上一个刻的方向
- 修复了一个漏洞，即 getEntitiesFromViewDirection将使用上一个刻的方向
- 修复了一个漏洞，即 getBlockFromViewDirection将使用上一个刻的方向
- 修复了一个漏洞，即 headLocation将返回上一个刻的位置
- 将ScriptScriptCommandMessageEvent重命名为ScriptEventCommandMessageEvent