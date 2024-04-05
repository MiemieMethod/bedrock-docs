# <!-- md:samp std::optional<class MolangVariableMap> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<class MolangVariableMap> -->类型。

## 结构

```viz
digraph "std::optional<class MolangVariableMap>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		12	[comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
		17	[comment="name: \"MolangVariableMap\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=MolangVariableMap];
	}
	10	[comment="name: \"std::optional<class MolangVariableMap>\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<class MolangVariableMap>"];
	11	[comment="name: \"Has Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	10 -> 11;
	13	[comment="name: \"Value\", typeName: \"MolangVariableMap\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Value];
	10 -> 13;
	11 -> 12;
	13 -> 17;
}

```

## 字段

/// define
std::optional<class MolangVariableMap>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing

Value：[<!-- md:samp MolangVariableMap -->](refs/protocols/types/molangvariablemap.md)

- 类型：MolangVariableMap。


///
