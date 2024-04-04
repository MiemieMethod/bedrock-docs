# <!-- md:samp ActorEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorEventPacket -->数据包，数字ID是`27`。

## 结构

```dot
digraph ActorEventPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"ActorEventPacket\", typeName: \"\", id: 0, branchId: 27, recurseId: -1, attributes: 0, notes: \"\"",
		label=ActorEventPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorEvent\"",
		label="Event ID"];
	0 -> 3;
	5	[comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Data];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
ActorEventPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Event ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ActorEvent

Data：<!-- md:samp varint -->

- 类型：varint。


///
