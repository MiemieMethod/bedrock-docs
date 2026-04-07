-- ###########################version1.0.0####################
-- 登录弹窗
CREATE TABLE IF NOT EXISTS `neteaseFlyPluginInfo` (
`uid` INT UNSIGNED NOT NULL auto_increment COMMENT '用户唯一ID',
`flyState` INT UNSIGNED NOT NULL COMMENT '是否处于飞行状态',
`flyCnt` INT UNSIGNED NOT NULL COMMENT '飞行时间计数器',
PRIMARY KEY (uid) COMMENT '主键'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;