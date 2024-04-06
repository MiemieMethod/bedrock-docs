# <!-- md:samp std::optional&lt;bool&gt; -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional&lt;bool&gt; -->类型。

## 结构

```viz
digraph "std::optional<bool>" {
rankdir = LR
32
32 -> 33
33 -> 34

32 [label="std::optional<bool>",comment="name: \"std::optional<bool>\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="Has Value",comment="name: \"Has Value\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data type, otherwise nothing\""];
34 [label="bool",comment="name: \"bool\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;34}

}

```

## 字段

```title='std::optional&lt;bool&gt;'
[has_value]
```

/// html | div.result
//// define
Has Value：<!-- md:samp bool -->

- 基本类型。If true, follow with appropriate data type, otherwise nothing


////

///

