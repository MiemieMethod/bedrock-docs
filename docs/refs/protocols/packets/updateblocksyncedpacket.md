# <!-- md:samp UpdateBlockSyncedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateBlockSyncedPacket -->数据包，数字ID是`110`。

## 结构

```viz
digraph UpdateBlockSyncedPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		4	[comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"unsigned varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		10	[comment="name: \"varint64\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
		12	[comment="name: \"varint64\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint64];
	}
	0	[comment="name: \"UpdateBlockSyncedPacket\", typeName: \"\", id: 0, branchId: 110, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateBlockSyncedPacket];
	1	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 1;
	3	[comment="name: \"Block Runtime ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Block Runtime ID"];
	0 -> 3;
	5	[comment="name: \"Flags\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Flags];
	0 -> 5;
	7	[comment="name: \"Layer\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Layer];
	0 -> 7;
	9	[comment="name: \"Unique Actor Id\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id for the Moving Block Actor\"",
		label="Unique Actor Id"];
	0 -> 9;
	11	[comment="name: \"Actor Sync Message\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorBlockSyncMessage::\
MessageId\"",
		label="Actor Sync Message"];
	0 -> 11;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
UpdateBlockSyncedPacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Block Runtime ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Layer：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Unique Actor Id：<!-- md:samp varint64 -->

- 类型：varint64。Id for the Moving Block Actor

Actor Sync Message：<!-- md:samp varint64 -->

- 类型：varint64。enumeration: ActorBlockSyncMessage::MessageId


///
