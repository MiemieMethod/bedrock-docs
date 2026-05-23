# Apollo服务器通信接口<!-- md:flag china -->
本页汇总Apollo网络服多进程通信接口，包括客户端、大厅服、游戏服、控制服和功能服之间的消息投递与请求响应接口。
## 通信模型
- 单点消息：定向发送到单个目标服务器或单个客户端。
- 广播消息：向同类型或全量目标服务器广播事件。
- 请求响应：通过请求接口发起调用，再由回调或响应接口返回结果。

## client和game/lobby通信
| 接口 | 说明 |
| --- | --- |
| `NotifyToClient` | game/lobby接口，game/lobby发送事件到指定客户端 |
| `NotifyToServer` | 客户端接口，给lobby/game服务器发送事件。注意，玩家只能存在于一个game或lobby，不可能同时存在于两个服务器 |

## master和game/lobby通信
| 接口 | 说明 |
| --- | --- |
| `NotifyToMaster` | lobby/game接口，lobby/game给master发事件。 |
| `NotifyToServerNode` | master接口，master给某个lobby/game发事件 |

## service和master通信
| 接口 | 说明 |
| --- | --- |
| `BroadcastToService` | master接口，master给所有service广播消息。 |
| `NotifyToServiceNode` | master接口，master给某个service发消息。 |
| `NotifyToMaster` | service接口，service给master发消息。 |

## service和service/master通信
| 接口 | 说明 |
| --- | --- |
| `RegisterRpcMethod` | service/master接口，用于监听service/master发过来请求，通常用于官方插件开发，服主请使用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)。要求：MCStudio打开配置文件目录，打开deploy.json文件，然后给service配置module_names信息 |
| `RegisterRpcMethodForMod` | service接口，监听service/master发过来的请求。service/master使用[RequestToServiceMod](#RequestToServiceMod)发送请求 |
| `RequestToService` | service/master接口，给service/master发请求，通常用于官方插件开发，服主请使用[RequestToServiceMod](#RequestToServiceMod) |
| `RequestToServiceMod` | master接口，给service发请求。要求service调用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)监听请求 |
| `ResponseToServer` | service/master接口，给service/master返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口 |

## service和game/lobby通信
| 接口 | 说明 |
| --- | --- |
| `BroadcastToServerByType` | service接口，service给某种类型服务器广播消息 |
| `BroadcastToService` | service/lobby/game接口，service/lobby/game给所有service广播消息。 |
| `NotifyToServerNode` | service接口，service给某个lobby/game发消息。 |
| `NotifyToServiceNode` | service/lobby/game接口，service/lobby/game给某个service发消息。 |
| `RegisterRpcMethod` | service接口，通常用于官方插件开发，服主请使用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)。本接口注册一个监听函数，用于监听lobby/game发过来的请求。 |
| `RegisterRpcMethodForMod` | service接口，监听lobby/game发过来的请求，lobby/game使用[RequestToServiceMod](#RequestToServiceMod)发送请求 |
| `RequestToService` | service/lobby/game接口，通常用于官方插件开发，服主请使用[RequestToServiceMod](#RequestToServiceMod)。lobby/game给service发请求，两个service间可以通过这个接口通信 |
| `RequestToServiceMod` | lobby/game接口，lobby/game给service发送事件。要求service调用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)监听请求 |
| `ResponseToServer` | service接口，给lobby/game返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口 |

## client和service通信
| 接口 | 说明 |
| --- | --- |
| `NotifyToServiceNode` | 客户端接口，给service服务器发送事件 |
| `RemoteNotifyToClient` | service接口，service发送事件到指定客户端 |
