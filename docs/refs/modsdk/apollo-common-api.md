# Apollo公共接口<!-- md:flag china -->
本页汇总Apollo公共脚本接口，覆盖异步线程池、数据库连接池、通用工具、计时器与在线状态工具。
/// warning | Apollo专用能力
本页接口来自中国版Apollo网络服脚本环境。接口命名与调用方式与国际版脚本API不同，不能直接互换。
///

## 异步线程池
| 接口 | 说明 |
| --- | --- |
| `EmitOrder` | 添加一个异步任务 |
| `Finish` | 等待线程池退出，线程池会执行完所有异步任务后退出，会阻塞主线程。建议Mod退出时执行 |
| `ForkNewPool` | 创建线程池，设置线程池大小 |

## mysql连接池
| 接口 | 说明 |
| --- | --- |
| `AsyncExecuteFunctionWithOrderKey` | 添加一个异步mysql任务，func将在子线程中执行，注意func中不支持执行引擎提供的API |
| `AsyncExecuteWithOrderKey` | 添加一个异步mysql任务，执行所有mysql操作 |
| `AsyncExecutemanyWithOrderKey` | 添加一个异步mysql任务，针对同一条sql语句，使用paramsList中的每个参数各执行一次，并且返回成功修改/新建的记录数，其中任何一条语句执行失败，最终所有语句都会被执行失败，返回None |
| `AsyncInsertOneWithOrderKey` | 添加一个异步mysql任务，向主键为AUTO INCREASEl类型的表格中插入一条记录，并且返回新建记录的主键 |
| `AsyncQueryWithOrderKey` | 添加一个异步mysql任务，执行mysql查询 |
| `InitDB` | 初始化myqsl连接池，要求在MCStudio的“服务器配置”中配置mysql |
| `SyncFetchAll` | 阻塞性执行sql语句，查询数据 |
| `SyncInsert` | 阻塞性执行sql语句，插入数据 |

## redis连接池
| 接口 | 说明 |
| --- | --- |
| `AsyncDelete` | 执行redis操作，删除某个redis key,相当于redis中执行命令:del key |
| `AsyncFuncWithKey` | 添加一个异步redis任务 |
| `AsyncGet` | 执行redis操作，获取key的value,相当于redis中执行命令:get key |
| `AsyncHgetall` | 执行redis操作，获取key的value,相当于redis中执行命令:hgetall key |
| `AsyncMget` | 执行redis操作，获取多个key的值,相当于redis中执行命令:mget key1 key2 ... |
| `AsyncSet` | 执行redis操作，设置key的值为value,相当于redis中执行命令:set key value |

## mongo连接池
| 接口 | 说明 |
| --- | --- |
| `AsyncExecute` | 添加一个异步mongo任务 |

## 通用
| 接口 | 说明 |
| --- | --- |
| `ChangeDatabaseSlowLogLimit` | 修改数据库连接池慢请求报警日志限定时间 |
| `CheckNameValid` | 判定一个输入的string是否通过了命名库敏感词检查，没有敏感词返回1，存在敏感词返回0 |
| `CheckWordsValid` | 判定一个输入的string是否通过了通用库敏感词检查，没有敏感词返回1，存在敏感词返回0 |
| `CloseAsyncTaskSlowCheck` | 停止每帧检查异步线程池中的任务 |
| `ConvertBsonToInt` | 递归转换输入数据中的所有bson.int64.Int64类型的对象为int类型 |
| `DumpAsyncTaskPool` | 打印当前异步线程池中的正在排队和执行中的任务信息 |
| `GetApolloGameId` | 获取游戏当前项目的gameId（商城查询订单时需要） |
| `GetApolloGameKey` | 获取游戏当前项目的gameKey（商城查询订单时需要） |
| `GetApolloReviewStage` | 获取游戏当前审核阶段 |
| `GetApolloUniqueId` | 获取游戏当前项目唯一ID |
| `GetModJsonConfig` | 根据脚本根目录读取mod.json配置文件。要求mod已经被加载 |
| `GetModJsonConfigByName` | 读取基于脚本根目录的[pathFile]路径下的json格式配置文件 |
| `GetModScriptRootDir` | 获取脚本根目录的绝对路径。要求mod已经被加载 |
| `GetServerType` | 获取本服的服务器类型，对应MCStudio中配置：服务器配置->游戏配置->类型 |
| `OpenAsyncTaskSlowCheck` | 启动每帧检查异步线程池中的任务，并且打印执行时间超过指定时间且尚未完成的任务，此功能消耗较大，仅建议在测试阶段和遇到线上紧急问题时启用 |
| `StartDatabaseProfile` | 开始记录数据库连接池请求信息统计，启动后调用[StopDatabaseMysqlProfile(db)](#StopDatabaseMysqlProfile)即可获取两个函数调用之间数据库连接池请求记录信息 |
| `StartYappiProfile` | 开始启动服务端脚本性能分析，启动后调用[StopYappiProfile(path)](#StopYappiProfile)即可在路径path生成函数性能火焰图 |
| `StopDatabaseMysqlProfile` | 停止记录数据库连接池请求信息并输出统计结果，与[StartDatabaseProfile(db)](#StartDatabaseProfile)配合使用，输出结果为字典，具体见示例 |
| `StopYappiProfile` | 停止服务端脚本性能分析并生成火焰图，与[StartYappiProfile()](#StartYappiProfile)配合使用 |
| `UnicodeConvert` | 递归转换输入数据中的所有unicode格式的字符串为utf-8格式 |

## 世界
| 接口 | 说明 |
| --- | --- |
| `AddRepeatedTimer` | 添加服务端触发的定时器，重复执行 |
| `AddTimer` | 添加服务端触发的定时器，非重复 |
| `CancelTimer` | 取消定时器 |

## 玩家
| 接口 | 说明 |
| --- | --- |
| `GetOnlineKey` | 输入玩家uid，返回此玩家保存在redis中的在线标识的key |
| `GetOnlineServerInfoOfMultiPlayers` | 获取多个玩家在线信息 |
| `GetOnlineServerInfoOfPlayer` | 获取玩家在线信息 |
| `GetWeekOnlineKey` | 输入玩家uid，返回此玩家保存在redis中的本周的在线时间 |
| `ToPcUid` | 将玩家的uid转换为pc平台的uid |
| `ToPeUid` | 将玩家的uid转换为pe平台的uid |
