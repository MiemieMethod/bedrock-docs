---
title: Minecraft Beta & 预览 - 1.21.50.24
date: 2024-10-17T14:28:52Z
updated: 2024-10-17T15:43:25Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/31137892416269-Minecraft-Beta-Preview-1-21-50-24
hash:
  user-content-features-and-bug-fixes: features-and-bug-fixes
  user-content-winter-drop-features: winter-drop-features
  user-content-pale-garden: pale-garden
  user-content-creaking-heart: creaking-heart
  user-content-accessibility: accessibility
  user-content-blocks-%26-items: blocks--items
  user-content-gameplay: gameplay
  user-content-graphical: graphical
  user-content-items: items
  user-content-realms: realms
  user-content-realm-events: realm-events
  user-content-sounds: sounds
  user-content-user-interface: user-interface-1
  user-content-technical-updates: technical-updates
  user-content-api: api-1
  01JADC7EB21289JGS5TDCMVMGK: blocks
  user-content-editor: editor
  user-content-experimental-technical-updates: experimental-technical-updates
  user-content-scripting: scripting
---

**发布于：** 2024年10月17日

**关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)获取详细说明

![一个苍白之园，搭建了一个小型基地，使用苍白橡木。背景中隐约可见嘎枝。](https://feedback.minecraft.net/hc/article_attachments/31137863479565)

是时候进行新的预览和Beta更新了！一如既往，我们期待您对这些新功能的反馈，您可以在 [aka.ms/mcgamedropfeedback](https://aka.ms/mcgamedropfeedback)上提供反馈，任何漏洞请在 [bugs.mojang.com](https://bugs.mojang.com/)上报告！以下是本周的新内容：

# 新功能和修复

## 冬季更新功能

### 苍白之园

- 调整了苍白苔藓 patches 的大小和位置

  - 苍白苔藓 patches 现在在自然生成时更大
  - 苍白苔藓 patches 现在有机会在不靠近苍白橡树的情况下自然生成
  - 苍白苔藓 patches 上的高草丛减少了

- 增加了苍白橡树的致密度，以匹配Java版

- 花和蘑菇不再在该生物群系中生成

- 在该生物群系中，天空现在完全是灰色，而不是地平线上的蓝色 ([MCPE-187291](https://bugs.mojang.com/browse/MCPE-187291))

- 去皮苍白橡木原木的颜色现在更亮，匹配其余的木材系列 ([MCPE-187289](https://bugs.mojang.com/browse/MCPE-187289))

- 苍白橡树树苗现在会长成带有悬挂苍白苔藓的苍白橡树，但其根部没有苍白苔藓 patches

- 苍白橡木告示牌的用户界面不再在左上角缺失一个像素 ([MCPE-187304](https://bugs.mojang.com/browse/MCPE-187304))

- 苍白橡木告示牌和苍白橡木悬挂告示牌的纹理已调整，以与木材系列中的其他物品保持一致 ([MCPE-187294](https://bugs.mojang.com/browse/MCPE-187294))

- 带箱子的苍白橡木船的纹理已调整，以与其他带箱子的船保持一致

- 苍白苔藓地毯在玩家的手中不再漂浮，尤其是在第三人称视角下

### 嘎枝之心

- 带有生成嘎枝和部分苍白橡木支撑的嘎枝之心在嘎枝通过命令被毁除时现在会停用

- 在创造模式中，ctrl选择该方块时不再保留嘎枝之心数据

- 嘎枝之心现在无法被活塞移动

- 嘎枝之心不再可以用作燃料

- 嘎枝之心生成和毁除其嘎枝时现在会从嘎枝的位置发出振动

## 辅助功能

- 修复了iOS上的触觉反馈问题 ([MCPE-145524](https://bugs.mojang.com/browse/MCPE-145524))

## 方块与物品

> **开发者备注**：我们修复了多个问题，某些方块的开采工具未正确影响掉落或开采速度。与这些更改相关，任何在支撑被破坏时掉落的方块，在使用任何工具开采时也会掉落。

- 以下方块现在仅在用镐破坏时掉落：高炉、炼药锅、发射器、投掷器、附魔台、熔炉、漏斗和烟熏炉 ([MCPE-33950](https://bugs.mojang.com/browse/MCPE-33950))

- 以下需要支撑的方块现在在用任何工具破坏时总是掉落：所有铜门、铁门、重质测重压力板、轻质测重压力板、磨制黑石压力板和石头压力板

- 紫水晶母岩现在用不当工具开采时速度变慢

- 以下方块（总是掉落的）在使用不正确的工具时开采速度变快：钟、酿造台、合成器、末影箱、灯笼和灵魂灯笼。请注意，末影箱被视为“总是掉落的方块”，即使掉落的不是末影箱 ([MCPE-176374](https://bugs.mojang.com/browse/MCPE-176374))

## 游戏玩法

- 杀死命令或任何大于或等于目标当前生命值的伤害现在将在1.18.20以下的基础游戏版本中杀死目标

- 由下界传送门生成的僵尸猪灵现在在再次使用传送门之前有15秒的冷却时间

## 图形

- 具有多种变体的纹理现在将加载PBR纹理数据 ([MCPE-174191](https://bugs.mojang.com/browse/MCPE-174191))

## 物品

- 更新了沉重核心的物品纹理

## 领域

- 更改活动领域槽时添加加载模态，以防止因玩家快速点击编辑世界按钮而导致多个领域槽设置屏幕被推入堆栈的故障

- 修复了在领域槽中上传或替换世界后，游戏模式和难度未被保留的问题。

### 领域事件

- 添加了与生物相关的新领域事件。

## 声音

- 调整了紫水晶块的破坏、击打、放置、坠落、踩踏和着陆声音的音量和音调

## 用户界面

- 调整了纸娃娃的位置，以避免与用户界面条重叠 ([MCPE-186341](https://bugs.mojang.com/browse/MCPE-186341))

- 移动设备：进入窗口/分屏模式不再覆盖自定义控制的保存位置 ([MCPE-185964](https://bugs.mojang.com/browse/MCPE-185964))

- 泰语字体在聊天和告示牌上的渲染改进。 ([MCPE-166005](https://bugs.mojang.com/browse/MCPE-166005))

- 从视频设置中移除了“新床屏幕”切换选项。（仅限预览）

- 为多个方块的GUI添加了缺失的快速交换动画

- 在玩家光标下移动的收纳袋现在会正确更新其提示框

# 技术更新

## API

- 在 `@minecraft/server-net` 模块版本 `1.0.0-beta` 中添加了 `beforeEvents` 对象，暴露两个事件
  - `packetReceive`：当游戏服务器从客户端接收到网络数据包时调用。如果被取消，服务器将静默忽略该数据包。
  - `packetSend`：当游戏服务器向客户端发送网络数据包时调用。如果被取消，该数据包将被丢弃，并且永远不会发送给接收者。

## 方块

- 在资源包的blocks.json文件架构中添加了新的字段 `"ambient_occlusion_exponent"`，替换了损坏的 `"brightness_gamma"` 字段。

## 编辑器

- 修复了一个错误，导致无法使用标题上的拖动图标拖动快速面板

- 修复了一个错误，导致下拉菜单在可滚动面板内打开时位置不正确

- 为菜单栏添加了溢出处理，以将溢出的项目折叠到菜单中，并改善子菜单以适应窗口边界

- 改进了持久设置存储。editorOptions.txt文件现在位于相同AppData目录中的editor子文件夹中。

- 改进了视口焦点可见性，聚焦时添加了动画轮廓，并将聚焦状态作为切换模式的步骤（CTRL + TAB）

- 在 `IModalToolContainer` 中添加了 `focusToolInputContext` 函数，该函数将尝试设置模态输入焦点（例如，工具轨道的视口）

## 用户界面

- 修复了资源包世界的高级提示中的拼写错误

# 实验性技术更新

## API

- 在 `Entity` 中添加了新的方法 `lookAt`，该方法将实体的旋转设置为面向所需的目标位置。

## 脚本

- 枚举 `InputMode`。
  - 移除了 `Undetermined` 条目。
- 类 `InputInfo`。
  - 在发生内部错误时抛出 `EngineError` 而不是 `Error`。