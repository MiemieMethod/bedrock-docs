# <!-- md:samp EducationSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp EducationSettingsPacket -->数据包，数字ID是`137`。

## 结构

```viz
digraph EducationSettingsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		32	[comment="name: \"EducationLevelSettings\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=EducationLevelSettings];
	}
	0	[comment="name: \"EducationSettingsPacket\", typeName: \"\", id: 0, branchId: 137, recurseId: -1, attributes: 0, notes: \"\"",
		label=EducationSettingsPacket];
	1	[comment="name: \"Education Level Settings\", typeName: \"EducationLevelSettings\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Education Level Settings"];
	0 -> 1;
	1 -> 32;
}

```

## 字段

/// define
EducationSettingsPacket

Education Level Settings：[<!-- md:samp EducationLevelSettings -->](refs/protocols/types/educationlevelsettings.md)

- 类型：EducationLevelSettings。


///
