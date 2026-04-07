CREATE TABLE IF NOT EXISTS `playerCol` (
  `uid` bigint unsigned NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `login_time` bigint unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;