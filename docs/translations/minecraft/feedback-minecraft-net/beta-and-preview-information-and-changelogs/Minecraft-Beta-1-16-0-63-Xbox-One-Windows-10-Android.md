---
title: Minecraft Beta - 1.16.0.63（Xbox One/Windows 10/Android）
date: 2020-05-20T14:39:41Z
updated: 2020-05-21T09:38:32Z
categories: Beta与预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/360043896251-Minecraft-Beta-1-16-0-63-Xbox-One-Windows-10-Android
---

**参与Minecraft Beta测试前请阅读：**

- 加入Beta测试将用Minecraft的开发中版本替换您的游戏
- 在预览Beta期间，您将无法访问Realms，也无法加入非Beta玩家的游戏
- 在Beta测试期间创建的世界无法在游戏的旧版本中打开，请备份您的世界以防丢失
- Beta版本可能不稳定，且无法代表最终版本的质量
- Beta测试仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta测试，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 了解详细说明

 

**崩溃与稳定性**

- 修复了在游戏过程中可能发生的多个崩溃问题
- 修复了在生存模式中通过配方书自动合成64个蜂蜜块时发生的崩溃问题 [MCPE-68604](https://bugs.mojang.com/browse/MCPE-68604)
- 修复了玩家装备任何下界合金盔甲后，使用clear命令清除盔甲，再装备相同类型的下界合金盔甲时可能发生的问题
- 修复了当生物状态变化时可能发生的崩溃问题
- 修复了navigation.walk在应用于飞行动物时的情况，以防飞行动物在接触地面时导致延迟

**通用**

- 更新了Mojang Studios的加载界面
- 下界生物群系的分布现在更符合Minecraft: Java Edition中的分布
- 修复了Xbox One玩家在访问Marketplace时可能出现的错误问题
- 提高了加载角色的可靠性 [MCPE-55968](https://bugs.mojang.com/browse/MCPE-55968)
- 修复了离线时角色可能丢失的情况
- 修复了在重新连接后阻止离线解锁成就的问题
- 修复了第三人称使用钓鱼竿时玩家手部动画不正确的问题 [MCPE-63088](https://bugs.mojang.com/browse/MCPE-63088)
- 修复了取消同步弹出框后Xbox主菜单永久卡住的问题 [MCPE-53266](https://bugs.mojang.com/browse/MCPE-53266)
- 分屏游戏中的第二位玩家在被注视时现在会正确动画
- 挂起和恢复游戏将不再使玩家模型消失 [MCPE-63119](https://bugs.mojang.com/browse/MCPE-63119)
- 分屏游戏中，当第一位玩家注视第二位玩家时，第二位玩家的手不会再消失 [MCPE-58806](https://bugs.mojang.com/browse/MCPE-58806)
- 下界砖块纹理已更新
- 刻花下界砖和石英砖的纹理已更新
- 绯红木活板门现在称为绯红木活板门
- 诡异森林相较于其他下界生物群系现在更加罕见
- 当玩家进入诡异森林时，之前的音乐曲目现在会播放到结束
- 基岩鸣谢页面已更新
- 修复了当服务器级别启用实验性模式时，客户端未启用的问题
- 优化了声音加载 - sound_definitions.json中的"load_on_low_memory"现已弃用，因为所有音频现在可以在低内存设备上播放
- 修复了世界转换问题，导致某些区块中的物品错误转换为基岩

**游戏玩法**

- 着色潜影盒不再导致物品消失 [MCPE-64164](https://bugs.mojang.com/browse/MCPE-64164)
- 修正了在压力板上设置的错误生成位置 [MCPE-65487](https://bugs.mojang.com/browse/MCPE-65487)
- 修复了将箭、烟花或鹦鹉螺壳放入副手时会破坏副手UI槽位的问题 [MCPE-64227](https://bugs.mojang.com/browse/MCPE-64227)
- 修复了熔岩会掉落未煮熟食物的问题 [MCPE-74767](https://bugs.mojang.com/browse/MCPE-74767)
- 如果Respawn Anchor生成点被阻挡，增加了回退至世界生成点的功能
- "您的家床缺失或被阻挡"的消息再次显示
- "Respawn点已设置"的消息现在在所有情况下都会显示在Respawn Anchor上 [MCPE-73159](https://bugs.mojang.com/browse/MCPE-73159)
- Respawn Anchor可以在未设置Respawn点且不在下界爆炸的情况下充能 [MCPE-69044](https://bugs.mojang.com/browse/MCPE-69044)
- 如果Respawn Anchor未充能，现在可以放置方块
- 村民现在会收割作物，无论他们的物品栏中有多少作物 [MCPE-67694](https://bugs.mojang.com/browse/MCPE-67694)
- XP经验球再次会随机方向飞射 [MCPE-58715](https://bugs.mojang.com/browse/MCPE-58715)
- 如果床旁或床上方没有足够的空间供玩家站立，玩家现在无法使用床睡觉 [MCPE-42881](https://bugs.mojang.com/browse/MCPE-42881)
- 现在无法与正在欣赏黄金物品的猪灵互动 [MCPE-69861](https://bugs.mojang.com/browse/MCPE-69861)
- Respawn Anchor不会再在水下引爆时破坏方块
- Respawn Anchor耗尽时现在会播放适当的声音 [MCPE-69265](https://bugs.mojang.com/browse/MCPE-69265)
- Lodestone Compass现在在命令中被支持 [MCPE-68994](https://bugs.mojang.com/browse/MCPE-68994)
- 屏障方块不再在堡垒遗迹中生成
- 堡垒遗迹中的箱子现在总是生成带有战利品 [MCPE-69003](https://bugs.mojang.com/browse/MCPE-69003)
- 生物不会再消耗在同一地点掉落的相同材料的两把剑
- 修复了锻造台使用时声音不播放的问题 [MCPE-69066](https://bugs.mojang.com/browse/MCPE-69066)
- Respawn Anchor充能时的声音不再在玄武岩三角洲生物群系中播放 [MCPE-69189](https://bugs.mojang.com/browse/MCPE-69189)
- Lodestone和指南针现在会播放适当的声音
- 缠怨藤块现在称为缠怨藤
- '哦，闪亮的！'成就现在会在用金锭右键分散猪灵注意时解锁
- 缠怨藤和垂泪藤在被淹没时立即被破坏，并作为物品弹出
- 挖掘下界苗不再产生无法使用的无效物品 [MCPE-74339](https://bugs.mojang.com/browse/MCPE-74339)
- 当关闭Fire ticking时，火现在会在灵魂沙和灵魂土上正确转换为灵魂火 [MCPE-69823](https://bugs.mojang.com/browse/MCPE-69823)
- 现在可以使用下界合金锹熄灭营火 [MCPE-65730](https://bugs.mojang.com/browse/MCPE-65730)
- 使用石切机中的石英块现在会生成石英台阶而非平滑石英台阶 [MCPE-57925](https://bugs.mojang.com/browse/MCPE-57925)
- 发射器现在在填充Respawn Anchor时使用1个荧石 [MCPE-72686](https://bugs.mojang.com/browse/MCPE-72686)
- 精准采集附魔现在可用于Respawn Anchor
- 精准采集附魔和setBlock命令现在可用于绯红木按钮、诡异木按钮、绯红菌核、去皮绯红菌核、诡异菌核、去皮诡异菌核、垂泪藤、缠怨藤、黑石压力板、磨制黑石按钮
- 键链现在可以被活塞推动而不破裂
- 灵魂火把现在也可以用木炭合成 [MCPE-70585](https://bugs.mojang.com/browse/MCPE-70585)
- 诡异菌钓竿现在可以像胡萝卜钓竿一样附魔 [MCPE-70948](https://bugs.mojang.com/browse/MCPE-70948)
- 炽足兽现在会受到坠落伤害 [MCPE-70886](https://bugs.mojang.com/browse/MCPE-70886)
- 成年炽足兽上坐着的小炽足兽现在在其父母在陆地上时会冻结 [MCPE-71413](https://bugs.mojang.com/browse/MCPE-71413)
- 炽足兽的移动速度已调整，更接近Minecraft Java Edition
- 下界合金物品因耐火性不再会被点燃
- 大玄武岩石柱现在不能高于10个方块
- 玄武岩三角洲现在在生物群系中生成正确的方块
- 黑石按钮、压力板、台阶和墙现在在地图上有正确的外观
- Respawn Anchor现在只能用钻石或下界合金镐挖掘 [MCPE-72102](https://bugs.mojang.com/browse/MCPE-72102)
- 生物现在更倾向于石剑而非金剑（猪灵除外！）
- 缠怨藤和垂泪藤破坏时现在会发出正确的声音
- 锁链在放置时现在会发出正确的声音
- Lodestone现在需要镐来挖掘
- 许多门的纹理已更新
- 诡异菌柄和绯红菌柄现在与橡木原木有相同的挖掘时间
- 诡异木板或绯红木板台阶现在在某些物品的配方中不再作为默认项出现
- 玩家在重新启动世界时掉落时不会再在方块上生成
- 修复了可能导致玩家在水下重生的问题
- 下界合金锹现在可以用来熄灭营火 [MCPE-65730](https://bugs.mojang.com/browse/MCPE-65730)
- 现在可以更快地用锹挖掘灵魂土 [MCPE-65382](https://bugs.mojang.com/browse/MCPE-65382)
- 绯红菌核和诡异菌核（包括去皮的）现在可以在基岩版中合成成木板 [MCPE-73099](https://bugs.mojang.com/browse/MCPE-73099)
- 现在可以使用骨粉和发射器种植垂泪藤 [MCPE-65660](https://bugs.mojang.com/browse/MCPE-65660)

**生物**

- 修复了板块上的鸡不会受到熔岩伤害的问题 [MCPE-74990](https://bugs.mojang.com/browse/MCPE-74990)
- 疣猪兽在逃离诡异菌后现在总是会被平息
- 生物现在可以在灵魂沙块上导航
- 猪灵现在可以跑得比疣猪兽更快
- 疣猪兽对使用弩的猪灵的反击频率降低
- 村民不会再掉落它们拾取的物品
- 在僵尸疣猪兽上使用Pickblock现在会给予僵尸疣猪兽刷怪蛋
- 下界合金头盔现在在猪灵身上正确渲染
- 疣猪兽和僵尸疣猪兽现在更能抵抗击退
- 猪灵在逃离灵魂火把、灵魂火灯和灵魂火时现在会发出撤退的声音
- 猪灵和疣猪兽在逃离时的行为已得到改善
- 僵尸疣猪兽和僵尸猪灵现在不会在熔岩中淹死
- 更改许多生物在熔岩中溺水时的行为
- 加剧的猪灵不再进行交易
- 金锭现在在猪灵交易时总是正确渲染在猪灵手中
- 生物不再消费它们捡起的物品 [MCPE-71542](https://bugs.mojang.com/browse/MCPE-71542)
- 当陷阱箱被破坏时，猪灵会变得愤怒
- 疣猪兽不再逃离僵尸疣猪兽
- 僵尸猪灵的纹理已更新
- 可以装备头盔盔甲的生物现在也可以装备海龟壳
- 修复了驯服的宠物在转移到下界或从下界转移时偶尔会消失的问题 [MCPE-66978](https://bugs.mojang.com/browse/MCPE-66978)
- 愤怒的蜜蜂现在更慢 [MCPE-53689](https://bugs.mojang.com/browse/MCPE-53689)

**方块**

- 铁栏杆和玻璃板现在连接到墙上 [MCPE-73989](https://bugs.mojang.com/browse/MCPE-73989)
- 菌核方块现在可以合成成各自的木板 [MCPE-73099](https://bugs.mojang.com/browse/MCPE-73099)
- 移动物块现在有正确的碰撞箱  [MCPE-62419](https://bugs.mojang.com/browse/MCPE-62419)

**图形**

- 修复了低光发光方块物品与放置方块亮度不匹配的问题
- 修复了生物生成器中的生物不显示的问题 [MCPE-56879](https://bugs.mojang.com/browse/MCPE-56879)
- 物品展示框中的地图不再有穿透的线条 [MCPE-46154](https://bugs.mojang.com/browse/MCPE-46154)
- 修复了重新加载世界后地图缺失纹理的问题 [MCPE-54228](https://bugs.mojang.com/browse/MCPE-54228)
- 修复了通过传送门返回主世界时光照没有刷新的问题 [MCPE-69037](https://bugs.mojang.com/browse/MCPE-69037)
- 修复了由于手部和摄像机同时播放动画导致过度手部晃动的问题 [MCPE-54072](https://bugs.mojang.com/browse/MCPE-54072)
- 生物持有的物品现在应正确渲染
- Lodestone Compass现在在物品栏中正确渲染

**用户界面**

- 调整了服务器标签的导航
- 创造模式的配方书再次显示物品分组
- 为标题和副标题文本添加了一个具有可调不透明度的背景，不透明度可在设置菜单中的“辅助功能”标签中更改
- 为/ title命令中使用的动作栏文本添加了背景。相同的背景也应用于快捷栏上方的物品文本
- 锻造台用户界面已更新

**命令**

- 修复了一个错误，导致蜜蜂和其他新生物在/summon命令中缺少非"minecraft:"版本。您现在应该能够在不使用前缀的情况下召唤原版生物了！ [MCPE-58557](https://bugs.mojang.com/browse/MCPE-58557)
- 为/replaceitem添加了新的重载选项，包括destroy（旧行为）或keep（如果槽位被物品占用，命令将返回错误）
- 修复了clear命令无法清除损坏工具的问题
- 如果尝试使用非默认状态设置新方块，/setblock命令失败 [MCPE-65395](https://bugs.mojang.com/browse/MCPE-65395)
- /setblock命令现在适用于更多的方块状态

**附加包和脚本**

- 修复了“救援任务熔岩小镇”Marketplace附加包中的箱子在被攻击时不移动的击退问题
- 为动画添加了新的循环模式：现在，您可以设置"loop": "hold_on_last_frame"来在动画完成时保持应用最后一帧，而不是省略"loop"让动画在完成后停止，或设置"loop": true让动画在完成后循环
- 如果Range json节点被定义为只有一个值的数组，现在会显示内容错误
- 如果使用超过一个Move Control组件、Jump Control组件或Navigation组件，现在会显示内容错误
- 含有无效和有效命令的函数在命令版本1.15及以下情况下只会执行有效命令。在这些情况下，函数名称不会出现在自动建议列表中，但仍可通过输入来执行
- 从1.16开始，包含任何无效命令（例如错误选择器语法）的函数将不再注册并无法调用
- 设置json变量"attack_interval_min"和"attack_interval_max"时，如果max小于min，组件现在会正确抛出内容错误 [MCPE-63542](https://bugs.mojang.com/browse/MCPE-63542)
- 修复了声音有时会应用错误设置，导致2D声音播放为3D声音，反之亦然的问题
- 修复了错误地截断正在播放的声音的问题，尽管如果加载占用大量内存的音频，仍然可能会发生
- JSON数组中的注释不再导致错误 [MCPE-40873](https://bugs.mojang.com/browse/MCPE-40873)