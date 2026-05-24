---
comments: true
---

# 事件系统

Allay提供了一个强大的事件系统，允许插件监听服务器中发生的各种事件。本指南将引导你注册一个简单的事件监听器。

## 添加事件处理器

假设你的插件想要监听玩家加入服务器的事件，并向服务器中的所有人发送消息。你需要在一个类中创建事件监听器并用`@EventHandler`注解该方法：

```java linenums="1"
import org.allaymc.api.entity.interfaces.EntityPlayer;
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerJoinEvent;
import org.allaymc.api.server.Server;
import org.allaymc.api.utils.TextFormat;

public class MyEventListener {
    @EventHandler
    private void onPlayerJoin(PlayerJoinEvent event) { /*(1)!*/
        Server.getInstance().getMessageChannel().broadcastText(
            TextFormat.YELLOW + "欢迎" + event.getPlayer().getOriginName() + "加入服务器！"
        );
    }
}
```

1. :star: 参见提示

/// tip
使用`@EventHandler`注解的方法必须有且仅有一个参数并返回`void`。参数的类型是你想要监听的事件。
///

## 注册监听器

现在我们需要将事件处理器注册到Allay事件系统。

```java linenums="1" hl_lines="7"
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.server.Server;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Server.getInstance().getEventBus().registerListener(new MyEventListener());
    }
}
```

**完成了！** 你的插件现在应该监听并处理玩家加入时的事件。记住，你可以向一个监听器类中添加任意数量的方法来监听任何事件。

## 探索可用事件

Allay提供了多种可以监听的事件。要查看所有可用事件的列表，请访问[事件列表](../../docs/server/allay.md#api范围)页面。

常见事件包括：

- **玩家相关**
  - `PlayerJoinEvent` - 玩家加入服务器
  - `PlayerQuitEvent` - 玩家离开服务器
  - `PlayerDeathEvent` - 玩家死亡
  - `PlayerChatEvent` - 玩家发送聊天消息

- **方块相关**
  - `BlockBreakEvent` - 玩家破坏方块
  - `BlockPlaceEvent` - 玩家放置方块

- **实体相关**
  - `EntityDamageEvent` - 实体受伤
  - `EntitySpawnEvent` - 实体生成

## 事件优先级

你可以为事件处理器设置优先级，以控制多个监听器的执行顺序。使用`@EventHandler`的`priority`属性：

```java linenums="1"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.EventPriority;
import org.allaymc.api.eventbus.event.player.PlayerJoinEvent;

public class MyEventListener {
    @EventHandler(priority = EventPriority.HIGH)
    private void onPlayerJoinHighPriority(PlayerJoinEvent event) {
        // 此方法先执行
    }

    @EventHandler(priority = EventPriority.LOW)
    private void onPlayerJoinLowPriority(PlayerJoinEvent event) {
        // 此方法后执行
    }
}
```

## 取消事件

某些事件是可以取消的，意味着你可以阻止事件的默认行为。例如，你可以取消玩家破坏方块的事件：

```java linenums="1"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.block.BlockBreakEvent;

public class MyEventListener {
    @EventHandler
    private void onBlockBreak(BlockBreakEvent event) {
        if (event.getBlock().getBlockType() == BlockTypes.DIAMOND_ORE) {
            event.setCancelled(true); // 阻止破坏钻石矿石
        }
    }
}
```

## 注销监听器

当你不再需要监听事件时，可以注销监听器对象：

```java linenums="1"
Server.getInstance().getEventBus().unregisterListener(myEventListener);
```

## 接下来

现在你已经了解了事件系统的基础。建议继续学习：

- [任务调度](schedule-guide.md) - 异步执行任务
- [命令系统](command-guide.md) - 创建自定义命令