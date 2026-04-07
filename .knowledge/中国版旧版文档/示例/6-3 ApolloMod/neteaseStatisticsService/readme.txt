插件介绍：
运营数据统计插件，运营数据统计插件支持统计DAU，MAU等运营数据。

插件构成:
（1）neteaseStatistics:部署于游戏服、大厅服。
（2）neteaseStatisticsService：部署于功能服，


使用步骤：
（1）请在mysql中执行mod.sql（位于neteaseStatisticsService中）
（2）配置game中的mod.json，请按照文件mod.json中"_comment"注释配置对应内容。
（3）MCStudio把neteaseStatistics添加到游戏服，把neteaseStatisticsService添加到功能服。
（4）如需统计收入数据，需在在处理订单的时候，调用sendPayEventByPlayerId函数提交数据

查看统计数据：
请参考【http://mc.163.com/mcstudio/mc-dev/MCDocs/3-Apollo%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%BC%80%E5%8F%91/5-%E5%8F%91%E5%B8%83%E7%BD%91%E7%BB%9C%E6%9C%8D/5-%E7%9B%91%E6%8E%A7%E6%8E%A5%E5%85%A5/1-Monitor%E7%9B%91%E6%8E%A7%E6%8A%A5%E8%AD%A6%E7%B3%BB%E7%BB%9F.html】
可以使用附带的
【min5.json】、【retain.json】、【daily.json】直接生成统计表格
请参考【http://mc.163.com/mcstudio/mc-dev/MCDocs/3-Apollo%E7%BD%91%E7%BB%9C%E6%9C%8D%E5%BC%80%E5%8F%91/5-%E5%8F%91%E5%B8%83%E7%BD%91%E7%BB%9C%E6%9C%8D/5-%E7%9B%91%E6%8E%A7%E6%8E%A5%E5%85%A5/1-Monitor%E7%9B%91%E6%8E%A7%E6%8A%A5%E8%AD%A6%E7%B3%BB%E7%BB%9F.html#%E4%BD%BF%E7%94%A8%E6%A8%A1%E6%9D%BF】

插件支持的运营数据类型：
【daily_account_new】：新增账号数
【daily_account_login】：登录账号数
【daily_account_pay】：付费总值（钻石）
【daily_pay_rate】：付费率
【daily_pay_diamand】：人均付费值（钻石）
【daily_avg_oltime】：平均在线时长
【daily_avg_new_oltime】：新增用户平均在线时长
【daily_avg_login_cnt】：平均进入次数
【daily_retain1】：一天留存率
【daily_retain3】：三天留存率
【daily_retain7】：七天留存率


插件原理
    本插件是将上述提到的运营数据类型存到grafana influxDB中，服主可以按照"查看统计数据"来查看grafana influxDB中的数据


插件api：
（1）提交玩家支付数据:如需统计收入数据，需在在处理订单的时候，调用此函数提交数据
适用服务器：lobby or game
函数：sendPayEventByPlayerId(playerId, pay, orderKey)
参数：
    playerId： str  玩家对象的entityId
    pay：int 支付的钻石数
	orderKey：str 订单的唯一ID
示例：
    import server.extraServerApi as serverApi
    system = serverApi.GetSystem("neteaseStatistics", "neteaseStatisticsServer")
    system.sendPayEventByPlayerId('1234455', 1000, "xxyyzz")
