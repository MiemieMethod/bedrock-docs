# <!-- md:samp LevelEventGenericPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelEventGenericPacket -->数据包，数字ID是`124`。

## 结构

```viz
digraph "LevelEventGenericPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="LevelEventGenericPacket",comment="name: \"LevelEventGenericPacket\", typeName: \"\", id: 0, branchId: 124, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LevelEvent\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Data",comment="name: \"Event Data\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\""];
4 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

/// define
LevelEventGenericPacket

Event ID：<!-- md:samp varint -->

- 类型：varint。enumeration: LevelEvent

Event Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)


///
