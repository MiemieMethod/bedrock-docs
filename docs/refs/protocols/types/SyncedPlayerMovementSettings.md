# <!-- md:samp SyncedPlayerMovementSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SyncedPlayerMovementSettings -->类型。

## 结构

```dot
digraph SyncedPlayerMovementSettings {
	graph [rankdir=LR];
	{
		graph [rank=max];
		149	[comment="name: \"byte\", typeName: \"\", id: 149, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		151	[comment="name: \"varint\", typeName: \"\", id: 151, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		153	[comment="name: \"bool\", typeName: \"\", id: 153, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	147	[comment="name: \"SyncedPlayerMovementSettings\", typeName: \"\", id: 147, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SyncedPlayerMovementSettings];
	148	[comment="name: \"Authority Mode\", typeName: \"\", id: 148, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ServerAuthMovementMode\"",
		label="Authority Mode"];
	147 -> 148;
	150	[comment="name: \"Rewind History Size\", typeName: \"\", id: 150, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Rewind History Size"];
	147 -> 150;
	152	[comment="name: \"Server Authoratative Block Breaking\", typeName: \"\", id: 152, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Server Authoratative Block Breaking"];
	147 -> 152;
	148 -> 149;
	150 -> 151;
	152 -> 153;
}

```

## 字段

/// define
SyncedPlayerMovementSettings

Authority Mode：<!-- md:samp byte -->

- 类型：byte。enumeration: ServerAuthMovementMode

Rewind History Size：<!-- md:samp varint -->

- 类型：varint。

Server Authoratative Block Breaking：<!-- md:samp bool -->

- 类型：bool。


///
