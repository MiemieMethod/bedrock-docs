# <!-- md:samp ActorUniqueID -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ActorUniqueID -->类型。该类型用于protocol.type.actoruniqueid.description

## 结构

```viz
digraph "ActorUniqueID" {
rankdir = LR
2
2 -> 3
3 -> 4

2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="Actor Unique ID",comment="name: \"Actor Unique ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;4}

}

```

## 字段

```title='ActorUniqueID'
[actor_unique_id]
```

/// html | div.result
//// define
Actor Unique ID：<!-- md:samp varint64 -->

- 基本类型。protocol.type.actoruniqueid.actor_unique_id.description


////

///

