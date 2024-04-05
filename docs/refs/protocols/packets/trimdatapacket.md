# <!-- md:samp TrimDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TrimDataPacket -->数据包，数字ID是`302`。

## 结构

```viz
digraph TrimDataPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		11	[comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		18	[comment="name: \"string\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"TrimDataPacket\", typeName: \"\", id: 0, branchId: 302, recurseId: -1, attributes: 0, notes: \"\"",
		label=TrimDataPacket];
	1	[comment="name: \"TrimPattern List\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="TrimPattern List"];
	0 -> 1;
	9	[comment="name: \"TrimMaterial List\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="TrimMaterial List"];
	0 -> 9;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Item Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Name"];
	4 -> 5;
	7	[comment="name: \"Pattern Id\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Pattern Id"];
	4 -> 7;
	5 -> 6;
	7 -> 8;
	10	[comment="name: \"Array Size\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	9 -> 10;
	12	[comment="name: \"example element\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	9 -> 12;
	10 -> 11;
	13	[comment="name: \"Material Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Material Id"];
	12 -> 13;
	15	[comment="name: \"Color\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Color];
	12 -> 15;
	17	[comment="name: \"Item Name\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Name"];
	12 -> 17;
	13 -> 14;
	15 -> 16;
	17 -> 18;
}

```

## 字段

/// define
TrimDataPacket

TrimPattern List

TrimPattern List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

TrimPattern List的示例元素

Item Name：<!-- md:samp string -->

- 类型：string。

Pattern Id：<!-- md:samp string -->

- 类型：string。

TrimMaterial List

TrimMaterial List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

TrimMaterial List的示例元素

Material Id：<!-- md:samp string -->

- 类型：string。

Color：<!-- md:samp string -->

- 类型：string。


///
