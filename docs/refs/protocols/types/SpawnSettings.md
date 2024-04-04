# <!-- md:samp SpawnSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SpawnSettings -->类型。

## 结构

```dot
digraph SpawnSettings {
	graph [rankdir=LR];
	{
		graph [rank=max];
		29	[comment="name: \"short\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=short];
		31	[comment="name: \"string\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		33	[comment="name: \"varint\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
	}
	27	[comment="name: \"SpawnSettings\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=SpawnSettings];
	28	[comment="name: \"Type\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: SpawnBiomeType\"",
		label=Type];
	27 -> 28;
	30	[comment="name: \"User Defined Biome Name\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="User Defined Biome Name"];
	27 -> 30;
	32	[comment="name: \"Dimension\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently 0 for Overworld, 1 for Nether, \
2 for The End, 3 Undefined\"",
		label=Dimension];
	27 -> 32;
	28 -> 29;
	30 -> 31;
	32 -> 33;
}

```

## 字段

/// define
SpawnSettings

Type：<!-- md:samp short -->

- 类型：short。enumeration: SpawnBiomeType

User Defined Biome Name：<!-- md:samp string -->

- 类型：string。

Dimension：<!-- md:samp varint -->

- 类型：varint。Currently 0 for Overworld, 1 for Nether, 2 for The End, 3 Undefined


///
