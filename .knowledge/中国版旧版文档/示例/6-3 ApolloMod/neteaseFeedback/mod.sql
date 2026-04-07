CREATE TABLE IF NOT EXISTS `neteaseFeedbackMessage` (
  `id` int unsigned primary key auto_increment COMMENT '反馈id',
  `message` varchar(500) not null COMMENT '反馈内容',
  `uid` bigint signed NOT NULL COMMENT '玩家uid',
  `userName` varchar(20) NOT NULL COMMENT '玩家名字',
  `createTime` int unsigned not null COMMENT '创建时间',
  INDEX `idx_uid` (uid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFeedbackTagType` (
  `id` int unsigned primary key auto_increment COMMENT 'tag的id',
  `type` varchar(20) not null COMMENT '反馈标签描述',
  UNIQUE KEY `idx_type` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFeedbackHasTag` (
  `id` int unsigned primary key auto_increment COMMENT 'tag的id',
  `messageId` int unsigned not null COMMENT '消息的Id',
  `tagId` int unsigned not null COMMENT '标签的Id',
  UNIQUE KEY `idx_messageId_tagId` (`messageId`, `tagId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;