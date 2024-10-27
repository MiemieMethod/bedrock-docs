---
title: .mcstructure
category: 一般
mentions:
    - SirLich
    - MedicalJewel105
    - Misledwater79
    - SmokeyStack
description: 关于 .mcstructure 格式。
---

[int]: /assets/images/nbt/int.png
[list]: /assets/images/nbt/list.png
[compound]: /assets/images/nbt/compound.png
[string]: /assets/images/nbt/string.png

### 保存与加载

**导出**按钮会在结构方块中创建 `.mcstructure` 文件。这些文件必须放置在行为包中，以便在游戏中通过加载结构方块加载它们。路径决定了结构标识符，该标识符需输入到结构方块中以加载结构。

**示例：**
`BP/structures/house.mcstructure` → `mystructure:house`
`BP/structures/dungeon/entrance.mcstructure` → `dungeon:entrance`
`BP/structures/stuff/towers/diamond.mcstructure` → `stuff:towers/diamond`

第一个子文件夹定义了命名空间，后续文件夹定义了路径，最后是结构文件的名称。

请注意，任何直接放在 `structures` 文件夹中的文件都将被赋予 `mystructure` 命名空间。如果在 `structures` 文件夹中存在一个结构，并且与 `mystructure` 文件夹中的结构同名，游戏将生成以下内容日志警告：

```
[structure][warning]-在默认命名空间加载结构时发生冲突。在根目录和 mystructure 目录中都找到了名称为 <name> 的结构。
```

在这种情况下，`mystructure` 文件夹中的文件将“胜出”，导致直接在 `structures` 文件夹中的文件被忽略。

### 文件格式

`mcstructure` 文件是未压缩的 [NBT 文件](https://wiki.vg/NBT#Specification)。与所有基岩版 NBT 文件一样，它们以小端格式存储。标签结构如下：

> ![整数][int] `format_version`：当前始终设置为 `1`。
>
> ![列表][list] `size`：包含三个整数的列表，描述结构的边界大小。
>
> > ![整数][int] 结构在 X 方向的大小。
> >
> > ![整数][int] 结构在 Y 方向的大小。
> >
> > ![整数][int] 结构在 Z 方向的大小。
>
> ![复合][compound] `structure`：实际数据复合。
>
> > ![列表][list] `block_indices`：包含两个子列表的列表，每个层一个。这些包含结构中的方块。每个方块作为一个整数索引存储在调色板中（见下文）。从最低角落到最高角落按 ZYX 顺序进行。例如，如果结构大小为 `[2,3,4]`，则每个层列表中的 24（维度的乘积）个值表示位于 `[(0,0,0), (0,0,1), (0,0,2), (0,0,3), (0,1,0), (0,1,1), (0,1,2), (0,1,3), (0,2,0), (0,2,1), (0,2,2), (0,2,3), (1,0,0), (1,0,1), (1,0,2), (1,0,3), (1,1,0), (1,1,1), (1,1,2), (1,1,3), (1,2,0), (1,2,1), (1,2,2), (1,2,3)]` 相对于原点的位置。索引值等于 `-1` 表示没有方块，导致加载时任何现有方块保持不变。这发生在保存结构空洞时，并且是第二层中大多数方块的情况。两个层共享相同的调色板。
> >
> > > ![列表][list] 的 ![整数][int] 主层方块的索引。
> > >
> > > ![列表][list] 的 ![整数][int] 次层方块的索引。此层通常为空，除非当此处的方块被水淹没时。
> >
> > ![列表][list] 的 ![复合][compound] `entities`：作为 NBT 存储的实体列表，存储方式与世界文件中的实体完全相同。像 `Pos` 和 `UniqueID` 这样的标签被保存，但在加载时会被替换。
> >
> > ![复合][compound] `palette`：包含多个命名调色板，可能是为了支持同一结构的多个变体。然而，目前仅保存和加载 `default`。
> >
> > > ![复合][compound] 单个调色板（当前仅命名为 `default`）。
> > >
> > > > ![列表][list] `block_palette`：方块状态列表。此列表包含方块索引所指向的有序条目。
> > > >
> > > > > ![复合][compound] 单个方块状态。
> > > > >
> > > > > > ![字符串][string] `name`：方块的标识符，例如 `minecraft:planks`。
> > > > > > ![复合][compound] `states`：方块的状态作为键值对。示例：`wood_type:"acacia"`、`bite_counter:3`、`open_bit:1b`。值为状态的适当 NBT 类型：字符串用于枚举值，整数用于标量数字，字节用于布尔值。
> > > > > > ![整数][int] `version`：此方块的兼容性版本号（截至撰写时为 `17959425`，在 1.19 中）。
> > > >
> > > > ![复合][compound] `block_position_data`：包含结构中单个方块的附加数据。每个键是 `block_indices` 中扁平化方块列表的整数索引。层是未指定的，因为它无关紧要。
> > > >
> > > > > ![复合][compound] `<index>`：应用于其索引位置的单个附加方块数据。
> > > > >
> > > > > > ![复合][compound] `block_entity_data`：作为 NBT 存储的方块实体数据，存储方式与世界文件中的方块实体相同。位置标签被保存，但在加载时会被替换。目前似乎没有其他对象与此对象相邻。
>
> ![列表][list] `structure_world_origin`：包含三个整数的列表，描述结构最初保存时在世界中的位置。等于保存结构方块的位置，加上其偏移设置。这用于确定加载时实体应放置的位置。实体的新绝对位置等于其旧位置减去这些值，加上结构加载位置的原点。
>
> > ![整数][int] 结构原点 X 位置。
> > ![整数][int] 结构原点 Y 位置。
> > ![整数][int] 结构原点 Z 位置。

### 如果发生...

测试修改后的结构文件加载时会发生什么的结果：

- 如果 `size` 中的维度超过原版保存限制 `64*256*64`，结构仍然可以按预期加载。
- 如果方块层列表中的值不是整数标签，所有值都将被视为 `0`。
- 如果方块层列表中的值等于或大于调色板大小或小于 `-1`，则放置一个空气方块。
- 如果 `default` 调色板不存在，加载结构将导致没有方块被放置。
- 如果任何具有常量名称的标签未指定或标签类型错误，结构加载失败，并出现以下内容日志错误：

```
[Structure][error]-加载结构 '<identifier>` 来自行为包: '<path>' | "<tag>" 字段，必填字段，缺失于结构中。
```

- 如果 `block_indices` 不包含恰好两个值，结构加载失败，并出现以下内容日志错误：

```
[Structure][error]-加载结构 '<identifier>` 来自行为包: '<path>' | "block_indices" 字段应为包含 2 个数组的数组，而我们有 <count> 个数组。
```

- 如果 `block_indices` 中的值不列出标签，结构加载失败，并出现以下内容日志错误：

```
[Structure][error]-加载结构 '<identifier>` 来自行为包: '<path>' | "block_indices" 字段的第一个数组缺失或不是列表。
```

- 如果 `block_indices` 中的两个列表长度不相等，结构加载失败，并出现以下内容日志错误：

```
[Structure][error]-加载结构 '<identifier>` 来自行为包: '<path>' | "block_indices" 字段的数组需要大小相同。
```

- 如果 `block_indices` 中的两个列表长度不等于结构维度的乘积，结构加载失败，并出现以下内容日志错误：

```
[Structure][error]-加载结构 '<identifier>` 来自行为包: '<path>' | "block_indices" 字段应具有与 "size" 字段定义的元素数量相同的元素。
```

## NBT 编辑器

您可以在 [这里](../meta/useful-links.md#software-installed) 找到一些 NBT 编辑器的下载链接。

---

[原始来源](https://gist.github.com/tryashtar/87ad9654305e5df686acab05cc4b6205)