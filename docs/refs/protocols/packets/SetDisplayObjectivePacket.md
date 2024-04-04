# <!-- md:samp SetDisplayObjectivePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetDisplayObjectivePacket -->数据包，数字ID是`107`。

## 结构

```dot
digraph SetDisplayObjectivePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		10	[comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"SetDisplayObjectivePacket\", typeName: \"\", id: 0, branchId: 107, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetDisplayObjectivePacket];
	1	[comment="name: \"Display Slot Name\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Display Slot Name"];
	0 -> 1;
	3	[comment="name: \"Objective Name\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Objective Name"];
	0 -> 3;
	5	[comment="name: \"Objective Display Name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Objective Display Name"];
	0 -> 5;
	7	[comment="name: \"Criteria Name\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Criteria Name"];
	0 -> 7;
	9	[comment="name: \"Sort Order\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ObjectiveSortOrder\"",
		label="Sort Order"];
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
SetDisplayObjectivePacket

Display Slot Name：<!-- md:samp string -->

- 类型：string。

Objective Name：<!-- md:samp string -->

- 类型：string。

Objective Display Name：<!-- md:samp string -->

- 类型：string。

Criteria Name：<!-- md:samp string -->

- 类型：string。

Sort Order：<!-- md:samp byte -->

- 类型：byte。enumeration: ObjectiveSortOrder


///
