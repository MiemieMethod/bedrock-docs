# <!-- md:samp CompletedUsingItemPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CompletedUsingItemPacket -->数据包，数字ID是`142`。

## 结构

```viz
digraph CompletedUsingItemPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"short\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=short];
		4	[comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
	}
	0	[comment="name: \"CompletedUsingItemPacket\", typeName: \"\", id: 0, branchId: 142, recurseId: -1, attributes: 0, notes: \"\"",
		label=CompletedUsingItemPacket];
	1	[comment="name: \"Item Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Item Id"];
	0 -> 1;
	3	[comment="name: \"Item Use Method\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemUseMethod\"",
		label="Item Use Method"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
CompletedUsingItemPacket

Item Id：<!-- md:samp short -->

- 类型：short。

Item Use Method：<!-- md:samp int -->

- 类型：int。enumeration: ItemUseMethod


///
