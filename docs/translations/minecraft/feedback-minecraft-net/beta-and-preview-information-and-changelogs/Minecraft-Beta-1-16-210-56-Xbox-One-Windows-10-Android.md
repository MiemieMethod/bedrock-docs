---
标题: Minecraft Beta - 1.16.210.56 (Xbox One/Windows 10/Android)
日期: 2021-01-20T16:15:19Z
更新: 2021-01-20T16:57:32Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360055733571-Minecraft-Beta-1-16-210-56-Xbox-One-Windows-10-Android
哈希:
  幽匿感测体: sculksensor
---

**发布于:** 2021年1月20日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览Beta时无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防止丢失
- Beta版本可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**新实验性功能：**

在本周的Beta中，我们有一些令人兴奋的新洞穴和悬崖功能，可以通过在您的世界中启用“实验性功能”开关来访问。（您可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)了解更多关于使用开关的信息。）请记住，这些功能尚未完成，因为它们仍在开发中。您可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中给我们反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的任何新漏洞。

![img_616.JPG](https://feedback.minecraft.net/hc/article_attachments/360082619692/img_616.JPG)

## **滴水石**

- 添加了小型滴水石锥块
  - 这些目前可以在创造模式物品栏中找到
- 小型滴水石锥块可以放置在天花板和地面上，形成钟乳石和石笋
- 站在石笋上会造成更高的跌落伤害
- 破坏钟乳石上方的天花板会导致其掉落并对实体造成伤害
- 钟乳石具有滴水和熔岩的动画

<!-- -->

- **已知问题：**
  - 当悬挂的小型滴水石锥开始掉落时，其位置会稍微偏移
  - 在放置相对的钟乳石和石笋的尖端时潜行会将它们合并
  - 放置的小型滴水石锥可以被基岩上的熔岩摧毁
  - 如果玩家被钟乳石或石笋的跌落伤害击杀，自定义死亡信息不会显示
  - 小型滴水石锥物品在基岩版中与Java版的手持显示不同
  - 在水中放置小型滴水石锥会导致水被移除
  - 玩家在跳到石笋上时会受到2点伤害

## **幽匿感测体**

- 引入奇异的、充满触须的幽匿世界——准备好让幽匿感测体以其独特的能力来检测附近的振动而感到惊讶吧
- 振动是指任何导致物理运动的事物；如果您小心，有些动作在潜行时是无法被感测体检测到的。不过，仍然有很多这样的事件缺失——敬请期待！
- 这些适合潜行的振动目前包括走路、掉落到地面
- 当前的振动事件列表如下：（未来更新中将添加更多）
  - 脚步
  - 游泳
  - 放置方块
  - 破坏方块
  - 鞘翅自由落体
  - 碰撞地面
  - 闪烁标语
  - 投射物射击
- 幽匿感测体不会监听由其他幽匿源直接产生的振动
- 当检测到振动时，信号会以每个区块1个游戏刻的速度从源位置发送到感测体
- 当信号已经在传输时，其他振动无法被感测体检测到
- 当信号到达时，感测体将激活40个游戏刻（大约2秒）
- 在激活期间，感测体无法检测到其他振动
- 幽匿感测体可以检测到其周围8个区块范围内的振动

<!-- -->

- **已知问题：**
  - 幽匿感测体无法被水淹没
  - 羊毛遮挡尚未添加到方块的功能中。此功能将在后续Beta中添加

## **漏洞修复**

**常规**

- 修复了生猪排成就和奖杯被生猪排解锁的问题 ([MCPE-95446](https://bugs.mojang.com/browse/MCPE-95446))
- 修复了狐狸不会掉落并吃甜浆果的漏洞 ([MCPE-70790](https://bugs.mojang.com/browse/MCPE-70790))
- 当缺少现有世界所需的模板时，点击“下载模板”现在会正确下载所需的模板
- 修复了允许玩家在冒险模式下默认放置自定义刷怪蛋的漏洞

**命令**

- '/setblock'命令现在支持设置灵魂灯笼方块的连接状态 ([MCPE-89609](https://bugs.mojang.com/browse/MCPE-89609))
- '/setblock'命令现在支持设置锁链方块的旋转状态 ([MCPE-105912](https://bugs.mojang.com/browse/MCPE-105912))
- 'SetBlock'和'SetBlockAtPos'事件现在支持自定义方块状态

**方块**

- 修复了某些市场世界在领域和移动与PC之间的多人游戏中播放时方块数据不正确的问题

**世界生成**

- 保存了实体的Mcstructure文件在加载到世界时不再导致游戏崩溃 ([MCPE-63387](https://bugs.mojang.com/browse/MCPE-63387))

**技术变更**

- 为方块事件响应“decrement_stack”添加了一个名为“ignore_game_mode”的布尔参数，默认设置为false。因此“decrement_stack”在创造模式下默认不再减少物品堆叠

**此Beta中的其他已知问题：**

- 在Android上挂起和恢复游戏时可能会发生崩溃
- 补丁说明屏幕可能包含指向市场的无效链接