# <!-- md:samp std::optional<bool> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<bool> -->类型。

## 结构

```viz
digraph "std::optional<bool>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		34	[comment="name: \"bool\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	32	[comment="name: \"std::optional<bool>\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<bool>"];
	33	[comment="name: \"Has Value\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	32 -> 33;
	33 -> 34;
}

```

## 字段

/// define
std::optional<bool>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///
