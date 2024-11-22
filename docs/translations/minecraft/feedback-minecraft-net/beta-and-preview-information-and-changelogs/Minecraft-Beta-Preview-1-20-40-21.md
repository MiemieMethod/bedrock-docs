---
标题: Minecraft Beta & 预览 - 1.20.40.21
日期: 2023-09-12T17:31:51Z
更新: 2023-09-12T17:35:57Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/19424781869837-Minecraft-Beta-Preview-1-20-40-21
哈希:
  h_01HA57AKDPSZZM52SPJ6BTFD7G: 实验性特性
  h_01HA57AKDP5BPRXCKBTYCDNN3A: 村民交易重新平衡
  h_01HA57AKDPP25W7Q2V2VJHTAKE: 特性和漏洞修复
  h_01HA57AKDPTMTJAHQQXCNDPFG2: 性能与稳定性
  h_01HA57AKDPRJH2NMR6YVTCSRCK: 原版趋同
  h_01HA57AKDP4SVWEPAE724RJ48Y: 游戏玩法
  h_01HA57AKDPJQS2JV9JW8DSTBFY: 物品
  h_01HA57AKDP7R8V4EJQNB2J1JQB: 触控控制
  h_01HA57AKDP4GDGZQCTS5J9WPGR: 技术更新
  h_01HA57AKDPXGHHB3JMZN41CBW4: 附加包和脚本引擎
  h_01HA57AKDPV161CE4C9QE9ZAG5: API
  h_01HA57AKDPTDDXM4KE4AZMZRMC: 实验性技术更新
  h_01HA57AKDPMMJ6XFKJG57CYD9J: 图形
  h_01HA57AKDQC2DCHR4DJP10X32F: 物品-1
---

**发布:** 2023年9月13日

**关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![r20u4-2_patchnotes.png](https://feedback.minecraft.net/hc/article_attachments/19424855494797)

以下是本周Minecraft预览和Beta中的新内容！一如既往，我们非常希望听到您对这些实验的看法，因此请将您的反馈和想法发送至 [aka.ms/MC120Feedback](http://aka.ms/MC120Feedback) 并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。  
  

# 实验性特性

## 村民交易重新平衡

- 制图师的新七张探险地图现在也可以指向已探索区块中的结构  
    

# 特性和漏洞修复

## 性能 / 稳定性

- 修复了在Spellrune市场地图的Archold房间中运行时可能发生的崩溃

## 原版趋同

- 水的闪烁声音发生了变化 ([MCPE-174524](https://bugs.mojang.com/browse/MCPE-174524))
  - 进入和退出水时的环境声音现在仅在活动对象浸没在水中低于视线水平时播放，符合Java版
  - 进入水时的闪烁声音已更新以匹配Java版
- HUD上的Boss条现在与Java版相同颜色 ([MCPE-43591](https://bugs.mojang.com/browse/MCPE-43591))
- 骆驼在熔岩或水中不再能够冲刺
- 铁傀儡不再自然生成在2格高的空间中，以免窒息 ([MCPE-173006](https://bugs.mojang.com/browse/MCPE-173006))

## 游戏玩法

- 如果箭被阻挡，玩家不再受到箭的效果影响 ([MCPE-52904](https://bugs.mojang.com/browse/MCPE-52904))
- 末地和下界的村庄不再保存到主世界 ([MCPE-85954](https://bugs.mojang.com/browse/MCPE-85954))

## 物品

- 铁桶再次可以从含水方块中移除水，除非完全浸没 ([MCPE-174529](https://bugs.mojang.com/browse/MCPE-174529))

## 触控控制

- 当“使用摇杆冲刺”选项关闭时，为骆驼添加了冲刺按钮 ([MCPE-172674](https://bugs.mojang.com/browse/MCPE-172674))
- 修复了在使用触控控制时，潜行按钮部分遮挡D-Pad上按钮的问题 ([MCPE-38566](https://bugs.mojang.com/browse/MCPE-38566))  
    

# 技术更新

## 附加包和脚本引擎

- "minecraft:transformation"现在防止方块被转换超过30x30x30像素限制，并且"minecraft:unit_cube"不再被平移或缩放。无效方块将显示为“更新”方块 ([MCPE-173799](https://bugs.mojang.com/browse/MCPE-173799))

## API

- 发布了*World.getMoonPhase*、*MoonPhase*和*MoonPhaseCount* v1.6.0  
    

# 实验性技术更新

## 图形

- 修复了在延迟技术预览中粒子未持续被照亮的问题

## 物品

- 从版本1.20.40开始，弃用"minecraft:weapon"组件
- 从版本1.20.40开始，弃用"minecraft:on_use"组件
- 从版本1.20.40开始，弃用"minecraft:on_use_on"组件