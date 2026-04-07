-- ###########################version1.0.0####################
-- 用户静态信息
CREATE TABLE IF NOT EXISTS `neteaseStatsUser` (
`uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
`ctime` INT UNSIGNED NOT NULL COMMENT '首次登录时间',
`login_cnt` INT UNSIGNED NOT NULL COMMENT '登录次数',
`otime` INT UNSIGNED NOT NULL COMMENT '总在线时间',
`pay` INT UNSIGNED NOT NULL COMMENT '总支付',
`uptime` INT UNSIGNED NOT NULL COMMENT '最后更新时间',
primary key (uid) COMMENT '主键',
INDEX `ctime_index` (`ctime`) COMMENT '创建时间索引，方便查询留存'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 用户每日信息
CREATE TABLE IF NOT EXISTS `neteaseStatsUserDaily` (
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
`day_str` CHAR(10) NOT NULL COMMENT '日期，类似2019-12-17',
`flogin_time` INT UNSIGNED NOT NULL COMMENT '本日首次登录时间',
`ctime` INT UNSIGNED NOT NULL COMMENT '首次登录时间',
`login_cnt` INT UNSIGNED NOT NULL COMMENT '本日登录次数',
`otime` INT UNSIGNED NOT NULL COMMENT '本日总在线时间',
`pay` INT UNSIGNED NOT NULL COMMENT '本日总支付',
`uptime` INT UNSIGNED NOT NULL COMMENT '最后更新时间',
PRIMARY KEY (_id) COMMENT '主键',
constraint uni_rec unique (`uid`, `day_str`) COMMENT '每个用户每日都只有一条记录',
INDEX uid_uptime (`uid`, `uptime`) COMMENT '查询每个玩家的最新记录',
INDEX pay_day (`day_str`, `pay`) COMMENT '查询付费',
INDEX day_index (`day_str`) COMMENT '查询每日的信息',
INDEX ctime_index (`day_str`, `ctime`) COMMENT '查询留存'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
