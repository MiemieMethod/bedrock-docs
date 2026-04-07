根目录为exe文件所在目录
1、server的mod的放置在developer_mods目录下
2、client的mod
	2.1、resource结尾的放置在resource_packs目录下，
		必须把对应的world_resource_packs.json放置在worlds/level/目录下，客户端才会加载
	2.2、behavior结尾的放置在behavior_packs目录下，
		必须把对应的world_behavior_packs.json放置在worlds/level/目录下，客户端才会加载

主城完整版：
1、server需要四个mod
	database
	online
	sample
	shutdown
2、client需要两个mod
	ntes_sample_behavior
	ntes_sample_resource
3、主城server.properties重命名为server.properties，放置在根目录


游戏最简版：
1、server需要两个mod
	online
	shutdown
