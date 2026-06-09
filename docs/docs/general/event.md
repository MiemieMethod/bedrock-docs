# 事件

**事件（Event）**是Minecraft基岩版中连接游戏逻辑各环节的通信机制。事件用于通知特定的状态变化或触发预定的行为响应，广泛应用于实体系统、方块系统、脚本API和动画控制器等领域。

## 概述

基岩版的数据驱动架构依赖事件系统来实现灵活的运行时行为控制。通过事件，开发者可以在不修改引擎代码的前提下定义当某种条件满足时应执行的操作。事件通常由游戏引擎内部触发，也可以由附加包中的定义或脚本显式触发。

## 实体事件

实体事件是数据驱动实体系统的核心组成部分。在行为包的实体定义文件中，事件定义在`events`字段下，每个事件由一个赋命名空间标识符标识。

### 事件响应

实体事件被触发时，可以执行以下类型的**事件响应（Event Response）**：

- **`add`**：向实体添加指定的组件组。
- **`remove`**：从实体移除指定的组件组。
- **`set_property`**：设置实体属性的值。
- **`queue_command`**：排列一条待执行的命令。
- **`trigger`**：触发另一个事件。
- **`sequence`**：按顺序执行一系列事件响应。
- **`randomize`**：从一组事件响应中随机选择一个执行，每个选项可指定权重。

### 内置事件

游戏引擎会在特定时机自动触发一些内置事件，常见的包括：

- `minecraft:entity_spawned`：实体首次生成时触发。
- `minecraft:entity_born`：实体通过繁殖出生时触发。
- `minecraft:entity_transformed`：实体发生类型转化时触发。
- `minecraft:on_prime`：TNT被激活时触发。

开发者可以在实体定义中为这些内置事件编写响应逻辑。

### 过滤器

**过滤器（Filter）**是一种用于检测条件的机制，可以在事件触发链路中作为门控。过滤器通过`filters`字段附加在事件响应、环境感知组件或其他需要条件判断的位置。每个过滤器测试由测试名称、目标、运算符和值组成，多个过滤器可以通过`all_of`、`any_of`和`none_of`进行逻辑组合。

## 方块事件

与实体不同，自定义方块并没有长期稳定的数据驱动事件系统。早期版本中，自定义方块曾通过`events`字段定义方块事件，并由`minecraft:on_interact`、`minecraft:on_step_on`、`minecraft:on_placed`等**触发器（Trigger）**组件触发，事件可执行`set_block_state`、`run_command`、`damage`、`decrement_stack`、`die`、`play_effect`、`play_sound`、`teleport`、`transform`等响应。但这套机制始终属于实验性的**假日创作者功能（Holiday Creator Features）**，从未进入稳定接口，并已随格式版本`1.20.80`整体移除。

在现行版本中，自定义方块的事件逻辑改由[脚本API](../addon/script-api.md)承担。方块定义通过`minecraft:custom_components`组件声明其使用的自定义组件，由脚本在`onPlayerInteract`、`onStepOn`、`onPlace`、`onTick`等事件钩子中实现对应行为。换言之，方块的事件响应已从数据驱动的JSON定义迁移到了脚本注册的自定义组件中。<!-- md:flag vanilla -->

## 脚本事件<!-- md:flag vanilla -->

脚本API提供了一套基于发布/订阅模式的事件系统。开发者可以订阅引擎触发的内置事件（如`worldInitialize`、`entityHurt`等），也可以使用`/scriptevent`命令和`system.afterEvents.scriptEventReceive`等接口实现脚本与命令系统之间的事件通信。

脚本事件分为**前置事件（Before Event）**和**后置事件（After Event）**两类。前置事件在引擎执行相应逻辑之前触发，允许取消操作；后置事件在逻辑执行完毕之后触发，用于响应已经发生的变化。

## 动画事件

在动画和动画控制器中，可以通过时间轴定义**动画事件（Animation Event）**。在动画播放到达指定时间点时触发，可以执行命令、触发实体事件或播放音效和粒子特效。动画控制器在状态转移时也可以触发入口事件和退出事件。