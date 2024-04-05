# <!-- md:samp GameRulesChangedPacketData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp GameRulesChangedPacketData -->类型。

## 结构

```viz
digraph GameRulesChangedPacketData {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		7	[comment="name: \"string\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		9	[comment="name: \"bool\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		11	[comment="name: \"unsigned varint\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		16	[comment="name: \"unsigned varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		17	[comment="name: \"unsigned varint\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		15	[comment="name: \"bool\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	1	[comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=GameRulesChangedPacketData];
	2	[comment="name: \"Rules List\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Rules List"];
	1 -> 2;
	3	[comment="name: \"Array Size\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	2 -> 3;
	5	[comment="name: \"example element\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	2 -> 5;
	3 -> 4;
	6	[comment="name: \"Rule Name\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Rule Name"];
	5 -> 6;
	8	[comment="name: \"Can Be Modified By Player\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Can Be Modified By Player"];
	5 -> 8;
	10	[comment="name: \"Rule Type\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameRule::Type\"",
		label="Rule Type"];
	5 -> 10;
	12	[comment="name: \"Dependency on 'Rule Type'\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Rule Type'",
		shape=note];
	5 -> 12;
	6 -> 7;
	8 -> 9;
	10 -> 11;
	10 -> 16;
	10 -> 17;
	13	[comment="name: \"if (1)\", typeName: \"\", id: 13, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	12 -> 13;
	14	[comment="name: \"Rule Value\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Rule Value"];
	13 -> 14;
	14 -> 15;
}

```

## 字段

/// define
GameRulesChangedPacketData

Rules List

//// define
Rules List数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Rules List的示例元素

Rule Name：<!-- md:samp string -->

- 类型：string。

Can Be Modified By Player：<!-- md:samp bool -->

- 类型：bool。

Rule Type

Dependency on 'Rule Type'

///// tab | if (1)
////// define
if (1)

Rule Value：<!-- md:samp bool -->

- 类型：bool。


//////

/////



////



///
