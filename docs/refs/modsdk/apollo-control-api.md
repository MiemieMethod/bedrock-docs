# Apollo控制服接口<!-- md:flag china -->
本页汇总Apollo控制服脚本接口，覆盖配置、玩家管理、HTTP交互与服务器管理能力。
/// warning | Apollo专用能力
本页接口来自中国版Apollo网络服脚本环境。接口命名与调用方式与国际版脚本API不同，不能直接互换。
///

## 配置
| 接口 | 说明 |
| --- | --- |
| `GetCommonConfig` | 获取服务器公共配置，包括所有服务器和db的配置，具体参见备注 |
| `GetGameTypeByServerId` | 获取指定ID服务器的类型 |
| `GetServerIdsByGameType` | 获取指定类型的服务器id列表 |
| `GetServerLoadedModsById` | 根据服务器id获取服务器加载mod列表 |
| `GetServerLoadedModsByType` | 根据服务器类型获取服务器加载mod列表。若同种类型服务器配置了不同的mod，则返回其中一个对应mod列表。 |
| `IsService` | 服务器是否是service服 |

## 玩家
| 接口 | 说明 |
| --- | --- |
| `BanUser` | 封禁某个玩家 |
| `GetBanUserInfo` | 获取玩家的封禁信息 |
| `GetOnlineUidList` | 获取所有在线玩家的uid列表 |
| `GetProtocolVersionByUID` | 获取在线玩家客户端协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中 |
| `GetServerIdByUid` | 获取在线玩家所在的服务器的ID，返回的信息为当前控制服内存缓存中的信息，玩家很可能很快就离线或者转服 |
| `GetUserSilentInfo` | 获取玩家的禁言信息 |
| `SetLoginStratege` | 设置玩家登陆选服策略，要求服务器启动后加载mod时候设置 |
| `SilentByUID` | 禁言某个玩家 |
| `UnBanUser` | 解除某个玩家的封禁 |
| `UnSilentByUID` | 解除某个玩家的禁言 |

## HTTP服务器
| 接口 | 说明 |
| --- | --- |
| `RegisterMasterHttp` | 注册一个新的HTTP接口 |
| `SendHttpRequestToService` | 给service发送http请求 |
| `SendHttpResponse` | 发送HTTP的Response，支持异步返回，返回时候指定请求传入的clientId |

## 服务器管理
| 接口 | 说明 |
| --- | --- |
| `GetAllResetingServers` | 获取所有重置中服务器的id列表 |
| `GetAllServerStatus` | 获取所有服务器的状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务。 |
| `GetAllServersOnlineNum` | 获取所有服务器的在线人数 |
| `GetConnectedLobbyAndGameIds` | 获取所有已经连接的lobby/game的服务器id列表 |
| `GetOneServerStatus` | 获取服务器状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务 |
| `GetOnlineNumByServerId` | 获取服务器(lobby/game/proxy)的在线人数 |
| `GetOnlineNumByServerType` | 获取某类型服务器的在线人数 |
| `GetServerProtocolVersion` | 获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中 |
| `GetTotalOnlineNum` | 获取总得在线人数 |
| `IsConnectedServer` | master是否与lobby/game/proxy建立连接 |
| `IsValidServer` | 服务器是否有效。一种用途：master将玩家分配到服务器之前，会检查服务器是否有效，避免把玩家分配到一个即将关闭的服务器中 |
| `ResetServer` | 重置某个lobby/game。它会将服务器地图恢复到启动时状态并重启服务器。开始重置会触发ResetGamesBeginEvent事件，重置结束会触发ResetGamesEndEvent事件 |
| `RollingCloseServers` | 滚动关服 |
| `RollingUpdateServers` | 滚动更新服务器，要求网络服使用了这个ip，要求至少存在一个服务器类型为serverType、引擎版本为appVersion的服务器在运行，只能滚动更新代理服/大厅服/游戏服 |
| `StopServerByServerid` | 关闭某个服务器。若MCStudio配置网络游戏时设置了“崩溃自动拉起”，则关闭服务器后会被自动拉起，实现重启功能 |