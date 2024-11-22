---
title: Minecraft Beta & Preview - 1.19.20.22
date: 2022-07-13T13:52:10Z
updated: 2022-07-19T13:12:53Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/7647851092237-Minecraft-Beta-Preview-1-19-20-22
---

**发布时间：** 2022年7月13日

## **Minecraft预览版和测试版信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，显示悦灵和蜜蜂在竹子附近飞翔](https://feedback.minecraft.net/hc/article_attachments/7647827631117/beta19U2_2_1600x900.jpg)

这是本周Minecraft预览版和测试版的新内容列表！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](http://bugs.mojang.com/)并向我们发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **新特性和漏洞修复**

### **旁观模式（实验性）**

- 在旁观模式下移除了表情功能
- 旁观者的头颅现在正确渲染为半透明
- 在旁观模式下，角色创建器的头部物品（帽子、兜帽、头盔等）现在正确渲染为半透明
- 在旁观模式下，披风和动画背部物品不再渲染（[MCPE-156929](https://bugs.mojang.com/browse/MCPE-156929)）
- 旁观者不再能够使用或受到传送门的影响（[MCPE-156684](https://bugs.mojang.com/browse/MCPE-156684)）

## **悦灵**

- 悦灵现在可以在船上拾取和丢弃物品（[MCPE-156183](https://bugs.mojang.com/browse/MCPE-156183)）
- 悦灵现在始终可以拾取掉落的脚手架方块（[MCPE-157512](https://bugs.mojang.com/browse/MCPE-157512)）
- 当唱片机的音乐结束时，悦灵现在会正确停止跳舞
- 悦灵现在会关注目标，例如玩家（[MCPE-158222](https://bugs.mojang.com/browse/MCPE-158222)）

## **方块**

- 钟不再能够着火或被火摧毁
- 幽匿催发体在绽放时现在会播放绽放音效（[MCPE-153562](https://bugs.mojang.com/browse/MCPE-153562)）
- 如果保持物品栏规则设置为真，幽匿催发体在玩家死亡时不再传播幽匿（[MCPE-157884](https://bugs.mojang.com/browse/MCPE-157884)）
- 如果生物在幽匿催发体上方死亡，幽匿催发体不再被幽匿脉络覆盖

## **命令**

- 改进了定位生物命令的性能，以减轻在搜索远处生物时服务器的停顿（[MCPE-157609](https://bugs.mojang.com/browse/MCPE-157609)）

## **深暗之域**

### **远古城市**

- 通往远古城市中心红石房间的秘密门现在能够正确开关（[MCPE-156718](https://bugs.mojang.com/browse/MCPE-156718)）

## **教育版**

- 修复了在切换材料还原器输入时发生的崩溃，通过禁用输入切换来解决。玩家现在必须在添加新输入之前移除旧输入

## **火球实体**

- 修改了*json*实体文件，使其除了包含爆炸和火焰伤害外，还包含投射物伤害（[MCPE-153740](https://bugs.mojang.com/browse/MCPE-153740)）

## **游戏玩法**

- 修复了当顶部雪落在玩家上方时的透视问题，现在当顶部雪遮挡玩家视线时，它表现为一个实心方块（[MCPE-150709](https://bugs.mojang.com/browse/MCPE-150709)）

## **常规**

- 修复了添加服务器功能无法保存IPV6地址的问题（[MCPE-66233](https://bugs.mojang.com/browse/MCPE-66233)）

## **物品**

- 当熔岩在铁桶中无法放置或分配到部分方块时，熔岩不再消失（[MCPE-50664](https://bugs.mojang.com/browse/MCPE-50664)）
- 带有*item_lock*组件的物品不再能够放置在物品展示框或盔甲架上（[MCPE-138479](https://bugs.mojang.com/browse/MCPE-138479)）
- 修复了某些耐久物品在创造模式物品栏中无法被创建的问题

## **市场**

- 实施了新的市场错误屏幕艺术和消息

## **移动控制**

- 修复了在使用鼠标和键盘的iOS设备上，玩家无法悬停在滚动视图中的UI元素上的问题。这是由于滚动视图自动聚焦于最近的未裁剪元素导致的
- 修复了当连接的设备（如游戏手柄）缺失时可能发生的崩溃

## **生物**

- 悦灵和蜜蜂不再卡在非完整方块中（[MCPE-155777](https://bugs.mojang.com/browse/MCPE-155777)）
- 鱼在放置在孤立的水方块中时不再抖动
- 修复了一个导致狼在通过*entity_born*或*on_tame*事件召唤时变为红色的漏洞
- 修复了生物的远程武器附魔未被应用的问题（[MCPE-113623](https://bugs.mojang.com/browse/MCPE-113623)）

### **女巫**

- 修复了可能导致女巫停止生成的漏洞。女巫小屋结构现在被设置为女巫的表面生成器（[MCPE-60552](https://bugs.mojang.com/browse/MCPE-60552)）

## **性能和稳定性**

- 修复了由于村民在交易时更改职业而导致的崩溃。如果村民在交易中途更改职业，交易界面将关闭

## **幽匿感测体**

- 幽匿感测体现在也可以检测蜜蜂、鸡、悦灵、幻翼和末影龙的飞行（[MCPE-153725](https://bugs.mojang.com/browse/MCPE-153725)，[MCPE-154055](https://bugs.mojang.com/browse/MCPE-154055)）
- 幽匿感测体现在可以根据振动发出的距离发出整个范围的红石信号强度。之前，输出只能是1、15或0
- 振动粒子现在始终朝向目标幽匿感测体（[MCPE-156648](https://bugs.mojang.com/browse/MCPE-156648)）

## **稳定性和性能**

- 连接到多人游戏的超时从180秒减少到90秒
- 修复了在活塞在可移动方块和箭矢附近伸缩时可能发生的崩溃

## **用户界面**

- 物品栏中*can_place_on*方块的悬停文本现在在游戏存档之间保持一致的顺序（[MCPE-153516](https://bugs.mojang.com/browse/MCPE-153516)）
- 移除了Oculus的控制器设置标签

## **原版趋同**

- 村民工作时锻造台的声音现在与玩家使用该台时的声音相同（[MCPE-79716](https://bugs.mojang.com/browse/MCPE-79716)）
- 修复了生物走在紫水晶块上时紫水晶步声音效的音量级别

### **方块**

- 紫水晶块已更名为“紫水晶块”（[MCPE-125821](https://bugs.mojang.com/browse/MCPE-125821)）

### **生物**

- 末影龙不再能够摧毁哭泣的黑曜石、重生锚、光源方块、拒绝、允许、边界和拼图方块（[MCPE-158343](https://bugs.mojang.com/browse/MCPE-158343)）

### **幽匿感测体**

- 幽匿感测体不再检测在水中静止的船只（[MCPE-155368](https://bugs.mojang.com/browse/MCPE-155368)）

# **技术更新**

## **账户暂停**

- 修复了暂停账户无法在Xbox平台上玩本地世界或导航菜单的漏洞

## **活动对象属性**

- 添加了新的Molang *had_component_group*，以允许从先前保存的实体数据计算适当的默认值
- 将*'actor_property'*和*'has_actor_property'*的Molang查询重命名为*'property'*和*'has_property'*。同时将*'set_actor_property'*重命名为*'set_property'*
- 更新*'set_property'*以仅允许更改本地活动对象的属性，而不是其他目标

# **实验性技术特性**

## **常规**

- 将*their render_method*组件设置为*double_sided*的方块现在正确渲染其背面
