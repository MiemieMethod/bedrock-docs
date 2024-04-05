# <!-- md:samp ChunkRadiusUpdatedPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ChunkRadiusUpdatedPacket -->数据包，数字ID是`70`。

## 结构

```viz
digraph ChunkRadiusUpdatedPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"ChunkRadiusUpdatedPacket\", typeName: \"\", id: 0, branchId: 70, recurseId: -1, attributes: 0, notes: \"\"",
		label=ChunkRadiusUpdatedPacket];
	1	[comment="name: \"Chunk Radius\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chunk Radius"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
ChunkRadiusUpdatedPacket

Chunk Radius：<!-- md:samp varint -->

- 类型：varint。


///
