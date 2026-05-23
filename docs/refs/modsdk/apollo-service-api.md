# Apollo功能服接口<!-- md:flag china -->
本页汇总Apollo功能服脚本接口，覆盖配置读取、事件统计、HTTP接口与服务器管理能力。
/// warning | Apollo专用能力
本页接口来自中国版Apollo网络服脚本环境。接口命名与调用方式与国际版脚本API不同，不能直接互换。
///

## 配置
| 接口 | 说明 |
| --- | --- |
| `GetCommonConfig` | 获取服务器公共配置，包括所有服务器和db的配置，具体参见备注 |
| `GetServerId` | 获取服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |
| `GetServerLoadedModsById` | 根据服务器id获取服务器加载mod列表 |
| `GetServerLoadedModsByType` | 根据服务器类型获取服务器加载mod列表。若同种类型服务器配置了不同的mod，则返回其中一个对应mod列表。 |
| `GetServiceConfig` | 获取service配置，该配置对应公共配置中servicelist下对应service的配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |

## 通用
| 接口 | 说明 |
| --- | --- |
| `StartRecordEvent` | 开始启动大厅服/游戏服与功能服之间的脚本事件收发包统计，启动后调用[StopRecordEvent()](#StopRecordEvent)即可获取两个函数调用之间引擎收发包的统计信息 |
| `StopRecordEvent` | 停止大厅服/游戏服与功能服之间的脚本事件收发包统计并输出结果，与[StartRecordEvent()](#StartRecordEvent)配合使用，输出结果为字典，具体见示例 |

## HTTP服务器
| 接口 | 说明 |
| --- | --- |
| `RegisterOpCommand` | 注册一个新的HTTP接口 |
| `ResponseOpCommandFail` | 发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId |
| `ResponseOpCommandSuccess` | 发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId |
| `UnRegisterOpCommand` | 注销一个已注册的HTTP接口 |
| `RegisterServiceHttp` | 注册一个新的HTTP接口 |
| `SendHttpRequestToMaster` | 给master发送http请求 |
| `SendHttpResponse` | 发送HTTP的Response。支持异步返回，返回时指定输入clientId |

## 服务器
| 接口 | 说明 |
| --- | --- |
| `ResetServer` | 重置服务器 |

## 服务器管理
| 接口 | 说明 |
| --- | --- |
| `GetServerIdsByServerType` | 根据类型获取服务器id列表 |
| `GetServerProtocolVersion` | 获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中 |
| `GetServerType` | 获取服务器类型 |
| `GetServersStatus` | 获取所有lobby/game服务器的状态。只有状态1表示服务器正常服务，其他状态表示服务器不能对外服务 |
| `IsConnectedServer` | service是否与lobby/game/proxy建立连接 |
