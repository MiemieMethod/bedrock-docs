# <!-- md:samp PotionMixDataEntry -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PotionMixDataEntry -->类型。

## 结构

```viz
digraph PotionMixDataEntry {
	graph [rankdir=LR];
	{
		graph [rank=max];
		14	[comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		16	[comment="name: \"varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		18	[comment="name: \"varint\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		20	[comment="name: \"varint\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		22	[comment="name: \"varint\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		24	[comment="name: \"varint\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	12	[comment="name: \"PotionMixDataEntry\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PotionMixDataEntry];
	13	[comment="name: \"From Potion: Input - Potion Id\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="From Potion: Input - Potion Id"];
	12 -> 13;
	15	[comment="name: \"From Item Aux\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="From Item Aux"];
	12 -> 15;
	17	[comment="name: \"Reagent Item Id\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reagent Item Id"];
	12 -> 17;
	19	[comment="name: \"Reagent Item Aux\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Reagent Item Aux"];
	12 -> 19;
	21	[comment="name: \"To Potion: Output - Potion Id\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="To Potion: Output - Potion Id"];
	12 -> 21;
	23	[comment="name: \"To Item Aux\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="To Item Aux"];
	12 -> 23;
	13 -> 14;
	15 -> 16;
	17 -> 18;
	19 -> 20;
	21 -> 22;
	23 -> 24;
}

```

## 字段

/// define
PotionMixDataEntry

From Potion: Input - Potion Id：<!-- md:samp varint -->

- 类型：varint。

From Item Aux：<!-- md:samp varint -->

- 类型：varint。

Reagent Item Id：<!-- md:samp varint -->

- 类型：varint。

Reagent Item Aux：<!-- md:samp varint -->

- 类型：varint。

To Potion: Output - Potion Id：<!-- md:samp varint -->

- 类型：varint。

To Item Aux：<!-- md:samp varint -->

- 类型：varint。


///
