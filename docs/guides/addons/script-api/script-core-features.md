# 脚本核心功能<!-- md:flag vanilla -->

本页面介绍脚本API中最常用的核心功能：事件系统、任务调度、动态属性，以及`runCommand`方法。

## 事件系统

脚本API事件分为**后置事件**（afterEvents）和**前置事件**（beforeEvents）。

- **后置事件**：在游戏行为已经发生后触发，脚本只能做出响应，无法取消。
- **前置事件**：在游戏行为实际执行前触发，脚本可以通过`event.cancel = true`阻止该行为。但此时处于受限执行模式，不能修改世界状态。

### 事件来源

| 来源 | 对象 | 说明 |
|------|------|------|
| 世界事件 | `world.afterEvents` / `world.beforeEvents` | 与游戏世界直接相关的事件 |
| 系统事件 | `system.afterEvents` / `system.beforeEvents` | 与引擎运行时相关的事件 |
| 脚本事件 | `world.afterEvents.scriptEventReceive` | 通过`/scriptevent`命令触发 |

### 订阅与取消订阅

```javascript
import { world } from "@minecraft/server";

// 订阅并保存句柄
const subscription = world.afterEvents.playerSpawn.subscribe(
    ({ player, initialSpawn }) => {
        if (initialSpawn) {
            player.sendMessage(`欢迎来到服务器，${player.name}！`);
        }
    }
);

// 取消订阅
world.afterEvents.playerSpawn.unsubscribe(subscription);
```

### 脚本事件

通过`/scriptevent <命名空间:事件名> [消息]`命令可以从命令方块或聊天框向脚本发送消息：

```javascript
world.afterEvents.scriptEventReceive.subscribe((event) => {
    const { id, message, sourceType } = event;
    if (id === "wiki:greet") {
        world.sendMessage(`脚本收到问候：${message}`);
    }
});
```

在游戏中用命令触发：`/scriptevent wiki:greet 你好`

/// tip | 事件过滤器
部分事件支持通过订阅时传入过滤器对象来减少不必要的触发，例如`scriptEventReceive`支持按命名空间过滤：
```javascript
world.afterEvents.scriptEventReceive.subscribe(handler, {
    namespaces: ["wiki"]
});
```
///

## 任务调度

脚本API通过`system`对象提供了多种调度方式。

### 单次延迟（system.run / system.runTimeout）

`system.run(callback)`会在下一刻执行一次回调，是最常用的"推迟执行"手段：

```javascript
import { system } from "@minecraft/server";

system.run(() => {
    world.sendMessage("这条消息在下一刻发送。");
});
```

`system.runTimeout(callback, ticks)`可指定延迟刻数（20刻约等于1秒）：

```javascript
system.runTimeout(() => {
    world.sendMessage("3秒后发送。");
}, 60);
```

### 周期性执行（system.runInterval）

`system.runInterval(callback, ticks)`会按固定间隔重复执行，返回一个任务ID：

```javascript
const tickId = system.runInterval(() => {
    world.sendMessage("每秒广播一次。");
}, 20);

// 停止周期任务
system.clearRun(tickId);
```

### 生成器任务（system.runJob）

当需要执行耗时操作（如大范围方块扫描）而不导致卡顿时，可以使用生成器任务。脚本会在每刻只处理生成器中`yield`之前的部分，将长时任务分散到多个刻中：

```javascript
function* scanBlocks() {
    for (let x = -100; x <= 100; x++) {
        for (let z = -100; z <= 100; z++) {
            const block = world.getDimension("overworld").getBlock({ x, y: 64, z });
            if (block?.typeId === "minecraft:diamond_ore") {
                console.log(`找到钻石矿：${x}, 64, ${z}`);
            }
            yield; // 每次循环后让出控制权，下一刻继续
        }
    }
}

system.runJob(scanBlocks());
```

## 动态属性

动态属性（Dynamic Properties）允许脚本将自定义数据存储在世界或实体上，数据会随存档持久化。

### 存储与读取

```javascript
import { world } from "@minecraft/server";

// 存储到世界
world.setDynamicProperty("wiki:playerDeaths", 0);

// 读取
const deaths = world.getDynamicProperty("wiki:playerDeaths");
// 返回 number | string | boolean | Vector3 | undefined

// 存储到实体
const player = world.getAllPlayers()[0];
player.setDynamicProperty("wiki:firstLoginTime", Date.now().toString());
```

### 支持的数据类型

动态属性支持`boolean`、`number`、`string`和`Vector3`。如需存储复杂对象，可以序列化为JSON字符串：

```javascript
const data = { kills: 5, deaths: 2 };
player.setDynamicProperty("wiki:stats", JSON.stringify(data));

const raw = player.getDynamicProperty("wiki:stats");
const stats = raw ? JSON.parse(raw) : { kills: 0, deaths: 0 };
```

### 字符串属性大小限制

单个字符串属性最大为**32767字符**，超过将抛出错误。如需存储更多数据，可以将数据分段存储为多个属性。

### 枚举所有动态属性

```javascript
const keys = world.getDynamicPropertyIds();
for (const key of keys) {
    const value = world.getDynamicProperty(key);
    console.log(`${key} = ${value}`);
}
```

## runCommand

脚本可以通过`runCommand`在实体或维度上执行命令，但有一定限制。

```javascript
import { world, system } from "@minecraft/server";

world.afterEvents.playerSpawn.subscribe(({ player, initialSpawn }) => {
    if (!initialSpawn) return;

    const dimension = world.getDimension("overworld");
    const result = dimension.runCommand(
        `give ${player.name} minecraft:diamond 1`
    );
    console.log(`命令状态码：${result.successCount}`);
});
```

### 多条命令的执行

`runCommand`是同步执行的，但游戏内部处理可能有一帧延迟。若需要顺序执行多条命令且依赖上一条的结果，使用`runTimeout`间隔执行：

```javascript
system.run(() => {
    dimension.runCommand("summon minecraft:creeper 0 64 0");
    system.runTimeout(() => {
        dimension.runCommand("kill @e[type=minecraft:creeper,r=5]");
    }, 2);
});
```

### runCommand的限制

部分命令不能通过脚本的`runCommand`执行：

/// define
**`/fog`**

- 脚本无法管理玩家的迷雾设置。

**`/stopsound`**

- 脚本无法通过命令停止音效。音乐可以使用`World.stopMusic()`或`Player.stopMusic()`停止。

**`/dialogue`**

- 没有专用的脚本方法控制NPC对话，但可以用`player.runCommand("dialogue open @e[tag=npc,r=5] @s 场景标签")`作为变通方案。

///