# <!-- md:samp std::optional&lt;class Json::Value&gt; -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional&lt;class Json::Value&gt; -->类型。

## 结构

```viz
digraph "std::optional<class Json::Value>" {
rankdir = LR
4
4 -> 5
5 -> 6

4 [label="std::optional<class Json::Value>",comment="name: \"std::optional<class Json::Value>\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="Has Value",comment="name: \"Has Value\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data type, otherwise nothing\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;6}

}

```

## 字段

```title='std::optional<class Json::Value>'
[has_value]
```

/// html | div.result
//// define
Has Value：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。If true, follow with appropriate data type, otherwise nothing


////

///

