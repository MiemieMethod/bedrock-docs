# <!-- md:samp LevelSoundEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelSoundEventPacket -->数据包，数字ID是`123`。

## 结构

```viz
digraph "LevelSoundEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12

0 [label="LevelSoundEventPacket",comment="name: \"LevelSoundEventPacket\", typeName: \"\", id: 0, branchId: 123, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Puv::Legacy::LevelSoundEvent\""];
2 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Actor Identifier",comment="name: \"Actor Identifier\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="string",comment="name: \"string\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Is Baby Mob",comment="name: \"Is Baby Mob\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Is Global",comment="name: \"Is Global\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

```title='LevelSoundEventPacket'
[event_id][position][data][actor_identifier][is_baby_mob][is_global]
```

/// html | div.result
//// define
Event ID：<!-- md:samp unsigned varint -->

- 类型：<!-- md:samp unsigned varint -->。enumeration: Puv::Legacy::LevelSoundEvent


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：<!-- md:samp Vec3 -->。


////
//// define
Data：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。


////
//// define
Actor Identifier：<!-- md:samp string -->

- 类型：<!-- md:samp string -->。


////
//// define
Is Baby Mob：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////
//// define
Is Global：<!-- md:samp bool -->

- 类型：<!-- md:samp bool -->。


////

///

