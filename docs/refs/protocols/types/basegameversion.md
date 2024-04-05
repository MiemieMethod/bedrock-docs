# <!-- md:samp BaseGameVersion -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BaseGameVersion -->类型。

## 结构

```viz
digraph BaseGameVersion {
	graph [rankdir=LR];
	{
		graph [rank=max];
		26	[comment="name: \"string\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
	}
	24	[comment="name: \"BaseGameVersion\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=BaseGameVersion];
	25	[comment="name: \"Base Game Version\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 0, notes: \"Format: 0.0.0 (i.e. Major.Minor.Patch)\"",
		label="Base Game Version"];
	24 -> 25;
	25 -> 26;
}

```

## 字段

/// define
BaseGameVersion

Base Game Version：<!-- md:samp string -->

- 类型：string。Format: 0.0.0 (i.e. Major.Minor.Patch)


///
