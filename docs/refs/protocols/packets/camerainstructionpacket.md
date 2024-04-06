# <!-- md:samp CameraInstructionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraInstructionPacket -->数据包，数字ID是`300`。

## 结构

```viz
digraph "CameraInstructionPacket" {
rankdir = LR
0
0 -> 1
1 -> 15

0 [label="CameraInstructionPacket",comment="name: \"CameraInstructionPacket\", typeName: \"\", id: 0, branchId: 300, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Camera Instruction",comment="name: \"Camera Instruction\", typeName: \"CameraInstruction\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
15 [label="CameraInstruction",comment="name: \"CameraInstruction\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;15}

}

```

## 字段

```title='CameraInstructionPacket'
[camera_instruction]
```

/// html | div.result
//// define
Camera Instruction：[<!-- md:samp CameraInstruction -->](../types/camerainstruction.md)

- <!-- md:samp CameraInstruction -->类型。


////

///

