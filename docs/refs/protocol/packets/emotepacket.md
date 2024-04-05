# <!-- md:samp EmotePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EmotePacket -->数据包，数字ID是`138`。

## 结构

```viz
digraph EmotePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"EmotePacket\", typeName: \"\", id: 0, branchId: 138, recurseId: -1, attributes: 0, notes: \"\"",
		label=EmotePacket];
	1	[comment="name: \"Actor Runtime Id\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Runtime Id"];
	0 -> 1;
	3	[comment="name: \"Emote Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Emote Id"];
	0 -> 3;
	5	[comment="name: \"Xuid\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Xuid];
	0 -> 5;
	7	[comment="name: \"PlatformId\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlatformId];
	0 -> 7;
	9	[comment="name: \"Flags\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: EmotePacket::Flags\"",
		label=Flags];
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
EmotePacket

Actor Runtime Id：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Emote Id：<!-- md:samp string -->

- 类型：string。

Xuid：<!-- md:samp string -->

- 类型：string。

PlatformId：<!-- md:samp string -->

- 类型：string。

Flags：<!-- md:samp byte -->

- 类型：byte。enumeration: EmotePacket::Flags


///
