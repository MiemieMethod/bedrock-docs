---
标题: Minecraft Beta - 1.16.200.56 (Xbox One/Windows 10/Android)
日期: 2020-11-18T17:03:12Z
更新: 2020-11-18T17:03:26Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360052266712-Minecraft-Beta-1-16-200-56-Xbox-One-Windows-10-Android
---

**发布于:** 2020年11月18日

在参与Minecraft Beta之前，请阅读以下内容：

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请务必备份世界以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

## 漏洞修复

**原版趋同**

- 玄武岩现在无法被恶魂的火球摧毁（[MCPE-75252](https://bugs.mojang.com/browse/MCPE-75252)）
- 玄武岩块现在需要稍微更长的时间才能摧毁
- 龙蛋现在在被爆炸摧毁时总是会掉落为物品（[MCPE-52632](https://bugs.mojang.com/browse/MCPE-52632)）

**常规**

- 如果用户拥有，创始人斗篷现在将在更衣室的斗篷标签中再次显示
- 修复了在渲染距离边缘使用'/fill'命令时出现的服务器/客户端块不同步问题
- 如果无法查询可用的GPU内存，最大渲染区块距离现在将默认为16
- 修复了在尝试加载256x分辨率资源包时导致Nintendo Switch崩溃的问题
  - 系统现在会阻止该选择，并通知玩家无法选择它

**技术变更**

- 添加了每帧可处理的日志消息数量限制，以防止加载时延迟
- 修复了在区块边界上放置大于1x1x1的数据驱动块时的一些剔除问题。还为较大块添加了内容警告
- 修复了模板世界中的自定义刷怪蛋生成问题
- 修复了玩家在游泳和滑翔时小型击中箱在事件发送后被重置的问题