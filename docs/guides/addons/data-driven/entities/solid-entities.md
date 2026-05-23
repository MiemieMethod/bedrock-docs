# 固体实体

**固体实体**是指玩家可以与之产生物理碰撞的实体——玩家会被阻挡、可以站在其上、无法穿越。这类实体有很多用途，例如模拟方块、制作载具平台或创造机关道具。

本文介绍几种创建固体实体的方式，并非所有方法都适合所有场景，请根据需求自行尝试。

## 方法一：可碰撞实体（推荐）

这是目前最佳的方案，无需修改玩家实体JSON即可实现碰撞。

`minecraft:is_collidable`组件允许其他实体与该实体发生碰撞。配合`minecraft:collision_box`可以设定碰撞箱的大小。

```json title="BP/entities/solid_entity.json"
{
    "format_version": "1.26.10",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:solid_entity",
            "is_spawnable": true,
            "is_summonable": true
        },
        "components": {
            "minecraft:is_collidable": {},
            "minecraft:collision_box": {
                "height": 1,
                "width": 1
            },
            "minecraft:body_rotation_blocked": {},
            "minecraft:rotation_axis_aligned": {},
            "minecraft:renders_when_invisible": {},
            "minecraft:spell_effects": {
                "add_effects": [
                    {
                        "duration": "infinite",
                        "effect": "invisibility",
                        "visible": false
                    }
                ]
            }
        }
    }
}
```

这里用了`minecraft:body_rotation_blocked`和`minecraft:rotation_axis_aligned`防止实体旋转，用隐身效果配合`minecraft:renders_when_invisible`来隐藏阴影（适合用模型替代视觉表现的情况）。

## 方法二：可叠加实体

给实体添加`minecraft:is_stackable`组件，使其能与其他可叠加实体（如船和矿车）发生碰撞。还需要同时添加`minecraft:push_through`并将`value`设为`1`。

```json title="minecraft:entity > components（节选）"
"components": {
    "minecraft:is_stackable": {},
    "minecraft:push_through": 1
}
```

## 方法三：运行时标识符

通过[运行时标识符](../../../docs/addon/entity.md)也可以实现固体碰撞，但目前只有两种可用形状，且无法缩放，各有附带效果。

### 船形碰撞

```json title="BP/entities/solid_entity.json（description节选）"
"runtime_identifier": "minecraft:boat"
```

- 提供船形的固体碰撞箱
- 附带其他船类硬编码效果（如旋转限制）

### 潜影贝形碰撞

```json title="BP/entities/solid_entity.json（description节选）"
"runtime_identifier": "minecraft:shulker"
```

- 提供1×1×1方块大小的固体碰撞
- 实体会吸附到方块网格上
- 支撑方块被移除时实体会随机传送

## 方法四：屏障方块

某些场合下，动态放置和移除屏障方块是更实际的方案。这需要同时设计放置和清除的机制。

```
/fill ~ ~ ~ ~ ~1 ~ barrier 0 replace air
```
在2×1×1区域内放置屏障。

```
/fill ~1 ~1 ~1 ~-1 ~-1 ~-1 air 0 replace barrier
```
清除3×3×3范围内的屏障。

这些命令通常配合行为包动画或动画控制器循环触发。该方法适合静态障碍物或临时需要阻挡玩家的场景。
