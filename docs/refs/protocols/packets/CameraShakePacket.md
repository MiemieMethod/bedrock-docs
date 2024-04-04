# <!-- md:samp CameraShakePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraShakePacket -->数据包，数字ID是`159`。

## 结构

```viz
digraph CameraShakePacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"float\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		4	[comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		6	[comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		8	[comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
	}
	0	[comment="name: \"CameraShakePacket\", typeName: \"\", id: 0, branchId: 159, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraShakePacket];
	1	[comment="name: \"Intensity\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Camera shake intensity\"",
		label=Intensity];
	0 -> 1;
	3	[comment="name: \"Seconds\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"Duration\"",
		label=Seconds];
	0 -> 3;
	5	[comment="name: \"Shake Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CameraShakeType\"",
		label="Shake Type"];
	0 -> 5;
	7	[comment="name: \"Shake action\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CameraShakeAction\"",
		label="Shake action"];
	0 -> 7;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
}

```

## 字段

/// define
CameraShakePacket

Intensity：<!-- md:samp float -->

- 类型：float。Camera shake intensity

Seconds：<!-- md:samp float -->

- 类型：float。Duration

Shake Type：<!-- md:samp byte -->

- 类型：byte。enumeration: CameraShakeType

Shake action：<!-- md:samp byte -->

- 类型：byte。enumeration: CameraShakeAction


///
