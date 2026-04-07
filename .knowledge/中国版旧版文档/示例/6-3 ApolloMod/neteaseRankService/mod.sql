CREATE TABLE IF NOT EXISTS `neteaseRankData` (
  `id` int unsigned primary key auto_increment COMMENT '数据id',
  `rankData` MediumBlob not null comment 'rank的信息',
  `serverType` varchar(10) not null COMMENT 'server的type',
  `fromId` bigint unsigned not null COMMENT '数据来源的id，可能是玩家的id或者是公会的id',
  `insertTime` int signed NOT NULL COMMENT '上榜时间',
  INDEX `idx_serverType` (serverType)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
