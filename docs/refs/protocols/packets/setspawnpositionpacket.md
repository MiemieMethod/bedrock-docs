# <!-- md:samp SetSpawnPositionPacket -->

> 文档版本：r/20_u8<br/>协议版本：671

<!-- md:samp SetSpawnPositionPacket -->数据包，数字ID是`43`。该数据包用于protocol.packet.setspawnpositionpacket.description

## 结构

```viz
digraph "SetSpawnPositionPacket" {
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

0 [label="SetSpawnPositionPacket",comment="name: \"SetSpawnPositionPacket\", typeName: \"\", id: 0, branchId: 43, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Spawn Position Type",comment="name: \"Spawn Position Type\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Block Position",comment="name: \"Block Position\", typeName: \"NetworkBlockPosition\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Dimension type",comment="name: \"Dimension type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Spawn Block Pos",comment="name: \"Spawn Block Pos\", typeName: \"NetworkBlockPosition\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
8 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='SetSpawnPositionPacket'
[spawn_position_type][block_position][dimension_type][spawn_block_pos]
```

/// html | div.result
//// define
Spawn Position Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.setspawnpositionpacket.spawn_position_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`PlayerRespawn`|`0`|protocol.enum.playerrespawn|
  |`WorldSpawn`|`1`|protocol.enum.worldspawn|



////
//// define
Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.setspawnpositionpacket.block_position.description


////
//// define
Dimension type：<!-- md:samp varint -->

- 基本类型。protocol.packet.setspawnpositionpacket.dimension_type.description


////
//// define
Spawn Block Pos：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.packet.setspawnpositionpacket.spawn_block_pos.description


////

///

