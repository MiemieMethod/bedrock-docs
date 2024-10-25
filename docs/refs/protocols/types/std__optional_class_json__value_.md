# <!-- md:samp std::optional&lt;class Json::Value&gt; -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp std::optional&lt;class Json::Value&gt; -->类型。该类型用于protocol.type.std::optional&lt;class_json::value&gt;.description

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

```title='std::optional&lt;class Json::Value&gt;'
[has_value]
```

/// html | div.result
//// define
Has Value：<!-- md:samp bool -->

- 基本类型。protocol.type.std::optional&lt;class_json::value&gt;.has_value.descriptionIf true, follow with appropriate data type, otherwise nothing


////

///

