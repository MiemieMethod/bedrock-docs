# 旧版物品和方块事件响应

<!-- md:flag experimental --><!-- md:version range 1.16.100 1.19.20 false true -->

本页收录了旧版实验性自定义物品和自定义方块定义事件中可用的事件响应（Event Response）。这些事件响应需要开启"假日创作者功能"实验性玩法才能生效，属于1.16.100至1.19.20阶段的接口，其中部分已被现代脚本API自定义组件取代。现代自定义方块和自定义物品的交互逻辑建议优先使用脚本API，本页仅供旧包维护和历史参考。

## 适用范围

| 事件响应类 | 实体 | 物品 | 方块 |
|---|---|---|---|
| `run_command`（ActorCommandResponse） | ✓ | — | — |
| `set_property`（SetPropertyResponse，实体） | ✓ | — | — |
| `run_command`（CommandResponse） | — | ✓ | ✓ |
| `decrement_stack` | — | ✓ | ✓ |
| `damage` | — | ✓ | ✓ |
| `die` | — | ✓ | ✓ |
| `add_mob_effect` | — | ✓ | ✓ |
| `remove_mob_effect` | — | ✓ | ✓ |
| `play_effect` | — | ✓ | ✓ |
| `play_sound` | — | ✓ | ✓ |
| `set_property`（SetBlockProperty，方块属性） | — | ✓ | ✓ |
| `shoot` | — | ✓ | — |
| `swing` | — | ✓ | ✓ |
| `teleport` | — | ✓ | ✓ |
| `transform_item` | — | ✓ | ✓ |
| `set_block` | — | — | ✓ |
| `set_block_at_pos` | — | — | ✓ |
| `spawn_loot` | — | — | ✓ |

## `run_command`（实体）

```json
"run_command": {
  "command": "say hello",
  "target": "self"
}
```

`command`也可以是字符串数组，一次执行多条命令。

| `target`值 | 效果 |
|---|---|
| `self` | 命令起点为实体本身 |
| `other` | 命令起点为对立实体（若有） |
| `player` | 命令起点为玩家（若为玩家实体） |
| `target` | 命令起点为攻击目标（若有） |
| `parent` | 命令起点为父实体（若有） |
| `baby` | 命令起点为子实体（若有） |
| `block` | 命令起点为正在交互的方块（若有） |
| `item` | 命令起点为手持物品对应的持有实体（若有） |

## `set_property`（实体属性）

```json
"set_property": {
  "demo:my_property": "true"
}
```

设置实体的一个属性，接受字面值或Molang表达式。键名应为属性的赋命名空间标识符。

## `run_command`（物品/方块）

```json
"run_command": {
  "command": "say hello",
  "target": "self"
}
```

`command`同样可以是字符串数组。`target`的可选值及效果与实体版本相同，但"命令起点"的解释依上下文（物品持有者/方块位置）而定：

| `target`值 | 效果 |
|---|---|
| `self` | 物品：持有该物品的实体；方块：方块本身 |
| `other` | 对立实体（若有） |
| `player` | 上下文玩家（若有） |
| `target` | 攻击目标（若有） |
| `parent` | 父实体（若有） |
| `baby` | 子实体（若有） |
| `block` | 正在交互的方块（若有） |
| `item` | 持有该物品的实体（若有） |

## `decrement_stack`

```json
"decrement_stack": {
  "ignore_game_mode": false
}
```

将物品堆叠数量减少1。`ignore_game_mode`为`true`时在创造模式下也会减少。

## `damage`

```json
"damage": {
  "target": "self",
  "type": "magic",
  "amount": 2,
  "mob_amount": 2
}
```

对目标造成带有击退的伤害或损坏（对物品为损坏值）。`type`为伤害类型，对物品造成损坏时`type`不起作用。当`type`为`fire`时会额外点燃目标实体。

| `target`值 | 效果 |
|---|---|
| `self` | 实体：伤害自身；物品：损坏物品；方块：无意义 |
| `other` | 对立实体（若有） |
| `player` | 上下文玩家（若有） |
| `target` | 攻击目标（若有） |
| `parent` | 父实体（若有） |
| `baby` | 子实体（若有） |
| `holder` | 持有该物品/方块所对应物品的实体（若有） |
| `item` | 方块：对方块对应的物品造成损坏 |

## `die`

```json
"die": {
  "target": "self"
}
```

致目标实体死亡，或破坏目标方块（产生掉落物）。

| `target`值 | 效果 |
|---|---|
| `self` | 实体：死亡；物品：持有者死亡；方块：破坏方块并产生掉落物 |
| `other` | 对立实体死亡（若有） |
| `player` | 上下文玩家死亡（若有） |
| `target` | 攻击目标死亡（若有） |
| `parent` | 父实体死亡（若有） |
| `baby` | 子实体死亡（若有） |
| `block` | 方块：破坏方块并产生掉落物（若有） |
| `holder` | 持有该物品/方块所对应物品的实体死亡（若有） |

## `add_mob_effect`

```json
"add_mob_effect": {
  "effect": "speed",
  "target": "self",
  "duration": 10.0,
  "amplifier": 1
}
```

给予目标一个状态效果。`duration`单位为秒，`amplifier`为等级（0对应I级）。

| `target`值 | 效果 |
|---|---|
| `self` | 实体：给予自身；物品：给予持有者；方块：给予对应物品的持有者 |
| `other` | 给予对立实体（若有） |
| `player` | 给予上下文玩家（若有） |
| `target` | 给予攻击目标（若有） |
| `parent` | 给予父实体（若有） |
| `baby` | 给予子实体（若有） |
| `holder` | 给予持有者（若有） |

## `remove_mob_effect`

```json
"remove_mob_effect": {
  "effect": "speed",
  "target": "self"
}
```

移除目标的一个状态效果。将`effect`设为`"all"`可移除全部状态效果。`target`可选值与`add_mob_effect`相同。

## `play_effect`

```json
"play_effect": {
  "effect": "smoke",
  "target": "self",
  "data": 0
}
```

在目标位置播放一个旧版粒子效果（`data`为粒子数据值）。

| `target`值 | 效果 |
|---|---|
| `self` | 实体：在实体处；物品：在持有者处；方块：在方块处 |
| `other` | 在对立实体处（若有） |
| `player` | 在上下文玩家处（若有） |
| `target` | 在攻击目标处（若有） |
| `parent` | 在父实体处（若有） |
| `baby` | 在子实体处（若有） |
| `block` | 在方块处（若有） |
| `holder` | 在持有者处（若有） |

## `play_sound`

```json
"play_sound": {
  "sound": "random.levelup",
  "target": "self"
}
```

在目标位置广播一个存档声音事件。`target`可选值与`play_effect`相同。

## `set_property`（方块属性）

```json
"set_property": {
  "demo:my_state": "1"
}
```

设置方块的一个方块状态，接受字面值或Molang表达式。键名应为方块状态的赋命名空间标识符。

## `shoot`

```json
"shoot": {
  "projectile": "minecraft:snowball",
  "target": "self",
  "launch_power": 1.0,
  "angle_offset": 0.0
}
```

从持有者处发射一个弹射物。`launch_power`和`angle_offset`也可以是Molang表达式；`angle_offset`目前仅被解析，无实际效果。弹射物的初始威力为`minecraft:projectile`组件`power`字段的值乘以`launch_power`。仅对物品有效，方块不支持。

| `target`值 | 效果 |
|---|---|
| `self` | 物品：从持有者处以持有者朝向发射；实体：从武器挂接点朝自身朝向发射 |
| `other` | 朝对立实体方向发射（若有） |
| `target` | 朝攻击目标方向发射（若有） |
| `parent` | 朝父实体方向发射（若有） |
| `baby` | 朝子实体方向发射（若有） |

## `swing`

```json
"swing": {}
```

使持有该物品的实体播放一次摆臂动画，无参数。

## `teleport`

```json
"teleport": {
  "target": "self",
  "max_range": [32.0, 16.0, 32.0],
  "destination": [0.0, 0.0, 0.0],
  "land_on_block": true,
  "avoid_water": true
}
```

在指定最大范围内随机传送目标实体，或传送到`destination`指定的绝对坐标处。`land_on_block`控制是否落在方块表面，`avoid_water`控制是否避免传送到水中。

| `target`值 | 效果 |
|---|---|
| `self` | 实体：传送自身；物品：传送持有者；方块：传送对应物品的持有者 |
| `other` | 传送对立实体（若有） |
| `player` | 传送上下文玩家（若有） |
| `target` | 传送攻击目标（若有） |
| `parent` | 传送父实体（若有） |
| `baby` | 传送子实体（若有） |
| `holder` | 传送持有者（若有） |

## `transform_item`

```json
"transform_item": {
  "transform": "minecraft:apple"
}
```

将当前物品替换为`transform`指定标识符的物品。

## `set_block`

```json
"set_block": {
  "block_type": "minecraft:stone"
}
```

将当前方块替换为`block_type`指定的方块类型。仅对方块有效。

## `set_block_at_pos`

```json
"set_block_at_pos": {
  "block_type": "minecraft:stone",
  "block_offset": [0.0, 1.0, 0.0]
}
```

在相对于当前方块的偏移位置处设置指定方块类型。`block_offset`为`[x, y, z]`偏移向量。仅对方块有效。

## `spawn_loot`

```json
"spawn_loot": {
  "table": "loot_tables/blocks/my_loot.json"
}
```

在当前方块处按战利品表产生掉落物。以0.0幸运值、无关联实体、无玩家、无伤害来源的模式从表中抽取物品。仅对方块有效。
