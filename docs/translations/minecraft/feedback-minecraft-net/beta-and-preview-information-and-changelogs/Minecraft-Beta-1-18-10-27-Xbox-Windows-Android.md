---
标题: Minecraft Beta - 1.18.10.27 (Xbox / Windows / Android)
日期: 2022-01-11T18:02:14Z
更新: 2022-01-11T18:31:38Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4420146557325-Minecraft-Beta-1-18-10-27-Xbox-Windows-Android
---

**发布于:** 2022年1月11日

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- Beta版本可能不稳定，且不代表最终版本的质量
- Beta仅在Xbox、Windows和Android（Google Play）上可用。要加入或退出Beta，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Picture1.jpg](https://feedback.minecraft.net/hc/article_attachments/4420159360013/Picture1.jpg)

以下是本周Beta中的新内容！请在[aka.ms/MCFrogFeedback](https://aka.ms/MCFrogFeedback)的讨论串中给我们提供任何具体反馈或建议，并且请随时在[bugs.mojang.com](http://bugs.mojang.com/)搜索并报告您可能发现的任何漏洞。

**实验性特性**

**青蛙**

- 青蛙不再吃山羊！ ([MCPE-151536](https://bugs.mojang.com/browse/MCPE-151536))

**特性和漏洞修复**

**方块**

- 放置在区块边界上的可可果荚在重新加载世界时不再破坏 ([MCPE-67479](https://bugs.mojang.com/browse/MCPE-67479))
- 结构方块的结构现在能够正确变换（旋转和/或镜像）多面方块（例如发光地衣）

**游戏玩法**

- 修复了侦测器方块在物品栏中保持点亮状态的问题，如果在闪烁时被摧毁 ([MCPE-114173](https://bugs.mojang.com/browse/MCPE-114173))
- 修复了画作与荧光物品展示框、告示牌、旗帜和火把重叠的问题
- 掠夺者前哨站现在生成正确数量的掠夺者和铁傀儡 ([MCPE-141499](https://bugs.mojang.com/browse/MCPE-141499))

**图形**

- 船在长时间骑乘后下船时不再消失 ([MCPE-108568](https://bugs.mojang.com/browse/MCPE-108568), [MCPE-125388](https://bugs.mojang.com/browse/MCPE-125388))
- 船桨现在与船的颜色相同 ([MCPE-150492](https://bugs.mojang.com/browse/MCPE-150492))

**生物**

- 未驯服的猫现在可以被系上绳子
- 守卫者和远古守卫者在锁定敌人或玩家时不再下沉

**用户界面**

- 物品栏屏幕上的建筑选项卡在使用口袋用户界面时现在具有正确的颜色
- 修复了在使用口袋用户界面时缺少物品栏槽位的问题 ([MCPE-151545](https://bugs.mojang.com/browse/MCPE-151545))
- 修复了创造模式物品栏中空白槽位的问题，这可能导致在世界中的交互问题 ([MCPE-151506](https://bugs.mojang.com/browse/MCPE-151506))

**世界生成**

- 箱子和刷怪笼现在在结构中正确生成 ([MCPE-23416](https://bugs.mojang.com/browse/MCPE-23416)) ([MCPE-48622](https://bugs.mojang.com/browse/MCPE-48622)) ([MCPE-97295](https://bugs.mojang.com/browse/MCPE-97295))

**技术更新**

**稳定性和性能**

- 减少常加载区域的内存和加载时间

**GameTest框架（实验性）**

- 添加函数 setVelocity(velocity: Vector): bool- 设置此实体的速度
- 添加属性 viewVector: Vector- 表示实体正在查看的方向，作为一个向量
- 添加属性 headLocation: Location- 表示实体头部的位置
- 添加属性 bodyRotation: number- 表示实体的身体旋转，作为浮点数（以度为单位）

**动画**

- 修复了动画事件、音效事件和粒子事件在事件时间指定等于总“animation_length”时不会触发的漏洞
- 修复了在“animation_length”未明确指定时，事件时间未被考虑在动画长度计算中的问题

**通用**

- 修复了导致以数字值而非字符串声明的format_versions未能正确解析的问题
- 当从具有Caves and Cliffs更新之前的基础游戏版本的模板创建平坦世界时，层将不再悬空64个方块

**Molang**

- 添加alland查询.any以检查一个值是否匹配以下所有或任何值
- 添加in_range以检查一个值是否在最小值和最大值之间（包括）的范围内
- 添加query.in_range以检查一个值是否在最小值和最大值之间（包括）的范围内