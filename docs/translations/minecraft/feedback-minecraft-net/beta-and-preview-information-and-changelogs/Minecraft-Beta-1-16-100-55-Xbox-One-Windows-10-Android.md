---
title: Minecraft Beta - 1.16.100.55 (Xbox One/Windows 10/Android)
date: 2020-09-10T14:46:46Z
updated: 2020-09-11T08:32:15Z
categories: Beta和预览信息与更新日志
tags:
  - beta
  - beta_changelog
link: https://feedback.minecraft.net/hc/en-us/articles/360049002892-Minecraft-Beta-1-16-100-55-Xbox-One-Windows-10-Android
---

**发布于:** 2020年9月10日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

# **漏洞修复**

**性能与稳定性**

- 玩家在重新加入多人会话后打开站在其上的潜影盒时，游戏不再崩溃
- 使用/填充命令与传送门填充大量方块时修复了崩溃问题

**原版趋同**

- 幼年僵尸疣猪兽现在有可爱的超大头颅（[MCPE-65454](https://bugs.mojang.com/browse/MCPE-65454)）
- 菌光体方块现在可以与堆肥桶一起使用（[MCPE-82999](https://bugs.mojang.com/browse/MCPE-82999)）
- 绯红菌和诡异菌现在可以放置在菌丝体方块上（[MCPE-88588](https://bugs.mojang.com/browse/MCPE-88588)）
- 侦测器在被活塞移动时不再卡在激活状态（[MCPE-61175](https://bugs.mojang.com/browse/MCPE-61175)）
- “Thing”旗帜现在可以在织布机上制作（[MCPE-70449](https://bugs.mojang.com/browse/MCPE-70449)）
- 所有预期的方块和物品现在可以再次进行堆肥（[MCPE-94671](https://bugs.mojang.com/browse/MCPE-94671)）

**一般**

- 使用/setblock或/填充命令放置的传送门方块，如果不是有效传送门结构的一部分，将仅存在1秒钟后被移除
- 狐狸不再在掉落到浆果上时受到伤害（[MCPE-82273](https://bugs.mojang.com/browse/MCPE-82273)）
- 标题命令（标题、副标题和动作栏）的文本和背景已调整并进行了间距调整
- 更衣室在离线时现在显示缓存的角色创建器物品
- 不再接受没有alpha通道的24位PNG作为有效的自定义皮肤（[MCPE-50094](https://bugs.mojang.com/browse/MCPE-50094)）
- 在Android上添加了带有新Mojang Studios标志的原生闪屏（[MCPE-79353](https://bugs.mojang.com/browse/MCPE-79353)）

**游戏玩法**

- 附魔了灵魂疾行的靴子在破坏后不再卡在生物或玩家身上（[MCPE-75375](https://bugs.mojang.com/browse/MCPE-75375)）
- 猪灵蛮兵在变成僵尸后保留装备（[MCPE-83683](https://bugs.mojang.com/browse/MCPE-83683)）

**用户界面**

- 锻造台界面现在包含锤子图标，并且在使用“口袋”UI配置设置时UI元素正确显示（[MCPE-79541](https://bugs.mojang.com/browse/MCPE-79541)）

**新成就界面**

- 将列表项上的奖励框架与艺术框架设置为相同
- 改进了点击视觉反馈
- 减小了安全区大小
- 修复了无法使用键盘将焦点移开“返回”按钮的问题
- 修复了新成就界面有时在分屏模式下错误应用安全区的问题，而不是仅在窗口边缘

**技术更改**

**附加包和脚本引擎**

- 带宽优化：确保等级事件数据包仅在本地广播
- 空间带宽优化现在通过组件“minecraft:conditional_bandwidth_optimization”公开
- 每个使用“minecraft:conditional_bandwidth_optimization”的活动对象现在都利用空间带宽优化
- 将选择器组件添加到原始文本中，可用于在命令如'tellraw'和'titleraw'中打印实体名称
- 使用/结构命令加载的结构不再被截断

**音频**

- FMOD音乐通道在播放音乐时现在将其优先级设置为0，以防止FMOD虚拟通道在游戏中播放常规声音时抢占它（默认优先级为128）