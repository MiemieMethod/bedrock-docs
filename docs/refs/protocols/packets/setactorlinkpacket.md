# <!-- md:samp SetActorLinkPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SetActorLinkPacket -->数据包，数字ID是`41`。该数据包用于protocol.packet.setactorlinkpacket.description

## 结构

```viz
digraph "SetActorLinkPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetActorLinkPacket",comment="name: \"SetActorLinkPacket\", typeName: \"\", id: 0, branchId: 41, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Link",comment="name: \"Link\", typeName: \"ActorLink\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorLink",comment="name: \"ActorLink\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetActorLinkPacket'
[link]
```

/// html | div.result
//// define
Link：[<!-- md:samp ActorLink -->](../types/actorlink.md)

- 特殊类型。protocol.packet.setactorlinkpacket.link.description


////

///

