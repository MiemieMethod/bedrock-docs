# <!-- md:samp PropertySyncData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PropertySyncData -->类型。

## 结构

```viz
digraph PropertySyncData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		64	[comment="name: \"unsigned varint\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		67	[comment="name: \"unsigned varint\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		69	[comment="name: \"varint\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		72	[comment="name: \"unsigned varint\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		75	[comment="name: \"unsigned varint\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		77	[comment="name: \"float\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
	}
	61	[comment="name: \"PropertySyncData\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PropertySyncData];
	62	[comment="name: \"Int Entries List\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Int Entries List"];
	61 -> 62;
	70	[comment="name: \"Float Entries List\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Float Entries List"];
	61 -> 70;
	63	[comment="name: \"Array Size\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	62 -> 63;
	65	[comment="name: \"example element\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	62 -> 65;
	63 -> 64;
	66	[comment="name: \"Property Index\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Property Index"];
	65 -> 66;
	68	[comment="name: \"Data\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	65 -> 68;
	66 -> 67;
	68 -> 69;
	71	[comment="name: \"Array Size\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	70 -> 71;
	73	[comment="name: \"example element\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	70 -> 73;
	71 -> 72;
	74	[comment="name: \"Property Index\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Property Index"];
	73 -> 74;
	76	[comment="name: \"Data\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	73 -> 76;
	74 -> 75;
	76 -> 77;
}

```

## 字段

/// define
PropertySyncData

Int Entries List

Int Entries List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Int Entries List的示例元素

Property Index：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Data：<!-- md:samp varint -->

- 类型：varint。

Float Entries List

Float Entries List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Float Entries List的示例元素

Data：<!-- md:samp float -->

- 类型：float。


///
