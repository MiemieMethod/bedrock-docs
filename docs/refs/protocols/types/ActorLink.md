# <!-- md:samp ActorLink -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorLink -->类型。

## 结构

```viz
digraph ActorLink {
	graph [rankdir=LR];
	{
		graph [rank=max];
		112	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		114	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		116	[comment="name: \"byte\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		118	[comment="name: \"bool\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		120	[comment="name: \"bool\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	110	[comment="name: \"ActorLink\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ActorLink];
	111	[comment="name: \"Actor Unique ID - A\", typeName: \"ActorUniqueID\", id: 111, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Unique ID - A"];
	110 -> 111;
	113	[comment="name: \"Actor Unique ID - B\", typeName: \"ActorUniqueID\", id: 113, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Actor Unique ID - B"];
	110 -> 113;
	115	[comment="name: \"Link Type\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorLinkType\"",
		label="Link Type"];
	110 -> 115;
	117	[comment="name: \"Immediate\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Immediate];
	110 -> 117;
	119	[comment="name: \"Passenger Initiated\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether the link was changed \
by the passenger\"",
		label="Passenger Initiated"];
	110 -> 119;
	111 -> 112;
	113 -> 114;
	115 -> 116;
	117 -> 118;
	119 -> 120;
}

```

## 字段

/// define
ActorLink

Actor Unique ID - A：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Actor Unique ID - B：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Link Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ActorLinkType

Immediate：<!-- md:samp bool -->

- 类型：bool。

Passenger Initiated：<!-- md:samp bool -->

- 类型：bool。Whether the link was changed by the passenger


///
