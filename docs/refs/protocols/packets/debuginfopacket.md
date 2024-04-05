# <!-- md:samp DebugInfoPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DebugInfoPacket -->数据包，数字ID是`155`。

## 结构

```viz
digraph DebugInfoPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"DebugInfoPacket\", typeName: \"\", id: 0, branchId: 155, recurseId: -1, attributes: 0, notes: \"\"",
		label=DebugInfoPacket];
	1	[comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Id"];
	0 -> 1;
	3	[comment="name: \"Data\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
DebugInfoPacket

Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。

Data：<!-- md:samp string -->

- 类型：string。


///
