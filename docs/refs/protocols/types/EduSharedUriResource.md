# <!-- md:samp EduSharedUriResource -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EduSharedUriResource -->类型。

## 结构

```dot
digraph EduSharedUriResource {
	graph [rankdir=LR];
	{
		graph [rank=max];
		127	[comment="name: \"string\", typeName: \"\", id: 127, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		129	[comment="name: \"string\", typeName: \"\", id: 129, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	125	[comment="name: \"EduSharedUriResource\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=EduSharedUriResource];
	126	[comment="name: \"Button Name\", typeName: \"\", id: 126, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Button Name"];
	125 -> 126;
	128	[comment="name: \"Link Uri\", typeName: \"\", id: 128, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Link Uri"];
	125 -> 128;
	126 -> 127;
	128 -> 129;
}

```

## 字段

/// define
EduSharedUriResource

Button Name：<!-- md:samp string -->

- 类型：string。

Link Uri：<!-- md:samp string -->

- 类型：string。


///
