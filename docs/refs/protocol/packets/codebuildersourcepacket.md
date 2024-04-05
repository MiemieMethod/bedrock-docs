# <!-- md:samp CodeBuilderSourcePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CodeBuilderSourcePacket -->数据包，数字ID是`178`。

## 结构

```viz
digraph CodeBuilderSourcePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"CodeBuilderSourcePacket\", typeName: \"\", id: 0, branchId: 178, recurseId: -1, attributes: 0, notes: \"\"",
		label=CodeBuilderSourcePacket];
	1	[comment="name: \"Operation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CodeBuilderStorageQueryOptions::\
Operation\"",
		label=Operation];
	0 -> 1;
	3	[comment="name: \"Category\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CodeBuilderStorageQueryOptions::\
Category\"",
		label=Category];
	0 -> 3;
	5	[comment="name: \"Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Value];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
CodeBuilderSourcePacket

Operation：<!-- md:samp byte -->

- 类型：byte。enumeration: CodeBuilderStorageQueryOptions::Operation

Category：<!-- md:samp byte -->

- 类型：byte。enumeration: CodeBuilderStorageQueryOptions::Category

Value：<!-- md:samp string -->

- 类型：string。


///
