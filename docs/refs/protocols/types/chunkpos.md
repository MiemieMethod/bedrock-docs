# <!-- md:samp ChunkPos -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChunkPos -->类型。

## 结构

```viz
digraph ChunkPos {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	2	[comment="name: \"ChunkPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ChunkPos];
	3	[comment="name: \"X\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=X];
	2 -> 3;
	5	[comment="name: \"Z\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Z];
	2 -> 5;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
ChunkPos

X：<!-- md:samp varint -->

- 类型：varint。

Z：<!-- md:samp varint -->

- 类型：varint。


///
