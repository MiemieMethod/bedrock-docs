create table score_rank(
	uid bigint unsigned not null primary key,
	rank_id int not null default -1,
	score int unsigned not null default 0,
	nickname varchar(50) not null default ''
);

insert into score_rank (uid, rank_id, score, nickname) values (1,1, 10, 'test1');
insert into score_rank (uid, rank_id, score, nickname) values (2,2, 9, 'test2');
insert into score_rank (uid, rank_id, score, nickname) values (3,3, 8, 'test3');
insert into score_rank (uid, rank_id, score, nickname) values (4,4, 7, 'test4');
insert into score_rank (uid, rank_id, score, nickname) values (5,5, 6, 'test5');
insert into score_rank (uid, rank_id, score, nickname) values (6,6, 5, 'test6');
insert into score_rank (uid, rank_id, score, nickname) values (7,7, 4, 'test7');
insert into score_rank (uid, rank_id, score, nickname) values (8,8, 3, '118');