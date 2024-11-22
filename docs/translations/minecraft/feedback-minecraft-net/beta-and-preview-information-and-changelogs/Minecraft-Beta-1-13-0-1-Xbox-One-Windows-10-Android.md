---
title: Minecraft Beta - 1.13.0.1 (Xbox One/Windows 10/Android)
date: 2019-06-27T09:22:22Z
updated: 2019-06-28T08:53:38Z
categories: Beta与预览信息和更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/360029655632-Minecraft-Beta-1-13-0-1-Xbox-One-Windows-10-Android
---

**请在参与Minecraft Beta之前阅读**：

- 加入Beta将用一个进行中的Minecraft版本替换您的游戏
- 您将无法访问Realms，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间游玩的任何世界无法在游戏的先前版本中打开，因此请复制世界以防止丢失
- Beta版本可能不稳定，且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出Beta，请参阅[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)了解详细说明

## **实验性游戏玩法：**

（仅在世界设置中启用实验性游戏玩法时可用的进行中功能）

- 新的和改进的结构方块！

## **新功能：**

- 添加了狐狸！
  - 添加了北极狐狸作为一种变种
  - 在寒冷气候中，狐狸现在会生成北极变种，北极熊会无缘无故攻击它们
  - 可信的狐狸会保护可信的玩家
  - 狐狸可以用嘴叼起和携带物品
  - 狐狸可能会吃它们携带的物品，有时会产生有趣的结果！
- 编写命令时，现在可以使用Tab键自动完成坐标
- 新增“PersistComponent”用于怪物持久性
- 添加了新的和改进的结构方块
  - 保存和加载功能位于实验性切换后面

## **更改：**

- 添加了一条消息，通知玩家Marketplace包是否与他们的Minecraft版本兼容（特别是如果它包含来自游戏新版本的方块）
- iOS版Minecraft将不再显示“您是否要关闭Minecraft”的弹出窗口，因为iOS不支持该应用行为
- 添加了新的聊天设置选项以改进辅助功能

## **针对地图制作人和附加包创建者：**

- **新的数据驱动物品**
  - 为数据驱动箭头添加了摇动动画 ([MCPE-40744](https://bugs.mojang.com/browse/MCPE-40744))
  - 数据驱动的活动对象推送逻辑和行为
  - 破坏物品粒子现在是数据驱动的
  - 实现了数据驱动的环境伤害
  - 数据驱动的烟花棒粒子
  - 数据驱动的守卫者/远古守卫者动画和渲染
    - 修复了1.8之前守卫者的未父级几何体
    - 远古守卫者尖刺动画
  - 添加了新的地物规则数据，通过json实现现有生物群系装饰
    - 支持完全数据驱动功能所需的最终基础设施更改。规则本身必须在启用实验性的行为包中提供
  - 将鱼钩活动对象转换为数据驱动
  - 将气球活动对象转换为数据驱动
  - 数据驱动的玩家渲染
  - 雪傀儡轨迹行为现在是数据驱动的
  - 马模型/动画现在是数据驱动的
  - 用户故事龙息粒子现在是数据驱动的
  - 矿团现在是数据驱动的（OreFeature）
- 为ActorDamageSource添加了脚本文档
- 为死亡事件添加了额外的脚本信息
- 添加了块容器脚本组件
- 添加了“Projectile Hit”脚本事件
- 添加了“Actor Hurt”脚本事件
- 为脚本API添加了新的活动对象标签
- 为爆炸添加了块破坏脚本事件
- 现在可以通过脚本触发活动对象定义事件
- 添加了“actor_sneak”脚本事件
- 添加了“actor attacked”脚本事件
- 拉杆现在有自己的方块状态
- 修复了从发射器射箭时显示的脚本错误
- 为数据驱动的配方添加了“build document”代码
- 玩家现在可以在游戏运行时打开和查看脚本日志
- 所有柱状块现在有自己的方块状态，而不是使用方向方块状态的一些值。这允许镜像和使用结构方块旋转

## **修复：**

- **崩溃/性能**
  - 修复了游戏过程中可能发生的几次崩溃
  - 修复了在导航游戏UI时的不一致崩溃
  - 修复了与缓存资源相关的可能偶尔发生的崩溃
  - 改善了图形渲染性能
  - 通过优化网络和资源任务，提高了世界启动时间
  - 修复了在Oculus Rift上启动游戏时可能偶尔发生的崩溃
  - 修复了在Windows 10上退出游戏时可能偶尔发生的崩溃
  - 修复了在Oculus Rift上恢复游戏时可能偶尔发生的崩溃
  - 修复了在Windows 10 Mobile上恢复游戏时可能偶尔发生的冻结问题
  - 修复了在iOS上使用全局资源包重新启动游戏时的崩溃问题
  - 修复了在探索世界模板时可能偶尔发生的崩溃
  - 修复了在Xbox上启动游戏时可能发生的崩溃
  - 修复了在Xbox上输入某些字符到告示牌时可能发生的崩溃
  - 修复了在玩灵感中心世界时可能发生的崩溃
  - 修复了在尝试创建新世界或加入多人游戏时可能偶尔发生的崩溃
  - 修复了在登录微软账户时可能偶尔发生的崩溃
  - 修复了在选择某些皮肤时可能偶尔发生的崩溃
  - 修复了使用某些Marketplace包创建新世界时可能发生的崩溃
  - 优化了草的生长块刻
  - 修复了在聊天中输入某些字符时可能发生的崩溃 ([MCPE-44419](https://bugs.mojang.com/browse/MCPE-44419))
  - 修复了在Xbox One上切换配置文件时可能发生的崩溃
  - 修复了在破坏探测铁轨下方块时可能发生的崩溃
  - 修复了当分屏玩家在函数中被执行命令目标时离开游戏可能发生的崩溃
  - 修复了当成年熊猫吃竹子时离开并重新加入世界可能发生的崩溃
  - 修复了在“野生动物：丛林”地图上3-4人分屏时玩家离开后可能发生的崩溃

<!-- -->

- **通用**
  - 信标不再播放潮涌核心环境音，而是现在播放正确的信标环境音 ([MCPE-34413](https://bugs.mojang.com/browse/MCPE-34413))
  - 调整了“如何玩”部分，具体说明应使用雕刻南瓜作为防护免受末影人的攻击
  - 调整了袭击“如何玩”部分的措辞
  - 为下拉菜单、按钮和游戏开始画面调整了辅助功能的颜色和对比
  - Xbox One上的玩家现在可以在不重新启动游戏的情况下切换用户账户
  - 修复了尝试导入由新版本制作的世界模板时的消息
  - 拴绳现在在正确的位置连接到怪物
  - 更新了“如何玩”部分中关于修复鞘翅的信息，现在描述使用幻翼膜而不是皮革来修复它们 ([MCPE-41608](https://bugs.mojang.com/browse/MCPE-41608))
  - 世界加载画面现在在加载足够数量的区块后关闭 ([MCPE-44815](https://bugs.mojang.com/browse/MCPE-44815))
    - （部分修复 [MCPE-44815](https://bugs.mojang.com/browse/MCPE-44815)，区块有时无法正确加载的问题仍在处理中）
  - 熔炉现在播放所有适用的声音，并且音调正确 ([MCPE-43915](https://bugs.mojang.com/browse/MCPE-43915))
  - 最近查看的皮肤现在在皮肤选择菜单中按正确顺序显示

<!-- -->

- **游戏玩法**
  - 如果盔甲架受到隐身效果影响，其装备现在正确渲染 ([MCPE-39779](https://bugs.mojang.com/browse/MCPE-39779))
  - TNT在点燃后不再穿过方块下降 ([MCPE-41313](https://bugs.mojang.com/browse/MCPE-41313))
  - 在点燃的红石上使用拾取方块现在给予玩家正确的方块 ([MCPE-43450](https://bugs.mojang.com/browse/MCPE-43450))
  - 如果盔甲架受到隐身效果影响，其装备现在正确渲染 ([MCPE-39779](https://bugs.mojang.com/browse/MCPE-39779))
  - 更新了石匠交易
  - 喷溅型水瓶现在再次对烈焰人和末影人怪物造成伤害 ([MCPE-42589](https://bugs.mojang.com/browse/MCPE-42589))
  - 分屏玩家加入世界后现在会在正确的安全位置生成，不再出现在虚空中
  - 箭现在会再次导致沙子和沙砾下落 ([MCPE-18257](https://bugs.mojang.com/browse/MCPE-18257))
  - 修复了摄像头的俯仰角问题，导致玩家在直视上方时后退
  - 摄像头在第三人称视角下现在会正确旋转
  - 更改了玩家手持钟的方式，现在是作为物品而不是武器持有 ([MCPE-43638](https://bugs.mojang.com/browse/MCPE-43638))
  - 玩家在创造模式下掉落或着陆时不再听到伤害声音 ([MCPE-515](https://bugs.mojang.com/browse/MCPE-515))
  - 在未开启“教育版”切换时，创造模式的物品栏中不再显示摄像头
  - 水中的玩家现在会被TNT爆炸击退
  - 从发射器发射的火焰弹现在会点燃带有TNT的矿车
  - 在花上使用骨粉现在会在其周围生成更多该类型的花，而不仅仅是蒲公英和罂粟 ([MCPE-7979](https://bugs.mojang.com/browse/MCPE-7979))
  - 潜影盒现在不能与玩家放置在同一空间 ([MCPE-39674](https://bugs.mojang.com/browse/MCPE-39674))
  - 站在熔岩炼药锅中现在对玩家造成正确的伤害 ([MCPE-39356](https://bugs.mojang.com/browse/MCPE-39356))
  - 在制图师输出槽中使用“全部放置”（Y）现在只制作尽可能多的显示结果
  - 玩家现在在与掠夺者队长战斗死亡时正确获得不祥之兆效果 (195068)
  - 当禁用怪物破坏时，怪物不再打破海龟蛋 ([MCPE-36245](https://bugs.mojang.com/browse/MCPE-36245))
  - 下降的雪现在不能替换其他方块 ([MCPE-44613](https://bugs.mojang.com/browse/MCPE-44613))
  - 制图师交易现在需要11块玻璃板，而不是10块
  - 忠诚三叉戟在弹开盾牌后现在会正确返回给玩家 ([MCPE-44225](https://bugs.mojang.com/browse/MCPE-44225))
  - 下界传送门现在在简单难度下生成僵尸猪人 ([MCPE-45934](https://bugs.mojang.com/browse/MCPE-45934))
  - 修复了激流三叉戟未能正确推动玩家前进的问题
  - 平衡了书籍上的附魔 - 拥有3个或更多附魔的书籍不再总是拥有羽落IV和/或爆炸保护IV ([MCPE-41944](https://bugs.mojang.com/browse/MCPE-41944))
  - 营火现在只能用喷溅型水瓶扑灭，以匹配Java版
  - 爆炸不再摧毁和掉落末地折跃门方块 ([MCPE-47174](https://bugs.mojang.com/browse/MCPE-47174))
  - 通过调整怪物高度生成逻辑修复了苦力怕农场 ([MCPE-45935](https://bugs.mojang.com/browse/MCPE-45935))
  - 熔岩现在正确影响与之接触的怪物 ([MCPE-45531](https://bugs.mojang.com/browse/MCPE-45531))

<!-- -->

- **世界生成**
  - 沙漠神殿中生成的箱子现在朝正确的方向 ([MCPE-37393](https://bugs.mojang.com/browse/MCPE-37393))

<!-- -->

- **怪物**
  - 铁傀儡不再被爆炸推回 ([MCPE-43662](https://bugs.mojang.com/browse/MCPE-43662))
  - 劫掠兽现在会通过水寻找路径
  - 修复了小型僵尸骑士的坐姿
  - 修复了蜘蛛的死亡动画 ([MCPE-41417](https://bugs.mojang.com/browse/MCPE-41417))
  - 懒熊猫不再在背上躺卧时漂浮在地面上 ([MCPE-43164](https://bugs.mojang.com/browse/MCPE-43164))
  - 被闪电击中的小猪变成小僵猪人 ([MCPE-38134](https://bugs.mojang.com/browse/MCPE-38134))
  - 修复了玩家睡觉时对床的对齐
  - 僵尸不再能打破铁门 ([MCPE-43725](https://bugs.mojang.com/browse/MCPE-43725))
  - 村庄怪物（如铁傀儡和猫）不再生成在方块（如草路径和耕地方块）内 ([MCPE-44442](https://bugs.mojang.com/browse/MCPE-44442), [MCPE-41886](https://bugs.mojang.com/browse/MCPE-41886))
  - 怪物现在可以正确地在含水块中寻找路径 ([MCPE-37005](https://bugs.mojang.com/browse/MCPE-37005))
  - 怪物现在可以在未点燃的营火块上正确地寻找路径
  - 怪物不再尝试在1.5块高的障碍物上寻找路径 ([MCPE-45256](https://bugs.mojang.com/browse/MCPE-45256))
  - 村民现在在夜晚来临时都会正确入睡
  - 流浪者和骷髅现在在持有附魔弓时显示附魔效果
  - 村民在被玩家击中时，现在即使尚未进行交易，也会显示生气的粒子效果 ([MCPE-29700](https://bugs.mojang.com/browse/MCPE-29700))
  - 怪物现在在站在灵魂沙上时会正确攻击玩家
  - 村民现在会关闭由玩家或红石打开的门 ([MCPE-21946](https://bugs.mojang.com/browse/MCPE-21946))
  - 村民交易等级现在与Java版的5个职业等级徽章相匹配 ([MCPE-43206](https://bugs.mojang.com/browse/MCPE-43206))
  - 修复了“吐司”兔子的复活节彩蛋 ([MCPE-44510](https://bugs.mojang.com/browse/MCPE-44510))

<!-- -->

- **方块**
  - TNT在点燃后不再穿过方块下降 ([MCPE-41313](https://bugs.mojang.com/browse/MCPE-41313))
  - 在点燃的红石上使用拾取方块现在给予玩家正确的方块 ([MCPE-43450](https://bugs.mojang.com/browse/MCPE-43450))
  - 霜冰在地下等待融化时不再导致延迟 ([MCPE-39698](https://bugs.mojang.com/browse/MCPE-39698))
  - 花岗岩、闪长岩和安山岩现在不能再烧炼成平滑石头 ([MCPE-45914](https://bugs.mojang.com/browse/MCPE-45914))
  - 砂土在顶端生长树木时不再被泥土替换 ([MCPE-26215](https://bugs.mojang.com/browse/MCPE-26215))
  - 木块在放置时现在具有方向性 ([MCPE-43367](https://bugs.mojang.com/browse/MCPE-43367))

<!-- -->

- **物品**
  - 按钮在玩家快捷栏中不再显示旋转 ([MCPE-11365](https://bugs.mojang.com/browse/MCPE-11365), [MCPE-42584](https://bugs.mojang.com/browse/MCPE-42584))
  - 盾牌的耐久度条在承受伤害时现在会正确更新 ([MCPE-44788](https://bugs.mojang.com/browse/MCPE-44788))
  - 锁定地图现在有一个独特的物品图标

<!-- -->

- **图形**
  - 活塞在任何方向放置时现在都有正确的纹理 ([MCPE-38053](https://bugs.mojang.com/browse/MCPE-38053))
  - 修复了在Android上恢复游戏后主屏幕显示黑色损坏纹理的问题 ([MCPE-39031](https://bugs.mojang.com/browse/MCPE-39031))
  - 调整了盾牌在副手中持有时的位置，以修复轻微的纹理剪辑问题
  - 隐形基岩跌落时不再发射石头粒子
  - 调整了第一人称手部攻击动画
  - 修复了从持有物切换为空手时的手部动画
  - 修复了一个问题，导致暂停和恢复游戏后方块实体（如床）无法渲染
  - 修复了在Oculus Rift上启动游戏时的一些图形错误
  - 修复了手持和投掷三叉戟时的位置问题

<!-- -->

- **用户界面**
  - 玩家坐标的背景色调现在与聊天背景一致 ([MCPE-43791](https://bugs.mojang.com/browse/MCPE-43791))
  - 调整了自动合成时控制器光标的位置，以适应满物品栏的情况
  - 使用触摸屏的玩家在使用触摸并按住钓鱼竿时不再能破坏方块

<!-- -->

- **命令**
  - 执行检测命令现在正确使用局部坐标 ([MCPE-29942](https://bugs.mojang.com/browse/MCPE-29942))
    - 修改了CommandPosition，以便可以指定可选偏移量来移动旋转点，以防使用局部坐标
    - 修复了ExecuteCommand检测选项，正确使用实体而不是位置，以便可以使用实体朝向来计算相机相对偏移

<!-- -->

- **附加包和脚本引擎**
  - 修复了为旧内容记录的MoLang脚本错误
  - 修改行为的末影人现在可以用投射物射击和造成伤害
  - 穿越区块边界的实体不再因移动而损坏
  - 修复了人形体的进食动画
  - 修复了脚本包中迷你弓仅在玩家之外的怪物上渲染的问题
  - “has_equipment”过滤器现在正确处理可损坏物品
  - 加载包含大量自定义物品的包现在能正确工作
  - 在“抽象立方体”Marketplace地图中创建新的末地折跃门传送门现在正常工作
  - 粒子UV不再包括选定UV旁边的纹理线
  - 使用“nearest_attackable_target”的自定义实体现在重新评估当前目标的有效性