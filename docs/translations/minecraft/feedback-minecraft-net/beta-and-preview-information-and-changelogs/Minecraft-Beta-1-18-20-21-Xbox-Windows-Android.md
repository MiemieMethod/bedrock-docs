---
title: Minecraft Beta - 1.18.20.21（Xbox / Windows / Android）
date: 2022-01-27T15:54:04Z
updated: 2022-01-27T16:45:34Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4423151445901-Minecraft-Beta-1-18-20-21-Xbox-Windows-Android
---

**发布于：**2022年1月27日

**参与Minecraft测试版前请阅读：**

- 加入测试版将用Minecraft的开发中版本替换您的游戏
- 在预览测试版期间，您将无法访问Realms，并且无法加入非测试版玩家的游戏
- 在测试版中进行的任何世界无法在游戏的早期版本中打开，请务必备份世界以防丢失
- 测试版构建可能不稳定，无法代表最终版本的质量
- 测试版仅在Xbox、Windows和Android（Google Play）上提供。要加入或退出测试版，请参阅 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

 

![Create_New_World.png](https://feedback.minecraft.net/hc/article_attachments/4423164039309/Create_New_World.png)

 

以下是本周测试版的新功能列表！我们很高兴展示全新的“创建新世界”界面，这将作为可选项提供给部分测试版玩家。我们希望在 [此帖](http://aka.ms/MCCreateNewWorldUI) 中听到您的反馈！如往常一样，请在 [bugs.mojang.com](http://bugs.mojang.com/) 搜索并报告您可能发现的任何漏洞。

 

# **实验性功能**

## **青蛙**

- 青蛙现在跳跃的频率更高
- 青蛙卵重命名为青蛙生成
- 青蛙生成孵化成蝌蚪的时间增加了
- 蝌蚪的击中箱现在更大
- 青蛙生成拥有新的纹理
- 草甸生物群系中的青蛙现在为温带变种

## **动画调整**

- 调整了青蛙的跳跃和舌头动画
- 清理了动画、实体和控制器文件
- 将*水*和游泳动画从线性更改为平滑

# **非实验性功能和漏洞修复**

**创建新世界**

- *创建新世界*界面已进行了新设计，现在部分玩家可以看到。我们希望在 [此帖](http://aka.ms/MCCreateNewWorldUI) 中听到您的反馈！

## **原版趋同**

- 现在可以使用64位种子（-9223372036854775808到9223372036854775807）创建世界，并且这些种子可以在基岩版和Java版之间复制以生成相同的世界（[MCPE-144994](https://bugs.mojang.com/browse/MCPE-144994)）([MCPE-148168](https://bugs.mojang.com/browse/MCPE-148168))
- 非数字种子的用户界面输入现在与Java版生成相同的种子
- 玩家在充能弓时，手臂不再抽搐（[MCPE-148486](https://bugs.mojang.com/browse/MCPE-148486)）
- 下落的方块再次拥有完整的块击中箱
- 修复了工匠牧师在提供荧石粉时错误地提供荧石块的问题（[MCPE-57524](https://bugs.mojang.com/browse/MCPE-57524)）
- 未驯服的狼现在可以被牵引（[MCPE-82050](https://bugs.mojang.com/browse/MCPE-82050)）

## **方块**

- TNT方块在点燃后现在会正确地向随机X/Z方向移动
- 修复了资源掉落在快速破坏并放置方块后偶尔保持黑色的问题
- 顶部雪在下落时不再与下方方块发生碰撞

## **命令**

- 为实体的目标选择器添加了“hasitem”过滤器。这允许玩家根据实体库存中拥有的物品或穿戴的物品来定位实体

## **游戏玩法**

- 修复了来自掠夺者法术的獠牙在没有边界框的方块中无法生成的问题
- 水桶和熔岩桶现在可以在与水共存的水下方块上使用，例如光源方块或大型滴水叶（[MCPE-148392](https://bugs.mojang.com/browse/MCPE-148392)）
- 游客模式下的玩家不能再破坏画作和矿车（[MCPE-132869](https://bugs.mojang.com/browse/MCPE-132869)）
- 垂直传送超过可见距离现在会正确加载地形（[MCPE-150021](https://bugs.mojang.com/browse/MCPE-150021)）
- 提高了伤害计算的准确性
- 修复了在持有可充能物品时与钟互动不会持续响铃的问题（[MCPE-56968](https://bugs.mojang.com/browse/MCPE-56968)）
- 修复了玩家在某些情况下骑乘时可以切换至滑翔的漏洞（[MCPE-147904](https://bugs.mojang.com/browse/MCPE-147904)）

## **生物**

- 生物现在能够在杜鹃树方块上移动（[MCPE-129373](https://bugs.mojang.com/browse/MCPE-129373)）
- 生物现在能够在滴水叶方块上移动，并在未完全倾斜时正确进行路径寻找
- 生物现在能够在小型滴水石锥方块上移动，并在其顶部正确进行路径寻找（[MCPE-133270](https://bugs.mojang.com/browse/MCPE-133270)）
- 生物现在可以在固体的部分方块上正常移动，如钟、酿造台和附魔台
- 生物现在可以从足够高的固体部分方块跳跃到更高位置的完整方块
- 生物现在可以跳过如果它们站在相邻台阶或足够高的其他方块上的栅栏
- 即使天花板（如果有）与生物本身一样高，生物现在也可以通过不到半块高的顶部雪移动（[MCPE-148355](https://bugs.mojang.com/browse/MCPE-148355)）
- 生物现在可以通过珊瑚和珊瑚扇移动，因为它们不再被视为实体的固体障碍物（[MCPE-128687](https://bugs.mojang.com/browse/MCPE-128687)）
- 修复了玩家在持有刷怪蛋时无法访问村民交易的问题（[MCPE-76153](https://bugs.mojang.com/browse/MCPE-76153)）
- 修复了村庄袭击期间生成的女巫可能在袭击期间被毁除的问题（[MCPE-149883](https://bugs.mojang.com/browse/MCPE-149883)）
- 鳕鱼、鲑鱼、河豚、热带鱼和海豚再次在深海生物群系的变种中生成（[MCPE-150191](https://bugs.mojang.com/browse/MCPE-150191)）

## **稳定性和性能**

- 修复了在退出更衣室的缩放菜单时可能发生的崩溃

## **用户界面**

- 口袋用户界面物品栏左侧的默认标签更改为“可制作”，右侧更改为“合成”
- 移除了口袋用户界面物品栏上的问号按钮
- 在未使用工作台时，不再显示需要3x3配方的物品
- 玩家现在可以使用自动移动在口袋用户界面的工作台菜单中脱下或装备盔甲（[MCPE-148970](https://bugs.mojang.com/browse/MCPE-148970)）
- 更新了移动设备上的通用控制器面按钮图标
- 按下Control + Backspace现在会删除插入点之前的整个单词
- 按下Control + Delete现在会删除插入点之后的整个单词
- 按下Control + 左箭头现在会将插入点移动到插入点前一个单词的开头
- 按下Control + 右箭头现在会将插入点移动到插入点后一个单词的开头

### **村民**

- 更新了盔甲匠、牧师、渔夫、牧羊人、工具匠和武器匠的村民交易表，以匹配Java版
- 修复了当玩家用绿宝石交易时，村民不会持有他们将交易的物品的问题（[MCPE-150303](https://bugs.mojang.com/browse/MCPE-150303)）
- 村民不再避开僵尸猪灵（[MCPE-94102](https://bugs.mojang.com/browse/MCPE-94102)）
- 村民不再共享种子和甜菜种子

# **技术更新**

- “StorageVersion” 为8或更低的世界将提升至9，并将其“RandomSeed”从仅使用64位数的低32位升级为使用完整的64位范围，同时仍表示相同的数字。这仅与负的32位种子相关，这些种子需要符号位扩展

## **附加模组能力实验/JavaScript API**

**重要！**在此版本及随后的测试版中，我们将移除附加模组能力实验。此实验包含于2018年推出的实验性JavaScript API，并且随着此移除，与此API相关的世界中的JavaScript将不再功能。GameTest框架——一个独立的JavaScript API——不应受到影响，行为包/资源包类型的附加包也不应受到影响。您可以通过 [此文章](https://aka.ms/mcamc) 了解更多信息。

## **命令**

- 为 '/tickingarea' 命令添加了预加载重载
- 实体现在必须被加载才能使区域被视为完全加载和计时

## **Molang**

- 动画脚本中用于活动对象资源定义的Molang表达式（pre_animation和initialize）包含大写字母时，在format_version 1.18.20或更高版本中现在能够正确评估

## **用户界面**

- 加载进度屏幕现在在加载标记为预加载的常加载区域时显示

# **实验性技术更新**

## **命令**

- 添加了新的 '/volumearea' 命令，用于在世界中创建、移除和列出体积

## **GameTest框架**

新模块！我们添加了一个 **mojang-minecraft-ui** 模块，包含用于创建简单对话框的API结构：

- 在 mojang-minecraft-ui 命名空间中添加了 ActionFormData/ModalFormData/MessageFormData 类型。有关新命名空间的更多文档将显示在 [Minecraft Creator文档网站](https://aka.ms/buildwithminecraft) 上。

mojang-minecraft 模块更新：

- World
  - 在 world.events.beforeItemUseOn 和 world.events.itemUseOn 中更新了属性 directionto blockFace
    - 添加了事件 World.event.beforeDataDrivenEntityTriggerEvent - 在应用数据驱动触发器之前触发
    - 添加了事件 World.event.dataDrivenEntityTriggerEvent - 在应用数据驱动触发器之后触发
    - 对于上述事件，每个事件接受一个可选的 EntityDataDrivenTriggerEventOptions
  - （重大变更）属性 entityremoved
  - 添加了属性 entities: Entity[] - 如果指定，将仅限制为指定的实体
  - 更改了函数 getPlayersto PlayerIterator 的返回类型

- EntityDataDrivenTriggerEventOptions
  - 继承自 EntityEventOptions
  - 属性 eventTypes: string[] - 如果指定，将限制为具有指定名称的事件（例如 minecraft:ageable_grow_up）
  - （继承）属性 entities: Entity[] - 如果指定，将仅限制为指定的实体
  - （继承）属性 entityTypes: string[] - 如果指定，将限制为具有指定类型的实体（例如 minecraft:creeper）

- DefinitionModifier
  - 只读属性 componentGroupsToAdd: string[] - 将作为此修改器一部分添加的组件组列表
  - 只读属性 componentGroupsToRemove: string[] - 将作为此修改器一部分移除的组件组列表
  - 属性 triggers: Trigger[] - 作为此修改器一部分将触发的触发器列表

- Trigger
  - 属性 eventName: string - 触发器的事件名称

- DataDrivenEntityTriggerEvent
  - 只读属性 entity: Entity - 触发事件的实体
  - 只读属性 id: string - 事件的名称

- BeforeDataDrivenEntityTriggerEvent
  - 只读属性 entity: Entity - 触发事件的实体
  - 只读属性 id: string - 事件的名称
  - 属性 modifiers: DefinitionModifier[] - 事件触发时将应用的修改器列表
  - 属性 cancel: bool - 如果为true，事件将不会被触发

- EnchantmentType
  - 添加了 EnchantmentType 类
  - 只读属性 id: string - 魔咒类型的名称
  - 只读属性 maxLevel: int - 此类型魔咒的最大等级

- EnchantmentInstance
  - 添加了 EnchantmentInstance 类。此类代表可以添加到物品上的 EnchantmentType 和等级的绑定
  - 构造函数 EnchantmentInstance(type: EnchantmentType, level: int)
  - 只读属性 type: EnchantmentType - 此实例的魔咒类型
  - 属性 level: int - 此魔咒实例的等级

- EnchantmentSlot
  - 添加了 EnchantmentSlot 枚举。此枚举表示可以应用魔咒的物品槽位或类型

- EnchantmentList
  - 添加了 EnchantmentList 类。此类代表可以应用于物品的一组魔咒
  - 构造函数 EnchantmentList(slot: EnchantSlot)
  - 只读属性 slot: EnchantSlot - 此魔咒集合要应用的物品槽位/类型
  - 只读属性 allEnchantments: EnchantmentInstance[] - 作为此魔咒集合一部分的所有魔咒
  - 方法 canAddEnchantment(instance: EnchantmentInstance): bool - 返回是否可以将提供的 EnchantmentInstance 添加到此集合
  - 方法 addEnchantment(instance: EnchantmentInstance): bool - 尝试将魔咒添加到此集合。如果成功则返回 true
  - 方法 removeEnchantment(type: EnchantmentType) - 如果存在，则从此集合中移除具有类型 type 的 EnchantmentInstance
  - 方法 hasEnchantment(type: EnchantmentType): int - 如果此集合具有类型 type 的 EnchantmentInstance，则返回魔咒的等级。否则返回 0

- ItemEnchantmentComponent
  - 添加了 ItemEnchantmentComponent 物品组件类。

- ItemStack
  - 属性 enchantments: EnchantmentList - 获取当前此 ItemStack 上的魔咒集合的副本。或允许用户设置 ItemStack 的 EnchantmentList
  - 方法 removeAllEnchantments - 移除此 ItemStack 上可能存在的任何魔咒
  - 添加了函数 setLore(loreList: string[]): void - 设置物品的附言文本
  - 添加了函数 getLore(): string[] - 获取物品的附言文本