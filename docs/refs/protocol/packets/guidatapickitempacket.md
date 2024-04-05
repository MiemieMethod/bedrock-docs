# <!-- md:samp GuiDataPickItemPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GuiDataPickItemPacket -->数据包，数字ID是`54`。

## 结构

```viz
digraph GuiDataPickItemPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
	}
	0	[comment="name: \"GuiDataPickItemPacket\", typeName: \"\", id: 0, branchId: 54, recurseId: -1, attributes: 0, notes: \"\"",
		label=GuiDataPickItemPacket];
	1	[comment="name: \"Item Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Name"];
	0 -> 1;
	3	[comment="name: \"Item Effect Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Effect Name"];
	0 -> 3;
	5	[comment="name: \"Slot\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
GuiDataPickItemPacket

Item Name：<!-- md:samp string -->

- 类型：string。

Item Effect Name：<!-- md:samp string -->

- 类型：string。

Slot：<!-- md:samp int -->

- 类型：int。


///
