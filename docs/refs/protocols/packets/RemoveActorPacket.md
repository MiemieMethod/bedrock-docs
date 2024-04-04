# <!-- md:samp RemoveActorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RemoveActorPacket -->数据包，数字ID是`14`。

## 结构

```dot
digraph RemoveActorPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"RemoveActorPacket\", typeName: \"\", id: 0, branchId: 14, recurseId: -1, attributes: 0, notes: \"\"",
		label=RemoveActorPacket];
	1	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
RemoveActorPacket

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。


///
