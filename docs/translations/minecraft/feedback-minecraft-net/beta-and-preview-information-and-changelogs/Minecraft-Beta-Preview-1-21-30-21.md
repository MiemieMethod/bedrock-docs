---
标题：Minecraft Beta & Preview - 1.21.30.21
日期：2024-08-01T12:11:38Z
更新：2024-08-01T16:50:36Z
类别：Beta 和 Preview 信息及更新日志
链接：[https://feedback.minecraft.net/hc/en-us/articles/28896769176845-Minecraft-Beta-Preview-1-21-30-21](https://feedback.minecraft.net/hc/en-us/articles/28896769176845-Minecraft-Beta-Preview-1-21-30-21)
哈希：
  h_01J475C518A80MW7EV6130D1R6: 特性与漏洞修复
  h_01J475C518YEZRQAFJ4PH2ATXC: 方块
  h_01J475C51807K3D6XQCZS1VECS: 合成
  h_01J475C518WVND80HTAZX6DGCF: 完整键盘游戏
  h_01J475C518HPH15E4F1HBDNG54: 游戏玩法
  h_01J475C518G15898PZ5Q1EGEAP: 一般
  h_01J475C518X4R4M19Z69QQ5TYW: 图形
  h_01J475C518ET5PG3H1XT3T68ZQ: 如何玩
  h_01J475C518QM6N82HQQ38BJ2QR: 物品
  h_01J475D95T982P8B6FR89Y800V: 生物
  h_01J475D95T2N6M5KM25ESPVXVK: 多人游戏
  h_01J475D95TBKNYPN3S7DYACPMF: 稀有度
  h_01J475D95TM666M23G03APPED3: 普通
  h_01J475D95TGC4HK47NQGR7NYK3: 史诗
  h_01J475D95T9GM1B70Z96YP5W2X: 稀有
  h_01J475D95TTDBREXMBWGAES613: 不常见
  h_01J475D95TTF92R6CPD7WW3HP5: 领域
  h_01J475D95TJ36P7V01007C0V4E: 触控控制
  h_01J475D95TZPBJGVYYHF3J2A7P: 试炼密室
  h_01J475D95T66RETEXEF1000JGM: 用户界面
  h_01J475D95TD1ZYY96RMG879G5V: 原版趋同
  h_01J475D95T04B3J96BHYEPX23E: 技术更新
  h_01J475D95TNN5GG8VQBQN9RG87: 附加包与脚本引擎
  h_01J475D95TR653HF46G1M67FF8: API
  h_01J475D95TFEN25041SPHK06ZS: 方块-1
  h_01J475D95TN1GG3A93JP9H7D7N: 命令
  h_01J475D95TGKG6DGP2STC7BZCP: 编辑器
  h_01J475D95TRRE38AR9GYYV6CDS: 实体组件
  h_01J475D95TZKCNGWBCNG7K1V66: 游戏玩法-1
  h_01J475D95TTYS7XFX72RBG5844: 一般-1
  h_01J475D95T2N7EG11Z4M9X69WQ: 物品-1
  h_01J475D95TV5KC6FD39XWEMV39: 战利品表
  h_01J475D95TJEFATRW19Q85DDGX: 结构
  h_01J475D95T3EPA350DXZ6DHG2V: 实验性技术更新
  h_01J475D95T0GMNA6SJ7QRZNE9G: 附加包与脚本引擎-1
  h_01J475D95T8VVBH2ETK3Z4P630: API-1
  h_01J475D95V6F2TXG2WVWXF60CY: 图形-1
---

**发布日期：** 2024年8月1日

**关于Minecraft Preview和Beta的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量。
- Minecraft Preview可在Xbox、PlayStation、Windows和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)。
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![Minecraft树冠的截图，阳光透过树叶洒下，展示了增加了次表面散射效果的Deferred Technical Preview特性。](https://feedback.minecraft.net/hc/article_attachments/28896805992461)

新的Minecraft Preview和Beta版本正在发布，修复了消失的船只、抗热的雪傀儡等问题！对于那些关心收纳袋的玩家，我们的开发者仍在努力将收纳袋引入Preview和Beta，请关注未来的更新日志以获取最新消息！

以下是本周Preview和Beta的新内容：

# 特性与漏洞修复

## 方块

- 使用活塞垂直收缩的含水方块不再在客户端产生“幽灵水”（[MCPE-144222](https://bugs.mojang.com/browse/MCPE-144222)）。
- “purpur_block”方块现在分为独特实例“purpur_block”和“purpur_pillar”；之前未使用的雕刻和光滑紫珀块被重命名为“deprecated_purpur_block_1”和“deprecated_purpur_block_2”以兼容旧版，但在创造模式物品栏和命令中隐藏。
- “structure_void”的方块状态已被移除，“air”变体将转换为基础方块。
- 添加了新的原版方块和物品标签，以支持数据驱动方块的原版物品等级破坏速度。
- 所有原木、去皮原木、木头和去皮木头在各种场景下现在被一致对待：
  - 能够降落在树上的飞行动物现在会将这些方块视为适合的降落位置。
  - 鹦鹉现在会优先选择这些方块作为降落点。
  - 之前这些行为仅适用于这些方块的子集。
- 海带不再能放置在任何类型的栅栏上，而不仅仅是它们的子集。
- 海草不再能放置在任何类型的栅栏上，而不仅仅是它们的子集。
- 海龟蛋不再能放置在任何类型的栅栏上，而不仅仅是它们的子集。
- “cobblestone_wall”方块现在分为独特实例“cobblestone_wall”、“mossy_cobblestone_wall”、“granite_wall”、“diorite_wall”、“andesite_wall”、“sandstone_wall”、“brick_wall”、“stone_brick_wall”、“mossy_stone_brick_wall”、“nether_brick_wall”、“end_stone_brick_wall”、“prismarine_wall”、“red_sandstone_wall”和“red_nether_brick_wall”。
- “granite_wall”、“diorite_wall”、“andesite_wall”、“stone_brick_wall”、“mossy_stone_brick_wall”和“prismarine_wall”的破坏时间现在为1.5。
- “sandstone_wall”和“red_sandstone_wall”的破坏时间现在为0.8。
- “end_stone_brick_wall”的破坏时间现在为3.0。

## 合成

- 合成烟花时，添加或移除网格中的物品将相应更新输出物品（[MCPE-183455](https://bugs.mojang.com/browse/MCPE-183455)）。

## 完整键盘游戏

- 在完整键盘游戏模式下，添加Q和E作为JSON UI菜单（包括物品栏菜单）的左键和右键单击等效项。

## 游戏玩法

- 不祥之兆效果现在可以通过喝任意等级的不祥之瓶重置。
- 船只在冰面滑动时不再消失（[MCPE-180432](https://bugs.mojang.com/browse/MCPE-180432)）。
- 修复了在活塞移动讲台时打开讲台可能导致的崩溃。讲台在移动时现在会关闭书本界面（[MCPE-183508](https://bugs.mojang.com/browse/MCPE-183508)）。
- 在某些平台上，玩家下车后不再会被放置在地面下（[MCPE-184363](https://bugs.mojang.com/browse/MCPE-184363)，[MCPE-182448](https://bugs.mojang.com/browse/MCPE-182448)）。

## 一般

- 修复了在最小化并恢复游戏窗口后，导致占位符纹理出现的漏洞。

## 图形

- 修复了横幅在其他透明物体之前渲染的问题，无论其位置如何（[MCPE-130262](https://bugs.mojang.com/browse/MCPE-130262)）。

## 如何玩

- 添加了换行功能，以便在“如何玩”主题标签过长时不再添加“...”。

## 物品

- 每个旗帜图案物品的名称现在包括其图案类型，而不是作为副标题（[MCPE-182508](https://bugs.mojang.com/browse/MCPE-182508)）。
- 锻造模板物品现在根据其模板类型命名，而不是通用的“锻造模板”名称。
  - 它们通过悬停文本的副标题指定为锻造模板。
- 每个旗帜图案物品都获得了独特的物品纹理，以便更好地区分彼此。
- 恼鬼旗帜已重命名为不祥旗帜，以匹配Java版。

![Minecraft创造模式物品栏，显示搜索结果为旗帜。更新后的旗帜图案物品可见。](https://feedback.minecraft.net/hc/article_attachments/28902005618957)

## 生物

- 修复了自定义实体名称在死亡消息中未正确显示的问题（[MCPE-158447](https://bugs.mojang.com/browse/MCPE-158447)）。

## 多人游戏

- 修复了游戏内邀请界面未显示正确子状态的问题。

## 稀有度

- 各种物品和方块的稀有度已更改（[MCPE-182414](https://bugs.mojang.com/browse/MCPE-182414)）。
  - 一旦这些稀有度变化在未来的Java版快照中生效，所有物品和方块的稀有度将在两个平台上保持一致。
- 稀有度是一组类别，用于确定物品或方块名称的显示颜色。
  - 它对游戏玩法没有影响，但用于指示某物获取的难度。
  - 默认情况下，除非另有说明，所有物品和方块的稀有度为普通，名称以白色显示。
- 我们重新评估了游戏中所有物品和方块的稀有度，以更准确地反映获取它们的当前挑战，依据以下准则：
  - 物品和方块的稀有度取决于以下因素：
    - 在战利品表中找到它的几率，包括生物掉落。
    - 获取它所需的旅行量。
    - 获取它所需克服的障碍的难度。
    - 该物品或方块在世界中可能存在的数量。
  - 任何可以合成的物品必须继承其合成材料中最高的稀有度。
    - 例如，重锤的稀有度为史诗，因为其材料之一（沉重核心）的稀有度为史诗。
    - 同样，任何仅具有普通合成材料的合成物品也必须是普通的。
  - 以下列表详细列出已更改为该稀有度类别的物品和方块。

### 普通

- 末地水晶
- 金苹果

### 史诗

- 鞘翅
- 龙首
- 沉默盔甲装饰

### 稀有

- 附魔金苹果
  - 附魔金苹果在近年来变得更加常见，因为可以在古代城市和试炼密室中找到，因此降级为稀有而非史诗。
- 三叉戟
  - 我们最近将三叉戟的稀有度从普通提升到史诗，但在重新评估后，我们认为它比其他史诗类别的物品（如沉重核心或鞘翅）更容易获取。
- 下界之星
- 守卫盔甲装饰
- 眼睛盔甲装饰
- 恼鬼盔甲装饰
- 塔楼盔甲装饰
- 凋灵骷髅头颅
- 头颅盾徽旗帜图案
  - 由于凋灵骷髅头颅现在为稀有，这些旗帜图案也应为稀有。
- Mojang徽标旗帜图案
  - 由于附魔金苹果现在为稀有，这些旗帜图案也应为稀有。
- 以下音乐唱片：
  - Pigstep
  - otherside
  - Creator

### 不常见

- 嗅探兽蛋
- 锁链头盔
- 锁链胸甲
- 锁链护腿
- 锁链靴子
- 追溯指针
- 唱片残片5
- 鹦鹉螺壳
- 回响碎片
- 山羊角
- 陶片
- 不祥之瓶
- 不祥旗帜
- 下界升级
- 哨兵盔甲装饰
- 沙丘盔甲装饰
- 海岸盔甲装饰
- 野生盔甲装饰
- 潮汐盔甲装饰
- 鼻子盔甲装饰
- 肋骨盔甲装饰
- 导航者盔甲装饰
- 造型师盔甲装饰
- 提升者盔甲装饰
- 主机盔甲装饰
- 流动盔甲装饰
- 闪电盔甲装饰
- 以下音乐唱片：
  - 13
  - Cat
  - Blocks
  - Chirp
  - Creator (音乐盒)
  - Far
  - Mall
  - Mellohi
  - Stal
  - Strad
  - Ward
  - 11
  - Wait
  - Relic
  - 5
  - Precipice

## 领域

- 修复了阻止RealismCraft和其他一些包在领域中正常工作的漏洞。这是一个服务端修复，已在Preview和最新完整版本中生效（[REALMS-11913](https://bugs.mojang.com/browse/REALMS-11913)，[REALMS-11916](https://bugs.mojang.com/browse/REALMS-11916)）。
- 领域故事内容在滚动时不再被裁剪。
- 在任何UI大小下，文本不再与Galaxy Z Flip设备上的领域故事截图重叠。
- 在选择要创建世界的Preview领域时，游戏手柄图例不再与UI元素重叠。
- 在分屏模式下，仅为主玩家显示订阅标签。
- 在连接到领域或相关屏幕时，领域ID现在在调试文本中显示。

## 触控控制

- 改进了触控控制的新十字键。现在更紧凑，包含后退移动按钮，并稍微扩展了不接收相机输入的区域，以防止意外的相机移动。在自定义控制时，斜对角按钮也可见。
- 修复了隐藏HUD命令无法隐藏十字键触控控制的漏洞（[MCPE-184157](https://bugs.mojang.com/browse/MCPE-184157)）。

## 试炼密室

- 添加了新变体的走廊，包括“遭遇”：短挑战，通向更大的密室。
- 交叉口的床现在颜色随机化（[MCPE-180424](https://bugs.mojang.com/browse/MCPE-180424)）。
- 用漏斗和木桶替换了密室入口处的空箱子，以更好地向玩家展示这些是用于处理和库存管理的物品！
- 修复了多个试炼密室模板缺少或不正确的方块（[MCPE-176952](https://bugs.mojang.com/browse/MCPE-176952)）。
- 修复了试炼密室中可能在墙后生成的不可接触的陷阱（[MCPE-180912](https://bugs.mojang.com/browse/MCPE-180912)）。
- 一些试炼密室中的史莱姆刷怪笼在没有玩家干预的情况下不会生成史莱姆。
- 修复了不祥宝库可能未能在基座和密室1/2中生成的问题。

## 用户界面

- 修复了购买订阅时可能出现的软锁定问题。
- 修复了当玩家持有不祥之瓶时未显示“饮用”交互提示的漏洞。
- 修复了玩家生命值被向下取整而非向上取整的问题，导致HUD有时仅显示空生命图标（[MCPE-183157](https://bugs.mojang.com/browse/MCPE-183157)）。
- 聊天输出的滚动位置在游戏屏幕重新获得焦点后保持其位置。
- 缩短了在其他设备上登录的URL，变为microsoft.com/link。

## 原版趋同

- 实体掉入水中时现在发出与Java版相同的溅水声（[MCPE-44120](https://bugs.mojang.com/browse/MCPE-44120)）。
- 修复了无法将独立脚手架方块放置在结构方块顶部的漏洞（[MCPE-169818](https://bugs.mojang.com/browse/MCPE-169818)）。
- 具有抗火能力的雪傀儡在温暖的生物群系中不再受到伤害（[MCPE-94448](https://bugs.mojang.com/browse/MCPE-94448)）。
- 未雕刻的南瓜块不再用于创建雪傀儡和铁傀儡（[MCPE-33801](https://bugs.mojang.com/browse/MCPE-33801)）。
- 当物品被附魔时，其稀有度状态现在会根据其基础稀有度提高：
  - 如果物品的基础稀有度为普通或不常见，则附魔后将变为稀有。
  - 如果物品的基础稀有度为稀有，则附魔后将变为史诗。
  - 如果物品的基础稀有度为史诗，则附魔后仍为史诗。

# 技术更新

## 附加包与脚本引擎

- 从世界加入流程的包中移除了已弃用的行为包下载相关代码。

## API

- 发布了@minecraft/server版本1.3.0
  - 注意：在Preview期间可能仍会更改。
- 添加了@minecraft/server版本1.4.0-beta。
- 修复了玩家的isEmoting方法（[MCPE-180083](https://bugs.mojang.com/browse/MCPE-180083)）。
- 发布了playerEmoteWorld事件，从Beta版本更新到1.14.0。
- 发布了BlockRecordPlayerComponent类，从Beta版本更新到1.14.0。
- 发布了UIManager类，从Beta版本更新到1.3.0。
- 发布了EntityQueryPropertyOptions，从Beta版本更新到1.14.0。
- 将EntityStrengthComponent从Beta版本更新到1.13.0。

## 方块

- 修复了`minecraft:repeating_command_block`在切换到`needs redstone`时不会执行的问题。
- 添加了'minecraft:redstone_conductivity'组件，用于控制自定义方块的基本红石属性。

## 命令

- /locate structure命令的输出现在显示找到的结构的标识符，而不是其名称。

## 编辑器

- 改进了客户端小部件系统。
  - 重构了客户端小部件系统，以使用组件实现基本小部件功能。
  - 添加了编辑器客户端渲染器助手服务，以帮助在编辑器中渲染小部件。
  - 更改了小部件移动为完全自由移动，释放时对齐网格。
  - 为实体、文本、小部件、高度引导和基本渲染原语添加了新小部件组件。
- 对PropertyPane API进行了额外更新。
  - 移除了IPropertyPane的addBlockPicker和addEntityPicker方法，取而代之的是利用类型安全的IObservableProp\<string\>值的addComboBox API。
    - 添加了IComboBoxPropertyItem和IComboBoxPropertyItemOptions接口。
    - 下拉框支持不同数据类型，以便进行额外验证，ComboBoxPropertyItemDataType。实体和方块类型的工作方式与旧组件相似，自定义类型允许用户定义列表，并且是默认值。
  - 添加了一种替代Property Pane的addNumber API，利用类型安全的IObservableProp\<number\>值API。
    - 为新属性项添加了INumberPropertyItem和INumberPropertyItemOptions接口。
    - 将创建属性包数字项的函数重命名为addNumber_deprecated。
  - 更新了输入字段的主题颜色，并将数字输入字段值居中对齐。
  - 添加了一种替代Property Pane的addDropdown API，利用类型安全的IObservableProp\<number\>值。
    - 为新属性项添加了IDropdownPropertyItem、IDropdownPropertyItemOptions和IDropdownPropertyItemEntry接口。每个下拉项现在支持imageData?: ImageResourceData属性以渲染图像。
    - 将创建属性包数字项的函数重命名为addDropdown_deprecated。
  - 修复了下拉UI元素的主题和内容对齐问题。
  - 添加了一种替代Property Pane的addColorPicker API，利用类型安全的IObservableProp\<RGBA\>值API。
    - 为新属性项添加了IColorPickerPropertyItem和IColorPickerPropertyItemOptions接口。
    - 将创建属性包颜色选择器项的函数重命名为addColorPicker_deprecated。
  - 添加了一种替代Property Pane的addString API，利用类型安全的IObservableProp\<string\>值API。
    - 为新属性项添加了IStringPropertyItem和IStringPropertyItemOptions接口。
    - 将创建属性包字符串项的函数重命名为addString_deprecated。
  - 修复了缺失的召唤工具图标。
  - 为“ExtensionContext.settings.theme”添加了以下函数：addNewTheme(name: string): void、deleteTheme(name: string): void、getCurrentTheme(): string和updateThemeColor(name: string, key: ThemeSettingsColorKey, newColor: minecraftserver.RGBA): void。这些函数在传入“minecraft:default”或任何其他内置主题时将抛出错误。updateThemeColor和deleteTheme也将抛出错误，如果主题不存在。
  - 为块选择器模态添加了块图像支持。
  - 修复了在块或实体选择器中输入某些字符时导致错误的问题。
  - 添加了验证，以防止在概率调色板项中添加已存在的块。
  - 为“ExtensionContext.settings.theme”添加了以下函数：addNewTheme(name: string): void、deleteTheme(name: string): void、getCurrentTheme(): string和updateThemeColor(name: string, key: ThemeSettingsColorKey, newColor: minecraftserver.RGBA): void。这些函数在传入“minecraft:default”或任何其他内置主题时将抛出错误。updateThemeColor和deleteTheme也将抛出错误，如果主题不存在。

## 实体组件

- “behavior.fire_at_target”不再限制于原版内容。
  - 该目标允许实体通过延迟射击攻击。
- “behavior.jump_around_target”不再限制于原版内容。
  - 该目标允许实体在目标周围跳跃。
- “behavior.move_around_target”不再限制于原版内容。
  - 该目标允许实体在目标周围移动。

## 游戏玩法

- 暴露实体偏移量，以便用户可以从实体中心更改相机的轴心点，以适应第三人称镜头。

## 一般

- 更新了地物规则文档。
- 在设置的创作者部分添加了GUI日志级别选项，改变启用内容日志时在屏幕上显示的内容日志级别。

## 物品

- 添加了一个内容错误，以防在1.10数据中无法找到与icon_name相关的图标。
- 修复了物品组件在远程客户端上未初始化的问题。
- 添加了“minecraft:rarity”物品组件，允许指定物品的稀有度。
  - 它有一个字段“value”，接受以下值：
    - “common”
    - “uncommon”
    - “rare”
    - “epic”
  - 也可以作为内联值写成：“minecraft:rarity”: “uncommon”。
  - 物品的稀有度将决定其名称使用的颜色。
    - 如果物品指定了“minecraft:hover_text_color”组件，则该悬停文本颜色将优先于稀有度颜色。

## 战利品表

- 添加了“set_potion”物品功能，用于战利品表，可以设置与药水ID兼容的物品的药水类型。
  - 它有一个字段“id”，接受以下药水ID值：
    - “water”
    - “mundane”
    - “long_mundane”
    - “thick”
    - “awkward”
    - “nightvision”
    - “long_nightvision”
    - “invisibility”
    - “long_invisibility”
    - “leaping”
    - “long_leaping”
    - “strong_leaping”
    - “fire_resistance”
    - “long_fire_resistance”
    - “swiftness”
    - “long_swiftness”
    - “strong_swiftness”
    - “slowness”
    - “long_slowness”
    - “strong_slowness”
    - “water_breathing”
    - “long_water_breathing”
    - “healing”
    - “strong_healing”
    - “harming”
    - “strong_harming”
    - “poison”
    - “long_poison”
    - “strong_poison”
    - “regeneration”
    - “long_regeneration”
    - “strong_regeneration”
    - “strength”
    - “long_strength”
    - “strong_strength”
    - “weakness”
    - “long_weakness”
    - “wither”
    - “turtle_master”
    - “long_turtle_master”
    - “strong_turtle_master”
    - “slow_falling”
    - “long_slow_falling”
    - “wind_charged”
    - “weaving”
    - “oozing”
    - “infested”
  - 与“set_potion”功能兼容的物品类型如下：
    - 药水
    - 滞留药水
    - 喷溅药水
    - 箭

## 结构

- 修复了在客户端最初加载包含minecraft:structure_block的服务器世界时，调试边界框渲染的问题。

# 实验性技术更新

## 附加包与脚本引擎

- 在块几何文件中添加了“item_display_transforms”控制。这控制了块在UI、玩家身上和地面上浮动时的视觉表现。它存在于minecraft:geometry JSON对象内部，并需要几何格式版本1.21.0和“即将推出的创作者特性”切换。
  - 默认值示例：
    - "item_display_transforms": { "gui" : { "translation": \[0, 0, 0\], "rotation": \[30, 225, 0\], "scale": \[0.625, 0.625, 0.625\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\], "fit_to_frame" : true }, "firstperson_righthand": { "translation": \[0, 0, 0\], "rotation": \[0, 45, 0\], "scale": \[0.4, 0.4, 0.4\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "firstperson_lefthand": { "translation": \[0, 0, 0\], "rotation": \[0, -135, 0\], "scale": \[0.4, 0.4, 0.4\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "thirdperson_righthand": { "translation": \[0, 2.5, 0\], "rotation": \[75, 45, 0\], "scale": \[0.375, 0.375, 0.375\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "thirdperson_lefthand": { "translation": \[0, 2.5, 0\], "rotation": \[75, 45, 0\], "scale": \[0.375, 0.375, 0.375\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "ground": { "translation": \[0, 3.0, 0\], "rotation": \[0, 0, 0\], "scale": \[0.25, 0.25, 0.25\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "fixed": { "translation": \[0, 0, 0\], "rotation": \[0, 0, 0\], "scale": \[0.5, 0.5, 0.5\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] }, "head": { "translation": \[0, 0, 0\], "rotation": \[0, 0, 0\], "scale": \[1, 1, 1\], "rotation_pivot" : \[0, 0, 0\], "scale_pivot" : \[0, 0, 0\] } }

## API

- PlayerInteractWithBlockBeforeEvent
  - 向beta添加了只读属性isFirstEvent: boolean。如果事件是在玩家初始交互按钮按下时触发，则该值为true；如果是在按住交互按钮时触发，则为false。
- PlayerInteractWithBlockAfterEvent
  - 向beta添加了只读属性beforeItemStack?: ItemStack。这是玩家在交互成功之前选择的物品。
  - 向beta添加了只读属性isFirstEvent: boolean。如果事件是在玩家初始交互按钮按下时触发，则该值为true；如果是在按住交互按钮时触发，则为false。
  - 该后事件现在不再在空手时总是触发。与方块的交互需要成功才能触发后事件。
- PlayerInteractWithEntityAfterEvent
  - 向beta添加了只读属性beforeItemStack?: ItemStack。这是玩家在交互成功之前选择的物品。
  - 取消之前的事件现在将不再触发后事件。
  - 该事件现在仅在成功交互时触发。

## 图形

- 修复了Android Mali设备系列上的各种问题，最显著的是在Deferred Technical Preview中的“条纹阴影”错误（[MCPE-175207](https://bugs.mojang.com/browse/MCPE-175207)）。
- 移除了在插值关键帧值时不正确的偏移量，阳光亮度和阳光颜色的关键帧值现在与其他基于时间的关键帧值一致。创作者需要将任何阳光亮度和颜色关键帧向后移动0.5。关于创作者门户的文档已相应更新。
- 在Deferred Technical Preview中添加了通过纹理集数据驱动次表面散射的能力。该效果允许光线穿透物体的表面到一定程度，类似于蜡、树叶或皮肤。之前在叶子上的默认次表面效果已被移除，以便包提供自己的纹理。创作者可以在其纹理集JSON中使用“metalness_emissive_roughness_subsurface”而不是“metalness_emissive_roughness”来激活特定方块、生物等的效果。次表面值从提供纹理的alpha通道中提取。有关更多信息，请参见创作者门户上的更新文档。
  - 请注意，此新字段仅在格式版本为“1.21.30”的纹理集JSON中可用。
- 更改了Deferred Technical Preview的颜色分级JSON架构，现在要求明确启用高光和阴影特定的颜色分级设置。有关更多信息，请参见创作者门户上的更新文档。
- 向编辑器的Deferred图形设置添加了高光和阴影颜色分级控制。
- 在Deferred Technical Preview中添加了数据驱动的自发光去饱和度的能力。有关更多信息，请参见创作者门户上的更新文档。
- 在Deferred Technical Preview中添加了对附魔物品的支持。
- 减少了在Deferred Technical Preview中启用上采样时，玩家手中挥动物品时出现的模糊或“幽灵”伪影。
- 修复了导致某些物体无法从点光源投射阴影的各种问题，并修改了点光源，使其几何体在Deferred Technical Preview中不再投射阴影。