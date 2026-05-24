# 实体定义

**实体定义（Entity Definition）**是附加包中描述自定义实体身份、行为与表现的数据驱动文件集合。它由**行为包（Behavior Pack）**中的服务端实体定义和**资源包（Resource Pack）**中的客户端实体定义共同构成，并可与生成规则共同决定实体在世界中的出现方式与运行特征。

## 概述

实体定义不是单一文件，而是一组围绕同一赋命名空间标识符协同工作的定义：

- 行为包`entities/`目录中的`minecraft:entity`用于描述服务端逻辑。
- 资源包`entity/`目录中的`minecraft:client_entity`用于描述客户端渲染。
- 行为包`spawn_rules/`目录中的`minecraft:spawn_rules`用于描述自然生成条件。

三者通常以同一标识符关联。移除其中任一部分不会直接删除另外两部分，但会导致对应能力缺失。

## 服务端实体定义

服务端定义用于组织实体运行时逻辑，核心由**组件（Component）**、**组件组（Component Group）**和**事件（Event）**构成：

- `components`用于声明实体始终存在的能力。
- `component_groups`用于声明可被动态切换的能力集合。
- `events`用于在条件满足时添加或移除组件组，或执行其他事件响应动作。

这种结构使实体能够在同一生命周期内切换形态、状态和行为，而无需切换实体标识符。

## 客户端实体定义

客户端定义用于绑定模型、纹理、材质、动画和渲染控制器，并决定实体在不同条件下的视觉表现。客户端定义通常通过短名称映射组织资源，并在渲染控制器与脚本中按条件选择实际资源。

客户端定义不负责服务端判定逻辑；它主要解决“如何显示”，而非“如何行动”。

## 运行时标识符

`runtime_identifier`用于让自定义实体复用某个原版实体的硬编码行为。该能力可用于快速获得特定底层机制，但也会引入兼容性风险，例如碰撞箱被强制覆盖、交互逻辑异常或在特定版本触发崩溃。

运行时标识符适合用于受控场景验证，不适合作为跨版本稳定能力的唯一依赖。详见[运行时标识符参考](../../refs/addon/runtime-identifier.md)。

## 虚拟组件

**虚拟组件（Dummy Component）**是指仅用于存储数据的组件。此类组件本身不产生任何游戏行为，但其携带的值可通过Molang查询函数读取，从而驱动动画、渲染控制器或过滤器中的条件逻辑。虚拟组件是在不使用脚本的情况下为实体附加可查询状态的常用手段。

虚拟组件分为两类：

- **整数型**：存储一个整数值，适合表达变种、皮肤编号等多状态信息。
- **布尔型（位型）**：通过该组件是否被添加到实体上来表达真/假状态。

下表列出了常见的虚拟组件及其对应的Molang查询：

| 类型 | 查询函数 | 组件 | 备注 |
| --- | --- | --- | --- |
| 整数 | `query.variant` | `minecraft:variant` | |
| 整数 | `query.mark_variant` | `minecraft:mark_variant` | |
| 整数 | `query.skin_id` | `minecraft:skin_id` | |
| 整数 | 过滤器测试`is_color` | `minecraft:color` | 同时影响材质颜色通道 |
| 整数 | 无已知查询（可用`has_component`检测） | `minecraft:color2` | 同时影响材质颜色通道 |
| 布尔 | `query.is_illager_captain` | `minecraft:is_illager_captain` | |
| 布尔 | `query.is_baby` | `minecraft:is_baby` | 添加后会禁用`minecraft:breedable`组件 |
| 布尔 | `query.is_sheared` | `minecraft:is_sheared` | |
| 布尔 | `query.is_saddled` | `minecraft:is_saddled` | |
| 布尔 | `query.is_tamed` | `minecraft:is_tamed` | |
| 布尔 | `query.is_chested` | `minecraft:is_chested` | 实体死亡时会掉落箱子 |
| 布尔 | `query.is_powered` | `minecraft:is_charged` | |
| 布尔 | `query.is_stunned` | `minecraft:is_stunned` | |
| 布尔 | `query.can_climb` | `minecraft:can_climb` | 允许实体攀爬梯子 |
| 布尔 | `query.can_fly` | `minecraft:can_fly` | 寻路器不限制实体必须沿有地面的路径 |
| 布尔 | `query.can_power_jump` | `minecraft:can_power_jump` | 允许实体像马一样蓄力跳跃 |
| 布尔 | `query.is_ignited` | `minecraft:is_ignited` | |

`minecraft:color`与`minecraft:color2`的合法值为颜色名称字符串：`black`、`blue`、`brown`、`cyan`、`gray`、`green`、`light_blue`、`light_green`、`magenta`、`orange`、`pink`、`purple`、`red`、`silver`、`white`、`yellow`。

## 实体属性与动态置换

实体可通过`description.properties`声明**实体属性（Entity Property）**，并在事件、过滤器和Molang表达式中读写。属性常用于表达实体的阶段状态、变种状态和脚本协同状态。

实体还可使用动态置换结构按条件附加组件，从而在不改变标识符的前提下实现状态化能力切换。

## 与生成规则的关系

生成规则只控制实体是否自然生成及其生成条件，不定义实体生成后的行为与表现。实体定义与生成规则应保持标识符一致，以避免“可召唤但不自然生成”或“可自然生成但渲染缺失”等配置不一致问题。

## 参考

- [实体定义参考](../../refs/addon/entity.md)
- [运行时标识符参考](../../refs/addon/runtime-identifier.md)
- [客户端实体定义参考](../../refs/addon/client-entity.md)
- [实体组件参考](../../refs/addon/entity-component.md)
- [实体事件与触发器参考](../../refs/addon/entity-event.md)
- [生成规则参考](../../refs/addon/spawn-rule.md)
