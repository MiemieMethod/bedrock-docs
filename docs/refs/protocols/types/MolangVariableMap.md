# <!-- md:samp MolangVariableMap -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MolangVariableMap -->类型。

## 结构

```viz
digraph MolangVariableMap {
	graph [rankdir=LR];
	{
		graph [rank=max];
		16	[comment="name: \"string\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	14	[comment="name: \"MolangVariableMap\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=MolangVariableMap];
	15	[comment="name: \"Serialized Variable Map\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Serialized Variable Map"];
	14 -> 15;
	15 -> 16;
}

```

## 字段

/// define
MolangVariableMap

Serialized Variable Map：<!-- md:samp string -->

- 类型：string。


///
