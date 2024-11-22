---
标题: Minecraft Beta - 1.15.0.56 (Xbox One/Windows 10/Android)
日期: 2020-03-11T15:18:56Z
更新: 2020-03-11T15:51:19Z
分类: Beta和预览信息及更改日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360040841731-Minecraft-Beta-1-15-0-56-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防止丢失
- Beta版本可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**修复：**

- **崩溃/性能**
  - 修复了在游戏过程中可能发生的多个崩溃
  - 修复了有时因使用自定义方块而导致的崩溃
  - 修复了尝试使用自定义配方附加包时可能发生的崩溃，该附加包也会将物品返回给玩家
  - 修复了在玩家使用抗火药水或水下呼吸后，尝试加载保存的游戏时可能发生的崩溃，尤其是在水或熔岩中
  - 修复了在菜单打开时退出游戏可能导致游戏崩溃的问题
  - 修复了在近战中使用附魔时发生的崩溃（[MCPE-63517](https://bugs.mojang.com/browse/MCPE-63517)）
  - 修复了加载存档数据时可能发生的崩溃

<!-- -->

- **常规**
  - 修复了将世界从主机版转换为基岩版时可能导致区块被覆盖的问题（[MCPE-58480](https://bugs.mojang.com/browse/MCPE-58480)）
  - 地图现在可以以正确的比例从其他版本转换为基岩版（[MCPE-58796](https://bugs.mojang.com/browse/MCPE-58796)）
  - 修复了在第三人称视角中多种手臂动画的问题（[MCPE-63088](https://bugs.mojang.com/browse/MCPE-63088)）

<!-- -->

- **游戏玩法**
  - 修复了破坏方块后方块会重新出现的问题（[MCPE-48914](https://bugs.mojang.com/browse/MCPE-48914)）
  - 修复了移动侦测器方块时未被激活的问题（[MCPE-63785](https://bugs.mojang.com/browse/MCPE-63785)）
  - 附魔武器现在再次正确应用其效果（[MCPE-63124](https://bugs.mojang.com/browse/MCPE-63124)）
  - 更换盔甲现在会更新并正确显示盔甲（[MCPE-63135](https://bugs.mojang.com/browse/MCPE-63135)）
  - 剪羊毛现在会正确更新绵羊（[MCPE-63188](https://bugs.mojang.com/browse/MCPE-63188)）
  - 云杉和巨型云杉树不再生成缺失的原木（[MCPE-63658](https://bugs.mojang.com/browse/MCPE-63658)）
  - 树叶不再阻止树苗生长为树木（[MCPE-63153](https://bugs.mojang.com/browse/MCPE-63153)）
  - 漏斗现在会从上方放置的堆肥桶中收集骨粉（[MCPE-63809](https://bugs.mojang.com/browse/MCPE-63809)）

<!-- -->

- **用户界面**
  - 命令方块的用户界面现在可以正确适应4:3比例的屏幕（[MCPE-41730](https://bugs.mojang.com/browse/MCPE-41730)）

<!-- -->

- **附加包和脚本**
  - 蜜蜂刷怪蛋现在可以在内容包中编辑
  - 修复了阻止自定义方块在附加包中使用的问题（[MCPE-63121](https://bugs.mojang.com/browse/MCPE-63121)）
  - 修复了可能导致minecraft:timer组件在某些条件下提前触发的问题
  - 修复了导致粒子动画反转的问题
  - 在附加包中使用minecraft:pushable组件不再破坏旧内容
  - 修复了阻止行为包中的动画控制器在专用服务器和Realm上运行的问题（[MCPE-59881](https://bugs.mojang.com/browse/MCPE-59881)）