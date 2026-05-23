# 生成已驯服实体

本文介绍如何在附加包中生成一个预先与玩家绑定的已驯服实体。文中提供两种方法：脚本API方法（推荐）和基于事件的传统方法。

## 脚本API方法（推荐）

使用`EntityTameableComponent.tame()`方法，在实体生成后立即将其驯服给指定玩家。这是最简洁、兼容性最好的方式。

以下示例在每个玩家生成（或重生）时，为其召唤一匹已驯服的狼：

```js title="BP/scripts/spawn_tamed.js"
import { world } from "@minecraft/server";

world.afterEvents.playerSpawn.subscribe(({ player }) => {
    const wolf = player.dimension.spawnEntity("minecraft:wolf", player.location);
    const tameable = wolf.getComponent("minecraft:tameable");
    tameable.tame(player);
});
```

这种方法无需修改任何JSON文件，也不依赖运行时标识符。

## 事件方法（不推荐）

/// warning | 兼容性警告
此方法依赖运行时标识符和对玩家实体的修改，可能与其他附加包产生冲突。**推荐优先使用脚本API方法。**
///

### 原理

创建一个"中间实体"作为弹射物，它一旦出现便立即变换为已驯服的目标实体，同时保留所有者信息。

### 第一步：创建中间实体

```json title="BP/entities/pretamed_wolf.json"
{
    "format_version": "1.21.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:pretamed_wolf",
            "runtime_identifier": "minecraft:arrow",
            "is_spawnable": false,
            "is_summonable": true
        },
        "components": {
            "minecraft:projectile": {},
            "minecraft:transformation": {
                "into": "minecraft:wolf<minecraft:on_tame>",
                "keep_owner": true
            }
        }
    }
}
```

- `runtime_identifier: "minecraft:arrow"`：使弹射物能够正确传递所有者信息
- `minecraft:transformation`：中间实体生成后立即变换为驯服的狼
- `keep_owner: true`：变换后保留弹射物的发射者作为主人

/// warning | 自定义宠物
如果你希望变换的目标是**自定义实体**而非原版狼，必须确保该实体包含`minecraft:is_tamed`组件，否则驯服后的某些行为将不正常。
///

### 第二步：修改player.json

在玩家实体中添加一个组件组和事件，用于召唤中间实体：

```json title="BP/entities/player.json（片段）"
"component_groups": {
    "wiki:spawn_tamed_wolf": {
        "minecraft:spawn_entity": {
            "entities": {
                "min_wait_time": 0,
                "max_wait_time": 0,
                "spawn_entity": "wiki:pretamed_wolf",
                "single_use": true,
                "num_to_spawn": 1
            }
        }
    }
},
"events": {
    "wiki:spawn_tamed_wolf": {
        "add": { "component_groups": ["wiki:spawn_tamed_wolf"] }
    }
}
```

通过命令`/event entity @a wiki:spawn_tamed_wolf`即可为所有玩家生成驯服的狼。

### 进阶：投掷物触发

还可以制作一个可投掷的"驯服蛋"物品，投出后在落点变换为已驯服实体：

#### 物品定义

```json title="BP/items/tame_egg.json"
{
    "format_version": "1.21.50",
    "minecraft:item": {
        "description": { "identifier": "wiki:tame_egg" },
        "components": {
            "minecraft:icon": "wiki:tame_egg",
            "minecraft:throwable": { "do_swing_animation": true },
            "minecraft:projectile": { "projectile_entity": "wiki:pretamed_wolf" }
        }
    }
}
```

#### 修改中间实体（延迟变换）

让中间实体在命中时才触发变换，而不是一生成就变换：

```json title="BP/entities/pretamed_wolf.json"
{
    "format_version": "1.21.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:pretamed_wolf",
            "runtime_identifier": "minecraft:arrow",
            "is_spawnable": false,
            "is_summonable": true
        },
        "component_groups": {
            "wiki:transform_to_entity": {
                "minecraft:transformation": {
                    "into": "minecraft:wolf<minecraft:on_tame>",
                    "keep_owner": true
                }
            }
        },
        "components": {
            "minecraft:projectile": {
                "on_hit": {
                    "impact_damage": { "damage": 0 },
                    "stick_in_ground": {},
                    "definition_event": {
                        "event_trigger": { "event": "wiki:on_hit" }
                    }
                }
            }
        },
        "events": {
            "wiki:on_hit": {
                "add": { "component_groups": ["wiki:transform_to_entity"] }
            }
        }
    }
}
```

这样，投出"驯服蛋"后，它会在落点变为一只已与玩家绑定的驯服狼。
