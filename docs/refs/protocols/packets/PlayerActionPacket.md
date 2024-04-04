# <!-- md:samp PlayerActionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerActionPacket -->数据包，数字ID是`36`。

## 结构

```viz
digraph PlayerActionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		8	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"PlayerActionPacket\", typeName: \"\", id: 0, branchId: 36, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerActionPacket];
	1	[comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Action\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerActionType\"",
		label=Action];
	0 -> 3;
	5	[comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Block Position"];
	0 -> 5;
	7	[comment="name: \"Result Pos\", typeName: \"NetworkBlockPosition\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Result Pos"];
	0 -> 7;
	9	[comment="name: \"Face\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Face];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
PlayerActionPacket

Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Action：<!-- md:samp varint -->

- 类型：varint。enumeration: PlayerActionType

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Result Pos：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/NetworkBlockPosition.md)

- 类型：NetworkBlockPosition。

Face：<!-- md:samp varint -->

- 类型：varint。


///
