# <!-- md:samp TakeItemActorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp TakeItemActorPacket -->数据包，数字ID是`17`。

## 结构

```viz
digraph TakeItemActorPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
	}
	0	[comment="name: \"TakeItemActorPacket\", typeName: \"\", id: 0, branchId: 17, recurseId: -1, attributes: 0, notes: \"\"",
		label=TakeItemActorPacket];
	1	[comment="name: \"Item Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Item Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Actor Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Runtime ID"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
TakeItemActorPacket

Item Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Actor Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。


///
