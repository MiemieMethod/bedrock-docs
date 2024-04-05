# <!-- md:samp UpdateSubChunkBlocksPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateSubChunkBlocksPacket -->数据包，数字ID是`172`。

## 结构

```viz
digraph UpdateSubChunkBlocksPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		10	[comment="name: \"unsigned varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"unsigned varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		14	[comment="name: \"unsigned varint64\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
		16	[comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		19	[comment="name: \"unsigned varint\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		22	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		24	[comment="name: \"unsigned varint\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		26	[comment="name: \"unsigned varint\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		28	[comment="name: \"unsigned varint64\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
		30	[comment="name: \"unsigned varint\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	0	[comment="name: \"UpdateSubChunkBlocksPacket\", typeName: \"\", id: 0, branchId: 172, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateSubChunkBlocksPacket];
	1	[comment="name: \"Sub Chunk Block Position\", typeName: \"NetworkBlockPosition\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Sub Chunk Block Position"];
	0 -> 1;
	3	[comment="name: \"Blocks Changed - Standards\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Blocks Changed - Standards"];
	0 -> 3;
	17	[comment="name: \"Blocks Changed - Extras\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Blocks Changed - Extras"];
	0 -> 17;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Pos\", typeName: \"NetworkBlockPosition\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Pos];
	6 -> 7;
	9	[comment="name: \"Runtime Id\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Runtime Id"];
	6 -> 9;
	11	[comment="name: \"Update Flags\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Update Flags"];
	6 -> 11;
	13	[comment="name: \"Sync Message - Entity Unique ID\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sync Message - Entity Unique ID"];
	6 -> 13;
	15	[comment="name: \"Sync Message - Message\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorBlockSyncMessage::\
MessageId\"",
		label="Sync Message - Message"];
	6 -> 15;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	18	[comment="name: \"Array Size\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	17 -> 18;
	20	[comment="name: \"example element\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	17 -> 20;
	18 -> 19;
	21	[comment="name: \"Pos\", typeName: \"NetworkBlockPosition\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Pos];
	20 -> 21;
	23	[comment="name: \"Runtime Id\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Runtime Id"];
	20 -> 23;
	25	[comment="name: \"Update Flags\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Update Flags"];
	20 -> 25;
	27	[comment="name: \"Sync Message - Entity Unique ID\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Sync Message - Entity Unique ID"];
	20 -> 27;
	29	[comment="name: \"Sync Message - Message\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorBlockSyncMessage::\
MessageId\"",
		label="Sync Message - Message"];
	20 -> 29;
	21 -> 22;
	23 -> 24;
	25 -> 26;
	27 -> 28;
	29 -> 30;
}

```

## 字段

/// define
UpdateSubChunkBlocksPacket

Sub Chunk Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Blocks Changed - Standards

//// define
Blocks Changed - Standards数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Blocks Changed - Standards的示例元素

Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Runtime Id：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Update Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Sync Message - Entity Unique ID：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。

Sync Message - Message：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ActorBlockSyncMessage::MessageId


////


Blocks Changed - Extras

//// define
Blocks Changed - Extras数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Blocks Changed - Extras的示例元素

Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Runtime Id：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Update Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Sync Message - Entity Unique ID：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。

Sync Message - Message：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ActorBlockSyncMessage::MessageId


////



///
