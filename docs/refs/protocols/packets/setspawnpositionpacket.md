# <!-- md:samp SetSpawnPositionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetSpawnPositionPacket -->数据包，数字ID是`43`。

## 结构

```viz
digraph SetSpawnPositionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
	}
	0	[comment="name: \"SetSpawnPositionPacket\", typeName: \"\", id: 0, branchId: 43, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetSpawnPositionPacket];
	1	[comment="name: \"Spawn Position Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SpawnPositionType\"",
		label="Spawn Position Type"];
	0 -> 1;
	3	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 3;
	5	[comment="name: \"Dimension type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Dimension type"];
	0 -> 5;
	7	[comment="name: \"Spawn Block Pos\", typeName: \"NetworkBlockPosition\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Spawn Block Pos"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
SetSpawnPositionPacket

Spawn Position Type：<!-- md:samp varint -->

- 类型：varint。enumeration: SpawnPositionType

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Dimension type：<!-- md:samp varint -->

- 类型：varint。

Spawn Block Pos：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。


///
