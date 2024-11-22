---
title: Minecraft Beta & Preview - 1.20.70.22
date: 2024-02-07T16:19:40Z
updated: 2024-02-07T17:03:15Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/23935492768781-Minecraft-Beta-Preview-1-20-70-22
hash:
  h_01HNG7NYQBZ0YBS3K63A5FSGFH: 关于Minecraft预览版和测试版的信息
  h_01HP262N0R8RMZFP8VES54Q7AM: 实验性特性
  h_01HP262N0RTV4HM71TQF0HFJ7F: 犰狳
  h_01HP262N0RVHH6PCDRNP4RPSYD: 宝库
  h_01HP262N0RMWG6M2X7TGXCE9YD: 旋风人
  h_01HP28BXHM13BVCHS33HDMZQC7: ""
  h_01HP262N0R6GM6VXSWTH1CFPX4: 特性和漏洞修复
  h_01HP262N0RK57A44G8ZCTE5MEP: 方块
  h_01HP268VCEYSYWBK3PKVFAB9S0: 游戏内提示
  h_01HP268VCEXKFZ4Q0TKV1MQQQX: 物品栏
  h_01HP268VCEMPDGSBA8HBVFRCH9: 领域
  h_01HP268VCEXRCXK788VHPDVPKB: 领域故事
  h_01HP268VCEX77T1WRDWYKVE93Z: 用户界面
  h_01HP268VCE9T9HE5QV9CH57GHY: 世界生成
  h_01HP268VCEZKBWR2VWSEAFW2Y2: 技术更新
  h_01HP268VCEZENPDK0GZ3QE7WP4: API
  h_01HP268VCEGDHW5F78XE7D53SZ: 方块-1
  h_01HP268VCE8KYJXPCMV5R4AKHC: 组件
  h_01HP268VCEHXTPH5EG400PGB09: 编辑器
  h_01HP268VCEK5P9R8461ZVANXNW: Molang
  h_01HP28BXHMN8C3APDCKXXF3DAC: "-1"
  h_01HP268VCFDNPRF9JPCYBV05V6: 实验性技术更新
  h_01HP268VCFQQEMDEPP9YWCP8N4: API-1
  h_01HP268VCFGXSVY4HEH0VCVCCQ: 图形

**发布于:** 2024年2月7日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![犰狳卷起时的姿态，四肢和面部露出。](https://feedback.minecraft.net/hc/article_attachments/23935504574349)

# 实验性特性

## 犰狳

- 犰狳有了全新的展开动画
- 犰狳在卷起时会随机探出壳外
- 为了适应这些新动画，卷起的犰狳在没有威胁的情况下保持卷起状态的时间已从3秒增加到4秒

## 宝库

- 宝库的纹理已更新
- 如果附近的玩家没有解锁宝库，钥匙孔将处于打开状态
- 如果所有附近的玩家都已解锁宝库，钥匙孔将处于关闭状态

## 旋风人

- 只有在启用相应的实验性切换时，旋风人才会在类型选择器中显示
- 旋风人的攻击伤害已调整

#  

# 特性和漏洞修复

## 方块

- 没有发光浆果的洞穴藤蔓不再在精准采集时掉落发光浆果 ([MCPE-151348](https://bugs.mojang.com/browse/MCPE-151348))
- 蓝色和黑色蜡烛蛋糕现在显示并掉落正确类型的蜡烛 ([MCPE-162868](https://bugs.mojang.com/browse/MCPE-162868))
- “wood”方块现在被拆分为独特的实例：“oak_wood”、“spruce_wood”、“birch_wood”、“jungle_wood”、“acacia_wood”、“dark_oak_wood”、“stripped_oak_wood”、“stripped_spruce_wood”、“stripped_birch_wood”、“stripped_jungle_wood”、“stripped_acacia_wood”和“stripped_dark_oak_wood”

## 游戏内提示

- 你可能注意到，在之前的预览中，我们推出了动态游戏提示功能。它将帮助玩家学习探索和享受Minecraft所需的基本知识。由于这些提示主要面向新玩家，因此你不太可能遇到它们，但如果你确实看到了，请随时在 [aka.ms/mcgametipsfeedback](https://aka.ms/mcgametipsfeedback) 留下反馈

## 物品栏

- 末地传送门框架物品已移至创造模式物品栏的自然类别中

## 领域

- 在领域中，除非玩家在该区域，否则我们将不再保持末地的区块加载 ([REALMS-11358](https://bugs.mojang.com/browse/REALMS-11358)) ([REALMS-11290](https://bugs.mojang.com/browse/REALMS-11290))
- 修复了领域订阅登录页面文本略微被截断的漏洞

## 领域故事

- 添加了四个新的领域事件
- 添加了两个额外的特大领域事件
- 修复了在领域故事设置屏幕上游戏手柄返回按钮输入无法正常工作的漏洞
- 修复了在Switch上时间方块未在正确时区渲染的问题
- 为评论屏幕添加了屏幕阅读器叙述
- 在分屏模式下，只有主用户可以访问领域故事

## 用户界面

- 更新后的死亡屏幕现在默认启用，即使在应用了资源包的情况下
- 新的游戏界面中的网格/列表布局按钮现在在重启时保留所选的布局模式 ([MCPE-177975](https://bugs.mojang.com/browse/MCPE-177975))
- 新的游戏界面中好友抽屉中的反馈按钮现在指向正确的反馈页面

## 世界生成

- 修复了有时可能导致要塞传送门房间无法生成的漏洞 ([MCPE-19426](https://bugs.mojang.com/browse/MCPE-19426))

 

# 技术更新

## API

- 修复了 *PlayerInteractWithEntityAfterEvent* 和 *PlayerInteractWithBlockAfterEvent* 的时机
- 将 *Player.setGameMode* 和 *Player.getGameMode* 添加到 *beta* 以更改玩家的 *GameMode*
- 将事件 *PlayerGameModeChangeAfterEvent*、 *PlayerGameModeChangeBeforeEvent* 与信号 *world.afterEvents.playerGameModeChange* 和 *world.beforeEvents.playerGameModeChange* 添加到 *beta*
- 添加 *GameRuleChangeAfterEvent*、 *GameRule* 和 *world.afterEvents.gameRuleChange* 以响应游戏规则的更改

## 方块

- 修复了'minecraft:geometry.full_block'面未旋转以匹配变换组件
- 修复了'minecraft:geometry.full_block'方块未对某些原版方块进行面剔除

## 组件

- 具有“damage_sensor”组件的实体可以再次通过命令被杀死
- “damage_sensor”组件可以再次在非拥有者的实体上触发实体事件

## 编辑器

编辑器及其相应的API仍处于早期开发阶段，并可在Windows PC基岩预览版构建中通过键盘/鼠标使用。请在社交媒体上标记我们，使用 **\#BedrockEditor。**

了解 [如何使用](https://aka.ms/LearnEditor) 编辑器，加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛与团队互动，并通过 [入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- 将枚举 ClipboardMirrorAxis 重命名为 StructureMirrorAxis 并移动到模块 @minecraft/server
- 将枚举 ClipboardRotation 重命名为 StructureRotation 并移动到模块 @minecraft/server
- 面板布尔值现在可以作为切换开关表示，作为复选框的替代

## Molang

- 从实验性中发布 *query.is_attached* 和 *query.has_player_rider*
- 移除实验性Molang查询 *query.get_ride* 和 *query.get_riders*
- 弃用Molang特性实验
- 发布Molang *query.scoreboard* 以供行为包使用（资源包将返回0）

#  

# 实验性技术更新

## API

- 修复了一个漏洞，导致动态物品属性有时会应用于堆叠数量大于1的物品
  - 移除函数 *triggerEvent()*
- WorldBeforeEvents
  - 移除属性 *itemDefinitionEvent*
- WorldAfterEvents
  - 移除属性 *itemDefinitionEvent*
  - 将 *explosion* 从 *beta* 移动到 *1.9.0*
- WorldBeforeEvents
  - 将 *explosion* 从 *beta* 移动到 *1.9.0*

## 图形

- 修复了在进入延迟技术预览世界时Android设备崩溃的问题
- 修复了在延迟技术预览中使用新点光源阴影特性时可能出现的循环视觉伪影