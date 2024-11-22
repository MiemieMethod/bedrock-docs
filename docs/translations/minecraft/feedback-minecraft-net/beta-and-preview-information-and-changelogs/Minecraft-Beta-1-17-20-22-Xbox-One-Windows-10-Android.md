---
标题: Minecraft Beta - 1.17.20.22 (Xbox One/Windows 10/Android)
日期: 2021-07-14T13:11:23Z
更新: 2021-07-14T15:47:21Z
类别: Beta 和预览信息及更新日志
标签:
  - beta
  - beta_changelog
  - 洞穴与山崖
链接: https://feedback.minecraft.net/hc/en-us/articles/4404997186189-Minecraft-Beta-1-17-20-22-Xbox-One-Windows-10-Android
哈希:
  experimental-features: experimentalfeatures
  gametest-framework-experimental: gametestframework-experimental
---

**发布于:** 2021年7月14日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的早期版本中打开，因此请制作世界的副本以防止丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Screen_Shot_07-13-21_at_01.43_PM.PNG](https://feedback.minecraft.net/hc/article_attachments/4404990171661/Screen_Shot_07-13-21_at_01.43_PM.PNG)

我们今天发布了另一个基岩版Beta更新，并修复了许多漏洞！此外，我们对敌对生物的生成方式进行了相当重要的更改——要测试这一点，您需要启用[Caves and Cliffs实验性功能](https://feedback.minecraft.net/hc/en-us/community/posts/360075718432)。我们希望这一更改能让您的洞穴探险之旅稍微安全一些，但您仍然需要避免在满是钻石的快捷栏中掉入熔岩。不是说这种情况经常发生，对吧？

请在<https://aka.ms/CavesCliffsFeedback>的讨论中给我们反馈，并在[https://bugs.mojang.com](https://bugs.mojang.com/)上搜索并报告您可能遇到的任何新漏洞。

# **实验性功能**

- 怪物仅会在完全黑暗中生成
  - 这一更改旨在平衡玩家照亮新更大洞穴的能力，使其免受怪物生成的威胁
  - 请注意，此更改仅影响块光，而不影响天空光
  - 请在[aka.ms/CCMobSpawningFeedback](https://aka.ms/CCMobSpawningFeedback)上给我们反馈！

# **功能和漏洞修复**

## **稳定性和性能**

- 修复了在游戏过程中可能发生的几次崩溃

## **方块**

- 紫水晶簇方块现在无法放置在草地路径方块上
- 更正了深板岩青金石矿块的名称，从深板岩青金石矿更改为深板岩矿([MCPE-123605](https://bugs.mojang.com/browse/MCPE-123605))
- 发射器现在在移除水时会移除气泡柱([MCPE-56462](https://bugs.mojang.com/browse/MCPE-56462))
- 海泡菜现在会根据是否在水中而改变光照([MCPE-131642](https://bugs.mojang.com/browse/MCPE-131642))
- 雪层现在会被火把等光源融化([MCPE-131272](https://bugs.mojang.com/browse/MCPE-131272))
- 原版趋同：下落的重力方块在落在某些方块上时将不再破坏([MCPE-20109](https://bugs.mojang.com/browse/MCPE-20109))

## **游戏玩法**

- 原版趋同：在苔藓块上使用骨粉现在也会替换凝灰岩块([MCPE-125922](https://bugs.mojang.com/browse/MCPE-125922))
- 原版趋同：修复了持有光源方块时未正确显示的问题([MCPE-123249](https://bugs.mojang.com/browse/MCPE-123249))
- 修复了在启用保持物品规则时，玩家死亡后持有物品在其他玩家视角中未消失的问题([MCPE-64235](https://bugs.mojang.com/browse/MCPE-64235))
- 在区块之间放置的下界传送门在离开下界时不再破坏([MCPE-74333](https://bugs.mojang.com/browse/MCPE-74333))
- 剪刀现在可以更快地切割藤蔓和发光地衣([MCPE-123139](https://bugs.mojang.com/browse/MCPE-123139))
- 哭泣藤和缠怨藤在玩家破坏后现在会正确生长([MCPE-90932](https://bugs.mojang.com/browse/MCPE-90932))

## **图形**

- 调整了纹理图集中mipmap级别1的高清纹理的填充，以修复纹理渗漏
- 附魔台书本的一半不再渲染为黑色([MCPE-106627](https://bugs.mojang.com/browse/MCPE-106627))
- 活塞移动的方块在移动时不再是白色([MCPE-66250](https://bugs.mojang.com/browse/MCPE-66250))

## **生物**

- 美西螈仅在其下方最多10个方块处有石头时生成，而不在气泡柱中
- 盔甲架在被火或熔岩摧毁时现在会掉落装备的物品([MCPE-94603](https://bugs.mojang.com/browse/MCPE-94603))
- 限制了可生成的幻翼生物的最大数量([MCPE-106557](https://bugs.mojang.com/browse/MCPE-106557))
- 山羊现在会播放其“冲击3”的声音([MCPE-127757](https://bugs.mojang.com/browse/MCPE-127757))

## **用户界面**

- 配方书中的合成估算不再与实际结果不同
- 实验性警告消息在加载测试版世界时不再不一致地显示
- 光标物品不再计入配方书中的配方材料
- 当玩家耗尽材料时，选定的配方现在会被取消选择
- 使用搜索机制时，配方书中不再显示不可合成的配方
- 如果任何其他材料不可用，下界方块现在会出现在合成网格中
- 修复了在玩家通过有线网络连接时出现的无线网络连接错误消息
- 修复了角色创建器中的各种拼写错误
- 小部件按钮的悬停在完全加载完成之前会显示损坏的外观
- 修复了一些日文字体字符的可读性问题
- 骑乘动物时在非触摸屏上现在会显示正确的提示框术语

# **技术更新**

## **GameTest框架（实验性）**

- 将BlockTypes类重命名为MinecraftBlockTypes
- 将Effects类重命名为MinecraftEffectTypes
- 将Items类重命名为MinecraftItemTypes
- 事件
- 为刻事件添加只读属性currentTick - 返回当前服务器刻
- 将事件createEntity重命名为entityCreate
- 将事件addEffect重命名为effectAdd
- 将事件activatePiston重命名为pistonActivate
- 将事件beforeActivatePiston重命名为beforePistonActivate
- 将事件explodeBlock重命名为blockExplode
- 将事件changeWeather重命名为weatherChange

## **命令**

- 目标选择器ry和rym现在支持绕北方循环

## **物品**

- 杀死具有未知战利品表条目类型的自定义生物将不再导致崩溃，而是会抛出内容错误([MCPE-129006](https://bugs.mojang.com/browse/MCPE-129006))

## **生物**

- 指定initialEvent的兔子现在会正确缩放到成年兔子的大小([MCPE-76643](https://bugs.mojang.com/browse/MCPE-76643))

## **生成**

- 类似于spawns_on_block_filter，spawns_above_block_filter指定了一个方块列表和一个距离。生物只能在指定生成点下方的最近方块在该列表中时生成（不包括水和空气）。“minecraft:spawns_above_block_filter”: { “blocks”: “minecraft:stone”, “distance”: 10 }