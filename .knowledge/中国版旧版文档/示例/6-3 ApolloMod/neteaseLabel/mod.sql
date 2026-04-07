-- ###########################version1.0.0####################
-- 玩家称号信息表
CREATE TABLE IF NOT EXISTS `neteaseLabelDataInfo` (
  `uid` int(10) unsigned NOT NULL COMMENT '用户唯一ID',
  `label_id` varchar(200) NOT NULL COMMENT '称号唯一ID',
  `recv_date` varchar(30) NOT NULL COMMENT '领取日期',
  `part` tinyint(1) NOT NULL COMMENT '称号位置',
  `in_use` tinyint(1) DEFAULT '0' COMMENT '是否为佩戴中',
  PRIMARY KEY (`uid`,`label_id`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;