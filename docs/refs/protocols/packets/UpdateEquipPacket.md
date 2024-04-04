# <!-- md:samp UpdateEquipPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateEquipPacket -->数据包，数字ID是`81`。

## 结构

```dot
digraph UpdateEquipPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		10	[comment="name: \"CompoundTag\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"UpdateEquipPacket\", typeName: \"\", id: 0, branchId: 81, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateEquipPacket];
	1	[comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 1;
	3	[comment="name: \"Container Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerType\"",
		label="Container Type"];
	0 -> 3;
	5	[comment="name: \"Size\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Size];
	0 -> 5;
	7	[comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Actor ID"];
	0 -> 7;
	9	[comment="name: \"Data Tags\", typeName: \"CompoundTag\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Data Tags"];
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
UpdateEquipPacket

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID

Container Type：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerType

Size：<!-- md:samp varint -->

- 类型：varint。

Target Actor ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/ActorUniqueID.md)

- 类型：ActorUniqueID。

Data Tags：[<!-- md:samp CompoundTag -->](refs/protocols/types/CompoundTag.md)

- 类型：CompoundTag。


///
