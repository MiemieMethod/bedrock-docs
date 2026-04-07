---
sidebarDepth: 1
---

# <span id="启动器信息API"></span>启动器信息API

这里是获取启动器信息的接口

<span id="玩家"></span>
### 玩家

<span id="ApplyUserFriend"></span>
#### ApplyUserFriend

- 描述

    **Lobby/Game接口**，申请添加为启动器中的好友
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | requestUID | int | 玩家的uid |
    | appliedUID | int | 被申请添加好友玩家的uid |
    | message | str | 申请的好友的描述信息 |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段b_success，b_success表示申请是否成功。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #申请成功返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_success': true}}
        #申请失败返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_success': false}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.ApplyUserFriend(123, 456, '我想加个好友', callback)
```
<span id="GetPeGameUserStars"></span>
#### GetPeGameUserStars

- 描述

    **Master/Service/Lobby/Game接口**，获取玩家对本游戏的评分
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段stars，表示玩家评分，评分正常范围为1-5，值为-1表示没有评分数据。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'stars': 1}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetPeGameUserStars(123, callback)
```
<span id="GetUIDByNickname"></span>
#### GetUIDByNickname

- 描述

    **Master/Service/Lobby/Game接口**，根据玩家昵称获取玩家uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | nickname | str | 玩家昵称，要求是utf8编码 |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段uid，表示玩家的uid。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'uid': 2147583768}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUIDByNickname('我的昵称', callback)
 ```
<span id="GetUserFriend"></span>
#### GetUserFriend

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家好友信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段friend_uids，friend_uids对应内容是个list，对应好友玩家uid列表。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'friend_uids': [234,456]}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUserFriend(123, callback)
```
<span id="GetUserGuest"></span>
#### GetUserGuest

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家是否游客的信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段guest，表示玩家是否游客，字段意义 0：非游客，1：游客，2：不确定。 |
- 返回值

    无
- 备注

    除了官网渠道和苹果渠道之外，其他第三方渠道启动器无法返回确定的游客信息，guest字段返回2
    
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'guest': 1}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUserGuest(123, callback)
```
<span id="GetUsersVIP"></span>
#### GetUsersVIP

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家会员信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uids | list(int) | 玩家的uid列表，列表长度不超过20 |
    | callback | function | 回调函数，该函数会被异步执行。函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；        "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段users_vip，users_vip对应内容是个dict，key表示玩家uid，value表示是否是vip。 |
- 返回值

    无
- 备注

    只能获取体验过本游戏玩家会员信息。要求在MCStudio中配置游戏ID（路径：服务器配置->更多->游戏ID）
    
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'users_vip': {u'123': True}}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUsersVIP([123], callback)
```
<span id="ShareApolloGame"></span>
#### ShareApolloGame

- 描述

    **Lobby/Game接口**，在RN上拉起“网络游戏分享”的界面，界面包含游戏ICON以及描述
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int | 玩家的uid |
    | message | str | 分享的描述信息，不能超过20个字符，要求传入utf8字符串 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 拉起分享界面是否成功。False：存在敏感词或游戏ID为0或玩家不在线或分享信息超过20个字符 |
- 示例

```python
import apolloCommon.launcherApi as launcherApi
# 注意要求传入utf8字符串
ret = launcherApi.ShareApolloGame(123, u'这款游戏挺不错的，大家试试')
```
