# <!-- md:samp FullContainerName -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp FullContainerName -->类型。该类型用于protocol.type.fullcontainername.description

## 结构

```viz
digraph "FullContainerName" {
rankdir = LR
10
10 -> 11
11 -> 12
10 -> 13
13 -> 17

10 [label="FullContainerName",comment="name: \"FullContainerName\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
11 [label="Container Name",comment="name: \"Container Name\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="byte",comment="name: \"byte\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="Optional Dynamic Container ID",comment="name: \"Optional Dynamic Container ID\", typeName: \"std::optional<unsigned int>\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
17 [label="std::optional<unsigned int>",comment="name: \"std::optional<unsigned int>\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;12;17}

}

```

## 字段

```title='FullContainerName'
[container_name][optional_dynamic_container_id]
```

/// html | div.result
//// define
Container Name：<!-- md:samp byte -->

- 基本类型。protocol.type.fullcontainername.container_name.description


////
//// define
Optional Dynamic Container ID：[<!-- md:samp std::optional&lt;unsigned int&gt; -->](../types/std__optional_unsigned_int_.md)

- 特殊类型。protocol.type.fullcontainername.optional_dynamic_container_id.description


////

///

