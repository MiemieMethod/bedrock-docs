# <!-- md:samp CorrectPlayerMovePredictionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CorrectPlayerMovePredictionPacket -->数据包，数字ID是`161`。

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
1 [label="Pos",comment="name: \"Pos\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected position\""];
2 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Pos Delta",comment="name: \"Pos Delta\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Corrected velocity\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="On Ground",comment="name: \"On Ground\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Is on ground\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Tick",comment="name: \"Tick\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which frame we're correcting; should match the tick in the Player Auth Input packet\""];
8 [label="unsigned varint64",comment="name: \"unsigned varint64\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="PredictionType",comment="name: \"PredictionType\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"Vehicle or Player Prediction\""];
10 [label="byte",comment="name: \"byte\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='CorrectPlayerMovePredictionPacket'
[pos][pos_delta][on_ground][tick][predictiontype]
```

/// html | div.result
//// define
Pos：[<!-- md:samp Vec3 -->](../types/vec3.md)

- <!-- md:samp Vec3 -->类型。Corrected position


////
//// define
Pos Delta：[<!-- md:samp Vec3 -->](../types/vec3.md)

- <!-- md:samp Vec3 -->类型。Corrected velocity


////
//// define
On Ground：<!-- md:samp bool -->

- <!-- md:samp bool -->类型。Is on ground


////
//// define
Tick：<!-- md:samp unsigned varint64 -->

- <!-- md:samp unsigned varint64 -->类型。Which frame we're correcting; should match the tick in the Player Auth Input packet


////
//// define
PredictionType：<!-- md:samp byte -->

- <!-- md:samp byte -->类型。Vehicle or Player Prediction


////

///

