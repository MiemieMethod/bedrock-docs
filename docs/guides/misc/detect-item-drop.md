# 掉落来源检测

这个小技巧用来区分"玩家主动丢出的物品"和"其他来源产生的物品"（如死亡掉落、爆炸散落、漏斗吐出等）。

## 原理

当玩家按下丢弃键（默认Q键）主动丢出物品时，生成的物品实体会**继承玩家当时的朝向**，因此它的Y轴旋转（偏航角）会和玩家完全一致，绝不会恰好为`0°`（除非玩家恰好朝正南方向）。

非玩家来源的物品实体（漏斗弹出、方块掉落等）没有继承来自玩家的朝向，在统计上，其旋转为`0°`的概率极高。

利用这个差异，可以用`ry=0,rym=0`来**筛出"旋转角度精确为0°"的物品**，将其标记为其他来源，剩下的则归为玩家来源：

```mcfunction title="BP/functions/wiki/detect/item/is_dropped_by.mcfunction"
# 第一步：旋转角恰好为0的物品 → 标记为其他来源
tag @e[type=item,ry=0,rym=0,tag=!wiki:source.player] add wiki:source.other

# 第二步：剩余未标记的物品 → 标记为玩家来源
tag @e[type=item,tag=!wiki:source.other] add wiki:source.player
```

/// tip | 边界情况
即使玩家恰好朝正南方向（0°）丢物，其物品实体的旋转也不会精确等于`0°`，因此第二步仍能把玩家掉落正确归入`wiki:source.player`。不过，如果其他来源的物品恰好具有非0角度（极少数情况），可能会被错误归类。对于大多数玩法场景，这套方案足够可靠。
///

## 清除标记

处理完毕后，记得清除标记，避免下一轮检测出现残留：

```mcfunction title="清除标记"
tag @e[type=item,tag=wiki:source.other] remove wiki:source.other
tag @e[type=item,tag=wiki:source.player] remove wiki:source.player
```

## 继续阅读

- [移动状态检测](./detect-movements.md)
- [execute逻辑门](./logic-gates.md)