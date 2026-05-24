# 服务端系列教程

基岩版服务端开发可以分成两条线：一条是运行和管理服务器，另一条是在服务器上扩展玩法。官方BDS适合先学习基本运维；LeviLamina、Endstone、Allay、SerenityJS、Nukkit-MOT和PocketMine-MP等生态则面向不同语言、不同兼容目标和不同插件模型。

/// html | div.grid.cards
- :material-server: __[搭建BDS](bds.md)__
  下载、启动、开放端口、连接本机服务器，并理解`server.properties`、世界目录和包目录。
- :material-language-cpp: __[LeviLamina入门](levilamina.md)__
  使用lip安装LeviLamina，了解C++模组开发的工具链和模板。
- :material-language-python: __[Endstone入门](endstone/index.md)__
  用pip或Docker启动Endstone，并创建第一个Python/C++插件。
- :material-language-java: __[Allay入门](allay.md)__
  安装Java21，启动Allay，并使用Java插件模板。
- :material-language-javascript: __[SerenityJS入门](serenity.md)__
  使用Node.js创建SerenityJS项目，了解事件、命令、自定义方块和插件模板。
- :material-coffee: __[Nukkit、PocketMine与旧生态](nukkit-pocketmine.md)__
  了解Nukkit-MOT安装、插件放置，以及PocketMine-MP的启动方式和插件生态定位。
///

## 先选哪一个

- 只想开原版服务器：先读BDS。
- 想在官方BDS上加载原生模组：读LeviLamina。
- 会Python，想写BDS插件：读Endstone。
- 会Java、Kotlin或其他JVM语言，想研究社区服务端：读Allay或Nukkit-MOT。
- 会TypeScript/JavaScript，想把基岩版服务端嵌入Node.js项目：读SerenityJS。
- 维护PHP服务端或旧PocketMine插件：先看本系列的旧生态说明，并结合PocketMine-MP官方文档核对安装、配置和插件要求。

/// warning | 不同服务端的插件不能直接通用
BDS脚本、LeviLamina模组、Endstone插件、Allay插件、SerenityJS插件、Nukkit插件和PocketMine-MP插件面向的运行时不同。不要把一个生态的API名称直接复制到另一个生态中。
///
