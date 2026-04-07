-- ###########################version1.0.0####################
-- 玩家活动奖励领取信息表
CREATE TABLE IF NOT EXISTS `neteaseChillRewardInfo` (
  `uid` INT UNSIGNED NOT NULL PRIMARY KEY COMMENT '用户唯一ID',
  `achv_date` VARCHAR(20) NOT NULL COMMENT '达成日期',
  `recv_date` VARCHAR(20) NOT NULL DEFAULT '-1' COMMENT '领取日期'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;