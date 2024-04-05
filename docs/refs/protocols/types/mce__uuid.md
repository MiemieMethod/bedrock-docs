# <!-- md:samp mce::UUID -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp mce::UUID -->类型。

## 结构

```viz
digraph "mce::UUID" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		45	[comment="name: \"unsigned int64\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
		47	[comment="name: \"unsigned int64\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int64"];
	}
	43	[comment="name: \"mce::UUID\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="mce::UUID"];
	44	[comment="name: \"Most Significant Bits\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Most Significant Bits"];
	43 -> 44;
	46	[comment="name: \"Least Significant Bits\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Least Significant Bits"];
	43 -> 46;
	44 -> 45;
	46 -> 47;
}

```

## 字段

/// define
mce::UUID

Most Significant Bits：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。

Least Significant Bits：<!-- md:samp unsigned int64 -->

- 类型：unsigned int64。


///
