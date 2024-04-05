# <!-- md:samp CameraPresetsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraPresetsPacket -->数据包，数字ID是`198`。

## 结构

```viz
digraph CameraPresetsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		37	[comment="name: \"CameraPresets\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CameraPresets];
	}
	0	[comment="name: \"CameraPresetsPacket\", typeName: \"\", id: 0, branchId: 198, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraPresetsPacket];
	1	[comment="name: \"Camera Presets\", typeName: \"CameraPresets\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Camera Presets"];
	0 -> 1;
	1 -> 37;
}

```

## 字段

/// define
CameraPresetsPacket

Camera Presets：[<!-- md:samp CameraPresets -->](refs/protocols/types/camerapresets.md)

- 类型：CameraPresets。


///
