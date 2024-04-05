# <!-- md:samp SetHudPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetHudPacket -->数据包，数字ID是`308`。

## 结构

```viz
digraph SetHudPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		3	[comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		6	[comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		8	[comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	0	[comment="name: \"SetHudPacket\", typeName: \"\", id: 0, branchId: 308, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetHudPacket];
	1	[comment="name: \"Hud Element List\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Hud Element List"];
	0 -> 1;
	7	[comment="name: \"isHudVisible\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: HudVisibility\"",
		label=isHudVisible];
	0 -> 7;
	2	[comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	1 -> 2;
	4	[comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	1 -> 4;
	2 -> 3;
	5	[comment="name: \"Hud Element\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: HudElement\"",
		label="Hud Element"];
	4 -> 5;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
SetHudPacket

Hud Element List

//// define
Hud Element List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Hud Element List的示例元素

Hud Element：<!-- md:samp varint -->

- 类型：varint。enumeration: HudElement


////


isHudVisible：<!-- md:samp varint -->

- 类型：varint。enumeration: HudVisibility


///
