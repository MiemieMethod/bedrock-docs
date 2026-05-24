# 注视检测

这是一套“玩家是否正在看某目标”的纯命令方案，适合交互方块、观察触发、剧情机关。

/// warning | 局限
该方案不检测遮挡。也就是说，中间有墙时仍可能命中“看向目标”。
///

## 通用命令

```mcfunction title="BP/functions/wiki/detect/player/is_looking_at.mcfunction"
execute as <target> at @s anchored eyes facing <entity|coordinate> positioned ^^^1 positioned ~~-1.62~ rotated as @s positioned ^^^-1 if entity @s[r=0.2] run <command>
```

这条命令的关键是“向前一步再退一步”后检查是否仍接近自己，借此判断视线是否对准目标。

## 示例

```mcfunction title="BP/functions/wiki/detect/player/is_looking_at/target.mcfunction"
execute as @a at @s anchored eyes facing entity @e[type=cow,tag=wiki:target] eyes positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s[r=0.2] run say 你在看牛
execute as @a at @s anchored eyes facing 10 20 30 positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s[r=0.2] run say 你在看目标坐标
```

## 视角容差计算

若希望按角度反推半径容差，可用：

$$
r=2\sin\left(rac{lpha}{2}
ight)
$$

反向计算角度：

$$
lpha=2rcsin\left(rac{r}{2}
ight)
$$

当`r=0.2`时，容差角大约在12°左右。

## 高精度版本V2

```mcfunction title="BP/functions/wiki/detect/player/is_precisely_looking_at.mcfunction"
execute as @a at @s anchored eyes positioned ~~-0.5~ facing entity @e[type=armor_stand,rm=0.0001] feet positioned ^^^10 rotated as @s positioned ^^^10 facing entity @s eyes positioned as @s positioned ^^^-1 rotated as @s positioned ^^^-1 if entity @s[r=0.766] run title @s actionbar 命中精确注视
```

V2更适合准星级检测，但调参成本更高。

## 继续阅读

- [移动状态检测](./detect-movements.md)
- [execute逻辑门](./logic-gates.md)