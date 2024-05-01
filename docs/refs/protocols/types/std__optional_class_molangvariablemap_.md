# <!-- md:samp std::optional&lt;class MolangVariableMap&gt; -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp std::optional&lt;class MolangVariableMap&gt; -->类型。该类型用于protocol.type.std::optional&lt;class_molangvariablemap&gt;.description

## 结构

```viz
digraph "std::optional<class MolangVariableMap>" {
rankdir = LR
10
10 -> 11
11 -> 12
10 -> 13
13 -> 17

10 [label="std::optional<class MolangVariableMap>",comment="name: \"std::optional<class MolangVariableMap>\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="Has Value",comment="name: \"Has Value\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data type, otherwise nothing\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Value",comment="name: \"Value\", typeName: \"MolangVariableMap\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
17 [label="MolangVariableMap",comment="name: \"MolangVariableMap\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;12;17}

}

```

## 字段

```title='std::optional&lt;class MolangVariableMap&gt;'
[has_value][value]
```

/// html | div.result
//// define
Has Value：<!-- md:samp bool -->

- 基本类型。protocol.type.std::optional&lt;class_molangvariablemap&gt;.has_value.descriptionIf true, follow with appropriate data type, otherwise nothing


////
//// define
Value：[<!-- md:samp MolangVariableMap -->](../types/molangvariablemap.md)

- 特殊类型。protocol.type.std::optional&lt;class_molangvariablemap&gt;.value.description


////

///

