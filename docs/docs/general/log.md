# 日志

**日志**（**Log**）是记录软件运行状态的重要信息，包括软件的运行状态、错误信息、警告信息等。日志可以帮助开发者快速定位问题，提高软件的可维护性。在Minecraft基岩版中，有各类日志文件。

## 日志目录

Minecraft自身拥有一个日志目录，用于存放各类日志文件。该目录的位置取决于你的操作系统。

在Windows系统中：

- 国际版零售构建和Playtest构建：{{samp|%LocalAppData%\\Packages\\Microsoft.MinecraftUWP_8wekyb3d8bbwe\\LocalState\\logs}}
- 中国版零售构建和ModPC开发包：{{samp|%AppData%\\MinecraftPE_Netease\\logs}}
- 中国版编辑器构建：{{samp|%AppData%\\MinecraftPE_Netease_Editor\\logs}}

在Android系统中：

- 国际版零售构建和Playtest构建：{{samp|/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/logs}}

## 内容日志

**内容日志**（**Content Log**）是Minecraft基岩版的一种日志文件，用于记录附加包内容的加载情况。内容日志的文件名格式为`ContentLog__<day>__<date>__<time>.txt`，位于日志目录下，例如`ContentLog__Saturday__2024_May_25__09_58_15_1.txt`，是2024年5月25日星期六约9:58创建的文件。

内容日志需要手动在设置中开启才可以正常记录。进入游戏后，点击“设置->创建者->内容日志设置”，将“开启内容日志文件”打开即可启用内容日志的输出，将“开启内容日志GUI”打开即可开启内容日志在游戏内的实时打印。不过，只有`inform`及更高级别的日志才会在游戏内实时输出，`verbose`级别的日志只会输出到文件中。

## 调试日志

**调试日志**（**Debug Log**）是Minecraft基岩版的一种日志文件，用于记录游戏运行时的调试信息。调试日志的文件名格式为`Debug_Log__<day>__<date>__<time>.txt`，位于日志目录下，例如`Debug_Log__Friday__2024_May_24__23_38_06`，是2024年5月24日星期五约23:38创建的文件。

一般只有Playtest构建、ModPC开发包和中国版编辑器构建才会生成调试日志。除了内容日志和调试日志，日志目录中还有一些其他文件，但一般也只有以上三种构建才会生成这些文件，这里不再赘述。

## 脚本日志

对于中国版的ModPC开发包，会连接MCStudio所唤起的一个名为Safaia的服务端并输出Python脚本日志。这些日志会保存在{{samp|%LocalAppData%\\NetEase\\MCSafaiaServer\\log_storages}}文件夹中。你也可以在调试窗口中手动保存当前实例的日志到其他位置。