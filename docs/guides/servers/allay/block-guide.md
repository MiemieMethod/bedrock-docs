---
comments: true
---

# 方块API

本指南介绍了Allay方块API的核心概念，并展示了实际的方式来查找方块类型、使用方块状态和属性，以及在维度中读写方块。

**你将学到：**

- 关键概念：方块、方块类型、方块状态、方块属性类型、方块行为
- 如何获取方块类型和方块状态
- 如何在维度中读取和设置方块
- 使用方块属性和图层

## 关键概念

### 方块

一个不可变的数据对象，代表维度中特定位置（和图层）的方块。它包装一个方块状态并添加维度位置/图层实用程序。

```java linenums="1"
// "在这个位置，方块是什么，我可以对它做什么？"
Block block = new Block(dimension, x, y, z);
BlockState state = block.getBlockState();
boolean isOpen = block.getPropertyValue(BlockPropertyTypes.OPEN_BIT);
```

### 方块类型

描述一种方块（例如，石头、泥土、箱子）。每个方块类型：

- 拥有可能状态和属性的集合
- 提供默认状态和所有已知状态
- 与定义其逻辑的方块行为相关联

```java linenums="1"
BlockType<?> stoneType = BlockTypes.STONE;
BlockState defaultStone = stoneType.getDefaultState();
BlockBehavior behavior = stoneType.getBlockBehavior();
```

### 方块类型静态字段

一个方便的类，为所有已知的原版方块类型提供静态字段。非常适合快速访问，无需手动查找标识符。

```java linenums="1"
BlockType<?> air = BlockTypes.AIR;
BlockType<?> stone = BlockTypes.STONE;
BlockType<?> oakDoor = BlockTypes.OAK_DOOR;
```

### 方块状态

方块类型的具体、不可变状态（例如"橡木门，打开=假，朝向=北"）。

- 状态是**单例对象**：可以安全地用`==`比较
- 携带一个方块属性类型->值的映射
- 支持`setPropertyValue()`来产生新状态（不变性）

```java linenums="1"
BlockState closedDoor = BlockTypes.OAK_DOOR.getDefaultState();
BlockState openDoor = closedDoor.setPropertyValue(BlockPropertyTypes.OPEN_BIT, true);
// closedDoor != openDoor（不同的状态）
```

## 读取方块

```java linenums="1"
// 在维度中读取方块
Block block = dimension.getBlock(x, y, z);
BlockState state = block.getBlockState();
BlockType<?> type = state.getBlockType();

// 检查方块类型
if (type == BlockTypes.STONE) {
    player.sendMessage("这是石头！");
}
```

## 设置方块

```java linenums="1"
// 获取方块状态
BlockState stoneState = BlockTypes.STONE.getDefaultState();

// 在维度中设置方块
dimension.setBlockState(x, y, z, stoneState);
```

## 更多信息

详细的方块API参考，请访问[Allay官方文档](https://docs.allaymc.org/)。

