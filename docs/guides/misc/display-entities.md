# FMBE显示实体

本页介绍**狐狸方块实体（Fox MBE，FMBE）**：用狐狸骨骼与`playanimation`组合渲染可调方块显示。

{{video|youtube|FVRd2n7JX3k}}

/// note | 成本提醒
每个显示实体都对应1只狐狸。数量大时会明显增加实体负载。
///

## 基础渲染系统

```mcfunction title="BP/functions/wiki/fmbe/render.mcfunction"
# 重定位与缩放
playanimation @e[tag=wiki:fmbe] animation.player.sleeping none 0 "" controller.animation.fox.move
playanimation @e[tag=wiki:fmbe] animation.creeper.swelling none 0 "v.scale=v.scale??1;v.xzscale=v.xzscale??1;v.yscale=v.yscale??1;" wiki:scale
playanimation @e[tag=wiki:fmbe] animation.ender_dragon.neck_head_movement none 0 "v.xbasepos=v.xbasepos??0;v.ybasepos=v.ybasepos??0;v.zbasepos=v.zbasepos??0;" wiki:shift_pos

# 旋转
playanimation @e[tag=wiki:fmbe] animation.warden.move none 0 "v.body_x_rot=90+v.xrot;v.body_z_rot=90+v.yrot;" wiki:xrot
playanimation @e[tag=wiki:fmbe] animation.player.attack.rotations none 0 "v.attack_body_rot_y=-v.zrot;" wiki:zrot

# 位置
playanimation @e[tag=wiki:fmbe] animation.parrot.moving none 0 "v.wing_flap=(16-v.xpos)/0.3;" wiki:xpos
playanimation @e[tag=wiki:fmbe] animation.minecart.move.v1.0 none 0 "v.rail_offset.y=1.6485+v.ypos/16;" wiki:ypos
playanimation @e[tag=wiki:fmbe] animation.parrot.dance none 0 "v.dance.x=-v.zpos;" wiki:zpos
```

## 使用流程

```mcfunction title="BP/functions/wiki/fmbe/setup.mcfunction"
summon fox ~~~ ~ ~ minecraft:as_adult "wiki:fmbe"
replaceitem entity @e[name="wiki:fmbe",c=1] slot.weapon.mainhand 0 <itemID>
tag @e[name="wiki:fmbe"] add wiki:fmbe
```

常用变量分组：

- 位置：`v.xpos`、`v.ypos`、`v.zpos`
- 旋转：`v.xrot`、`v.yrot`、`v.zrot`
- 缩放：`v.scale`、`v.xzscale`、`v.yscale`
- 基准偏移：`v.xbasepos`、`v.ybasepos`、`v.zbasepos`

### 动态改参数

```mcfunction title="BP/functions/wiki/fmbe/set_variable.mcfunction"
playanimation @e[tag=wiki:fmbe] animation.player.attack.positions none 0 "v.xrot=35;v.ypos=16;v.scale=1.5;" wiki:setvariable
```

### 静音处理

```mcfunction title="BP/functions/wiki/fmbe/stopsound.mcfunction"
stopsound @a mob.fox.spit
stopsound @a mob.fox.sniff
stopsound @a mob.fox.sleep
stopsound @a mob.fox.screech
stopsound @a mob.fox.hurt
stopsound @a mob.fox.eat
stopsound @a mob.fox.death
stopsound @a mob.fox.bite
stopsound @a mob.fox.ambient
stopsound @a mob.fox.aggro
```

### 动态替换显示物品

```mcfunction title="BP/functions/wiki/fmbe/change_display.mcfunction"
execute as @e[name="wiki:fmbe_pickaxe"] at @e[tag=wiki:fmbe,name="wiki:test_target"] run loot replace entity @e[c=1] slot.weapon.mainhand 0 mine ~~-1~ mainhand
```

## 压缩版与进阶版

- 压缩版可用`render.compressed.mcfunction`，命令更少但可调项更少。
- 进阶版按3D方块/2D方块/物品三套渲染函数区分。
- 超长表达式建议放函数文件维护，避免命令方块直接编辑。

{{video|youtube|DdYq_nOFeKM}}
{{video|youtube|zwyGmxjBDDw}}
{{video|youtube|-5N8yVGR1MA}}

## 继续阅读

- [MBE方块实体](./block-entities.md)
- [playanimation命令](./playanimation.md)
