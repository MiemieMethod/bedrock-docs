# playanimation命令

`playanimation`是命令侧做姿态控制、骨骼偏移和显示实体伪装的核心工具。

## 语法

```mcfunction title="命令语法"
playanimation <entity:target> <animation:string> [next_state:string] [blend_out_time:float] [stop_expression:string] [controller:string]
```

- `stop_expression`使用Molang表达式。
- `controller`用于区分并叠加不同动画控制器状态。

## 基础示例

```mcfunction title="BP/functions/wiki/playanimation/basic.mcfunction"
playanimation @a animation.player.riding.legs none 0 "query.is_moving"
```

## 动画控制器覆盖

```mcfunction title="BP/functions/wiki/playanimation/controller.mcfunction"
# 覆盖现有控制器
playanimation @e[type=allay] animation.player.attack.positions none 1 controller.animation.allay.dancing

# 注册自定义控制器
playanimation @a animation.ender_dragon.neck_head_movement animation.piglin.celebrate_hunt_special 0 "v.head_rotation_y=q.life_time*1000;return !q.is_sneaking;" wiki:head
playanimation @a animation.piglin.celebrate_hunt_special animation.ender_dragon.neck_head_movement 0 "v.head_rotation_y=q.target_y_rotation;return q.is_sneaking;" wiki:dance
```

/// note | 客户端侧特性
自定义控制器存储在客户端实体上。离开世界或实体远距离卸载后会重置。
///

## 动画叠加与移除

```mcfunction title="BP/functions/wiki/playanimation/stack_remove.mcfunction"
# 叠加
playanimation @a animation.player.riding.legs none 0 "0" wiki:rideleg
playanimation @a animation.piglin.celebrate_hunt_special none 0 "0" wiki:dance

# 覆盖移除
playanimation @a animation.player.attack.positions none 0 "1" wiki:rideleg
playanimation @a animation.player.attack.positions none 0 "1" wiki:dance
```

## 变量改写

```mcfunction title="BP/functions/wiki/playanimation/custom_variable.mcfunction"
playanimation @a animation.parrot.moving none 0 "v.wing_flap=10;" wiki:body_ypos
playanimation @a animation.player.attack.rotations none 0 "v.attack_body_rot_y=0;" wiki:body_yrot
playanimation @a animation.minecart.move none 0 "v.rail_offset.x=0;v.rail_offset.y=0;v.rail_offset.z=0;" wiki:root_pos
playanimation @a animation.ender_dragon.neck_head_movement none 0 "v.head_position_x=0;v.head_position_y=0;v.head_position_z=0;v.head_rotation_x=0;v.head_rotation_y=0;v.head_rotation_z=0;" wiki:head_pos_rot
```

## 使用建议

- 控制器名保持命名空间前缀，避免冲突。
- 高频循环命令可能闪烁，优先事件触发或加延迟。
- 遇到复杂表达式，建议函数化管理。

## 继续阅读

- [FMBE显示实体](./display-entities.md)
- [MBE方块实体](./block-entities.md)
