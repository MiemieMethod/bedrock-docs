# <!-- md:samp InventoryContentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryContentPacket -->数据包，数字ID是`49`。

## 结构

```viz
digraph InventoryContentPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
	}
	0	[comment="name: \"InventoryContentPacket\", typeName: \"\", id: 0, branchId: 49, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventoryContentPacket];
	1	[comment="name: \"Inventory Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Inventory Id"];
	0 -> 1;
	3	[comment="name: \"Slots\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Slots];
	0 -> 3;
	1 -> 2;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Item stack\", typeName: \"NetworkItemStackDescriptor\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Item stack"];
	6 -> 7;
	7 -> 8;
}

```

## 字段

/// define
InventoryContentPacket

Inventory Id：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Slots

Slots数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Slots的示例元素

Item stack：[<!-- md:samp NetworkItemStackDescriptor -->](refs/protocols/types/networkitemstackdescriptor.md)

- 类型：NetworkItemStackDescriptor。


///
