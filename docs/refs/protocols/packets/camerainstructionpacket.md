# <!-- md:samp CameraInstructionPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp CameraInstructionPacket -->数据包，数字ID是`300`。该数据包用于protocol.packet.camerainstructionpacket.description

## 结构

```viz
digraph "CameraInstructionPacket" {
rankdir = LR
0
0 -> 1
1 -> 22

0 [label="CameraInstructionPacket",comment="name: \"CameraInstructionPacket\", typeName: \"\", id: 0, branchId: 300, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Camera Instruction",comment="name: \"Camera Instruction\", typeName: \"CameraInstruction\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
22 [label="CameraInstruction",comment="name: \"CameraInstruction\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;22}

}

```

## 字段

```title='CameraInstructionPacket'
[camera_instruction]
```

/// html | div.result
//// define
Camera Instruction：[<!-- md:samp CameraInstruction -->](../types/camerainstruction.md)

- 特殊类型。protocol.packet.camerainstructionpacket.camera_instruction.description


////

///

