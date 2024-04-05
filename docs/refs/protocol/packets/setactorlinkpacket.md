# <!-- md:samp SetActorLinkPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetActorLinkPacket -->数据包，数字ID是`41`。

## 结构

```viz
digraph SetActorLinkPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorLink\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorLink];
	}
	0	[comment="name: \"SetActorLinkPacket\", typeName: \"\", id: 0, branchId: 41, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetActorLinkPacket];
	1	[comment="name: \"Link\", typeName: \"ActorLink\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Link];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
SetActorLinkPacket

Link：[<!-- md:samp ActorLink -->](refs/protocols/types/actorlink.md)

- 类型：ActorLink。


///
