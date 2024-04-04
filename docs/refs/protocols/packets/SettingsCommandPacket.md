# <!-- md:samp SettingsCommandPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SettingsCommandPacket -->数据包，数字ID是`140`。

## 结构

```viz
digraph SettingsCommandPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"bool\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"SettingsCommandPacket\", typeName: \"\", id: 0, branchId: 140, recurseId: -1, attributes: 0, notes: \"\"",
		label=SettingsCommandPacket];
	1	[comment="name: \"Command\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Command to update setting.\"",
		label=Command];
	0 -> 1;
	3	[comment="name: \"Suppress Output?\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Suppress Output?"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
SettingsCommandPacket

Command：<!-- md:samp string -->

- 类型：string。Command to update setting.

Suppress Output?：<!-- md:samp bool -->

- 类型：bool。


///
