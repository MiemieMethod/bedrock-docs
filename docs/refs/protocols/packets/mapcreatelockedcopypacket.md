# <!-- md:samp MapCreateLockedCopyPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp MapCreateLockedCopyPacket -->数据包，数字ID是`131`。该数据包用于protocol.packet.mapcreatelockedcopypacket.description

## 结构

```viz
digraph "MapCreateLockedCopyPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="MapCreateLockedCopyPacket",comment="name: \"MapCreateLockedCopyPacket\", typeName: \"\", id: 0, branchId: 131, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Original Map Id",comment="name: \"Original Map Id\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id of the map being locked.\""];
2 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="New Map Id",comment="name: \"New Map Id\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id that the new map should have.\""];
4 [label="ActorUniqueID",comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='MapCreateLockedCopyPacket'
[original_map_id][new_map_id]
```

/// html | div.result
//// define
Original Map Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.mapcreatelockedcopypacket.original_map_id.descriptionId of the map being locked.


////
//// define
New Map Id：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 特殊类型。protocol.packet.mapcreatelockedcopypacket.new_map_id.descriptionId that the new map should have.


////

///

