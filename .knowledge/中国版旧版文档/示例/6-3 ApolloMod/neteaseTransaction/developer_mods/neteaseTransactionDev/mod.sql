-- ###########################version1.0.0####################
-- 登录弹窗
CREATE TABLE IF NOT EXISTS `neteaseTransactionInfo` (
`uid` INT UNSIGNED NOT NULL auto_increment COMMENT '用户唯一ID',
`lastUpdate` VARCHAR(8) NOT NULL COMMENT '上次更新日期',
`remainTimes` INT UNSIGNED NOT NULL COMMENT '今日剩余交易次数',
PRIMARY KEY (uid) COMMENT '主键'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;