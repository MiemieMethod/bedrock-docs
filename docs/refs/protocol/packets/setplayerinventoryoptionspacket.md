# <!-- md:samp SetPlayerInventoryOptionsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetPlayerInventoryOptionsPacket -->数据包，数字ID是`307`。

## 结构

```viz
digraph SetPlayerInventoryOptionsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		4	[comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		10	[comment="name: \"varint\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetPlayerInventoryOptionsPacket\", typeName: \"\", id: 0, branchId: 307, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetPlayerInventoryOptionsPacket];
	1	[comment="name: \"Left Inventory Tab\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLeftTabIndex\"",
		label="Left Inventory Tab"];
	0 -> 1;
	3	[comment="name: \"Right Inventory Tab\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryRightTabIndex\"",
		label="Right Inventory Tab"];
	0 -> 3;
	5	[comment="name: \"Filtering\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Filtering];
	0 -> 5;
	7	[comment="name: \"Layout Inv\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLayout\"",
		label="Layout Inv"];
	0 -> 7;
	9	[comment="name: \"Layout Craft\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InventoryLayout\"",
		label="Layout Craft"];
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
SetPlayerInventoryOptionsPacket

Left Inventory Tab：<!-- md:samp varint -->

- 类型：varint。enumeration: InventoryLeftTabIndex

Right Inventory Tab：<!-- md:samp varint -->

- 类型：varint。enumeration: InventoryRightTabIndex

Filtering：<!-- md:samp bool -->

- 类型：bool。

Layout Inv：<!-- md:samp varint -->

- 类型：varint。enumeration: InventoryLayout

Layout Craft：<!-- md:samp varint -->

- 类型：varint。enumeration: InventoryLayout


///
