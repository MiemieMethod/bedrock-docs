# <!-- md:samp UpdateSoftEnumPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateSoftEnumPacket -->数据包，数字ID是`114`。

## 结构

```viz
digraph UpdateSoftEnumPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"unsigned int\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
	}
	0	[comment="name: \"UpdateSoftEnumPacket\", typeName: \"\", id: 0, branchId: 114, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateSoftEnumPacket];
	1	[comment="name: \"Enum Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Name"];
	0 -> 1;
	3	[comment="name: \"Values\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Values];
	0 -> 3;
	9	[comment="name: \"Update Type\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SoftEnumUpdateType\"",
		label="Update Type"];
	0 -> 9;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Enum Value\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enum Value"];
	6 -> 7;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
UpdateSoftEnumPacket

Enum Name：<!-- md:samp string -->

- 类型：string。

Values

//// define
Values数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Values的示例元素

Enum Value：<!-- md:samp string -->

- 类型：string。


////


Update Type：<!-- md:samp unsigned int -->

- 类型：unsigned int。enumeration: SoftEnumUpdateType


///
