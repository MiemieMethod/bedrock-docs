---
title: Minecraft Beta & Preview - 1.21.50.25
date: 2024-10-23T14:04:45Z
updated: 2024-10-24T11:52:44Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/zh-cn/articles/31291872110733-Minecraft-Beta-Preview-1-21-50-25
hash:
  features-and-bug-fixes: 新功能与漏洞修复
  01JAWYFZMBZTNGQ2D4GVW3NHHQ: 新功能与漏洞修复
---

**发布时间:** 2024年10月23日

**Minecraft预览和Beta信息:**

- 这些进行中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上获取。加入或退出Beta版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一个苍白之园，附近放置了树脂块类型的工作台和熔炉。有张开的眼眸花，附近有一个嘎枝，带有粒子效果，连接到带有嘎枝之心的苍白橡木。](https://feedback.minecraft.net/hc/article_attachments/31291909576205)

哦，太好了！你找到了我！自从上次预览和Beta更新后，我一直在苍白之园徘徊——让我告诉你——嘎枝不是最好的室友。幸运的是，本周苍白之园将新增两个功能：树脂和张开的眼眸花！树脂是一种新方块，你可以在与嘎枝遭遇后合成（试着让它洗洗碗……），而张开的眼眸花是苍白之园独有的花朵，会在夜间绽放。它们甚至会带有橙色的微光，也许能帮助我找到出路！一如既往，我们希望收到你对这些新功能的反馈，访问 [aka.ms/mcgamedropfeedback](http://aka.ms/mcgamedropfeedback) ，并且你可以在 [bugs.mojang.com](http://bugs.mojang.com/) 报告任何漏洞！以下是本周的其他更新内容：

# 新功能与漏洞修复

## 树脂

- 树脂团是一种新的多面方块：
  - 由嘎枝之心被摧毁时掉落
  - 当嘎枝之心被攻击时，放置在嘎枝之心周围
  - 可合成成树脂块
  - 可在熔炉中硬化成树脂砖块
  - 可用于修剪盔甲
- 树脂砖块可合成树脂砖套装：
  - 红砖块
  - 楼梯
  - 墙
  - 台阶
  - 凿刻树脂砖块
- 这两者都可以在林地府邸的箱子中找到
- 树脂块可使用两块苍白橡木原木合成嘎枝之心

## 张开的眼眸花

张开的眼眸花是生成在苍白之园生物群系中的新花朵。独特特性：

- 它们存在两种变种：闭合眼眸花和张开眼眸花
- 根据时间的不同，眼眸花会在两种变种之间转换
  - 夜间，眼眸花会变为张开
  - 白天，眼眸花会变为闭合
  - 在没有昼夜循环的维度中，它们将保持原状
- 种植在地面的眼眸花会彼此交流，帮助彼此打开或关闭
- 晚上，张开的眼眸花有发光的眼睛
- 可以通过给苍白之园生物群系中的草施骨粉获得眼眸花
- 蜜蜂与眼眸花互动时会中毒
- 使用眼眸花制作的谜之炖菜会根据变种产生失明或反胃效果
- 可以从闭合和张开的眼眸花分别合成灰色或橙色染料

## 苍白之园

- 进一步调整了苍白之园地平线处天空的颜色，使其更接近Java版 ([MCPE-187519](https://bugs.mojang.com/browse/MCPE-187519))
- 调整了苍白橡木告示牌模型和UI的纹理，使其与其他告示牌一致 ([MCPE-187306](https://bugs.mojang.com/browse/MCPE-187306 "https://bugs.mojang.com/browse/MCPE-187306"))
- 苍白橡树树苗现在可以堆肥 ([MCPE-187457](https://bugs.mojang.com/browse/MCPE-187457 "https://bugs.mojang.com/browse/MCPE-187457"))
- 苍白垂须现在使用与其他苔藓块和苍白苔藓块相同的声音 ([MCPE-187327](https://bugs.mojang.com/browse/MCPE-187327 "https://bugs.mojang.com/browse/MCPE-187327"))
- 增加了苍白垂须环境声音的频率
- 苍白垂须不再在从苍白橡树树苗种植的苍白橡树上生成

## 嘎枝之心

- 自然生成的嘎枝之心现在即使使用精准采集也会掉落20到24经验
- 增加了嘎枝之心环境声音的频率
- 非活动状态的嘎枝之心纹理已更新，以更一致地与其活动状态保持一致 ([MCPE-187395](https://bugs.mojang.com/browse/MCPE-187395 "https://bugs.mojang.com/browse/MCPE-187395"))

## 嘎枝

- 增加了愤怒嘎枝的速度
- 嘎枝现在造成更多的攻击伤害
- 当嘎枝之心被摧毁时，其嘎枝现在会在崩塌前扭动几秒钟
- 由嘎枝之心生成的嘎枝在与玩家卡在洞中超过5秒后会崩塌
  - 这防止了潜在的软锁，因为无敌的嘎枝会阻止玩家开采或放置任何方块，要求他们退出并重新进入世界以强制嘎枝摧毁
- 嘎枝崩塌现在会导致附近的幽匿催发体绽放
  - 但不会放置幽匿，因为嘎枝不会掉落任何经验
- 嘎枝的行走动画已更新
- 嘎枝的攻击动画已更新
- 由嘎枝之心生成的嘎枝不再避免破坏方块
- 由命令或刷怪蛋生成的嘎枝不再对火和熔岩无敌
- 由命令或刷怪蛋生成的嘎枝现在避免破坏方块
- 嘎枝的攻击速度已减少，以匹配Java版 ([MCPE-187309](https://bugs.mojang.com/browse/MCPE-187309 "https://bugs.mojang.com/browse/MCPE-187309"))

# 新功能与漏洞修复

## 方块与物品

- 以下方块现在仅在使用镐破坏时掉落：高炉、炼药锅、发射器、投掷器、附魔台、熔炉、漏斗和烟熏炉 ([MCPE-33950](https://bugs.mojang.com/browse/MCPE-33950 "https://bugs.mojang.com/browse/MCPE-33950"))
- 需要支撑的以下方块现在在使用任何工具破坏时总是掉落：所有铜门、铁门、重质测重压力板、轻质测重压力板、磨制黑石压力板和石头压力板
- 紫水晶母岩现在使用不当工具开采更慢
- 以下总是掉落的方块在使用不正确工具时现在开采更快：钟、酿造台、合成器、末影箱、灯笼和灵魂灯笼。请注意，末影箱被视为“总是掉落方块”，即使掉落的不是末影箱 ([MCPE-176374](https://bugs.mojang.com/browse/MCPE-176374 "https://bugs.mojang.com/browse/MCPE-176374"))
- 修复了潜影盒颜色未作为名称部分列出的一个问题 ([MCPE-182930)](https://bugs.mojang.com/browse/MCPE-182930)
- 草和菌岩在位于史莱姆、蜂蜜、漏斗或化学热（教育版方块）下方时不再衰败为泥土和下界岩 ([MCPE-62132](https://bugs.mojang.com/browse/MCPE-62132))
- 草和菌岩在位于侦测器下方时现在会衰败为泥土和下界岩

## 功能

- 苍白橡树树苗现在可以在苔藓块和苍白苔藓块上生长 ([MCPE-187322](https://bugs.mojang.com/browse/MCPE-187322 "https://bugs.mojang.com/browse/MCPE-187322"))

## 游戏玩法

- 使用 /camera 命令时，摄像机现在会在X轴和Y轴上正确旋转
- 使用空收纳袋现在会在第一视角和第三视角中播放动画
- 船或骆驼的第二乘客在撞击未加载区块时现在也会有警告消息

## 常规

- 改进了玩家生成算法，使其更难在水或细雪中生成 ([MCPE-120237](https://bugs.mojang.com/browse/MCPE-120237 "https://bugs.mojang.com/browse/MCPE-120237"))

## 图形

- 移除了海带意外产生的更暗色调 ([MCPE-169713](https://bugs.mojang.com/browse/MCPE-169713))

## 物品

- 所有着火的投射物现在点燃TNT矿车和TNT块 ([MCPE-183512](https://bugs.mojang.com/browse/MCPE-183512 "https://bugs.mojang.com/browse/MCPE-183512"))
- 苍白橡木告示牌和苍白橡木悬挂式告示牌物品的纹理已调整，使其与其他告示牌一致

## 生物

- 如果不在坚固的表面上，旋风人的空闲声音现在正确播放 ([MCPE-180023](https://bugs.mojang.com/browse/MCPE-180023 "https://bugs.mojang.com/browse/MCPE-180023"))

## Realms

- 从Realms Stories设置中移除了退出选项，现在它位于时间轴标签中
- 修复了玩家无法在活动Realm上创建新世界的问题

## 声音

- 湿海绵现在播放正确的方块声音 ([MCPE-187287](https://bugs.mojang.com/browse/MCPE-187287))

## 试炼密室

- 更改end_2中箱子的内容以引用战利品表

## 用户界面

- 当物品在槽位之间移动时，盾牌物品的大小不再变化
- 在玩家光标下移动的收纳袋现在正确更新其提示框
- 现在可以使用收纳袋收集合成输出，将合成的物品添加到收纳袋中
- 触控控制：修复了在控制自定义期间船只可交互的错误 ([MCPE-184404](https://bugs.mojang.com/browse/MCPE-184404 "https://bugs.mojang.com/browse/MCPE-184404"), [MCPE-184406](https://bugs.mojang.com/browse/MCPE-184406 "https://bugs.mojang.com/browse/MCPE-184406"))
- 触控控制：在摇杆模式下，现在可以双击“向上飞行”以停止飞行 ([MCPE-185237](https://bugs.mojang.com/browse/MCPE-185237 "https://bugs.mojang.com/browse/MCPE-185237"))
- 触控控制：快速连续点击向上和向下飞行不再导致玩家停止飞行 ([MCPE-185236](https://bugs.mojang.com/browse/MCPE-185236 "https://bugs.mojang.com/browse/MCPE-185236"))
- 热键栏中的工具在耐久度减少时不再动画化 ([MCPE-186979](https://bugs.mojang.com/browse/MCPE-186979 "https://bugs.mojang.com/browse/MCPE-186979"))
- 在使用手柄时，从命令方块UI中移除“X”关闭按钮
- 修复了一个问题，导致在新服务器标签中输入错误的IP地址时，未在加入外部服务器前正确验证
- 选中收纳袋中的物品时，触控屏设备上会弹出显示物品名称的窗口

# 技术更新

## API

- 为 addNewTheme() 添加了 name 和 parentThemeId 的额外可选参数。当通过函数传递了有效的 parentThemeId 时，新创建的主题将继承父主题的所有主题颜色属性

## 生物群系

- 修复了一个问题，即在1.17.40之前创建的区块可能表现为海洋生物群系，具有类似海洋的迷雾、天空颜色和生物生成 ([MCPE-186928](https://bugs.mojang.com/browse/MCPE-186928 "https://bugs.mojang.com/browse/MCPE-186928"))

## 编辑器

- 添加了新的定位工具以帮助查找生物群系
- 编辑器启动时，时间固定为正午
- 改进了视口焦点可见性，增加了动画轮廓并将聚焦状态添加为切换模式 (CTRL + TAB) 的一步
- 向 `IModalToolContainer` 添加了 `focusToolInputContext` 函数，该函数将尝试设置模式输入焦点（例如工具轨道的视口）

## 实体组件

- 移除了 'minecraft:can_attack_ghast' 组件，取而代之的是新的 'minecraft:cannot_be_attacked' 组件。当添加到实体时，除非它们满足例外过滤器，否则其他实体无法攻击它。原版中，它被添加到恶魂，创建者可以将他们的实体添加到例外过滤器，允许它们攻击恶魂。

## 实体事件响应

- "execute_event_on_home_block" 实体事件响应现在标记为 \[Beta\]，并且需要在根JSON对象中指定 "use_beta_features"
  - 当前实现未完全符合我们的内部标准，因此在我们能开发出更健全的技术解决方案之前，它将保持不可用于创建者内容
  - 这种方法允许我们在不影响向后兼容性的情况下迭代该功能
- 添加了 "emit_particle" 实体事件响应，允许在实体的包围盒中心处发射粒子
  - "particle" 字段允许指定要发射的粒子类型

## 网络协议

- 移除了等级事件：ParticleCreakingTeardown
- 添加了新的粒子类型：CreakingCrumble

# 实验性技术更新

## 摄像机

- 添加了实验性切换 "Aim Assist" ，允许在使用自定义摄像机视角时轻松瞄准。
  - 目前Aim Assist仅瞄准方块。实体将在未来版本中启用。
- 可通过 "/aimassist" 命令启用Aim Assist。
  - Aim Assist的瞄准行为（距离、宽度和高度）可以通过使用行为包在 "aim_assist" 文件夹下的设置进行配置。
  - Aim Assist将高亮显示选定的目标。高亮纹理可通过使用资源包在 "textures\ui" 文件夹下的纹理进行自定义

## API

- 在 `system` 类的 `beforeEvents` 中添加了 `shutdown` 事件。这将在所有玩家离开后且世界即将关闭时触发。
- 输入API
  - 添加了一套输入API，即使玩家的输入被禁用（具有输入权限）也可读取
  - 为 `InputInfo` 添加了 `getMovementVector(): Vector2` 以读取原始移动值
  - 添加了枚举 `InputButton`，包含 `Jump` 和 `Sneak`
  - 添加了枚举 `ButtonState`，包含 `Pressed` 和 `Released`
  - 为 `InputInfo` 添加了 `getButtonState(button: InputButton): ButtonState` 以读取原始玩家按钮输入
  - 添加了 `world.afterEvents.playerButtonInput` 事件以监听按钮变化事件

## 创建者选项

- 添加了 "设备信息设置" 部分
  - 添加了允许覆盖脚本和Molang使用的内存层级的选项

# 实验性技术更新

## 摄像机

- 添加了实验性切换 "Aim Assist" ，允许在使用自定义摄像机视角时轻松瞄准。
  - 目前Aim Assist仅瞄准方块。实体将在未来版本中启用。
- 可通过 "/aimassist" 命令启用Aim Assist。
  - Aim Assist的瞄准行为（距离、宽度和高度）可以通过使用行为包在 "aim_assist" 文件夹下的设置进行配置。
  - Aim Assist将高亮显示选定的目标。高亮纹理可通过使用资源包在 "textures\ui" 文件夹下的纹理进行自定义

## API

- 在 `system` 类的 `beforeEvents` 中添加了 `shutdown` 事件。这将在所有玩家离开后且世界即将关闭时触发。
- 输入API
  - 添加了一套输入API，即使玩家的输入被禁用（具有输入权限）也可读取
  - 为 `InputInfo` 添加了 `getMovementVector(): Vector2` 以读取原始移动值
  - 添加了枚举 `InputButton`，包含 `Jump` 和 `Sneak`
  - 添加了枚举 `ButtonState`，包含 `Pressed` 和 `Released`
  - 为 `InputInfo` 添加了 `getButtonState(button: InputButton): ButtonState` 以读取原始玩家按钮输入
  - 添加了 `world.afterEvents.playerButtonInput` 事件以监听按钮变化事件

## 创建者选项

- 添加了 "设备信息设置" 部分
  - 添加了允许覆盖脚本和Molang使用的内存层级的选项

# 解答

以下是按照您的要求翻译的Minecraft Beta & Preview - 1.21.50.25更新文档。