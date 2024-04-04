# <!-- md:samp MobArmorEquipmentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MobArmorEquipmentPacket -->数据包，数字ID是`32`。

## 结构

```dot
digraph MobArmorEquipmentPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		6	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		8	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		10	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
	}
	0	[comment="name: \"MobArmorEquipmentPacket\", typeName: \"\", id: 0, branchId: 32, recurseId: -1, attributes: 0, notes: \"\"",
		label=MobArmorEquipmentPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Head\", typeName: \"NetworkItemStackDescriptor\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Head];
	0 -> 3;
	5	[comment="name: \"Torso\", typeName: \"NetworkItemStackDescriptor\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Torso];
	0 -> 5;
	7	[comment="name: \"Legs\", typeName: \"NetworkItemStackDescriptor\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Legs];
	0 -> 7;
	9	[comment="name: \"Feet\", typeName: \"NetworkItemStackDescriptor\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Feet];
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
MobArmorEquipmentPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Head：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。

Torso：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。

Legs：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。

Feet：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。


///
