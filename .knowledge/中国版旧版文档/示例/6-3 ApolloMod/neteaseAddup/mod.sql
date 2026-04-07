-- ###########################version1.0.0####################
-- 登录弹窗
CREATE TABLE IF NOT EXISTS `neteaseAddupData` (
`uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
`addupData` JSON DEFAULT NULL COMMENT '消费累积存档信息',
PRIMARY KEY (uid) COMMENT '主键'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;