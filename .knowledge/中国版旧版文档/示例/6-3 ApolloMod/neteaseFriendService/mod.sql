CREATE TABLE IF NOT EXISTS `neteaseFriendShip` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `fuid` bigint unsigned NOT NULL COMMENT '好友uid',
  `isRNFriend` bool not null default false COMMENT '是否RN好友',
  `time` int signed NOT NULL COMMENT '申请时间',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_fid` (uid, fuid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendUnread` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `fuid` bigint unsigned NOT NULL COMMENT '好友uid',
  `time` int signed NOT NULL COMMENT '申请时间',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_fid` (uid, fuid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendBlack` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `buid` bigint unsigned NOT NULL COMMENT '黑名单玩家uid',
  `time` int signed NOT NULL COMMENT '申请时间',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_buid` (uid, buid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendApply` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `auid` bigint unsigned NOT NULL COMMENT '申请玩家uid',
  `time` int signed NOT NULL COMMENT '申请时间',
  `message` varchar(200) not null comment '申请语',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_auid` (uid, auid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendChat` (
  `id` bigint unsigned primary key auto_increment COMMENT '消息id',
  `fromuid` bigint unsigned NOT NULL COMMENT '消息来源uid',
  `touid` bigint unsigned NOT NULL COMMENT '消息发送到玩家uid',
  `time` int signed NOT NULL COMMENT '申请时间',
  `message` varchar(300) not null comment '消息',
  INDEX `idx_fromuid_touid` (fromuid, touid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendPlayerData` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `username` varchar(200) not null comment '玩家名字',
  `head_image` varchar(200) not null comment '玩家头像框',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid` (uid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendShipRNAlreadySync` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `fuid` bigint unsigned NOT NULL COMMENT '好友uid',
  `time` int signed NOT NULL COMMENT '删除时间时间',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_fuid` (uid, fuid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseFriendTemp` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `fuid` bigint unsigned NOT NULL COMMENT '好友uid',
  `time` int signed NOT NULL COMMENT '申请时间',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid_fid` (uid, fuid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
