# 构建第一个脚本<!-- md:flag vanilla -->

这一课的目标很小：让行为包加载一个脚本文件，并让它每隔10秒在聊天栏输出一句话。只要这一步能跑通，后面的事件监听、方块操作、实体生成和小游戏逻辑都只是继续往这个入口里添加代码。

## 准备行为包

你需要一个已经能被游戏加载的行为包。可以使用自己的测试行为包，也可以使用官方示例行为包。为了让行为包拥有脚本入口，需要在`manifest.json`里做两件事：

1. 在`modules`数组中加入一个`type`为`script`的模块。
2. 在`dependencies`数组中加入`@minecraft/server`模块依赖。

下面是最小化示例。`uuid`必须替换成你自己生成的UUID；`@minecraft/server`的版本需要与你目标Minecraft版本支持的模块版本一致，示例保留官方入门文档中的写法。

```json title="manifest.json" hl_lines="14-20 24-27"
{
  "format_version": 2,
  "header": {
    "name": "My Script Pack",
    "description": "My first script behavior pack.",
    "uuid": "PUT-A-NEW-UUID-HERE",
    "version": [1, 0, 0],
    "min_engine_version": [1, 20, 30]
  },
  "modules": [
    {
      "type": "data",
      "uuid": "PUT-A-NEW-UUID-HERE",
      "version": [1, 0, 0]
    },
    {
      "type": "script",
      "language": "javascript",
      "uuid": "PUT-A-NEW-UUID-HERE",
      "version": [1, 0, 0],
      "entry": "scripts/main.js"
    }
  ],
  "dependencies": [
    {
      "module_name": "@minecraft/server",
      "version": "1.5.0"
    }
  ]
}
```

/// tip | 入口文件路径要完全一致
如果`entry`写的是`scripts/main.js`，行为包根目录下就必须存在`scripts`文件夹和`main.js`文件。文件名大小写、扩展名和路径层级都要对应。
///

## 编写入口脚本

在行为包根目录创建`scripts`文件夹，再创建`scripts/main.js`。写入下面的代码：

```javascript title="scripts/main.js"
import { world, system } from "@minecraft/server";

system.runInterval(() => {
  world.sendMessage("脚本正在运行。当前刻：" + system.currentTick);
}, 200);
```

这段代码做了三件事：

- `import`从`@minecraft/server`导入`world`和`system`。
- `system.runInterval`按固定刻间隔执行回调函数。Minecraft通常每秒运行20刻，因此200刻大约是10秒。
- `world.sendMessage`向世界中的玩家发送聊天消息。

## 进入游戏测试

1. 把行为包放入开发行为包目录，或用你平时的附加包部署流程导入。
2. 新建一个测试世界，并在行为包列表中启用这个行为包。
3. 进入世界后等待约10秒，聊天栏应出现脚本输出。

如果没有输出，先检查三处：

- `manifest.json`是否是合法JSON。
- `modules`中的脚本模块是否有`entry`字段。
- `scripts/main.js`是否位于行为包根目录下的`scripts`文件夹中。

## 使用热重载

脚本开发不必每次都完全退出游戏。修改`main.js`并保存后，可以在世界中执行：

```text
/reload
```

如果脚本文件能被重新加载，游戏会提示函数和脚本文件已重载。然后等待下一次`runInterval`触发即可看到新消息。

/// warning | 不要只依赖某一个绝对刻
官方入门示例提醒过，如果逻辑只在`system.currentTick === 400`时执行，那么这个世界错过第400刻后就不会再次触发。教程中使用`runInterval`是为了让逻辑重复运行，更适合热重载和调试。
///

## 脚本API 2.0.0与世界加载事件

从`@minecraft/server` 2.0.0版本起，脚本在世界完全加载之前就开始执行。这意味着如果你的脚本在顶层（模块根上下文）直接调用`world.getAllPlayers()`或`world.getDimension()`等依赖世界状态的API，会得到一个权限错误。

解决办法是将这类代码移入`world.afterEvents.worldLoad`的回调中：

```javascript title="scripts/main.js"
import { world } from "@minecraft/server";

// 事件订阅可以在顶层注册
world.afterEvents.playerSpawn.subscribe(({ player }) => {
    player.sendMessage("你好！");
});

// 需要世界已加载才能运行的代码放在这里
world.afterEvents.worldLoad.subscribe(() => {
    world.sendMessage("世界已加载，脚本正常运行。");
});
```

/// tip | 何时需要worldLoad
如果你的脚本只注册事件监听器而不立即访问世界状态，不需要`worldLoad`。只有当顶层代码需要直接调用依赖世界已加载的API时才需要此模式。
///

## 关于模块版本

`manifest.json`的`dependencies`中声明的`@minecraft/server`版本号决定了你能使用哪些API。版本越新功能越多，但同时要求玩家使用对应版本的Minecraft：

- **稳定版**（如`"2.6.0"`）：不需要启用实验性功能，建议大多数附加包使用。
- **测试版**（如`"2.7.0-beta"`）：需要在世界设置中启用"测试版API"实验性功能，API可能随时变化，不适合发布的附加包。

/// tip | 如何确定应使用的版本
在对应版本Minecraft的官方Microsoft Learn文档页面，每个API描述都会标明该API从哪个模块版本起可用。使用最新的稳定版即可获得最完整的稳定API支持。
///

## 下一步：改成一个小互动

确认消息能输出后，可以试着订阅物品使用事件。下面的示例会在玩家使用物品时给使用者发送一条消息：

```javascript title="scripts/main.js"
import { world } from "@minecraft/server";

world.afterEvents.itemUse.subscribe((event) => {
  event.source.sendMessage("你刚刚使用了：" + event.itemStack.typeId);
});
```

`world.afterEvents`中的事件回调会在事件发生后执行，通常处于默认执行权限下；不过，具体能否修改世界状态仍以各API自身权限要求为准。多人游戏中不要假设只有一个玩家，优先使用事件参数中的`event.source`、`event.player`等对象来确定真正触发事件的玩家。