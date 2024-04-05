# <!-- md:samp DeathInfoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DeathInfoPacket -->数据包，数字ID是`189`。

## 结构

```viz
digraph DeathInfoPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"DeathInfoPacket\", typeName: \"\", id: 0, branchId: 189, recurseId: -1, attributes: 0, notes: \"\"",
		label=DeathInfoPacket];
	1	[comment="name: \"Death Cause Attack Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Death Cause Attack Name"];
	0 -> 1;
	3	[comment="name: \"Death Cause Message List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Death Cause Message List"];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Death Cause Entity Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Death Cause Entity Name"];
	6 -> 7;
	9	[comment="name: \"Death Cause Entity Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Death Cause Entity Name"];
	6 -> 9;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
DeathInfoPacket

Death Cause Attack Name：<!-- md:samp string -->

- 类型：string。

Death Cause Message List

//// define
Death Cause Message List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Death Cause Message List的示例元素

Death Cause Entity Name：<!-- md:samp string -->

- 类型：string。


////



///
