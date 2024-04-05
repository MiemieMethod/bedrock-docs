# <!-- md:samp InventoryTransaction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp InventoryTransaction -->类型。

## 结构

```viz
digraph InventoryTransaction {
	graph [rankdir=LR];
	{
		graph [rank=max];
		25	[comment="name: \"unsigned varint\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		51	[comment="name: \"InventoryAction\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=InventoryAction];
	}
	22	[comment="name: \"InventoryTransaction\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=InventoryTransaction];
	23	[comment="name: \"Actions\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Actions];
	22 -> 23;
	24	[comment="name: \"Array Size\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	23 -> 24;
	26	[comment="name: \"example element\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	23 -> 26;
	24 -> 25;
	27	[comment="name: \"Action\", typeName: \"InventoryAction\", id: 27, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Action];
	26 -> 27;
	27 -> 51;
}

```

## 字段

/// define
InventoryTransaction

Actions

//// define
Actions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Actions的示例元素

Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 类型：InventoryAction。


////



///
