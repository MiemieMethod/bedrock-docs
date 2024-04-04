# <!-- md:samp ItemStackResponseSlotInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackResponseSlotInfo -->类型。

## 结构

```viz
digraph ItemStackResponseSlotInfo {
	graph [rankdir=LR];
	{
		graph [rank=max];
		28	[comment="name: \"byte\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		30	[comment="name: \"byte\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		32	[comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		37	[comment="name: \"TypedServerNetId<struct ItemStackNetIdTag,int,0>\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="TypedServerNetId<struct ItemStackNetIdTag,int,0>"];
		39	[comment="name: \"string\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		41	[comment="name: \"varint\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	26	[comment="name: \"ItemStackResponseSlotInfo\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemStackResponseSlotInfo];
	27	[comment="name: \"Requested slot\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Requested slot"];
	26 -> 27;
	29	[comment="name: \"Slot\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	26 -> 29;
	31	[comment="name: \"Amount\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Amount];
	26 -> 31;
	33	[comment="name: \"Item Stack Net Id\", typeName: \"TypedServerNetId<struct ItemStackNetIdTag,int,0>\", id: 33, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="Item Stack Net Id"];
	26 -> 33;
	38	[comment="name: \"Custom Name\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 0, notes: \"Allows you to filter for profanity \
on the server and return the updated name\"",
		label="Custom Name"];
	26 -> 38;
	40	[comment="name: \"Durability Correction\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Durability Correction"];
	26 -> 40;
	27 -> 28;
	29 -> 30;
	31 -> 32;
	33 -> 37;
	38 -> 39;
	40 -> 41;
}

```

## 字段

/// define
ItemStackResponseSlotInfo

Requested slot：<!-- md:samp byte -->

- 类型：byte。

Slot：<!-- md:samp byte -->

- 类型：byte。

Amount：<!-- md:samp byte -->

- 类型：byte。

Item Stack Net Id：[<!-- md:samp TypedServerNetId<struct ItemStackNetIdTag,int,0> -->](refs/protocols/types/TypedServerNetId<struct ItemStackNetIdTag,int,0>.md)

- 类型：TypedServerNetId<struct ItemStackNetIdTag,int,0>。

Custom Name：<!-- md:samp string -->

- 类型：string。Allows you to filter for profanity on the server and return the updated 'name'

Durability Correction：<!-- md:samp varint -->

- 类型：varint。


///
