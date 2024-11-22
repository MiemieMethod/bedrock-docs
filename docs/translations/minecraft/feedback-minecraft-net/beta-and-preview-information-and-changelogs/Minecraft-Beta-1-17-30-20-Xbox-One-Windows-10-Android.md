---
标题: Minecraft Beta - 1.17.30.20 (Xbox One/Windows 10/Android)
日期: 2021-08-04T13:43:02Z
更新: 2021-08-04T15:44:55Z
类别: Beta 和预览信息及更新日志
标签:
  - beta
  - beta_changelog
  - 洞穴与山崖
链接: https://feedback.minecraft.net/hc/en-us/articles/4406445924237-Minecraft-Beta-1-17-30-20-Xbox-One-Windows-10-Android
哈希:
  edu-chemistry: edu--chemistry
---

**发布:** 2021年8月4日

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入Beta将用一个正在开发中的版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防丢失
- Beta版本可能不稳定，并且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Screen_Shot_07-28-21_at_11.24_AM.JPG](https://feedback.minecraft.net/hc/article_attachments/4406445864461/Screen_Shot_07-28-21_at_11.24_AM.JPG)

我们今天有另一个基岩版Beta更新，我们修复了一些漏洞！

请在<https://aka.ms/CavesCliffsFeedback>的讨论中向我们反馈，并在[https://bugs.mojang.com](https://bugs.mojang.com/)搜索并报告您可能遇到的任何新漏洞。

# **特性和漏洞修复**

## **稳定性和性能**

- 修复了在游戏过程中可能发生的几次崩溃
- 修复了在下载大型市场世界时有时会发生的崩溃

## **辅助功能**

- 语音朗读现在正确读取物品栏中的物品名称
- 物品栏网格槽位不再被双重计算用于语音朗读焦点控制

## **游戏玩法**

- 当持有另一个光源方块时，光源方块现在可见，并显示亮度值（[MCPE-123249](https://bugs.mojang.com/browse/MCPE-123249)）
- 修复了在持有光源方块时左键点击光源方块未被移除的问题（[MCPE-123258](https://bugs.mojang.com/browse/MCPE-123258)）
- 修复了右键点击光源方块时亮度无法调整的问题（[MCPE-123387](https://bugs.mojang.com/browse/MCPE-123387)）
- 修复了光源方块的击中箱问题（[MCPE-135277](https://bugs.mojang.com/browse/MCPE-135277)）
- 修复了在未持有屏障方块时屏障方块可被破坏的问题
- 在生存模式下，将船放置在水面上后，船现在会正确从物品栏中消失（[MCPE-136445](https://bugs.mojang.com/browse/MCPE-136445)）

## **用户界面**

- 语音朗读聊天设置再次正确叙述聊天消息（[MCPE-129901](https://bugs.mojang.com/browse/MCPE-129901)）
- 侧边栏字符串在加载新语言或当前语言更改时现在正确本地化
- 更新了成就按钮，并将其从个人资料屏幕移动到主菜单和暂停屏幕
- 为VR启用了新的成就屏幕（不包括PSVR）

## **原版趋同**

- 在滑翔时吃紫颂果不再对玩家造成坠落伤害（[MCPE-112621](https://bugs.mojang.com/browse/MCPE-112621)）
- 修复了骷髅未使用双臂持弓的动画趋同问题（[MCPE-670](https://bugs.mojang.com/browse/MCPE-670)）

## **生物**

- 修复了在结构方块预览窗口中查看生物时，有时会渲染出不正确几何体的问题（[MCPE-95183](https://bugs.mojang.com/browse/MCPE-95183)）
- 实验性特性：凋零现在可以在负高度生成（[MCPE-125270](https://bugs.mojang.com/browse/MCPE-125270)）
- 恶魂不再在小于5x4x5的区域生成（[MCPE-133687](https://bugs.mojang.com/browse/MCPE-133687)）
- 岩浆怪不再在小于3x3x2的区域生成（[MCPE-46540](https://bugs.mojang.com/browse/MCPE-46540)）
- 中型岩浆怪现在有更大的击中箱（[MCPE-132159](https://bugs.mojang.com/browse/MCPE-132159)）
- 潜影盒在世界边界处发射时现在会保留在发射器中（[MCPE-130085](https://bugs.mojang.com/browse/MCPE-130085)）

## **方块**

- Unicode字体现在在发光文本的告示牌上正确高亮显示（[MCPE-130072](https://bugs.mojang.com/browse/MCPE-130072)）
- 含水方块不再偶尔变成幽灵方块（[MCPE-136537](https://bugs.mojang.com/browse/MCPE-136537)）
- 面朝南、东或西放置的南瓜，如果用精准采集工具开采，现在可以用来与村民交易（[MCPE-105540](https://bugs.mojang.com/browse/MCPE-105540)）
- 不再可以向没有任何支撑方块的蜡烛添加更多蜡烛（[MCPE-130810](https://bugs.mojang.com/browse/MCPE-130810)）

## **图形**

- 使用迷雾时，天空不再通过大型封闭区域的墙壁渲染

# **技术更新**

## **教育/化学**

- 新的化学材料减少可以在JSON文件中定义
- 黑板现在在放置时一致出现

## **命令**

- '/clone'命令现在复制拉杆和红石粉的信号强度
- '/structure'命令现在可以指定一个\<to: x y z\>位置参数，y值可以低于0，只要它等于或高于该维度的最小高度
- 为游戏模式命令选择器添加了Intellisense选项功能：“d”和“default”
- 命令方块矿车现在可以在其命令中使用自我选择器(@s)来针对自身（[MCPE-60126](https://bugs.mojang.com/browse/MCPE-60126)）
- "/time set"命令现在在指定时间超过24000或低于当前时间时设置正确的时间和日期（例如，"/time set 0"将日期设置为0，"/time set 28000"将日期设置为1），并且"/time"现在可以设置或添加负的世界时间（[MCPE-43394](https://bugs.mojang.com/browse/MCPE-43394)）

## **物品**

- 更新了物品组件的文档格式
- 使用水桶收集鱼的功能已被版本锁定，以防止破坏旧的世界模板

## **生物**

- 修复了为通过'spawn_entity'组件生成的投射物添加发射点位置偏移的能力
- 修复了为通过'spawn_entity'组件生成的投射物添加角度偏移的能力
- 修复了通过交互召唤的投射物偏移不起作用的问题
- 修复了投射物'angleoffset'值仅在射手骑乘其他实体时才反映的问题
- 修复了在指定投射物偏移时，投射物发射点围绕生物的旋转

## **Molang**

- 修复了'query.item_remaining_use_duration'具有不正确缩放或反转结果的问题（这是为了解决引擎版本1.17.30的版本变更）
- 添加了'query.facing_target_to_range_attack'，返回查询的活动对象'minecraft:behavior.ranged_attack'目标是否正在运行

## **Molang文档**

- 改进了与实验相关的Molang文档
  - 实验查询和语言表达式现在列出它们所需的实验
- 版本变更现在在文档中详细说明，从'query.item_remaining_use_duration'修复开始