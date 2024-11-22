---
标题: Minecraft Beta - 1.18.10.22 (Xbox / Android)
日期: 2021-12-09T15:59:09Z
更新: 2021-12-09T21:37:57Z
分类: 测试版和预览信息及更改日志
链接: https://feedback.minecraft.net/hc/en-us/articles/4416062048397-Minecraft-Beta-1-18-10-22-Xbox-Android
---

**发布于:** 2021年12月9日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 此测试版仅在Xbox和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明。

![一个雪覆盖的Minecraft村庄](https://feedback.minecraft.net/hc/article_attachments/4416078376333/Screen_Shot_12-09-21_at_12.28_PM.JPG)

 

又到了另一个基岩版测试版的时间！一如既往，我们非常感谢您发送给我们的所有反馈，请在[bugs.mojang.com](http://bugs.mojang.com/)报告您可能发现的任何漏洞。正如我们经常做的，这周的测试版中有一些小的原版趋同漏洞。如果您想告诉我们您希望看到的其他小的趋同修复和功能，请在接下来的几天内通过此玩家调查告诉我们：<https://aka.ms/MCParitySurvey>

 

# **功能和漏洞修复**

## **方块**

- 在Y=1到Y=4之间（包括）的基岩层不一致的世界（例如在这些层中生成或放置了非基岩的情况）现在会正确且一致地用深板岩替换基岩。 ([MCPE-149251](https://bugs.mojang.com/browse/MCPE-149251))
- 在潜行时，现在可以将光源方块放置在其他光源方块上 ([MCPE-137744](https://bugs.mojang.com/browse/MCPE-137744))

## **游戏玩法**

- 修复了与制图师村民交易地图时可能发生的崩溃 ([MCPE-142388](https://bugs.mojang.com/browse/MCPE-142388))
- 修复了食物给予效果持续时间过长20倍的问题 ([MCPE-148553](https://bugs.mojang.com/browse/MCPE-148553))
- 修复了蜂蜜瓶未去除中毒效果的问题
- 修复了玩家在吃紫颂果后未传送的问题
- 玩家在船上朝南时的视角不再突然变化 ([MCPE-148460](https://bugs.mojang.com/browse/MCPE-148460))
- 玩家死亡时，摄像头现在向右倾斜，而不是向左 ([MCPE-148604](https://bugs.mojang.com/browse/MCPE-148604))
- 熔岩的击中箱不再超出熔岩范围

## **图形**

- 更新了泥土小径的侧面纹理 ([MCPE-148568](https://bugs.mojang.com/browse/MCPE-148568))
- 将“door_oak”纹理文件名更改回“door_wood” ([MCPE-148502](https://bugs.mojang.com/browse/MCPE-148502))
- 反转了鹦鹉头部和翅膀底部的纹理 ([MCPE-148573](https://bugs.mojang.com/browse/MCPE-148573))
- 将甜菜根和西瓜种子的纹理向下移动1像素行，以匹配Java版 ([MCPE-148561](https://bugs.mojang.com/browse/MCPE-148561))
- 移除了可可豆阶段0和阶段1纹理中的未使用像素，以匹配Java版
- 更新了盔甲架底座的平滑石头纹理 ([MCPE-148565](https://bugs.mojang.com/browse/MCPE-148565))
- 移除了橡木和铁制上门纹理中的水平线 ([MCPE-148566](https://bugs.mojang.com/browse/MCPE-148566))
- 移除了女巫、唤魔者和卫道士纹理中的兜帽，以匹配Java版
- 更改了红色和蓝色染色玻璃纹理的透明度值，以匹配Java版（原版趋同）
- 修复了铁砧界面上锤子图标的调色板 ([MCPE-148575](https://bugs.mojang.com/browse/MCPE-148575))
- 更新了制图台上的深色橡木木板纹理 ([MCPE-148562](https://bugs.mojang.com/browse/MCPE-148562))
- 更新了木桶底部的云杉木板纹理
- 更新了讲台底座的木板纹理 ([MCPE-148567](https://bugs.mojang.com/browse/MCPE-148567))
- 修复了金色和钻石盔甲纹理中的高亮不一致问题 ([MCPE-148591](https://bugs.mojang.com/browse/MCPE-148591))
- 移除了胡萝卜阶段3纹理中的游荡像素 ([MCPE-148563](https://bugs.mojang.com/browse/MCPE-148563))
- 使美西螈的背面纹理居中 ([MCPE-148571](https://bugs.mojang.com/browse/MCPE-148571))
- 更新了玻璃板顶部纹理，以匹配Java版的新纹理 ([MCPE-148572](https://bugs.mojang.com/browse/MCPE-148572))
- 修复了深色橡木原木的顶部纹理 ([MCPE-148577](https://bugs.mojang.com/browse/MCPE-148577))
- 更新了去皮深色橡木的侧面纹理，以匹配Java版的新纹理 ([MCPE-148576](https://bugs.mojang.com/browse/MCPE-148576))
- 修复了末地水晶光束在末地水晶超出玩家视野时停止渲染的漏洞 ([MCPE-149159](https://bugs.mojang.com/browse/MCPE-149159))
- 修复了某些设备上溺尸纹理在RenderDragon下未正确丢弃透明像素的问题

## **生物**

- 史莱姆再次对雪傀儡表现出攻击性 ([MCPE-146651](https://bugs.mojang.com/browse/MCPE-146651))

## **用户界面**

- 修复了在滑翔时物品栏界面上玩家视觉偏移的问题。之前偏离中心，可能会隐藏界面元素
- 暂停界面上的“邀请加入游戏”按钮在服务器满时现在正确禁用

# **技术更新**

## **通用**

- 减少了与子区块请求系统和数据包优化相关的网络数据包数量

## **图形**

- 在所有Android设备上测试RenderDragon

## **物品**

- 添加了9个新的无序配方JSON文件，替换了硬编码的锻造台合成配方

## **Molang**

- 添加了非实验性的is_name_any、is_item_name_any和is_owner_identifier_any查询
- 修复了relative_block_has_all_tags、block_neighbor_has_all_tags和biome_has_all_tags查询，要求所有标签，而不仅仅是任何标签
- 修复了嵌套条件（三元）运算符解析，从左到右改为从右到左
  - 这是一个Molang版本更改，仅对使用min_engine_version为1.18.10或更高版本的包中的Molang表达式生效
  - 之前的嵌套条件表达式如A?B:C?D:E将被评估为(A?B:C)?D:E，现在它们被评估为A?B:(C?D:E)

# **实验性功能**

## **GameTest框架**

              添加了新的实体查询能力，以新方法的形式在维度和世界中。

- 世界对象
  - 将函数getPlayers : Player\[\]替换为函数getPlayers(options: EntityQueryOptions = undefined) : EntityIterator- 返回一个迭代器，包含维度中的所有玩家集合。可选地，可以使用options过滤结果
  - 为events.addEffect添加了可选参数。此参数将限制回调仅对特定实体触发（见EntityEventOptions）
- 维度对象
  - 添加函数getPlayers(options: EntityQueryOptions = undefined) : EntityIterator- 返回一个迭代器，包含所有玩家的集合。可选地，可以使用options过滤结果
  - 添加函数getEntities(options: EntityQueryOptions = undefined) : EntityIterator- 返回一个迭代器，包含维度中的所有实体集合。可选地，可以使用options过滤结果
- EntityQueryOptions
  - 添加类EntityQueryOptions- 在调用getEntities和getPlayers时提供额外的过滤选项
- EntityQueryScoreOptions
  - 添加类EntityQueryScoreOptions- 与EntityQueryOptions一起使用，以提供记分板过滤
- EntityEventOptions
  - 用于过滤在实体上触发的事件，以限制回调仅对某些事件触发。
  - 属性entity: Entity\[\] - 如果指定，将限制为仅此实体
  - 属性entityTypes: string\[\] - 如果指定，将限制为具有指定类型的实体（例如，minecraft:creeper）