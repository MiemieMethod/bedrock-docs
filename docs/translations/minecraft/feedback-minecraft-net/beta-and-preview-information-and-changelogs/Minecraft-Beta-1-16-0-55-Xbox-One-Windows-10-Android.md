---
标题: Minecraft Beta - 1.16.0.55 (Xbox One/Windows 10/Android)
日期: 2020-03-31T17:39:26Z
更新: 2020-04-15T21:14:30Z
类别: Beta和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/360041294872-Minecraft-Beta-1-16-0-55-Xbox-One-Windows-10-Android
---

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中玩的任何世界无法在之前的游戏版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**注意：** 此测试版是完整下界更新的一个正在开发中的版本。在Java版快照中看到的一些功能可能尚未出现。

**此测试版中的已知问题：**

- 市场中的缩略图图标当前未正确加载

# **修复：**

**崩溃和稳定性**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了在iOS上创建新世界时可能发生的崩溃
- 修复了在存在粒子的世界中退出时可能发生的崩溃
- 修复了与玩家进入水有关的多个崩溃问题
- 修复了当生物的状态发生变化时可能发生的崩溃

**一般**

- 光传播现在正常工作，修复了敌对生物生成的问题（[MCPE-49616](https://bugs.mojang.com/browse/MCPE-49616)）
- 在+250MB世界中，区块不再加载失败（[MCPE-58514](https://bugs.mojang.com/browse/MCPE-58514)）
- 修复了在方块变化后光线持续存在的漏洞
- 常加载区域不再能在创建的同一刻被移除（[MCPE-36769](https://bugs.mojang.com/browse/MCPE-36769)）
- 光照现在可以正确穿过区块/子区块边界（[MCPE-58182](https://bugs.mojang.com/browse/MCPE-58182)）
- 修复了可能导致服务器区域显示光照错误的问题
- 为/replaceitem添加了新的重载选项，可以选择destroy（旧行为）或keep（如果该槽位被物品占用，命令将返回错误）
- 平滑相机选项（来自完整键盘游戏）不再抖动，恢复平滑（[MCPE-54969](https://bugs.mojang.com/browse/MCPE-54969)）
- 当玩家在下界或末地死亡时，屏幕不再抖动

**游戏玩法**

- 现在可以使用铁桶从气泡柱中收集水（[MCPE-37571](https://bugs.mojang.com/browse/MCPE-37571)）
- 投掷钓鱼竿不再会附着在玩家肩上的鹦鹉上（[MCPE-60361](https://bugs.mojang.com/browse/MCPE-60361)）
- 完全成熟的甜浆果丛现在可以在持有骨粉时收获（[MCPE-54206](https://bugs.mojang.com/browse/MCPE-54206)）
- 趋同：胡萝卜钓竿、盾牌和锹在基岩版中现在一致地损耗耐久
- 点燃TNT方块后，火焰弹现在会被消耗（[MCPE-42938](https://bugs.mojang.com/browse/MCPE-42938)）
- 玩家图标不再在定位地图上显示为白色方块

**方块**

- 附加在门上的墙上告示牌在门的下半部分被破坏后不再悬浮（[MCPE-43748](https://bugs.mojang.com/browse/MCPE-43748)）

**生物**

- 苦力怕在失去对目标的视线后不再立即失去仇恨（[MCPE-32815](https://bugs.mojang.com/browse/MCPE-32815)）
- 恶魂的击中箱现在与其渲染匹配（[MCPE-44326](https://bugs.mojang.com/browse/MCPE-44326)）
- 修复了“MeleeAttackGoal”，允许实体攻击其下方的目标实体
- 铁傀儡的腿不再摆动得那么远

**图形和渲染**

- 经验球已实现数据驱动
- 火球已实现数据驱动
- NPC几何体和动画已实现数据驱动
- 物品从熔炉中移除时不再闪烁绿色
- 修复了玻璃和水在彼此靠近时可能错误绘制的漏洞
- 修复了添加到指南针上的自定义闪烁纹理问题

**脚本和附加包**

- 从“minecraft:shooter”中移除了type属性，因为它从未被使用
- 更新了“minecraft:spawn_entity”，使其具有内部entities对象或数组
- 更新了“minecraft:behavior.circle_around_anchor”行为
- 为“minecraft:behavior.defend_village_target”目标添加了“attack_chance”
- 修复了查询已移除或摧毁的实体时仍被视为有效的问题
- 在“minecraft:spawn_entity”的“spawn_item”字段中，非法物品现在会显示错误
- “StompEggGoal”不再使用“search_count”，因为它现在会搜索指定区域内的所有方块
- 修复了“navigation.walk”，以处理在飞行实体上使用的情况，从而使飞行实体在接触地面时不会造成延迟
- “minecraft:density_limit”组件现在在生成规则文档部分中有文档说明（[MCPE-61126](https://bugs.mojang.com/browse/MCPE-61126)）
- 如果在“transform_to_item”字段中提供无效物品名称，将显示内容错误
