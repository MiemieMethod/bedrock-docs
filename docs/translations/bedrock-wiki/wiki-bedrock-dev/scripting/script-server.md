---
title: 脚本核心功能
category: 教程
tags:
    - 实验性
mentions:
    - JaylyDev
    - SmokeyStack
    - ThomasOrs
    - kumja1
description: 对部分核心API机制的介绍。
---

::: warning
脚本API目前正在积极开发中，且经常有重大变更。本页面基于Minecraft 1.21.20版本的格式。
:::

在脚本API中，大多数核心功能都在 `@minecraft/server` 模块中实现，该模块包含许多与Minecraft世界交互的方法，包括实体、方块、维度等。本文对部分核心API机制进行了基本介绍。欲了解更详细的信息，请访问 [微软文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server) 页面。

## 设置

你需要在你的 `manifest.json` 中将脚本模块添加为依赖项。

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
    "dependencies": [
        {
            "module_name": "@minecraft/server",
            "version": "1.13.0"
        }
    ]
}
```

## 事件

在脚本API中，`@minecraft/server` 模块使用其自身的事件驱动架构，通过订阅事件监听器，可以在特定事件发生时执行代码。

**世界事件**

世界事件API提供了许多事件监听器，当Minecraft世界中发生特定类型的事件时触发，例如 `chatSend`、`entityHurt`、`playerSpawn`、`worldInitialize` 等等。

::: tip
查看微软文档以了解Minecraft中可用的世界事件。

-   事件前触发器会在事件发生前触发，且为只读但可以被取消。 [事件前文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/worldbeforeevents)。
-   事件后触发器会在事件执行后触发，且不能被取消。 [事件后文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/worldafterevents)
-   除非需要取消事件，否则应始终使用事件后触发器。
:::

为了订阅事件，需要从世界对象中获取 `afterEvents` 属性。在这个例子中，我们将订阅破坏方块事件。

```js
import { world } from "@minecraft/server";

// 订阅破坏方块事件
// 当玩家破坏方块时触发
world.afterEvents.playerBreakBlock.subscribe((event) => {
    const player = event.player; // 触发此事件的玩家。
    const block = event.block; // 受影响的方块。注意，此方块的 typeId 将始终为 air。
    const permutation = event.brokenBlockPermutation; // 在方块被破坏前的排列信息。
    player.sendMessage(
        `你在 (${block.x}, ${block.y}, ${block.z}) 破坏了 ${permutation.type.id}`
    ); // 向玩家发送消息。
});
```

**系统事件**

系统事件在Minecraft附加包系统范围内发生特定类型的事件时触发。

::: tip
查看微软文档以了解Minecraft中可用的系统事件。

-   事件前触发器会在事件发生前触发，且为只读但可以被取消。 [事件前文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/systembeforeevents)。
-   事件后触发器会在事件执行后触发，且不能被取消。 [事件后文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/systemafterevents)
-   两种类型的事件用于不同的目的。
:::

从系统对象中获取 `beforeEvents` 属性。在这个例子中，我们将订阅 watchdogTerminate 事件，允许API在游戏超出性能边界时取消性能看门狗关闭世界，具体取决于脚本环境的配置。

```js
import { system } from "@minecraft/server";

// 订阅 watchdogTerminate 事件
system.beforeEvents.watchdogTerminate.subscribe((event) => {
    event.cancel = true; // 取消关闭世界。这样将终止脚本引擎。
    console.warn("取消了类型为 " + event.terminateReason + " 的关键异常"); // 如果此事件触发，向控制台打印消息。
});
```

**脚本事件**

脚本事件，不同于世界事件或系统事件，允许我们通过注册 `scriptEventReceive` 事件处理器来响应入站的 `/scriptevent` 命令，当玩家、NPC 或方块调用 `/scriptevent` 命令时触发。更多关于此事件的信息可以在 [脚本事件文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/scripteventcommandmessageafterevent) 页面找到。

```
/scriptevent <messageId: string> <message: string>
```

-   `messageId` 在 scriptevent 命令中可以通过 `ScriptEventCommandMessageEvent.id` 在API中接收。
-   `message` 在 scriptevent 命令中可以通过 `ScriptEventCommandMessageEvent.message` 在API中接收。

**示例**：

命令输入：

```
/scriptevent wiki:test Hello World
```

事件监听器返回：

```js
import { system } from "@minecraft/server";

system.afterEvents.scriptEventReceive.subscribe((event) => {
    const {
        id, // 返回字符串 (wiki:test)
        initiator, // 返回 Entity（如果NPC未触发命令，则为 undefined）
        message, // 返回字符串 (Hello World)
        sourceBlock, // 返回 Block（如果方块未触发命令，则为 undefined）
        sourceEntity, // 返回 Entity（如果实体未触发命令，则为 undefined）
        sourceType, // 返回 MessageSourceType（可以是 'Block'、'Entity'、'NPCDialogue' 或 'Server'）
    } = event;
});
```

## 调度

我们可能会决定在将来的某个时间点执行一个函数。这被称为“调度调用”。

在脚本API中，像 `setTimeout` 和 `setInterval` 这样的原生JavaScript方法在脚本引擎中不存在。Minecraft 取而代之的是实现了自己的调度方法，这些方法使用游戏刻（tick）而非实时时间。

这些方法可以通过导入获得的 `system` 对象访问：

```js
import { system } from "@minecraft/server";
```

有两种方法：

**调度计时器**
`system.run(callback)` - 在下一个可用的未来时间运行指定的函数。这通常用于实现延迟行为和游戏循环。在事件处理器的上下文中运行时，通常会在事件发生的同一刻结束时运行代码。在其他代码（system.run 调用）中运行时，这将在下一个刻运行函数。然而，请注意，根据系统负载，运行在同一刻或下一个刻并不保证。

```js
import { system, world } from "@minecraft/server";

system.run(() => {
    world.sendMessage("这将在前一刻之后运行一个刻");
});
```

`system.runInterval(callback: () => void, tickInterval?: number): number` - 重复运行一组代码，首次执行在第一个时间间隔后开始，并持续以该间隔不断重复。

```js
import { system, world } from "@minecraft/server";

system.runInterval(() => {
    world.sendMessage("此消息每20刻运行一次（每秒一次）");
}, 20);
```

`system.runTimeout(callback: () => void, tickDelay?: number): number` - 在时间间隔经过后运行一次函数。

```js
import { system, world } from "@minecraft/server";

system.runTimeout(() => {
    world.sendMessage("此消息将在20刻后运行一次。");
}, 20);
```

`system.runJob(generator: Generator<void, void, void>): number` - 将生成器函数排队运行直到完成。生成器每刻将获得一个时间片，并将运行直到yield或完成。[生成器函数参考](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*)。

```js
import { system, world, BlockPermutation } from "@minecraft/server";

function* blockPlacingGenerator(size, startX, startY, startZ) {
    const overworld = world.getDimension("overworld"); // 获取类型为 overworld 的维度。
    for (let x = startX; x < startX + size; x++) {
        for (let y = startY; y < startY + size; y++) {
            for (let z = startZ; z < startZ + size; z++) {
                const block = overworld.getBlock({ x: x, y: y, z: z }); // 获取当前循环坐标的方块。
                if (block) block.setType("minecraft:cobblestone"); // 如果方块已加载，则将其设置为鹅卵石。
                // 在每放置一个方块后yield回到作业协调器
                yield;
            }
        }
    }
}
// 从 overworld 位置 -2, -60, 1 开始构建一个10x10x10的鹅卵石立方体。
system.runJob(blockPlacingGenerator(10, -2, -60, 1));
```

**清除计时器**

`system.clearRun(runId): void` - 取消先前通过 `run`、`runTimeout` 或 `runInterval` 函数调度的函数运行。

```js
import { system, world } from "@minecraft/server";

const callbackId = system.runInterval(() => {
    world.sendMessage("每刻运行一次");
});

system.runTimeout(() => {
    system.clearRun(callbackId); // 在20刻后停止 system.runInterval 回调的运行
    world.sendMessage("已停止");
}, 20);
```

`clearJob(jobId: number): void` - 取消通过 `runJob` 函数排队的作业的执行。

```js
import { system, world } from "@minecraft/server";

const callbackId = system.runInterval(() => {
    world.sendMessage("每刻运行一次");
});

system.runTimeout(() => {
    system.clearRun(callbackId); // 在20刻后停止 system.runInterval 回调的运行
    world.sendMessage("已停止");
}, 20);
```

关于所有系统方法的更多信息，请参阅 [游戏循环与定时回调](https://learn.microsoft.com/en-us/minecraft/creator/documents/systemrunguide) 文档页面。

## 保存和加载数据

通过 `@minecraft/server` 模块，开发者可以定义自己的自定义属性，称为动态属性，可以在Minecraft中使用和存储。这些数据专门存储在世界的 db 文件夹中，使用行为包模块的 UUID。

![dynamic_properties](/assets/images/gametest/script-server/dynamic_properties.png)

为了保存数据，必须先初始化属性。有多种方式声明动态属性，可以在实体、世界或物品上声明。你可以定义任意数量的数字和布尔值属性，然而Minecraft API仅允许每个行为包在每个动态属性上保存有限数量的数据。

-   字符串动态属性的最大长度为32767个字符。
-   数字动态属性的最大值为64位浮点数限制（-1.7976931348623158e+308 到 -2.2250738585072014e-308，或从2.2250738585072014e-308到1.7976931348623158e+308）。

**获取和设置动态属性**

要获取和设置动态属性，可以使用 `getDynamicProperty` 和 `setDynamicProperty` 方法。

:::tip
请注意，获取动态属性并不保证其有保存的值。第一次获取属性时，方法会返回 `undefined`。
:::

考虑到这一点，以下是如何在Minecraft中获取和设置动态属性的一些示例：

```js
import { system, world } from "@minecraft/server";

system.runInterval(() => {
    world.getPlayers().forEach((player) => {
        // 对数组返回的每个玩家运行代码。
        // 所有三个属性对每个玩家都是唯一的，类似于标签/记分板数据。
        player.setDynamicProperty("number_value", 12); // 在玩家上设置一个数字属性。
        player.setDynamicProperty("string_value", "这是一个字符串 :)"); // 字符串属性
        player.setDynamicProperty("boolean_value", true); // 布尔属性
    });
}, 20); // 每20个游戏刻运行一次此间隔。

world.afterEvents.playerBreakBlock.subscribe((data) => {
    // 订阅破坏方块事件。
    const player = data.player; // 定义稍后使用的玩家变量。
    const numberProperty = player.getDynamicProperty("number_value"); // 获取已保存的动态属性。
    player.sendMessage(`你有一个值为 ${numberProperty} 的属性！`); // 将玩家保存的值打印到聊天中。
});
```

以下是如何在全局级别获取和设置动态属性的示例：

```js
import { world } from "@minecraft/server";

world.setDynamicProperty("player_score", 100); // 设置一个数字值的属性
const playerScore = world.getDynamicProperty("player_score"); // 获取先前设置的属性 - 将返回100。
```

## 运行命令

`Entity.runCommandAsync()` 或 `Dimension.runCommandAsync()` 允许API在更广泛的维度上下文中异步运行特定命令。请注意，在给定刻中最多可以运行128个异步命令。尽可能避免使用 runCommandAsync 调用，而应使用内置API方法。

游戏在世界的下一个刻执行排队的命令。要与脚本并行运行命令，必须将代码包裹在异步函数中。

```js
import { world } from "@minecraft/server";

(async () => {
    await world.getDimension("overworld").runCommandAsync("say 使用维度中的 say 命令。");

    world.sendMessage("这将在 runCommandAsync 执行后运行");
})();
```

返回一个 `Promise<CommandResult>`。如果队列已满，将**同步**抛出错误。

**避免在脚本中运行命令**

通常建议避免使用命令，因为从脚本API运行命令速度较慢，并且随着时间的推移执行更多命令会导致服务器性能下降。然而，以下命令功能尚未在脚本API中实现，这使我们不得不使用 `runCommand` 或 `runCommandAsync`。

**末影箱**

脚本API没有提供任何方法来获取/设置玩家末影箱的信息。可以使用 `/replaceitem`、`/clear`、`@s[hasitem=]`等命令作为替代方案。

**tickingarea**

脚本API无法访问、设置或移除计区块区域。

**踢出玩家**

脚本API无法踢出玩家。

**设置方块**

脚本API无法摧毁方块 `/setblock ... destroy`。然而，可以设置方块。

**玩家能力**

-   脚本API无法为每个玩家设置能力。
-   你无法读取玩家的能力。

**执行**

脚本API可以利用新的执行语法，通过大量 if/unless 条件简化或提高性能来运行命令。

`/execute` 可以用于触发 `/loot` 命令，因为 `runCommandAsync` 无法直接访问原版战利品表。

**Minecraft 函数**

-   脚本API无法在不使用 `/function` 的情况下运行Minecraft函数文件。

**定位**

-   脚本API无法获取结构的位置。
-   无法获取生物群系的位置。

**战利品**

-   虽然战利品从一开始就被打破，但它对于给玩家/世界掉落或设置物品有用。

**天气**

-   脚本API无法获取/设置世界天气。

**难度**

-   脚本API无法设置世界难度。

**mobevent**

-   脚本API无法启用/禁用mobevent。

**雾**

-   脚本API无法管理玩家的活动雾设置。

**停止声音**

-   脚本API无法停止播放声音。可以使用 `World::stopMusic()` 或 `Player::stopMusic()` 停止音乐。

**对话**

-   脚本API无法向玩家打开NPC对话。
-   它无法更改NPC显示的对话。

## BeforeEvents 权限系统

::: tip
开发者可能会在微软文档中发布讨论此主题的文章，但目前这是社区收集的信息。
:::

在1.20.0版本中，Minecraft脚本API为事件前触发器（如 `ChatSendBeforeEvent`）中的回调发布了权限系统。

这限制了允许在事件前触发器回调中执行的本地函数。这些是允许在同一刻修改世界的本地函数（如使用 `World::setTimeOfDay()` 设置世界时间）。此实现的目的是避免在游戏刻中间发生级联更改。

```js
import { world } from "@minecraft/server";

world.beforeEvents.chatSend.subscribe((event) => {
    event.cancel = true;
    world.setTimeOfDay(0);
});
```

在上面的示例代码中，发送到聊天的消息被取消，世界的时间被设置。`world.setTimeOfDay()` 会抛出一个错误，因为该本地函数没有所需的权限来更改世界状态。

要将代码迁移到这个新系统，必须在事件触发后的下一刻运行这些需要权限的本地函数，使用以下方法：

1. 使用 `system.run`:

```js
import { world, system } from "@minecraft/server";

world.beforeEvents.chatSend.subscribe((event) => {
    event.cancel = true;
    system.run(() => {
        world.setTimeOfDay(0);
    });
});
```

要将代码迁移到新的权限系统，`world.setTimeOfDay()` 函数被包裹在 `system.run()` 方法中，这延迟了其执行一个刻。这确保了函数不会在事件前触发器同一刻执行。

2. 使用 `system.runTimeout`:

```js
import { world, system } from "@minecraft/server";

world.beforeEvents.chatSend.subscribe(async (event) => {
    event.cancel = true;
    system.runTimeout(() => {
        world.setTimeOfDay(0);
    }, 5);
});
```

此代码与使用 `system.run()` 的示例非常相似，但可以在超时中指定自定义长度，允许更好地控制代码的执行时间。

3. 使用 `async` 函数在稍后的刻执行函数：

```js
import { world } from "@minecraft/server";

world.beforeEvents.chatSend.subscribe(async (event) => {
    // 同步代码
    event.cancel = true;

    // 异步代码
    await sleep(10); // 假装你有一个返回在10刻后解决的Promise的sleep函数
    world.setTimeOfDay(0);
});
```

通过使用等待超过一个刻的 `async` 函数，可以绕过权限系统。因为 `await` 之前的代码是同步运行的，所以事件可以使用 `event.cancel = true` 被取消，而在后续刻中，操作可以继续进行。请注意，仅使用异步/等待调用是不够的，因为以这种方式运行的代码在使用阻塞调用（如示例中的 `sleep()` 函数）之前仍然是同步执行的。