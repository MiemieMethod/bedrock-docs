# <!-- md:samp CameraInstructionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraInstructionPacket -->数据包，数字ID是`300`。

## 结构

```viz
digraph CameraInstructionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		15	[comment="name: \"CameraInstruction\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CameraInstruction];
	}
	0	[comment="name: \"CameraInstructionPacket\", typeName: \"\", id: 0, branchId: 300, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraInstructionPacket];
	1	[comment="name: \"Camera Instruction\", typeName: \"CameraInstruction\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Camera Instruction"];
	0 -> 1;
	1 -> 15;
}

```

## 字段

/// define
CameraInstructionPacket

Camera Instruction：[<!-- md:samp CameraInstruction -->](refs/protocols/types/camerainstruction.md)

- 类型：CameraInstruction。


///
