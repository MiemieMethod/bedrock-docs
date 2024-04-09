# <!-- md:samp ContainerMixDataEntry -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ContainerMixDataEntry -->类型。该类型用于protocol.type.containermixdataentry.description

## 结构

```viz
digraph "ContainerMixDataEntry" {
rankdir = LR
31
31 -> 32
32 -> 33
31 -> 34
34 -> 35
31 -> 36
36 -> 37

31 [label="ContainerMixDataEntry",comment="name: \"ContainerMixDataEntry\", typeName: \"\", id: 31, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
32 [label="From Item (Id): Input",comment="name: \"From Item (Id): Input\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
33 [label="varint",comment="name: \"varint\", typeName: \"\", id: 33, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
34 [label="Re-agent Item Id",comment="name: \"Re-agent Item Id\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
35 [label="varint",comment="name: \"varint\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
36 [label="To Item (Id): Output",comment="name: \"To Item (Id): Output\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
37 [label="varint",comment="name: \"varint\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;33;35;37}

}

```

## 字段

```title='ContainerMixDataEntry'
[from_item:_input][re-agent_item_id][to_item:_output]
```

/// html | div.result
//// define
From Item (Id): Input：<!-- md:samp varint -->

- 基本类型。protocol.type.containermixdataentry.from_item:_input.description


////
//// define
Re-agent Item Id：<!-- md:samp varint -->

- 基本类型。protocol.type.containermixdataentry.re-agent_item_id.description


////
//// define
To Item (Id): Output：<!-- md:samp varint -->

- 基本类型。protocol.type.containermixdataentry.to_item:_output.description


////

///

