---
title: Minecraft Beta & Preview - 1.21.10.21
date: 2024-05-29T13:04:47Z
updated: 2024-05-30T13:06:54Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/27128575309325-Minecraft-Beta-Preview-1-21-10-21
hash:
  h_01HZ272Z67Q4H3CQ806FP5VD12: 特性与漏洞修复
  h_01HZ272Z67XMTJ9QK1H9EB15G3: 角色创建器
  h_01HZ272Z67SFACG4RW1AEEDAHG: 可自定义控制
  h_01HZ272Z67KMVNK62KYYVVSGK6: 游戏提示
  h_01HZ272Z6736KD2JTS68EW7CJ7: 游戏玩法
  h_01HZ272Z67YZYG3RHQY1YEAV2D: 加载提示
  h_01HZ272Z671B6BDGB62RXS8AXK: 预览领域
  h_01HZ272Z67M9JT5D7Y4209FR63: 稳定性与性能
  h_01HZ272Z67988PVMGPT32V7TBV: 结构方块
  h_01HZ272Z67P0FYXSR1GF9X2NH0: 用户界面
  h_01HZ272Z67VK72H6X2F9GWQ0B1: 技术更新
  h_01HZ272Z67SFYD15WNZ4M1VFN8: 生物群系
  h_01HZ272Z67XCMK9CAFX3WQX2QE: 方块
  h_01HZ272Z672T12GB1W8J06MAJW: 编辑器
  h_01HZ272Z67126DCR5B0388HS2Q: 技术实验性更新
  h_01HZ272Z67XYHQ1VHWYWAJ167X: API
---

**发布于：** 2024年5月29日

**关于Minecraft预览和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、PlayStation 4、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一个热带草原村庄，背景中有一个村民、一个铁傀儡、一只猫和一只犰狳](https://feedback.minecraft.net/hc/article_attachments/27128575303309)

以下是最新Minecraft：基岩版测试版和预览更新中的新内容！请继续在 [feedback.minecraft.net](https://feedback.minecraft.net/) 提交您的建议，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告和投票您发现的任何漏洞！

我们在此预览和测试版中有一些已知问题，旨在尽快解决：

- 无法通过世界选项卡创建新的预览领域
- 玩家不会因窒息而受到伤害
- 游戏邀请在iOS上不会弹出
- 在某些平台的多人设置中缺少“仅邀请”和“对局域网玩家可见”切换选项

# 特性与漏洞修复

## 角色创建器

- 更新了“头饰”、“外套”和“鞋子”的服装间类别名称

## 可自定义控制

- 自定义控制在玩家停止飞行后不再恢复默认设置 ([MCPE-180234](https://bugs.mojang.com/browse/MCPE-180234))
- 当输入模式切换为触控以外的其他模式时，控制自定义界面现在会自动退出
- 当启用可自定义控制时，纸娃娃现在可以在HUD中显示 ([MCPE-176334](https://bugs.mojang.com/browse/MCPE-176334))
- 自定义控制按钮大小在上下移动脚手架或梯子时保持稳定 ([MCPE-178820](https://bugs.mojang.com/browse/MCPE-178820))

## 游戏提示

- 添加了聊天游戏提示。当世界中有远程玩家或启用作弊时，该提示会出现
  - 如果可以为玩家显示聊天游戏提示，则在聊天中发布的打开聊天说明将被移除

## 游戏玩法

- 修复了狼铠破坏时未发出足够的鳞片粒子 ([MCPE-179664](https://bugs.mojang.com/browse/MCPE-179664))
- 骑乘实体不再免疫风弹投射物伤害
- 旗帜再次可以通过配方书获得 ([MCPE-179650](https://bugs.mojang.com/browse/MCPE-179650))
- 调整了下车位置的计算方式，以更好地与移动载具对齐。这可能导致快速下车时出现轻微差异

## 加载提示

- 为加载提示对话框添加了动画标题

## 预览领域

- 现在可以通过编辑世界界面将本地世界上传到预览领域，类似于非预览领域
- 在领域故事成员选项卡的搜索框中输入内容不再覆盖过滤器选项
- 修复了在繁忙领域查看领域故事时可能发生的崩溃
- 领域故事帖子中显示的新行不再被移除

## 稳定性与性能

- 修复了从旧版控制台版转换世界时的物品和方块损坏问题

## 结构方块

- 修复了结构方块菜单中帮助按钮的链接 ([MCPE-179672](https://bugs.mojang.com/browse/MCPE-179672))

## 用户界面

- 刷新了成就界面的资产：所有成就解锁插图、未解锁成就插图和GamerScore图标
- 在死亡界面中添加了一个按钮，用于在极限模式下退出世界（仅限预览）
- 修复了导致半吸收心未渲染的漏洞 ([MCPE-181245](https://bugs.mojang.com/browse/MCPE-181245))

# 技术更新

## 生物群系

- 生物群系组件“minecraft:forced_features”和“minecraft:ignore_automatic_features”现已弃用

## 方块

- 恢复了向日葵背面的纹理为绿色叶子 ([MCPE-181275](https://bugs.mojang.com/browse/MCPE-181275))
- “coral_fan_hang”方块现在分为独特实例“tube_coral_wall_fan”、“brain_coral_wall_fan”、“dead_tube_coral_wall_fan”和“dead_brain_coral_wall_fan”
- “coral_fan_hang2”方块现在分为独特实例“bubble_coral_wall_fan”、“fire_coral_wall_fan”、“dead_bubble_coral_wall_fan”和“dead_fire_coral_wall_fan”
- “coral_fan_hang3”方块现在分为独特实例“horn_coral_wall_fan”和“dead_horn_coral_wall_fan”
- “stone_block_slab4”方块现在分为独特实例“mossy_stone_brick_slab”、“smooth_quartz_slab”、“normal_stone_slab”、“cut_sandstone_slab”和“cut_red_sandstone_slab”
- “mossy_stone_brick_slab”现在的破坏时间为1.5

## 编辑器

- 创建编辑器项目时不显示极限模式选项
- 更新选择、刷子、线条、粘贴、删除、填充工具以在应用更改之前加载边界
- 添加了*IActionBar* API以管理脚本化的*IActionBarItem*
- 在*IPlayerUISession* API中添加了属性*actionBar: IActionBar*，表示动作栏选择器UI中的快速动作项目
- 在*IPropertyPane* API中添加了*addColorPicker*方法，以显示用于修改*RGBA*值的颜色选择器属性面板项目

# 技术实验性更新

## API

- EntityBreathableComponent
  - 将函数*setAirSupply(value: number): void*更改为属性*airSupply: number*在*beta*中
  - 在*beta*中添加属性*readonly canBreathe: boolean*
- EntityComponent
  - 将类*EntityMovementComponent*从*beta*移动到*1.12.0*
  - 将类*EntityLavaMovementComponent*从*beta*移动到*1.12.0*
  - 将类*EntityMovementGlideComponent*从*beta*移动到*1.12.0*
  - 将类*EntityMovementSwayComponent*从*beta*移动到*1.12.0*
  - 将类*EntityUnderwaterMovementComponent*从*beta*移动到*1.12.0*
- 添加类*PlayerCursorInventoryComponent*，为玩家的光标物品栏提供只读访问权限，并能够清空它