# 定义事件

**定义事件（Definition Event）**是Minecraft基岩版数据驱动定义中声明的一类事件结构，用于在特定触发条件下执行预设响应。定义事件主要见于实体定义，历史上也曾在实验性的自定义物品和方块数据中出现。

## 概述

定义事件把“触发时机”和“响应内容”分离。组件、动画控制器、脚本或命令可以触发某个事件名；事件本身则在定义文件的`events`字段中描述要添加或移除哪些组件组、是否继续触发其他事件，以及是否按顺序或随机执行多个响应。

实体定义中的事件是最稳定、最常见的定义事件形式。事件键通常是赋命名空间标识符，也可以是游戏引擎预设的内置事件名，例如`minecraft:entity_spawned`。

## 结构

一个实体定义事件通常包含以下内容：

```json title="实体定义事件示例"
{
  "events": {
    "example:become_active": {
      "add": {
        "component_groups": ["example:active"]
      },
      "remove": {
        "component_groups": ["example:inactive"]
      }
    }
  }
}
```

`add`和`remove`字段用于向实体添加或移除组件组。通过组件组，实体可以在运行时切换行为、碰撞、AI意向、属性、传感器和其他数据驱动组件。

## 触发器

**定义触发器（Definition Trigger）**是指向另一个定义事件的结构。它通常包含事件名、目标和可选条件。实体组件中常见的触发器会在条件满足时触发指定事件。

```json
{
  "event": "example:become_active",
  "target": "self"
}
```

`target`用于说明事件应施加到哪个上下文对象上。常见目标包括`self`、`other`、`player`、`target`、`parent`和`baby`等。不同组件和响应可接受的目标集合并不完全相同，应以对应参考为准。

## 顺序与随机

定义事件可以使用`sequence`和`randomize`组织多个子事件：

- `sequence`按数组顺序执行多个子事件。
- `randomize`从数组中随机选择或随机执行子事件，具体权重由子事件的`weight`控制。

```json
{
  "randomize": [
    {
      "weight": 2,
      "trigger": "example:common_result"
    },
    {
      "weight": 1,
      "trigger": "example:rare_result"
    }
  ]
}
```

同一层级同时出现`sequence`和`randomize`时，引擎会优先采用`randomize`并忽略`sequence`，同时在内容日志中报告错误。维护旧文件时，如发现二者并列，应通过内容日志和实际测试确认实际行为，并删除多余的字段。

## 条件

定义事件中的条件通过事件的执行上下文（调用者类型）来确定：实体事件使用过滤器（`filters`字段），物品和方块事件使用Molang表达式（`condition`字段）。早期版本中二者共享同一套解析逻辑，导致物品/方块事件中的`filters`无法生效；此后实体定义事件单独分离为**活动对象定义事件（Actor Definition Event）**，使用专属过滤器系统。

实体定义事件通常通过**过滤器（Filter）**限制响应是否生效。过滤器可以使用`all_of`、`any_of`和`none_of`组合多个测试，以表达逻辑与、逻辑或和逻辑非。

```json
{
  "filters": {
    "test": "is_family",
    "subject": "other",
    "operator": "==",
    "value": "player"
  },
  "trigger": "example:met_player"
}
```

历史上的物品和方块事件结构曾更多使用Molang条件表达式或专用事件响应。现代自定义物品和自定义方块的交互逻辑已经大量转向脚本API自定义组件。新项目不应只依据旧物品、旧方块事件响应示例设计功能。

## 兼容性

定义事件的基础概念仍然是实体数据驱动系统的重要组成部分，但旧资料中的部分事件响应具有明确的历史语境：

- 早期实体事件响应侧重`add`、`remove`、`trigger`、`sequence`和`randomize`。
- 旧版实验性物品和方块事件响应曾包含`run_command`、`damage`、`decrement_stack`、`play_effect`、`play_sound`、`teleport`、`transform_item`等字段，完整列表参见[旧版物品和方块事件响应](../../../refs/addon/legacy-event-response.md)。
- 现代自定义方块和自定义物品通常通过脚本API注册自定义组件，并在组件事件回调中实现逻辑。

维护旧附加包时，可以利用定义事件资料理解旧JSON为什么能够触发行为；编写新附加包时，应优先查阅当前实体参考、方块自定义组件、物品自定义组件和脚本API文档。
