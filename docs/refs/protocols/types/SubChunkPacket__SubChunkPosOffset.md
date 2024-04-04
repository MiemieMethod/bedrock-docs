# <!-- md:samp SubChunkPacket::SubChunkPosOffset -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubChunkPacket::SubChunkPosOffset -->类型。

## 结构

```dot
digraph "SubChunkPacket::SubChunkPosOffset" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		21	[comment="name: \"byte\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		23	[comment="name: \"byte\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		25	[comment="name: \"byte\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	19	[comment="name: \"SubChunkPacket::SubChunkPosOffset\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="SubChunkPacket::SubChunkPosOffset"];
	20	[comment="name: \"Offset X\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Offset X"];
	19 -> 20;
	22	[comment="name: \"Offset Y\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Offset Y"];
	19 -> 22;
	24	[comment="name: \"Offset Z\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Offset Z"];
	19 -> 24;
	20 -> 21;
	22 -> 23;
	24 -> 25;
}

```

## 字段

/// define
SubChunkPacket::SubChunkPosOffset

Offset X：<!-- md:samp byte -->

- 类型：byte。

Offset Y：<!-- md:samp byte -->

- 类型：byte。

Offset Z：<!-- md:samp byte -->

- 类型：byte。


///
