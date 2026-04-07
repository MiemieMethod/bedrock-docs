-- ###########################version1.0.0####################
-- 玩家货币持有信息表
CREATE TABLE IF NOT EXISTS `neteaseTradePlayerDoughInfo` (
  `uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
  `dough_id` VARCHAR(10) NOT NULL COMMENT '货币类型，字符串ID，该种类货币的唯一标识',
  `balance` VARCHAR(10) NOT NULL COMMENT '货币持有数量',
  PRIMARY KEY (uid, dough_id) COMMENT '主键',
  INDEX `uid_index` (uid) COMMENT '用户ID索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 玩家商店购买信息表
CREATE TABLE IF NOT EXISTS `neteaseTradePlayerGroceryInfo` (
  `uid` INT UNSIGNED NOT NULL COMMENT '用户唯一ID',
  `grocery_id` VARCHAR(10) NOT NULL COMMENT '商店类型，字符串ID，该种类商店的唯一标识',
  `good_id` VARCHAR(10) NOT NULL COMMENT '商品于商店下的唯一标识，字符串ID',
  `bought` INTEGER NOT NULL COMMENT '已购次数',
  PRIMARY KEY (uid, grocery_id, good_id) COMMENT '主键',
  INDEX `uid_index` (uid) COMMENT '用户ID索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- 商店刷新表
CREATE TABLE IF NOT EXISTS `neteaseTradeGroceryRefreshInfo` (
  `grocery_id` VARCHAR(10) NOT NULL COMMENT '商店类型，字符串ID，该种类商店的唯一标识',
  `last_reset_date` VARCHAR(10) NOT NULL COMMENT '商店上次重置日期',
  PRIMARY KEY (grocery_id) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- ###########################version2.0.0####################
-- 玩家摆摊商品表
CREATE TABLE IF NOT EXISTS `neteaseTradeSaleMerchInfo` (
  `_id` INT PRIMARY KEY AUTO_INCREMENT,
  `uid` INT UNSIGNED NOT NULL,
  `currency` VARCHAR(10) NOT NULL,
  `unit` INTEGER NOT NULL,
  `qty` INTEGER NOT NULL,
  `init` INTEGER NOT NULL,
  `stuff` TEXT NOT NULL,
  `available` TINYINT(1) DEFAULT 0
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;