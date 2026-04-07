---
sidebarDepth: 1
---

# <span id="4-控制服API"></span>4-控制服API

这里是一些Master的基础API接口。

<span id="配置"></span>
### 配置

<span id="GetCommonConfig"></span>
#### GetCommonConfig

- 描述

    获取服务器公共配置，包括所有服务器和db的配置，具体参见备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 配置内容 |
- 备注

    服务器公共配置的示例如下，只展示了核心配置信息：
    ```
    {
    "apolloid":111,
    "extra_redis":{
    },
    "game_id":0,
    "game_key":"game_key",
    "gas_server_url":"http://127.0.0.1:111",
    "log_debug_level":true,
    "master":{
    "app_type":"master",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "keep_alive_period":30,
    "master_port":0,
    "mods":"",
    "port":8000,
    "serverid":0,
    "type":"master"
    },
    "mongo":null,
    "mysql":{
    "database":"test_db",
    "host":"127.0.0.1",
    "password":"test_password",
    "port":3306,
    "user":"test_user"
    },
    "redis":{
    "host":"127.0.0.1",
    "password":"",
    "port":6379
    },
    "review_stage":0,
    "serverlist":[
    {
    "app_type":"proxy",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":11003,
    "max_players":0,
    "mods":"",
    "optimum_players":0,
    "port":11002,
    "save":false,
    "serverid":2000,
    "type":"proxy"
    },
    {
    "app_type":"lobby",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":13003,
    "max_players":200,
    "mods":"neteaseRound",
    "optimum_players":0,
    "port":13002,
    "save":false,
    "serverid":4000,
    "type":"lobby"
    }
    ],
    "servicelist":[
    ],
    }
    ```
    
    
- 示例

```python
import master.netgameApi as netMasterApi
conf = netMasterApi.GetCommonConfig()
serverlist = conf['serverlist'] #获取serverlist配置
bDebugLevel = conf['log_debug_level'] #获取日志等级配置
 ```
<span id="IsService"></span>
#### IsService

- 描述

    服务器是否是service服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True表示是service，False不是service |
- 备注

    本api取代【masterConf.isService】，【masterConf.isService】废弃。
    
    
- 示例

```python
import master.netgameApi as netMasterApi
bService = netMasterApi.IsService(10)
 ```
<span id="玩家"></span>
### 玩家

<span id="BanUser"></span>
#### BanUser

- 描述

    封禁某个玩家
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家uid |
    | banTime | int | 封禁时间，单位为秒，-1表示永封 |
    | reason | str | 封禁原因，使用utf8编码。 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 备注

    效果说明如下：
    
    若banTime>0，则被封禁玩家登陆会提示：您的账号已经被封禁，剩余封禁时间：x天y小时z分，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    
    若banTime=-1，则被封禁玩家登陆会提示：您的账号已经被永久封禁，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    
    
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456，被封禁86400秒，封禁原因是“作弊被封禁一天”
netMasterApi.BanUser(123456, 86400, '作弊被封禁一天')
 ```
<span id="SetLoginStratege"></span>
#### SetLoginStratege

- 描述

    设置玩家登陆选服策略，要求服务器启动后加载mod时候设置
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | func | function | 计算玩家登陆服务器，包含两个参数：第一个参数为玩家uid；第二个参数为回调函数，执行后续登陆逻辑，无论登陆是否成功，必须要执行，回调函数只有一个参数，也即目标服务器。 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
def loginStratege(uid, callback):
        targetId = 20000 #登陆到id为20000的服务器
        callback(targetId) #必须执行，执行登陆后续操作
import master.netgameApi as netMasterApi
netMasterApi.SetLoginStratege(loginStratege)
 ```
<span id="SilentByUID"></span>
#### SilentByUID

- 描述

    禁言某个玩家
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家uid |
    | banTime | int | 禁言时间，单位为秒，-1表示永封 |
    | reason | str | 禁言原因，使用utf8编码 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456被禁言，禁言86400秒，禁言原因“说了敏感内容，被禁言一天”
netMasterApi.SilentByUID(123456, 86400, '说了敏感内容，被禁言一天')
 ```
<span id="UnBanUser"></span>
#### UnBanUser

- 描述

    解除某个玩家的封禁
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456解除封禁
netMasterApi.UnBanUser(123456)
 ```
<span id="UnSilentByUID"></span>
#### UnSilentByUID

- 描述

    解除某个玩家的禁言
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456被解除禁言
netMasterApi.UnSilentByUID(123456)
 ```
这里是Master的Http接口

<span id="HTTP服务器"></span>
### HTTP服务器

<span id="RegisterMasterHttp"></span>
#### RegisterMasterHttp

- 描述

    注册一个新的TTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
    | binder | instance | 响应HTTP请求的实例 |
    | func | function | 响应HTTP请求的实例函数 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                masterHttp.RegisterMasterHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，SendHttpResponse中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果
                response = '{"code":0,"message":"ok"}'
                masterHttp.SendHttpResponse(clientId, response)
 ```
<span id="SendHttpRequestToService"></span>
#### SendHttpRequestToService

- 描述

    给service发送http请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | service的服务器id |
    | requestUrl | str | 请求url，例如“/test-reqeust” |
    | body | str | HTTP post body，是个json字符串 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
params = {
        "message":"content",
        "code":1
 }
url = "/test-reqeust"
masterHttp.SendHttpRequestToService(8000, url, json.dumps(params))
 ```
<span id="SendHttpResponse"></span>
#### SendHttpResponse

- 描述

    发送HTTP的Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | message | str | HTTP Response的内容 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                masterHttp.RegisterMasterHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，SendHttpResponse中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果
                response = '{"code":0,"message":"ok"}'
                masterHttp.SendHttpResponse(clientId, response)
 ```
这里是master关于服务器管理的一些接口

<span id="服务器管理"></span>
### 服务器管理

<span id="GetAllServerStatus"></span>
#### GetAllServerStatus

- 描述

    获取所有服务器的状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务。
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | key:int类型，服务器id，value:int类型，服务器状态。服务器状态如下：<br/> 1:断开连接状态<br/>2:已连接状态<br/> 3:关服状态<br/>4:优雅关服状态<br/>6, 滚动更新中间状态，即将转换到状态7<br/>7 也是滚动更新中间状态，即将转换到状态1或2 |
- 备注

    服务器状态中，2表示正常服务，其他表示不能正常服务。
    
    
- 示例

```python
import master.serverManager as serverManager
statusDict = serverManager.GetAllServerStatus()
 ```
<span id="GetAllServersOnlineNum"></span>
#### GetAllServersOnlineNum

- 描述

    获取所有服务器的在线人数
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | key，int类型，表示服务器id，value，int类型，表示服务器在线人数 |
- 示例

```python
import master.serverManager as serverManager
onlineDict = serverManager.GetAllServersOnlineNum()
 ```
<span id="GetConnectedLobbyAndGameIds"></span>
#### GetConnectedLobbyAndGameIds

- 描述

    获取所有已经连接的lobby/game的服务器id列表
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list | 服务器id列表，服务器id是int类型。 |
- 示例

```python
import master.serverManager as serverManager
idList = serverManager.GetConnectedLobbyAndGameIds()
 ```
<span id="GetOneServerStatus"></span>
#### GetOneServerStatus

- 描述

    获取服务器状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务器状态。服务器状态如下：<br/> 1:断开连接状态<br/>2:已连接状态<br/> 3:关服状态<br/>4:优雅关服状态<br/>6, 滚动更新中间状态，即将转换到状态7<br/>7 也是滚动更新中间状态，即将转换到状态1或2 |
- 示例

```python
import master.serverManager as serverManager
status = serverManager.GetOneServerStatus(6000)
 ```
<span id="GetOnlineNumByServerId"></span>
#### GetOnlineNumByServerId

- 描述

    获取服务器(lobby/game/proxy)的在线人数
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetOnlineNumByServerId(4000)
 ```
<span id="GetOnlineNumByServerType"></span>
#### GetOnlineNumByServerType

- 描述

    获取某类型服务器的在线人数
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型，支持代理服/大厅服/游戏服的游戏类型（具体查看studio游戏配置中“类型”配置） |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetOnlineNumByServerType("lobby")
 ```
<span id="GetServerProtocolVersion"></span>
#### GetServerProtocolVersion

- 描述

    获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 协议版本 |
- 示例

```python
import master.serverManager as serverManager
version = serverManager.GetServerProtocolVersion(4000)
 ```
<span id="GetTotalOnlineNum"></span>
#### GetTotalOnlineNum

- 描述

    获取总得在线人数
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetTotalOnlineNum()
 ```
<span id="IsConnectedServer"></span>
#### IsConnectedServer

- 描述

    master是否与lobby/game/proxy建立连接
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，已经建立连接;False未建立连接 |
- 示例

```python
import master.serverManager as serverManager
bConnect = serverManager.IsConnectedServer(4000)
 ```
<span id="IsValidServer"></span>
#### IsValidServer

- 描述

    服务器是否有效。一种用途：master将玩家分配到服务器之前，会检查服务器是否有效，避免把玩家分配到一个即将关闭的服务器中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，master已经同服务器建立链接，且服务器正在提供服务，不是即将关闭的服务。 |
- 示例

```python
import master.serverManager as serverManager
bValid = serverManager.IsValidServer(4000)
 ```
<span id="StopServerByServerid"></span>
#### StopServerByServerid

- 描述

    关闭某个服务器。若MCStudio配置网络游戏时设置了“崩溃自动拉起”，则关闭服务器后会被自动拉起，实现重启功能
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | proxy/lobby/game服务器id |
    | actType | int | 1:强制踢出所有玩家后关服;2:等待所有玩家退出后关服 |
- 返回值

    无
- 示例

```python
import master.serverManager as serverManager
serverManager.StopServerByServerid(4000, 2)
 ```
