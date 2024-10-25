# <!-- md:samp TakeItemActorPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp TakeItemActorPacket -->数据包，数字ID是`17`。该数据包用于protocol.packet.takeitemactorpacket.description

## 结构

```viz
digraph "TakeItemActorPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="TakeItemActorPacket",comment="name: \"TakeItemActorPacket\", typeName: \"\", id: 0, branchId: 17, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Item Runtime ID",comment="name: \"Item Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Actor Runtime ID",comment="name: \"Actor Runtime ID\", typeName: \"ActorRuntimeID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='TakeItemActorPacket'
[item_runtime_id][actor_runtime_id]
```

/// html | div.result
//// define
Item Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.takeitemactorpacket.item_runtime_id.description


////
//// define
Actor Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.takeitemactorpacket.actor_runtime_id.description


////

///

