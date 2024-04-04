# <!-- md:samp BlockPickRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockPickRequestPacket -->数据包，数字ID是`34`。

## 结构

```dot
digraph BlockPickRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"BlockPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"BlockPickRequestPacket\", typeName: \"\", id: 0, branchId: 34, recurseId: -1, attributes: 0, notes: \"\"",
		label=BlockPickRequestPacket];
	1	[comment="name: \"Position\", typeName: \"BlockPos\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 1;
	3	[comment="name: \"With Data?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="With Data?"];
	0 -> 3;
	5	[comment="name: \"Max Slots\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Max Slots"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
BlockPickRequestPacket

Position：[<!-- md:samp BlockPos -->](refs/protocols/types/BlockPos.md)

- 类型：BlockPos。

With Data?：<!-- md:samp bool -->

- 类型：bool。

Max Slots：<!-- md:samp byte -->

- 类型：byte。


///
