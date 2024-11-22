---
title: Minecraft Beta & 预览 - 1.20.60.20
date: 2023-11-15T13:32:02Z
updated: 2023-11-15T14:01:43Z
categories: Beta 和 预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/21354522496525-Minecraft-Beta-Preview-1-20-60-20
hash:
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: 关于Minecraft预览和Beta的信息
  h_01HF9MJ4D5YFF3YRSZWW1APM8J: 实验性特性
  h_01HF9MJ4D5BVJPB5YM3R62GHVQ: 新增旋风人
  h_01HF9MJ4D59P55V7MCYWH2G560: 已知的趋同问题
  h_01HF9MJ4D5EV6H641ZJQ1M9HJ7: 试炼刷怪笼
  h_01HF9MJ4D5DDVK0G0TMJBKFBZN: 试炼密室
  h_01HF9MJ4D6YW6MSA7803B2222S: 已知问题
  h_01HF9MJ4D6RC7F221RS2A1V8FP: 试炼钥匙
  h_01HF9MJ4D6C480T18CDMYMMBN2: 合成器
  h_01HF9MJ4D6XBF7ZSWC6ZXGK4DN: 凝灰岩砖
  h_01HF9MJ4D6Q49D2JVGK6ZA0BD4: 特性和漏洞修复
  h_01HF9MJ4D6WB1QA47T1S93K2BP: 船
  h_01HF9MJ4D6F6TXJJKX5SFKM9ED: 游戏玩法
  h_01HF9MJ4D61FBN4Z2VSFG863H0: 一般
  h_01HF9MJ4D6RDG67YJPHAQZ3DN9: 角色创建器
  h_01HF9MJ4D6T4JSHA522M3PSKF4: 如何玩部分
  h_01HF9MJ4D65QEAA96ZQMZPC4ZH: 物品
  h_01HF9MJ4D626X577N3MWS93QCB: 领域
  h_01HF9MJ4D6792WHM0F4PWJ7HBX: 用户界面
  h_01HF9MJ4D66FZSXJ1EH77B4Z40: 技术更新
  h_01HF9MJ4D6SKC1SGRY5ZS9VTT7: API
  h_01HF9MJ4D6Z02QCKVE9ZCF4BP7: 编辑器
  h_01HF9MJ4D6E87GPSGBTP9PSPGD: 实体组件
  h_01HF9MJ4D6E3JNGDC40KVRHMHD: 物品-1
  h_01HF9MJ4D6J21MQ39THNYX068V: 战利品表
  h_01HF9MJ4D61TTYN4E5WP0ZJH62: 实验性技术特性
  h_01HF9MJ4D64BH36X3MYH4MNEC3: 图形
  h_01HF9MJ4D6HE3EM96X5HREN2SX: API-1
---

**发布时间:** 2023年11月15日

## **关于Minecraft预览和Beta的信息：**

- 这些进行中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一个黑暗的试炼密室，周围有旋风人和骷髅在试炼刷怪笼附近](https://feedback.minecraft.net/hc/article_attachments/21355297216269)

试炼密室、试炼刷怪笼和旋风人有什么共同点？它们都是1.21更新的特性，并且它们今天将进入Minecraft：基岩版Beta和预览的测试！作为一个混乱的爱好者和热衷于探索未知的冒险者，我迫不及待想要*跃入*这个预览，看看谁能跳得更远，我（不允许使用鞘翅）还是旋风人：一个用风的力量攻击的顽皮敌对生物！在充满铜灯泡的走廊中探险，穿过通往未知的门，挑战自己（双关语！）与试炼刷怪笼对抗，这是一种根据你队伍的规模喷出多种生物的狡猾装置。和往常一样，我们希望您对这些特性提供反馈，请在[这里](https://aka.ms/Minecraft121Feedback)告诉我们您的想法，并在[bugs.mojang.com](https://bugs.mojang.com/)报告任何漏洞！

# 实验性特性

## 新增旋风人

- 旋风人是一种狡猾的敌对生物，可以通过试炼刷怪笼在试炼密室中的某些房间生成
- 旋风人主要通过围绕目标跳跃移动，有时跳跃的距离相当长
- 作为一个攻击性对手，旋风人向目标发射以风能为基础的风弹
- 风弹在直接碰撞实体时造成少量伤害
- 碰撞实体或方块后，风弹会产生风爆，击退区域内的实体数个区块
- 风爆还会对某些方块产生“激活”效果：
  - 非铁门和活板门被翻转
  - 栅栏门被翻转
  - 按钮被按下
  - 拉杆被翻转
  - 钟被敲响和摆动
  - 点燃的蜡烛（无论是单独的还是在蛋糕上）被熄灭
- 风爆对铁门、铁活板门或任何被红石信号固定的方块没有任何效果

## 已知的趋同问题

- 旋风人在战斗中没有非跳跃的移动
- 旋风人不会偏转飞行物
- 旋风人不会避开活板门

## 试炼刷怪笼

- 试炼刷怪笼是一种新的变种刷怪笼，在完成后会喷出奖励，并且在多人游戏中具有可变的挑战等级
- 每当试炼刷怪笼注意到附近的新玩家时，挑战等级将增加
  - 挑战等级在试炼刷怪笼的冷却期间不会降低
- 与普通刷怪笼不同，试炼刷怪笼会根据当前的挑战等级生成有限数量的生物
  - 它只能在视线范围内的位子生成生物
  - 它可以在不满足生物任何光照要求的情况下生成生物
  - 生成的生物是持久的
- 一旦所有生物被击败，试炼刷怪笼将喷出与当前挑战等级成比例的奖励
  - 在奖励喷出后，试炼刷怪笼将进入30分钟的冷却期，此期间将不再生成生物
- 试炼刷怪笼无法被玩家在生存模式中合成或获得 - 相反，它们可以在试炼密室中自然生成
- 试炼刷怪笼非常难以开采，并且对爆炸有抵抗力，即使使用精准采集也不会掉落
- 在创造模式中放置时，试炼刷怪笼默认没有生物类型
  - 生物类型可以通过在持有刷怪蛋时与其交互来设置
- 创造模式和旁观模式的玩家无法被试炼刷怪笼检测到或注意到

## 试炼密室

- 试炼密室是主世界中的一种新结构，玩家可以在其中探索并在中期进行战斗挑战
  - 试炼密室由多种铜和凝灰岩方块构成，大小不一，从大到小都有
  - 试炼密室在地下的深板岩层中相对常见
- 每个试炼密室的布局是程序生成的，可能包括陷阱、奖励箱和多种战斗空间
  - 在不同房间之间可以找到补给箱，提供帮助你应对试炼的方块和物品
  - 每个房间的奖励箱由挑战守卫，并且可以是附魔书和装备的来源
  - 奖励箱中的战利品仍在迭代中，绝对不是最终版本
- 每个试炼密室将包括具有近战、小型近战或远程类别的试炼刷怪笼：
  - 近战
    - 僵尸
    - 尸壳
    - 史莱姆
  - 小型近战
    - 蜘蛛
    - 洞穴蜘蛛
    - 小僵尸
    - 蠹虫
  - 远程
    - 骷髅
    - 流浪者
- 每个试炼刷怪笼类别在生成时只会使用一种生物，且这些生物在每个试炼密室中是随机的
  - 例如，一个试炼密室可能只生成僵尸、洞穴蜘蛛和流浪者，而另一个可能只生成史莱姆、蠹虫和骷髅
  - 例外的是一些独特房间中的试炼刷怪笼，它们总是生成旋风人

## 已知问题

- 走廊有时会以死胡同结束
- 含水层、繁茂洞穴和幽匿脉络有时会与试炼密室相交
- 战利品表可能包含错误的物品或错误数量的物品

## 试炼钥匙

- 一种只能从试炼刷怪笼获得的物品
- 试炼钥匙目前没有任何功能

## 合成器

- 更新了合成器的纹理

## 凝灰岩砖

- 更新了凝灰岩砖的纹理

# 特性和漏洞修复

## 船

- 修复了船在放置时穿透方块的问题

## 游戏玩法

- 被红石触发的容器方块（例如漏斗、发射器）现在可以在由快速红石时钟供电时一致地进行交互
- 修复了在移动时构建方块时可能在某些情况下造成意外跌落伤害的问题（[MCPE-120140](https://bugs.mojang.com/browse/MCPE-120140)， [MCPE-175791](https://bugs.mojang.com/browse/MCPE-175791)）
- 玩家在切换到旁观模式再切换回来时不再掉落到他们站立的方块下（[MCPE-170522](https://bugs.mojang.com/browse/MCPE-170522)）

## 一般

- 在世界导出因外部操作系统问题失败时，添加了更具信息性的错误消息（[MCPE-41898](https://bugs.mojang.com/browse/MCPE-41898)）
- 改善了控制台平台上100%加载与主菜单出现之间的延迟

## 角色创建器

- 在横向分屏中，第二个玩家现在可以导航到个人资料屏幕，并且两个玩家现在可以看到彼此的角色更改

## ‘如何玩’部分

- 更新了“如何玩”部分中关于潮涌核心的信息（[MCPE-65038](https://bugs.mojang.com/browse/MCPE-65038)）
- 在百科全书信标标签中新增了下界合金作为方块类型（[MCPE-175929](https://bugs.mojang.com/browse/MCPE-175929)）

## 物品

- 修复了吃苹果时不会减缓玩家移动速度的问题（[MCPE-176556](https://bugs.mojang.com/browse/MCPE-176556)）

## 领域

- 在预览中将领域的最大渲染距离增加到20个区块。我们将收集数据和反馈，以确定我们可以为正常领域带来什么渲染距离的增加。请在反馈Discord服务器或[反馈网站](https://feedback.minecraft.net/hc/en-us/community/posts/21353469341581)上与我们分享您的反馈。
- 在游戏界面和槽位界面上的Feed按钮上添加未读帖子计数指示器

## 用户界面

- 修复了某些聊天消息在新死亡屏幕上短暂错误显示的漏洞

# 技术更新

## API

- 将*ItemReleaseUseAfterEvent*中的*itemStack*更改为可选
- 将DataDrivenEntityTriggerAfterEvent从*beta*发布到*1.8.0*
- 将DataDrivenEntityTriggerAfterEventSignal从*beta*发布到*1.8.0*
- 将DataDrivenEntityTriggerAfterEventSignalOptions从*beta*发布到*1.8.0*
- 将DefinitionModifier从*beta*发布到*1.8.0*
- 将WorldAfterEvents.dataDrivenEntityTriggerEvent从*beta*发布到*1.8.0*
- 改进了“不支持或超出范围的值”错误的错误消息，以包含边界

## 编辑器

编辑器及其对应的API处于早期开发阶段，并可在Windows PC基岩预览构建中通过键盘/鼠标使用。在社交媒体上标记我们，使用**\#BedrockEditor。**

了解[**如何使用**](https://aka.ms/LearnEditor)编辑器，加入[**GitHub讨论**](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队互动，并通过[**入门工具包**](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[**示例**](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周更新：

- 修复了由CTRL+TAB快捷键引起的编辑器屏幕冻结漏洞。
- 新API！现在可以通过编辑器全局对象的simulation属性在编辑器脚本中使用模拟暂停状态。
- 菜单项现在具有checked属性，类型为boolean | undefined。如果值被定义，当值为true时菜单将显示一个勾选标记。
- 在编辑器模式下运行时，向`/reload`斜杠命令添加了一个`all`可选参数，以启用整个编辑器的完全热重载。

## 实体组件

- 实体事件响应run_command已重命名为queue_command，并已从实验性发布。通过queue_command运行的命令可能会推迟到下一个刻。如果在命令运行之前实体被移除，则该命令将不会执行。使用run_command的内容在实验性下仍然有效，但该实验性特性现在被视为过时

## 物品

- 在格式版本1.20.60及更高版本中，组件物品JSON中的未识别字段将向内容日志发出警告

## 战利品表

- 饰纹陶罐现在支持使用战利品表

# 实验性技术特性

## 图形

- 通过修复导致在延迟技术预览中每帧不断重新分配的GPU资源分配漏洞来改善性能

## API

- PlayerPlaceBlockBeforeEvent
  - 从事件中移除*itemStack: ItemStack*
  - 向事件中添加*readonly permutationBeingPlaced: BlockPermutation*
  - 更新*createExplosion(location: Vector3, radius: number, explosionOptions?: ExplosionOptions)*以返回布尔值。如果爆炸成功则为true，如果爆炸失败或被取消则为false。
- 类 Player
- 添加方法*spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void;*。
