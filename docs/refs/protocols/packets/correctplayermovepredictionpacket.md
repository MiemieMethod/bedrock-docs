# <!-- md:samp CorrectPlayerMovePredictionPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CorrectPlayerMovePredictionPacket -->数据包，数字ID是`161`。该数据包用于protocol.packet.correctplayermovepredictionpacket.description

## 结构

```viz
digraph "CorrectPlayerMovePredictionPacket" {
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

0 [label="CorrectPlayerMovePredictionPacket",comment="name: \"CorrectPlayerMovePredictionPacket\", typeName: \"\", id: 0, branchId: 161, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="PredictionType",comment="name: \"PredictionType\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Vehicle or Player Prediction\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Pos",comment="name: \"Pos\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected position\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Pos Delta",comment="name: \"Pos Delta\", typeName: \"Vec3\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected velocity\""];
6 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="On Ground",comment="name: \"On Ground\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Is on ground\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Tick",comment="name: \"Tick\", typeName: \"PlayerInputTick\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"Which frame we're correcting; should match the tick in the Player Auth Input packet\""];
10 [label="PlayerInputTick",comment="name: \"PlayerInputTick\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='CorrectPlayerMovePredictionPacket'
[predictiontype][pos][pos_delta][on_ground][tick]
```

/// html | div.result
//// define
PredictionType：<!-- md:samp byte -->

- 基本类型。protocol.packet.correctplayermovepredictionpacket.predictiontype.descriptionVehicle or Player Prediction


////
//// define
Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.correctplayermovepredictionpacket.pos.descriptionCorrected position


////
//// define
Pos Delta：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.correctplayermovepredictionpacket.pos_delta.descriptionCorrected velocity


////
//// define
On Ground：<!-- md:samp bool -->

- 基本类型。protocol.packet.correctplayermovepredictionpacket.on_ground.descriptionIs on ground


////
//// define
Tick：[<!-- md:samp PlayerInputTick -->](../types/playerinputtick.md)

- 特殊类型。protocol.packet.correctplayermovepredictionpacket.tick.descriptionWhich frame we're correcting; should match the tick in the Player Auth Input packet


////

///

