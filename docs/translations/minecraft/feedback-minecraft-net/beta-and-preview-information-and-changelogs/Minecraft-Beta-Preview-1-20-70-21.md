---
标题: Minecraft Beta & 预览 - 1.20.70.21
日期: 2024-01-31T17:10:20Z
更新: 2024-02-05T09:32:43Z
类别: Beta 和预览信息及更新日志
链接: https://feedback.minecraft.net/hc/en-us/articles/23693972754957-Minecraft-Beta-Preview-1-20-70-21
哈希:
  h_01HNG7NYQBZ0YBS3K63A5FSGFH: 关于Minecraft预览和Beta的信息
  h_01HNG81NVW9R87QKR59K2XD2QT: 实验性特性
  h_01HNG81NVX0ENFC0DES9PA8SSD: 宝库
  h_01HNG81NVX9FFFNRTRZGSKWPS9: 犰狳
  h_01HNG81NVXSXWFSKW6SPBPW10V: 旋风人
  h_01HNG81NVX3H7CWCVN30DBGRQV: 特性和漏洞修复
  h_01HNG81NVXDA3MTS9GJM8JKDSP: 命令
  h_01HNG81NVX63EYC9PC16F3JNZQ: 物品
  h_01HNG81NVXSKZ51CJ4QYXCHHKG: 市场
  h_01HNG81NVX100280Q8QMD0JP9X: 生物
  h_01HNG81NVX6F1JWDGBBZHTZBGA: 领域
  h_01HNG81NVXH8CWE2VYYJ1CBQKK: 技术更新
  h_01HNG81NVXZ77198QWE3JDQ5EC: 方块
  h_01HNG81NVXV1EVQCQ3JM101RPG: 组件
  h_01HNG81NVX3VTWDAZN0SJRFTWB: 编辑器
  h_01HNG81NVXSVBQDXC3KYGEHYWR: 实体过滤器
  h_01HNG81NVXVHCGRWCZ2VADTGGJ: 物品-1
  h_01HNG81NVX82VJ9Q29A4H0SACV: molang
  h_01HNG81NVXFB16VFR51QH4ERJJ: 稳定性和性能
  h_01HNG81NVXH80JP3QA0TS46E68: 实验性技术更新
  h_01HNG81NVX6JDQ9NDSM42A0F98: api
  h_01HNG81NVX6AA0FKS7GR1HBEEP: 维度
  h_01HNG81NVXM2HTN0FW63ZZR0FZ: 图形

**发布:** 2024年1月31日

## **关于Minecraft预览和Beta的信息:**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一幅Minecraft试炼密室的场景。前面有一个宝库方块，旁边有一个试炼钥匙。背景中有两个旋风人生物。](https://feedback.minecraft.net/hc/article_attachments/23693972746253)

在本周的基岩预览和Beta中，我们带来了三件我*特别*兴奋的事情。怀恨在心的犰狳！（现在它们会*记住*谁打过它们，并将该玩家视为威胁。）旋风人与铁傀儡的战斗！（我们都在期待的那一场）最后是一个全新的方块：宝库！对于喜欢多人游戏的玩家来说，宝库尤其令人兴奋，因为它让你们团队中的每个人都能获得更多的奖励——字面意义上。这是因为宝库（与箱子不同）可以被多个玩家解锁和掠夺（尽管*每个玩家只能一次*）。所以再也不用为空箱子哭泣了！现在你只需要在不小心打到犰狳时哭泣——因为它们会记住。整整10秒钟！

以下是新内容列表。和往常一样，我们很乐意听取您的反馈，所以请在[这里](https://aka.ms/mcvaultsfeedback)告诉我们您的想法，并在[bugs.mojang.com](https://bugs.mojang.com/)报告您可能遇到的任何漏洞。

# 实验性特性

## 宝库

- 一个存放锁定宝藏和战利品的方块 - 找到正确的钥匙以获取其奖励
  - 在试炼密室中发现，包含该结构最有价值的战利品
  - 试炼密室中的宝库需要试炼钥匙才能解锁
- 可以被无限数量的玩家解锁
  - 玩家解锁宝库后，无法再次解锁该宝库
  - 如果玩家之前没有解锁该宝库，当靠近时，会有一条橙色的粒子流从玩家流向宝库
- 具有一个钥匙孔，根据附近玩家的情况会打开或关闭
  - 如果任何附近的玩家没有解锁该宝库，钥匙孔将打开
  - 如果所有附近的玩家都已解锁该宝库，钥匙孔将关闭
- 在其笼子内，它会循环显示可能从其战利品表中弹出的物品
- 每次解锁时，它弹出的奖励都是从其战利品表中随机生成的
- 宝库目前重用之前在试炼密室中奖励箱子使用的相同战利品表
  - 此战利品表是临时的，随着开发的继续将完全修订
- 在生存模式中无法制作或获得，开采时不会掉落任何物品
- 抗爆炸且无法移动

## 犰狳

- 犰狳发出的所有声音现在即使在玩家背对时也能听到
  - 犰狳现在会跟踪最后一个打过它们的玩家，将其视为威胁10秒钟
- 卷起来的犰狳发出的受伤声音已更新

## 旋风人

- 旋风人现在对铁傀儡具有攻击性，除了对玩家
- 旋风人不再对以下生物的攻击进行反击：骷髅、流浪者、僵尸、尸壳、蜘蛛、洞穴蜘蛛和史莱姆
  - 上述生物在受到旋风人的风弹投射物伤害时不会进行反击
- 修复了旋风人的奔跑粒子，使其在旋风人下方的叶子方块上拾取粒子颜色/纹理

# 特性和漏洞修复

## 命令

- 为实体目标选择器添加了“has_property”过滤器，允许根据属性的类型和值进行目标选择
- /damage命令不再包含“自杀”伤害类型。已替换为“自毁” ([MCPE-174865](https://bugs.mojang.com/browse/MCPE-174865))

## 物品

- 在领域中，尝试在创造模式下摧毁一堆超过一个的海龟蛋不再会一次性摧毁两个 ([REALMS-10477](https://bugs.mojang.com/browse/REALMS-10477))
- 刷怪蛋现在被称为“\[生物\] 刷怪蛋”，而不是“生成 \[生物\]”，以便玩家更容易在创造物品栏中搜索到它们

## 市场

- 修复了一个可能导致加载屏幕在41%时卡住的漏洞 ([MCPE-175550](https://bugs.mojang.com/browse/MCPE-175550))

## 生物

- 被喂食时，幼年生物现在会发出声音和粒子
- 幻翼发出的所有声音现在即使在玩家背对时也能听到 ([MCPE-133125](https://bugs.mojang.com/browse/MCPE-133125))
- 监守者发出的所有声音现在即使在玩家背对时也能听到 ([MCPE-159481](https://bugs.mojang.com/browse/MCPE-159481))

## 领域

- 添加了一种新的故事类型，称为“领域事件”。这些新故事会在您的领域发生有趣事件时自动发布到动态消息中。您玩得越多，发现的越多。
- 修复了故事的时间戳居中显示而不是在右上角显示的问题。
- 修复了由于领域故事分页导致的崩溃。
- 修复了使用游戏手柄从领域故事的成员标签返回时可能发生的崩溃。
- 修复了在PlayStation上更改时区后时间方块未正确渲染的问题。
- 修复了屏幕阅读器叙述不可用领域页面的问题。
- 修复了关闭GUI缩放导致大部分领域Plus PDP文本缺失的问题。
- 修复了用户在退出“选择订阅”屏幕后，在“选择预览领域”屏幕上错误显示错误消息的问题。

# 技术更新

## 方块

- “double_wooden_slab”方块现在分为独特的实例“oak_double_slab”、“spruce_double_slab”、“birch_double_slab”、“jungle_double_slab”、“acacia_double_slab”、“dark_oak_double_slab”
  - 这需要“格式版本”为1.20.70或更高

## 组件

- “damage_sensor”组件的“damage_modifier”和“damage_multiplier”字段现在在伤害免疫计算中被正确考虑，以便在实体的免疫期内，调整后的伤害小于或等于最高伤害时将被准确忽略 ([MCPE-167651](https://bugs.mojang.com/browse/MCPE-167651))
  - 这需要世界版本为1.20.70或更高

## 编辑器

编辑器及其对应的API处于早期开发阶段，适用于Windows PC基岩预览构建的键盘/鼠标。请在社交频道上标记我们，使用**\#BedrockEditor.**

了解[如何使用](https://aka.ms/LearnEditor)编辑器，加入[GitHub讨论](https://github.com/Mojang/minecraft-editor/discussions)论坛与团队互动，并通过[入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit)和[示例](https://github.com/Mojang/minecraft-editor-extension-samples)开始构建扩展。

本周修复:

- 修复了在多个连接的玩家按下按钮时，重载模态未能出现的漏洞

## 实体过滤器

- 添加了新的实体过滤器“was_last_hurt_by”，用于检查主题是否是最近攻击该实体的最后一个玩家或生物

## 物品

- 自定义盔甲附着物现在可以用原版装饰修饰，并且可以将修改过的原版图案应用于自定义盔甲附着物和物品  
  - 原版装饰纹理可以通过附着物组件进行覆盖
  - 原版装饰可以通过附着物组件应用于自定义几何盔甲
  - 修改过的原版装饰图案（以适应新的几何盔甲）可以通过附着物组件应用
  - 自定义盔甲上的装饰图案需要1.20.60+格式版本的附着物和物品

## Molang

- *surface_particle_color*、*query.surface_particle_texture_coordinate*和*query.surface_particle_texture_size*现在与1.20.70版本化，以允许这三个查询将叶子方块视为方块下方的表面纹理。低于1.20.70版本的Molang将继续无法看到它们下方的叶子方块
- 此更改适用于具有manifest.json最小引擎版本为1.20.70或更高的包中的Molang查询。

## 稳定性和性能

- 移除了*ItemFrameDropItemPacket* 

# 实验性技术更新

## API

- 实体组件
  - 添加了*EntityTypeFamilyComponent*，具有函数*getTypeFamilies(): string\[\]*和*hasTypeFamily(typeFamily: string): boolean*
- 物品
  - 将*ItemFoodComponent*从*beta*移动到*1.9.0*
  - 添加函数*matches(itemName: string, states?: Record\<string, boolean \| number \| string\>): boolean*
- 移除了类*BlockVolumeUtils*。将实用函数移动到*BlockVolumeBase*和*BlockVolume*
- 添加类*BlockVolumeBase*。是块体积将扩展的基类
- BlockVolume
  - **破坏性更改** 将*BlockVolume*从接口转换为扩展*BlockVolumeBase*的类
- *@minecraft/server.Entity.playAnimation*
  - 将Entity.playAnimation从*beta*移动到*stable*
- 将枚举*BlockPistonState*从*beta*移动到*1.9.0*
- 将类*BlockPistonComponent*从*beta*移动到*1.9.0*
- 将类*PistonActivateAfterEvent*从*beta*移动到*1.9.0*
- 将类*PistonActivateAfterEventSignal*从*beta*移动到*1.9.0*

## 维度

- *Dimension.getEntities*现在仅返回被查询维度内的实体

## 图形

- 为iOS设备启用延迟技术预览
- 为延迟技术预览添加点光源阴影。此新功能允许火把和灯笼等光源投射阴影
  - 请注意，根据您当前的阴影质量设置，此功能可能默认禁用。在视频设置的延迟图形部分添加了新标签和提示框，以指示点光源阴影当前是开启还是关闭。
  - 在与其他功能的“超高”设置同时使用此新功能时，可能会出现一些不稳定性。如果您遇到崩溃，降低一些视觉设置可能有助于缓解问题，直到解决为止。
- 修复了延迟技术预览中悦灵的光照问题