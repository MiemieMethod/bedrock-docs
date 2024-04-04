# <!-- md:samp UnlockedRecipesPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UnlockedRecipesPacket -->数据包，数字ID是`199`。

## 结构

```dot
digraph UnlockedRecipesPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"UnlockedRecipesPacket\", typeName: \"\", id: 0, branchId: 199, recurseId: -1, attributes: 0, notes: \"\"",
		label=UnlockedRecipesPacket];
	1	[comment="name: \"Packet Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Packet Type"];
	0 -> 1;
	3	[comment="name: \"Unlocked Recipes List\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Unlocked Recipes List"];
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
	7	[comment="name: \"Recipe\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Recipe];
	6 -> 7;
	7 -> 8;
}

```

## 字段

/// define
UnlockedRecipesPacket

Packet Type：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Unlocked Recipes List

Unlocked Recipes List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Unlocked Recipes List的示例元素

Recipe：<!-- md:samp string -->

- 类型：string。


///
