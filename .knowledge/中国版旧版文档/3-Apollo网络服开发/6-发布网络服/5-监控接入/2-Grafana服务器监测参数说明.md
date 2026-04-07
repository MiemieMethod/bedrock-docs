# Grafana服务器检测参数

## procstat

当前服务器进程性能参数（所有类型的进程都有）
* cpu_usage：当前服务器进程cpu的占用率，所有子线程的cpu占用之后，每个核算100%
* memory_rss：当前服务器进程占用的物理内存

## cpu_thread
当前服务器进程的各个子线程的性能参数（所有类型的进程都有）
* cpu_usage：当前选中子线程的cpu占用率

## proxy_stats
proxy服务器进程的在线信息（仅限proxy类型的进程）
* player_count：当前在线的client人数

## proxy_transfer
proxy服务器进程流量统计信息（仅限proxy类型的进程）
* server_pkg_num：proxy发送给server（lobby/game）服务器的数据包数量
* server_pkg_num_perminute：proxy发送给server（lobby/game）服务器的每分钟数据包数量
* client_pkg_num：proxy发送给client的数据包数量
* client_pkg_num_perminute：proxy发送给client的每分钟数据包数量
* server_bytes：proxy发送给server（lobby/game）服务器的数据总量
* server_bytes_perminute：proxy发送给server（lobby/game）服务器的每分钟数据总量
* client_bytes：proxy发送给client的数据总量
* client_bytes_perminute：proxy发送给client的每分钟数据总量

## server_playernum
当前服务器进程在线（仅限lobby/game类型的进程）
* num：当前服务器进程在线人数

## server_tps
当前服务器进程的帧率（master、service、lobby、game类型的进程都有，仅proxy没有）
* num：当前服务器进程帧率，master/service类型的服务器进程满帧率是60帧，game/lobby类型的服务器进程满帧率是30帧

## server_status
master统计到的每个服务器进程的服务状态
* status：状态标识，10--工作服，已连接状态（唯一的正常状态）； 0--服务器不存在； 1--正在工作的服，断线状态；3--强制关闭状态；4--优雅关机状态； 5--候选服，检查ok会成为正常工作服； 6--滚动更新候选服，检查ok会成为滚动更新就绪服；7--滚动更新就绪，滚动服都就绪后统一切换工作服。该状态服务器不会对外提供服务。

## player_action
master统计到的整个服务器组玩家的登录、登出、转服统计（仅限master类型的进程）
* login：玩家登录人次
* logout：玩家登出人次
* transfer：玩家转服人次

## master_playernum
master统计到的各个服务器进程的在线人数（仅限master类型的进程）
* serverid（进程代号）：master统计到的对应serverid的服务器进程的在线人数

## online_num
master统计到的各个种类的服务器级才能的在线人数（仅限master类型的进程）
* game：master统计到的所有game类型服务器进程的在线人数之和
* lobby：master统计到的所有lobby类型服务器进程的在线人数之和
* proxy：master统计到的所有proxy服务器进程的在线人数之和，所有的客户端都直接与porxy保持连接，所以proxy在线会计算game+lobby+转服中的三类不同玩家之和