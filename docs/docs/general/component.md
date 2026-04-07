# 组件

**组件（Component）**是Minecraft基岩版数据驱动系统中定义游戏对象行为和属性的基本模块。组件以键值对的形式附加到实体、方块或物品的定义上，每个组件控制一个特定方面的功能。

## 概述

组件是基岩版附加包架构中最核心的概念之一。基岩版采用**组合优于继承（Composition over Inheritance）**的设计思想，游戏对象的行为和属性不是通过类继承定义的，而是通过将多个组件附加到对象上进行组合。每个组件封装了一项独立的功能，多个组件组合在一起即构成了游戏对象的完整行为。

例如，一个生物实体可以同时拥有`minecraft:health`组件（赋予其生命值）、`minecraft:physics`组件（赋予其物理运动能力）和`minecraft:behavior.melee_attack`组件（赋予其近战攻击行为），这些组件各自独立但共同定义了该生物的表现。

## 实体组件

实体组件是组件系统中最丰富的一类，涵盖了实体的生命、运动、AI、交互、外观等方方面面。实体组件定义在行为包的实体定义文件中，位于`components`字段下。

### 引擎组件

**引擎组件（Engine Component）**是由游戏引擎提供的内置组件。这些组件的功能由引擎的原生代码实现，附加包只能配置其参数而不能改变其内在行为。引擎组件的标识符均以`minecraft:`命名空间为前缀。

引擎组件按功能可粗略分为以下几类：

- **属性组件**：定义实体的基础属性，如`minecraft:health`（生命值）、`minecraft:collision_box`（碰撞箱）、`minecraft:physics`（物理属性）等。
- **AI意向组件**：定义实体的行为目标，如`minecraft:behavior.melee_attack`（近战攻击）、`minecraft:behavior.follow_owner`（跟随主人）等。标识符通常包含`behavior.`前缀。
- **导航组件**：定义实体的寻路方式，如`minecraft:navigation.walk`（步行导航）、`minecraft:navigation.fly`（飞行导航）等。
- **传感器组件**：定义实体的感知能力，如`minecraft:environment_sensor`（环境感知）、`minecraft:hurt_on_condition`（条件伤害）等。
- **交互组件**：定义实体与玩家之间的交互，如`minecraft:rideable`（可骑乘）、`minecraft:interact`（交互）等。

### 组件组

**组件组（Component Group）**是实体定义中的一种组织机制，允许将一组组件打包成一个命名组，通过事件系统动态地添加或移除。组件组定义在实体定义文件的`component_groups`字段中。

组件组使得实体能够在运行时切换不同的行为集合。例如，一个动物实体可以定义“幼年”和“成年”两个组件组，分别包含不同的碰撞箱尺寸、行为模式和繁殖能力等组件，并通过成长事件在两者之间切换。

当多个组件组中包含同一组件时，后添加的组件组中的同名组件会覆盖先添加的。

## 方块组件

方块组件定义在行为包的方块定义文件中，用于控制自定义方块的行为和属性。方块组件的数量和种类比实体组件少得多，主要包括：

- **基础属性**：如`minecraft:destructible_by_mining`（可被开采）、`minecraft:destructible_by_explosion`（可被爆炸摧毁）、`minecraft:friction`（摩擦力）、`minecraft:light_emission`（光照发射）等。
- **外观属性**：如`minecraft:geometry`（几何体）、`minecraft:material_instances`（材质实例）等。
- **交互属性**：如`minecraft:collision_box`（碰撞箱）、`minecraft:selection_box`（选择箱）等。

方块组件不支持组件组机制，但可以通过方块置换系统为不同的方块状态组合指定不同的组件集。

## 物品组件

物品组件定义在行为包的物品定义文件中，用于控制自定义物品的行为和属性。物品组件包括：

- **基础属性**：如`minecraft:max_stack_size`（最大堆叠数量）、`minecraft:hand_equipped`（手持显示方式）等。
- **使用行为**：如`minecraft:food`（食物属性）、`minecraft:shooter`（射击属性）、`minecraft:throwable`（可投掷）等。
- **外观属性**：如`minecraft:icon`（图标）、`minecraft:display_name`（显示名称）等。
