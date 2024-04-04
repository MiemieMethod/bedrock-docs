# <!-- md:samp std::optional<enum CameraPreset::AudioListener> -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp std::optional<enum CameraPreset::AudioListener> -->类型。

## 结构

```dot
digraph "std::optional<enum CameraPreset::AudioListener>" {
	graph [rankdir=LR];
	{
		graph [rank=max];
		29	[comment="name: \"bool\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	27	[comment="name: \"std::optional<enum CameraPreset::AudioListener>\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="std::optional<enum CameraPreset::AudioListener>"];
	28	[comment="name: \"Has Value\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 0, notes: \"If true, follow with appropriate data \
type, otherwise nothing\"",
		label="Has Value"];
	27 -> 28;
	28 -> 29;
}

```

## 字段

/// define
std::optional<enum CameraPreset::AudioListener>

Has Value：<!-- md:samp bool -->

- 类型：bool。If true, follow with appropriate data type, otherwise nothing


///
