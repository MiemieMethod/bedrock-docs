---
标题: Minecraft Beta & Preview - 1.20.40.23
日期: 2023-09-27T14:32:53Z
更新: 2023-09-28T13:40:16Z
分类: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/19883048087693-Minecraft-Beta-Preview-1-20-40-23
哈希:
  h_01HBBGVQD2C4ZDZY3ZSSAAYJT8: 特性与漏洞修复
  h_01HBBGVQD2TY6J2WV44DZYSBJ1: 音频
  h_01HBBGVQD2XWM4XYGK92YYGFGF: 方块
  h_01HBBGVQD2BSP3DHB63RM699DV: 游戏玩法
  h_01HBBGVQD2YAFTBZKYKWV3SVKP: 图形
  h_01HBBGVQD2BD0JHV7NTT2AYHEV: 图形
  h_01HBBGVQD2BS5WFZDJ0DJWHHGA: 物品
  h_01HBBGVQD2SQPX9X739WW708T0: 生物
  h_01HBBGVQD21DNFN4B2KC0XEAJD: 稳定性与性能
  h_01HBBGVQD2Y7MC1P2X0DPXP6BN: 用户界面
  h_01HBBGVQD2QN0ZMDVZJTGWZD97: 技术更新
  h_01HBBGVQD22D3Q0RZ1CZC16MHM: 教育特性
  h_01HBBGVQD2GJPV52HZ4FB0YGJE: 编辑器
  h_01HBBGVQD2SEANVZ4ET10N4V2A: 实体组件
  h_01HBBGVQD2GB5JSWCXWN9A2SQZ: 实验性技术特性
  h_01HBBGVQD2AXMS9EMNBJ8RKD4B: API
  h_01HBBGVQD2XZ14JHHENB2FWYHV: 图形-1
---

**发布:** 2023年9月27日

**关于Minecraft预览和测试版的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明。

![一张Minecraft截图，展示Zuri站在山羊和炼药锅旁边。](https://feedback.minecraft.net/hc/article_attachments/19882985673613)

以下是本周Minecraft预览和测试版的新内容！一如既往，我们非常希望听到您对这些修复和特性的看法，因此请将您的反馈和想法发送至[aka.ms/MC120Feedback](http://aka.ms/MC120Feedback)，并将任何漏洞报告至[bugs.mojang.com](http://bugs.mojang.com/)。  
  

# 特性与漏洞修复

## 音频

- 更新后的闪烁声音现在也在Android上播放（[MCPE-174524](https://bugs.mojang.com/browse/MCPE-174524)）

## 方块

- 第三人称视角不再穿过炼药锅的下部（[MCPE-173010](https://bugs.mojang.com/browse/MCPE-173010)）
- 在细雪中跌落不再造成任何伤害，无论跌落高度如何（[MCPE-174859](https://bugs.mojang.com/browse/MCPE-174859)）
- 穿着皮革靴子的轻型生物和实体在从超过两块半的高度跌落时再次会沉入细雪的顶层

## 游戏玩法

- 山羊角的声音现在再次被视为唱片机/音符盒的声音（[MCPE-175156](https://bugs.mojang.com/browse/MCPE-175156)）
- 修复了一个问题，即如果生物在摩擦力为0的方块上移动，游戏会锁死（[MCPE-173073](https://bugs.mojang.com/browse/MCPE-173073)）

## 图形

- 随机光源不再在没有光源的情况下出现在世界中（[MCPE-169001](https://bugs.mojang.com/browse/MCPE-169001)）

## 图形

- 闪烁粒子现在在活动对象的腰部发出，而不是在其头顶上方

## 物品

- 诡异菌钓竿在第一人称视角中不再反向持有（[MCPE-169765](https://bugs.mojang.com/browse/MCPE-169765)）

## 生物

- 修复了一个漏洞，即嗅探兽在物品生成后立即停止挖掘，而不是在指定的挖掘持续时间结束时停止

## 稳定性与性能

- 修复了与水方块的细分相关的崩溃问题

## 用户界面

- 将无效物品放入副手槽位不再导致物品掉落

# 技术更新

## 教育特性

- 修复了一个漏洞，即如果用户在世界的基版本为1.19.80之前没有世界构建者权限，则召唤NPC命令无法工作

## 编辑器

编辑器及其相应的API处于早期开发阶段，并可在Windows PC基岩预览版构建中使用键盘/鼠标。请在社交渠道上标记我们，使用**\#BedrockEditor**。

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队互动，并通过[入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[示例](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周修复的内容：

- 修复了一个漏洞，即在移动小工具被拖动时，选择面板中的原点Vector3物品未能更新。

## 实体组件

- 解锁了“behavior.random_search_and_dig”供创作者使用
- 添加了“target_blocks”字段。生物可以挖掘的方块列表。如果未添加“target_blocks”，默认值为泥土、草、灰化土、带根的泥土、苔藓、泥巴和沾泥的红树根
- 添加了“item_table”字段。指向一个战利品表的路径，指定生物可以挖掘的物品。“item_table”优先于“items”
- 如果行为在读取或查找“item_table”时遇到问题，或者无法从“items”中获取物品，则添加内容错误
- 'on_item_found'事件现在在找到物品和挖掘完成时触发。在此之前，事件触发导致挖掘提前停止

# 实验性技术特性

## API

- 添加了在实体上调用的*matches*函数，该函数接受*EntityQueryOptions*并在实体匹配时返回true，否则返回false。
- 将*getRotation*从*beta*移动到1.*6.0*
- 将*setRotation*从*beta*移动到1.*6.0*
- 添加了*PlayerLeaveBeforeEvent* - 当玩家离开服务器时触发此事件，在Player对象被移除之前
- 将PlayerDimensionChangeAfterEvent的测试版发布到*1.6.0*

## 图形

- 高自发光值（> 0.25）不再在延迟技术预览中遮挡表面细节