# <!-- md:samp SpawnExperienceOrbPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SpawnExperienceOrbPacket -->数据包，数字ID是`66`。该数据包用于protocol.packet.spawnexperienceorbpacket.description

## 结构

```viz
digraph "SpawnExperienceOrbPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="SpawnExperienceOrbPacket",comment="name: \"SpawnExperienceOrbPacket\", typeName: \"\", id: 0, branchId: 66, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="XP Value",comment="name: \"XP Value\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='SpawnExperienceOrbPacket'
[position][xp_value]
```

/// html | div.result
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.spawnexperienceorbpacket.position.description


////
//// define
XP Value：<!-- md:samp varint -->

- 基本类型。protocol.packet.spawnexperienceorbpacket.xp_value.description


////

///

