# 无敌实体

有时你需要创建一个不能被伤害的实体，无论是用于装饰、机制实体，还是不应该被玩家破坏的地图道具。本文介绍两种实现无敌实体的方式。

## 方法一：伤害传感器

这是最灵活、最推荐的方式。`minecraft:damage_sensor`组件允许你用过滤器精确控制哪些伤害来源可以伤害实体，哪些不能。

### 完全无敌

下面的配置会让实体对所有伤害来源都免疫：

```json title="BP/entities/entity.json（components节选）"
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": "no"
    }
}
```

### 仅对玩家免疫

如果你只想阻止玩家伤害实体，而允许其他来源造成伤害：

```json title="BP/entities/entity.json（components节选）"
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            }
        },
        "deals_damage": "no"
    }
}
```

`triggers`还可以是一个数组，从而同时处理多种不同的伤害来源规则。具体字段可参考官方实体组件参考。

## 方法二：最低生命值限制

`minecraft:health`组件的`min`字段可以将实体的最低生命值设为一个不为零的值，使其无法通过正常手段杀死，包括`/kill @e`命令。

```json title="BP/entities/entity.json（components节选）"
"minecraft:health": {
    "value": 1,
    "max": 1,
    "min": 1
}
```

/// warning | 此方法存在隐患
使用`min`锁死生命值的实体很难被彻底清除。如果你使用此方法，**务必**同时提供另一种清除实体的途径。
///

建议的清除方式包括：
- 通过环境传感器或计时器触发`minecraft:instant_despawn`事件
- 通过`/event entity @e[type=wiki:my_entity] wiki:despawn`命令手动触发销毁事件
- 使用脚本API的`Entity.remove()`方法

/// note | 关于生命值为0
将`min`设为`0`可能会破坏死亡动画和某些生成效果，不建议这样做。
///