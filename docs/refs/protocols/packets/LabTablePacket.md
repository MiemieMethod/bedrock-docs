# <!-- md:samp LabTablePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LabTablePacket -->数据包，数字ID是`109`。

## 结构

```viz
digraph LabTablePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"BlockPos\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"LabTablePacket\", typeName: \"\", id: 0, branchId: 109, recurseId: -1, attributes: 0, notes: \"\"",
		label=LabTablePacket];
	1	[comment="name: \"Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LabTablePacket::Type\"",
		label=Type];
	0 -> 1;
	3	[comment="name: \"Position\", typeName: \"BlockPos\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 3;
	5	[comment="name: \"Reaction\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LabTableReactionType\"",
		label=Reaction];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
LabTablePacket

Type：<!-- md:samp byte -->

- 类型：byte。enumeration: LabTablePacket::Type

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/blockpos.md)

- 类型：BlockPos。

Reaction：<!-- md:samp byte -->

- 类型：byte。enumeration: LabTableReactionType


///
