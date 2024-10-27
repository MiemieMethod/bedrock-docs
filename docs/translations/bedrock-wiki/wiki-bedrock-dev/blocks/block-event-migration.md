---
title: 区块事件迁移
description: 查看已弃用的 JSON 区块事件响应的脚本 API 实现。
category: 一般
nav_order: 9
tags:
    - 帮助
mentions:
    - QuazChick
---

:::tip 开始之前
此页面要求您对基本 JavaScript 感到熟悉，并了解现代 [区块事件](../blocks/block-events.md) 的工作原理。
:::

在将您的区块 JSON 事件升级为 [自定义组件](../blocks/block-events.md#registering-custom-components) 时遇到困难吗？别担心！本页面将帮助您理解已弃用的 JSON 事件响应在脚本 API 中的实现方式。

## 添加生物效果

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ entity }) {
    entity?.addEffect("regeneration", 30, {
        amplifier: 10,
        showParticles: false
    });
}
```

## 伤害（实体）

```js
import { EntityDamageCause } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ entity }) {
    entity?.applyDamage(2, {
        cause: EntityDamageCause.drowning
    });
}
```

## 伤害（物品）

```js
import { EquipmentSlot, GameMode } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onPlayerInteract({ player }) {
    // 获取主手槽
    if (!player) return;

    const equippable = player.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    if (!mainhand.hasItem()) return;

    // 在非创造模式下应用耐久损伤
    if (player.getGameMode() === GameMode.creative) return;

    const itemStack = mainhand.getItem(); // 允许我们获取物品组件

    const durability = itemStack.getComponent("minecraft:durability");
    if (!durability) return;

    // 考虑耐久附魔
    const enchantable = itemStack.getComponent("minecraft:enchantable");
    const unbreakingLevel = enchantable?.getEnchantment("unbreaking")?.level;

    const damageChance = durability.getDamageChance(unbreakingLevel) / 100;

    if (Math.random() > damageChance) return; // 根据耐久等级随机跳过损伤

    // 物品损坏
    const shouldBreak = durability.damage === durability.maxDurability;

    if (shouldBreak) {
        mainhand.setItem(undefined); // 移除物品
        player.playSound("random.break"); // 播放破坏声音
    } else {
        durability.damage++; // 增加耐久损伤
        mainhand.setItem(itemStack); // 更新主手中的物品
    }
}
```

## 减少堆叠

```js
import { EquipmentSlot, GameMode } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onPlayerInteract({ player }) {
    if (!player) return;

    const equippable = player.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    if (!mainhand.hasItem()) return;

    if (player.getGameMode() !== GameMode.creative) {
        if (mainhand.amount > 1) {
            mainhand.amount--; // 从堆叠中移除一个物品
        } else {
            mainhand.setItem(undefined); // 移除物品堆叠
        }
    }
}
```

## 死亡（区块）

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ block }) {
    block.setType("minecraft:air");
}
```

## 死亡（实体）

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ entity }) {
    entity?.kill();
}
```

## 播放效果

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    dimension.spawnParticle("minecraft:campfire_smoke_particle", block.center());
}
```

## 播放声音

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    dimension.playSound("dig.stone", block.center());
}
```

## 移除生物效果

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ entity }) {
    entity?.removeEffect("regeneration");
}
```

## 执行命令

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension }) {
    dimension.runCommand("say Hello there!");
    dimension.runCommand("say Welcome to my world!");
}
```

## 设置区块

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ block }) {
    block.setType("minecraft:grass_block");
}
```

```js
import { BlockPermutation } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ block }) {
    block.setPermutation(BlockPermutation.resolve("minecraft:campfire", {
        "minecraft:cardinal_direction": "east",
        "extinguished": true
    }));
}
```

## 在位置设置区块

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    const offset = { x: -1, y: 1, z: 5 };

    const locationWithOffset = {
        x: block.location.x + offset.x,
        y: block.location.y + offset.y,
        z: block.location.z + offset.z
    };

    dimension.setBlockType(locationWithOffset, "minecraft:grass_block");
}
```

```js
import { BlockPermutation } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    const offset = { x: -1, y: 1, z: 5 };

    const locationWithOffset = {
        x: block.location.x + offset.x,
        y: block.location.y + offset.y,
        z: block.location.z + offset.z
    };

    dimension.setBlockPermutation(locationWithOffset, BlockPermutation.resolve("minecraft:campfire", {
        "minecraft:cardinal_direction": "east",
        "extinguished": true
    }));
}
```

## 设置区块状态

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ block }) {
    block.setPermutation(
        block.permutation.withState("wiki:integer_example", 5)
    );
}
```

```js
import { BlockPermutation } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ block }) {
    const states = {
        ...block.permutation.getAllStates(),
        "wiki:boolean_example": false,
        "wiki:integer_example": 5,
        "wiki:string_example": "blue"
    };

    block.setPermutation(
        BlockPermutation.resolve(block.typeId, states)
    );
}
```

## 生成战利品

```js
import { ItemStack } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    dimension.spawnItem(new ItemStack("minecraft:stick", 3), block.center());
}
```

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ dimension, block }) {
    const { x, y, z } = block.center();

    dimension.runCommand(`loot spawn ${x} ${y} ${z} loot "entities/ghast"`);
}
```

## 传送

<CodeHeader>自定义组件</CodeHeader>

```js
onStepOn({ entity }) {
    entity?.teleport({ x: 100, y: 20, z: 786 });
}
```

## 转换物品

```js
import { EquipmentSlot, ItemStack } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onPlayerInteract({ player }) {
    const equippable = player?.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    if (!mainhand.hasItem() || mainhand.typeId !== "minecraft:bowl") return;

    mainhand.setItem(new ItemStack("minecraft:suspicious_stew"));
}
```