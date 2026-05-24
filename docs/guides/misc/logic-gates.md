# execute逻辑门

命令里常说的**逻辑门（Logic Gate）**，本质上就是把布尔判断写进`execute if`或`execute unless`。你可以把它理解成"命令版电路"——条件成立时执行，不成立时跳过，正好对应布尔逻辑中的"真/假"。

## 前置概念

本页以实体**标签**作为输入条件。标签存在 = 真（1），标签不存在 = 假（0）。选择器参数`[tag=!红]`表示"没有红标签"，等价于NOT运算。

类似的逻辑也适用于`scores`、`hasitem`、`type`、`name`等其他条件，可以互相替换。

## 八种逻辑门

### 缓冲门（Buffer）

真值表：输入为真时输出为真。这是最简单的情形，直接检测条件即可。

| 输入 A | 输出 |
|:---:|:---:|
| 0 | 0 |
| 1 | 1 |

```mcfunction
execute if entity @s[tag=red] run <命令>
```

### 非门（NOT）

输入取反。

| 输入 A | 输出 |
|:---:|:---:|
| 0 | 1 |
| 1 | 0 |

```mcfunction
execute unless entity @s[tag=red] run <命令>
```

或者等价写法：

```mcfunction
execute if entity @s[tag=!red] run <命令>
```

### 与门（AND）

两个条件都成立时才输出真。把两个标签写进同一个选择器即可（隐式AND）。

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

```mcfunction
execute if entity @s[tag=red,tag=green] run <命令>
```

### 与非门（NAND）

AND的取反。

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```mcfunction
execute unless entity @s[tag=red,tag=green] run <命令>
```

### 或门（OR）

至少一个条件成立时输出真。利用"排除全假"来实现：

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

```mcfunction
execute unless entity @s[tag=!red,tag=!green] run <命令>
```

### 或非门（NOR）

OR的取反，即两个都为假时才输出真。

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

```mcfunction
execute if entity @s[tag=!red,tag=!green] run <命令>
```

### 异或门（XOR）

恰好只有一个输入为真时输出真。需要排除"两者都假"和"两者都真"两种情况：

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```mcfunction
execute unless entity @s[tag=!red,tag=!green] unless entity @s[tag=red,tag=green] run <命令>
```

### 同或门（XNOR）

XOR的取反，即两个输入相同时输出真。排除"一真一假"的两种情况：

| 输入 A | 输入 B | 输出 |
|:---:|:---:|:---:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

```mcfunction
execute unless entity @s[tag=red,tag=!green] unless entity @s[tag=!red,tag=green] run <命令>
```

## 迁移到其他条件

你不必把逻辑门绑定在`tag`上，任何可以写进选择器的条件都可以套相同结构。

```mcfunction title="其他条件示例"
# 分数OR：满足任一分数条件
execute unless entity @p[scores={wiki:a=!5,wiki:b=!5}] run say 命中OR条件

# hasitem OR：玩家有钻石剑或铁剑
execute unless entity @p[hasitem=[{item=diamond_sword,quantity=0},{item=iron_sword,quantity=0}]] run say 有武器

# type OR：实体是鸡或牛
execute unless entity @e[type=!chicken,type=!cow] run say 是鸡或牛
```

## 实战建议

/// tip | 逐步调试
先把每个输入条件单独写一条命令验证，确认它能按预期命中或排除实体，再把多个条件组合成目标的逻辑门。这样排错最快。
///

/// note | 多条件AND vs. 多条件OR的对称性
AND用","连接条件；OR用`unless ... unless ...`连接条件（排除全假）。记住这个对称性可以帮助你快速推导任意逻辑组合。
///

## 继续阅读

- [新版execute命令](./execute-command.md)
- [分数比较](./comparing-scores.md)
- [记分板运算](./scoreboard-operations.md)