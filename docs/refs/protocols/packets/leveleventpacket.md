# <!-- md:samp LevelEventPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp LevelEventPacket -->数据包，数字ID是`25`。该数据包用于protocol.packet.leveleventpacket.description

## 结构

```viz
digraph "LevelEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="LevelEventPacket",comment="name: \"LevelEventPacket\", typeName: \"\", id: 0, branchId: 25, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='LevelEventPacket'
[event_id][position][data]
```

/// html | div.result
//// define
Event ID：<!-- md:samp varint -->

- 基本类型。protocol.packet.leveleventpacket.event_id.description


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.leveleventpacket.position.descriptionNote about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)


////
//// define
Data：<!-- md:samp varint -->

- 基本类型。protocol.packet.leveleventpacket.data.description


////

///

