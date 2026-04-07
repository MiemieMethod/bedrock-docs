-- ###########################version1.0.0####################
-- 玩家持有弹幕头像信息表
CREATE TABLE IF NOT EXISTS `neteaseDanmuIconInfo` (
  `uid` int(10) UNSIGNED COMMENT '用户唯一ID',
  `icon_id` VARCHAR(44) NOT NULL COMMENT '头像资源id',
  PRIMARY KEY (uid, icon_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;