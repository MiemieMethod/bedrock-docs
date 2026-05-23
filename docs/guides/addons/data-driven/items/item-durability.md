# 物品耐久

物品耐久是物品在使用若干次后损坏的机制。本篇将介绍如何为自定义物品配置耐久，以及通过脚本API精确控制每次扣耗的耐久量。

## 基础配置

在物品的`components`中添加`minecraft:durability`组件：

```json title="BP/items/my_tool.json（节选）"
"components": {
    "minecraft:durability": {
        "max_durability": 300,
        "damage_chance": {
            "min": 60,
            "max": 100
        }
    }
}
```

/// define
`max_durability`

- 物品的最大耐久值。物品耐久耗尽时会损坏。

`damage_chance`

- 每次使用时扣除耐久的概率范围（%）。默认100%必定扣耐久。指定`min`和`max`后，游戏会随机取范围内的一个值。
///

/// info | 耐久损耗逻辑
原版耐久损耗：
- 攻击实体：+2点损耗
- 破坏方块：+1点损耗
- 使用物品（如食物、弓、三叉戟等）：+1点损耗

这是原版行为。如果使用脚本API监听`onHitEntity`/`onMineBlock`手动扣除耐久，则原版自动扣耐久依旧会触发——请注意不要双重扣耐久。
///

## 脚本控制耐久

### 注册自定义组件

若需要更精细的耐久逻辑（如命中不同生物扣不同量、破坏不同方块扣不同量），可使用脚本API中的`onBeforeDurabilityDamage`事件拦截并修改耐久损耗值：

```js title="BP/scripts/tool_durability.js"
import { system } from "@minecraft/server";

const ToolDurabilityComponent = {
    /**
     * 攻击实体前触发，可修改耐久扣减量
     */
    onBeforeDurabilityDamage({ attackingEntity, hitEntity, itemStack, durabilityDamage }, { params }) {
        // 攻击Boss类生物时扣3，其他扣1
        const isStrong = hitEntity?.hasTag?.("boss") ?? false;
        return { durabilityDamage: isStrong ? 3 : 1 };
    },
};

system.beforeEvents.startup.subscribe(({ itemComponentRegistry }) => {
    itemComponentRegistry.registerCustomComponent(
        "wiki:tool_durability",
        ToolDurabilityComponent
    );
});
```

```json title="物品 JSON（components 中添加）"
"wiki:tool_durability": {}
```

### 主动设置耐久

通过Script API主动读写物品耐久：

```js
// 读取当前耐久
const durabilityComponent = itemStack.getComponent("minecraft:durability");
const current = durabilityComponent.maxDurability - durabilityComponent.damage;

// 扣除N点耐久（不考虑damage_chance）
durabilityComponent.damage = Math.min(
    durabilityComponent.damage + n,
    durabilityComponent.maxDurability
);
```

## 修复物品

通过`minecraft:repairable`组件定义在铁砧中修复所需的材料：

```json title="BP/items/my_tool.json（components 中添加）"
"minecraft:repairable": {
    "repair_items": [
        {
            "items": ["minecraft:iron_ingot"],
            "repair_amount": "context.other->q.remaining_durability + 0.05 * context.other->q.max_durability"
        }
    ]
}
```

`repair_amount`是一个Molang表达式：
- `context.other->q.remaining_durability`：修复材料自身的剩余耐久（用于工具修复工具的场景）
- `context.other->q.max_durability`：当前物品的最大耐久
- `0.05 * context.other->q.max_durability`：每个铁锭修复5%最大耐久（原版标准）

## 已移除的旧版组件

/// warning | 已在新版本移除
- `on_hurt_entity`（格式版本1.20.40起移除）：旧版用于物品攻击实体后的响应，现须使用脚本API的`onHitEntity`事件。
- `on_dig`（格式版本1.20.20起移除）：旧版用于物品破坏方块后的响应，现须使用脚本API的`onMineBlock`事件。

若你的知识库中看到含有这两个字段的示例，请注意其已不可用于当前版本。
///