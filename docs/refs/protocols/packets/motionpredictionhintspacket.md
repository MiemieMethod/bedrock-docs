# <!-- md:samp MotionPredictionHintsPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp MotionPredictionHintsPacket -->数据包，数字ID是`157`。该数据包用于protocol.packet.motionpredictionhintspacket.description

## 结构

```viz
digraph "MotionPredictionHintsPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="MotionPredictionHintsPacket",comment="name: \"MotionPredictionHintsPacket\", typeName: \"\", id: 0, branchId: 157, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="mRuntimeId",comment="name: \"mRuntimeId\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id of moving actor\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="mMotion",comment="name: \"mMotion\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Position delta\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="mOnGround",comment="name: \"mOnGround\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Not falling / jumping\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='MotionPredictionHintsPacket'
[mruntimeid][mmotion][monground]
```

/// html | div.result
//// define
mRuntimeId：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.motionpredictionhintspacket.mruntimeid.descriptionId of moving actor


////
//// define
mMotion：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.motionpredictionhintspacket.mmotion.descriptionPosition delta


////
//// define
mOnGround：<!-- md:samp bool -->

- 基本类型。protocol.packet.motionpredictionhintspacket.monground.descriptionNot falling / jumping


////

///

