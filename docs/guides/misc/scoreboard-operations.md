# 记分板运算

**记分板运算（Scoreboard Operation）**是`scoreboard players operation`命令提供的一套运算符，用于直接在记分板数值之间进行算术或逻辑运算，无需通过代码。它是命令系统中做数学计算的核心手段。

## 基础语法

```mcfunction title="通用语法"
scoreboard players operation <目标持有者> <目标记分项> <运算符> <来源持有者> <来源记分项>
```

`<目标持有者>`是被修改的一方，大多数运算符只读取`<来源持有者>`而不修改它（`><`是例外）。持有者可以是玩家名、实体选择器或虚拟持有者（如`.Total`）。

## 算术运算符

### `+=`加法

把来源值加到目标值上：

```mcfunction
# 结果：.A = .A + .B
scoreboard players operation .A wiki:var += .B wiki:var
```

### `-=`减法

从目标值中减去来源值：

```mcfunction
# 结果：.A = .A - .B
scoreboard players operation .A wiki:var -= .B wiki:var
```

### `*=`乘法

目标值乘以来源值：

```mcfunction
# 结果：.A = .A × .B
scoreboard players operation .A wiki:var *= .B wiki:var
```

### `/=`整除

目标值除以来源值，结果向零取整（即截断，而非向下取整）：

```mcfunction
# 结果：.A = floor(.A / .B)（趋零取整）
scoreboard players operation .A wiki:var /= .B wiki:var
```

/// warning | 负数截断行为
`/=`使用的是**趋零取整**，而不是数学意义的向下取整。`-7 / 2 = -3`（不是`-4`）。如果需要真正的向下取整，需要额外处理负数边界。
///

### `%=`取余

目标值对来源值取余：

```mcfunction
# 结果：.A = .A mod .B
scoreboard players operation .A wiki:var %= .B wiki:var
```

取余结果的符号与**被除数（目标值）**相同。例如`-7 % 3 = -1`，而不是`2`。

## 逻辑运算符

### `=`赋值

将来源值复制到目标值，来源值不变：

```mcfunction
# 结果：.A = .B（.B不变）
scoreboard players operation .A wiki:var = .B wiki:var
```

### `<`取最小值

若来源值小于目标值，则将目标值替换为来源值（取两者较小的那个）：

```mcfunction
# 结果：.A = min(.A, .B)
scoreboard players operation .A wiki:var < .B wiki:var
```

/// note | 用途：钳位上限
`<`可以用来做上限钳位：把上限值存到来源持有者，再对目标持有者执行`<`，就可以保证目标值不超过上限。
///

### `>`取最大值

若来源值大于目标值，则将目标值替换为来源值（取两者较大的那个）：

```mcfunction
# 结果：.A = max(.A, .B)
scoreboard players operation .A wiki:var > .B wiki:var
```

### `><`交换

将两个持有者的值互换，这是唯一会同时修改双方的运算符：

```mcfunction
# 结果：.A 与 .B 互换
scoreboard players operation .A wiki:var >< .B wiki:var
```

## 综合示例

### 判断两个分数是否相等

```mcfunction title="BP/functions/wiki/scoreboard/operations/equal_check.mcfunction"
scoreboard objectives add wiki:temp dummy
scoreboard players operation .Temp wiki:temp = .Steve wiki:var
scoreboard players operation .Temp wiki:temp -= .Alex wiki:var
execute if score .Temp wiki:temp matches 0 run say 分数相同
```

### 限制分数上下界（钳位）

```mcfunction title="BP/functions/wiki/scoreboard/operations/clamp.mcfunction"
# 确保 .Value 在 [0, 100] 范围内
scoreboard players set .Min wiki:const 0
scoreboard players set .Max wiki:const 100
scoreboard players operation .Value wiki:var > .Min wiki:const
scoreboard players operation .Value wiki:var < .Max wiki:const
```

### 计算百分比

```mcfunction title="BP/functions/wiki/scoreboard/operations/percent.mcfunction"
# result = value * 100 / max
scoreboard players operation .Result wiki:temp = .Value wiki:var
scoreboard players set .Hundred wiki:const 100
scoreboard players operation .Result wiki:temp *= .Hundred wiki:const
scoreboard players operation .Result wiki:temp /= .Max wiki:var
```

## 注意事项

- 所有运算都是**整数运算**，没有浮点数。要模拟小数，可以乘以一个基数（如1000），在输出时再换算。
- 来源持有者不存在记分时，命令会失败。建议在使用前先用`scoreboard players add ... 0`确保持有者已注册。
- 与`scoreboard players set/add/remove`不同，`operation`不能直接使用字面数值，必须先把常数存入记分持有者。

## 继续阅读

- [记分板](../../docs/general/scoreboard.md)
- [记分板计时器](./scoreboard-timers.md)
- [分数比较](./comparing-scores.md)
