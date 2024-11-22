---
标题: Minecraft Beta - 1.16.210.54 (Xbox One/Windows 10/Android)
日期: 2021-01-07T16:26:56Z
更新: 2021-01-08T12:00:11Z
分类: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360055108571-Minecraft-Beta-1-16-210-54-Xbox-One-Windows-10-Android
---

**发布于:** 2021年1月7日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防止丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**一般**

- 添加了文本转语音音量滑块
- 流浪商人的墨囊现在可以用于合成，并且可以堆叠（[MCPE-101087](https://bugs.mojang.com/browse/MCPE-101087)）

**角色创建器**

- 表情轮现在支持Android和iOS设备的屏幕阅读器
- 分屏角色现在存储在内存中，重新加入游戏将保留玩家所拥有的角色（[MCPE-58640](https://bugs.mojang.com/browse/MCPE-58640)）

**市场**

- 修复了“format_version”1.13.0船只的升级路径，使其能够正确升级到1.16.100，这解决了一个漏洞，即在版本低于1.16.100的模板世界中，船只没有重力（[MCPE-104934](https://bugs.mojang.com/browse/MCPE-104934)）

**命令**

- 基岩服务器命令的文档已更新，以显示权限重新加载和列出正确的命令（[BDS-2341](https://bugs.mojang.com/browse/BDS-2341)）
- 传送命令现在正确对齐您的旋转与目标实体（[MCPE-35979](https://bugs.mojang.com/browse/MCPE-35979)）
- 选择器参数选项在指定一个后可以再次正确显示和自动完成（[MCPE-59794](https://bugs.mojang.com/browse/MCPE-59794)）
- 生成事件现在作为'/summon'命令的建议显示（[MCPE-101112](https://bugs.mojang.com/browse/MCPE-101112)）
- 'SendCommandFeedback'不再阻止显示发出的消息（[MCPE-95217](https://bugs.mojang.com/browse/MCPE-95217)）
- 在同一刻执行多个'/tickingarea add'或'/tickingarea remove'命令将不再导致关于正在使用的常加载区域数量的不准确消息
- 玩家不再通过在同一刻添加所有常加载区域而超过正在使用的独立常加载区域的最大数量
- 添加了'/screenshake'命令的停止动作
- 现在可以使用新的'/structure delete \<name\>'命令从保存的结构列表中删除结构

**记分板**

- 记分板上的分数值现在对齐到表格的右侧（[MCPE-64973](https://bugs.mojang.com/browse/MCPE-64973)）