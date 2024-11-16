---
title: 记分板操作
category: 一般
mentions:
    - Sprunkles137
    - Luthorius
    - MedicalJewel105
    - Hatchibombotar
description: 记分板可以用于执行复杂的操作，类似于 MoLang。操作分为两种类型：数学操作和逻辑操作。
---

记分板可以用于执行复杂的操作，类似于 [Molang](../concepts/molang.md)。操作分为两种类型：数学操作和逻辑操作。

## 概述
操作使用 `/scoreboard players operation` 命令执行。完整的语法如下：
```
/scoreboard players operation <目标分数> <目标> <操作> <源分数> <目标>
```
该命令由两个分数持有者组成：目标分数和源分数。目标分数是被操作的值，而源分数是影响操作的值。操作的结果写入目标分数，源分数的值不受影响，除了 [一个操作](../commands/scoreboard-operations.md#swap-operator)。

## 数学运算符
数学运算符使用算术运算来影响目标分数。可用的数学操作有五种：加法、减法、乘法、向下取整除法和向下取整模除法。

在以下每个示例中，假设分数持有者 `A var` 等于 25，`B var` 等于 10。

### 加法
运算符：**+=**

此操作将目标分数和源分数相加，然后将和存储到目标分数中。
```
/scoreboard players operation A var += B var
```
`A = A + B`，因此 `25 + 10 = 35`。

### 减法
运算符：**-=**

此操作将目标分数减去源分数，然后将差值存储到目标分数中。
```
/scoreboard players operation A var -= B var
```
`A = A - B`，因此 `25 - 10 = 15`。

### 乘法
运算符：**\*=**

此操作将目标分数乘以源分数，然后将积存储到目标分数中。
```
/scoreboard players operation A var *= B var
```
`A = A * B`，因此 `25 * 10 = 250`。

### 向下取整除法
运算符：**/=**

此操作将目标分数除以源分数，然后将商存储到目标分数中。由于分数值只能是整数，因此值会向下取整。
```
/scoreboard players operation A var /= B var
```
`A = floor(A / B)`，因此 `floor(25 / 10) = 2`。

### 向下取整模除法
运算符：**%=**

此操作也将目标分数除以源分数，但返回除法后的余数并存储到目标分数中。此操作同样会向下取整。
```
/scoreboard players operation A var %= B var
```
`A = floor(mod(A, B))`，因此 `floor(mod(25, 10)) = 5`。

## 逻辑运算符
逻辑操作使用逻辑门和赋值来影响目标分数。可用的逻辑操作有四种：赋值、小于、大于和交换。

与上述类似，假设分数持有者 `A var` 等于 25，`B var` 等于 10。

### 赋值运算符
运算符：**=**

此操作将目标分数设置为源分数的值。
```
/scoreboard players operation A var = B var
```
`A = B`，因此结果为 `10`。

### 最小运算符
运算符：**<**

此操作返回输入分数中最小的值，并将其存储到目标分数中。
```
/scoreboard players operation A var < B var
```
`A = min(A, B)`，因此 `min(25, 10) = 10`。

### 最大运算符
运算符：**>**

此操作返回输入分数中最大的值，并将其存储到目标分数中。
```
/scoreboard players operation A var > B var
```
`A = max(A, B)`，因此 `max(25, 10) = 25`。

### 交换运算符
运算符：**><**

此操作将目标分数和源分数的值互换。这是唯一会影响源分数的操作。
```
/scoreboard players operation A var >< B var
```
上述命令将交换 A 和 B 的值，例如：

之前：A = 10；B = 25；

之后：A = 25；B = 10；

这可以视为三个操作：`temp = A; A = B; B = temp;`，因此 `A var = 10` 和 `B var = 25`。

## 有用的创建

#### 检查值是否相等

如果你想在记分板中检查一个值是否等于另一个值，可以将第一个值复制到临时值中，减去另一个值并将临时值与零进行比较。给定值 A 和 B：

<CodeHeader></CodeHeader>

```
scoreboard objectives add temp dummy
scoreboard players operation @e temp = @s A
scoreboard players operation @e temp -= @s B
execute as @e[scores={temp=0}] run say A equals B
scoreboard objectives remove temp
```

#### 记分板初始化

如果你想将记分板值初始化为 0，但仅在其不存在时，可以使用 `scoreboard players add <选择器> <名称> 0`。如果实体上不存在该值，则将其设置为 0；如果已经存在，则不执行任何操作。