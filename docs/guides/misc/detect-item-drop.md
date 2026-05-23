# 掉落来源检测

这个小技巧用来区分“玩家丢出的物品”和“其他来源的物品”。

## 核心命令

```mcfunction title="BP/functions/wiki/detect/item/is_dropped_by.mcfunction"
# 先标记其他来源
tag @e[type=item,ry=0,rym=0,tag=!wiki:source.player] add wiki:source.other

# 再标记玩家来源
tag @e[type=item,tag=!wiki:source.other] add wiki:source.player
```

思路是先把满足特征的一类目标筛出去，再把剩余目标归为玩家来源。

/// tip | 细节
即使玩家正好朝0°方向丢物，第二步仍会正确把玩家掉落标记为`wiki:source.player`。
///

## 继续阅读

- [移动状态检测](./detect-movements.md)
- [分数比较](./comparing-scores.md)
