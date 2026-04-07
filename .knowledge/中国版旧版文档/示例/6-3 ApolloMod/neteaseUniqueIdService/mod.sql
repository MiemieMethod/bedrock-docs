-- ###########################version1.0.0####################
-- 记录ID的域和对应已经分发出去的最大ID
CREATE TABLE `neteaseUniqueId` (
  `keyword` VARCHAR(200) NOT NULL COMMENT '生成ID的域，相同域的ID不会重复',
  `max_id` BIGINT UNSIGNED NOT NULL COMMENT '对于域的ID当前已经分发出去的最大ID',
  `plus` INT UNSIGNED NOT NULL COMMENT '每次从数据库预生成可用ID，生成多少个',
  PRIMARY KEY (`keyword`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
