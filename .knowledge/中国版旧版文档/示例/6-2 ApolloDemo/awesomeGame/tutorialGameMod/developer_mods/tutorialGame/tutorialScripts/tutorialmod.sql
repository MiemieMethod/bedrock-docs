CREATE TABLE IF NOT EXISTS `tutorialmod` (
  `uid` bigint unsigned NOT NULL,
  `DiamondSwordNum` int unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;