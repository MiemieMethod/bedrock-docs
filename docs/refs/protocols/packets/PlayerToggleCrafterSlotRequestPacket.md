# <!-- md:samp PlayerToggleCrafterSlotRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerToggleCrafterSlotRequestPacket -->数据包，数字ID是`306`。

## 结构

```dot
digraph PlayerToggleCrafterSlotRequestPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		4	[comment="name: \"int\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		6	[comment="name: \"int\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"PlayerToggleCrafterSlotRequestPacket\", typeName: \"\", id: 0, branchId: 306, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerToggleCrafterSlotRequestPacket];
	1	[comment="name: \"Pos X\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Pos X"];
	0 -> 1;
	3	[comment="name: \"Pos Y\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Pos Y"];
	0 -> 3;
	5	[comment="name: \"Pos Z\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Pos Z"];
	0 -> 5;
	7	[comment="name: \"Slot Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Slot Index"];
	0 -> 7;
	9	[comment="name: \"Is Disabled\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Is Disabled"];
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
PlayerToggleCrafterSlotRequestPacket

Pos X：<!-- md:samp int -->

- 类型：int。

Pos Y：<!-- md:samp int -->

- 类型：int。

Pos Z：<!-- md:samp int -->

- 类型：int。

Slot Index：<!-- md:samp byte -->

- 类型：byte。

Is Disabled：<!-- md:samp bool -->

- 类型：bool。


///
