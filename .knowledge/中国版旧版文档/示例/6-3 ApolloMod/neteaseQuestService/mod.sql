-- ###########################version1.0.0####################
-- 任务数据信息表
CREATE TABLE IF NOT EXISTS `neteaseQuestDataInfo` (
  `uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
  `done` TINYINT(1) NOT NULL COMMENT '是否为已完成任务数据',
  `rec` LONGTEXT NOT NULL COMMENT '任务数据',
  PRIMARY KEY (uid, done) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;