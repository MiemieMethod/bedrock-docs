# 实体事件与触发器

本页列出国际版官方实体参考中收录的内置实体事件、触发器组件和事件响应动作。实体事件是行为包实体定义中运行时切换组件组、播放效果、设置属性或触发后续事件的主要机制。

## 事件位置

| 位置 | 说明 |
|---|---|
| `minecraft:entity.events` | 声明可被组件、AI意向、生成过程或其他事件响应触发的自定义事件和内置事件处理。 |
| 触发器组件 | 如`minecraft:on_death`、`minecraft:on_hurt`等组件，在特定生命周期或交互条件满足时触发事件。 |
| 事件响应动作 | 在事件体内执行，常见动作为添加组件组、移除组件组、随机选择、顺序执行、播放音效、发射粒子、排队命令和设置实体属性。 |

## 常用响应结构

```json title="实体事件响应示例"
"demo:become_angry": {
  "add": { "component_groups": ["demo:angry"] },
  "remove": { "component_groups": ["demo:calm"] }
}
```

## 列表

| 名称 | 类别 |
|---|---|
| `add` | 事件响应动作：添加组件组 |
| `emit_particle` | 事件响应动作 |
| `emit_vibration` | 事件响应动作 |
| `minecraft:entity_born` | 内置事件 |
| `minecraft:entity_spawned` | 内置事件 |
| `minecraft:entity_transformed` | 内置事件 |
| `minecraft:on_death` | 触发器组件 |
| `minecraft:on_equipment_changed` | 触发器组件 |
| `minecraft:on_friendly_anger` | 触发器组件 |
| `minecraft:on_hurt_by_player` | 触发器组件 |
| `minecraft:on_hurt` | 触发器组件 |
| `minecraft:on_ignite` | 触发器组件 |
| `minecraft:on_prime` | 内置事件 |
| `minecraft:on_start_landing` | 触发器组件 |
| `minecraft:on_start_takeoff` | 触发器组件 |
| `minecraft:on_target_acquired` | 触发器组件 |
| `minecraft:on_target_escape` | 触发器组件 |
| `minecraft:on_wake_with_owner` | 触发器组件 |
| `play_sound` | 事件响应动作 |
| `queue_command` | 事件响应动作 |
| `randomize` | 事件响应动作：按权重随机执行子节点 |
| `remove` | 事件响应动作：移除组件组 |
| `reset_target` | 事件响应动作 |
| `sequence` | 事件响应动作：按顺序执行子节点 |
| `set_entity_property` | 事件响应动作 |
| `set_property` | 事件响应动作 |
| `trigger` | 事件响应动作 |

<!-- md:sortable -->