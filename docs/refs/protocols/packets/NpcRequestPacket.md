# <!-- md:samp NpcRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NpcRequestPacket -->数据包，数字ID是`98`。

## 结构

```dot
digraph NpcRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"NpcRequestPacket\", typeName: \"\", id: 0, branchId: 98, recurseId: -1, attributes: 0, notes: \"\"",
		label=NpcRequestPacket];
	1	[comment="name: \"NPC Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="NPC Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Request Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: NpcRequestPacket::RequestType\"",
		label="Request Type"];
	0 -> 3;
	5	[comment="name: \"Actions\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Actions];
	0 -> 5;
	7	[comment="name: \"Action Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Action Index"];
	0 -> 7;
	9	[comment="name: \"Scene Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Scene Name"];
	0 -> 9;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
}

```

## 字段

/// define
NpcRequestPacket

NPC Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Request Type：<!-- md:samp byte -->

- 类型：byte。enumeration: NpcRequestPacket::RequestType

Actions：<!-- md:samp string -->

- 类型：string。

Action Index：<!-- md:samp byte -->

- 类型：byte。

Scene Name：<!-- md:samp string -->

- 类型：string。


///
