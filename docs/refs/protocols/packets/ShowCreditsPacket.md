# <!-- md:samp ShowCreditsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ShowCreditsPacket -->数据包，数字ID是`75`。

## 结构

```viz
digraph ShowCreditsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"ShowCreditsPacket\", typeName: \"\", id: 0, branchId: 75, recurseId: -1, attributes: 0, notes: \"\"",
		label=ShowCreditsPacket];
	1	[comment="name: \"Player Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Credits State\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ShowCreditsPacket::CreditsState\"",
		label="Credits State"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
ShowCreditsPacket

Player Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Credits State：<!-- md:samp varint -->

- 类型：varint。enumeration: ShowCreditsPacket::CreditsState


///
