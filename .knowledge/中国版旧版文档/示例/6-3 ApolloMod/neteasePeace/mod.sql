-- ###########################version1.0.0####################
-- 玩家PVP记录表
CREATE TABLE IF NOT EXISTS `neteasePVPRec` (
  `uid1` int(10) unsigned NOT NULL COMMENT '用户唯一ID',
  `uid2` int(10) unsigned NOT NULL COMMENT '用户唯一ID',
  `foe` tinyint(1) NOT NULL COMMENT '0为击杀1为被杀',
  `uname` VARCHAR(44) NOT NULL COMMENT '玩家游戏内名称',
  `ts` INTEGER NOT NULL COMMENT '次数',
  `t` VARCHAR(44) NOT NULL COMMENT '时间',
  PRIMARY KEY (`uid1`, `uid2`, `foe`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 玩家PVP设置表
CREATE TABLE IF NOT EXISTS `neteasePVPPlayerInfo` (
  `uid` int(10) unsigned PRIMARY KEY COMMENT '用户唯一ID',
  `switch` tinyint(1) NOT NULL,
  `hood` tinyint(1) NOT NULL,
  `crew` tinyint(1) NOT NULL,
  `gang` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;