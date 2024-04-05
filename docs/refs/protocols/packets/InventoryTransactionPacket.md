# <!-- md:samp InventoryTransactionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryTransactionPacket -->数据包，数字ID是`30`。

## 结构

```viz
digraph InventoryTransactionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		5	[comment="name: \"[No Data]\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		9	[comment="name: \"unsigned varint\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		12	[comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		15	[comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		18	[comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		20	[comment="name: \"unsigned varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		52	[comment="name: \"InventoryTransaction\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=InventoryTransaction];
	}
	0	[comment="name: \"InventoryTransactionPacket\", typeName: \"\", id: 0, branchId: 30, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventoryTransactionPacket];
	1	[comment="name: \"Raw Id (32 bit signed)\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Raw Id (32 bit signed)"];
	0 -> 1;
	3	[comment="name: \"Dependency on 'above ID (the legacy request ID) nonzero'\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 2, \
notes: \"\"",
		label="Dependency on 'above ID (the legacy request ID) nonzero'",
		shape=note];
	0 -> 3;
	19	[comment="name: \"Transaction Type\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ComplexInventoryTransaction::\
Type\"",
		label="Transaction Type"];
	0 -> 19;
	21	[comment="name: \"mTransaction->mTransaction\", typeName: \"InventoryTransaction\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\
Our ComplexInventoryTransaction contains an InventoryTransaction within it\"",
		label="mTransaction->mTransaction"];
	0 -> 21;
	1 -> 2;
	4	[comment="name: \"if (0)\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	3 -> 4;
	6	[comment="name: \"if (1)\", typeName: \"\", id: 6, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Legacy Set Item Slots\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 8, notes: \"Only matters when ItemStackNetManager \
is enabled\"",
		label="Legacy Set Item Slots"];
	6 -> 7;
	8	[comment="name: \"Array Size\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	7 -> 8;
	10	[comment="name: \"example element\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	7 -> 10;
	8 -> 9;
	11	[comment="name: \"Container Enum\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Container Enum"];
	10 -> 11;
	13	[comment="name: \"Slot vector\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Slot vector"];
	10 -> 13;
	11 -> 12;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	13 -> 14;
	16	[comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	13 -> 16;
	14 -> 15;
	17	[comment="name: \"Slot\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	16 -> 17;
	17 -> 18;
	19 -> 20;
	21 -> 52;
}

```

## 字段

/// define
InventoryTransactionPacket

Raw Id (32 bit signed)：<!-- md:samp varint -->

- 类型：varint。

Dependency on 'above ID (the legacy request ID) nonzero'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Legacy Set Item Slots

Legacy Set Item Slots数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Legacy Set Item Slots的示例元素

Container Enum：<!-- md:samp byte -->

- 类型：byte。

Slot vector

Slot vector数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Slot vector的示例元素

Slot：<!-- md:samp byte -->

- 类型：byte。


/////

////


Transaction Type：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ComplexInventoryTransaction::Type

mTransaction->mTransaction：[<!-- md:samp InventoryTransaction -->](refs/protocols/types/inventorytransaction.md)

- 类型：InventoryTransaction。Our ComplexInventoryTransaction contains an InventoryTransaction within it


///
