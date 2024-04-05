# <!-- md:samp AdventureSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AdventureSettings -->类型。

## 结构

```viz
digraph AdventureSettings {
	graph [rankdir=LR];
	{
		graph [rank=max];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		8	[comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		10	[comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	2	[comment="name: \"AdventureSettings\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=AdventureSettings];
	3	[comment="name: \"no PvM\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="no PvM"];
	2 -> 3;
	5	[comment="name: \"no MvP\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="no MvP"];
	2 -> 5;
	7	[comment="name: \"Immutable World\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Immutable World"];
	2 -> 7;
	9	[comment="name: \"Show Name Tags\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Show Name Tags"];
	2 -> 9;
	11	[comment="name: \"Auto Jump\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Auto Jump"];
	2 -> 11;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
}

```

## 字段

/// define
AdventureSettings

no PvM：<!-- md:samp bool -->

- 类型：bool。

no MvP：<!-- md:samp bool -->

- 类型：bool。

Immutable World：<!-- md:samp bool -->

- 类型：bool。

Show Name Tags：<!-- md:samp bool -->

- 类型：bool。

Auto Jump：<!-- md:samp bool -->

- 类型：bool。


///
