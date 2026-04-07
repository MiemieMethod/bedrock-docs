-- ###########################version1.0.0####################
-- 玩家每日登录奖励领取信息表
CREATE TABLE IF NOT EXISTS `neteaseDailyRewardInfo` (
  `uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
  `recv_date` VARCHAR(10) NOT NULL COMMENT '领取日期',
  PRIMARY KEY (uid, recv_date) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;