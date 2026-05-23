# 船型实体

本文介绍如何制作能浮在水面上的船型实体，使其支持骑乘和玩家控制。

/// warning | 格式版本限制
以下介绍的`minecraft:behavior.rise_to_liquid_level`和`minecraft:buoyant`两种方法，**仅在格式版本1.16.100或更低版本下有效**。若使用更高的格式版本，这两个组件将不起作用。目前在高版本中实现浮力效果的替代方案尚不成熟，建议使用运行时标识符方案或等待官方提供新组件。
///

## 方法一：运行时标识符

使用`minecraft:boat`作为运行时标识符可以继承原版船的硬编码行为，包括浮力、碰撞箱等。更多内容参见[运行时标识符](../../../docs/addon/entity.md)文档。

**缺点**：船始终朝北，不随玩家旋转。

## 方法二：rise_to_liquid_level

`minecraft:behavior.rise_to_liquid_level`组件让实体漂浮在液体表面——原版用于炽足兽漂浮在熔岩上，我们可以将其用于水面。

```json title="BP/entities/boat.json"
{
    "format_version": "1.14.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:boat",
            "is_summonable": true,
            "is_spawnable": true
        },
        "components": {
            "minecraft:behavior.rise_to_liquid_level": {
                "priority": 0,
                "liquid_y_offset": 0.5,
                "rise_delta": 0.05,
                "sink_delta": 0.05
            },
            "minecraft:underwater_movement": {
                "value": 5
            },
            "minecraft:navigation.walk": {
                "can_sink": false
            },
            "minecraft:rideable": {
                "seat_count": 1,
                "family_types": ["player"],
                "interact_text": "action.interact.enter_boat",
                "seats": {
                    "position": [0, 0, 0]
                }
            },
            "minecraft:input_ground_controlled": {},
            "minecraft:health": {
                "value": 10,
                "max": 10
            },
            "minecraft:movement": {
                "value": 3
            },
            "minecraft:movement.basic": {},
            "minecraft:collision_box": {
                "width": 1,
                "height": 1
            },
            "minecraft:physics": {}
        }
    }
}
```

关键组件说明：
- `liquid_y_offset`：调整实体浮在水面的高度
- `rise_delta`/`sink_delta`：控制上浮/下沉的速度，可以模拟波浪起伏效果
- `minecraft:navigation.walk`中的`can_sink: false`：**必须添加**，否则实体会下沉
- `minecraft:input_ground_controlled`：让玩家可以用移动键控制实体

## 方法三：buoyant

`minecraft:buoyant`组件提供了更细粒度的浮力控制。

```json title="BP/entities/boat.json > components"
"minecraft:buoyant": {
    "apply_gravity": true,
    "base_buoyancy": 1.0,
    "simulate_waves": true,
    "big_wave_probability": 0.03,
    "big_wave_speed": 10.0,
    "drag_down_on_buoyancy_removed": 0,
    "liquid_blocks": ["water"]
}
```

关键字段说明：
- `base_buoyancy`：0到1之间，控制实体浮在水面的高度
- `simulate_waves`：是否模拟波浪起伏
- `big_wave_probability`：大波浪出现的概率
- `liquid_blocks`：可以浮在哪种液体上（`water`或`lava`）

其余组件（速度、导航、骑乘等）与方法二相同。

## 如何选择

| 比较项 | rise_to_liquid_level | buoyant |
|---|---|---|
| 禁用波浪效果 | 容易（调小`rise_delta`） | 不完全（`simulate_waves: false`仍有残留） |
| 波浪控制精细度 | 一般 | 高 |
| 推荐场景 | 可移动的船型实体 | 静态浮标等固定场景 |
