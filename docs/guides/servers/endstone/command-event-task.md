# Endstone命令、事件与调度实战

当你已经能加载插件后，下一步通常就是把“交互入口”补齐：命令负责输入，事件负责触发，调度器负责周期行为。这篇教程给出一套最常见的组合方式。

## 命令：先做一个可扩展骨架

先声明`commands`和`permissions`，再在`on_command`中分发逻辑。这样后续加子命令不会把代码写乱。

```python
from endstone.command import Command, CommandSender
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    commands = {
        "hello": {
            "description": "Greet the command sender.",
            "usages": ["/hello [msg: message]"],
            "permissions": ["my_plugin.command.hello"],
        }
    }
    permissions = {
        "my_plugin.command.hello": {
            "description": "Allow users to use /hello.",
            "default": True,
        }
    }

    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if command.name == "hello":
            sender.send_message(args[0] if args else "Hello World!")
        return True
```

`message`参数应放在最后，否则后续参数不会再被正确解析。

## 事件：把注册放在`on_enable`

事件监听器建议统一在`on_enable`中注册：

```python
from endstone import ColorFormat
from endstone.event import PlayerJoinEvent, event_handler
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_join(self, event: PlayerJoinEvent) -> None:
        self.server.broadcast_message(
            ColorFormat.YELLOW + f"{event.player.name}加入了服务器" + ColorFormat.RESET
        )
```

写监听器时先看事件是否可取消，再决定要不要修改事件对象属性。

## 调度：把周期逻辑与业务逻辑分开

```python
from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version = "0.11"

    def on_enable(self) -> None:
        self.server.scheduler.run_task(self, self.say_hi, delay=0, period=20)

    def say_hi(self) -> None:
        for player in self.server.online_players:
            player.send_popup("Hi!")
```

周期任务里避免长时间阻塞；网络请求或重计算建议拆到异步流程或外部服务。

## 一条可复用的实践顺序

1. 先写命令，确保你能手动触发功能。
2. 再接入事件，让功能自动触发。
3. 最后上调度器，做轮询、心跳或定时同步。

按这个顺序调试，定位问题会更快。

## 延伸阅读

- [注册命令（翻译）](../../../translations/endstone/tutorials/register-commands.md)
- [注册事件监听器（翻译）](../../../translations/endstone/tutorials/register-event-listeners.md)
- [调度任务（翻译）](../../../translations/endstone/tutorials/schedule-tasks.md)
- [Endstone命令与文本格式](../../../refs/server/endstone-command-format.md)