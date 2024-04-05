# <!-- md:samp std::optional<float> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<float> -->类型。

## 结构

```viz
digraph "std::optional<float>" {
rankdir = LR
14
14 -> 15
15 -> 16

14 [label="std::optional<float>",comment="name: \"std::optional<float>\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
15 [label="Has Value",comment="name: \"Has Value\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data type, otherwise nothing\""];
16 [label="bool",comment="name: \"bool\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;16}

}

```

## 字段

/// define
std::optional<float>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///
