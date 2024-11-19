---
title: 物品事件
description: 物品事件在满足特定条件时触发。创作者可以在这些事件触发时挂钩，以修改游戏世界。
category: 一般
nav_order: 4
tags:
    - 脚本
mentions:
    - SmokeyStack
---

/// tip | 格式版本 `1.21.40`
在创建自定义物品时使用最新的格式版本可以访问新的功能和改进。维基旨在分享关于自定义物品的最新信息，目前针对格式版本 `1.21.40`。
///

## 注册自定义组件

物品事件在满足特定条件时触发，可以在**自定义组件**中“监听”，这些组件在世界加载之前在脚本中注册。

在每个自定义组件中，列出事件处理函数（例如 [`onBeforeDurabilityDamage`](#onBeforeDurabilityDamage)）以配置每个事件触发时希望发生的事情。

_此示例在击打实体时防止物品受到耐久度损伤：_

```js title="BP/scripts/unbreakable_component.js"
import { world } from "@minecraft/server";

const UnbreakableItemComponent = {
    onBeforeDurabilityDamage(event) {
        event.durabilityDamage = 0;
    },
};

world.beforeEvents.worldInitialize.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent("wiki:unbreakable", UnbreakableItemComponent);
});
```

## 应用自定义组件

要将自定义组件绑定到自定义物品，只需在物品 JSON 中的 [`minecraft:custom_components`](/items/item-components#custom-components) 组件中列出它们。

```json title="minecraft:item"
"components": {
    "minecraft:custom_components": ["wiki:unbreakable"]
}
```

## 事件列表

### 耐久度损伤前

当包含此组件的物品击打实体并即将受到耐久度损伤时，将调用此事件。

```js title="自定义组件"
onBeforeDurabilityDamage(event) {
    event.attackingEntity // 攻击实体。
    event.durabilityDamage // 事件发生时施加于物品耐久度的损伤。
    event.hitEntity // 被击中的实体。
    event.itemStack // 用于击打实体的物品堆叠。
}
```

### 完成使用

/// tip | 依赖项
完成使用事件需要在你的物品上激活 [`minecraft:use_modifiers`](/items/item-components#use-modifiers) 组件才能触发。
///

当包含此组件的物品的使用持续时间完成时，将调用此事件。

```json title="minecraft:item > components"
"minecraft:use_modifiers": {
    "use_duration": 5
}
```

```js title="自定义组件"
onCompleteUse(event) {
    event.itemStack // 返回已完成充能的物品堆叠。
    event.source // 返回触发此物品事件的源实体。
}
```

### 消耗

当包含此组件的物品被实体食用时，将调用此事件。

/// tip | 依赖项
完成使用事件需要在你的物品上激活 [`minecraft:use_modifiers`](/items/item-components#use-modifiers) 和 [`minecraft:food`](/items/item-components#food) 组件才能触发。
///

```json title="minecraft:item > components"
"minecraft:food": {},
"minecraft:use_modifiers": {
    "use_duration": 5
}
```

```js title="自定义组件"
onConsume(event) {
    event.itemStack // 被消耗的物品堆叠。
    event.source // 消耗该物品的源实体。
}
```

### 击打实体

当包含此组件的物品被用于击打另一个实体时，将调用此函数。

```js title="自定义组件"
onHitEntity(event) {
    event.attackingEntity // 攻击实体。
    event.hadEffect // 是否击中并产生了效果。
    event.hitEntity // 被击中的实体。
    event.itemStack // 用于击打实体的物品堆叠。
}
```

### 挖掘区块

当包含此组件的物品被用于挖掘一个区块时，将调用此函数。

```js title="自定义组件"
onMineBlock(event) {
    event.block // 此事件影响的区块。
    event.itemStack // 用于挖掘区块的物品堆叠。
    event.minedBlockPermutation // 被挖掘的区块排列。
    event.source // 挖掘区块的实体。
}
```

### 使用

当包含此组件的物品被玩家使用时，将调用此函数。

```js title="自定义组件"
onUse(event) {
    event.itemStack // 使用物品时的物品堆叠。
    event.source // 使用物品的玩家。
}
```

### 在区块上使用

当包含此组件的物品在一个区块上使用时，将调用此函数。

```js title="自定义组件"
onUseOn(event) {
    event.source // 在区块上使用物品的实体。
    event.usedOnBlockPermutation // 物品使用的区块排列。
}
```