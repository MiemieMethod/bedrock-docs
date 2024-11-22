---
标题：Minecraft Beta - 1.16.200.57（Xbox One/Windows 10/Android）
日期：2020-11-24T16:58:55Z
更新：2020-11-24T16:59:11Z
类别：Beta和预览信息及更新日志
链接：https://feedback.minecraft.net/hc/en-us/articles/360052476232-Minecraft-Beta-1-16-200-57-Xbox-One-Windows-10-Android
---

**发布于：** 2020年11月24日

在参与Minecraft Beta之前，请阅读以下内容：

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- Beta版本可能不稳定，并且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。有关加入或退出Beta的详细说明，请参见[ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

## 漏洞修复

**性能和稳定性**

- 改进了使用鞘翅飞行时的地形构建速度（[MCPE-85614](https://bugs.mojang.com/browse/MCPE-85614)）  
- 修复了在创造模式下使用工作台时导致游戏崩溃的漏洞  
- 修复了在循环数据驱动区块上发生的失控区块计时队列的问题，该区块会将自身更改为不同的排列。该漏洞可能导致内存问题，增加加载和保存时间，并定期导致游戏停顿  

**技术更改**

- 减少了数据驱动区块几何体的内容警告垃圾信息  
- 修复了专用服务器在初始化服务器实例时将实验性切换状态复制到LevelSettings，以确保使用加载世界中指定的值  
- 修复了数据驱动区块以相同方式缩小UV，防止UV渗漏