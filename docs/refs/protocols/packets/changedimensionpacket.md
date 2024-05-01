# <!-- md:samp ChangeDimensionPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp ChangeDimensionPacket -->数据包，数字ID是`61`。该数据包用于protocol.packet.changedimensionpacket.description

## 结构

```viz
digraph "ChangeDimensionPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ChangeDimensionPacket",comment="name: \"ChangeDimensionPacket\", typeName: \"\", id: 0, branchId: 61, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Dimension ID",comment="name: \"Dimension ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Currently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Respawn",comment="name: \"Respawn\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ChangeDimensionPacket'
[dimension_id][position][respawn]
```

/// html | div.result
//// define
Dimension ID：<!-- md:samp varint -->

- 基本类型。protocol.packet.changedimensionpacket.dimension_id.descriptionCurrently supported: (0 -> Overworld, 1 -> Nether, 2 -> The End, 3 -> Undefined)


////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.changedimensionpacket.position.description


////
//// define
Respawn：<!-- md:samp bool -->

- 基本类型。protocol.packet.changedimensionpacket.respawn.description


////

///

