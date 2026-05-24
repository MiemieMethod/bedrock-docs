# 脚本执行权限<!-- md:flag vanilla -->

脚本API的不同执行阶段对API的访问权限有严格限制。理解这些限制可以避免最常见的`ReferenceError: Native function [Class::method] does not have required privileges.`错误。

## 受限执行模式

**受限执行模式（Restricted-Execution Mode）**，也称为只读模式，是指脚本不允许修改世界状态的执行状态。在Minecraft模拟开始时、事件触发之前，或脚本刻开始之前，脚本都处于受限执行状态。

在前置事件的回调函数中，脚本始终处于受限执行模式。如果在此状态下调用了修改世界状态的API，就会抛出上述错误。

### 脱离受限执行模式

最简单的解决方式是将所有需要修改世界状态的代码移入`system.run()`回调中。下面是一个在前置事件中尝试显示表单的示例：

```javascript
import { system, world } from "@minecraft/server";
import { MessageFormData } from "@minecraft/server-ui";

world.beforeEvents.playerInteractWithBlock.subscribe((event) => {
    if (
        event.block.typeId === "minecraft:crafter" &&
        event.itemStack &&
        event.itemStack.typeId === "minecraft:diamond"
    ) {
        event.cancel = true;

        const form = new MessageFormData()
            .title("合成台")
            .body("这是一个合成台！")
            .button1("关闭");

        // 错误：.show()不能在受限执行模式中调用
        // form.show(event.player);

        // 必须先保存玩家引用，因为事件对象在受限状态结束后会失效
        const player = event.player;

        // 用system.run()推迟到当前刻结束后执行
        system.run(() => {
            form.show(player);
        });

        // sendMessage不受受限执行模式限制，可以直接调用
        player.sendMessage("你正在使用合成台。");
    }
});
```

/// warning | 事件对象的生命周期
在前置事件回调中，如果需要在`system.run()`内使用`event.player`等属性，必须在回调内先将其赋值给独立变量。受限状态结束后，事件对象会被清空，直接在`system.run()`内访问`event.player`会得到`undefined`。
///

/// tip | 查阅API参考
API参考文档中明确标注了哪些方法或属性不能在受限执行模式中使用：
- 方法描述中带有"This function **can't be called** in read-only mode."
- 属性描述中带有"This property **can't be edited** in read-only mode."
///

## 早期执行模式

**早期执行模式（Early-Execution Mode）**是指脚本在世界加载完成之前运行的阶段。此时大多数API（如`world.getAllPlayers()`、`world.getDimension()`等世界状态查询）尚不可用。

从脚本API 2.0.0版本开始，脚本文件的顶层代码（根上下文）会在世界加载之前执行，这是与旧版行为的重要差异。

如果在早期执行模式中调用了需要世界已加载的API，也会产生权限错误。

### 脱离早期执行模式

将需要在世界加载后执行的代码移入`world.afterEvents.worldLoad`回调，或移入`system.run()`中。事件订阅本身可以在顶层代码中注册，不必等待世界加载。

```javascript
import { world } from "@minecraft/server";

// 事件订阅可以在顶层注册——这在早期执行模式中是合法的
world.afterEvents.playerSpawn.subscribe(({ player, initialSpawn }) => {
    if (!initialSpawn) return;
    player.sendMessage(`欢迎，${player.name}！`);
});

// world.getAllPlayers()需要等世界加载完成
world.afterEvents.worldLoad.subscribe(() => {
    for (const player of world.getAllPlayers()) {
        player.sendMessage(`服务器已重载，欢迎回来，${player.name}！`);
    }
});
```

/// tip | 早期执行模式下可用的API
以下API可以在早期执行模式中使用：
- `world.beforeEvents.*.subscribe/unsubscribe`
- `world.afterEvents.*.subscribe/unsubscribe`
- `system.afterEvents.*.subscribe/unsubscribe`
- `system.beforeEvents.*.subscribe/unsubscribe`
- `system.clearJob`、`system.clearRun`
- `system.run`、`system.runInterval`、`system.runJob`、`system.runTimeout`、`system.waitTicks`
- `BlockComponentRegistry.registerCustomComponent`
- `ItemComponentRegistry.registerCustomComponent`
///

/// tip | 查阅API参考
API参考文档中会标注哪些方法或属性可以在早期执行模式中使用：
- 方法描述中带有"This function **can be called** in early-execution mode."
- 属性描述中带有"This property **can be read** in early-execution mode."
///