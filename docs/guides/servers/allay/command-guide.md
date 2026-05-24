---
comments: true
---

# 注册命令

本指南将逐步引导你创建和注册命令。完成本部分后，你将能够定义和注册Allay命令。

## 创建命令

让我们从一个简单的`/hello`命令开始，该命令向命令执行者问候。

```java linenums="1"
import org.allaymc.api.command.Command;
import org.allaymc.api.server.Server;

public class HelloCommand extends Command {
    public HelloCommand() {
        super("hello", "向命令执行者问候。", "myplugin.command.hello");
    }
}
```

**就这么简单！** 你已经创建了一个带有描述的新命令。现在你需要将命令注册到服务器中：

```java linenums="1" hl_lines="7"
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.registry.Registries;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Registries.COMMANDS.register(new HelloCommand());
    }
}
```

## 添加权限

默认情况下，只有服务器操作员可以使用新创建的命令。由于我们创建的是hello world命令，我们可能希望改变其权限以让所有人使用。

让我们对代码做以下修改：

```java linenums="1" hl_lines="9"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.tree.CommandTree;
import org.allaymc.api.permission.OpPermissionCalculator;
import org.allaymc.api.server.Server;

public class HelloCommand extends Command {
    public HelloCommand() {
        super("hello", "向命令执行者问候。", "myplugin.command.hello");
        OpPermissionCalculator.NON_OP_PERMISSIONS.addAll(this.permissions); /*(1)!*/
    }
}
```

1. :star: 参见提示

/// tip
`getPermissions()`方法返回命令所需的权限列表，`OpPermissionCalculator`是新玩家的默认权限计算器。

第三方权限插件（例如LuckPerms）可能会用自己的权限计算器替换它，在这种情况下这行代码将无效。
///

## 处理命令

接下来是处理我们刚刚创建的命令。假设我们想向执行命令的人发送"你好，世界！"的问候消息。只需再添加几行代码：

```java linenums="1" hl_lines="10-17"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.tree.CommandTree;
import org.allaymc.api.server.Server;

public class HelloCommand extends Command {
    public HelloCommand() {
        super("hello", "向命令执行者问候。", "myplugin.command.hello");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .exec(context -> {
                    context.getSender().sendMessage("你好，世界！");
                    return context.success();
                });
    }
}
```

现在，[安装](first-plugin.md#构建插件)你的插件并重启服务器。加入游戏并输入`/help hello`。你应该能看到使用信息，这表示我们的命令已成功添加到游戏中！

现在输入`/hello`，你应该会收到"你好，世界！"的消息。

## 向命令添加参数

假设我们想要向执行者发送自定义问候消息，而不是"你好，世界！"。我们可以向命令添加一个参数来接受消息。

让我们修改代码以添加一个**可选的**`message`参数，类型为`msg`：

```java linenums="1" hl_lines="13-14 16-21"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.tree.CommandTree;
import org.allaymc.api.server.Server;

public class HelloCommand extends Command {
    public HelloCommand() {
        super("hello", "向命令执行者问候。", "myplugin.command.hello");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .msg("message")
                .optional()
                .exec(context -> {
                    String message = context.getResult(0);
                    if (message.isBlank()) { /*(1)!*/
                        context.getSender().sendMessage("你好，世界！");
                    } else {
                        context.getSender().sendMessage(message);
                    }
                    return context.success();
                });
    }
}
```

1. :white_check_mark: 这里我们检查了可选参数是否被提供。

**现在就完成了！** 当用户使用`/hello 这是我的消息！`时，"这是我的消息！"会显示给他们，而不是"你好，世界！"。

/// tip
要使参数变为必需的，只需移除`.optional()`方法调用。
///

### 内置参数类型

在上面的部分中，我们添加了一个类型为`msg`的参数，这是Allay支持的**内置类型**。以下是所有内置参数类型的完整列表：

| 类型                               | 描述                                          | 结果类型                   |
|----------------------------------|---------------------------------------------|--------------------------|
| `str(name)`                        | 单个单词字符串                                  | `String`                   |
| `msg(name)`                        | 消息（可包含空格，消耗剩余参数）                | `String`                   |
| `intNum(name)`                     | 整数                                         | `Integer`                  |
| `floatNum(name)`                   | 浮点数                                       | `Float`                    |
| `doubleNum(name)`                  | 双精度浮点数                                   | `Double`                   |
| `longNum(name)`                    | 长整数                                       | `Long`                     |
| `shortNum(name)`                   | 短整数                                       | `Short`                    |
| `bool(name)`                       | 布尔值（true/false）                         | `Boolean`                  |
| `enums(name, values...)`           | 字符串枚举                                    | `String`                   |
| `enumsIgnoreCase(name, values...)` | 字符串枚举（不区分大小写）                      | `String`                   |
| `enumClass(name, EnumClass.class)` | 枚举类（自动映射）                            | `EnumClass`                |
| `target(name)`                     | 实体选择器（@a、@e、@p等）                    | `List<Entity>`             |
| `playerTarget(name)`               | 玩家选择器                                    | `List<Entity>`             |
| `wildcardTarget(name)`             | 通配符目标选择器                              | `String`                   |
| `pos(name)`                        | 位置（x y z，支持~）                         | `Vector3d`                 |
| `gameMode(name)`                   | 游戏模式                                     | `GameMode`                 |
| `difficulty(name)`                 | 难度                                         | `Difficulty`               |
| `effect(name)`                     | 效果类型                                     | `EffectType`               |
| `enchantment(name)`                | 魔咒类型                                     | `EnchantmentType`          |
| `itemType(name)`                   | 物品类型                                     | `ItemType<?>`              |
| `blockType(name)`                  | 方块类型                                     | `BlockType<?>`             |
| `blockPropertyValues(name)`        | 方块属性值                                    | `List<BlockPropertyValue>` |
| `entityType(name)`                 | 实体类型                                     | `EntityType<?>`            |
| `remain(name)`                     | 剩余参数列表                                  | `List<String>`             |
| `key(name)`                        | 文字关键字（用于子命令）                        | `String`                   |
| `cmd(name)`                        | 命令字符串                                    | `String`                   |

## 添加命令别名

你可以为命令添加别名，使玩家能够使用较短或替代名称：

```java linenums="1" hl_lines="5"
public class HelloCommand extends Command {
    public HelloCommand() {
        super("hello", "向命令执行者问候。", "myplugin.command.hello");
        // 添加别名，使玩家也能使用/hi或/greet
        aliases.addAll(List.of("hi", "greet"));
    }
    // ...
}
```

现在玩家可以使用`/hello`、`/hi`或`/greet`来执行命令。

## 创建子命令

许多命令都有子命令（如`/time set`或`/time add`）。你可以使用`key()`方法创建子命令，并使用`up()`和`root()`在命令树中导航：

```java linenums="1"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.tree.CommandTree;

public class MyCommand extends Command {
    public MyCommand() {
        super("mycommand", "带有子命令的命令。", "myplugin.command.mycommand");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .key("help") // /mycommand help
                .exec(context -> {
                    context.getSender().sendMessage("可用命令：help、reload、set");
                    return context.success();
                })
                .root() /*(1)!*/
                .key("reload") // /mycommand reload
                .exec(context -> {
                    context.getSender().sendMessage("正在重新加载配置...");
                    return context.success();
                })
                .root()
                .key("set") // /mycommand set <key> <value>
                .str("key")
                .str("value")
                .exec(context -> {
                    String key = context.getResult(1);
                    String value = context.getResult(2);
                    context.getSender().sendMessage("设置" + key + "为" + value);
                    return context.success();
                });
    }
}
```

1. :star: `root()`返回根节点以定义新分支。你也可以使用`up()`向上走一级，或`up(n)`向上走n级。

### 树导航方法

| 方法       | 描述                  |
|-----------|----------------------|
| `root()`  | 返回根节点            |
| `up()`    | 向上走一级            |
| `up(n)`   | 向上走n级             |
| `parent()`| 获取父节点            |

### 常见错误：重复节点创建

/// warning
当定义多个子命令时，避免在同一个父节点上多次调用相同的节点创建方法（如`.key()`）。每次调用都会创建一个**新节点**，而不是重用现有的节点。

**错误示例：**

```java
// 错误！这会在根节点下创建两个单独的"test"节点！
tree.getRoot().key("test").key("sub1");
tree.getRoot().key("test").key("sub2");  // .key("test")在根节点上被调用了两次
```

这段代码看起来会创建`/mycommand test sub1`和`/mycommand test sub2`，但实际上会创建一个有两个单独"test"分支的破损树结构。命令解析可能会不正确，甚至没有抛出错误。

**正确的方法：**

存储中间节点引用并重用它：

```java
var test = tree.getRoot().key("test");
test.key("sub1").exec(context -> { /* ... */ });
test.key("sub2").exec(context -> { /* ... */ });
```

或使用`.up()`返回：

```java
tree.getRoot()
        .key("test")
        .key("sub1")
        .exec(context -> { /* ... */ })
        .up()  // 返回"test"节点
        .key("sub2")
        .exec(context -> { /* ... */ });
```

或仅当需要完全不同的分支时使用`.root()`和完整路径：

```java
tree.getRoot()
        .key("test")
        .key("sub1")
        .exec(context -> { /* ... */ })
        .root()  // 返回根节点
        .key("other")  // 不同分支，不是"test"
        .exec(context -> { /* ... */ });
```
///

## 限制命令为特定执行者

有时你希望命令只能由玩家执行，或只能从服务器控制台执行。使用`SenderType`来限制谁可以执行命令：

```java linenums="1" hl_lines="13"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.SenderType;
import org.allaymc.api.command.tree.CommandTree;

public class HealCommand extends Command {
    public HealCommand() {
        super("heal", "治疗自己。", "myplugin.command.heal");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .exec((context, player) -> { /*(1)!*/
                    player.setHealth(player.getMaxHealth());
                    context.addOutput("你已被治疗！");
                    return context.success();
                }, SenderType.PLAYER); /*(2)!*/
    }
}
```

1. :star: 使用`SenderType`时，执行器的第二个参数接收类型化的发送者。
2. :star: 此命令只能由玩家执行。控制台会收到错误消息。

### 可用的发送者类型

| SenderType                 | 描述                        |
|----------------------------|---------------------------|
| `SenderType.ANY`           | 任何发送者（默认）           |
| `SenderType.PLAYER`        | 只有玩家可以执行           |
| `SenderType.ACTUAL_PLAYER` | 只有真实玩家（不含虚拟玩家） |
| `SenderType.ENTITY`        | 只有实体可以执行           |
| `SenderType.SERVER`        | 只有服务器控制台可以执行    |

## 向命令节点添加权限

除了主命令权限外，你还可以向特定命令节点添加权限。这对于对无权访问的玩家隐藏子命令很有用：

```java linenums="1" hl_lines="12"
@Override
public void prepareCommandTree(CommandTree tree) {
    tree.getRoot()
            .key("info")
            .exec(context -> {
                context.addOutput("服务器信息...");
                return context.success();
            })
            .root()
            .key("admin")
            .permission("myplugin.command.admin") /*(1)!*/
            .key("reload")
            .exec(context -> {
                context.addOutput("正在重新加载...");
                return context.success();
            });
}
```

1. :star: 没有`myplugin.command.admin`权限的玩家将看不到也无法使用`/mycommand admin`子命令。

## 处理命令错误

当命令失败时，你应该返回`context.fail()`并可选地添加错误消息：

```java linenums="1"
.exec(context -> {
    List<EntityPlayer> targets = context.getResult(0);

    // 检查是否找到任何目标
    if (targets.isEmpty()) {
        context.addNoTargetMatchError(); /*(1)!*/
        return context.fail();
    }

    // 检查目标过多
    if (targets.size() > 1) {
        context.addTooManyTargetsError();
        return context.fail();
    }

    // 自定义错误消息
    if (!someCondition) {
        context.addError("出错了！"); /*(2)!*/
        return context.fail();
    }

    return context.success();
})
```

1. :star: "没有目标匹配"错误的内置错误助手。
2. :star: 自定义错误消息（将以红色显示）。

### 内置错误助手

| 方法                                  | 描述                 |
|---------------------------------------|-------------------|
| `addNoTargetMatchError()`             | 选择器未匹配任何实体  |
| `addTooManyTargetsError()`            | 匹配的实体过多        |
| `addPlayerNotFoundError()`            | 玩家未找到           |
| `addSyntaxError()`                    | 当前参数语法错误      |
| `addInvalidExecutorError(SenderType)` | 错误的发送者类型      |
| `addError(message, args...)`          | 自定义错误消息（红色） |
| `addOutput(message, args...)`         | 普通输出消息          |

## 使用枚举类

为了更清洁的代码，你可以直接使用Java枚举与`enumClass()`：

```java linenums="1"
public class ColorCommand extends Command {
    public ColorCommand() {
        super("color", "设置你的颜色。", "myplugin.command.color");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .enumClass("color", Color.class) /*(1)!*/
                .exec(context -> {
                    Color color = context.getResult(0); /*(2)!*/
                    context.addOutput("选定的颜色：" + color.name());
                    return context.success();
                });
    }

    private enum Color {
        RED, GREEN, BLUE, YELLOW
    }
}
```

1. :star: 枚举值将自动转换为命令选项。
2. :star: 结果已经被类型化为枚举类，不需要手动解析。

## 高级：仅服务器端命令

某些命令不应该被发送到客户端（例如，它们与客户端命令冲突）。覆盖`isServerSideOnly()`以向客户端隐藏命令：

```java linenums="1" hl_lines="9-12"
public class MyServerCommand extends Command {
    public MyServerCommand() {
        super("myserver", "仅服务器端命令。", "myplugin.command.myserver");
    }

    // 命令树设置...

    @Override
    public boolean isServerSideOnly() {
        return true;
    }
}
```

## 高级：调试命令

你可以将命令标记为调试命令，这会使其名称在客户端中显示为蓝色：

```java linenums="1" hl_lines="9-12"
public class DebugCommand extends Command {
    public DebugCommand() {
        super("mydebug", "一个调试命令。", "myplugin.command.debug");
    }

    // 命令树设置...

    @Override
    public boolean isDebugCommand() {
        return true;
    }
}
```

## 总结

你已经学到了如何：

- 创建和注册命令
- 添加各种类型的参数
- 使用树导航创建子命令
- 将命令限制为特定的发送者类型
- 正确处理错误
- 使用枚举类实现更清洁的代码

更多示例，请查看[Allay源码中的内置命令](https://github.com/AllayMC/Allay/tree/master/server/src/main/java/org/allaymc/server/command/defaults)。
