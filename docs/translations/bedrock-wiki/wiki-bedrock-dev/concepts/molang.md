---
title: MoLang
tags:
    - 中级
mentions:
    - yanasakana
    - TheDoctor15
    - MedicalJewel105
    - DoubleShotgun
    - Luthorius
    - TheItsNameless
description: 什么是MoLang？
---

## 介绍

几乎所有内容都可以计算为一个数字；如果某个内容无法计算为数字，你可以使用一个`运算符`将其转换为数字。你可以将Molang视为一个大型数学方程式。

当返回的数字不是`0`时，方程式的结果为`true`。当我提到`返回`时，我指的是方程式的输出。还有一个`return`语句，但我通常不使用它，因此不会讨论它。

## 访问值

在Molang中，有三种主要方式来访问和使用值（查询、变量和临时变量）

- **查询**是游戏返回的只读值。你不能设置这些值，只能读取它们。(`query.example_query` | `q.example_query`)

- **变量**是可以读写的值，你可以对其进行操作，这些值可以通过Molang进行设置和读取。(`variable.example_variable` | `v.example_variable`)
    - 还有一些硬编码变量，它们的作用与查询几乎相同，但只能在特定情况下使用。

- **临时变量**与变量几乎相同，除了它们只存在于当前作用域中。(`temp.example_temp` | `t.example_temp`)
    - “作用域”可以指当前的`for_each`或`loop`，*或者*仅指当前表达式，如果它不在这两者之内使用。

## 处理值

- **逻辑运算符**可用于将非数字转换为1或0。这些运算符包括：`==`、`!=`、`<`、`>`、`<=`、`>=`。
    - 示例："`q.get_equipped_item_name == 'stick'`" 当持有一根木棍时，将计算为`1`/`true`

    - 还有一组*第二*逻辑运算符，可用于将值“分组”成`与/或`语句，通常在需要*多个*条件为`true`或仅*一个*条件为`true`的情况下使用。`&&`表示`与`语句，`||`表示`或`语句。
        - 示例："`q.is_sneaking && q.is_using_item`" 当同时潜行*和*使用物品时，将计算为`1`/`true`
        - 示例："`q.is_sneaking || q.is_jumping`" // 当潜行*或*跳跃时，将计算为`1`/`true`

- **括号**，`( )`，在分组值或执行数学运算时也非常有帮助。
    - 示例："`q.is_sneaking && (q.get_equipped_item_name == "stick" || q.get_equipped_item_name == "diamond")`" 当潜行*并*持有一根木棍*或*一颗钻石时，将计算为`1`/`true`

- **条件运算符**可以用作`if/else`语句。
    - *二元*条件运算符指的是仅使用`?`。当使用此运算符时，它将根据给定输入值是否为`true`输出你的值或`0`。
        - 示例："`q.is_sneaking ? 5`" 当潜行时输出`5`，否则返回`0`
    - *三元*条件运算符指的是使用`?`和`:`。当使用此运算符时，它将根据给定输入值是否为`true`输出两个给定值中的一个。
        - 示例："`q.is_sneaking ? 10 : 3`" 当潜行时输出`10`，否则返回`3`