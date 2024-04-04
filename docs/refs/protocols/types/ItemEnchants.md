# <!-- md:samp ItemEnchants -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ItemEnchants -->类型。

## 结构

```dot
digraph ItemEnchants {
	graph [rankdir=LR];
	{
		graph [rank=max];
		10	[comment="name: \"int\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		13	[comment="name: \"unsigned varint\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		16	[comment="name: \"byte\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		18	[comment="name: \"byte\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		21	[comment="name: \"unsigned varint\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		24	[comment="name: \"byte\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		26	[comment="name: \"byte\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		29	[comment="name: \"unsigned varint\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		32	[comment="name: \"byte\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		34	[comment="name: \"byte\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	8	[comment="name: \"ItemEnchants\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=ItemEnchants];
	9	[comment="name: \"Slot\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	8 -> 9;
	11	[comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Item Enchants For Given Activation"];
	8 -> 11;
	19	[comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Item Enchants For Given Activation"];
	8 -> 19;
	27	[comment="name: \"Item Enchants For Given Activation\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Item Enchants For Given Activation"];
	8 -> 27;
	9 -> 10;
	12	[comment="name: \"Array Size\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	11 -> 12;
	14	[comment="name: \"example element\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	11 -> 14;
	12 -> 13;
	15	[comment="name: \"Enchant Type\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\"",
		label="Enchant Type"];
	14 -> 15;
	17	[comment="name: \"Enchant Level\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enchant Level"];
	14 -> 17;
	15 -> 16;
	17 -> 18;
	20	[comment="name: \"Array Size\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	19 -> 20;
	22	[comment="name: \"example element\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	19 -> 22;
	20 -> 21;
	23	[comment="name: \"Enchant Type\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\"",
		label="Enchant Type"];
	22 -> 23;
	25	[comment="name: \"Enchant Level\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enchant Level"];
	22 -> 25;
	23 -> 24;
	25 -> 26;
	28	[comment="name: \"Array Size\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	27 -> 28;
	30	[comment="name: \"example element\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	27 -> 30;
	28 -> 29;
	31	[comment="name: \"Enchant Type\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Enchant::Type\"",
		label="Enchant Type"];
	30 -> 31;
	33	[comment="name: \"Enchant Level\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Enchant Level"];
	30 -> 33;
	31 -> 32;
	33 -> 34;
}

```

## 字段

/// define
ItemEnchants

Slot：<!-- md:samp int -->

- 类型：int。

Item Enchants For Given Activation

Item Enchants For Given Activation数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Item Enchants For Given Activation的示例元素

Enchant Type：<!-- md:samp byte -->

- 类型：byte。enumeration: Enchant::Type

Enchant Level：<!-- md:samp byte -->

- 类型：byte。


///
