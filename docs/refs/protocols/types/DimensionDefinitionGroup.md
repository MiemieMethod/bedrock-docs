# <!-- md:samp DimensionDefinitionGroup -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DimensionDefinitionGroup -->类型。

## 结构

```viz
digraph DimensionDefinitionGroup {
	graph [rankdir=LR];
	{
		graph [rank=max];
		5	[comment="name: \"unsigned varint\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		8	[comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		17	[comment="name: \"DimensionDefinitionGroup::DimensionDefinition\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="DimensionDefinitionGroup::DimensionDefinition"];
	}
	2	[comment="name: \"DimensionDefinitionGroup\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=DimensionDefinitionGroup];
	3	[comment="name: \"Definitions\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Definitions];
	2 -> 3;
	4	[comment="name: \"Array Size\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	3 -> 4;
	6	[comment="name: \"example element\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	3 -> 6;
	4 -> 5;
	7	[comment="name: \"Name String\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Name String"];
	6 -> 7;
	9	[comment="name: \"Dimension Definition\", typeName: \"DimensionDefinitionGroup::DimensionDefinition\", id: 9, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="Dimension Definition"];
	6 -> 9;
	7 -> 8;
	9 -> 17;
}

```

## 字段

/// define
DimensionDefinitionGroup

Definitions

Definitions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。

Definitions的示例元素

Name String：<!-- md:samp string -->

- 类型：string。

Dimension Definition：[<!-- md:samp DimensionDefinitionGroup::DimensionDefinition -->](refs/protocols/types/DimensionDefinitionGroup::DimensionDefinition.md)

- 类型：DimensionDefinitionGroup::DimensionDefinition。


///
