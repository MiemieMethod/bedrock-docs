---
comments: true
---

# 任务调度

Allay提供了任务调度系统，允许插件为将来的执行（可能以定期间隔）调度任务。本指南将引导你调度一个简单的任务。

## 注册任务

这里我们想要每秒钟为每个在线玩家显示一个弹窗显示"嗨！"：

```java linenums="1" hl_lines="7-10"
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.server.Server;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Server.getInstance().getScheduler().scheduleRepeating(this, () -> {
            Server.getInstance().getPlayerManager().getPlayers().values()
                .forEach(player -> player.sendPopup("嗨！"));
            return true; /*(1)!*/
        }, 20/*(2)!*/);
    }
}
```

1. :star: 任务将以指定间隔继续运行，直到任务返回`false`。

2. :star: 间隔以刻为单位指定。一秒有20个刻，因此20个刻大约为1秒。

**完成了！** 服务器现在每20个刻（大约1秒）向所有在线玩家发送一条"嗨"消息。

## 调度器类型

Allay提供了四种调度器类型：服务器、世界、维度和实体。选择与所访问数据相匹配的最小范围。每个调度器在特定线程上运行：

- **服务器调度器**：在服务器线程上运行。
- **世界调度器**：在世界线程上运行。
- **维度调度器**：当`world-settings.tick-dimension-in-parallel`设置为`true`时，在计算线程池上运行，否则在世界线程上运行。
- **实体调度器**：在实体所在维度的线程上运行。

### 服务器调度器（全局、非世界工作）

对于不改变世界、维度或实体状态的全局任务，使用服务器调度器。

```java linenums="1" hl_lines="7-9"
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.server.Server;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Server.getInstance().getScheduler()
            .scheduleRepeating(this, this::cleanupExpiredSessions, 20 * 60);
    }

    private void cleanupExpiredSessions() {
        // 清理插件级缓存或指标。
    }
}
```

### 世界调度器（每个世界的状态）

对于在全球各地州运作（时间、天气、世界数据），使用世界调度器。

```java linenums="1" hl_lines="8-10"
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.server.Server;
import org.allaymc.api.world.WorldData;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Server.getInstance().getWorldPool().getWorlds().values().forEach(world -> {
            world.getScheduler().scheduleRepeating(this, () -> 
                world.getWorldData().setTimeOfDay(WorldData.TIME_NOON), 20 * 300);
        });
    }
}
```

### 维度调度器（每个维度的方块和实体）

对于更新维度内的方块、粒子或实体的任务，使用维度调度器。

```java linenums="1" hl_lines="9-13"
import org.allaymc.api.block.type.BlockTypes;
import org.allaymc.api.plugin.Plugin;
import org.allaymc.api.server.Server;

public class MyPlugin extends Plugin {
    @Override
    public void onEnable() {
        Server.getInstance().getWorldPool().getWorlds().values().forEach(world -> {
            world.getDimensions().values().forEach(dimension -> {
                dimension.getScheduler().scheduleRepeating(this, () -> {
                    dimension.setBlockState(0, 64, 0, BlockTypes.STONE.getDefaultState());
                    return true;
                }, 20);
            });
        });
    }
}
```

### 实体调度器（单个实体生命周期）

对于与单个实体相关的任务（以便当实体消失时任务停止），使用实体调度器。

```java linenums="1" hl_lines="6-9"
import org.allaymc.api.entity.interfaces.EntityPlayer;

public void onSomeEvent(EntityPlayer player) {
    player.getScheduler().scheduleRepeating(player, () -> {
        player.sendPopup("正在充电...");
        return true;
    }, 20);
}
```

## 单次执行任务

如果你想只调度一次任务而不是重复，使用`schedule()`方法：

```java linenums="1"
// 在5秒（100刻）后执行一次任务
Server.getInstance().getScheduler().schedule(this, () -> {
    System.out.println("任务执行！");
}, 100);
```

## 取消任务

`scheduleRepeating()`和`schedule()`都返回一个`Task`对象，你可以使用它来取消任务：

```java linenums="1"
Task task = Server.getInstance().getScheduler().scheduleRepeating(this, () -> {
    // 任务代码
    return true;
}, 20);

// 稍后...
task.cancel();
```

## 线程安全注意事项

在使用调度器时，有几个重要的线程安全考虑：

- **服务器调度器**的任务与世界线程分离，访问世界数据可能需要额外的同步。
- **世界调度器**的任务与世界线程一致，可以安全地访问该世界的数据。
- **维度调度器**的任务与维度线程一致，可以安全地访问该维度的数据。
- **实体调度器**的任务与实体所在维度的线程一致，可以安全地访问该实体。

选择适当的调度器来最小化跨线程同步的需要。

## 接下来

现在你已经了解了任务调度的基础。建议继续学习：

- [事件系统](event-guide.md) - 监听游戏事件
- [命令系统](command-guide.md) - 创建自定义命令
