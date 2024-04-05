# <!-- md:samp CameraInstruction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraInstruction -->类型。

## 结构

```viz
digraph CameraInstruction {
	graph [rankdir=LR];
	{
		graph [rank=max];
		7	[comment="name: \"std::optional<struct CameraInstruction::SetInstruction>\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 512, \
notes: \"\"",
			label="std::optional<struct CameraInstruction::SetInstruction>"];
		9	[comment="name: \"std::optional<bool>\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<bool>"];
		14	[comment="name: \"std::optional<struct CameraInstruction::FadeInstruction>\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: \
512, notes: \"\"",
			label="std::optional<struct CameraInstruction::FadeInstruction>"];
	}
	2	[comment="name: \"CameraInstruction\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraInstruction];
	3	[comment="name: \"Set\", typeName: \"std::optional<struct CameraInstruction::SetInstruction>\", id: 3, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label=Set];
	2 -> 3;
	8	[comment="name: \"Clear\", typeName: \"std::optional<bool>\", id: 8, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Clear];
	2 -> 8;
	10	[comment="name: \"Fade\", typeName: \"std::optional<struct CameraInstruction::FadeInstruction>\", id: 10, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label=Fade];
	2 -> 10;
	3 -> 7;
	8 -> 9;
	10 -> 14;
}

```

## 字段

/// define
CameraInstruction

Set：[<!-- md:samp std::optional<struct CameraInstruction::SetInstruction> -->](refs/protocols/types/std::optional<struct_camerainstruction::setinstruction>.md)

- 类型：std::optional<struct CameraInstruction::SetInstruction>。

Clear：[<!-- md:samp std::optional<bool> -->](refs/protocols/types/std::optional<bool>.md)

- 类型：std::optional<bool>。

Fade：[<!-- md:samp std::optional<struct CameraInstruction::FadeInstruction> -->](refs/protocols/types/std::optional<struct_camerainstruction::fadeinstruction>.md)

- 类型：std::optional<struct CameraInstruction::FadeInstruction>。


///
