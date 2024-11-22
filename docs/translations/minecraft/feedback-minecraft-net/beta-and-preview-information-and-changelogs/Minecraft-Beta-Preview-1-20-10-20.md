---
标题: Minecraft 测试版及预览版 - 1.20.10.20
日期: 2023-05-25T10:27:13Z
更新日期: 2023-05-25T15:30:42Z
分类: 测试版和预览信息及变更日志
链接: https://feedback.minecraft.net/hc/zh-cn/articles/16116960508813-Minecraft-Beta-Preview-1-20-10-20
---

**发布日期:** 2023年5月25日

**关于 Minecraft 预览版和测试版的信息:**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上获取。有关加入或退出测试版的详细说明，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![一张Minecraft截图，显示玩家在樱花树林中躲在樱花木活板门下，旁边有一个村民站在种植的花朵旁边，还有一对骆驼。](https://feedback.minecraft.net/hc/article_attachments/16116940626189)

# **功能和漏洞修复**

## **辅助功能**

- 改进了Xbox屏幕键盘的体验，包括更好的定位、使用输入更新字段以及在屏幕键盘开启时不再调暗屏幕 ([MCPE-156575](https://bugs.mojang.com/browse/MCPE-156575))

## **潜行与爬行（实验性）**

- 添加了在“短潜行与爬行”实验性切换后方爬行的能力
- 创建了新的玩家爬行动画
- 玩家在1个区块间隙时将开始爬行，类似于潜行
- 爬行速度与潜行相同
- 玩家离开1个区块间隙时将自动站立或开始潜行
- 玩家在爬行时进入水中将开始游泳，反之亦然
- 玩家模型在游泳时现在以其击中箱为中心 ([MCPE-54294](https://bugs.mojang.com/browse/MCPE-54294))
- 玩家在骑乘时不再能够潜行 ([MCPE-170613](https://bugs.mojang.com/browse/MCPE-170613))
- 玩家在潜行、游泳或滑翔时，将始终从摄像头位置生成投射物
- 玩家在正确位置进食时，如果处于潜行、游泳或滑翔状态，将生成粒子效果
- 忠诚三叉戟将始终返回到玩家的摄像头位置
- 玩家在某些情况下短潜行时不再会窒息
- 玩家在2个区块间隙骑乘骆驼时不再会窒息 ([MCPE-166451](https://bugs.mojang.com/browse/MCPE-166451))
- 玩家在被方块推动时短潜行不再会轻微被推 ( [MCPE-166411](https://bugs.mojang.com/browse/MCPE-166411))
- 修复了许多强制潜行与按住潜行按钮行为相同的交互问题 ([MCPE-170610](https://bugs.mojang.com/browse/MCPE-170610))

## **世界生成**

- 磨制玄武岩和雕纹深板岩在世界生成过程中不再会被幽匿块替换
- 磨制深板岩在世界生成过程中现在可以被幽匿块替换 ([MCPE-160238](https://bugs.mojang.com/browse/MCPE-160238))

## **村民**

- 农民村民现在会与火把花种子和瓶子草荚果互动。他们可以拾取种子并种植，但不会收获火把花或瓶子草植株 ([MCPE-169758](https://bugs.mojang.com/browse/MCPE-169758))

## **考古学**

- 至少使用一个碎片制作的饰纹陶罐现在有一个悬停提示显示碎片和红砖成分

## **音频**

- 摄像头位置现在用于音频系统监听和环境音
  - 之前有时使用玩家位置和旋转进行音频监听
  - 这有效地在使用“第三人称前”摄像头视角时翻转了音频声道

## **方块**

- 没有权限打开/关闭容器的玩家不再可以与雕纹书架互动
- 炼药锅的水纹理现在是正确的版本 ([MCPE-170427](https://bugs.mojang.com/browse/MCPE-170427))
- 灵魂土上的音符盒现在发出竖琴声音，而不是军鼓声音
- 锹不再能像镐那样快速开采泥坯 ([MCPE-161207](https://bugs.mojang.com/browse/MCPE-161207))
- 在上下左右移动时在顶雪和高草丛上放置方块不再会导致它们连续堆叠 ([MCPE-162785](https://bugs.mojang.com/browse/MCPE-162785))

## **图形**

- 修复了Switch上高亮方块和怪物阴影通过南瓜头覆盖层出现的问题
- 雪或雨的渲染现在基于摄像头位置而非玩家位置
- 盾牌在RTX上双手持有时不再闪烁
- 修复了睡眠和摄像头淡入效果在第一人称渲染发生前未覆盖屏幕的问题

## **地图**

- 修复了启用客户端区块生成时地图上生成黑色像素的问题

## **生物**

- 驼峰在冲刺时播放的声音不再重复播放 ([MCPE-164064](https://bugs.mojang.com/browse/MCPE-164064))
- 修复了跳跃提升效果不影响岩浆怪的问题 ([MCPE-54294](https://bugs.mojang.com/browse/MCPE-54294))

## **用户界面**

- 在所有平台添加了一个切换，允许GUI缩放超出GUI滑块所允许的额外大型
- 将暂停菜单的断开连接文本更改为与平台无关
- 修复了自动放置后导致物品栏被锁定的问题 ([MCPE-46795](https://bugs.mojang.com/browse/MCPE-46795))
- 导入的世界现在将其最后游玩日期修改为导入时间

## **原版趋同**

- 存储实体掉落的物品现在居中在最近的方块内 ([MCPE-160189](https://bugs.mojang.com/browse/MCPE-160189))
- 船的配方中移除了锹
  - 竹筏的配方尚未更新
- 木桶的配方已修改为使用木板而非木棍
- 蜘蛛网到线的配方已移除
- 修复了僵尸村民治愈后未掉落给予物品的漏洞 ([MCPE-163670](https://bugs.mojang.com/browse/MCPE-163670))
- 野马、骡和驴现在可以使用金苹果/胡萝卜或附魔苹果来诱惑。羊驼将被玩家手持干草捆诱惑 ([MCPE-140814](https://bugs.mojang.com/browse/MCPE-140814))

## **振动**

- 在物品展示框或荧光物品展示框中放置、旋转或移除物品现在会发出振动 ([MCPE-166741](https://bugs.mojang.com/browse/MCPE-166741))
- 充能重生锚现在会发出振动 ([MCPE-157409](https://bugs.mojang.com/browse/MCPE-157409))
- 在铜区块组的方块上刮擦或涂蜡现在会发出振动
- 将阳光探测器切换到反转阳光探测器，或反之亦然，现在会发出振动
- 向营火添加食物现在会发出振动
- 向唱片机添加或移除音乐唱片现在会发出振动
- 泥巴变成黏土现在会发出振动
- 收获甜浆果现在会发出振动
- 将末影之眼放置在末地传送门框架中现在会发出振动 ([MCPE-155372](https://bugs.mojang.com/browse/MCPE-155372))
- 蜜蜂进入或离开蜂箱或蜂巢现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 与堆肥桶互动现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 从栅栏上附加或分离拴绳现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 从生物上附加或分离拴绳现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 羊被宰杀现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 采摘发光浆果现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 耕地变成泥土现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 使用刷怪蛋在刷怪笼上现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 蠹虫与方块合并现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 在缠根泥土上使用锄现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 使用锹创建土径现在会发出振动 ([MCPE-156199](https://bugs.mojang.com/browse/MCPE-156199))
- 放置门现在会发出振动
- 在耕地上种植种子现在会发出振动

# **技术更新**

## **附加包和脚本引擎**

- 为 *part_visibility* 组件添加了弃用错误消息（应使用几何组件中的 *bone_visibility* 字段，详情见方块文档）
- 修复了在自定义实体中添加 *minecraft:peek* 组件导致游戏崩溃的问题

## **方块**

- 更新了 "minecraft:geometry" 方块组件，允许使用Molang表达式定义骨骼可见性

## **命令**

- 执行 "inputpermission set" 命令现在会在聊天中输出带有结果的消息 ([MCPE-168368](https://bugs.mojang.com/browse/MCPE-168368))
- 如果 "inputpermission set" 命令未影响任何玩家，则执行命令将导致错误
- 命令位置现在将在通过 execute 运行mcfunctions时使用当前的位置/旋转
- 修复了某些execute命令在Realms上停止工作的问题 ([MCPE-169974](https://bugs.mojang.com/browse/MCPE-169974))
- "hasitem" 目标选择器参数现在会计算用光标持有的物品 ([MCPE-152002](https://bugs.mojang.com/browse/MCPE-152002))
- 命令仍然支持 "concrete"，但在命令提示中不会建议 "concrete"，而是使用新名称
  - "concrete" 方块现在已拆分为唯一实例，具体为 "white_concrete"、"orange_concrete"、"magenta_concrete"、"light_blue_concrete"、"yellow_concrete"、"lime_concrete"、"pink_concrete"、"gray_concrete"、"light_gray_concrete"、"cyan_concrete"、"purple_concrete"、"blue_concrete"、"brown_concrete"、"green_concrete"、"red_concrete" 和 "black_concrete"
- Java趋同: 命令中的方块状态在1.20.0及更高版本中将使用等号而非冒号。例如使用 setblock 命令: /setblock ~ ~ ~ oak_log["pillar_axis"="x"] ([MCPE-168056](https://bugs.mojang.com/browse/MCPE-168056))
- 使用等号的方块状态不需要空格即可显示自动完成选项 ([MCPE-168056](https://bugs.mojang.com/browse/MCPE-168056))

## **组件**

- 当 *minecraft:balloonable* 用于 *minecraft:player* 时添加内容错误，以防止此组件以这种方式使用时出现问题 ([MCPE-164495](https://bugs.mojang.com/browse/MCPE-164495))

## **编辑器**

编辑器处于早期开发阶段，并在Windows PC Bedrock预览构建中支持键盘/鼠标。了解 [如何使用](https://aka.ms/LearnEditor) 编辑器并加入 [GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions) 论坛，发布漏洞，查看更详细的发布说明。在社交渠道上用 **#BedrockEditor** 标签我们。

- 解决了选择光标导致玻璃方块渲染为不可见的问题
- 为工具模式添加了日志面板以显示日志消息。可以从 *视图* 菜单或使用 *CTRL+H* 快捷键访问
- 修复了在编辑器模式下服务器标签中无法添加额外服务器的错误
- 修复了导致十字准星模式下工具无法显示的问题

## **物品**

- 在json格式1.20.10及更高版本中，*minecraft:cooldown* 物品组件已从实验性阶段发布
- 在json格式1.20.10及更高版本中，*minecraft:repairable* 物品组件已从实验性阶段发布

## **稳定性和性能**

- 实体组件 *"minecraft:behavior.nearest_attackable_target"* 中的无效JSON对象将不再导致游戏崩溃 ([MCPE-168129](https://bugs.mojang.com/browse/MCPE-168129))

# **实验性技术功能**

## **附加包和脚本引擎**

- 摄像头预设现在可以指定 *"listener":"player"*，以使音频系统使用玩家位置进行音频定位
  - 添加了 *"example:example_player_listener"* 摄像头预设以演示此选项

## **物品**

- 带有 "minecraft:block_placer" 组件的物品现在将以正确的方向放置方块
- 自定义物品的 *"minecraft:block_placer"* 将不再在错误的位置放置某些方块
- 将 *"minecraft:shooter"* 更改为仅在 *"charge_on_draw"* 设置为 "*true*" 时在充能物品时消耗弹药

## **API**

- 动态属性现在可以选择具有默认值
- 增加了动态属性注册限制:
  - 活动对象: ~1KB -> 128KB
  - 世界: ~10KB -> 1MB
- ScreenDisplay
  - 移除了 *clearTitle()* - 使用 *setTitle* 传递空字符串以清除标题
  - 将 *fadeInSeconds, staySeconds, fadeOutSeconds* 更新为 *fadeInDuration, stayDuration, fadeOutDuration*（秒转换为刻）在 TitleDisplayOptions 中
  - 更新 *setTitle* 以在每个新标题时重置时间
  - 为 *setTitle*、*updateSubtitle* 和 *setActionBar* 添加了 *RawMessage* 支持
- 实体添加
  - 添加了只读属性 *isGliding* - 返回玩家是否正在使用鞘翅滑翔
  - 添加了只读属性 *isJumping* - 返回玩家是否正在使用跳跃动作
  - 添加了只读属性 *isFlying* - 返回玩家是否在飞行（例如创造模式或旁观模式）
  - 添加了只读属性 *isSprinting* - 返回实体是否在疾跑
  - 添加了只读属性 *isSwimming* - 返回实体是否在游泳
  - 添加了只读属性 *isClimbing* - 返回实体是否在攀爬（例如玩家在梯子上或蜘蛛在墙上）
  - 添加了只读属性 *isOnGround* - 返回实体是否在地面上
  - 添加了只读属性 *isInWater* - 返回实体是否在水中
  - 添加了只读属性 *isFalling* - 返回实体是否在下落
  - 添加了只读属性 *fallDistance* - 返回当前下落距离（用于计算摔落伤害）
  - 添加了函数 *fly* - 使玩家飞行（例如创造模式或旁观模式）
  - 添加了函数 *stopFlying* - 使玩家停止飞行（例如创造模式或旁观模式）
  - 添加了函数 *glide* - 使玩家使用鞘翅滑翔
  - 添加了函数 *stopGliding* - 使玩家停止使用鞘翅滑翔
  - 添加了函数 *swim* - 使玩家游泳
  - 添加了函数 *stopSwimming* - 使玩家停止游泳
- 实体添加（效果）
  - 更新函数 *addEffect(effectType: EffectType | string, duration: number, options?: EntityEffectOptions): void* 以返回 void 并在效果不存在或参数超出范围时抛出错误
  - 更新函数 *getEffect(effectType: EffectType | string): Effect | undefined* 以在效果不存在时抛出错误
  - 更新函数 *removeEffect(effectType: EffectType | string): boolean* 以在效果不存在时抛出错误
- 块事件
  - 添加了事件 *'PressurePlatePushEvent'*、*'PressurePlatePopEvent'*、*'TargetBlockHitEvent'* 和 *'TripWireTripEvent'*
- 容器槽位
  - 移除了函数 *clone* - 请使用函数 *getItem* 代替
- 实体可治疗组件
  - 移除了 *filters: FilterGroup* 属性
- 实体属性组件
  - 添加了 *effectiveMin: number* - 返回组件的最小可能值
  - 添加了 *effectiveMax: number* - 返回组件的最大可能值
  - 将 *value* 属性重命名为 *defaultValue*
  - 将 *current* 属性重命名为 *currentValue*
  - 将 *setCurrent* 方法重命名为 *setCurrentValue*
- 添加了 *EntityHealthChangedAfterEvent*。当实体的任何生命值变化发生时触发

## **摄像头**

- 将摄像头命令的淡入颜色更改为使用0到255的整数值，而不是0.0到1.0的分数值
- 摄像头淡入命令现在强制执行淡入持续时间限制；淡入、保持和淡出必须在0到10秒之间
- 确保在使用 /camera 命令时摄像头俯仰角只能在-90到90度之间
- 修复了Minecraft教育版玩家无法使用 "/give" 命令给予摄像头物品的问题

## **物品**

- 在格式版本1.20.10及以上具有 *”minecraft:throwable”* 组件的物品在被投掷时将触发物品使用事件
- 带有 *"minecraft:block_placer"* 的自定义物品将不再在错误的位置放置某些方块
- 将 *"minecraft:shooter"* 更改为仅在 *"charge_on_draw"* 设置为 "*true*" 时在充能物品时消耗弹药