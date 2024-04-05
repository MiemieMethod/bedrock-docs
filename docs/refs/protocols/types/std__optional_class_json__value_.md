# <!-- md:samp std::optional<class Json::Value> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<class Json::Value> -->类型。

## 结构

```viz
digraph "std::optional<class Json::Value>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	4	[comment="name: \"std::optional<class Json::Value>\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<class Json::Value>"];
	5	[comment="name: \"Has Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	4 -> 5;
	5 -> 6;
}

```

## 字段

/// define
std::optional<class Json::Value>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///