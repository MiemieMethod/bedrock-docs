# <!-- md:samp GameTestRequestPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp GameTestRequestPacket -->数据包，数字ID是`194`。该数据包用于protocol.packet.gametestrequestpacket.description

## 结构

```viz
digraph "GameTestRequestPacket" {
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
0 -> 13
13 -> 14

0 [label="GameTestRequestPacket",comment="name: \"GameTestRequestPacket\", typeName: \"\", id: 0, branchId: 194, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="MaxTestsPerBatch",comment="name: \"MaxTestsPerBatch\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="RepeatCount",comment="name: \"RepeatCount\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Rotation",comment="name: \"Rotation\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="StopOnFailure",comment="name: \"StopOnFailure\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="bool",comment="name: \"bool\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="TestPos",comment="name: \"TestPos\", typeName: \"BlockPos\", id: 9, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
10 [label="BlockPos",comment="name: \"BlockPos\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="TestsPerRow",comment="name: \"TestsPerRow\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="varint",comment="name: \"varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="TestName",comment="name: \"TestName\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="string",comment="name: \"string\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14}

}

```

## 字段

```title='GameTestRequestPacket'
[maxtestsperbatch][repeatcount][rotation][stoponfailure][testpos][testsperrow][testname]
```

/// html | div.result
//// define
MaxTestsPerBatch：<!-- md:samp varint -->

- 基本类型。protocol.packet.gametestrequestpacket.maxtestsperbatch.description


////
//// define
RepeatCount：<!-- md:samp varint -->

- 基本类型。protocol.packet.gametestrequestpacket.repeatcount.description


////
//// define
Rotation：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.gametestrequestpacket.rotation.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Rotate90`|`1`|protocol.enum.rotate90|
  |`Rotate180`|`2`|protocol.enum.rotate180|
  |`Rotate270`|`3`|protocol.enum.rotate270|
  |`Clockwise90`|`Rotate90`|protocol.enum.clockwise90|
  |`Clockwise180`|`Rotate180`|protocol.enum.clockwise180|
  |`CounterClockwise90`|`Rotate270`|protocol.enum.counterclockwise90|
  |`Total`|`4`|protocol.enum.total|



////
//// define
StopOnFailure：<!-- md:samp bool -->

- 基本类型。protocol.packet.gametestrequestpacket.stoponfailure.description


////
//// define
TestPos：[<!-- md:samp BlockPos -->](../types/blockpos.md)

- 特殊类型。protocol.packet.gametestrequestpacket.testpos.description


////
//// define
TestsPerRow：<!-- md:samp varint -->

- 基本类型。protocol.packet.gametestrequestpacket.testsperrow.description


////
//// define
TestName：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.gametestrequestpacket.testname.description


////

///

