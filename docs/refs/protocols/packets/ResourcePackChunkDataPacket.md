# <!-- md:samp ResourcePackChunkDataPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackChunkDataPacket -->数据包，数字ID是`83`。

## 结构

```dot
digraph ResourcePackChunkDataPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
		6	[comment="name: \"unsigned int64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"ResourcePackChunkDataPacket\", typeName: \"\", id: 0, branchId: 83, recurseId: -1, attributes: 0, notes: \"\"",
		label=ResourcePackChunkDataPacket];
	1	[comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Resource Name"];
	0 -> 1;
	3	[comment="name: \"Chunk ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chunk ID"];
	0 -> 3;
	5	[comment="name: \"Byte Offset\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Byte Offset"];
	0 -> 5;
	7	[comment="name: \"Chunk Data\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Chunk Data"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
ResourcePackChunkDataPacket

Resource Name：<!-- md:samp string -->

- 类型：string。

Chunk ID：<!-- md:samp unsigned int -->

- 类型：unsigned int。

Byte Offset：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Chunk Data：<!-- md:samp string -->

- 类型：string。


///
