# <!-- md:samp InventoryAction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryAction -->类型。

## 结构

```viz
digraph InventoryAction {
	graph [rankdir=LR];
	{
		graph [rank=max];
		44	[comment="name: \"InventorySource\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=InventorySource];
		46	[comment="name: \"unsigned varint\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		48	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		50	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
	}
	28	[comment="name: \"InventoryAction\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventoryAction];
	29	[comment="name: \"Source\", typeName: \"InventorySource\", id: 29, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Source];
	28 -> 29;
	45	[comment="name: \"Slot\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	28 -> 45;
	47	[comment="name: \"From Item Descriptor\", typeName: \"NetworkItemStackDescriptor\", id: 47, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="From Item Descriptor"];
	28 -> 47;
	49	[comment="name: \"To Item Descriptor\", typeName: \"NetworkItemStackDescriptor\", id: 49, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="To Item Descriptor"];
	28 -> 49;
	29 -> 44;
	45 -> 46;
	47 -> 48;
	49 -> 50;
}

```

## 字段

/// define
InventoryAction

Source：[<!-- md:samp InventorySource -->](refs/protocols/types/InventorySource.md)

- 类型：InventorySource。

Slot：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

From Item Descriptor：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。

To Item Descriptor：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/NetworkItemStackDescriptor.md)

- 类型：NetworkItemStackDescriptor。


///
