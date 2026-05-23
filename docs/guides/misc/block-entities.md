# MBE方块实体

本页介绍**Max方块实体（Max's Block Entity，MBE）**方案：用盔甲架+`playanimation`伪装成方块显示。

{{video|youtube|kb8rz9ItE_M}}

## 快速准备

```mcfunction title="BP/functions/wiki/mbe/setup.mcfunction"
summon armor_stand ~~~ 81 ~ default "Grumm"
# 可选：把方块放到副手，防止被玩家取走
replaceitem entity @e[name="Grumm"] slot.weapon.offhand 0 <itemID>
```

`Grumm`命名是为了避免贴图翻转。

## 渲染核心

```mcfunction title="BP/functions/wiki/mbe/render.mcfunction"
# 对齐手臂
playanimation @e[type=armor_stand,name="Grumm"] animation.armor_stand.entertain_pose null 0 "0" wiki:align.arms

# 小方块尺寸
playanimation @e[type=armor_stand,name="Grumm"] animation.player.move.arms.zombie null 0 "0" wiki:size.mini_block

# 可选：整方块尺寸
playanimation @e[type=armor_stand,name="Grumm"] animation.ghast.scale null 0 "0" wiki:size.full_block
playanimation @e[type=armor_stand,name="Grumm"] animation.fireworks_rocket.move null 0 "0" wiki:align.full_block

# 冻结并隐藏本体
execute as @e[type=armor_stand,name="Grumm"] at @s run tp ~~~
effect @e[type=armor_stand,name="Grumm"] invisibility infinite 1 true
```

## 旋转与对位预设

/// details | 整方块朝向预设
```mcfunction
# 北
/tp @e[type=armor_stand,name="Grumm",c=1] ~-1.1245 ~0.2260 ~-0.097 81
# 南
/tp @e[type=armor_stand,name="Grumm",c=1] ~1.1245 ~0.2260 ~0.097 260
# 东
/tp @e[type=armor_stand,name="Grumm",c=1] ~0.097 ~0.2260 ~-1.1245 171
# 西
/tp @e[type=armor_stand,name="Grumm",c=1] ~-0.097 ~0.2260 ~1.1245 350
```
///

/// details | 小方块朝向预设
```mcfunction
# 北
/tp @e[type=armor_stand,name="Grumm",c=1] ~-0.417~-0.5 ~-0.035 81
# 南
/tp @e[type=armor_stand,name="Grumm",c=1] ~0.417 ~-0.5 ~0.035 260
# 东
/tp @e[type=armor_stand,name="Grumm",c=1] ~0.035 ~-0.5 ~-0.417 171
# 西
/tp @e[type=armor_stand,name="Grumm",c=1] ~-0.035 ~-0.5 ~0.417 350
```
///

## 保存与加载

```mcfunction title="BP/functions/wiki/mbe/save_load.mcfunction"
execute at @e[type=armor_stand,name="Grumm",c=1] run structure save wiki:mbe ~~~ ~~~ true disk false
structure load wiki:mbe <x> <y> <z>
```

## 继续阅读

- [FMBE显示实体](./display-entities.md)
- [playanimation命令](./playanimation.md)
