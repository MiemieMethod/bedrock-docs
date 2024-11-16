---
title: 可旋转方块
category: 教程
mentions:
    - Ultr4Anubis
    - SmokeyStack
    - ihategravel2
    - MedicalJewel105
    - MajestikButter
    - QuazChick
description: 创建可旋转的方块。
---

::: tip 格式与最低引擎版本 `1.21.40`
本教程假设你对方块有基本的了解，包括 [方块状态](../blocks/block-states.md) 和 [方块特性](../blocks/block-traits.md)。
在开始之前，请查看 [方块指南](../blocks/blocks-intro.md)。
:::

## 旋转类型

-   ### [基本方向](#cardinal-direction-rotation)

    -   被雕刻南瓜和熔炉使用
    -   4 个方向 - '北'、'南'、'东' 和 '西'。

-   ### [朝向方向](#facing-direction-rotation)

    -   被发射器和观察者使用
    -   6 个方向 - '下'、'上'、'北'、'南'、'东' 和 '西'。

-   ### [方块面](#block-face-rotation)

    -   被梯子和物品框架使用
    -   6 个附着点 - '下'、'上'、'北'、'南'、'东' 和 '西'。

-   ### [原木/柱子旋转](#log-rotation)

    -   被原木和玄武岩使用
    -   3 个轴对齐方向

-   ### [精确旋转](../blocks/precise-rotation.md)
    -   被头骨、标志和横幅使用
    -   16 个方向（22.5 度倍数）
    -   4 个基本侧附着方向

## 基本方向旋转

### 特性

为了设置决定方块方向的状态，我们将使用 `minecraft:placement_direction` 方块特性，并启用 `minecraft:cardinal_direction` 状态。

<CodeHeader>minecraft:block</CodeHeader>

```json
"description": {
  "identifier": "wiki:cardinal_direction_example",
  // 方块特性在此定义
  "traits": {
    "minecraft:placement_direction": {
      "enabled_states": ["minecraft:cardinal_direction"], // 可用于查询，例如 `q.block_state('minecraft:cardinal_direction') == 'north'`
      "y_rotation_offset": 180 // 面向玩家
    }
  }
}
```

### 排列

旋转利用方块排列。每个排列包含 `minecraft:transformation` 组件，通过检查 `minecraft:cardinal_direction` 状态并应用适当的旋转来实现基本旋转。

**以下旋转值假设你的模型正面朝北。**

<CodeHeader>minecraft:block</CodeHeader>

```json
"permutations": [
  // 面朝北
  {
    "condition": "q.block_state('minecraft:cardinal_direction') == 'north'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 0, 0] }
    }
  },
  // 面朝西
  {
    "condition": "q.block_state('minecraft:cardinal_direction') == 'west'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 90, 0] }
    }
  },
  // 面朝南
  {
    "condition": "q.block_state('minecraft:cardinal_direction') == 'south'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 180, 0] }
    }
  },
  // 面朝东
  {
    "condition": "q.block_state('minecraft:cardinal_direction') == 'east'",
    "components": {
      "minecraft:transformation": { "rotation": [0, -90, 0] }
    }
  }
]
```

## 朝向方向旋转

### 特性

为了设置决定方块方向的状态，我们将使用 `minecraft:placement_direction` 方块特性，并启用 `minecraft:facing_direction` 状态。

<CodeHeader>minecraft:block</CodeHeader>

```json
"description": {
  "identifier": "wiki:facing_direction_example",
  // 方块特性在此定义
  "traits": {
    "minecraft:placement_direction": {
      "enabled_states": ["minecraft:facing_direction"], // 可用于查询，例如 `q.block_state('minecraft:facing_direction') == 'north'`
    }
  }
}
```

### 排列

旋转利用方块排列。每个排列包含 `minecraft:transformation` 组件，通过检查 `minecraft:facing_direction` 状态并应用适当的旋转来实现基本旋转。

**以下旋转值假设你的模型正面朝北。**

<CodeHeader>minecraft:block</CodeHeader>

```json
"permutations": [
  // 面朝下
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'down'",
    "components": {
      "minecraft:transformation": { "rotation": [-90, 0, 0] }
    }
  },
  // 面朝上
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'up'",
    "components": {
      "minecraft:transformation": { "rotation": [90, 0, 0] }
    }
  },
  // 面朝北
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'north'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 0, 0] }
    }
  },
  // 面朝西
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'west'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 90, 0] }
    }
  },
  // 面朝南
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'south'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 180, 0] }
    }
  },
  // 面朝东
  {
    "condition": "q.block_state('minecraft:facing_direction') == 'east'",
    "components": {
      "minecraft:transformation": { "rotation": [0, -90, 0] }
    }
  }
]
```

## 方块面旋转

### 特性

为了设置决定方块附着的状态，我们将使用 `minecraft:placement_position` 方块特性，并启用 `minecraft:block_face` 状态。

<CodeHeader>minecraft:block</CodeHeader>

```json
"description": {
  "identifier": "wiki:facing_direction_example",
  // 方块特性在此定义
  "traits": {
    "minecraft:placement_position": {
      "enabled_states": ["minecraft:block_face"], // 可用于查询，例如 `q.block_state('minecraft:block_face') == 'north'`
    }
  }
}
```

### 排列

旋转利用方块排列。每个排列包含 `minecraft:transformation` 组件，通过检查 `minecraft:block_face` 状态并应用适当的旋转来实现基本旋转。

**以下旋转值假设你的模型正面朝北。**

<CodeHeader>minecraft:block</CodeHeader>

```json
"permutations": [
  // 面朝下
  {
    "condition": "q.block_state('minecraft:block_face') == 'down'",
    "components": {
      "minecraft:transformation": { "rotation": [-90, 0, 0] }
    }
  },
  // 面朝上
  {
    "condition": "q.block_state('minecraft:block_face') == 'up'",
    "components": {
      "minecraft:transformation": { "rotation": [90, 0, 0] }
    }
  },
  // 面朝北
  {
    "condition": "q.block_state('minecraft:block_face') == 'north'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 0, 0] }
    }
  },
  // 面朝西
  {
    "condition": "q.block_state('minecraft:block_face') == 'west'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 90, 0] }
    }
  },
  // 面朝南
  {
    "condition": "q.block_state('minecraft:block_face') == 'south'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 180, 0] }
    }
  },
  // 面朝东
  {
    "condition": "q.block_state('minecraft:block_face') == 'east'",
    "components": {
      "minecraft:transformation": { "rotation": [0, -90, 0] }
    }
  }
]
```

## 原木旋转

方块旋转与原版原木的旋转方式相同。

### 特性

为了设置决定方块附着的状态，我们将使用 `minecraft:placement_position` 方块特性，并启用 `minecraft:block_face` 状态。

该状态包含的值比我们需要的原木旋转更多，因此某些排列看起来是相同的。

<CodeHeader>minecraft:block</CodeHeader>

```json
"description": {
  "identifier": "wiki:log_rotation_example",
  // 方块特性在此定义
  "traits": {
    "minecraft:placement_position": {
      "enabled_states": ["minecraft:block_face"], // 可用于查询，例如 `q.block_state('minecraft:block_face') == 'north'`
    }
  }
}
```

### 排列

旋转利用方块排列。每个排列包含 `minecraft:transformation` 组件，通过检查 `minecraft:block_face` 状态并应用适当的旋转来实现基本旋转。

<CodeHeader>minecraft:block</CodeHeader>

```json
"permutations": [
  // X 轴
  {
    "condition": "q.block_state('minecraft:block_face') == 'west' || q.block_state('minecraft:block_face') == 'east'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 0, 90] }
    }
  },
  // Y 轴
  {
    "condition": "q.block_state('minecraft:block_face') == 'down' || q.block_state('minecraft:block_face') == 'up'",
    "components": {
      "minecraft:transformation": { "rotation": [0, 0, 0] }
    }
  },
  // Z 轴
  {
    "condition": "q.block_state('minecraft:block_face') == 'north' || q.block_state('minecraft:block_face') == 'south'",
    "components": {
      "minecraft:transformation": { "rotation": [90, 0, 0] }
    }
  }
]
```