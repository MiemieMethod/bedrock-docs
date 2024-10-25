# <!-- md:samp DebugInfoPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp DebugInfoPacket -->数据包，数字ID是`155`。该数据包用于protocol.packet.debuginfopacket.description

## 结构

```viz
digraph "DebugInfoPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="DebugInfoPacket",comment="name: \"DebugInfoPacket\", typeName: \"\", id: 0, branchId: 155, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Actor Id",comment="name: \"Actor Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Data",comment="name: \"Data\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="string",comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='DebugInfoPacket'
[actor_id][data]
```

/// html | div.result
//// define
Actor Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.debuginfopacket.actor_id.description


////
//// define
Data：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.debuginfopacket.data.description


////

///

