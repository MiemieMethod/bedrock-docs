# 物品事件

物品事件（item event）在特定条件发生时被触发。开发者通过在**自定义组件**中注册事件处理函数来监听这些事件，从而在事件触发时修改游戏状态。自定义组件在世界加载前由脚本注册。

/// tip | 格式版本
自定义组件需要格式版本1.21.90或以上，同时需要`@minecraft/server`模块版本2.0.0或以上。
///

## 注册自定义组件

在脚本的`system.beforeEvents.startup`阶段，通过`itemComponentRegistry.registerCustomComponent`注册组件。在自定义组件对象中，列出你希望监听的事件处理函数：

```js title="BP/scripts/item_components.js"
import { system } from "@minecraft/server";

/** @type {import("@minecraft/server").ItemCustomComponent} */
const ItemUnbreakableComponent = {
    onBeforeDurabilityDamage(event) {
        event.durabilityDamage = 0; // 阻止耐久损耗
    },
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent(
        "wiki:unbreakable",
        ItemUnbreakableComponent
    );
});
```

## 绑定自定义组件

在物品JSON的`components`中引用自定义组件标识符：

```json title="BP/items/my_item.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:my_item"
        },
        "components": {
            "wiki:unbreakable": {}
        }
    }
}
```

## 传递参数

自定义组件也可以接受来自JSON的参数，通过事件的第二个参数（`componentParameters`）访问：

```json title="BP/items/my_item.json (components)"
"wiki:colored_lore": {
    "color": "§a",
    "text": "这是一把神奇的剑"
}
```

```js title="BP/scripts/item_components.js"
const ItemColoredLoreComponent = {
    onUse({ source }, { params }) {
        const { color, text } = params;
        source.sendMessage(`${color}${text}`);
    },
};
```

## 事件一览

### `onBeforeDurabilityDamage`

物品攻击实体即将受到耐久损耗时触发。可修改`durabilityDamage`来增减耐久损耗量：

```js
onBeforeDurabilityDamage(event) {
    const { attackingEntity, durabilityDamage, hitEntity, itemStack } = event;
    event.durabilityDamage = 0; // 设为0即无敌
}
```

### `onCompleteUse`

物品的`use_duration`充能完成时触发（需配合`minecraft:use_modifiers`）：

```json title="需要在组件中配置"
"minecraft:use_modifiers": {
    "use_duration": 3.0
}
```

```js
onCompleteUse(event) {
    const { itemStack, source } = event;
    // source 是使用该物品的玩家实体
    source.sendMessage("充能完毕！");
}
```

### `onConsume`

物品被食用（消耗）时触发（需配合`minecraft:food`和`minecraft:use_modifiers`）：

```json title="需要在组件中配置"
"minecraft:food": {},
"minecraft:use_modifiers": { "use_duration": 1.6 }
```

```js
onConsume(event) {
    const { itemStack, source } = event;
    source.addEffect("speed", 200, { amplifier: 1 });
}
```

### `onHitEntity`

持有该物品攻击其他实体时触发：

```js
onHitEntity(event) {
    const { attackingEntity, hadEffect, hitEntity, itemStack } = event;
    if (hadEffect) {
        // 命中有效，可在此添加击中逻辑
        hitEntity.applyDamage(5);
    }
}
```

### `onMineBlock`

持有该物品挖掘方块时触发：

```js
onMineBlock(event) {
    const { block, itemStack, minedBlockPermutation, source } = event;
    // minedBlockPermutation 是被挖掘方块的置换信息
    source.sendMessage(`挖掘了 ${minedBlockPermutation.type.id}`);
}
```

### `onUse`

玩家对空气使用（右键/长按）该物品时触发：

```js
onUse(event) {
    const { itemStack, source } = event;
    // source 是使用物品的玩家
    source.teleport({ x: 0, y: 64, z: 0 });
}
```

### `onUseOn`

玩家将物品对准方块使用时触发：

```js
onUseOn(event) {
    const { source, usedOnBlockPermutation } = event;
    const blockId = usedOnBlockPermutation.type.id;
    source.sendMessage(`对 ${blockId} 使用了物品`);
}
```

## 综合示例：带效果的食物

结合`onConsume`，可以实现食用后给予多种状态效果的自定义食物：

```js title="BP/scripts/food_effects.js"
import { system } from "@minecraft/server";

const ItemFoodEffectsComponent = {
    onConsume({ source }, { params }) {
        for (const { name, duration, amplifier } of params) {
            source.addEffect(name, duration, { amplifier });
        }
    },
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent(
        "wiki:food_effects",
        ItemFoodEffectsComponent
    );
});
```

```json title="BP/items/magic_apple.json (components)"
"minecraft:food": {},
"minecraft:use_modifiers": { "use_duration": 1.6 },
"wiki:food_effects": [
    { "name": "regeneration", "duration": 100, "amplifier": 1 },
    { "name": "absorption",   "duration": 2400, "amplifier": 1 }
]
```

详细的食物物品制作流程参见[自定义食物](custom-food.md)。