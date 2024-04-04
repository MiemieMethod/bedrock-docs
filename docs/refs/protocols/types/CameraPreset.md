# <!-- md:samp CameraPreset -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraPreset -->类型。

## 结构

```dot
digraph CameraPreset {
	graph [rankdir=LR];
	{
		graph [rank=max];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"string\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		17	[comment="name: \"std::optional<float>\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<float>"];
		19	[comment="name: \"std::optional<float>\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<float>"];
		21	[comment="name: \"std::optional<float>\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<float>"];
		23	[comment="name: \"std::optional<float>\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<float>"];
		25	[comment="name: \"std::optional<float>\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<float>"];
		30	[comment="name: \"std::optional<enum CameraPreset::AudioListener>\", typeName: \"\", id: 30, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<enum CameraPreset::AudioListener>"];
		35	[comment="name: \"std::optional<bool>\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="std::optional<bool>"];
	}
	8	[comment="name: \"CameraPreset\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraPreset];
	9	[comment="name: \"Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Name];
	8 -> 9;
	11	[comment="name: \"Inherit From\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Inherit From"];
	8 -> 11;
	13	[comment="name: \"Pos X\", typeName: \"std::optional<float>\", id: 13, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Pos X"];
	8 -> 13;
	18	[comment="name: \"Pos Y\", typeName: \"std::optional<float>\", id: 18, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Pos Y"];
	8 -> 18;
	20	[comment="name: \"Pos Z\", typeName: \"std::optional<float>\", id: 20, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Pos Z"];
	8 -> 20;
	22	[comment="name: \"Rot X\", typeName: \"std::optional<float>\", id: 22, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Rot X"];
	8 -> 22;
	24	[comment="name: \"Rot Y\", typeName: \"std::optional<float>\", id: 24, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Rot Y"];
	8 -> 24;
	26	[comment="name: \"Listener\", typeName: \"std::optional<enum CameraPreset::AudioListener>\", id: 26, branchId: 0, recurseId: -1, attributes: 256, \
notes: \"\"",
		label=Listener];
	8 -> 26;
	31	[comment="name: \"Player Effects\", typeName: \"std::optional<bool>\", id: 31, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Effects"];
	8 -> 31;
	9 -> 10;
	11 -> 12;
	13 -> 17;
	18 -> 19;
	20 -> 21;
	22 -> 23;
	24 -> 25;
	26 -> 30;
	31 -> 35;
}

```

## 字段

/// define
CameraPreset

Name：<!-- md:samp string -->

- 类型：string。

Inherit From：<!-- md:samp string -->

- 类型：string。

Pos X：[<!-- md:samp std::optional<float> -->](refs/protocols/types/std::optional<float>.md)

- 类型：std::optional<float>。

Pos Y：[<!-- md:samp std::optional<float> -->](refs/protocols/types/std::optional<float>.md)

- 类型：std::optional<float>。

Pos Z：[<!-- md:samp std::optional<float> -->](refs/protocols/types/std::optional<float>.md)

- 类型：std::optional<float>。

Rot X：[<!-- md:samp std::optional<float> -->](refs/protocols/types/std::optional<float>.md)

- 类型：std::optional<float>。

Rot Y：[<!-- md:samp std::optional<float> -->](refs/protocols/types/std::optional<float>.md)

- 类型：std::optional<float>。

Listener：[<!-- md:samp std::optional<enum CameraPreset::AudioListener> -->](refs/protocols/types/std::optional<enum CameraPreset::AudioListener>.md)

- 类型：std::optional<enum CameraPreset::AudioListener>。

Player Effects：[<!-- md:samp std::optional<bool> -->](refs/protocols/types/std::optional<bool>.md)

- 类型：std::optional<bool>。


///
