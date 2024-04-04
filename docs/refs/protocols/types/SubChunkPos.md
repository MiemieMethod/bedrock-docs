# <!-- md:samp SubChunkPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SubChunkPos -->类型。

## 结构

```dot
digraph SubChunkPos {
	graph [rankdir=LR];
	{
		graph [rank=max];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	6	[comment="name: \"SubChunkPos\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SubChunkPos];
	7	[comment="name: \"X\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	6 -> 7;
	9	[comment="name: \"Y\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Y];
	6 -> 9;
	11	[comment="name: \"Z\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Z];
	6 -> 11;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
SubChunkPos

X：<!-- md:samp varint -->

- 类型：varint。

Y：<!-- md:samp varint -->

- 类型：varint。

Z：<!-- md:samp varint -->

- 类型：varint。


///
