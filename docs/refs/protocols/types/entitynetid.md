# <!-- md:samp EntityNetId -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp EntityNetId -->类型。该类型用于protocol.type.entitynetid.description

## 结构

```viz
digraph "EntityNetId" {
rankdir = LR
2
2 -> 3
3 -> 4

2 [label="EntityNetId",comment="name: \"EntityNetId\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Raw Entity Id",comment="name: \"Raw Entity Id\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4}

}

```

## 字段

```title='EntityNetId'
[raw_entity_id]
```

/// html | div.result
//// define
Raw Entity Id：<!-- md:samp unsigned varint -->

- 基本类型。protocol.type.entitynetid.raw_entity_id.description


////

///

