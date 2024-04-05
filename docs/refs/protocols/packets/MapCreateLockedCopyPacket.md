# <!-- md:samp MapCreateLockedCopyPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MapCreateLockedCopyPacket -->数据包，数字ID是`131`。

## 结构

```viz
digraph MapCreateLockedCopyPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"MapCreateLockedCopyPacket\", typeName: \"\", id: 0, branchId: 131, recurseId: -1, attributes: 0, notes: \"\"",
		label=MapCreateLockedCopyPacket];
	1	[comment="name: \"Original Map Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id of the map being \
locked.\"",
		label="Original Map Id"];
	0 -> 1;
	3	[comment="name: \"New Map Id\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id that the new map should \
have.\"",
		label="New Map Id"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
MapCreateLockedCopyPacket

Original Map Id：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。Id of the map being locked.

New Map Id：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。Id that the new map should have.


///
