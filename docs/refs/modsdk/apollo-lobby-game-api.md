# Apollo大厅与游戏服接口<!-- md:flag china -->
本页汇总Apollo大厅服与游戏服脚本接口，覆盖地图、玩家、切服、运维与调试能力。
/// warning | Apollo专用能力
本页接口来自中国版Apollo网络服脚本环境。接口命名与调用方式与国际版脚本API不同，不能直接互换。
///

## 配置
| 接口 | 说明 |
| --- | --- |
| `GetCommonConfig` | 获取服务器公共配置，包括本服、所有db和所有功能服的配置，具体参见备注，注意可能不包含其他大厅服和游戏服配置，不能获取所有服的配置 |
| `GetMongoConfig` | 获取mongo数据库的连接参数，对应公共配置中mongo配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |
| `GetMysqlConfig` | 获取mysql数据库的连接参数，对应公共配置中mysql配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |
| `GetRedisConfig` | 获取redis数据库的连接参数，对应公共配置中redis配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |
| `GetServerId` | 获取本服的服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |

## 地图
| 接口 | 说明 |
| --- | --- |
| `DelForbidDragonEggTeleportField` | 删除禁止龙蛋传送的地图区域 |
| `DelForbidFlowField` | 删除地图区域，不同的ID的区域边界会阻挡流体的流动 |
| `SetEnableLimitArea` | 设置地图最大区域，超过区域的地形不再生成 |
| `SetForbidDragonEggTeleportField` | 设置禁止龙蛋传送的地图区域 |
| `SetForbidFlowField` | 设置地图区域，不同的ID的区域边界会阻挡流体的流动 |
| `SetLevelGameType` | 强制设置游戏的玩法模式 |
| `SetShowFakeSeed` | 在客户端【设置】中，显示虚假的游戏地图种子 |
| `StopShowFakeSeed` | 在客户端【设置】中，显示真实的游戏地图种子 |

## 玩家
| 接口 | 说明 |
| --- | --- |
| `GetConnectingProxyIdOfPlayer` | 获取玩家客户端连接的proxy服务器id |
| `GetPlatformUid` | 获取玩家登录端的uid，假如玩家从手机端登录，返回手机端的uid，否则返回PC端的uid |
| `GetPlayerIdByUid` | 根据玩家uid获取玩家ID（也即playerId）。若玩家不在这个lobby/game，则返回为空字符 |
| `GetPlayerIpHash` | 获取玩家客户端ip的特征哈希值 |
| `GetPlayerLockResult` | 不建议开发者使用，把获取玩家在线锁结果告知给引擎层 |
| `GetPlayerNickname` | 获取玩家的昵称。 |
| `GetPlayerUid` | 获取玩家的uid |
| `GetUidIsSilent` | 根据玩家uid获取是否被禁言 |
| `HidePlayerFootprint` | 隐藏某个玩家的会员脚印外观 |
| `HidePlayerMagicCircle` | 隐藏某个玩家的会员法阵外观 |
| `IsPlayerPeUser` | 获取玩家是否从手机端登录 |
| `ReleasePlayerLockResult` | 不建议开发者使用，把释放玩家在线锁结果告知给引擎层 |
| `SetAutoRespawn` | 设置是否启用自动重生逻辑 |
| `ShieldPlayerJoinText` | 是否屏蔽客户端左上角 “xxx 加入了游戏”的提示 |
| `TryToKickoutPlayer` | 把玩家踢下线，message中的文字会显示在客户端的断线提示中 |

## 商城
| 接口 | 说明 |
| --- | --- |
| `NotifyClientToOpenShopUi` | 通知客户端打开商城界面 |

## 关服
| 接口 | 说明 |
| --- | --- |
| `SetGracefulShutdownOk` | 不建议开发者使用，设置脚本层的优雅关机逻辑已经执行完毕，引擎可以开始优雅关机了 |
| `SetShutdownOk` | 不建议开发者使用，设置脚本层的强制关机逻辑已经执行完毕，引擎可以开始强制关机了 |
| `ShutdownServer` | 强制关机 |

## 服务器
| 接口 | 说明 |
| --- | --- |
| `AddGetPlayerLockTask` | 添加获取玩家在线锁时的处理任务，会在玩家刚连接到服务端时执行，在所有任务都完成后，才会继续玩家的登录流程 |
| `CheckMasterExist` | 检查服务器是否与master建立连接 |
| `GetLastFrameTime` | 获取服务端脚本上一帧运行时间 |
| `GetOnlinePlayerNum` | 获取当前服务器的在线人数 |
| `GetServerProtocolVersion` | 获取服务器的协议版本号 |
| `IsServiceConnected` | 检查服务器是否与某个service建立连接 |
| `IsShowDebugLog` | 当前服务器是否打印debug等级的日志 |
| `ResetServer` | 重置服务器 |

## 切服
| 接口 | 说明 |
| --- | --- |
| `TransferToOtherServer` | 玩家转移到指定类型的服务器，假如同类服务器有多个，就根据负载均衡选择一个 |
| `TransferToOtherServerById` | 玩家迁移到指定服务器id的服务器 |

## 主城模式
| 接口 | 说明 |
| --- | --- |
| `SetCityMode` | 设置游戏为主城模式：包括有无法改变地形，不切换日夜，不改变天气，不刷新生物等限制 |

## HTTP服务器
| 接口 | 说明 |
| --- | --- |
| `RegisterOpCommand` | 注册一个新的HTTP接口 |
| `ResponseOpCommandFail` | 发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId |
| `ResponseOpCommandSuccess` | 发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId |
| `UnRegisterOpCommand` | 注销一个已注册的HTTP接口 |

## 调试
| 接口 | 说明 |
| --- | --- |
| `EnableNetgamePacketIdStatistics` | 开启（或关闭）玩家向服务器发包的数量统计。长时间不使用数据时请关掉统计，避免内存泄露。 |
| `GetAndClearNetgamePacketIdStatistics` | 获取玩家向服务器发包的数量统计，然后重置统计数据。即每次返回从上一次获取到现在的数量。需要用EnableNetgamePacketIdStatistics开启后才有数据 |
| `StartChunkProfile` | 开始启动服务端区块读写性能统计，启动后调用[StopChunkProfile](#StopChunkProfile)即可获得近期的服务端区块读写信息 |
| `StopChunkProfile` | 结束服务端区块读写性能统计，并返回近期区块读写信息，与[StartChunkProfile](#StartChunkProfile)配合使用 |

## 性能开关
| 接口 | 说明 |
| --- | --- |
| `ChangeAllPerformanceSwitch` | 整体关闭/打开预定义的游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提高服务器的性能，承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务器初始化时调用此接口，同时不要在服务器运行中途修改 |
| `ChangePerformanceSwitch` | 关闭/打开某个游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提高服务器的性能，承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务器初始化时调用此接口，同时不要在服务器运行中途修改 |