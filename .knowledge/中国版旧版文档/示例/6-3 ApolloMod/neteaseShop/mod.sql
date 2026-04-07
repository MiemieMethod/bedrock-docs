CREATE TABLE IF NOT EXISTS `neteaseOrderHistory` (
  `uid` bigint unsigned NOT NULL COMMENT '玩家uid',
  `_id` bigint unsigned NOT NULL COMMENT '订单id',
  `item_id` bigint unsigned NOT NULL COMMENT '商品id',
  `buy_time` int unsigned NOT NULL COMMENT '购买时间',
  `item_num` int unsigned NOT NULL COMMENT '购买数量',
  PRIMARY KEY (`uid`,`_id`) COMMENT '主键'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;