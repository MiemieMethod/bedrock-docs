# <!-- md:samp UpdateTradePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateTradePacket -->数据包，数字ID是`80`。

## 结构

```viz
digraph UpdateTradePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		12	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		14	[comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		16	[comment="name: \"bool\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		18	[comment="name: \"bool\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		20	[comment="name: \"CompoundTag\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"UpdateTradePacket\", typeName: \"\", id: 0, branchId: 80, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateTradePacket];
	1	[comment="name: \"Container Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container Id"];
	0 -> 1;
	3	[comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerType\"",
		label="Container Type"];
	0 -> 3;
	5	[comment="name: \"Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Size];
	0 -> 5;
	7	[comment="name: \"Trade Tier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Trade Tier"];
	0 -> 7;
	9	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 9;
	11	[comment="name: \"Last Trading Player ID\", typeName: \"ActorUniqueID\", id: 11, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Last Trading Player ID"];
	0 -> 11;
	13	[comment="name: \"Display Name\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Display Name"];
	0 -> 13;
	15	[comment="name: \"Use New Trade UI\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Use New Trade UI"];
	0 -> 15;
	17	[comment="name: \"Using Economy Trade\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"When set to false, it means \
the packet comes from the old Trade Component.\"",
		label="Using Economy Trade"];
	0 -> 17;
	19	[comment="name: \"Data Tags\", typeName: \"CompoundTag\", id: 19, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Data Tags"];
	0 -> 19;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	19 -> 20;
}

```

## 字段

/// define
UpdateTradePacket

Container Id：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

Container Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerType

Size：<!-- md:samp varint -->

- 类型：varint。

Trade Tier：<!-- md:samp varint -->

- 类型：varint。

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Last Trading Player ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Display Name：<!-- md:samp string -->

- 类型：string。

Use New Trade UI：<!-- md:samp bool -->

- 类型：bool。

Using Economy Trade：<!-- md:samp bool -->

- 类型：bool。When set to false, it means the packet comes from the old Trade Component.

Data Tags：[<!-- md:samp CompoundTag -->](refs/protocols/types/CompoundTag.md)

- 类型：CompoundTag。


///
