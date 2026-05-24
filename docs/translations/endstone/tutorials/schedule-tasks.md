# 调度任务

Endstone提供了一个任务调度系统，允许插件为将来的执行安排任务，可能在定期间隔。在本教程中，我们将指导您安排一个简单的任务。

这里，我们想要一个显示"Hi!"的屏幕弹出窗口每隔1秒钟为每个在线玩家出现。

=== ":fontawesome-brands-python: Python"

    ``` python title="src/endstone_my_plugin/my_plugin.py" linenums="1" hl_lines="10 12-14"
    from endstone.plugin import Plugin

    class MyPlugin(Plugin):
        api_version = "0.11"

        # ...

        def on_enable(self) -> None:
            self.logger.info("on_enable is called!")
            self.server.scheduler.run_task(self, self.say_hi, delay=0, period=20)

        def say_hi(self) -> None:
            for player in self.server.online_players:
                player.send_popup("Hi!")
    ```

=== ":simple-cplusplus: C++"

    ``` c++ title="include/my_plugin.h" linenums="1" hl_lines="10 13-19"
    #include <endstone/endstone.hpp>

    class MyPlugin : public endstone::Plugin {
    public:
        // ...

        void onEnable() override
        {
            getLogger().info("onEnable is called");
            getServer().getScheduler().runTaskTimer([&]() { sayHi(); }, 0, 20);
        }

        void sayHi()
        {
            for (auto& player : getServer().getOnlinePlayers())
            {
                player->sendPopup("Hi");
            }
        }
    };
    ```

**:partying_face: 就是这样！** 服务器现在将以20刻或约每秒一次的间隔向所有在线玩家发送"Hi"消息。