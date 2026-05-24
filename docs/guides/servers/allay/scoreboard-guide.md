---
comments: true
---

# 记分板

记分板很适合显示服务器信息、在线人数、任务进度和排行榜。本指南用Allay的最基础模式带你做一个可更新的侧边栏记分板。

## 创建一个记分板

先创建实例：

```java linenums="1"
import org.allaymc.api.scoreboard.Scoreboard;

public class MyScoreboard {
    protected static final Scoreboard info = new Scoreboard("INFO");
}
```

接着往里面写行内容：

```java linenums="1"
import org.allaymc.api.server.Server;

import java.util.List;

protected static void update() {
    var networkSettings = Server.SETTINGS.networkSettings();
    info.setLines(List.of(
            "欢迎来到服务器！",
            "在线人数：" + Server.getInstance().getPlayerManager().getPlayerCount(),
            networkSettings.ip() + ":" + networkSettings.port()
    ));
}
```

## 玩家进入时显示

记分板不会自动附着到所有玩家身上，所以通常要在加入事件里手动添加查看者：

```java linenums="1"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerJoinEvent;
import org.allaymc.api.eventbus.event.server.PlayerQuitEvent;
import org.allaymc.api.scoreboard.data.DisplaySlot;

@EventHandler
public void onPlayerJoin(PlayerJoinEvent event) {
    info.addViewer(event.getPlayer(), DisplaySlot.SIDEBAR);
    update();
}

@EventHandler
public void onPlayerQuit(PlayerQuitEvent event) {
    info.removeViewer(event.getPlayer(), DisplaySlot.SIDEBAR);
    update();
}
```

/// warning | 退出时也要移除
Allay资料明确提醒，玩家离开服务器时不会自动从记分板查看者列表里移除。你需要自己调用`removeViewer(...)`。
///

## 更新内容时会发生什么

只要再次调用`Scoreboard#setLines(...)`，Allay就会把更新后的内容重新发送给当前查看者，不需要你自己遍历所有玩家逐个刷新。

这意味着你可以把`update()`挂在：

- 玩家加入或退出事件里。
- 定时任务里。
- 某个业务状态变化后。

## 三种显示槽位

Allay给出了三个显示槽位：

| 槽位 | 说明 |
|------|------|
| `SIDEBAR` | 右侧侧边栏，最常用。 |
| `LIST` | 在线玩家列表区域。 |
| `BELOW_NAME` | 玩家名称标签下方。 |

大多数插件先从`SIDEBAR`开始就够了。`BELOW_NAME`和另外两种槽位的视觉语义差别很大，只有在你明确要给玩家头顶显示数值时再用它。

## 一个最小完整示例

```java linenums="1"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerJoinEvent;
import org.allaymc.api.eventbus.event.server.PlayerQuitEvent;
import org.allaymc.api.scoreboard.Scoreboard;
import org.allaymc.api.scoreboard.data.DisplaySlot;
import org.allaymc.api.server.Server;

import java.util.List;

public class MyScoreboard {
    private static final Scoreboard info = new Scoreboard("INFO");

    private static void update() {
        info.setLines(List.of(
                "欢迎来到服务器！",
                "在线人数：" + Server.getInstance().getPlayerManager().getPlayerCount()
        ));
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        info.addViewer(event.getPlayer(), DisplaySlot.SIDEBAR);
        update();
    }

    @EventHandler
    public void onPlayerQuit(PlayerQuitEvent event) {
        info.removeViewer(event.getPlayer(), DisplaySlot.SIDEBAR);
        update();
    }
}
```

## 实战建议

- 动态信息多时，优先用记分板，不要反复刷聊天栏。
- 需要周期更新时，可以配合[任务调度](schedule-guide.md)。
- 如果你还想把标题、倒计时做成屏幕顶部提示，可以再结合[Boss栏](bossbars-guide.md)。