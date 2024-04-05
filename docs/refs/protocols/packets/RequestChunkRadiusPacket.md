# <!-- md:samp RequestChunkRadiusPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RequestChunkRadiusPacket -->数据包，数字ID是`69`。

## 结构

```viz
digraph RequestChunkRadiusPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"RequestChunkRadiusPacket\", typeName: \"\", id: 0, branchId: 69, recurseId: -1, attributes: 0, notes: \"\"",
		label=RequestChunkRadiusPacket];
	1	[comment="name: \"Chunk Radius\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chunk Radius"];
	0 -> 1;
	3	[comment="name: \"Max ChunkRadius\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Max ChunkRadius"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
RequestChunkRadiusPacket

Chunk Radius：<!-- md:samp varint -->

- 类型：varint。

Max ChunkRadius：<!-- md:samp byte -->

- 类型：byte。


///
