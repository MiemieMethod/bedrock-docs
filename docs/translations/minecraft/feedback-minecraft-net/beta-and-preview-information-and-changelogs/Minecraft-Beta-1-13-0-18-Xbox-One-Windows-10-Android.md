---
标题: Minecraft Beta - 1.13.0.18 (Xbox One/Windows 10/Android)
日期: 2019-10-02T15:47:35Z
更新: 2019-10-02T15:51:31Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360034340052-Minecraft-Beta-1-13-0-18-Xbox-One-Windows-10-Android
---

**请在参与Minecraft Beta之前阅读**：

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- Beta版本可能不稳定，且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**修复内容：**

- **崩溃/性能**
  - 修复了在Android上接受存储权限时发生的崩溃
  - 修复了游戏过程中可能发生的多个崩溃
  - 修复了在设置中滚动语言时可能发生的崩溃（[MCPE-52009](https://bugs.mojang.com/browse/MCPE-52009)）
  - 修复了在Android上使用角色创建器时可能发生的崩溃（[MCPE-52474](https://bugs.mojang.com/browse/MCPE-52474)）

<!-- -->

- **一般**
  - “传送我上去”成就再次可以解锁

<!-- -->

- **游戏玩法**
  - 修复了玩家在创造模式下骑乘实体后从天空掉落的问题（[MCPE-52957](https://bugs.mojang.com/browse/MCPE-52957)）
  - 修复了玩家在将世界存档转移到不同的Xbox One后出现在意外位置的问题

<!-- -->

- **生物**
  - 僵尸再次在洞穴中生成（[MCPE-52743](https://bugs.mojang.com/browse/MCPE-52743)）

<!-- -->

- **物品**
  - 地毯再次出现在羊驼的物品栏界面上
  - 弩在装填后不再立即发射（[MCPE-52179](https://bugs.mojang.com/browse/MCPE-52179)）
  - 修复了从创造物品栏中丢弃损坏工具的能力（[MCPE-52465](https://bugs.mojang.com/browse/MCPE-52465)）
  - 指南针和时钟再次在快捷栏上动画显示（[MCPE-52901](https://bugs.mojang.com/browse/MCPE-52901)）
  - 盔甲再次可以直接从触摸屏的创造物品栏中装备（[MCPE-52413](https://bugs.mojang.com/browse/MCPE-52413)）
  - 冰霜行者靴再次可以冻结水

<!-- -->

- **图形**
  - 破坏动画再次出现在箱子上
  - 修复了潜行时玩家的头颅看起来不正确的问题（[MCPE-51181](https://bugs.mojang.com/browse/MCPE-51181)）
  - 修复了游泳时玩家的手臂不动画的问题（[MCPE-49749](https://bugs.mojang.com/browse/MCPE-49749)）
  - 生物头颅再次正确适配玩家
  - 修复了在某些GUI比例下工作台图标未显示其网格的问题
  - 修复了物品栏中多个缺失和损坏的纹理（[MCPE-52442](https://bugs.mojang.com/browse/MCPE-52442)）
  - 修复了一些皮肤出现白色斗篷的问题（[MCPE-52005](https://bugs.mojang.com/browse/MCPE-52005)）
  - 修复了盔甲未尊重皮肤上额外层的问题
  - 修复了被破坏的方块留下阴影的问题

<!-- -->

- **用户界面**
  - 对角色创建器界面进行了各种修复和加载时间改进
  - 外部服务器再次出现在服务器界面上
  - 修复了某些方块的物品栏界面在方块状态改变后首次尝试未出现的问题，例如漏斗和发射器
  - 在分屏游戏时可以访问个人资料界面
  - “阅读更多”按钮再次出现在全球资源菜单的包旁边

<!-- -->

- **命令**
  - '/summon '命令再次正确命名实体（如果已定义）

<!-- -->

- **附加包和脚本引擎**
  - 修复了自定义生物的刷怪蛋未出现在创造物品栏中的问题
  - 被缩放生物持有的物品再次适当调整大小
  - 使用'format_version' 1.2.0不再破坏'on_damage'组件
  - 触发自定义动画的功能再次可用
  - 在'xp_orb'上使用'transformation'组件再次移除源实体
  - 'spawn_entity'组件现在在实体被骑乘时执行
  - 修复了末影龙在某些附加包中未正确显示的问题
  - 错误再次在包清单验证界面上列出