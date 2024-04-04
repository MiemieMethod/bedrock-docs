# <!-- md:samp CompressedBiomeDefinitionList -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CompressedBiomeDefinitionList -->类型，数字ID是`301`。

## 结构

```dot
digraph CompressedBiomeDefinitionList {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	0	[comment="name: \"CompressedBiomeDefinitionList\", typeName: \"\", id: 0, branchId: 301, recurseId: -1, attributes: 0, notes: \"\"",
		label=CompressedBiomeDefinitionList];
	1	[comment="name: \"Compressed BiomeData\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Compressed BiomeData"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
CompressedBiomeDefinitionList

Compressed BiomeData：<!-- md:samp string -->

- 类型：string。


///
