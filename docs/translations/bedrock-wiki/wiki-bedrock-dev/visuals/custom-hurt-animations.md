---
title: 受伤动画
tags:
    - 中级
mentions:
    - MedicalJewel105
category: 教程
description: 教程：如何在实体受伤时触发自定义动画。
---

本指南将教你如何为实体触发自定义受伤动画。
目前并没有很好的方法来制作自定义受伤动画（至少我所知是这样）。

## BP 实体部分

首先，你需要设置实体文件。确保使用支持属性的文件版本。

在实体描述中添加以下内容：

```json title="BP/entity/my_entity.json#description"
"properties": {
    "wiki:is_hurt": {
        "client_sync": true, // 以便我们可以在资源包中使用
        "type": "bool",
        "default": false
    }
}
```

在组件组中添加以下内容：

```json title="BP/entity/my_entity.json#component_groups"
"wiki:hurt_group": {
    "minecraft:timer": {
        "time": 0.1,
        "time_down_event": {
            "event": "wiki:on_not_hurt_event"
        }
    }
}
```

添加此组件组和切换属性的事件：

```json title="BP/entity/my_entity.json#events"
"wiki:on_hurt_event": {
    "set_property": {
        "wiki:is_hurt": true
    },
    "add": {
        "component_groups": [
            "wiki:hurt_group"
        ]
    }
},
"wiki:on_not_hurt_event": {
    "remove": {
        "component_groups": [
            "wiki:hurt_group"
        ]
    },
    "set_property": {
        "wiki:is_hurt": false
    }
}
```

要调用此事件，请在组件中添加 `damage_sensor`：

```json title="BP/entity/my_entity.json#components"
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "on_damage": {
            "event": "nubs:on_hurt_event"
        }
    }
}
```

## RP AC 部分

你可以通过以下方式过渡到带有受伤动画的状态：`"damage_state": "q.property('wiki:is_hurt')"`，然后使用 `"default": "q.all_animations_finished"`。

这对于创建自定义船只可能会很有用。