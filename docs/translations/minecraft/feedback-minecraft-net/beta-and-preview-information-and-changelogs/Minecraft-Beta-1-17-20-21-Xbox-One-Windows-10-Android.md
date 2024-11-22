---
标题: Minecraft Beta - 1.17.20.21 (Xbox One/Windows 10/Android)
日期: 2021-06-30T15:18:59Z
更新: 2021-06-30T16:03:25Z
类别: Beta和预览信息与更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4404090095885-Minecraft-Beta-1-17-20-21-Xbox-One-Windows-10-Android
---

**发布于:** 2021年6月30日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

又到了另一个洞穴与山崖测试版更新的时间！请继续在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论中给我们反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的任何新漏洞。

 

![crystal_16x9.jpg](https://feedback.minecraft.net/hc/article_attachments/4404090082061/crystal_16x9.jpg)

 

## **功能与漏洞修复** 

**命令** 

- 修复了在未加载区域用命令放置结构时可能发生的崩溃，以及该结构被删除的情况  

**图形** 

- 修复了在RTX开启时，告示牌上的文本在地图上绘制的问题  

**物品** 

- 时钟和指南针物品在配方书中不再有效 ([MCPE-36354](https://bugs.mojang.com/browse/MCPE-36354))  

**结构方块** 

- 为结构方块添加了角落模式，该模式与保存模式的检测按钮一起使用，以自动设置您想要保存的区域  

<!-- -->

- 修复了在结构方块界面中被驯服的狼显示为透明的问题   

## **技术更新** 

**GameTest框架（实验性）** 

- 将辅助方法worldLocation(location : BlockLocation)重命名为worldBlockLocation(location : BlockLocation) 
- 将辅助方法relativeLocation(location : BlockLocation)重命名为relativeBlockLocation(location : BlockLocation) 
- 添加了辅助方法worldLocation(relativeLocation : Location) : Location - 从相对于GameTest结构方块的坐标位置返回一个新的相对于世界的坐标位置 
- 添加了辅助方法relativeLocation(worldLocation : Location) : Location - 从一个位置返回一个新的相对于当前GameTest结构方块的坐标位置 
- 添加了辅助方法spawnWithoutBehaviorsAtLocation(entityIdentifier : string, location : Location) : Entity - 在指定位置生成一个没有任何AI行为的实体 
- 添加了辅助方法rotateDirection(direction : Direction) : Direction - 相对于GameTest结构的旋转旋转给定的方向 
- 添加了辅助方法getTestDirection() : Direction - 根据其结构旋转返回GameTest所面对的方向 

**命令** 

- 通过动画运行的命令现在将在所有平台上按照动画文件中定义的顺序运行，包括Realm  
- 在仅部分加载的常加载区域中放置的命令或结构现在将在所需区块已加载的情况下被视为已加载