# 二进制逻辑

**二进制（Binary）**在命令系统里最实用的价值，是把“线性枚举”压缩成“按位拆解”，显著减少命令量。

## 位权回顾

| 位 | 值 |
|---|---|
| $2^0$ | 1 |
| $2^1$ | 2 |
| $2^2$ | 4 |
| $2^3$ | 8 |
| $2^4$ | 16 |
| $2^5$ | 32 |
| $2^6$ | 64 |

例如`1101_2=8+4+1=13`。

## 商店示例(1到64)

```mcfunction title="BP/functions/wiki/binary/shop.mcfunction"
execute as @a[hasitem={item=bread,quantity=64..}] run scoreboard players add @s wiki:money 64
execute as @a[hasitem={item=bread,quantity=64..}] run clear @s bread 0 64

execute as @a[hasitem={item=bread,quantity=32..}] run scoreboard players add @s wiki:money 32
execute as @a[hasitem={item=bread,quantity=32..}] run clear @s bread 0 32

execute as @a[hasitem={item=bread,quantity=16..}] run scoreboard players add @s wiki:money 16
execute as @a[hasitem={item=bread,quantity=16..}] run clear @s bread 0 16

execute as @a[hasitem={item=bread,quantity=8..}] run scoreboard players add @s wiki:money 8
execute as @a[hasitem={item=bread,quantity=8..}] run clear @s bread 0 8

execute as @a[hasitem={item=bread,quantity=4..}] run scoreboard players add @s wiki:money 4
execute as @a[hasitem={item=bread,quantity=4..}] run clear @s bread 0 4

execute as @a[hasitem={item=bread,quantity=2..}] run scoreboard players add @s wiki:money 2
execute as @a[hasitem={item=bread,quantity=2..}] run clear @s bread 0 2

execute as @a[hasitem={item=bread,quantity=1..}] run scoreboard players add @s wiki:money 1
execute as @a[hasitem={item=bread,quantity=1..}] run clear @s bread 0 1
```

/// tip | 为什么快
玩家有50个面包时，系统会按32→16→2拆解，只需命中3档，而不是从1数到50。
///

## 进阶方向

- 用二分思路获取坐标整数分数。
- 与[分叉执行](./execution-forking.md)结合生成复杂结构。

## 继续阅读

- [分叉执行](./execution-forking.md)
- [记分板运算](./scoreboard-operations.md)