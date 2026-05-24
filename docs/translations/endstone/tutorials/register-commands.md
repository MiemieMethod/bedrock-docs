# 注册命令

在本部分中，我们将引导您创建一个简单的命令。本部分结束时，您将对如何使用Endstone定义和注册命令有基本的了解。

## 创建命令

让我们从一个简单的命令`/hello`开始，该命令向命令执行者问好。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="6-11"
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        commands = {
            "hello": {
                "description": "向命令执行者问好。",
                "usages": ["/hello"],
            }
        }

        # ...
    ```

=== ":simple-cplusplus: C++"

    ``` c++ title="src/my_plugin.cpp" linenums="1" hl_lines="7-9"
    #include "my_plugin.h"

    ENDSTONE_PLUGIN("my_plugin", "0.1.0", MyPlugin)
    {
        description = "My first C++ plugin for Endstone servers";

        command("hello")
            .description("向命令执行者问好。")
            .usages("/hello");
    }
    ```

**这就是全部！** 您刚刚创建了一个带有描述和用法的新命令。

## 添加权限

默认情况下，endstone中的所有命令都需要`operator`权限才能执行，以出于安全原因。由于我们在这里创建一个简单的命令，我们可能想为所有人改变其权限。

让我们对我们的代码进行以下更改。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="11 15-20"
    from endstone.command import Command, CommandSender
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        commands = {
            "hello": {
                "description": "向命令执行者问好。",
                "usages": ["/hello"],
                "permissions": ["my_plugin.command.hello"],
            }
        }

        permissions = {
            "my_plugin.command.hello": {
                "description": "允许用户使用/hello命令。",
                "default": True, #(1)!
            }
        }

        # ...
    ```

    1.  :star: 见提示

    !!! tip

        `default`字段设置执行命令所需的权限级别。可能的值为：

        - `True`或`"true"`: 每个人都可以执行此命令
        - `False`或`"false"`: 没有人可以执行此命令，除非明确授予权限。
        - `"op"`: 只有操作员可以执行此命令
        - `"not_op"`: 只有非操作员可以执行此命令
        - `"console"`: 只有控制台可以执行此命令

=== ":simple-cplusplus: C++"

    ``` c++ title="src/my_plugin.cpp" linenums="1" hl_lines="10 12-14"
    #include "my_plugin.h"

    ENDSTONE_PLUGIN("my_plugin", "0.1.0", MyPlugin)
    {
        description = "My first C++ plugin for Endstone servers";

        command("hello")
            .description("向命令执行者问好。")
            .usages("/hello")
            .permissions("my_plugin.command.hello");

        permission("my_plugin.command.hello")
            .description("允许用户使用/hello命令。")
            .default_(endstone::PermissionDefault::True); /*(1)!*/
    }
    ```

    1.  :star: 见提示

    !!! tip

        `default_`方法设置执行命令所需的权限级别。可能的值为：

        - `endstone::PermissionDefault::True`: 每个人都可以执行此命令
        - `endstone::PermissionDefault::False`: 没有人可以执行此命令，除非明确授予权限。
        - `endstone::PermissionDefault::Operator`: 只有操作员可以执行此命令
        - `endstone::PermissionDefault::NotOperator`: 只有非操作员可以执行此命令
        - `endstone::PermissionDefault::Console`: 只有控制台可以执行此命令

## 处理命令

现在，下一步是处理我们刚刚创建的命令。假设我们想向执行此命令的人发送"Hello, World!"问候消息。只需再添加几行代码。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="1 22-26"
    from endstone.command import Command, CommandSender
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        commands = {
            "hello": {
                "description": "向命令执行者问好。",
                "usages": ["/hello"],
                "permissions": ["my_plugin.command.hello"],
            }
        }

        permissions = {
            "my_plugin.command.hello": {
                "description": "允许用户使用/hello命令。",
                "default": True,
            }
        }

        def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
            if command.name == "hello":
                sender.send_message("Hello World!")

            return True

        # ...
    ```

=== ":simple-cplusplus: C++"

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="5-12"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        bool onCommand(endstone::CommandSender &sender, const endstone::Command &command, const std::vector<std::string> &args) override
        {
            if (command.getName() == "hello") 
            {
                sender.sendMessage("Hello World!");
            }
            return true;
        }

        // ...
    };
    ```

现在，[安装]您的插件并重启您的服务器。进入游戏并输入`/help hello`。您应该看到使用信息，这表明我们的命令已成功添加到游戏！

现在，输入`/hello`，您应该收到消息"Hello World!"。

![示例命令](screenshots/command-example.png)

[安装]: install-your-plugin.md

## 为命令添加参数

现在，假设我们想向执行者发送自定义消息而不是"Hello World!"。我们可以向命令添加接受消息的参数。

在Endstone中，有两种基本的参数类型：

| 类型       | 描述                       | 语法           |
|-----------|--------------------------|----------------|
| **必选** | 必须提供此参数             | `<name: type>` |
| **可选**  | 此参数是可选的，可以省略 | `[name: type]` |

让我们更改我们的代码以添加**可选**参数`msg`，其类型为`message`。根据上表，语法应为`[msg: message]`。让我们将其添加到我们的代码中。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="10 24-27"
    from endstone.command import Command, CommandSender
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        commands = {
            "hello": {
                "description": "向命令执行者问好。",
                "usages": ["/hello [msg: message]"],
                "permissions": ["my_plugin.command.hello"],
            }
        }

        permissions = {
            "my_plugin.command.hello": {
                "description": "允许用户使用/hello命令。",
                "default": True,
            }
        }

        def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
            if command.name == "hello":
                if len(args) == 0: #(1)!
                    sender.send_message("Hello World!")
                else:
                    sender.send_message(args[0])

            return True

        # ...
    ```

    1.  :white_check_mark: 这里，我们检查是否提供了可选参数。

=== ":simple-cplusplus: C++"

    ``` c++ title="src/my_plugin.cpp" linenums="1" hl_lines="9"
    #include "my_plugin.h"

    ENDSTONE_PLUGIN("my_plugin", "0.1.0", MyPlugin)
    {
        description = "My first C++ plugin for Endstone servers";

        command("hello")
            .description("向命令执行者问好。")
            .usages("/hello [msg: message]")
            .permissions("my_plugin.command.hello");

        permission("my_plugin.command.hello")
            .description("允许用户使用/hello命令。")
            .default_(endstone::PermissionDefault::True);
    }
    ```

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="9-14"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        bool onCommand(endstone::CommandSender &sender, const endstone::Command &command, const std::vector<std::string> &args) override
        {
            if (command.getName() == "hello") 
            {
                if (args.empty()) {
                    sender.sendMessage("Hello World!");
                }
                else {
                    sender.sendMessage(args[0]);
                }
            }
            return true;
        }

        // ...
    };
    ```

**:partying_face: 完成了！** 现在当用户使用`/hello This is my message!`时，"This is my message!"将显示给他们，而不是"Hello World!"。

!!! tip

    要使参数强制，请将参数从`[msg: message]`更改为`<msg: message>`

### 内置类型

在上面的部分中，我们添加了类型为`message`的参数，这是Endstone支持的**内置类型**。以下是当前支持的所有内置类型的完整列表。

| 类型           | 别名                    | 描述                                            | 可能的值                                        |
|----------------|------------------------|-----------------------------------------------|-----------------------------------------------|
| `int`          |                        | 代表整数                                       | `10`                                          |
| `float`        |                        | 代表浮点数                                     | `3.14`                                        |
| `bool`         |                        | 代表布尔值                                     | `true`                                        |
| `target`       | `actor`, `entity`, `player` | 代表目标选择器                                 | `@e`, `@r`, `PlayerName`                      |
| `str`          | `string`               | 代表以空格结尾的字符串                         | `Hello`                                       |
| `block_pos`    | `vec3i`                | 代表3维整数位置                                | `1 2 3`                                       |
| `pos`          | `vec3`, `vec3f`        | 代表3维浮点位置                                | `1.0 2.0 3.0`                                 |
| `message`      |                        | 代表到行末的消息                               | `Hello World!`                                |
| `json`         |                        | 代表JSON字符串                                 | `{"key": "value"}`                            |
| `block`        |                        | 代表方块类型                                   | `wood`                                        |
| `block_states` |                        | 代表方块状态                                   | `["wood_type"="birch","stripped_bit"=true]`   |
| `entity_type`  |                        | 代表实体类型                                   | `minecraft:creeper`                           |

### 用户定义的枚举类型

枚举类型可用于表示一组预定义的字符串常数。此行为类似于现代编程语言（如Node.js和Python）中文字类型的工作方式。枚举类型提供了一种定义"类型"的方法，由一组命名常数组成，称为枚举，简称"enum"。

Endstone允许开发者添加他们自己的枚举。基本语法遵循以下模式：

- 必选：`(value1|value2|value3)<name: EnumType>`
- 可选：`(value1|value2|value3)[name: EnumType]`

这里，所有可能的值由管道运算符`|`分隔，范围在括号`()`内，后跟参数类型、名称和类型。

!!! example

    在命令用法中使用枚举类型的示例是：`/home (add|list|del)<action: HomeAction>`
    
    在此示例中，参数名为`action`，具有**用户定义的枚举**类型`HomeAction`。使用命令时，用户必须从指定集合中选择其中一个操作：`add`、`list`或`del`。
