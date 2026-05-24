# 方块放置拦截<!-- md:flag vanilla -->

通过`world.beforeEvents.playerPlaceBlock`事件，脚本可以监听玩家的方块放置操作并选择性地阻止。这是实现地皮系统、领地保护等功能的基础机制。

## 基础用法

在前置方块放置事件中调用`event.cancel = true`即可阻止放置：

```javascript
import { world } from "@minecraft/server";

world.beforeEvents.playerPlaceBlock.subscribe((event) => {
    const { player, block, permutationBeingPlaced } = event;
    const blockType = permutationBeingPlaced.type.id;

    // 阻止放置TNT
    if (blockType === "minecraft:tnt") {
        event.cancel = true;
        player.sendMessage("§c该区域禁止放置TNT！");
    }
});
```

/// warning | 受限执行模式限制
`world.beforeEvents.playerPlaceBlock`是前置事件，回调内处于受限执行模式。若需要在阻止方块放置后执行修改世界状态的操作（如给玩家发送物品），需通过`system.run()`推迟执行。
///

## 按区域限制放置

结合方块坐标可以实现区域性保护：

```javascript
import { world, system } from "@minecraft/server";

const PROTECTED_REGION = {
    minX: -10, maxX: 10,
    minY: 60,  maxY: 80,
    minZ: -10, maxZ: 10,
};

function isInProtectedRegion(pos) {
    return (
        pos.x >= PROTECTED_REGION.minX && pos.x <= PROTECTED_REGION.maxX &&
        pos.y >= PROTECTED_REGION.minY && pos.y <= PROTECTED_REGION.maxY &&
        pos.z >= PROTECTED_REGION.minZ && pos.z <= PROTECTED_REGION.maxZ
    );
}

world.beforeEvents.playerPlaceBlock.subscribe((event) => {
    if (isInProtectedRegion(event.block.location)) {
        event.cancel = true;

        const player = event.player;
        system.run(() => {
            player.sendMessage("§c该位置受到保护，无法放置方块。");
        });
    }
});
```

/// tip | 配合动态属性存储保护列表
若需要动态添加或移除受保护区域，可以将区域数据存储在世界的动态属性中，并在事件回调中读取。关于动态属性的用法，请参阅[脚本核心功能](./script-core-features.md)页面。
///

## 按玩家标签限制放置

利用标签系统可以区分不同权限的玩家：

```javascript
import { world } from "@minecraft/server";

world.beforeEvents.playerPlaceBlock.subscribe((event) => {
    const { player } = event;

    // 只有拥有"builder"标签的玩家才能放置方块
    if (!player.hasTag("builder") && !player.isOp()) {
        event.cancel = true;
    }
});
```

/// note | 与方块破坏事件配合
类似的机制也可用于方块破坏拦截，对应事件为`world.beforeEvents.playerBreakBlock`。
///