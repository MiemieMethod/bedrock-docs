# <!-- md:samp ResourcePackDataInfoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackDataInfoPacket -->数据包，数字ID是`82`。

## 结构

```viz
digraph ResourcePackDataInfoPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		6	[comment="name: \"unsigned int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		8	[comment="name: \"unsigned int64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		14	[comment="name: \"byte\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"ResourcePackDataInfoPacket\", typeName: \"\", id: 0, branchId: 82, recurseId: -1, attributes: 0, notes: \"\"",
		label=ResourcePackDataInfoPacket];
	1	[comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Resource Name"];
	0 -> 1;
	3	[comment="name: \"Chunk Size\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chunk Size"];
	0 -> 3;
	5	[comment="name: \"Number of Chunks\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Number of Chunks"];
	0 -> 5;
	7	[comment="name: \"File Size\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="File Size"];
	0 -> 7;
	9	[comment="name: \"File Hash\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="File Hash"];
	0 -> 9;
	11	[comment="name: \"Is Premium Pack\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"Do you need an entitlement to \
use this pack?\"",
		label="Is Premium Pack"];
	0 -> 11;
	13	[comment="name: \"Pack Type\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PackType\"",
		label="Pack Type"];
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
ResourcePackDataInfoPacket

Resource Name：<!-- md:samp string -->

- 类型：string。

Chunk Size：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Number of Chunks：<!-- md:samp unsigned int -->

- 类型：unsigned int。

File Size：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

File Hash：<!-- md:samp string -->

- 类型：string。

Is Premium Pack：<!-- md:samp bool -->

- 类型：bool。Do you need an entitlement to use this pack?

Pack Type：<!-- md:samp byte -->

- 类型：byte。enumeration: PackType


///
