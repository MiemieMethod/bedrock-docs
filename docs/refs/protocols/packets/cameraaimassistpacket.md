# <!-- md:samp CameraAimAssistPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp CameraAimAssistPacket -->数据包，数字ID是`316`。该数据包用于protocol.packet.cameraaimassistpacket.description

## 结构

```viz
digraph "CameraAimAssistPacket" {
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

0 [label="CameraAimAssistPacket",comment="name: \"CameraAimAssistPacket\", typeName: \"\", id: 0, branchId: 316, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="View Angle",comment="name: \"View Angle\", typeName: \"Vec2\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="Vec2",comment="name: \"Vec2\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Distance",comment="name: \"Distance\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="float",comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Target Mode",comment="name: \"Target Mode\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Action",comment="name: \"Action\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='CameraAimAssistPacket'
[view_angle][distance][target_mode][action]
```

/// html | div.result
//// define
View Angle：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 特殊类型。protocol.packet.cameraaimassistpacket.view_angle.description


////
//// define
Distance：<!-- md:samp float -->

- 基本类型。protocol.packet.cameraaimassistpacket.distance.description


////
//// define
Target Mode：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.cameraaimassistpacket.target_mode.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Angle`|`0`|protocol.enum.angle|
  |`Distance`|`1`|protocol.enum.distance|



////
//// define
Action：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.cameraaimassistpacket.action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Set`|`0`|protocol.enum.set|
  |`Clear`|`1`|protocol.enum.clear|



////

///

