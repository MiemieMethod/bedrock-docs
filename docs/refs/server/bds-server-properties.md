# BDS的server.properties

{{file|server.properties|txt}}是[基岩版专用服务器](../../docs/server/bds.md)的主要配置文件。该文件使用INI风格的键值格式，每行一个`key=value`，井号`#`开头的行为注释。修改文件后，通常需要重启服务器才能确保所有设置重新读取。

## 属性

| 属性 | 默认值 | 允许值 | 描述 |
|------|--------|--------|------|
| `server-name` | `Dedicated Server` | 不含分号的任意字符串 | 服务器名称。 |
| `gamemode` | `survival` | `survival`、`creative`、`adventure` | 新玩家的游戏模式。 |
| `force-gamemode` | `false` | `true`、`false` | 为`true`时，服务器始终向客户端发送`gamemode`配置值；为`false`时，服务器发送世界创建时保存的游戏模式。 |
| `difficulty` | `easy` | `peaceful`、`easy`、`normal`、`hard` | 世界难度。 |
| `allow-cheats` | `false` | `true`、`false` | 是否允许作弊命令。 |
| `max-players` | `10` | 正整数 | 最大玩家数量。较高数值会增加性能压力。 |
| `online-mode` | `true` | `true`、`false` | 是否要求连接玩家通过Xbox Live认证。接受互联网连接的服务器应保持开启。 |
| `allow-list` | `false` | `true`、`false` | 是否只允许{{file|allowlist.json}}中的玩家连接。 |
| `server-port` | `19132` | `1`至`65535`的整数 | 服务器监听的IPv4端口。 |
| `server-portv6` | `19133` | `1`至`65535`的整数 | 服务器监听的IPv6端口。 |
| `enable-lan-visibility` | `true` | `true`、`false` | 是否响应LAN发现。开启时，即使配置了非默认端口，服务器也可能绑定默认发现端口。 |
| `view-distance` | `32` | 大于等于`5`的正整数 | 允许的最大视距，以区块为单位。较高数值会增加性能压力。 |
| `tick-distance` | `4` | `4`至`12`的整数 | 围绕玩家保持模拟的区块距离。较高数值会增加性能压力。 |
| `player-idle-timeout` | `30` | 非负整数 | 玩家闲置多少分钟后被踢出；`0`表示不因闲置踢出。 |
| `max-threads` | `8` | 正整数；`0`或省略表示尽可能使用 | 服务器尝试使用的最大线程数。 |
| `level-name` | `Bedrock level` | 对宿主操作系统有效的文件名字符串 | 使用或生成的世界目录名。 |
| `level-seed` | 无 | 任意字符串 | 新世界使用的种子；留空时随机生成。 |
| `default-player-permission-level` | `member` | `visitor`、`member`、`operator` | 新玩家首次加入时的权限级别。 |
| `texturepack-required` | `false` | `true`、`false` | 世界使用特定资源包时，是否强制客户端使用这些资源包。 |
| `content-log-file-enabled` | `false` | `true`、`false` | 是否将内容错误记录到文件。 |
| `compression-threshold` | `1` | `0`至`65535`的整数 | 触发网络原始载荷压缩的最小大小。 |
| `compression-algorithm` | `zlib` | `zlib`、`snappy` | 网络压缩算法。 |
| `server-authoritative-movement-strict` | `false` | `true`、`false` | 是否更严格地由服务端跟踪玩家位置。高延迟时可能影响移动体验。 |
| `server-authoritative-dismount-strict` | `false` | `true`、`false` | 是否更严格地校正下乘位置。 |
| `server-authoritative-entity-interactions-strict` | `false` | `true`、`false` | 是否更严格地处理实体交互。高延迟时可能影响玩家交互。 |
| `player-position-acceptance-threshold` | `0.5` | 正浮点数 | 客户端与服务端玩家位置差异的容忍阈值。大于`1.0`会增加放行作弊行为的可能性。 |
| `player-movement-action-direction-threshold` | `0.85` | `0.0`至`1.0`的正浮点数 | 玩家攻击方向与视线方向可相差的程度。`1.0`表示必须完全一致。 |
| `server-authoritative-block-breaking` | `false` | `true`、`false` | 是否由服务器同步计算方块开采并校验客户端破坏行为。 |
| `server-authoritative-block-breaking-range-scalar` | `1.5` | 大于`1.0`的浮点数 | 增大可破坏方块范围；该值会平方后乘以默认范围。 |
| `chat-restriction` | `None` | `None`、`Dropped`、`Disabled` | 聊天限制级别。`Dropped`会丢弃聊天消息；`Disabled`会对非操作员隐藏聊天UI。 |
| `disable-player-interaction` | `false` | `true`、`false` | 是否通知客户端忽略其他玩家交互。该设置不是服务端权威校验。 |
| `client-side-chunk-generation-enabled` | `true` | `true`、`false` | 是否允许客户端在玩家交互距离外生成视觉区块。 |
| `block-network-ids-are-hashes` | `true` | `true`、`false` | 是否发送哈希形式的方块网络ID，而不是从`0`开始的连续ID。 |
| `disable-custom-skins` | `false` | `true`、`false` | 是否禁用玩家在市场或游戏内资源以外自定义的皮肤。 |
| `server-build-radius-ratio` | `Disabled` | `Disabled`或`0.0`至`1.0`的浮点数 | 当客户端侧区块生成开启时，控制服务器生成玩家视野内容的比例。 |
| `allow-outbound-script-debugging` | `false` | `true`、`false` | 是否启用脚本调试器`connect`命令，以及`script-debugger-auto-attach`的`connect`模式。 |
| `allow-inbound-script-debugging` | `false` | `true`、`false` | 是否启用脚本调试器`listen`命令，以及`script-debugger-auto-attach`的`listen`模式。 |
| `force-inbound-debug-port` | `19144` | `1`至`65535`的整数 | 固定入站调试器端口。`listen`自动附加模式需要该端口。 |
| `script-debugger-auto-attach` | `disabled` | `disabled`、`connect`、`listen` | 世界加载时是否自动附加脚本调试器。 |
| `script-debugger-auto-attach-connect-address` | `localhost:19144` | `hostname:port`格式字符串 | `connect`自动附加模式使用的调试器地址。 |
| `script-debugger-auto-attach-timeout` | `0` | 非负整数 | 世界加载时等待调试器附加的秒数。 |
| `script-debugger-passcode` | 无 | 字符串 | 连接Visual Studio Code脚本调试器时要求输入的口令。 |
| `script-watchdog-enable` | `true` | `true`、`false` | 是否启用脚本看门狗。 |
| `script-watchdog-enable-exception-handling` | `true` | `true`、`false` | 是否通过`events.beforeWatchdogTerminate`事件启用看门狗异常处理。 |
| `script-watchdog-enable-shutdown` | `true` | `true`、`false` | 未处理看门狗异常时是否关闭服务器。 |
| `script-watchdog-hang-exception` | `true` | `true`、`false` | 脚本挂起时是否抛出严重异常并中断执行。 |
| `script-watchdog-hang-threshold` | `10000` | 以随BDS发行的配置注释为准 | 单刻挂起阈值。Microsoft Learn当前资料的允许值说明与字段含义不一致，使用时应核对当前版本BDS自带注释。 |
| `script-watchdog-spike-threshold` | `100` | 正整数 | 单刻脚本尖峰阈值。留空时禁用警告。 |
| `script-watchdog-slow-threshold` | `10` | 正整数 | 多刻慢脚本阈值。留空时禁用警告。 |
| `script-watchdog-memory-warning` | `100` | `0`至`2000`的整数 | 脚本总内存使用超过指定兆字节数时输出内容日志警告；`0`禁用警告。 |
| `script-watchdog-memory-limit` | `250` | `0`至`2000`的整数 | 脚本总内存使用超过指定兆字节数时保存并关闭世界；`0`禁用限制。 |
| `diagnostics-capture-auto-start` | `false` | `true`、`false` | 世界加载时是否开始诊断捕获会话。 |
| `diagnostics-capture-max-files` | `5` | 非负整数 | 轮换前保留的最大诊断捕获文件数量。 |
| `diagnostics-capture-max-file-size` | `2097152` | 正整数 | 当前诊断捕获文件轮换到新文件前的最大字节数。 |
| `disable-client-vibrant-visuals` | `true` | `true`、`false` | 是否要求客户端使用次优图形设置而不是鲜艳视效。 |

<!-- md:sortable -->

## 相关文件

- {{file|allowlist.json}}：当`allow-list`为`true`时，保存允许连接的玩家列表。
- {{file|permissions.json}}：保存操作员和权限级别信息。
- {{file|config/default/permissions.json}}：保存BDS脚本模块默认可访问的脚本API模块列表。