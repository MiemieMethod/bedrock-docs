---
title: 方块事件
description: 方块事件在满足特定条件时触发。创作者可以通过这些事件来修改游戏世界。
category: 一般
nav_order: 8
tags:
    - 脚本
mentions:
    - SirLich
    - solvedDev
    - yanasakana
    - MedicalJewel105
    - aexer0e
    - SmokeyStack
    - TheDoctor15
    - XxPoggyisLitxX
    - TheItsNameless
    - ThomasOrs
    - QuazChick
    - VactricaKing
    - BlazeDrake
---

:::tip 格式版本 `1.21.40`
在创建自定义方块时使用最新的格式版本可以访问新功能和改进。维基旨在分享关于自定义方块的最新信息，目前目标格式版本为 `1.21.40`。
:::

## 注册自定义组件

方块事件在满足特定条件时触发，可以在**自定义组件**中“监听”，这些组件在世界加载之前通过脚本注册。

在每个自定义组件中，事件处理函数（如 [`beforeOnPlayerPlace`](#before-player-place)）被列出以配置每个事件触发时希望发生的事情。

_此示例防止玩家在非创造模式下放置方块：_

```js title="BP/scripts/creative_mode_only_component.js"
import { world, GameMode } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const CreativeModeOnlyBlockComponent = {
    beforeOnPlayerPlace(event) {
        const isInCreative = event.player?.getGameMode() === GameMode.creative;
        if (!isInCreative) event.cancel = true;
    },
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:creative_mode_only",
        CreativeModeOnlyBlockComponent
    );
});
```

## 应用自定义组件

要将自定义组件绑定到自定义方块，只需在方块 JSON 中的 [`minecraft:custom_components`](../blocks/block-components.md#custom-components) 组件中列出它们。

与任何普通组件一样，自定义组件可以根据方块的 [排列](../blocks/block-permutations.md) 添加或移除。

```json title="minecraft:block"
"components": {
    "minecraft:custom_components": ["wiki:creative_mode_only"]
}
```

## 事件列表

### 玩家放置之前

在玩家放置方块之前运行。

```js title="自定义组件"
beforeOnPlayerPlace(event) {
    event.block // 此事件影响的方块。即将被替换的方块。
    event.cancel // 如果设置为 true，取消放置方块事件。
    event.dimension // 包含该方块的维度。
    event.face // 被放置的方块面。
    event.permutationToPlace // 将要放置的方块排列。可以更改为放置不同的排列。
    event.player // 放置此方块的玩家。可能为未定义。
}
```

### 实体落在上面

:::tip 依赖项
实体落在上面的事件需要在方块上激活 [`minecraft:entity_fall_on`](../blocks/block-components.md#entity-fall-on) 组件才能触发。

实体落在上面的事件要求 [`minecraft:collision_box`](../blocks/block-components.md#collision-box) 组件在 Y 轴上为 4 或更高才能触发。
:::

当实体落在方块上时运行。

```json title="minecraft:block > components"
"minecraft:entity_fall_on": {
    "min_fall_distance": 5 // 实体必须下落的最小距离以触发此事件（可选）。
}
```

```js title="自定义组件"
onEntityFallOn(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
    event.entity // 踏上方块的实体。可能为未定义。
    event.fallDistance // 实体落地前下落的距离。
}
```

### 放置

当方块被放置时运行。

```js title="自定义组件"
onPlace(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
    event.previousBlock // 被替换方块的排列。
}
```

### 玩家破坏

当玩家破坏方块时运行。

```js title="自定义组件"
onPlayerDestroy(event) {
    event.block // 此事件影响的方块。即被破坏后的方块。
    event.destroyedBlockPermutation // 被破坏前方块的排列。
    event.dimension // 包含该方块的维度。
    event.player // 破坏方块的玩家。可能为未定义。
}
```

### 玩家交互

当玩家与方块交互/使用方块时运行。

```js title="自定义组件"
onPlayerInteract(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
    event.face // 与之交互的方块面。
    event.faceLocation // 相对于方块的底部西北角的交互位置。
    event.player // 与方块交互的玩家。可能为未定义。
}
```

### 随机滴答

在每个随机滴答时触发，允许实现随机作物生长等行为。

```js title="自定义组件"
onRandomTick(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
}
```

### 脚步离开

:::tip 依赖项
脚步离开事件要求 [`minecraft:collision_box`](../blocks/block-components.md#collision-box) 组件在 Y 轴上为 4 或更高才能触发。
:::

当实体离开方块时运行。

```js title="自定义组件"
onStepOff(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
    event.entity // 踏上方块的实体。可能为未定义。
}
```

### 脚步踩上

:::tip 依赖项
脚步踩上事件要求 [`minecraft:collision_box`](../blocks/block-components.md#collision-box) 组件在 Y 轴上为 4 或更高才能触发。
:::

当实体踩上方块时运行。

```js title="自定义组件"
onStepOn(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
    event.entity // 踏上方块的实体。可能为未定义。
}
```

### 滴答

:::tip 依赖项
滴答事件要求在方块上激活 [`minecraft:tick`](../blocks/block-components.md#tick) 组件才能触发。
:::

在方块的 [`minecraft:tick`](../blocks/block-components.md#tick) 组件的 `interval_range` 内的 X 和 Y 次滴答之间触发。

```json title="minecraft:block > components"
"minecraft:tick": {
    "interval_range": [10, 20],
    "looping": true
}
```

```js title="自定义组件"
onTick(event) {
    event.block // 此事件影响的方块。
    event.dimension // 包含该方块的维度。
}
```