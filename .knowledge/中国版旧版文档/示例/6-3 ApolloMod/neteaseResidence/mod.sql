-- ###########################version1.0.0####################
-- 玩家领地信息
CREATE TABLE IF NOT EXISTS `neteaseResidence` (
`resId` INT UNSIGNED NOT NULL COMMENT '领地id',
`name` VARCHAR(240) NOT NULL COMMENT '领地插件名字',
`serverType` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '服务器的type',
`area` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '区域坐标，前3个值表示区域(x, y, z)坐标最小值，后3个值表示最大值',
PRIMARY KEY (resId) COMMENT '主键',
UNIQUE KEY `type_id_uniq` (`serverType`, `resid`) COMMENT '领地唯一键索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteasePlayerResidence` (
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`resId` INT UNSIGNED NOT NULL COMMENT '领地id',
`serverType` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '服务器的type',
`uid` bigint unsigned NOT NULL COMMENT '玩家uid',
PRIMARY KEY (_id) COMMENT '主键',
KEY `uid_index` (`uid`) COMMENT '玩家索引',
UNIQUE KEY `type_id_uid_uniq` (`serverType`, `resid`, `uid`) COMMENT '领地唯一键索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- ###########################version1.0.1####################
-- 领地信息
ALTER TABLE `neteaseResidence` ADD COLUMN `resLevel` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '领地等级';
ALTER TABLE `neteaseResidence` ADD COLUMN `dimension` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '领地维度信息';
ALTER TABLE `neteaseResidence` ADD COLUMN `parentResId` INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '父领地的唯一ID';
ALTER TABLE `neteaseResidence` ADD COLUMN `authority` JSON DEFAULT NULL COMMENT '领地权限';
ALTER TABLE `neteaseResidence` ADD COLUMN `bornPos` VARCHAR(255) NOT NULL DEFAULT '' COMMENT '领地传送点';
-- 外部玩家权限设置
CREATE TABLE IF NOT EXISTS `neteaseOutPlayerResidenceAuthority` (
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`resId` INT UNSIGNED NOT NULL COMMENT '领地id',
`serverType` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '服务器的type',
`uid` bigint unsigned NOT NULL COMMENT '玩家uid',
`authority` JSON DEFAULT NULL COMMENT '领地权限',
PRIMARY KEY (_id) COMMENT '主键',
KEY `uid_index` (`uid`) COMMENT '玩家索引',
UNIQUE KEY `type_id_uid_uniq` (`serverType`, `resid`, `uid`) COMMENT '领地唯一键索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseOutPlayerResidenceApplication`(
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`resId` INT UNSIGNED NOT NULL COMMENT '领地id',
`serverType` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '服务器的type',
`uid` bigint unsigned NOT NULL COMMENT '玩家uid',
`applicationMessage` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '申请留言',
`authority` JSON DEFAULT NULL COMMENT '领地权限',
`userName` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '申请者名字',
PRIMARY KEY (_id) COMMENT '主键',
KEY `uid_index` (`uid`) COMMENT '玩家索引',
UNIQUE KEY `type_id_uid_uniq` (`serverType`, `resid`, `uid`) COMMENT '领地唯一键索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseOutPlayerResidenceMainAuth`(
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`resId` INT UNSIGNED NOT NULL COMMENT '领地id',
`serverType` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '服务器的type',
`uid` bigint unsigned NOT NULL COMMENT '玩家uid',
`mainAuth` JSON DEFAULT NULL COMMENT '领地主权限',
`userName` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '使用者名字',
PRIMARY KEY (_id) COMMENT '主键',
KEY `uid_index` (`uid`) COMMENT '玩家索引',
UNIQUE KEY `type_id_uid_uniq` (`serverType`, `resid`, `uid`) COMMENT '领地唯一键索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseResidencePlayerData` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `username` varchar(200) not null comment '玩家名字',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid` (uid)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `neteasePlayerResidence` ADD COLUMN `userName` VARCHAR(240) NOT NULL COMMENT '创建者名字';

CREATE TABLE IF NOT EXISTS `neteaseResidenceTransferUnread` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `resId` INT UNSIGNED NOT NULL COMMENT '领地id',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid` (uid, resId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `neteaseResidenceApplicationUnread` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `resId` INT UNSIGNED NOT NULL COMMENT '领地id',
  `applicatorUid` bigint unsigned NOT NULL COMMENT '申请者uid',
  INDEX `idx_uid` (uid),
  constraint unique `uniq_uid` (applicatorUid, resId)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ###########################version1.0.9####################
-- 领地ID全局唯一维护
CREATE TABLE IF NOT EXISTS `neteaseResidenceUniqueId` (
`askIndex` INT UNSIGNED NOT NULL COMMENT '申请分配领地ID的次数，用于防并发',
`usedResId` INT UNSIGNED NOT NULL COMMENT '已经分配出去的领地ID最大值',
PRIMARY KEY (askIndex) COMMENT '主键'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

