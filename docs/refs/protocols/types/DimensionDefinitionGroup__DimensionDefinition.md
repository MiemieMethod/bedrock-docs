# <!-- md:samp DimensionDefinitionGroup::DimensionDefinition -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp DimensionDefinitionGroup::DimensionDefinition -->类型。

## 结构

```dot
digraph "DimensionDefinitionGroup::DimensionDefinition" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		12	[comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		14	[comment="name: \"varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		16	[comment="name: \"varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	10	[comment="name: \"DimensionDefinitionGroup::DimensionDefinition\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="DimensionDefinitionGroup::DimensionDefinition"];
	11	[comment="name: \"Height Maximum\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Height Maximum"];
	10 -> 11;
	13	[comment="name: \"Height Minimum\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Height Minimum"];
	10 -> 13;
	15	[comment="name: \"Generator Type\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Generator Type"];
	10 -> 15;
	11 -> 12;
	13 -> 14;
	15 -> 16;
}

```

## 字段

/// define
DimensionDefinitionGroup::DimensionDefinition

Height Maximum：<!-- md:samp varint -->

- 类型：varint。

Height Minimum：<!-- md:samp varint -->

- 类型：varint。

Generator Type：<!-- md:samp varint -->

- 类型：varint。


///
