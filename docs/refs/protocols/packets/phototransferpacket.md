# <!-- md:samp PhotoTransferPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PhotoTransferPacket -->数据包，数字ID是`99`。

## 结构

```viz
digraph PhotoTransferPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		12	[comment="name: \"int64\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int64];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"PhotoTransferPacket\", typeName: \"\", id: 0, branchId: 99, recurseId: -1, attributes: 0, notes: \"\"",
		label=PhotoTransferPacket];
	1	[comment="name: \"Photo Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Photo Name"];
	0 -> 1;
	3	[comment="name: \"Photo Data\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Photo Data"];
	0 -> 3;
	5	[comment="name: \"Book ID\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Book ID"];
	0 -> 5;
	7	[comment="name: \"Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PhotoType\"",
		label=Type];
	0 -> 7;
	9	[comment="name: \"Source Type\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PhotoType\"",
		label="Source Type"];
	0 -> 9;
	11	[comment="name: \"Owner ID\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Owner ID"];
	0 -> 11;
	13	[comment="name: \"New Photo Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="New Photo Name"];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
PhotoTransferPacket

Photo Name：<!-- md:samp string -->

- 类型：string。

Photo Data：<!-- md:samp string -->

- 类型：string。

Book ID：<!-- md:samp string -->

- 类型：string。

Type：<!-- md:samp byte -->

- 类型：byte。enumeration: PhotoType

Source Type：<!-- md:samp byte -->

- 类型：byte。enumeration: PhotoType

Owner ID：<!-- md:samp int64 -->

- 类型：int64。

New Photo Name：<!-- md:samp string -->

- 类型：string。


///
