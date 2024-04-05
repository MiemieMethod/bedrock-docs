# <!-- md:samp LevelEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelEventPacket -->数据包，数字ID是`25`。

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
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LevelEvent\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

/// define
LevelEventPacket

Event ID：<!-- md:samp varint -->

- 类型：varint。enumeration: LevelEvent

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)

Data：<!-- md:samp varint -->

- 类型：varint。


///
