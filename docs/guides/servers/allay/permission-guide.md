---
comments: true
---

# 权限系统

Allay提供了简单的权限API，允许你轻松进行权限检查。它还允许你编写和使用自己的权限插件。本指南将引导你进行权限检查并编写/使用自定义权限插件。

## 什么是权限

在开始之前，我们需要了解什么是权限。在你的服务器上，将存在某些功能、命令和功能。其中一些功能将包含在服务器中，其他则由插件添加。这些操作中的大多数都有一个相关的权限，因此你可以控制哪些用户可以访问每个功能或命令。

权限只是一个字符串（字母/数字序列），并使用句号分成几部分。例如，`allay.command.say`是Allay的`/say`命令的权限。

表示某个权限的字符串有时也称为"权限节点"或简称"节点"。权限节点可以有三个值：`true`、`false`和`undefined`。

- `true`意味着玩家具有该权限，分配给它的条件将被授予玩家。
- `false`意味着玩家没有该权限，分配给它的条件将被拒绝给玩家。
- `undefined`意味着权限未被明确设置。这通常意味着它默认为`false`。极少数情况下，插件可以使未定义的权限默认为`true`，在这种情况下你需要将其显式设置为`false`。

## 进行权限检查

在`Permissible`对象上执行权限检查非常容易：

```java linenums="1"
import org.allaymc.api.permission.Permissible;
import org.allaymc.api.permission.Tristate;

public class Example {
    public void example(Permissible permissible) { /*(1)!*/
        // 检查这个permissible对象是否具有权限"allay.command.say"
        Tristate tristate = permissible.hasPermission("allay.command.say");
        // 将Tristate转换为布尔值，其中Tristate.TRUE将为true
        // 而Tristate.FALSE、Tristate.UNDEFINED将为false
        boolean bool = tristate.asBoolean();
    }
}
```

1. :star: 参见提示

/// tip
`Permissible`是包含所有必要权限相关方法的接口。`Entity`、`Server`和`CommandSender`等对象实现了此接口，因此你也可以对它们进行权限检查。
///

## 权限计算器

每个permissible对象都有一个关联的权限计算器。权限计算器用于在对permissible对象检查权限时计算权限值：

你可以为permissible对象设置自定义权限计算器。在以下示例中，我们将创建一个权限计算器，为任何权限始终返回`Tristate.TRUE`（是的这是危险的😅），并在玩家加入服务器时替换玩家的默认权限计算器：

```java linenums="1"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerSpawnEvent;
import org.allaymc.api.permission.PermissionCalculator;
import org.allaymc.api.permission.Tristate;

public class Example {
    @EventHandler
    public void onPlayerSpawn(PlayerSpawnEvent event) {
        event.getPlayer().getControlledEntity()
            .setPermissionCalculator(new MyPermissionCalculator());
    }
    
    public static class MyPermissionCalculator implements PermissionCalculator {
        @Override
        public Tristate calculatePermission(String permission) {
            // 为任何权限始终返回Tristate.TRUE！
            return Tristate.TRUE;
        }
    }
}
```

上面是权限计算器的一个简单示例。你可以用它做更复杂的事情来实现自己的权限插件。

## 默认权限计算器

默认情况下，Allay对玩家使用权限计算器，其中OP玩家拥有所有权限，非OP玩家拥有有限的权限集合。这是默认的`OpPermissionCalculator`的工作方式。

## 使用LuckPerms

你可能厌倦了原版的OP/非OP权限系统，想使用高级权限插件来更好地控制你的服务器。Allay官方支持[LuckPerms](https://luckperms.net/)，这是Minecraft服务器最流行的权限插件。

你可以在[这里](https://github.com/AllayMC/LuckPerms)找到源代码并下载Allay平台预构建的LuckPerms jar。

安装LuckPerms后，当玩家加入服务器时，它将替换玩家的默认权限计算器。LuckPerms不关心玩家的OP状态，这使服务器的操作员列表无效。有关如何使用LuckPerms的更多信息，请参阅它们的网站。

## 权限最佳实践

### 命名规范

使用反向域名表示法命名权限：

```
yourplugin.command.admin
yourplugin.command.user
yourplugin.feature.special
```

### 权限树结构

组织权限成树形结构，使用通配符：

```
yourplugin.*              // 所有权限
yourplugin.command.*      // 所有命令权限
yourplugin.command.admin  // 特定命令
```

## 接下来

现在你已经了解了权限系统的基础。建议继续学习：

- [命令系统](command-guide.md) - 在命令中使用权限
- [配置文件](config-guide.md) - 管理插件配置
