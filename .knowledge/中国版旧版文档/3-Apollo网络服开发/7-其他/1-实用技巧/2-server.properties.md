# server.properties

## 游戏玩法相关

### gamemode
* 类型：int（0-2）
* 默认值：0
* 说明：定义默认游戏模式
* 举例：0-生存模式；1-创造模式；2-冒险模式
### force-gamemode
* 类型：bool
* 默认值：false
* 说明：强制玩家加入时为默认游戏模式
* 举例：false-玩家将以退出前的游戏模式加入；true-玩家总是以默认游戏模式加入
### difficulty
* 类型：string
* 默认值：easy
* 说明：定义服务器的游戏难度（例如生物对玩家造成的伤害，饥饿与中毒对玩家的影响方式等）
* 举例：peaceful(或0)-和平；easy(或1)-简单；normal(或2)-普通；hard(或3)-困难
### player-idle-timeout
* 类型：int
* 默认值：30
* 说明：设置玩家多久空闲无操作会被踢出游戏。

### enable-netease-vip

- 类型：bool
- 默认值：false
- 说明：设置是否开启网易官方会员组件。默认为不开启

## 游戏地图相关
### level-name
* 类型：string
* 默认值：level
* 说明：定义游戏启动后加载的世界地图所在的文件夹名字，对应文件夹需要位于worlds/下
### level-seed
* 类型：int
* 默认值：空白
* 说明：生成地形时的随机数种子，留空将随机选择种子
### level-type
* 类型：string
* 默认值：DEFAULT
* 说明：确定随机地图所生成的类型
* 举例：DEFAULT-标准的世界带有丘陵，河谷，海洋等；FLAT-一个没有特色的平坦世界，适合用于建设；LEGACY-旧世界类型
### tick-distance
* 类型：int(4-12)
* 默认值：4
* 说明：停止加载区块的距离，当玩家远离某个区块的距离超过设定值后，该区块会停止加载
### view-distance
* 类型：int
* 默认值：10
* 说明：玩家可视距离最大值，单位为区块
### max-threads
* 类型：int
* 默认值：8
* 设置服务器使用的最大线程数，如果设置为0，服务器会尽可能多地使用所有线程。

## 玩家权限相关
### max-players
* 类型：int
* 默认值：10
* 说明：设置服务器同时能容纳的最大玩家数量
### op-permission-level
* 类型：int（1-4）
* 默认值：1
* 说明：玩家默认OP权限等级，越大就拥有更多的command的执行权限，每个command执行需要不同的op等级
### allow-cheats
* 类型：bool
* 默认值：false
* 说明：是否允许某些作弊行为
* 举例：true-允许作弊行为（使用命令方块等）；false-不允许作弊行为
### default-player-permission-level
* 类型：string
* 默认值：member
* 说明：设置新玩家加入服务器时的基础权限，
* 举例：visitor-新玩家不可破坏方块；member-新玩家正常加入；operator-新玩家加入时即为OP
  default-player-permission-level=member

## 更多信息
更多具体信息可以查看https://minecraft-zh.gamepedia.com/Server.properties资料
## 自动生成的配置项
服务器端口等配置信息，会在服务器部署的时候，由部署脚本统一生成，在Mod中手动配置并不会部署后生效