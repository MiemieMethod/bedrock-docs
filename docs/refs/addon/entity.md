# 实体定义

本页列出国际版行为包实体定义文件的主要结构。实体行为定义存放于行为包的`entities/`目录，根键为`minecraft:entity`；客户端实体定义存放于资源包的`entity/`目录，根键为`minecraft:client_entity`。本页不包含中国版网易ModSDK的实体接口。

## 行为包实体文件

| 字段 | 类型 | 说明 |
|---|---|---|
| `format_version` | 字符串 | 声明定义文件使用的数据格式版本。 |
| `minecraft:entity` | 对象 | 行为包实体定义根对象。 |
| `description` | 对象 | 声明实体标识符、是否可生成、是否可召唤、实验性属性和运行时关联等基本信息。 |
| `components` | 对象 | 声明实体始终拥有的实体组件。 |
| `component_groups` | 对象 | 声明可由事件动态添加或移除的组件组。 |
| `events` | 对象 | 声明实体事件及其响应动作。 |

## `description`

| 字段 | 类型 | 说明 |
|---|---|---|
| `identifier` | 字符串 | 实体的赋命名空间标识符。行为包实体、客户端实体和生成规则通常应使用同一标识符。 |
| `is_spawnable` | 布尔值 | 是否为实体创建刷怪蛋并允许在创造物品栏中生成。 |
| `is_summonable` | 布尔值 | 是否允许通过`/summon`命令生成该实体。 |
| `is_experimental` | 布尔值 | 是否将实体标记为实验性内容。 |
| `runtime_identifier` | 字符串 | 使自定义实体复用某个原版实体的部分运行时行为。该字段应谨慎使用。 |
| `properties` | 对象 | 声明实体属性。属性可供Molang、事件响应和部分组件读写。 |

## 动态结构

`components`中的组件在实体创建时即存在；`component_groups`中的组件组不会自动生效，通常由`events`中的`add`、`remove`、`randomize`、`sequence`等响应动作控制。组件组适合描述年龄、愤怒、驯服、变种、交互状态等会在运行时发生变化的状态。

```json title="行为包实体结构"
{
  "format_version": "1.20.80",
  "minecraft:entity": {
    "description": {
      "identifier": "demo:robot",
      "is_spawnable": true,
      "is_summonable": true
    },
    "components": {},
    "component_groups": {},
    "events": {}
  }
}
```

## 相关参考

- [实体组件](entity-component.md)
- [实体AI意向](entity-ai-goal.md)
- [实体过滤器](entity-filter.md)
- [实体事件与触发器](entity-event.md)
- [客户端实体定义](client-entity.md)
- [生成规则](spawn-rule.md)