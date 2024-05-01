# <!-- md:samp ActorLink -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ActorLink -->类型。该类型用于活动对象链接。

## 结构

```viz
digraph "ActorLink" {
rankdir = LR
110
110 -> 111
111 -> 112
110 -> 113
113 -> 114
110 -> 115
115 -> 116
110 -> 117
117 -> 118
110 -> 119
119 -> 120

110 [label="ActorLink",comment="name: \"ActorLink\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
111 [label="Actor Unique ID - A",comment="name: \"Actor Unique ID - A\", typeName: \"ActorUniqueID\", id: 111, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
112 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
113 [label="Actor Unique ID - B",comment="name: \"Actor Unique ID - B\", typeName: \"ActorUniqueID\", id: 113, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
114 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
115 [label="Link Type",comment="name: \"Link Type\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
116 [label="byte",comment="name: \"byte\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
117 [label="Immediate",comment="name: \"Immediate\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
118 [label="bool",comment="name: \"bool\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
119 [label="Passenger Initiated",comment="name: \"Passenger Initiated\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 0, notes: \"Whether the link was changed by the passenger\""];
120 [label="bool",comment="name: \"bool\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;112;114;116;118;120}

}

```

## 字段

```title='ActorLink'
[actor_unique_id_a][actor_unique_id_b][link_type][immediate][passenger_initiated]
```

/// html | div.result
//// define
Actor Unique ID - A：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.type.actorlink.actor_unique_id_a.description


////
//// define
Actor Unique ID - B：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.type.actorlink.actor_unique_id_b.description


////
//// define
Link Type：<!-- md:samp byte -->

- 基本类型。protocol.type.actorlink.link_type.description


////
//// define
Immediate：<!-- md:samp bool -->

- 基本类型。protocol.type.actorlink.immediate.description


////
//// define
Passenger Initiated：<!-- md:samp bool -->

- 基本类型。protocol.type.actorlink.passenger_initiated.descriptionWhether the link was changed by the passenger


////

///

