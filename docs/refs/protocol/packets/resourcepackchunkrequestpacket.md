# <!-- md:samp ResourcePackChunkRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ResourcePackChunkRequestPacket -->数据包，数字ID是`84`。

## 结构

```viz
digraph ResourcePackChunkRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"unsigned int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
	}
	0	[comment="name: \"ResourcePackChunkRequestPacket\", typeName: \"\", id: 0, branchId: 84, recurseId: -1, attributes: 0, notes: \"\"",
		label=ResourcePackChunkRequestPacket];
	1	[comment="name: \"Resource Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Resource Name"];
	0 -> 1;
	3	[comment="name: \"Chunk\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Chunk];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ResourcePackChunkRequestPacket

Resource Name：<!-- md:samp string -->

- 类型：string。

Chunk：<!-- md:samp unsigned int -->

- 类型：unsigned int。


///
