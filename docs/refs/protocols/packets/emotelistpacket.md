# <!-- md:samp EmoteListPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EmoteListPacket -->数据包，数字ID是`152`。

## 结构

```viz
digraph EmoteListPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"mce::UUID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="mce::UUID"];
	}
	0	[comment="name: \"EmoteListPacket\", typeName: \"\", id: 0, branchId: 152, recurseId: -1, attributes: 0, notes: \"\"",
		label=EmoteListPacket];
	1	[comment="name: \"Runtime id\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Runtime id"];
	0 -> 1;
	3	[comment="name: \"Emote piece ids\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Emote piece ids"];
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
	7	[comment="name: \"Piece id\", typeName: \"mce::UUID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Piece id"];
	6 -> 7;
	7 -> 8;
}

```

## 字段

/// define
EmoteListPacket

Runtime id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Emote piece ids

//// define
Emote piece ids数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Emote piece ids的示例元素

Piece id：[<!-- md:samp mce::UUID -->](../types/mce::uuid.md)

- 类型：mce::UUID。


////



///
