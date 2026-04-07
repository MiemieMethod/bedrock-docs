-- ###########################version1.0.0####################
-- 玩家抽奖记录信息表
CREATE TABLE IF NOT EXISTS `hzistudioGachaChestData` (
  `_id` int NOT NULL AUTO_INCREMENT COMMENT '唯一id, 自增',
  `uid` INT UNSIGNED NOT NULL COMMENT '玩家uid',
  `poll_identifier` varchar(25) CHARACTER SET utf8mb4 NULL COMMENT '奖池标识符',
  `prize_data` varchar(255) CHARACTER SET utf8mb4 NULL COMMENT '奖励数据',
  `status` TINYINT(1) DEFAULT 0 COMMENT '奖励发放状态 0未发放 1已发放',
  `create_time` datetime NULL COMMENT '数据产生时间(玩家按下抽奖按钮)',
  `prize_time` datetime NULL COMMENT '奖励发放时间(动画播放完毕, 真正发放奖励时)',
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;