---
标题: Minecraft Beta - 1.17.40.20 (Xbox One/Windows 10/Android)
日期: 2021-09-15T13:23:32Z
更新: 2021-09-15T16:08:56Z
分类: Beta和预览信息及更新日志
标签:
  - beta
  - beta_changelog
  - caves&cliffs
链接: https://feedback.minecraft.net/hc/en-us/articles/4409280122381-Minecraft-Beta-1-17-40-20-Xbox-One-Windows-10-Android
---

**发布于:** 2021年9月15日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![bedrock-beta17U4-1-header.jpg](https://feedback.minecraft.net/hc/article_attachments/4409288020237/bedrock-beta17U4-1-header.jpg)

 

哟哟哟！咳咳，失礼了！自从我在这座裸岩山峰上开店以来，我就一直通过山歌与人交流。为了这次基岩版测试更新，我将切换回文字，带来从这些高处到滴水石和繁茂洞穴的更新。希望您喜欢这个测试版，请通过发送反馈到[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)告诉我们您的想法，并在[bugs.mojang.com](http://bugs.mojang.com/)报告您发现的任何漏洞。

我们也非常希望听到您对游戏性能的反馈！在启用洞穴与山崖实验性功能后，请通过这个简短的调查告诉我们您在世界中是否遇到任何延迟：[aka.ms/MCPerfPoll](https://aka.ms/MCPerfPoll)

 

# **此测试版已知问题**

- 蜂巢在世界中生成过于频繁

# **实验性功能**

## **一般**

- 新增了一种山脉生物群系：裸岩山峰！
  - 这只是高耸/雪顶山峰的一种变种，使用石头和沙砾而不是雪和冰，以避免温度冲突，例如丛林中冒出的雪顶山峰
- 修正了山脉草甸中的植被
- 滴水石簇现在只能在滴水石生物群系中找到
- 滴水石地物现在仅在滴水石生物群系中生成
- 山脉生物群系现在具有正确的地物位置，以匹配Java版的侧快照
- 寄生石头可以在新山脉下找到
- 调整了矿物分布以匹配Java版的侧快照
- 云层现在位于Y轴192级
- 调整了生物群系分布、河流大小和地形形状，以提供更好的主世界体验
- 调整了山脉和洞穴生物群系中的生物生成，以匹配Java版的侧快照
- 沼泽中的树木现在可以在水中稍微更深的地方生成
- 深板岩现在在更低的深度生成（[MCPE-125117](https://bugs.mojang.com/browse/MCPE-125117)）
- 滴水石地物现在在深板岩深度生成
- 小滴水石地物的放置逻辑已重构，频率相似但确切位置会有所不同
- 地图现在正确显示零以下Y轴的方块颜色（[MCPE-136638](https://bugs.mojang.com/browse/MCPE-136638)）

## **繁茂洞穴**

- 藤蔓现在在繁茂洞穴中生成，而不是在地表上生成（[MCPE-125800](https://bugs.mojang.com/browse/MCPE-125800)）
- 藤蔓现在可以在零高度以下生长

### **村庄**

- 村庄现在以其所在生物群系的风格生成（[MCPE-136939](https://bugs.mojang.com/browse/MCPE-136939)）

# **非实验性功能和漏洞修复**

## **方块**

- 落下的钟乳石现在正确偏移，以避免与其预期击中箱外的实体交互（[MCPE-132772](https://bugs.mojang.com/browse/MCPE-132772)）
- 蜂箱现在在世界中朝南生成

### **蜡烛蛋糕方块**

- 按下蜡烛蛋糕的“使用”按钮现在消耗正确数量的蛋糕切片（[MCPE-135519](https://bugs.mojang.com/browse/MCPE-135519)）

## **角色创建器**

- 修复了使用角色创建器时可能发生的崩溃
- 调整了默认Steve皮肤的颜色，以匹配默认Steve（[MCPE-120818](https://bugs.mojang.com/browse/MCPE-120818)）
- 修改了朋友更改皮肤时的消息（[MCPE-92772](https://bugs.mojang.com/browse/MCPE-92772)）

## **命令**

- 使用@e\[type=\]时不再显示教育版物品作为选项（[MCPE-78363](https://bugs.mojang.com/browse/MCPE-78363)）

## **游戏玩法**

- 修复了一个漏洞，该漏洞导致玩家在更换维度时，如果下界传送门下方有熔岩，则会着火（[MCPE-28765](https://bugs.mojang.com/browse/MCPE-28765)）
- 玩家在生存模式下不再可以在饥饿值满时吃食物（[MCPE-60807](https://bugs.mojang.com/browse/MCPE-60807)）
- 在世界生成期间，海草不再在睡莲下生成，以避免破坏它们
- 村民不再可以不停地开关门（[MCPE-28055](https://bugs.mojang.com/browse/MCPE-28055)）
- 制图师现在在所有平台上更一致地提供新地图

## **世界生成**

- 紫晶洞现在在要塞中生成的几率大大降低，如果生成也不会破坏末地传送门（[MCPE-129861](https://bugs.mojang.com/browse/MCPE-129861），[MCPE-128799](https://bugs.mojang.com/browse/MCPE-128799)）

## **图形**

- 改进了地下情况的世界可见性剔除，以消除在隧道/楼梯尽头看到天空的情况（[MCPE-128372](https://bugs.mojang.com/browse/MCPE-128372)）

## **生物**

- 改进了生物在部分方块周围的路径规划（[MCPE-127381](https://bugs.mojang.com/browse/MCPE-127381)）
- 盔甲不再在掠夺者和卫道士上渲染，但仍然会获得盔甲效果（[MCPE-74242](https://bugs.mojang.com/browse/MCPE-74242)）
- 修复了一个生物渲染问题，导致卫道士的斧头在未攻击时仍然可见，尤其是在旧的资源包中（[MCPE-123229](https://bugs.mojang.com/browse/MCPE-123229)）
- 更多生物将在主世界的地下生成

## **细雪**

- 细雪在远处观看时不再消失（[MCPE-127565](https://bugs.mojang.com/browse/MCPE-127565)）

## **结构方块**

- 活板门在从结构方块加载时现在正确旋转（[MCPE-66933](https://bugs.mojang.com/browse/MCPE-66933)）

## **用户界面**

- 修复了在某些UI部分无法使用方向键和十字键导航的问题（[MCPE-132826](https://bugs.mojang.com/browse/MCPE-132826)）
- 修复了在禁用屏幕动画的成就界面上暂停游戏后可能显示错误消息的问题（[MCPE-132269](https://bugs.mojang.com/browse/MCPE-132269)）
- 修复了设置中添加了一个模糊的游戏规则的问题（[MCPE-139025](https://bugs.mojang.com/browse/MCPE-139025)）
- 修复从自定义服务器到编辑服务器按钮的键盘/十字键导航
- Windows 10 ARM架构的PC上可用新的成就界面
- 开始屏幕上的登录文本不再与市场按钮重叠
- 在设置屏幕上为文本转语音添加选项卡标题和“选项卡”之间的空格
- 在登录失败的模态中添加“更多信息”按钮

# **技术更新**

## **数据驱动物品**

- 更新了方块旋转组件的文档
- 向文档和内容错误中添加了方块组件所需的切换

## **命令**

- 带有“需要红石”和非零“刻延迟”的命令方块现在仅在保持供电达到延迟持续时间时执行（[MCPE-74281](https://bugs.mojang.com/browse/MCPE-74281)）
- 修复了/scoreboard命令的侧边栏显示在文本长度变化时的对齐问题

## **数据驱动方块**

- 更新了方块爆炸抗性文档

## **图形**

- 修复了在视口外附着于生物时未能渲染绳索的问题（[MCPE-63931](https://bugs.mojang.com/browse/MCPE-63931)）
- 为使用材料但未提供所需数量的纹理到渲染控制器添加了内容错误
- 在一部分Android设备（ARMv7）上测试RenderDragon引擎

## **生物**

- 修复了通过/summon命令召唤经验球的能力（[MCPE-130835](https://bugs.mojang.com/browse/MCPE-130835)）
- 修复了在区块丢弃场景中仅显示实体销毁的问题

## **Molang**

- 修复了query.item_remaining_use_duration具有不正确缩放或反转结果的问题（此修复自引擎版本1.17.30起为版本更改）
- 为像'text' + 3这样的表达式添加新的编译错误，以前被忽略（此修复自引擎版本1.17.40起为版本更改）

## **用户界面**

- 添加了一个ImGUI窗口，以便更轻松地查看内容错误

## **GameTest框架（实验性）**

- 将方法succeedWhenBlockTypePresent重命名为succeedWhenBlockPresent
- 修复了一个错误，该错误导致属性id在自定义实体上返回“未知”（[MCPE-137786](https://bugs.mojang.com/browse/MCPE-137786)）
- 从属性id返回的标识符字符串现在包括物品的命名空间

**     GameTestSequence**

- 移除了方法thenWaitWithDelay
- 添加了方法thenWaitAfter(delayTicks: number, callback: () => undefined) - 在延迟后，每个刻执行给定的回调，直到成功。回调中抛出的异常将结束序列执行

**玩家**

- 修复了位置属性返回玩家高度不正确的问题
- 添加了属性id

**方块**

- 用属性location替换方法getLocation
- 用属性permutation替换方法getPermutation
- 用属性type替换方法getType
- 用属性isWaterlogged替换方法isWaterlogged和setWaterlogged
- 用属性permutation替换方法getBlockData
- 用属性isEmpty替换方法isEmpty
- 移除了属性canBeWaterlogged

**方块类型**

- 用属性id替换方法getName
- 用属性canBeWaterlogged替换方法canBeWaterlogged

**方块排列**

- 用属性type替换方法getType