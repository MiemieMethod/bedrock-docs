# <!-- md:samp PurchaseReceiptPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PurchaseReceiptPacket -->数据包，数字ID是`92`。

## 结构

```viz
digraph PurchaseReceiptPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"PurchaseReceiptPacket\", typeName: \"\", id: 0, branchId: 92, recurseId: -1, attributes: 0, notes: \"\"",
		label=PurchaseReceiptPacket];
	1	[comment="name: \"Purchase Receipts\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Purchase Receipts"];
	0 -> 1;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Proof of Purchase\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Proof of Purchase"];
	4 -> 5;
	5 -> 6;
}

```

## 字段

/// define
PurchaseReceiptPacket

Purchase Receipts

Purchase Receipts数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Purchase Receipts的示例元素

Proof of Purchase：<!-- md:samp string -->

- 类型：string。


///
