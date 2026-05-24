# Apollo网络服事件<!-- md:flag china -->
本页汇总Apollo网络服体系的脚本事件名称与用途说明。以下事件均属于中国版网络服生态能力，不适用于国际版脚本API。
/// warning | 使用边界
这些事件名称来自Apollo网络服脚本环境。不要将它们用于国际版行为包JavaScript脚本，也不要与`@minecraft/server`事件系统混写。
///

## 大厅与游戏服事件
| 事件 | 分类 | 说明 |
| --- | --- | --- |
| `MasterConnectStatusEvent` | 服务器 | master成功连接到当前服务器事件 |
| `MasterForceShutDownEvent` | 服务器 | 不建议开发者使用，强制关闭当前服务器时会触发本事件 |
| `MasterGraceShutDownEvent` | 服务器 | 不建议开发者使用，优雅关闭当前服务器时会触发本事件 |
| `ServerWillShutDownEvent` | 服务器 | 不建议开发者使用，游戏即将强制关闭触发本事件。事件回调函数需要好清理和存档工作，同时终止或强制join所有异步线程 |
| `ServiceConnectEvent` | 服务器 | service与lobby/game的成功建立连接事件 |
| `ServiceDisconnectEvent` | 服务器 | service与lobby/game断开连接事件 |
| `ServiceRegisterModuleEvent` | 服务器 | 不建议开发者使用，service向lobby/game注册module |
| `ReloadCommonConfigEvent` | 配置 | 不建议开发者使用，公共配置发生变化时触发本事件，注意只有与本服相关配置发生变化时才会触发本事件，比如日志等级 |
| `MasterResponseTransferFailServerEvent` | 玩家 | 转服失败事件，当玩家试图转服时，没有符合条件的目标服务器时抛出此事件 |
| `MasterResponseTransferSucServerEvent` | 玩家 | 转服成功事件，当玩家试图转服时，成功定位到可转服的目标服务器时抛出此事件 |
| `ServerGetPlayerLockEvent` | 玩家 | 玩家登录到lobby/game过程中，获取玩家在线锁事件。事件触发时，玩家还处于开始登录阶段，还没有下载行为包，且没有在地图中出生。在线锁实质是redis中记录的玩家在线信息，redis key格式是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid |
| `ServerPlayerBornPosEvent` | 玩家 | 创建玩家对象过程中，设置玩家出生位置时触发本事件 |
| `ServerReleasePlayerLockEvent` | 玩家 | 玩家下线过程中，释放在redis中的玩家在线锁事件。事件触发时，客户端同服务端断开了连接，玩家数据已经保存到地图，玩家已经不存在于mc的世界中。在线锁实质是redis中记录的玩家在线信息，redis key格式是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid |
| `ServerReleasePlayerLockOnShutDownEvent` | 玩家 | 不建议开发者使用，游戏强制关闭过程中，玩家强制下线时触发本事件。事件回调函数需要释放在redis中的玩家的在线锁 |
| `StoreBuySuccServerEvent` | 玩家 | 玩家游戏内购买商品时服务端抛出的事件 |

## 控制服事件
| 事件 | 分类 | 说明 |
| --- | --- | --- |
| `ResetGamesBeginEvent` | 服务器 | 开始重置lobby/game事件。具体可以参见API【ResetServer】 |
| `ResetGamesEndEvent` | 服务器 | 重置lobby/game结束事件。本事件只是表示重置完成了，但是服务器可能还未完成初始化。具体可以参见API【ResetServer】 |
| `RollingCloseServersEndEvent` | 服务器 | 使用RollingCloseServersEndEvent滚动关服结束事件。 |
| `RollingUpdateServersEndEvent` | 服务器 | 使用RollingUpdateServers滚动更新服务器结束事件。 |
| `ServerConnectedEvent` | 服务器 | lobby/game/proxy成功建立连接时触发 |
| `ServerDisconnectEvent` | 服务器 | lobby/game/proxy断开连接时触发 |
| `NetGameCommonConfChangeEvent` | 配置 | 公共配置发生变化时触发，具体包括：新增或删服服务器；服务器相关配置变化；日志等级发生变化 |
| `PlayerLoginServerEvent` | 玩家 | 玩家开始登陆事件，此时master开始给玩家分配lobby/game，可以区分玩家是登录还是切服 |
| `PlayerLogoutServerEvent` | 玩家 | 玩家登出时触发，玩家在lobby/game下载行为包的过程中退出也会触发该事件，可以以区分玩家是登出还是切服 |
| `PlayerTransferServerEvent` | 玩家 | 玩家开始切服事件，此时master开始为玩家准备服务器，玩家还没切服完毕，后续可能切服失败 |

## 功能服事件
| 事件 | 分类 | 说明 |
| --- | --- | --- |
| `ServerConnectedEvent` | 服务器 | lobby/game/proxy成功建立连接时触发 |
| `ServerDisconnectEvent` | 服务器 | lobby/game/proxy断开连接时触发 |
| `UpdateServerStatusEvent` | 服务器 | lobby/game/proxy状态发生变化时触发 |
| `NetGameCommonConfChangeEvent` | 配置 | 服务器配置发生变化时触发，具体包括：新增或删服服务器；服务器相关配置变化；日志等级发生变化 |