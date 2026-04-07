-- ###########################version1.0.0####################
-- 存储玩家外观
CREATE TABLE IF NOT EXISTS `neteaseAppearInfo` (
`uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
`appearInfo` VARCHAR(2000) NOT NULL DEFAULT '' COMMENT '玩家外观的解锁和选中信息，使用json.dumps序列化',
PRIMARY KEY (uid) COMMENT '主键'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;