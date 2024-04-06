# <!-- md:samp RemoveActorPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RemoveActorPacket -->数据包，数字ID是`14`。

## 结构

```viz
digraph "RemoveActorPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="RemoveActorPacket",comment="name: \"RemoveActorPacket\", typeName: \"\", id: 0, branchId: 14, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Actor ID",comment="name: \"Target Actor ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='RemoveActorPacket'
[target_actor_id]
```

/// html | div.result
//// define
Target Actor ID：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。


////

///

