# 可投掷物品

本篇介绍如何制作一种可以投掷的自定义物品——类似雪球，投掷后生成一个飞行实体，落地时产生自定义效果。

## 物品定义

```json title="BP/items/my_bomb.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:my_bomb",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:icon": "wiki:my_bomb",
            "minecraft:max_stack_size": 16,
            "minecraft:throwable": {
                "do_swing_animation": true,
                "launch_power_scale": 1.0,
                "max_launch_power": 1.0,
                "min_launch_power": 1.0,
                "default_facing_direction": "overhand"
            },
            "minecraft:projectile": {
                "projectile_entity": "wiki:my_bomb_projectile",
                "minimum_critical_power": 1.0
            }
        }
    }
}
```

/// define
`minecraft:throwable`

- 让物品可以被"扔出"，按住使用键蓄力，松开后投掷。
    - `do_swing_animation`：是否播放手臂挥舞动画。
    - `launch_power_scale`/`max_launch_power`/`min_launch_power`：控制投掷力度的缩放与范围。
    - `default_facing_direction`：投掷方向，`overhand`为正常过顶抛出。

`minecraft:projectile`

- 指定投掷后生成的弹射物实体标识符。`minimum_critical_power`为1.0时，满蓄力才算暴击。
///

## 弹射物实体定义

在行为包中创建弹射物实体。弹射物需要使用`minecraft:snowball`作为运行时标识符，以继承弹射物运动逻辑：

```json title="BP/entities/my_bomb_projectile.json"
{
    "format_version": "1.21.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:my_bomb_projectile",
            "is_spawnable": false,
            "is_summonable": false,
            "is_experimental": false,
            "runtime_identifier": "minecraft:snowball"
        },
        "components": {
            "minecraft:projectile": {
                "on_hit": {
                    "impact_damage": {
                        "damage": 3
                    },
                    "spawn_chance": {
                        "first_spawn_percent_chance": 100,
                        "second_spawn_percent_chance": 0,
                        "first_spawn_count": 1,
                        "second_spawn_count": 0,
                        "spawn_definition": "minecraft:tnt"
                    },
                    "remove_on_hit": {}
                },
                "power": 1.5,
                "gravity": 0.05,
                "liquid_inertia": 0.6,
                "angle_offset": 0
            },
            "minecraft:physics": {},
            "minecraft:collision_box": {
                "width": 0.25,
                "height": 0.25
            }
        }
    }
}
```

`minecraft:projectile.on_hit`定义命中时的行为：

/// define
`impact_damage`

- 对命中实体造成指定伤害。

`spawn_chance`

- 命中时以指定概率生成实体（此例在命中点生成TNT）。

`remove_on_hit`

- 命中后立即移除弹射物实体。

`arrow_effect`

- 当弹射物命中生物时，给予药水状态效果（需要实体有`minecraft:arrow`的相关特性）。

`teleport_owner`

- 将投掷者传送至命中位置（末影珍珠效果）。
///

## 客户端实体定义

弹射物实体还需要资源包中的客户端实体定义，否则在世界中不可见：

```json title="RP/entity/my_bomb_projectile.entity.json"
{
    "format_version": "1.10.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "wiki:my_bomb_projectile",
            "materials": {
                "default": "entity_alphatest"
            },
            "textures": {
                "default": "textures/items/my_bomb"
            },
            "geometry": {
                "default": "geometry.snowball"
            },
            "render_controllers": ["controller.render.item_sprite"]
        }
    }
}
```

这里借用了原版雪球的几何体与渲染控制器，使弹射物显示为2D精灵图（方块图标效果）。

## 显示名称

```lang title="RP/texts/zh_CN.lang"
item.wiki:my_bomb=魔法炸弹
entity.wiki:my_bomb_projectile=魔法炸弹
```

## 测试

通过`/give @s wiki:my_bomb`获取物品，右键投掷，观察弹射物飞出并命中方块或实体时生成TNT并造成3点伤害。