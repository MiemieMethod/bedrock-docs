---
标题: Minecraft Beta - 1.16.200.55 (Xbox One/Windows 10/Android)
日期: 2020-11-10T16:11:24Z
更新: 2020-11-11T17:08:06Z
分类: Beta 和预览信息及更新日志
标签:
  - beta
  - beta_changelog
链接: https://feedback.minecraft.net/hc/en-us/articles/360051928792-Minecraft-Beta-1-16-200-55-Xbox-One-Windows-10-Android
---

**发布于:** 2020年11月11日

在参与Minecraft Beta之前，请阅读以下内容：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。有关加入或退出测试版的详细说明，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

## 漏洞修复

### 一般

- 修复了导致掠夺者等生物躲避阳光的漏洞
- 修复了某些移动设备在挂起和恢复后会失去音频的问题 ([MCPE-101027](https://bugs.mojang.com/browse/MCPE-101027))
- 修复了导致垂直击退过弱的漏洞
- 修复了RTX中飞行时卡顿和帧率较差的问题 ([MCPE-103532](https://bugs.mojang.com/browse/MCPE-103532))
- 添加了UI启动屏幕，以告知玩家他们是否使用过时的图形驱动程序

### 技术变更

- 修复旧命令版本使用之前位置而非当前位置
  - 修复了'query.cardinal_block_face_placed_on'在'on_player_placing'时不再有效的问题
- 当禁用mipmap时，将纹理图集的填充大小从0更改为1
- 修复了在“minecraft:block_placer”组件中列出的方块无法正常工作的的问题

### MoLang

- 几何体、材质和纹理变量名称可以再次包含点符号