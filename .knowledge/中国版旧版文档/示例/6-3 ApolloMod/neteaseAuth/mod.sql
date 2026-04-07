CREATE TABLE IF NOT EXISTS `neteasePlayerAuth` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `auth_group` int unsigned NOT NULL COMMENT '玩家权限分组',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;