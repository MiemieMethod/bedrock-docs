---
标题: Minecraft Beta - 1.16.200.51 (Xbox One/Windows 10/Android)
日期: 2020-10-22T13:56:34Z
更新: 2020-10-22T16:07:37Z
类别: Beta 和预览信息及更新日志
标签:
  - beta
  - beta_changelog
链接: https://feedback.minecraft.net/hc/en-us/articles/360050933412-Minecraft-Beta-1-16-200-51-Xbox-One-Windows-10-Android
---

在参与Minecraft Beta之前，请阅读以下内容：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防止丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

## 漏洞修复

## 辅助功能

- 修复了一个漏洞，UI屏幕阅读器未能读取游戏中的屏幕标题
- 修复了一个漏洞，UI屏幕阅读器未能读取暂停屏幕上的快捷按钮
- 修复了一个漏洞，UI屏幕阅读器未能读取个人资料和编辑角色屏幕上的标题
- 修复了一个问题，在使用文本转语音时，暂停屏幕上按钮的编号错误
- 修复了多个与文本对比度相关的问题

## 游戏玩法

- 死亡信息漏洞修复（[MCPE-30360](https://bugs.mojang.com/browse/MCPE-30360)，[MC-116558](https://bugs.mojang.com/browse/MC-116558)）
  - 被潜影贝射击的死亡信息现在为“被潜影贝狙击”而不是“被潜影贝子弹杀死”
  - 被烈焰人或恶魂火球击中的死亡信息现在为“被\<烈焰人 \| 恶魂\>火球击中”而不是“被\<烈焰人 \| 恶魂\>杀死”
  - 被骷髅射击的死亡信息现在为“被骷髅射击”而不是“被箭射击”
  - 被羊驼唾沫击中的死亡信息现在为“被羊驼唾沫击中”而不是“被羊驼唾沫杀死”
  - 被三叉戟杀死的死亡信息现在为“被……刺死”而不是“被三叉戟杀死”
- 下界砖块再次可合成（[MCPE-101736](https://bugs.mojang.com/browse/MCPE-101736)）
- 修复了工作台中下界砖块的数量问题（[MCPE-101818](https://bugs.mojang.com/browse/MCPE-101818)）

## 生物

- 增加了袭击生物的生成距离，并改善了找到有效袭击生成位置的能力

## 组件

- 带有物品栏锁定组件的盔甲现在可以放置在盔甲槽位中（[MCPE-102244](https://bugs.mojang.com/browse/MCPE-102244)）

## 物品

- 修复了使用“query.get_equipped_item_name”与重命名物品时不会得到正确结果的问题。现在我们将其与原版版本关联，以便如果世界与特定原版版本关联，则返回旧名称