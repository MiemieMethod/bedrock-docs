# Apollo运营指令<!-- md:flag china -->
本页汇总Apollo控制服HTTP运营指令路径、用途和主要请求字段。调用方式为向控制服基础地址发送POST请求。
/// warning | 运维接口风险
运营指令涉及封禁、踢人、停服与远程脚本执行。建议仅在受控运维环境使用，并限制调用权限。
///

## 查询UID
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/netease/get-online-uids` | 查询当前在线玩家的uid | 无 |
| `/netease/get-lazy-uids` | 查询最近请求登录玩家的uid以及请求登录时间 | 无 |

## 在线人数
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/netease/update-player-online-limit` | 修改全局最高同时在线人数限制 | online_limit |
| `/online-num/query` | 获取proxy/lobby/game在线人数或获取总在线人数。 | serverType |
| `/online-num/query-by-server-id` | 获取某个proxy/game/lobby在线人数 | serverId |

## 日志等级
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/conf/set-log-debug-level` | 开服工具日志等级设置为debug或info level等级 | debugLevel |
| `/conf/set-server-log-debug-level` | 设置某个服务器的日志等级。 | debugLevel、serverId |

## 服务器
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/query-all-server-status` | 查询所有服务器状态 | 无 |
| `/query-one-server-status` | 查询某个服务器状态 | serverId |

## 禁言，解除禁言
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/silent` | 禁言某个玩家 | banTime、reason、type、uid |
| `/unban-silent` | 解除某个玩家的禁言 | type、uid |
| `/global-silent` | 全局公屏禁言开关 | isSilent、reason |

## 踢出玩家
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/kickout-user` | 把某个玩家从游戏中踢出 | reason、uid |

## 封禁，解除封禁
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/ban-user` | 封禁某个玩家 | bCombineReason、banTime、reason、uid |
| `/unban-user` | 解除某个玩家的封禁 | uid |

## 强制解除玩家在线标识
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/netease/release-online-lock` | 强制解除指定UID玩家的在线标识 | uidList |
| `/netease/release-online-lock-by-server` | 强制解除指定ID服务器当前在线玩家的在线标识 | serverId |

## 停服维护
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/invalid-all-servers` | 开启/关闭停服维护 | invalid、reason |

## Hunter调试命令
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/netease/hunter-debug` | 使目的服务器执行Python脚本，脚本中使用**print**打印的信息会体现在请求返回中，同时，也会打印到目的服务器的日志文件中，具体是"hunterDebug exec"日志的下面n行日志。 | command、opServerIds、opServerType、script |
| `/hunter-debug` | 使目的服务器执行Python脚本，其结果打印到目的服务器的日志文件中，具体是"hunterDebug exec"日志的下面n行日志。 | command、script、serverId |

## 性能分析
| 指令路径 | 说明 | 主要请求字段 |
| --- | --- | --- |
| `/check-memory-run` | 检查服务器脚本层内存泄漏。需要执行两次指令，第一次生成快照，第二次生成同第一次的diff。 | objNames、serverId、useList |
| `/profile` | 用于测量python函数占用cpu时间。需要执行两次指令，第一次开始profile，第二次生成性能数据文件。性能数据文件放到执行文件所在目录下的profile子目录中。性能数据文件名的格式：profile+生成文件的时间戳 | bBegin、serverId |
