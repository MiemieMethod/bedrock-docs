# <!-- md:samp NetworkChunkPublisherUpdatePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkChunkPublisherUpdatePacket -->数据包，数字ID是`121`。

## 结构

```viz
digraph NetworkChunkPublisherUpdatePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"BlockPos\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=BlockPos];
		4	[comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"unsigned int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		9	[comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"ChunkPos\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ChunkPos];
	}
	0	[comment="name: \"NetworkChunkPublisherUpdatePacket\", typeName: \"\", id: 0, branchId: 121, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkChunkPublisherUpdatePacket];
	1	[comment="name: \"New position for view\", typeName: \"BlockPos\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="New position for view"];
	0 -> 1;
	3	[comment="name: \"New radius for view\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="New radius for view"];
	0 -> 3;
	5	[comment="name: \"Server Built Chunks Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Server Built Chunks Size"];
	0 -> 5;
	7	[comment="name: \"Server Built Chunks List\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Server Built Chunks List"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	8	[comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	7 -> 8;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	7 -> 10;
	8 -> 9;
	11	[comment="name: \"Chunk Pos\", typeName: \"ChunkPos\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Chunk Pos"];
	10 -> 11;
	11 -> 12;
}

```

## 字段

/// define
NetworkChunkPublisherUpdatePacket

New position for view：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 类型：BlockPos。

New radius for view：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Server Built Chunks Size：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Server Built Chunks List

//// define
Server Built Chunks List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Server Built Chunks List的示例元素

Chunk Pos：[<!-- md:samp ChunkPos -->](../types/chunkpos.md)

- 类型：ChunkPos。


////



///
