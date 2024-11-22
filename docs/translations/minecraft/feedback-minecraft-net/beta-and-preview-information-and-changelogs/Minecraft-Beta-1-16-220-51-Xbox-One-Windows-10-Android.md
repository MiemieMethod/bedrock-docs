---
标题: Minecraft Beta - 1.16.220.51 (Xbox One/Windows 10/Android)
日期: 2021-03-11T15:36:32Z
更新: 2021-03-11T17:10:07Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360058319571-Minecraft-Beta-1-16-220-51-Xbox-One-Windows-10-Android
---

**发布于:** 2021年3月11日

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入测试版将用一个正在开发中的Minecraft版本替代您的游戏
- 您将无法访问Realm，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。有关加入或退出测试版的详细说明，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

在本周的测试版中，我们修复了一些重要的漏洞！您仍然可以通过在您的世界中启用“实验性功能”开关来测试令人兴奋的新洞穴和悬崖特性！（您可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)了解更多关于使用开关的信息。）您可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中给我们反馈这些特性，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的任何新漏洞。

 

![mountains_1280_720.jpg](https://feedback.minecraft.net/hc/article_attachments/360088994311/mountains_1280_720.jpg)

 

# 漏洞修复

- 使用铁桶挖掘/收集细雪的声音现在已分配到正确的声音类别中（[MCPE-111739](https://bugs.mojang.com/browse/MCPE-111739)）
- 玩家在退出细雪后不再持续发出粒子效果（[MCPE-111679](https://bugs.mojang.com/browse/MCPE-111679)）
- 细雪块不再出现在创造菜单中（[MCPE-105407](https://bugs.mojang.com/browse/MCPE-105407)）
- 修复了溺尸在攻击时反向持有三叉戟的问题（[MCPE-118213](https://bugs.mojang.com/browse/MCPE-118213)）
- 启用了Xbox上的“寻找朋友”按钮

**性能与稳定性**

- 在启用垂直同步时，Windows 10的输入延迟得到了改善（[MCPE-98861](https://bugs.mojang.com/browse/MCPE-98861)）

**辅助功能**

- 修复了UI屏幕阅读器未能读取“在线游戏未评级”弹出窗口中默认控制器焦点和复选框状态的漏洞

**技术修复和更改**

- 将所有“Actor”的引用重命名为“Entity”
- 将“BlockPos”重命名为“BlockLocation”
- 在GameTest中添加了startSequence，允许对高级测试序列进行更细致的控制
- GameTest序列回调不再将测试作为参数，因为初始测试对象现在与整个测试的生命周期相同
- 更新行为包以在使用其他原生模块时要求显式模块依赖关系
- 如果“render_controllers”中没有与该名称匹配的渲染控制器，则将被视为内容错误
- 版本1.16.100之前的Entity json不再因弃用字段“minecraft:foot_size”而产生内容错误
- 修改了“animation_controllers.json”中的条件，以允许生物进入“wield_third_person_raise”（[MCPE-118213](https://bugs.mojang.com/browse/MCPE-118213)）
- 修复了加载世界时导致“未处理请求未知变量”的连续molang错误的问题