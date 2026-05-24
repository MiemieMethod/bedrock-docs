# 注册自定义命令

SerenityJS提供了强大的自定义命令注册工具，可以在服务器实例中使用。本指南将指导你完成创建自定义命令的全过程，包括定义其属性和重载。

## 命令注册基础

在SerenityJS中，命令与世界关联。这意味着不同的世界可以拥有各自独立的命令集。要注册命令，首先需要确定要将其注册到哪个世界，这通过访问世界实例的`commandPalette`属性来实现。下面是一个简单自定义命令的示例。

> **在这些示例中，我们需要一个`World`实例来注册命令。**

在第一个例子中，我们将创建一个名为`ping`的简单命令，执行时会返回"Pong!"。这个命令不需要任何参数，任何命令发送者都可以执行。

```typescript
import { World } from "@serenityjs/core";

// 为给定的世界注册一个命令的函数
function register(world: World): void {
  // 在这个示例中，我们将注册一个简单的命令"ping"
  // 执行时会返回"Pong!"

  // 命令通过世界实例的"commandPalette"属性来注册
  world.commandPalette.register(
    "ping", // 命令的名称
    "Ping the server to check if it's responsive.", // 命令的简短描述
    // 当没有重载匹配时的默认执行器函数
    () => {
      return {
        message: "Pong!"
      };
    }
  );
}
```

在下一个示例中，我们将为命令分配额外的权限。SerenityJS提供了一个权限系统，允许你根据命令发送者的权限来限制命令的访问。在本例中，我们将`ping`命令限制为只能由具有`example.ping`权限的玩家执行。

```typescript
import { World } from "@serenityjs/core";

// 为给定的世界注册一个命令的函数
function register(world: World): void {
  // 在这个示例中，我们将注册一个简单的命令"ping"
  // 执行时会返回"Pong!"

  // 命令通过世界实例的"commandPalette"属性来注册
  world.commandPalette.register(
    "ping", // 命令的名称
    "Ping the server to check if it's responsive.", // 命令的简短描述
    // 这个函数被称为注册器函数
    // 它允许你定义命令的额外属性
    // 以及用于不同参数结构的重载
    (registry) => {
      // 为该命令分配权限
      registry.permissions = ["example.ping"];

      // 注册器对象还允许你将命令标记为调试命令
      // 这意味着命令在游戏内命令列表中会显示为蓝色
      // 功能上，这不会改变任何东西
      registry.debug = true;
    },
    // 当没有重载匹配时的默认执行器函数
    () => {
      return {
        message: "Pong!"
      };
    }
  );
}
```

在下一个示例中，我们将创建一个具有重载的命令。重载允许你定义命令的不同参数结构。这意味着你可以有多种方式执行同一命令，每种方式都有自己的参数集。在本例中，我们为`ping`命令创建一个重载，该重载接受一个名为`target`的单个字符串参数。执行时，命令会返回"Pong, {target}!"。

```typescript
import { TargetEnum, World } from "@serenityjs/core";

// 为给定的世界注册一个命令的函数
function register(world: World): void {
  // 在这个示例中，我们将注册一个简单的命令"ping"
  // 执行时会返回"Pong!"

  // 命令通过世界实例的"commandPalette"属性来注册
  world.commandPalette.register(
    "ping", // 命令的名称
    "Ping the server to check if it's responsive.", // 命令的简短描述
    // 这个函数被称为注册器函数
    // 它允许你定义命令的额外属性
    // 以及用于不同参数结构的重载
    (registry) => {
      // 为该命令分配权限
      registry.permissions = ["example.ping"];

      // 注册器对象还允许你将命令标记为调试命令
      // 这意味着命令在游戏内命令列表中会显示为蓝色
      // 功能上，这不会改变任何东西
      registry.debug = true;

      // 为命令注册一个重载
      registry.overload(
        {
          // 我们定义了一个名为"target"的参数
          // 你可以在此处找到所有可用参数类型的列表：https://www.serenityjs.net/classes/_serenityjs_core.Enum.html
          target: [TargetEnum, false] // false表示该参数不是可选的
        },
        // 该重载的执行器函数
        ({ target }) => {
          // 验证target参数
          if (!target.result || target.result?.length > 1) {
            // 如果参数无效则抛出错误
            throw new Error(
              "Invalid target argument, expected a single value."
            );
          }

          // 获取target参数的值
          const value = target.result[0].isPlayer()
            ? target.result[0].username
            : target.result[0].type.identifier;

          // 返回响应消息
          return {
            message: `Pong, ${value}!`
          };
        }
      );
    },
    // 当没有重载匹配时的默认执行器函数
    () => {
      return {
        message: "Pong!"
      };
    }
  );
}
```

在下一个示例中，我们将创建一个使用自定义枚举的命令，以及一个目标参数。该命令还将演示如何使用命令上下文的`origin`属性来获取有关命令发送者的信息。在本例中，我们将创建一个名为`kit`的命令，该命令将`beginner | intermediate | professional`项目套件分配给`target`参数。

```typescript
import { CustomEnum, Player, TargetEnum, World } from "@serenityjs/core";

// 为kit参数创建一个自定义枚举
class KitEnum extends CustomEnum {
  public static readonly identifier = "kit_enum";
  public static readonly options = ["beginner", "intermediate", "professional"];
}

// 为给定的世界注册一个命令的函数
function register(world: World): void {
  // 在这个示例中，我们将注册一个命令"kit"
  // 该命令会给玩家分配一个项目套件

  // 命令通过世界实例的"commandPalette"属性来注册
  world.commandPalette.register(
    "kit", // 命令的名称
    "Give a kit to a player.", // 命令的简短描述
    // 这个函数被称为注册器函数
    // 它允许你定义命令的额外属性
    // 以及用于不同参数结构的重载
    (registry) => {
      // 为该命令分配权限
      registry.permissions = ["serenity.operator"];

      // 为命令注册一个重载
      registry.overload(
        {
          target: TargetEnum, // 接收套件的玩家
          kit: KitEnum // 要分配的套件
        },
        // 该重载的执行器函数
        ({ origin, target, kit }) => {
          // 验证命令发送者是否为玩家
          if (!(origin instanceof Player)) {
            // 如果命令发送者不是玩家则抛出错误
            throw new Error("Only players can use this command.");
          }

          // 准备一个计数变量用于计算分配的套件数量
          let giveCount = 0;

          // 遍历target参数
          for (const entity of target.result ?? []) {
            // 验证实体是否为玩家
            if (!entity.isPlayer()) continue;

            // 根据kit参数进行切换
            switch (kit.result) {
              default:
                break;

              case "beginner": {
                // 给予初学者套件
                entity.executeCommand("give @s minecraft:wooden_sword 1");
                entity.executeCommand("give @s minecraft:apple 5");
                entity.executeCommand("give @s minecraft:leather_chestplate 1");
                break;
              }

              case "intermediate": {
                // 给予中级套件
                entity.executeCommand("give @s minecraft:stone_sword 1");
                entity.executeCommand("give @s minecraft:apple 25");
                entity.executeCommand("give @s minecraft:iron_chestplate 1");
                break;
              }

              case "professional": {
                // 给予专业套件
                entity.executeCommand("give @s minecraft:diamond_sword 1");
                entity.executeCommand("give @s minecraft:apple 64");
                entity.executeCommand("give @s minecraft:diamond_chestplate 1");
                break;
              }
            }

            // 增加计数器
            giveCount++;
          }

          // 返回响应消息
          return {
            message: `Gave the ${kit.result} kit to ${giveCount} player(s).`
          };
        }
      );
    },
    // 当没有重载匹配时的默认执行器函数
    () => {
      throw new Error("Invalid arguments, please specify a target and kit.");
    }
  );
}
```

## 总结

在本指南中，我们介绍了在Serenity中注册命令的基础知识。我们注册了一个简单的命令、添加了权限、创建了重载，并为参数使用了自定义枚举。你可以使用这些技术来为你的服务器创建强大而灵活的命令。

如果你对完整的代码片段感兴趣，可以在[这里](https://github.com/SerenityJS/serenity/tree/main/docs/custom-command/code.ts)找到！