# 基岩版存档格式——其他数据格式

/// details-info | 来源信息
- 原文仓库：[中文Minecraft Wiki](https://zh.minecraft.wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[基岩版存档格式/其他数据格式 - 中文Minecraft Wiki](https://zh.minecraft.wiki/w/基岩版存档格式/其他数据格式)
- 作者或组织：Minecraft Wiki 编者
- 许可：[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
///

本页面介绍基岩版存档中其他数据格式的NBT结构。

## 命令方块

命令方块和命令方块矿车的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|string|Command}}：命令方块内的命令。
    - {{nbt|int|Version}}：数据版本。
    - {{nbt|int|SuccessCount}}：成功次数，表示红石比较器输出的信号强度。
    - {{nbt|string|CustomName}}：命令方块的自定义名称，显示在方块顶部以及GUI内。
    - {{nbt|string|LastOutput}}：由命令方块最新的一行输出的本地化键名。在游戏规则`commandBlockOutput`被设置为false时仍会储存。在命令方块的GUI中显示。
    - {{nbt|list|LastOutputParams}}：输出的本地化字符串的参数列表。
        - {{nbt|string}}：具体参数。
    - {{nbt|boolean|TrackOutput}}：用于决定是否储存`LastOutput`。可以在命令方块UI内的"上一个输出"旁边的按钮进行控制。
    - {{nbt|long|LastExecution}}：存储命令方块最后一次执行命令的时间。
    - {{nbt|int|TickDelay}}：执行每次命令的间隔时间（刻）。
    - {{nbt|boolean|ExecuteOnFirstTick}}：在保存或激活后在首个刻执行命令时为true。
///

## 刷怪笼

刷怪笼的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|string|EntityIdentifier}}：将要生成的实体的ID。
    - {{nbt|short|Delay}}：在下次生成前的冷却时间（刻）。设为0会导致玩家进入刷怪范围后立即生成实体。
    - {{nbt|short|MinSpawnDelay}}：下一次生成冷却时间的最小随机冷却时间值。
    - {{nbt|short|MaxSpawnDelay}}：下一次生成冷却时间的最大随机冷却时间值。
    - {{nbt|short|SpawnCount}}：每次生成的实体数。
    - {{nbt|short|MaxNearbyEntities}}：允许的附近相同实体的最大数量（`SpawnRange`* 2 + 1 × `SpawnRange`* 2 + 1 × 8的范围，以刷怪笼为中心）。
    - {{nbt|short|RequiredPlayerRange}}：当玩家激活此刷怪笼时覆盖的球形范围。
    - {{nbt|short|SpawnRange}}：刷怪笼尝试随机放置生物的范围半径。范围是方形的，且中心定于为刷怪笼的X和Z坐标的随机附近，而不是刷怪笼的位置。默认值为4。
    - {{nbt|float|DisplayEntityWidth}}：刷怪笼内显示的实体的宽度。
    - {{nbt|float|DisplayEntityHeight}}：刷怪笼内显示的实体的高度。
    - {{nbt|float|DisplayEntityScale}}：刷怪笼内显示的实体的大小。
    - {{nbt|compound|SpawnData}}：（可能不存在）包含在生成后复制到下一个生成的实体的标签。
        - {{nbt|compound|Properties}}：属性组件。
        - {{nbt|string|TypeId}}：实体的命名空间ID。
        - {{nbt|int|Weight}}：与其他生成权重相比，该生成被选中的概率。必须为正且至少为1。
    - {{nbt|list|SpawnPotentials}}：（可能不存在）允许生成的实体的列表。
        - {{nbt|compound}}：下一次生成。
            - {{nbt|compound|Properties}}：属性组件。
            - {{nbt|string|TypeId}}：实体的命名空间ID。
            - {{nbt|int|Weight}}：与其他生成权重相比，该生成被选中的概率。必须为正且至少为1。
///

## 烟花火箭爆裂

烟花火箭和烟火之星的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|boolean|FireworkTrail}}：爆裂是否有轨迹效果（钻石）。
    - {{nbt|boolean|FireworkFlicker}}：爆裂是否有闪烁效果（荧石粉）。
    - {{nbt|byte|FireworkType}}：爆裂的形状。0为小型爆裂，1为大型爆裂，2为星型爆裂，3为苦力怕型爆裂，4为炸裂效果。
    - {{nbt|byte-array|FireworkColor}}：对应于烟花爆裂的基本颜色的字节值数组。
    - {{nbt|byte-array|FireworkFade}}：对应于烟花爆裂的渐变颜色的字节值数组。
///

## 属性

生物的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|list}}：属性列表。
        - {{nbt|compound}}：单个属性。（参见[单个属性](#单个属性)）
///

## 单个属性

单个属性NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|string|Name}}：属性名称。
    - {{nbt|float|Base}}：属性的基础值。
    - {{nbt|float|DefaultMin}}：默认的最小值。
    - {{nbt|float|DefaultMax}}：默认的最大值。
    - {{nbt|float|Min}}：调整后的最小值。
    - {{nbt|float|Max}}：调整后的最大值。
    - {{nbt|float|Current}}：当前值。
    - {{nbt|list|Modifiers}}：（可能不存在）修饰符列表。
        - {{nbt|compound}}：单个修饰符。（参见[属性修饰符](#属性修饰符)）
    - {{nbt|list|TemporalBuffs}}：增益/减益的列表。
        - {{nbt|float|Amount}}：数量。
        - {{nbt|int|Duration}}：持续时间。
        - {{nbt|int|LifeTime}}：总时间。
        - {{nbt|int|Type}}：类型。
///

## 属性修饰符

属性修饰符的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|string|Name}}：修饰符的名称。
    - {{nbt|float|Amount}}：此修饰符在计算中修改基础值的值。
    - {{nbt|int|Operation}}：定义此修饰符对属性的基础值执行的操作。0为按照`Amount`的值增加X，1为按照`Amount`的值增加X * `Amount`，2为 Y = Y * (1 + `Amount`)，相当于按照Y * `Amount`增加Y的值。
    - {{nbt|int|Operand}}：未知。
    - {{nbt|long|UUIDMost}}：修饰符的UUID前半部分。
    - {{nbt|long|UUIDLeast}}：修饰符的UUID后半部分。
///

## 生物效果

状态效果的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|byte|Id}}：状态效果的数字ID。
    - {{nbt|byte|Amplifier}}：效果的等级。0为I级效果。
    - {{nbt|int|Duration}}：效果的持续时间（刻）。
    - {{nbt|int|DurationEasy}}：简单模式下的持续时间。
    - {{nbt|int|DurationNormal}}：普通模式下的持续时间。
    - {{nbt|int|DurationHard}}：困难模式下的持续时间。
    - {{nbt|boolean|Ambient}}：该效果是否由信标给予，用于减少屏幕干扰。
    - {{nbt|boolean|ShowParticles}}：是否显示粒子。
    - {{nbt|boolean|DisplayOnScreenTextureAnimation}}：是否在屏幕上显示该状态效果的图标动画（被不祥之兆和村庄英雄使用）。
///

## 方块

方块的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|string|name|required=1|existonsave=1}}：方块的命名空间ID。
    - {{nbt|compound|states|required=1|existonsave=1}}：方块的方块状态列表。
        - {{nbt|any|<state_name>}}：方块状态及其对应数据类型的值。
    - {{nbt|short|val}}：方块的旧版数据值。
    - {{nbt|int|version|existonsave=1}}：数据版本。
///

## 玩家能力

玩家的能力NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|compound|abilities}}：玩家的能力设定。
        - {{nbt|boolean|build}}：玩家是否能放置方块。
        - {{nbt|boolean|mine}}：玩家是否能挖掘方块。
        - {{nbt|boolean|doorsandswitches}}：玩家是否能打开或关闭门、拉杆等方块。
        - {{nbt|boolean|opencontainers}}：玩家是否能打开容器（例如箱子）。
        - {{nbt|boolean|attackplayers}}：玩家是否能攻击其他玩家。
        - {{nbt|boolean|attackmobs}}：玩家是否能攻击生物。
        - {{nbt|boolean|op}}：玩家是否为管理员。
        - {{nbt|boolean|teleport}}：玩家是否能使用`/teleport`命令。
        - {{nbt|boolean|invulnerable}}：玩家是否无敌。
        - {{nbt|boolean|flying}}：玩家是否处于飞行状态。
        - {{nbt|boolean|mayfly}}：玩家是否能飞行。
        - {{nbt|boolean|instabuild}}：玩家是否能瞬间破坏方块。
        - {{nbt|boolean|lightning}}：玩家是否能被闪电劈中。
        - {{nbt|float|flySpeed}}：玩家的飞行速度。
        - {{nbt|float|walkSpeed}}：玩家的移动速度。
        - {{nbt|boolean|mute}}：玩家是否被禁言。
        - {{nbt|boolean|worldbuilder}}：（仅教育版）玩家是否拥有世界建造者权限。
        - {{nbt|boolean|noclip}}：玩家是否无碰撞箱。
        - {{nbt|int|permissionsLevel}}：世界主人的权限等级。
        - {{nbt|int|playerPermissionsLevel}}：其他玩家的权限等级。
        - {{nbt|boolean|<s>buildandmine</s>}}：不再使用。玩家是否可以放置和挖掘方块。
///

## 兴趣点

兴趣点的NBT结构文件：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|list|POI|existonsave=1}}：兴趣点的数据。
        - {{nbt|compound}}：组成兴趣点的组件，每个村民都拥有。
            - {{nbt|long|VillagerID|required=1|existonsave=1}}：村民实体的唯一ID。
            - {{nbt|list|instances|existonsave=1}}：兴趣点实例。
            - {{nbt|compound|0|existonsave=1}}：实例下的第一个组件，用于控制村民认领的床。通常有13个条目，但在没有认领时只含有1个{{nbt|boolean|Skip}}标签。
                - {{nbt|boolean|Skip|required=1|existonsave=1}}：兴趣点是否有效，值为`true`时表示无效，读取时将跳过以下所有标签。
                - {{nbt|int|X}}：兴趣点的X轴坐标。
                - {{nbt|int|Y}}：兴趣点的Y轴坐标。
                - {{nbt|int|Z}}：兴趣点的Z轴坐标。
                - {{nbt|int|Type}}：兴趣点的类型。0为床，1为钟，2为工作站点方块，如果读取至此时发现当前村民在当前坐标已经认领过当前类型的兴趣点了，则以下标签都不会再被读取。
                - {{nbt|string|Name}}：兴趣点的适用对象。工作站点方块为村民的职业名称，床和钟则总是为`villager`。
                - {{nbt|string|InitEvent}}：兴趣点的初始化事件，村民认领后会在村民实体上触发该事件。工作站点方块为`minecraft:become_<村民的职业>`，床和钟则为空。如果该值为空且村庄版本为`Base`（0），则会根据{{nbt|string|Name}}自动推导正确的初始化事件。
                - {{nbt|boolean|UseAABB}}：兴趣点是否使用了轴对齐边界框（AxisAlignedBoundingBox）。
                - {{nbt|float|Radius}}：兴趣点的运作范围。床为0.75，钟为7，工作站点方块为2。
                - {{nbt|long|OwnerCount}}：兴趣点的拥有者的数量。床和单个工作站点方块为1，钟为无限多。
                - {{nbt|long|Capacity}}：兴趣点可容纳的对象的数量限制，和{{nbt|long|OwnerCount}}相同。
                - {{nbt|long|Weight}}：兴趣点的权重。床和钟总为1，工作站点方块为1-8不等的数值。
                - {{nbt|string|SoundEvent}}：兴趣点的声音事件。工作站点方块的声音事件见村民音效条目，床和钟则总是为`undefined`。
            - {{nbt|compound|1|existonsave=1}}：实例下的第二个组件，结构与上述第一个组件相同，用于控制村民认领的钟。通常有13个条目，但在没有认领时只含有1个{{nbt|boolean|Skip}}标签。
            - {{nbt|compound|2|existonsave=1}}：实例下的第三个组件，结构与上述第一个组件相同，用于控制村民认领的工作站点方块。通常有13个条目，但在没有认领时只含有1个{{nbt|boolean|Skip}}标签。
///
