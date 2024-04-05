# <!-- md:samp UpdateBlockPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateBlockPacket -->数据包，数字ID是`21`。

## 结构

```viz
digraph UpdateBlockPacket {
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
	}
	0	[comment="name: \"UpdateBlockPacket\", typeName: \"\", id: 0, branchId: 21, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateBlockPacket];
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
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
UpdateBlockPacket

Block Position：[<!-- md:samp NetworkBlockPosition -->](refs/protocols/types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Block Runtime ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Flags：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Layer：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///
