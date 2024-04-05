# <!-- md:samp InventorySlotPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventorySlotPacket -->数据包，数字ID是`50`。

## 结构

```viz
digraph InventorySlotPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		4	[comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
	}
	0	[comment="name: \"InventorySlotPacket\", typeName: \"\", id: 0, branchId: 50, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventorySlotPacket];
	1	[comment="name: \"Container ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerID\"",
		label="Container ID"];
	0 -> 1;
	3	[comment="name: \"Slot\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	0 -> 3;
	5	[comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Item];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
InventorySlotPacket

Container ID：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ContainerID

Slot：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Item：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/networkitemstackdescriptor.md)

- 类型：NetworkItemStackDescriptor。


///
