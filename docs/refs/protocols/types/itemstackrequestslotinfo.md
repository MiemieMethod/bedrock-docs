# <!-- md:samp ItemStackRequestSlotInfo -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemStackRequestSlotInfo -->类型。

## 结构

```viz
digraph ItemStackRequestSlotInfo {
	graph [rankdir=LR];
	{
		graph [rank=max];
		97	[comment="name: \"byte\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		99	[comment="name: \"byte\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		101	[comment="name: \"varint\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	95	[comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemStackRequestSlotInfo];
	96	[comment="name: \"Open container net id\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerEnumName\"",
		label="Open container net id"];
	95 -> 96;
	98	[comment="name: \"Slot\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	95 -> 98;
	100	[comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw Id (32 bit signed)"];
	95 -> 100;
	96 -> 97;
	98 -> 99;
	100 -> 101;
}

```

## 字段

/// define
ItemStackRequestSlotInfo

Open container net id：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerEnumName

Slot：<!-- md:samp byte -->

- 类型：byte。

Raw Id (32 bit signed)：<!-- md:samp varint -->

- 类型：varint。


///
