# <!-- md:samp MobEquipmentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MobEquipmentPacket -->数据包，数字ID是`31`。

## 结构

```viz
digraph MobEquipmentPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"MobEquipmentPacket\", typeName: \"\", id: 0, branchId: 31, recurseId: -1, attributes: 0, notes: \"\"",
		label=MobEquipmentPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Item];
	0 -> 3;
	5	[comment="name: \"Slot\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	0 -> 5;
	7	[comment="name: \"Selected Slot\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Selected Slot"];
	0 -> 7;
	9	[comment="name: \"Container ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
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
MobEquipmentPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。

Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 类型：NetworkItemStackDescriptor。

Slot：<!-- md:samp byte -->

- 类型：byte。

Selected Slot：<!-- md:samp byte -->

- 类型：byte。

Container ID：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerID


///
