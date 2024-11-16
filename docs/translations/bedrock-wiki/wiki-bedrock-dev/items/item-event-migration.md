---
title: 物品事件迁移
description: 查看已弃用的 JSON 物品事件响应的脚本 API 实现。
category: 一般
nav_order: 5
tags:
    - 帮助
mentions:
    - QuazChick
---

:::tip 开始之前
本页面要求你对基本的 JavaScript 有一定了解，并需要掌握现代 [物品事件](/items/item-events) 的工作原理。
:::

在将你的物品 JSON 事件升级为 [自定义组件](/items/item-events#registering-custom-components) 时遇到困难吗？别担心！本页面将帮助你理解已弃用的 JSON 事件响应在脚本 API 中的实现方式。

## 添加生物效果

<CodeHeader>自定义组件</CodeHeader>

```js
onHitEntity({ hitEntity }) {
    hitEntity.addEffect("regeneration", 30, {
        amplifier: 10,
        showParticles: false
    });
}
```

## 伤害（持有者）

```js
import { EntityDamageCause } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onUse({ source }) {
    source.applyDamage(2, {
        cause: EntityDamageCause.drowning
    });
}
```

## 伤害（物品）

```js
import { EquipmentSlot, GameMode, Player } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onMineBlock({ source }) {
    // 获取主手槽
    if (!(source instanceof Player)) return;

    const equippable = source.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    if (!mainhand.hasItem()) return;

    // 在非创造模式下应用耐久损伤
    if (source.getGameMode() === GameMode.creative) return;

    const itemStack = mainhand.getItem(); // 允许我们获取物品组件

    const durability = itemStack.getComponent("minecraft:durability");
    if (!durability) return;

    // 考虑无敌附魔
    const enchantable = itemStack.getComponent("minecraft:enchantable");
    const unbreakingLevel = enchantable?.getEnchantment("unbreaking")?.level;

    const damageChance = durability.getDamageChance(unbreakingLevel) / 100;

    if (Math.random() > damageChance) return; // 根据无敌等级随机跳过伤害

    // 对物品造成伤害
    const shouldBreak = durability.damage === durability.maxDurability;

    if (shouldBreak) {
        mainhand.setItem(undefined); // 移除物品
        source.playSound("random.break"); // 播放破碎声音
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
onUse({ source }) {
    if (!source) return;

    const equippable = source.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);
    if (!mainhand.hasItem()) return;

    if (source.getGameMode() !== GameMode.creative) {
        if (mainhand.amount > 1) {
            mainhand.amount--; // 从堆叠中移除一个物品
        } else {
            mainhand.setItem(undefined); // 移除物品堆叠
        }
    }
}
```

## 移除生物效果

<CodeHeader>自定义组件</CodeHeader>

```js
onHitEntity({ hitEntity }) {
    hitEntity.removeEffect("regeneration");
}
```

## 执行命令

<CodeHeader>自定义组件</CodeHeader>

```js
onUse({ source }) {
    source.runCommand("say Hello there!")
    source.runCommand("say Welcome to my world!")
}
```

## 传送

<CodeHeader>自定义组件</CodeHeader>

```js
onConsume({ source }) {
    source.teleport({ x: 100, y: 20, z: 786 });
}
```

## 转换物品

```js
import { EquipmentSlot, ItemStack } from "@minecraft/server";
```

<CodeHeader>自定义组件</CodeHeader>

```js
onUse({ source }) {
    const equippable = source?.getComponent("minecraft:equippable");
    if (!equippable) return;

    const mainhand = equippable.getEquipmentSlot(EquipmentSlot.Mainhand);

    mainhand.setItem(new ItemStack("minecraft:suspicious_stew"));
}
```