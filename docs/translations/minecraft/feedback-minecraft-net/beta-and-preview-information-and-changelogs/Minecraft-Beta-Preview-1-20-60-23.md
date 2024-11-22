---
title: Minecraft Beta & Preview - 1.20.60.23
date: 2023-12-13T12:57:23Z
updated: 2023-12-13T14:50:22Z
categories: Beta and Preview Information and Changelogs
link: https://feedback.minecraft.net/hc/en-us/articles/22307322045197-Minecraft-Beta-Preview-1-20-60-23
hash:
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: information-on-the-minecraft-preview-and-beta
  h_01HHHQJSE6ZG709W6316GE9541: experimental-features
  h_01HHHQJSE6EY2RKBTQV739W4AV: armadillo
  h_01HHHQJSE6F6YWFHW19HS8W26R: armadillo-scutes
  h_01HHHQJSE670PXD402T06XX2G9: wolf-armor
  h_01HHHQJSE6ZPPKN8NHHZ7ZYFDX: blocks
  h_01HHHQJSE6TQ95HHCESQXDEGTT: copper-grate
  h_01HHHQJSE6Z7K4TS8QN5N81K7R: breeze
  h_01HHHQJSE64HRE36N7BNFBFR2R: commands
  h_01HHHQJSE6584KJ7ZGPDDGQWTH: features-and-bug-fixes
  h_01HHHQJSE6705B75P7RK1RKK05: gameplay
  h_01HHHQJSE6VP5G926ZQH666K5Y: mobs
  h_01HHHQJSE62XMK8EHXZA1MVFCT: graphical
  h_01HHHQJSE6Z2TKZ1CDV1RKTCJY: user-interface
  h_01HHHQJSE67WGY6FAD0W58KP29: updated-edit-world-screen
  h_01HHHQQRD1YQ6DHPVHA5MGDB3M: realms
  h_01HHHQQRD19GRWV7PA32C7NECR: technical-updates
  h_01HHHQQRD113M011EQHAZTGHRM: add-ons-and-script-engine
  h_01HHHQQRD1V7WXMH03HR89WS54: general
  h_01HHHQQRD1NHCNJZYSYHK28FHR: api
  h_01HHHQQRD1KAVRE9N1VMRYKYR5: components
  h_01HHHQQRD1Y9DN7XGKN1F3P8CD: editor
  h_01HHHQQRD161CKVVGGXEYGKJKE: molang
  h_01HHHQQRD1SDQYG6W2GDAFBVGQ: experimental-technical-features
  h_01HHHQQRD13Z0JWXW60WZNP9GQ: add-ons-and-script-engine-1
  h_01HHHQQRD2PSM7MAFSVPBC0VC9: api-1
  h_01HHHQQRD243258SQBMYPDTYRX: molang-1
  h_01HHHQQRD2QQSA1EK1E533NKMM: graphical-1
---

**发布于:** 2023年12月13日

## **Minecraft预览与测试版信息:**

- 这些开发中的版本可能不稳定，且可能不代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上获取。加入或退出测试版的详细说明，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 

![r20u6_4.jpg](https://feedback.minecraft.net/hc/article_attachments/22309433054349)

我喜欢在Minecraft中冒险。探索生物群系！开采东西！我觉得我的宠物狼也会喜欢，但作为一个过度保护的数字狗家长，我一直不愿让它们离开基地。直到今天！因为不仅犰狳即将出现在Minecraft基岩版预览和测试版的预发布版本中（看看它可爱的卷缩动画！），狼铠甲也来了。认识一下谨慎的犰狳，一个中立的、居住在热带草原的生物群系生物，喜欢蜘蛛眼，感到威胁时会卷缩。犰狳还会掉落鳞甲，可以用来制作狼铠甲，目前给予你的四足朋友的保护力大约与钻石马铠相当。既时尚又更安全！一如既往，我们希望收到您关于犰狳和狼铠甲的反馈，请在[这里](https://aka.ms/MinecraftArmadilloFeedback)告诉我们您的想法，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告任何漏洞（蜘蛛眼除外）。现在，如果您能原谅我，我和我的毛茸茸的朋友要去测试我对一堆可爱像素的担忧程度了！

# 实验性功能

## 犰狳

- 添加了犰狳
- 犰狳是中立的生物群系生物
- 定期掉落犰狳鳞甲
- 被刷子刷过时掉落犰狳鳞甲
- 在热带草原生成
- 喜爱的食物是蜘蛛眼
- 当犰狳检测到威胁时，会卷缩
  - 威胁包括：
    - 疾跑的玩家
    - 有座骑或在载具中的玩家
    - 不死生物
  - 如果犰狳正在逃跑、在水中、在空中或被牵引时不会卷缩
  - 当犰狳卷缩时，它不会行走，无法进食，也不会被食物诱惑
  - 它会继续扫描威胁，如果连续3秒未检测到威胁，则会展开

## 犰狳鳞甲

- 可用于制作狼铠甲
- 犰狳掉落
- 发射器可用于刷犰狳鳞甲

## 狼铠甲

- 在成年驯服狼身上使用狼铠甲将装备此铠甲
  - 只有狼的主人可以给驯服的狼装备狼铠甲，因此发射器无法给狼装备狼铠甲
- 在穿戴铠甲的狼身上使用剪刀将使它掉落铠甲
  - 只有狼的主人可以从狼身上卸下狼铠甲，因此发射器无法从狼身上卸下狼铠甲
- 狼铠甲提供与钻石马铠相同的保护
- 如果狼在穿戴铠甲时死亡，它会掉落铠甲

## 方块

- 试炼密室中的暴露、风化和氧化的铜灯现在是涂蜡的 ([MCPE-176949](https://bugs.mojang.com/browse/MCPE-176949))
- 试炼刷怪笼在每场战斗中仅随机化一次战利品表，适用于所有玩家

## 铜格栅

- 修复了涂蜡铜格栅透明度的问题 ([MCPE-177171](https://bugs.mojang.com/browse/MCPE-177171))

## Breeze

- 调整了Breeze风和风弹的渲染

## 命令

- 添加了一个新命令，用于隐藏和重置HUD元素的可见性。
  - /hud hide \<hud element\>
  - /hud reset \<hud element\>

可用的HUD元素包括：

- paperdoll
- armor
- tooltips
- touch_controls
- crosshair
- hotbar
- health
- progress_bar
- hunger
- air_bubbles
- horse_health
- all

要使用此命令，请开启即将到来的创造者功能切换。

# 功能和漏洞修复

## 游戏玩法

- 修复了频繁切换维度时发生崩溃的问题 ([MCPE-166934](https://bugs.mojang.com/browse/MCPE-166934))
- 修复了在特定高度如62处执行交互时导致玩家意外受到坠落伤害的某些情况 ([MCPE-168518](https://bugs.mojang.com/browse/MCPE-168518))
- 重新引入了一个修复，即玩家有时在站在方块上建造时会意外受到坠落伤害的问题 ([MCPE-120140](https://bugs.mojang.com/browse/MCPE-120140))
- 修复了玩家在明显没有从悬崖坠落的边缘附近可能会意外受到坠落伤害的某些情况 ([MCPE-120140](https://bugs.mojang.com/browse/MCPE-120140))

## 生物

- 修复了僵尸等生物无法从地面拾取完整物品堆叠的问题

## 图形

- 为Xbox Series主机添加了4k分辨率支持

## 用户界面

- 新的Play屏幕中的好友抽屉现在允许通过加入按钮加入好友的世界。请在此处发送您对这一新功能的反馈！

## 更新的编辑世界屏幕

最新的基岩预览引入了以全新重新设计的体验编辑世界的新方法。某些功能尚不受支持，但我们希望您能提前了解我们的建设内容。更新的编辑世界体验将从今天开始逐步向玩家推出。

![edit_world_sharp.png](https://feedback.minecraft.net/hc/article_attachments/22310475920269)

更改内容：编辑世界正在更新，导航更加优化，描述更多，以及与新的创建新世界屏幕相匹配的新外观和感觉。将在未来几天逐步向Android、iOS、Windows和Xbox平台推出。我们仍在处理一些事项，例如对其他平台的支持，以及一些小的漏洞和改进。我们需要更多时间来开发这些功能，以提供最佳体验。我们希望听到您的想法！在反馈网站上分享您的反馈，并将“编辑世界”放在标题中，以便我们可以找到它。

## Realms

- 推出了Realms Stories，一个为您的Realm设计的新社交中心
  - Realms Stories的功能包括：
    - 故事动态 – 让您与您的Realm成员分享最伟大的游戏时刻
    - 时间线 – 让您查看其他成员何时在Realm上玩耍
    - 成员标签 – 显示所有Realm成员及其权限级别的列表
  - 请注意，在您第一次启动1.20.60.23版本时，Realms Stories将无法访问。要使用Realms Stories，请启动游戏，关闭游戏，然后再次启动游戏。
  - 您可以在反馈网站上找到有关此功能的更多详细信息，我们也希望您能在此分享您对该功能的看法。
  - 已知问题：
    - 故事动态在用户发布新故事后不会更新，除非退出Realms Stories并重新进入
    - 被邀请至Realm但尚未加入的用户，以及之前在Realm中但已离开的成员，会出现在成员标签中
    - 通知所有者有关故事/评论的功能不起作用
    - 作为Realm所有者点击“管理成员”按钮可能导致卡顿
    - 评论可能不会始终正常显示
    - 屏幕阅读器旁白未完成
    - Realm成员在成员标签中看不到自己

# 技术更新

## 附加包和脚本引擎

- 为“minecraft:geometry”方块组件添加了"minecraft:geometry.full_block"标识符
  - "minecraft:geometry.full_block"标识符提供了一个居中的1x1x1立方体几何体
  - 当与具有“render_layer”: "opaque"的*material_instances*组件结合使用时，它启用了之前包含在“minecraft:unit_cube”组件中的仅渲染功能，包括：
    - 阻挡原版和自定义相邻的完整方块
    - Cull面板与原版和自定义相邻的完整方块，以提高渲染性能
- 添加内容错误日志记录，帮助创作者识别每个方块的状态位/排列组合数超出的内容 ([MCPE-177045](https://bugs.mojang.com/browse/MCPE-177045))

## 通用

- 在文档中更新了原版“orientation”方块状态的列出值

## API

- 为原版元数据生成添加了生物群系注册表的生物群系名称和*StructureFeatureType*枚举

## 组件

- 为“ageable”组件添加了“interact_filters”字段，允许指定何时可以给活动对象喂食的条件

## 编辑器

编辑器及其对应的API处于早期开发阶段，并在Windows PC基岩预览版的键盘/鼠标上可用。在社交媒体上使用**#BedrockEditor**标记我们。

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)讨论论坛，与团队互动，并通过[starter kit](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[samples](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周更新：

- 选择工具中的BlockType默认方块现在为‘草’
- 脚本属性窗格在达到一定高度后将变为可滚动
- 编辑器的Playtest窗格现在支持在测试关卡时设置时间和天气，以及对布局进行了一些小调整。Playtest窗格中的时间支持Minecraft时间（0-23999）或24小时制时间（00:00-23:59）。
- 添加了新的绑定和对脚本的支持，能够将TypeScript对象作为有效负载推送到事务堆栈，并注册一组处理函数，当事务系统接收到撤销或重做事件时将接收有效负载
- 添加了导航记录系统到编辑器。查看GitHub发布说明以获取更多关于功能和功能性的信息。
- 为stringFromExtension添加了导出，以便在内部和外部创作者扩展中使用
- 向编辑器添加了新线工具。查看GitHub发布说明以获取更多关于功能和功能性的信息。
- 编辑器UI现在根据屏幕分辨率进行缩放，而不是根据游戏窗口大小
- Play/test窗格中的属性选项在游戏重新加载时保留其值。

本周，我们正式关闭了v0.4.X语义迭代，并认为我们的v0.5工作已完成。查看GitHub中的发布说明以获取所有v0.4.X迭代更新的其他详细信息和汇总。

## Molang

- 将Molang查询从实验性中发布
  - *query.is_cooldown_type*
  - *query.cooldown_time*
  - *query.cooldown_time_remaining*
  - *query.relative_block_has_any_tag*
  - *query.relative_block_has_all_tags*
  - *query.block_neighbor_has_any_tag*
  - *query.block_neighbor_has_all_tags*
  - *query.block_has_any_tag*
  - *query.block_has_all_tags*
  - *query.bone_orientation_trs*
  - *query.bone_orientation_matrix* 

# 实验性技术功能

## 附加包和脚本引擎

- “minecraft:unit_cube”方块组件已被弃用。在标记为1.20.60及以后的内容中使用它将提供内容错误
  - 在1.20.60之前标记的内容将把它们的“minecraft:unit_cube”方块组件升级为带有“minecraft:geometry.full_block”标识符的“minecraft:geometry”方块组件，但仍保持与所有行为的向后兼容性

## API

- 更新了函数 *addEffect* 以返回添加的效果（如果失败则返回未定义）。此更改在测试版中，不影响当前发布版本的此函数。
- 添加了物品动态属性
  - 添加函数 *clearDynamicProperties(): void* - 从物品堆栈中移除所有动态属性
  - 添加函数 *getDynamicProperty(identifier: string): boolean \| number \| string \| Vector3 \| undefined* - 返回具有给定标识符的动态属性的值（如果存在），否则返回未定义
  - 添加函数 *getDynamicPropertyIds(): string\[\]* - 返回物品堆栈上的所有动态属性标识符的数组
  - 添加函数 *getDynamicPropertyTotalByteCount(): number* - 返回物品堆栈上所有动态属性的总字节数
  - 添加函数 *setDynamicProperty(identifier: string, value?: boolean \| number \| string \| Vector3): void* - 设置具有给定标识符的动态属性的值。如果值为未定义，则将移除动态属性
  - 添加函数 *clearDynamicProperties(): void* - 从物品堆栈中移除所有动态属性
  - 添加函数 *getDynamicProperty(identifier: string): boolean \| number \| string \| Vector3 \| undefined* - 返回具有给定标识符的动态属性的值（如果存在），否则返回未定义
  - 添加函数 *getDynamicPropertyIds(): string\[\]* - 返回物品堆栈上的所有动态属性标识符的数组
  - 添加函数 *getDynamicPropertyTotalByteCount(): number* - 返回物品堆栈上所有动态属性的总字节数
  - 添加函数 *setDynamicProperty(identifier: string, value?: boolean \| number \| string \| Vector3): void* - 设置具有给定标识符的动态属性的值。如果值为未定义，则将移除动态属性
- 添加类 *EntityProjectileComponent*。此组件用于射出投射物实体并修改其属性
- 添加接口 *ProjectileShootOptions*。此接口与函数 *EntityProjectileComponent.shoot* 一起使用，可选择性地修改投射物发射时的准确性

## Molang

- 将冷却查询槽ID更改为必须对于具有多个索引的容器槽位，并在未提供时记录内容错误
  - *query.cooldown_time(slotName,slotId)*
  - *query.cooldown_time_remaining(slotName,slotId)*
  - *query.is_cooldown_type(cooldownName,slotName,slotId)*

## 图形

- 在延迟技术预览版中，玩家的身体现在将在第一人称模式下投射阴影。请注意，某些手持物品仍不会投射阴影
- 启用延迟技术预览后，进入支持PBR的世界时，加载屏幕将不再在Android上变黑
- 启用延迟技术预览后，矿车中的漏斗在摄像机运动期间不再出现幽灵伪影
- 启用延迟技术预览后，退出世界时游戏不再崩溃