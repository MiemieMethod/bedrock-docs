CREATE TABLE IF NOT EXISTS `neteaseGuildPlayerCol` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `name` varchar(50) NOT NULL COMMENT '玩家名字',
  `guild_id` int signed NOT NULL COMMENT '所在公会id',
  `duty` int unsigned NOT NULL COMMENT '职务',
  `activity` int unsigned NOT NULL COMMENT '活跃度',
  `player_level` int unsigned NOT NULL COMMENT '等級',
  `last_login_time` int unsigned NOT NULL COMMENT '上次登录的时间',
  PRIMARY KEY (`uid`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE IF NOT EXISTS `neteaseGuildCol` (
  `guild_id` int unsigned NOT NULL COMMENT '公会id',
  `name` varchar(50) NOT NULL COMMENT '公会名字',
  `map_id` int signed NOT NULL COMMENT '地图标识',
  `max_num` int signed NOT NULL COMMENT '上限人数',
  `activity` int signed NOT NULL COMMENT '活跃度',
  `un_active_day` int signed NOT NULL COMMENT '活跃度不足的天数',
  PRIMARY KEY (`guild_id`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE IF NOT EXISTS `neteaseGuildApplication` (
  `guild_id` int unsigned NOT NULL COMMENT '公会id',
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `application_time` int signed NOT NULL COMMENT '申请时间',
  KEY (`guild_id`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;