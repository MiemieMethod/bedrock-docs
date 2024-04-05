# <!-- md:samp std::optional<float> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<float> -->类型。

## 结构

```viz
digraph "std::optional<float>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		16	[comment="name: \"bool\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	14	[comment="name: \"std::optional<float>\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<float>"];
	15	[comment="name: \"Has Value\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	14 -> 15;
	15 -> 16;
}

```

## 字段

/// define
std::optional<float>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///
