# <!-- md:samp BlockPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BlockPos -->类型。

## 结构

```dot
digraph BlockPos {
	graph [rankdir=LR];
	{
		graph [rank=max];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		14	[comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	8	[comment="name: \"BlockPos\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=BlockPos];
	9	[comment="name: \"X\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	8 -> 9;
	11	[comment="name: \"Y\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Y];
	8 -> 11;
	13	[comment="name: \"Z\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Z];
	8 -> 13;
	9 -> 10;
	11 -> 12;
	13 -> 14;
}

```

## 字段

/// define
BlockPos

X：<!-- md:samp varint -->

- 类型：varint。

Y：<!-- md:samp varint -->

- 类型：varint。

Z：<!-- md:samp varint -->

- 类型：varint。


///
