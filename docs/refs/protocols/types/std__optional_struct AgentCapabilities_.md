# <!-- md:samp std::optional<struct AgentCapabilities> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<struct AgentCapabilities> -->类型。

## 结构

```viz
digraph "std::optional<struct AgentCapabilities>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		18	[comment="name: \"bool\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	16	[comment="name: \"std::optional<struct AgentCapabilities>\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<struct AgentCapabilities>"];
	17	[comment="name: \"Has Value\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	16 -> 17;
	17 -> 18;
}

```

## 字段

/// define
std::optional<struct AgentCapabilities>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///
