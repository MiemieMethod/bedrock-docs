-- ###########################version1.0.0####################
-- 云端背包
CREATE TABLE IF NOT EXISTS `neteaseCloudItems` (
`_id` INT UNSIGNED NOT NULL auto_increment COMMENT '唯一ID，自增',
`uid` BIGINT UNSIGNED NOT NULL COMMENT '玩家uid',
`cloud_items` varchar(10000) NOT NULL DEFAULT '' COMMENT '记录云背包内容',
PRIMARY KEY (_id) COMMENT '主键',
INDEX `uid_idx` (`uid`) COMMENT '索引'
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- ###########################version2.0.0####################
alter table neteaseCloudItems add column apply_tag varchar(20) not null default "";
ALTER TABLE neteaseCloudItems ADD INDEX apply_tag_index (`apply_tag`, `uid`);
