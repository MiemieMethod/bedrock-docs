# 注册事件监听器

Endstone提供了一个强大的事件系统，允许插件监听在服务器中发生的各种事件。让我们引导您注册一个简单的事件监听器。

## 添加事件处理器

假设您的插件想在玩家加入服务器时监听并向服务器上的所有人发送消息。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="1-2 13-16"
    from endstone import ColorFormat
    from endstone.event import event_handler, PlayerJoinEvent
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "{{ git.short_tag[1:].rsplit('.', 1)[0] }}"

        # ...

        def on_enable(self) -> None:
            self.logger.info("on_enable is called!")

        @event_handler
        def on_player_join(self, event: PlayerJoinEvent):
            self.server.broadcast_message(ColorFormat.YELLOW + f"{event.player.name} has joined the server")
    ```

=== ":simple-cplusplus: C++"

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="12-15"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        // ...

        void onEnable() override
        {
            getLogger().info("onEnable is called");
        }
    
        void onPlayerJoin(endstone::PlayerJoinEvent& event)
        {
            getServer().broadcastMessage(ColorFormat::Yellow + "{} has joined the server", event.getPlayer().getName());
        }
    };
    ```

## 注册监听器

现在，我们需要向Endstone事件系统注册我们的事件处理器。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="12"
    from endstone import ColorFormat
    from endstone.event import event_handler, PlayerJoinEvent
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "{{ git.short_tag[1:].rsplit('.', 1)[0] }}"

        # ...

        def on_enable(self) -> None:
            self.logger.info("on_enable is called!")
            self.register_events(self)

        @event_handler
        def on_player_join(self, event: PlayerJoinEvent):
            self.server.broadcast_message(ColorFormat.YELLOW + f"{event.player.name} has joined the server")
    ```

    通过调用`self.register_events`，Endstone将查看作为参数传入的对象，并向事件系统注册所有带有`@event_handler`装饰器的处理器。

=== ":simple-cplusplus: C++"

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="10"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        // ...

        void onEnable() override
        {
            getLogger().info("onEnable is called");
            registerEvent(&MyPlugin::onPlayerJoin, *this);
        }
    
        void onPlayerJoin(endstone::PlayerJoinEvent& event)
        {
            getServer().broadcastMessage(ColorFormat::Yellow + "{} has joined the server", event.getPlayer().getName());
        }
    };
    ```

**:partying_face: 就是这样！** 您的插件现在应该能够监听和处理玩家加入时的事件。记住，您可以添加任意多个方法来监听任何事件。
