# 自定义命令<!-- md:flag vanilla -->

从`@minecraft/server` 2.1.0版本起，脚本API支持通过`system.beforeEvents.startup`注册自定义命令。自定义命令与原版命令一样可以在聊天框、命令方块和函数中使用。

## 基础注册

自定义命令必须在`system.beforeEvents.startup`的回调中注册，且只能在该事件中注册。

```javascript title="BP/scripts/Main.js"
import { system, world } from "@minecraft/server";

system.beforeEvents.startup.subscribe((event) => {
    const { customCommandRegistry: registry } = event;

    registry.registerCommand(
        {
            name: "wiki:greet",
            description: "向指定玩家发送问候",
            permissionLevel: 1,  // 0 = 管理员，1 = 任意玩家
            cheatsRequired: false,
        },
        (origin, args) => {
            const sender = origin.player ?? origin.entity;
            if (sender) {
                sender.sendMessage("你好，世界！");
            }
        }
    );
});
```

/// warning | 注册时机
`system.beforeEvents.startup`只会在脚本加载时触发一次。注册命令的代码必须在该回调内执行，不能异步延迟到`system.run()`或其他事件中。
///

## 带参数的命令

可以通过`mandatoryParameters`和`optionalParameters`配置命令参数：

```javascript
system.beforeEvents.startup.subscribe((event) => {
    const { customCommandRegistry: registry } = event;

    const { CustomCommandParamType } = event;

    registry.registerCommand(
        {
            name: "wiki:tp",
            description: "传送至指定玩家附近",
            permissionLevel: 1,
            mandatoryParameters: [
                {
                    name: "target",
                    type: CustomCommandParamType.String,
                },
            ],
            optionalParameters: [
                {
                    name: "message",
                    type: CustomCommandParamType.String,
                },
            ],
        },
        (origin, args) => {
            const [target, message] = args;
            const targetPlayer = world.getAllPlayers().find(
                (p) => p.name === target
            );
            if (!targetPlayer) {
                origin.player?.sendMessage(`找不到玩家：${target}`);
                return;
            }
            origin.player?.teleport(targetPlayer.location);
            if (message) {
                origin.player?.sendMessage(message);
            }
        }
    );
});
```

## 可用参数类型

| 类型 | `CustomCommandParamType`枚举值 | 说明 |
|------|-------------------------------|------|
| 布尔值 | `Boolean` | `true`或`false` |
| 整数 | `Integer` | 整数数字 |
| 浮点数 | `Float` | 小数数字 |
| 字符串 | `String` | 文本字符串 |
| 玩家选择器 | `PlayerSelector` | 目标选择器（玩家） |
| 实体选择器 | `EntitySelector` | 目标选择器（所有实体） |
| 方块类型 | `BlockType` | 方块类型标识符 |
| 物品类型 | `ItemType` | 物品类型标识符 |

<!-- md:sortable -->

## 权限级别

命令的`permissionLevel`控制谁可以执行该命令：

- `0`（管理员）：仅创造模式玩家或通过命令方块/函数执行时可用。对应`/gamerule sendcommandfeedback`。
- `1`（所有玩家）：生存模式玩家也可以执行。

/// tip | 命令前缀与命名空间
自定义命令必须使用命名空间前缀（如`wiki:greet`），直接使用`/wiki:greet`调用。命令的命名空间应与行为包标识符保持一致以避免冲突。
///