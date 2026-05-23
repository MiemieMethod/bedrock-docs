# Allay API概览

本文列出Allay官方资料中出现的主要插件API主题、常用配置字段和能力边界。Allay是第三方自实现服务端，以下内容均为Allay项目公开或讨论的接口，不是BDS原生能力。

/// warning | 版本提示
Allay的服务端版本、API版本和Minecraft基岩版协议版本相互关联。具体接口签名、类名和可用性应以当前Allay发行版、Javadoc和官方文档为准。
///

## 插件描述文件

Allay插件通常使用`plugin.json`描述元数据。

| 字段 | 类型 | 必要性 | 说明 |
|------|------|--------|------|
| `name` | 字符串 | 必要 | 插件名称。 |
| `entrance` | 字符串 | 必要 | 插件入口类的全限定名。 |
| `authors` | 字符串数组 | 建议 | 插件作者列表。 |
| `version` | 字符串 | 必要 | 插件版本，必须是合法语义化版本。 |
| `api_version` | 字符串 | 可选 | 目标Allay API版本或版本表达式。 |
| `description` | 字符串 | 可选 | 插件描述。 |
| `website` | 字符串 | 可选 | 插件网站。 |
| `dependencies` | 对象数组 | 可选 | 依赖插件名称、版本表达式和是否可选。 |

`api_version`和依赖版本支持常见版本表达式，例如单一版本、NPM风格、CocoaPods风格和Ivy风格表达式。

## 生命周期

| 方法 | 阶段 | 注意事项 |
|------|------|----------|
| `onLoad()` | 插件被加载，服务器尚未完全启动。 | 不应注册监听器、命令和调度任务，也不应访问世界。 |
| `onEnable()` | 插件被启用。 | 适合注册命令、事件监听器和任务。 |
| `onDisable()` | 插件被禁用。 | 适合保存配置、释放资源和清理状态。 |
| `reload()` | 插件显式重载。 | JAR插件默认不可热重载；只有确认安全时才应实现。 |

## 命令树

Allay命令通过继承`Command`并在`prepareCommandTree(CommandTree tree)`中构造命令树。命令节点可以执行回调、添加参数、限制发送者类型、设置节点权限和返回错误。

### 内置参数类型

| 方法 | 结果类型 | 说明 |
|------|----------|------|
| `str(name)` | `String` | 单个词。 |
| `msg(name)` | `String` | 消息文本，可包含空格并消耗剩余参数。 |
| `intNum(name)` | `Integer` | 整数。 |
| `floatNum(name)` | `Float` | 浮点数。 |
| `doubleNum(name)` | `Double` | 双精度浮点数。 |
| `longNum(name)` | `Long` | 长整数。 |
| `shortNum(name)` | `Short` | 短整数。 |
| `bool(name)` | `Boolean` | 布尔值。 |
| `enums(name, values...)` | `String` | 字符串枚举。 |
| `enumsIgnoreCase(name, values...)` | `String` | 忽略大小写的字符串枚举。 |
| `enumClass(name, EnumClass.class)` | 枚举类 | Java枚举类。 |
| `target(name)` | 实体列表 | 实体目标选择器。 |
| `playerTarget(name)` | 实体列表 | 玩家目标选择器。 |
| `wildcardTarget(name)` | `String` | 通配目标。 |
| `pos(name)` | `Vector3d` | 位置参数，支持相对坐标。 |
| `gameMode(name)` | `GameMode` | 游戏模式。 |
| `difficulty(name)` | `Difficulty` | 难度。 |
| `effect(name)` | `EffectType` | 状态效果类型。 |
| `enchantment(name)` | `EnchantmentType` | 魔咒类型。 |
| `itemType(name)` | `ItemType<?>` | 物品类型。 |
| `blockType(name)` | `BlockType<?>` | 方块类型。 |
| `blockPropertyValues(name)` | `List<BlockPropertyValue>` | 方块属性值列表。 |
| `entityType(name)` | `EntityType<?>` | 实体类型。 |
| `remain(name)` | `List<String>` | 剩余参数。 |
| `key(name)` | `String` | 字面量子命令。 |
| `cmd(name)` | `String` | 命令字符串。 |

### 发送者类型

| 类型 | 说明 |
|------|------|
| `SenderType.ANY` | 任意发送者。 |
| `SenderType.PLAYER` | 玩家。 |
| `SenderType.ACTUAL_PLAYER` | 真实玩家，不含假玩家。 |
| `SenderType.ENTITY` | 实体。 |
| `SenderType.SERVER` | 服务器控制台。 |

### 错误输出

| 方法 | 说明 |
|------|------|
| `addNoTargetMatchError()` | 没有实体匹配目标选择器。 |
| `addTooManyTargetsError()` | 匹配实体过多。 |
| `addPlayerNotFoundError()` | 未找到玩家。 |
| `addSyntaxError()` | 当前参数处存在语法错误。 |
| `addInvalidExecutorError(SenderType)` | 命令发送者类型错误。 |
| `addError(message, args...)` | 添加自定义错误消息。 |
| `addOutput(message, args...)` | 添加普通输出消息。 |

## 权限

Allay权限节点使用点号表示树状关系，例如`allay.command.say`。权限值使用`Tristate`表示。

| 值 | 说明 |
|----|------|
| `TRUE` | 显式允许。 |
| `FALSE` | 显式拒绝。 |
| `UNDEFINED` | 未显式设置，通常按拒绝处理。 |

实现`Permissible`的对象可以执行权限检查。Allay默认玩家权限计算器会让操作员拥有全部权限，让非操作员只拥有有限权限。插件也可以替换`PermissionCalculator`实现自定义权限系统。Allay资料还提到Allay平台的LuckPerms支持；安装后它会替换玩家默认权限计算器。

## 事件

事件监听方法使用`@EventHandler`标注，并且应只有一个事件类型参数和`void`返回值。监听器需要注册到事件总线。

Allay存在服务器实例事件总线和世界事件总线。旧线程模型资料说明，世界相关事件应注册到对应世界的事件总线；非世界事件由服务器实例事件总线处理。

## 调度器

| 调度器 | 线程或作用域 | 适用场景 |
|--------|--------------|----------|
| 服务器调度器 | 服务器线程 | 全局、非世界状态任务。 |
| 世界调度器 | 对应世界线程 | 世界级状态，例如时间、天气和世界数据。 |
| 维度调度器 | 维度线程或并行计算线程池 | 维度中的方块、粒子和实体更新。 |
| 实体调度器 | 实体当前维度线程 | 与单个实体生命周期绑定的任务。 |

Allay重复任务以刻为间隔。教程示例中，任务回调返回`true`表示继续运行，返回`false`表示停止。

## 方块API

| 概念 | 说明 |
|------|------|
| `BlockType` | 方块种类，拥有状态集合、属性集合、默认状态和行为。 |
| `BlockState` | 某一方块种类的具体不可变状态。Allay资料说明方块状态可按单例使用`==`比较。 |
| `Block` | 维度中某一位置和层的方块状态包装对象。 |
| `BlockPropertyType` | 方块属性定义。 |
| `BlockBehavior` | 方块逻辑，例如掉落、交互和刻处理。 |
| `BlockTypes` | 原版方块类型的静态引用集合。 |

Allay维度API可读写指定坐标和层的方块状态。基岩版同一位置可有多层方块，教程中将第0层作为主方块层，将第1层作为液体或含水层。

## 物品API

| 概念 | 说明 |
|------|------|
| `ItemStack` | 可持有、存储或掉落的物品实例，包含数量、损坏值、自定义名称、描述和魔咒等数据。 |
| `ItemType` | 物品种类，可创建物品栈并关联`ItemData`。 |
| `ItemTypes` | 原版物品类型的静态引用集合。 |
| `ItemData` | 最大堆叠数、耐久、攻击伤害、护甲值和附魔能力等元数据。 |
| `ItemTag` | 物品分类标签，例如工具、剑、食物和品质标签。 |

Allay物品栈是可变对象。修改共享物品栈前应先复制。

## 容器API

| 类型 | 大小 | 说明 |
|------|------|------|
| `INVENTORY` | 36 | 玩家物品栏。 |
| `ARMOR` | 4 | 玩家盔甲槽。 |
| `OFFHAND` | 1 | 副手槽。 |
| `CHEST` | 27 | 单箱子。 |
| `DOUBLE_CHEST` | 54 | 大箱子。 |
| `BARREL` | 27 | 木桶。 |
| `SHULKER_BOX` | 27 | 潜影盒。 |
| `ENDER_CHEST` | 27 | 末影箱。 |
| `FURNACE` | 3 | 熔炉。 |
| `BREWING_STAND` | 5 | 酿造台。 |
| `ANVIL` | 3 | 铁砧。 |
| `CRAFTING_TABLE` | 9 | 工作台。 |
| `FAKE_CHEST` | 27 | 伪箱子容器。 |
| `FAKE_DOUBLE_CHEST` | 54 | 伪大箱子容器。 |

伪容器用于创建自定义GUI。Allay资料特别提示，伪容器应使用`addPlayer()`显示给玩家，因为该方法会在打开容器前处理客户端所需的伪方块。

## 表单API

| 类型 | 说明 |
|------|------|
| 简单表单 | 显示文本和多个按钮，适合菜单。 |
| 模态表单 | 显示两个按钮，适合确认或二选一。 |
| 自定义表单 | 支持输入框、下拉菜单、开关、滑块、步进滑块、标签、标题和分隔线。 |

自定义表单响应按元素添加顺序返回。标签、标题和分隔线不产生响应，但仍会影响编者对索引的理解，处理回调时应显式记录可响应元素顺序。

## Boss栏API

| 属性 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `title` | 字符串 | `""` | Boss栏文本。 |
| `progress` | `float` | `1.0` | 进度，范围为0至1。 |
| `color` | `BossBarColor` | `PINK` | 颜色。 |
| `style` | `BossBarStyle` | `SOLID` | 分段样式。 |
| `darkenSky` | 布尔值 | `false` | 是否加深天空。 |

颜色包括`PINK`、`BLUE`、`RED`、`GREEN`、`YELLOW`、`PURPLE`、`REBECCA_PURPLE`和`WHITE`。样式包括`SOLID`、`SEGMENTED_6`、`SEGMENTED_10`、`SEGMENTED_12`和`SEGMENTED_20`。

## 记分板API

Allay记分板可以设置行内容并添加或移除查看者。显示槽位包括：

| 槽位 | 说明 |
|------|------|
| `SIDEBAR` | 屏幕右侧，常用于动态信息。 |
| `LIST` | 在线玩家列表。 |
| `BELOW_NAME` | 玩家名称标签下方。 |

## 配置API

| 格式 | 扩展名 | 说明 |
|------|--------|------|
| YAML | `.yml`、`.yaml` | 推荐用于复杂配置，支持嵌套结构和注释。 |
| JSON | `.json`、`.js` | 适合与其他系统交换数据。 |
| Properties | `.properties`、`.cnf` | 简单键值对。 |
| Enum | `.txt`、`.list`、`.enum` | 每行一个值。 |

`Config`支持按点号访问嵌套键、读取列表、读取配置节、保存、重载、删除键和类型检查。

## 国际化

Allay国际化系统使用翻译键。插件语言文件位于JAR内的`assets/lang/`目录，文件名形如`en_US.json`、`zh_CN.json`。翻译键建议使用插件命名空间，例如`myplugin:greeting.welcome`。

| 占位符 | 说明 |
|--------|------|
| `%1`、`%2`、`%3` | 有序参数，推荐使用。 |
| `%s` | 无序字符串参数。 |
| `%d` | 无序数字参数。 |

旧语言文件资料说明，Allay还会从`%`开始识别翻译键，并在遇到非法字符时停止；连续两个冒号会使键不被视作有效翻译键。

## 持久化数据容器

**持久化数据容器（Persistent Data Container）**，简称PDC，用于在Allay对象上保存插件自定义数据。资料列出的持有者包括世界、实体、方块实体和物品栈。

| 类型 | 说明 |
|------|------|
| `Byte`、`Byte Array` | 字节和字节数组。 |
| `Short`、`Integer`、`Integer Array`、`Long`、`Long Array` | 整数类型。 |
| `Float`、`Double` | 浮点类型。 |
| `String` | 字符串。 |
| `Boolean` | 布尔值。 |
| `PersistentDataContainer` | 嵌套容器。 |
| `List` | 由其他持久化数据类型包装的列表。 |

数据不会在不同持有者之间自动复制。例如，将一个物品栈放置为带方块实体的方块时，其PDC数据不会自动迁移到方块实体。

## 自定义方块定义

高级自定义方块API使用`CustomBlockDefinitionGenerator`为每个`BlockState`生成客户端渲染定义。该API要求访问服务端模块，具有内部API风险。

| 工厂方法 | 说明 |
|----------|------|
| `of(Function<BlockState, BlockStateDefinition>)` | 按方块状态返回不同定义。 |
| `ofConstant(BlockStateDefinition)` | 所有状态使用同一定义。 |
| `ofTexture(String)` | 使用单一纹理的简单方块。 |

`BlockStateDefinition`可包含几何体、材质、变换和显示名称。几何体可设置骨骼可见性、剔除规则、剔除图层和UV锁定。材质实例可设置渲染方法、面暗化、环境光遮蔽、随机UV旋转和纹理变种。

## 自定义物品定义

高级自定义物品API使用`CustomItemDefinitionGenerator`生成客户端物品定义。该API也要求访问服务端模块。

| 属性 | 类型 | 说明 |
|------|------|------|
| `texture` | 字符串 | 资源包中的物品纹理名，必需。 |
| `displayName` | 字符串 | 物品栏显示名。 |
| `renderOffsets` | `RenderOffsets` | 手持时的位置、旋转和缩放。 |
| `foil` | 布尔值 | 是否总是显示附魔光泽。 |
| `canDestroyInCreative` | 布尔值 | 创造模式中是否可破坏方块。 |
| `allowOffHand` | 布尔值 | 是否可放入副手。较新Allay变更记录提示应改用`ItemTags.ALLOW_OFFHAND`。 |
| `cooldown` | 整数 | 使用冷却秒数。 |
| `customProperties` | 映射 | 自定义NBT属性。 |
| `customComponents` | 映射 | 自定义基岩版组件。 |
生成器会按物品组件自动识别盔甲、工具、食物和有耐久物品，并写入相应客户端属性。自定义物品仍需要资源包提供对应纹理。
生成器会按物品组件自动识别盔甲、工具、食物和有耐久物品，并写入相应客户端属性。自定义物品仍需要资源包提供对应纹理。
